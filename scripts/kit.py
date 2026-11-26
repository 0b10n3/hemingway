"""Kit de distribuição da esteira v2 (skill /distribuir). Regras e números: config/esteira.yaml.

  python3 scripts/kit.py montar <slug> [AAAA-MM-DD] [--substituir]
        escreve distribuicao/kit.json (peças e datas) e o esqueleto de distribuicao/textos.md.
        Sem data: o próximo dia de publicação da linha, a partir de hoje.
  python3 scripts/kit.py validar <slug>    confere kit.json e textos.md; escreve kit.md (mini-gate)
  python3 scripts/kit.py url <slug>        troca {{URL_POST}} pela url_publicada do post.md e revalida
  python3 scripts/kit.py guarda            hook PreToolUse: o subagent só escreve textos.md, video/roteiro.md e video/storyboard.json
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

import jsonschema
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_catalogo import RAIZ, ler_post  # noqa: E402
from parecer import EMOJI, NUMERO, _catalogo, termina_em_pergunta  # noqa: E402

CONFIG = RAIZ / "config/esteira.yaml"
ESQUEMA = RAIZ / ".claude/skills/distribuicao/referencias/kit.schema.json"
DIAS = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
CURTO = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
MARCADOR = "{{URL_POST}}"
URL_ESTIMADA = 80  # ponytail: {{URL_POST}} conta como 80 caracteres (URL de post do Substack tem ~60)
URL = re.compile(r"https?://[^\s)>\]]+|\{\{URL_POST\}\}")
BLOCO = re.compile(r"^## ([A-Z]\d+) · ([a-z0-9-]+) · ([a-z0-9-]+)[ \t]*$", re.M)
HASHTAG = re.compile(r"(?<![\w&/])#\w+")
PREFIXO = {"note": "N", "post-linkedin": "P", "video": "L", "carrossel": "L"}


def ler_config():
    return yaml.safe_load(CONFIG.read_text(encoding="utf-8"))


def _pasta(slug):
    p = Path(slug)
    return p if p.is_dir() else RAIZ / "posts" / slug


def proximo_dia(cfg, linha, hoje):
    alvo = DIAS.index(cfg["linhas"][linha]["dia_publicacao"])
    return hoje + dt.timedelta((alvo - hoje.weekday()) % 7)


def _dia(iso):
    d = dt.date.fromisoformat(iso)
    return f"{CURTO[d.weekday()]} {d:%d/%m}"


def precisa_link(peca, cfg):
    """True: leva {{URL_POST}}; False: não pode ter URL; None: livre."""
    if peca["tipo"] == "post-linkedin":
        return cfg["linkedin"]["link_no_post"]
    return peca.get("link")


def montar_kit(cfg, slug, fm, data_pub, url=None):
    rotulo = fm.get("linha_editorial")
    linha = next((k for k, v in cfg["linhas"].items() if v["rotulo"] == rotulo), None)
    if linha is None:
        raise SystemExit(f"{slug}: linha_editorial {rotulo!r} não está em config/esteira.yaml")
    pecas = []
    for p in cfg["pecas"][linha]:
        t = cfg["tipos"][p["tipo"]]
        if p["tipo"] in ("video", "carrossel"):
            situacao = "aguarda-producao"
        else:
            situacao = "aguarda-url" if precisa_link(p, cfg) and not url else "pronto"
        pecas.append({"id": p["id"], "tipo": p["tipo"], "canais": p["canais"], "offset_dias": p["offset_dias"],
                      "data": (data_pub + dt.timedelta(p["offset_dias"])).isoformat(),
                      "arquivos": t["arquivos"], "producao_manual": t["producao_manual"],
                      "apetite_min": p["apetite_min"], "situacao": situacao, "retorno": cfg["retorno"]["texto"]})
    return {"versao_esquema": "1.0",
            "post": {"slug": slug, "linha": linha, "titulo": fm.get("titulo") or fm.get("título") or slug,
                     "data_publicacao": data_pub.isoformat(), "url": url},
            "pecas": pecas}


def esqueleto(kit, cfg):
    """Cabeçalhos de textos.md, um por texto, com o ID: o redator só preenche o corpo."""
    pecas = sorted(kit["pecas"], key=lambda p: (p["data"], kit["pecas"].index(p)))
    cont, linhas = {}, [f"# Textos de distribuição: {kit['post']['titulo']}", ""]
    for p in pecas:
        for canal in cfg["tipos"][p["tipo"]]["textos"]:
            pre = PREFIXO[p["tipo"]]
            cont[pre] = cont.get(pre, 0) + 1
            linhas += [f"## {pre}{cont[pre]} · {p['id']} · {canal}", "", ""]
    return "\n".join(linhas)


def ler_textos(md):
    """[(id, peça, canal, texto)] a partir dos blocos '## N1 · note-d0 · substack-notes'."""
    partes = BLOCO.split(md)
    return [(partes[i], partes[i + 1], partes[i + 2], partes[i + 3].strip()) for i in range(1, len(partes), 4)]


def _canon(n):
    """'1.000' == '1000', '11,85' == '11.85', '1,50' == '1,5'."""
    if "," in n:
        n = n.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", n):
        n = n.replace(".", "")
    return n.rstrip("0").rstrip(".") if "." in n else n


def numeros(texto):
    return {_canon(n) for n in NUMERO.findall(URL.sub(" ", texto))}


def checar(kit, md, cfg, fontes, catalogo, url_post=None):
    """Lista de erros (vazia = kit válido). fontes = numeros() do post + FEAR.md + GREED.md."""
    try:
        jsonschema.validate(kit, json.loads(ESQUEMA.read_text(encoding="utf-8")))
    except jsonschema.ValidationError as e:
        return [f"kit.json fora do esquema 1.0: {'/'.join(map(str, e.absolute_path)) or '(raiz)'}: {e.message}"]
    erros = []
    linha = kit["post"]["linha"]
    pub = dt.date.fromisoformat(kit["post"]["data_publicacao"])
    dia = cfg["linhas"][linha]["dia_publicacao"]
    if DIAS[pub.weekday()] != dia:
        erros.append(f"data_publicacao {pub} cai numa {DIAS[pub.weekday()]}; {linha} publica na {dia}")

    previstas = {p["id"]: p for p in cfg["pecas"][linha]}
    ids = [p["id"] for p in kit["pecas"]]
    erros += [f"falta a peça {i}, prevista em config/esteira.yaml" for i in previstas if i not in ids]
    erros += [f"peça {i} não está prevista para {linha}" for i in ids if i not in previstas]
    for p in kit["pecas"]:
        d = dt.date.fromisoformat(p["data"])
        esperada = pub + dt.timedelta(p["offset_dias"])
        if p["id"] in previstas and p["offset_dias"] != previstas[p["id"]]["offset_dias"]:
            erros.append(f"{p['id']}: offset {p['offset_dias']}, o config diz {previstas[p['id']]['offset_dias']}")
        if d < esperada:  # adiar pode (peça remarcada pelo autor); antecipar, não
            erros.append(f"{p['id']}: data {d} antes de data_publicacao + {p['offset_dias']} ({esperada})")
        if DIAS[d.weekday()] in cfg["dias_sem_publicacao"]:
            erros.append(f"{p['id']}: cai num {DIAS[d.weekday()]}, dia sem publicação")

    url_ok = {MARCADOR, cfg["assinatura"]["url_inscricao"], url_post}
    indisponiveis = [(oid, t) for oid, i in catalogo.items() if i["tipo"] != "post" and not i["citavel"]
                     for t in [i["titulo"], *i.get("termos", [])] if t]
    vistos = {}
    for id_, peca, canal, texto in ler_textos(md):
        p = previstas.get(peca)
        slots = cfg["tipos"][p["tipo"]]["textos"] if p else {}
        if canal not in slots:
            erros.append(f"{id_}: {peca} · {canal} não está previsto (config/esteira.yaml, tipos)")
            continue
        if (peca, canal) in vistos:
            erros.append(f"{id_}: repete {peca} · {canal}, já escrito em {vistos[(peca, canal)]}")
            continue
        vistos[(peca, canal)] = id_
        if not texto:
            erros.append(f"{id_}: texto vazio")
            continue
        chave = slots[canal]
        n = len(texto.replace(MARCADOR, "x" * URL_ESTIMADA))
        if n > cfg["limites_caracteres"][chave]["max"]:
            erros.append(f"{id_}: {n} caracteres, limite {cfg['limites_caracteres'][chave]['max']} ({chave})")
        if canal not in cfg["regras"]["pergunta_final_exceto"] and not termina_em_pergunta(texto):
            erros.append(f"{id_}: não termina com uma pergunta (o link pode vir depois, sozinho na última linha)")
        if EMOJI.search(texto):
            erros.append(f"{id_}: contém emoji")
        h, hmax = len(HASHTAG.findall(texto)), cfg["regras"]["hashtags_max"].get(canal, 0)
        if h > hmax:
            erros.append(f"{id_}: {h} hashtag(s), máximo {hmax} em {canal}")
        urls = URL.findall(texto)
        link = precisa_link(p, cfg)
        if link and not urls:
            erros.append(f"{id_}: falta {MARCADOR}")
        if urls and (link is False or canal.startswith("instagram")):
            erros.append(f"{id_}: não pode ter URL ({'Instagram: ' + cfg['instagram']['link'] if canal.startswith('instagram') else 'Note sem link'})")
        erros += [f"{id_}: URL fora da esteira: {u}" for u in urls if u not in url_ok]
        erros += [f"{id_}: número {x!r} não está no post nem em FEAR.md ou GREED.md" for x in sorted(numeros(texto) - fontes)]
        erros += [f"{id_}: menciona {t!r} ({oid}), que não está disponível no catálogo" for oid, t in indisponiveis
                  if re.search(rf"(?<!\w){re.escape(t)}(?!\w)", texto, re.I)]
    for p in kit["pecas"]:
        for canal in cfg["tipos"][p["tipo"]]["textos"] if p["id"] in previstas else []:
            if (p["id"], canal) not in vistos:
                erros.append(f"falta o texto de {p['id']} · {canal}")
    return erros


def renderizar(kit, md, cfg, erros):
    post = kit["post"]
    L = [f"# Kit de distribuição: {post['titulo']}", "",
         f"{cfg['linhas'][post['linha']]['rotulo']} · publicação no Substack: {_dia(post['data_publicacao'])}/"
         f"{post['data_publicacao'][:4]} · URL: {post['url'] or 'ainda sem URL (' + MARCADOR + ' nos textos)'}", ""]
    if erros:
        L += ["**KIT INVÁLIDO.** O validador (`scripts/kit.py validar`) reprovou os itens abaixo.", ""]
        L += [f"- {e}" for e in erros] + [""]
    else:
        L += ["Kit válido (`scripts/kit.py validar`). Responda no mini-gate: `aceito`, ou os IDs a ajustar "
              "(`N1: gancho mais curto; L2: …`).", ""]
    textos = ler_textos(md)
    por_peca = {}
    for id_, peca, canal, _ in textos:
        por_peca.setdefault(peca, []).append(id_)
    dias = {p["data"] for p in kit["pecas"]}
    L += ["## Calendário", "", "| Data | Peça | IDs | Canais | Situação | Apetite | À mão |", "|---|---|---|---|---|---|---|"]
    for p in sorted(kit["pecas"], key=lambda p: p["data"]):
        L.append(f"| {_dia(p['data'])} | {p['id']} | {', '.join(por_peca.get(p['id'], [])) or '—'} | "
                 f"{', '.join(p['canais'])} | {p['situacao']} | {p['apetite_min']} min | {'; '.join(p['producao_manual'])} |")
    total = sum(p["apetite_min"] for p in kit["pecas"])
    L += ["", f"Apetite do kit: {total} min de peças + {len(dias)} dias × {cfg['retorno']['janela_min']} min "
              f"de resposta = {total + len(dias) * cfg['retorno']['janela_min']} min.", "", "## Textos", ""]
    datas = {p["id"]: p["data"] for p in kit["pecas"]}
    for id_, peca, canal, texto in textos:
        p = next((x for x in cfg["pecas"][post["linha"]] if x["id"] == peca), None)
        chave = cfg["tipos"][p["tipo"]]["textos"].get(canal) if p else None
        lim = f"/{cfg['limites_caracteres'][chave]['max']}" if chave else ""
        n = len(texto.replace(MARCADOR, "x" * URL_ESTIMADA))
        L += [f"### {id_} · {peca} · {canal} · {_dia(datas[peca]) if peca in datas else '?'} ({n}{lim} caracteres)",
              "", "```text", texto, "```", ""]
    return "\n".join(L)


def _fontes(pasta, cfg):
    texto = (pasta / "post.md").read_text(encoding="utf-8")
    for f in cfg["regras"]["fontes_numero"]:
        if (RAIZ / f).exists():
            texto += "\n" + (RAIZ / f).read_text(encoding="utf-8")
    return numeros(texto)


def montar(slug, data=None, substituir=False):
    pasta, cfg = _pasta(slug), ler_config()
    dist = pasta / "distribuicao"
    if (dist / "kit.json").exists() and not substituir:
        sys.exit(f"{dist / 'kit.json'} já existe; use --substituir para refazer as datas")
    fm, _, _ = ler_post(pasta / "post.md")
    linha = next((k for k, v in cfg["linhas"].items() if v["rotulo"] == fm.get("linha_editorial")), None)
    if linha is None:
        sys.exit(f"{pasta.name}: linha_editorial {fm.get('linha_editorial')!r} não está em config/esteira.yaml")
    pub = dt.date.fromisoformat(data) if data else proximo_dia(cfg, linha, dt.date.today())
    kit = montar_kit(cfg, pasta.name, fm, pub, fm.get("url_publicada") or None)
    dist.mkdir(exist_ok=True)
    (dist / "kit.json").write_text(json.dumps(kit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if not (dist / "textos.md").exists():
        (dist / "textos.md").write_text(esqueleto(kit, cfg), encoding="utf-8")
    print(f"{dist / 'kit.json'}: {linha}, publicação em {_dia(pub.isoformat())}/{pub.year}, {len(kit['pecas'])} peças")
    if DIAS[pub.weekday()] != cfg["linhas"][linha]["dia_publicacao"]:
        print(f"atenção: {pub} não é {cfg['linhas'][linha]['dia_publicacao']}; o validador vai reprovar", file=sys.stderr)
    return 0


def validar(slug):
    pasta, cfg = _pasta(slug), ler_config()
    dist = pasta / "distribuicao"
    try:
        kit = json.loads((dist / "kit.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        sys.exit(f"kit.json ilegível: {e}. Rode antes: python3 scripts/kit.py montar {pasta.name}")
    md = (dist / "textos.md").read_text(encoding="utf-8") if (dist / "textos.md").exists() else ""
    erros = checar(kit, md, cfg, _fontes(pasta, cfg), _catalogo(), kit["post"]["url"])
    (dist / "kit.md").write_text(renderizar(kit, md, cfg, erros), encoding="utf-8")
    print("\n".join(erros) if erros else "kit válido", file=sys.stderr if erros else sys.stdout)
    return 1 if erros else 0


def url(slug):
    pasta = _pasta(slug)
    fm, _, _ = ler_post(pasta / "post.md")
    u = fm.get("url_publicada")
    if not u:
        sys.exit(f"{pasta.name}: post.md ainda não tem url_publicada (o /forja-de-voz colher propõe a linha)")
    dist = pasta / "distribuicao"
    n = 0
    for f in sorted(dist.rglob("*.md")):
        t = f.read_text(encoding="utf-8")
        if MARCADOR in t:
            n += t.count(MARCADOR)
            f.write_text(t.replace(MARCADOR, u), encoding="utf-8")
    kit = json.loads((dist / "kit.json").read_text(encoding="utf-8"))
    kit["post"]["url"] = u
    for p in kit["pecas"]:
        if p["situacao"] == "aguarda-url":
            p["situacao"] = "pronto"
    (dist / "kit.json").write_text(json.dumps(kit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{n} marcador(es) {MARCADOR} trocados por {u}")
    return validar(slug)


def guarda():
    caminho = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
    if re.search(r"(^|/)posts/[^/]+/distribuicao/(textos\.md|video/roteiro\.md|video/storyboard\.json)$", caminho):
        return 0
    print(f"os subagents da distribuição só escrevem distribuicao/textos.md, video/roteiro.md e "
          f"video/storyboard.json, não {caminho} (kit.json, kit.md e storyboard.md são dos scripts)", file=sys.stderr)
    return 2


if __name__ == "__main__":
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ("", [])
    sub = "--substituir" in args
    args = [a for a in args if a != "--substituir"]
    if cmd == "montar" and 1 <= len(args) <= 2:
        sys.exit(montar(*args, substituir=sub))
    if cmd == "validar" and len(args) == 1:
        sys.exit(validar(args[0]))
    if cmd == "url" and len(args) == 1:
        sys.exit(url(args[0]))
    if cmd == "guarda":
        sys.exit(guarda())
    sys.exit(__doc__)
