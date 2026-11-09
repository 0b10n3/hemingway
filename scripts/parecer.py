"""Checagens e aplicação do parecer de marketing (etapa 9a do /post-substack).

  python3 scripts/parecer.py validar <slug>            valida marketing.json e escreve marketing.md
  python3 scripts/parecer.py aplicar <slug> C1 R2 'R1=novo texto'
                                                       aplica só os itens aceitos no gate
  python3 scripts/parecer.py guarda                    hook PreToolUse do subagent: só deixa
                                                       escrever posts/<slug>/marketing.json
"""
import json
import re
import sys
from pathlib import Path

import jsonschema

sys.path.insert(0, str(Path(__file__).resolve().parent))
from gerar_catalogo import MKT, RAIZ, ler_post  # noqa: E402

ESQUEMA = RAIZ / ".claude/skills/estrategia-marketing/referencias/esquema.json"
ESTRATEGIA = RAIZ.parent.parent / "strategy"
FONTES_NUMERO = ["FEAR.md", "GREED.md", "PRICE_TAG.md"]
LIMITES = {"principal": 1, "secundario": 2, "referencias": 4}
FIM_DO_CORPO = re.compile(r"^## (Para continuar aprendendo|Para ir além|Referências)", re.M)
LINK_GENERICO = ["clique aqui", "leia mais", "saiba mais", "este link", "neste link"]
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️‍]")
NUMERO = re.compile(r"\d+(?:[.,]\d+)*")


def _pasta(slug):
    p = Path(slug)
    return p if p.is_dir() else RAIZ / "posts" / slug


def _catalogo():
    return {i["id"]: i for i in json.loads((MKT / "catalogo.json").read_text(encoding="utf-8"))["itens"]}


def _corpo_principal(corpo):
    m = FIM_DO_CORPO.search(corpo)
    return corpo[:m.start()] if m else corpo


def _generico(texto):
    t = re.sub(r"[^\w\s]", "", texto.lower()).strip()
    return t == "aqui" or any(re.search(rf"\b{g}\b", t) for g in LINK_GENERICO)


def _textos(parecer):
    """Todo texto que o autor pode colar no post: (id, campo, valor)."""
    for c in parecer.get("ctas", []):
        for k in ("texto_sugerido", "texto_link"):
            if c.get(k):
                yield c["id"], k, c[k]
    for r in parecer.get("referencias", []):
        for k in ("texto_link", "frase_nova"):
            if r.get(k):
                yield r["id"], k, r[k]
    for b in parecer.get("backlinks_sugeridos", []):
        yield b["id"], "texto_link", b["texto_link"]


def checar(parecer, corpo, catalogo, slug, fontes_numero=""):
    """Devolve a lista de erros (vazia = válido)."""
    try:
        jsonschema.validate(parecer, json.loads(ESQUEMA.read_text(encoding="utf-8")))
    except jsonschema.ValidationError as e:
        caminho = "/".join(str(p) for p in e.absolute_path)
        return [f"esquema: {caminho or '(raiz)'}: {e.message}"]

    erros = []
    principal = _corpo_principal(corpo)
    n = len(principal)

    def unica(id_, trecho):
        k = corpo.count(trecho)
        if k != 1:
            erros.append(f"{id_}: âncora aparece {k} vez(es) no post, deve aparecer 1: {trecho[:60]!r}")
            return None
        return corpo.find(trecho)

    def citavel(id_, destino):
        item = catalogo.get(destino)
        if item is None:
            erros.append(f"{id_}: destino {destino!r} não existe no catálogo")
        elif not item["citavel"]:
            erros.append(f"{id_}: destino {destino!r} não é citável (situação {item['situacao']!r}, url {item['url']!r})")
        elif destino == f"post:{slug}":
            erros.append(f"{id_}: o post não pode apontar para si mesmo")
        return item

    d = parecer["diagnostico"]
    for j in d["justificativas"]:
        if j["trecho"] not in corpo:
            erros.append(f"diagnóstico ({j['escolha'][:30]}): trecho não aparece no post: {j['trecho'][:60]!r}")
    for a in parecer["alinhamento"]:
        if a.get("trecho") and a["trecho"] not in corpo:
            erros.append(f"{a['id']}: trecho não aparece no post: {a['trecho'][:60]!r}")
    for x in parecer["riscos"]:
        if x.get("trecho") and x["trecho"] not in corpo:
            erros.append(f"{x['id']}: trecho não aparece no post: {x['trecho'][:60]!r}")

    inscricao_inicio = inscricao_fim = False
    papeis = {"principal": 0, "secundario": 0}
    for c in parecer["ctas"]:
        pos = unica(c["id"], c["ancora"])
        item = citavel(c["id"], c["destino_id"])
        if c["papel"] in papeis:
            papeis[c["papel"]] += 1
        if c["formato"] == "botao_nativo" and item and item["tipo"] != "nativo":
            erros.append(f"{c['id']}: botão nativo só aponta para destino substack:*")
        if c["formato"] == "texto" and item and item["url"]:
            tl = c.get("texto_link")
            if not tl or tl not in c["texto_sugerido"]:
                erros.append(f"{c['id']}: destino com URL pede texto_link contido em texto_sugerido")
            elif _generico(tl):
                erros.append(f"{c['id']}: texto de link genérico: {tl!r}")
        if c["papel"] == "inscricao" and pos is not None:
            fim_paragrafo = pos + len(c["ancora"])
            inscricao_inicio |= fim_paragrafo <= n * 0.25
            inscricao_fim |= pos >= n * 0.75
    for papel, k in papeis.items():
        if k > LIMITES[papel]:
            erros.append(f"CTAs: {k} com papel {papel}, máximo {LIMITES[papel]}")
    if not inscricao_inicio:
        erros.append("CTAs: falta botão de inscrição no primeiro quarto do post")
    if not inscricao_fim:
        erros.append("CTAs: falta botão de inscrição no fim do post (último quarto)")

    if len(parecer["referencias"]) > LIMITES["referencias"]:
        erros.append(f"referências: {len(parecer['referencias'])}, máximo {LIMITES['referencias']}")
    for r in parecer["referencias"]:
        unica(r["id"], r["ancora"])
        citavel(r["id"], r["destino_id"])
        base = r.get("frase_nova") or r["ancora"]
        if r["texto_link"] not in base:
            erros.append(f"{r['id']}: texto_link precisa estar dentro de {'frase_nova' if r.get('frase_nova') else 'ancora'}")
        if _generico(r["texto_link"]):
            erros.append(f"{r['id']}: texto de link genérico: {r['texto_link']!r}")

    for b in parecer["backlinks_sugeridos"]:
        item = catalogo.get(b["origem_id"])
        if item is None or item["tipo"] != "post" or b["origem_id"] == f"post:{slug}":
            erros.append(f"{b['id']}: origem {b['origem_id']!r} não é outro post do catálogo")
        elif b["origem_id"].startswith("post:"):
            _, corpo_origem, _ = ler_post(RAIZ / "posts" / b["origem_id"][5:] / "post.md")
            if not b["ancora_na_origem"] or corpo_origem.count(b["ancora_na_origem"]) != 1:
                erros.append(f"{b['id']}: ancora_na_origem precisa aparecer 1 vez em {b['origem_id']}")

    for id_, campo, texto in _textos(parecer):
        if EMOJI.search(texto):
            erros.append(f"{id_}: {campo} contém emoji")
        if campo in ("texto_sugerido", "frase_nova"):
            for num in NUMERO.findall(texto):
                if num not in corpo and num not in fontes_numero:
                    erros.append(f"{id_}: número {num!r} sem fonte no post nem em {', '.join(FONTES_NUMERO)}")

    ids = [x["id"] for k in ("alinhamento", "ctas", "referencias", "backlinks_sugeridos", "riscos") for x in parecer[k]]
    for i in {i for i in ids if ids.count(i) > 1}:
        erros.append(f"id repetido: {i}")
    return erros


ROTULO = {"inscricao": "inscrição", "compartilhar": "compartilhar", "comentar": "comentário",
          "responder_email": "resposta ao e-mail", "skill_check": "Skill Check", "link_post": "link para post"}


def _local(corpo, pos):
    """'3º parágrafo de «Seção»': onde achar o ponto no editor do Substack."""
    if pos < 0:
        return "local não encontrado"
    antes = corpo[:pos + 1]
    titulos = list(re.finditer(r"^#{2,3} (.+)$", antes, re.M))
    secao = f"de «{titulos[-1].group(1).strip()}»" if titulos else "da abertura"
    desde = antes[titulos[-1].end():] if titulos else antes
    n = len([b for b in re.split(r"\n\s*\n", desde) if b.strip()]) or 1
    return f"{n}º parágrafo {secao}"


def _fonte_numeros():
    return "\n".join((ESTRATEGIA / f).read_text(encoding="utf-8")
                     for f in FONTES_NUMERO if (ESTRATEGIA / f).exists())


def renderizar(parecer, erros, corpo, catalogo):
    nome = lambda i: (catalogo.get(i) or {}).get("titulo") or i  # noqa: E731
    url = lambda i: (catalogo.get(i) or {}).get("url") or "botão do Substack"  # noqa: E731
    cita = lambda t: "> " + t.replace("\n", "\n> ")  # noqa: E731
    L = [f"# Parecer de marketing: {parecer.get('post', '?')}", ""]
    if erros:
        L += ["**PARECER INVÁLIDO.** O validador reprovou os itens abaixo. Leia com cautela; "
              "itens com erro não podem ser aplicados.", ""] + [f"- {e}" for e in erros] + [""]
    else:
        L += ["Parecer válido (scripts/parecer.py). Responda no gate com os IDs, por exemplo: "
              "`aceito C1, R2; recuso C2; R1 com o texto \"…\"`.", ""]
    if "diagnostico" not in parecer:
        return "\n".join(L)

    d = parecer["diagnostico"]
    L += ["## Diagnóstico", "",
          f"Linha: {d['linha_editorial']} · voz {d['voz']} · segmento `{d['segmento']}` · eixo {d['eixo']} · "
          f"estágio {d['estagio']} · cluster {d['cluster'] or 'nenhum'}", ""]
    for j in d["justificativas"]:
        L += [f"- {j['escolha']}", "", cita(j["trecho"]), ""]

    L += ["## Alinhamento à estratégia", "", "| ID | Critério | Veredito | Evidência |", "|---|---|---|---|"]
    for a in parecer["alinhamento"]:
        L.append(f"| {a['id']} | {a['criterio']} | {a['veredito']} | {a['evidencia'].replace('|', '/')} |")
    for a in (a for a in parecer["alinhamento"] if a["veredito"] == "não passa"):
        L += ["", f"**{a['id']}, o que mudaria:** {a['o_que_mudaria']}", "", cita(a["trecho"])]
    L.append("")

    L += ["## CTAs", ""]
    texto = [c for c in parecer["ctas"] if c["formato"] == "texto"]
    for c in texto or []:
        pos = corpo.find(c["ancora"])
        L += [f"**{c['id']}** ({c['papel']}, {ROTULO[c['tipo']]} → {nome(c['destino_id'])}), parágrafo novo "
              f"depois do {_local(corpo, pos)}:", "", cita(c["texto_sugerido"]), "",
              f"Por quê: {c['motivo']}", ""]
    if not texto:
        L += ["Nenhuma sugestão de CTA em texto.", ""]

    L += ["### Inserção manual no Substack (botões nativos)", ""]
    nativos = [c for c in parecer["ctas"] if c["formato"] == "botao_nativo"]
    for c in nativos:
        pos = corpo.find(c["ancora"])
        L.append(f"- **{c['id']}**: botão de {ROTULO[c['tipo']]} depois do {_local(corpo, pos)}, "
                 f"que contém “{c['ancora'][:70]}”. {c['motivo']}")
    L += ([] if nativos else ["Nenhum."]) + [""]

    L += ["## Referências internas", ""]
    for r in parecer["referencias"]:
        onde = f"na frase nova “{r['frase_nova']}”, depois de" if r.get("frase_nova") else "no trecho"
        L += [f"**{r['id']}**: link “{r['texto_link']}” → {nome(r['destino_id'])} ({url(r['destino_id'])}), {onde}:",
              "", cita(r["ancora"]), "", f"Pergunta que o link responde: {r['pergunta_do_leitor']}", ""]
    if not parecer["referencias"]:
        L += ["Nenhuma sugestão.", ""]

    L += ["## Backlinks: posts antigos que devem apontar para este (edição manual no Substack)", ""]
    for b in parecer["backlinks_sugeridos"]:
        onde = f" no trecho “{b['ancora_na_origem']}”" if b["ancora_na_origem"] else ""
        L.append(f"- [ ] **{b['id']}**: em {nome(b['origem_id'])} ({url(b['origem_id'])}){onde}, "
                 f"link “{b['texto_link']}”. {b['motivo']}")
    L += ([] if parecer["backlinks_sugeridos"] else ["Nenhuma sugestão."]) + [""]

    L += ["## Riscos", ""]
    L += [f"- **{x['id']}**: {x['descricao']}" for x in parecer["riscos"]] or ["Nenhum."]
    return "\n".join(L) + "\n"


def validar(slug):
    pasta = _pasta(slug)
    _, corpo, _ = ler_post(pasta / "post.md")
    catalogo = _catalogo()
    try:
        parecer = json.loads((pasta / "marketing.json").read_text(encoding="utf-8"))
        erros = checar(parecer, corpo, catalogo, pasta.name, _fonte_numeros())
    except (OSError, json.JSONDecodeError) as e:
        parecer, erros = {"post": pasta.name}, [f"marketing.json ilegível: {e}"]
    (pasta / "marketing.md").write_text(renderizar(parecer, erros, corpo, catalogo), encoding="utf-8")
    print("\n".join(erros) if erros else "parecer válido", file=sys.stderr if erros else sys.stdout)
    return 1 if erros else 0


def aplicar(slug, escolhas):
    pasta = _pasta(slug)
    arquivo = pasta / "post.md"
    texto = arquivo.read_text(encoding="utf-8")
    _, corpo, inicio = ler_post(arquivo)
    parecer = json.loads((pasta / "marketing.json").read_text(encoding="utf-8"))
    catalogo = _catalogo()
    itens = {x["id"]: x for k in ("alinhamento", "ctas", "referencias", "backlinks_sugeridos", "riscos")
             for x in parecer[k]}

    operacoes, manual, avisos = [], [], []
    for e in escolhas:
        id_, _, novo = e.partition("=")
        item = itens.get(id_)
        if item is None:
            sys.exit(f"{id_}: não existe no parecer")
        if id_[0] in "AX":
            avisos.append(f"{id_}: pede redação, não inserção. Aplicar na etapa 4 (principal + voz-syntaxis), só no trecho citado.")
            continue
        if id_[0] == "B":
            manual.append(f"{id_}: em {item['origem_id']}, link “{item['texto_link']}” → este post (Substack, à mão)")
            continue
        if corpo.count(item["ancora"]) != 1:
            sys.exit(f"{id_}: a âncora não aparece exatamente 1 vez no post atual; nada foi aplicado")
        destino = catalogo.get(item["destino_id"])
        if not destino or not destino["citavel"]:
            sys.exit(f"{id_}: destino {item['destino_id']} não é citável; nada foi aplicado")
        pos = inicio + texto[inicio:].find(item["ancora"])
        fim = pos + len(item["ancora"])

        if id_[0] == "C" and item["formato"] == "botao_nativo":
            manual.append(f"{id_}: botão de {ROTULO[item['tipo']]} depois do {_local(corpo, pos - inicio)} "
                          f"(“{item['ancora'][:60]}”)")
            continue
        if id_[0] == "C":
            novo_texto = novo or item["texto_sugerido"]
            tl = item.get("texto_link")
            if destino["url"]:
                if not tl or tl not in novo_texto:
                    sys.exit(f"{id_}: o texto do link “{tl}” não está no texto novo; nada foi aplicado")
                novo_texto = novo_texto.replace(tl, f"[{tl}]({destino['url']})", 1)
            quebra = texto.find("\n\n", fim)
            onde = len(texto.rstrip("\n")) if quebra < 0 else quebra
            operacoes.append((onde, onde, "\n\n" + novo_texto))
        else:  # R
            tl = item["texto_link"]
            link = f"[{tl}]({destino['url']})"
            if item.get("frase_nova"):
                frase = novo or item["frase_nova"]
                if tl not in frase:
                    sys.exit(f"{id_}: o texto do link “{tl}” não está na frase nova; nada foi aplicado")
                operacoes.append((fim, fim, " " + frase.replace(tl, link, 1)))
            else:
                tl = novo or tl
                k = item["ancora"].find(tl)
                if k < 0:
                    sys.exit(f"{id_}: “{tl}” não está dentro da âncora; nada foi aplicado")
                operacoes.append((pos + k, pos + k + len(tl), f"[{tl}]({destino['url']})"))

    for a, b, novo in sorted(operacoes, reverse=True):
        texto = texto[:a] + novo + texto[b:]
    arquivo.write_text(texto, encoding="utf-8")
    print(f"{len(operacoes)} item(ns) aplicados em {arquivo}")
    for titulo, linhas in (("Inserção manual no Substack", manual), ("Fora do escopo deste script", avisos)):
        if linhas:
            print(f"\n{titulo}:\n- " + "\n- ".join(linhas))
    return 0


def guarda():
    caminho = json.load(sys.stdin).get("tool_input", {}).get("file_path", "")
    if re.search(r"(^|/)posts/[^/]+/marketing\.json$", caminho):
        return 0
    print(f"estrategista-marketing só escreve posts/<slug>/marketing.json, não {caminho}", file=sys.stderr)
    return 2


if __name__ == "__main__":
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ("", [])
    if cmd == "validar" and len(args) == 1:
        sys.exit(validar(args[0]))
    if cmd == "aplicar" and len(args) >= 2:
        sys.exit(aplicar(args[0], args[1:]))
    if cmd == "guarda":
        sys.exit(guarda())
    sys.exit(__doc__)
