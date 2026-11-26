"""Storyboard do vídeo D+1 (Fatia C da esteira v2). Contrato com o ../spielberg: storyboard.json 1.0.

  python3 scripts/storyboard.py validar <slug>   confere distribuicao/video/storyboard.json
  python3 scripts/storyboard.py md <slug>        (re)gera distribuicao/video/storyboard.md a partir do JSON
  python3 scripts/storyboard.py data <slug>      imprime a data do vídeo (peça de vídeo do kit.json)

O storyboard.md nunca é editado à mão: o validador reprova se ele diferir do que o script gera.
"""
import json
import re
import sys
from pathlib import Path

import jsonschema

sys.path.insert(0, str(Path(__file__).resolve().parent))
from kit import RAIZ, _fontes, _pasta, ler_config, numeros  # noqa: E402
from parecer import EMOJI, termina_em_pergunta  # noqa: E402

ESQUEMA = RAIZ / ".claude/skills/distribuicao/referencias/storyboard.schema.json"
PALAVRA = re.compile(r"[A-Za-zÀ-ÿ]")


def palavras(texto):
    """Palavras com letra (número e símbolo não contam)."""
    return [w for w in (texto or "").split() if PALAVRA.search(w)]


def estimar_s(texto, cfg):
    return len((texto or "").split()) / cfg["video"]["palavras_por_s"]


def data_video(kit):
    """Data da peça de vídeo no kit.json (o kit já fez a conta: publicação + offset)."""
    return next((p["data"] for p in kit["pecas"] if p["tipo"] == "video"), None)


def textos_na_tela(sb):
    out = []
    for c in sb["cenas"]:
        k = c.get("cartao") or {}
        out += [(k.get("id", c["id"]), k.get(campo) or "") for campo in ("eyebrow", "texto", "destaque", "rodape")]
    out += [("capa", sb["capa"].get(campo) or "") for campo in ("eyebrow", "texto", "destaque")]
    return [(i, t) for i, t in out if t]


def checar(sb, kit, cfg, fontes, post, md=None):
    """Lista de erros. `fontes`: números do post + FEAR/GREED; `post`: texto do post.md."""
    try:
        jsonschema.validate(sb, json.loads(ESQUEMA.read_text(encoding="utf-8")))
    except jsonschema.ValidationError as e:
        return [f"esquema 1.0: {e.message} (em {'/'.join(map(str, e.absolute_path)) or 'raiz'})"]
    v, erros = cfg["video"], []
    if kit and sb["post"]["data_video"] != data_video(kit):
        erros.append(f"data_video {sb['post']['data_video']} ≠ {data_video(kit)} (peça de vídeo do kit.json)")
    falas = {t["id"]: t["fala"] for t in sb["tomadas"]}
    for t in sb["tomadas"]:
        s = estimar_s(t["fala"], cfg)
        if s > v["tomada_max_s"] and not t.get("excecao"):
            erros.append(f"{t['id']}: ~{s:.0f} s de fala, acima de {v['tomada_max_s']} s (divida a tomada ou registre `excecao`)")
    total = sum(estimar_s(t["fala"], cfg) for t in sb["tomadas"])
    a, b = sb["formato"]["duracao_alvo_s"]
    if not a <= total <= b:
        erros.append(f"duração estimada ~{total:.0f} s fora da faixa {a}–{b} s ({v['palavras_por_s']} palavras/s)")
    for c in sb["cenas"]:
        if c["tomada"] not in falas:
            erros.append(f"{c['id']}: tomada {c['tomada']} não existe")
            continue
        for campo in ("ancora_inicio", "ancora_fim"):
            if c[campo] not in falas[c["tomada"]]:
                erros.append(f"{c['id']}: {campo} “{c[campo]}” não é trecho literal da fala da {c['tomada']}")
        if (k := c.get("cartao")):
            lim = v["cartao_palavras_max"]
            n = len(palavras(" ".join(k.get(x) or "" for x in ("texto", "destaque"))))
            if n > lim[k["modo"]]:
                erros.append(f"{k['id']}: {n} palavras no texto e no destaque, acima de {lim[k['modo']]} ({k['modo']})")
            if len(palavras(k.get("eyebrow"))) > lim["eyebrow"]:
                erros.append(f"{k['id']}: eyebrow com mais de {lim['eyebrow']} palavras")
        for num in c.get("numeros", []):
            if num["fonte"] not in post:
                erros.append(f"{c['id']}: a fonte de {num['valor']} não é trecho literal do post")
    for ident, texto in textos_na_tela(sb):
        for n in sorted(numeros(texto) - fontes):
            erros.append(f"{ident}: número {n} não está no post nem em FEAR/GREED")
    tudo = json.dumps(sb, ensure_ascii=False)
    if EMOJI.search(tudo):
        erros.append("emoji no storyboard")
    if not termina_em_pergunta(sb["fechamento"]["pergunta"]):
        erros.append("fechamento.pergunta não termina em pergunta")
    if not sb["fechamento"]["convite"].strip():
        erros.append("fechamento sem convite")
    if md is not None and md != renderizar(sb, cfg):
        erros.append("storyboard.md difere do gerado pelo script (nunca edite à mão: rode `storyboard.py md`)")
    return erros


def _cel(s):
    return (s or "").replace("\n", " / ").replace("|", "\\|")


def renderizar(sb, cfg):
    p, e = sb["post"], sb["estrategia"]
    total = sum(estimar_s(t["fala"], cfg) for t in sb["tomadas"])
    L = [f"# Storyboard · {p['titulo']}", "",
         "Gerado por `scripts/storyboard.py md` a partir de `storyboard.json`. Não edite à mão.", "",
         f"Vídeo de {p['data_video']} · {e['segmento']} · {e['estagio_funil']} · ~{total:.0f} s estimados "
         f"(faixa {sb['formato']['duracao_alvo_s'][0]}–{sb['formato']['duracao_alvo_s'][1]} s)", "",
         "## Tomadas", "", "| ID | Bloco | Fala | ~s | Nota |", "|---|---|---|---|---|"]
    L += [f"| {t['id']} | {t['bloco']} | {_cel(t['fala'])} | {estimar_s(t['fala'], cfg):.0f} | "
          f"{_cel(t.get('excecao') or t.get('nota'))} |" for t in sb["tomadas"]]
    L += ["", "## Cenas", "", "| ID | Tomada | De → até | Visual | Cartão | Números |", "|---|---|---|---|---|---|"]
    for c in sb["cenas"]:
        k = c.get("cartao") or {}
        cartao = " · ".join(x for x in [k.get("id"), k.get("modo"), k.get("chassi") and f"chassi {k['chassi']}",
                                        _cel(k.get("eyebrow")), _cel(k.get("texto")),
                                        k.get("destaque") and f"**{_cel(k['destaque'])}**", _cel(k.get("rodape"))] if x)
        visual = c["visual"] + (f", zoom {c['zoom']['de']}→{c['zoom']['para']}" if c.get("zoom") else "") + \
            (f", {c['grafico']['arquivo']}" if c.get("grafico") else "")
        L.append(f"| {c['id']} | {c['tomada']} | “{_cel(c['ancora_inicio'])}” → “{_cel(c['ancora_fim'])}” | {visual} | "
                 f"{cartao or '—'} | {', '.join(n['valor'] for n in c.get('numeros', [])) or '—'} |")
    capa = sb["capa"]
    L += ["", "## Capa", "", f"Chassi {capa['chassi']}: " + " · ".join(
        x for x in [capa.get("eyebrow"), capa.get("destaque") and f"**{capa['destaque']}**", capa["texto"]] if x),
          "", "## Fechamento", "", f"Pergunta: {sb['fechamento']['pergunta']}", "",
          f"Convite: {sb['fechamento']['convite']}", ""]
    return "\n".join(L)


def _ler(slug):
    pasta, cfg = _pasta(slug), ler_config()
    video = pasta / "distribuicao/video"
    sb = json.loads((video / "storyboard.json").read_text(encoding="utf-8"))
    kit_p = pasta / "distribuicao/kit.json"
    kit = json.loads(kit_p.read_text(encoding="utf-8")) if kit_p.exists() else None
    return pasta, cfg, video, sb, kit


def validar(slug):
    pasta, cfg, video, sb, kit = _ler(slug)
    md_p = video / "storyboard.md"
    md = md_p.read_text(encoding="utf-8") if md_p.exists() else None
    erros = checar(sb, kit, cfg, _fontes(pasta, cfg), (pasta / "post.md").read_text(encoding="utf-8"), md)
    if md is None:
        erros.append("storyboard.md ausente: rode `storyboard.py md`")
    print("\n".join(erros) if erros else "storyboard válido", file=sys.stderr if erros else sys.stdout)
    return 1 if erros else 0


def gerar_md(slug):
    _, cfg, video, sb, _ = _ler(slug)
    (video / "storyboard.md").write_text(renderizar(sb, cfg), encoding="utf-8")
    print(video / "storyboard.md")
    return 0


if __name__ == "__main__":
    cmd, args = (sys.argv[1], sys.argv[2:]) if len(sys.argv) > 1 else ("", [])
    if cmd == "validar" and len(args) == 1:
        sys.exit(validar(args[0]))
    if cmd == "md" and len(args) == 1:
        sys.exit(gerar_md(args[0]))
    if cmd == "data" and len(args) == 1:
        print(data_video(_ler(args[0])[4]))
        sys.exit(0)
    sys.exit(__doc__)
