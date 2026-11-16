#!/usr/bin/env python3
"""Triplas de edição: rascunho -> post.md final -> publicado, para cada post da era pipeline.

  python3 scripts/diff_edicoes.py            # todos os posts com slug_repo no mapa
  python3 scripts/diff_edicoes.py <slug-repo>

Lê estilo/corpus/mapa-publicados.json (gerado por corpus_publicado.py) e grava
estilo/corpus/edicoes/<slug-repo>.json + estilo/corpus/edicoes/_resumo.json.

Como funciona: cada texto vira uma sequência de tokens (palavra, pontuação ou bloco especial:
imagem, fórmula, CTA...), com a marcação (negrito, itálico, link) guardada como atributo e
fora da comparação. O alinhamento é global, por token (difflib), o que pega divisão e fusão de
parágrafo sem confundir com reescrita. Cada diferença post.md -> publicado vira uma operação
com classe, natureza e sinais:
  - reversao: o autor desfez texto que o pipeline introduziu, ou restaurou o rascunho;
  - acrescimo_autoral: texto que só existe no publicado (nem no rascunho, nem no post.md).
A natureza (estilo | conteúdo/fato | marketing | layout-substack | ambíguo) é heurística e
existe para não aprender estilo com edição de fato ou de marketing; o `ambíguo` vai ao autor.
Só stdlib.
"""

import difflib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
MAPA = RAIZ / "estilo" / "corpus" / "mapa-publicados.json"
SAIDA = RAIZ / "estilo" / "corpus" / "edicoes"
JANELA_MAX = 60  # tokens; acima disso a âncora no rascunho é vaga demais para dizer "restaurou"
DECISOES = RAIZ / "estilo" / "corpus" / "natureza-decidida.json"  # casos que o autor classificou
AVISO_LEGAL = re.compile(r"expressam exclusivamente minhas opiniões|não constitui recomendação|"
                         r"finalidade educacional|posição de meu empregador", re.I)

# ---------------------------------------------------------------- leitura e blocos


def ler(caminho):
    return ler_texto((RAIZ / caminho).read_text())


def ler_texto(t):
    t = unicodedata.normalize("NFC", t)
    meta = {}
    m = re.match(r"---\n(.*?)\n---\n", t, re.S)
    if m:
        for linha in m.group(1).splitlines():
            k, _, v = linha.partition(":")
            v = v.strip()
            try:
                meta[k.strip()] = json.loads(v)
            except json.JSONDecodeError:
                meta[k.strip()] = v.strip("'\"")
        t = t[m.end():]
    return meta, t


ESPECIAL = re.compile(r"^\[\[(CTA|PULLQUOTE|VIDEO|ENQUETE|EMBED)\b(.*)\]\]$", re.S)
IMAGEM = re.compile(r"^!\[(.*?)\]\(([^)]*)\)$", re.S)
ITEM = re.compile(r"^\s*(?:[-+]|\*(?=\s)|\d+[.)])\s+(?=\S)")


def blocos(corpo):
    """[(tipo, texto)]; tipo: paragrafo | titulo | item | imagem | formula | codigo | hr | CTA..."""
    cercas = []

    def guarda(m):
        cercas.append(m.group(0))
        return f"\x00{len(cercas) - 1}\x00"

    corpo = re.sub(r"```.*?```", guarda, corpo, flags=re.S)
    corpo = re.sub(r"\$\$.*?\$\$", guarda, corpo, flags=re.S)
    out = []
    for pedaco in re.split(r"\n\s*\n", corpo):
        atual = []
        if all(l.strip().startswith("|") for l in pedaco.strip().splitlines() if l.strip()) and pedaco.strip():
            out.append(("tabela", pedaco.strip()))  # o Substack não tem tabela nativa
            continue

        def fecha():
            if atual:
                out.append(("paragrafo", " ".join(atual)))
                atual.clear()

        for linha in pedaco.strip().splitlines():
            s = linha.strip()
            if not s or s == ">":
                continue
            if re.fullmatch(r"(\*\s*){3,}|-{3,}|_{3,}", s):
                fecha(); out.append(("hr", ""))
            elif re.match(r"#{1,6}\s", s):
                fecha(); out.append(("titulo", s.lstrip("#").strip()))
            elif ITEM.match(s):
                fecha(); out.append(("item", ITEM.sub("", s)))
            elif IMAGEM.match(s):
                fecha(); out.append(("imagem", IMAGEM.match(s).group(1)))
            elif ESPECIAL.match(s):
                fecha(); m = ESPECIAL.match(s); out.append((m.group(1), m.group(2).lstrip(": ")))
            elif re.fullmatch(r"\x00\d+\x00", s):
                fecha()
                bruto = cercas[int(s.strip("\x00"))]
                out.append(("codigo" if bruto.startswith("```") else "formula", bruto))
            else:
                atual.append(s.lstrip("> ").strip())
        fecha()
    return out, cercas


# ---------------------------------------------------------------- tokens

ASPAS = {"'": "'", "‘": "'", "’": "'", "´": "'", '"': '"', "“": '"', "”": '"', "«": '"', "»": '"'}
TRACOS = {"—", "–", "−", "-"}
RE_TOK = re.compile(
    r"\x00\d+\x00|\x01[^\x02]*\x02|\x03|\*\*|__|~~|\*|_|`[^`]*`|\.\.\.|"
    r"[^\W_]+(?:[-–'’][^\W_]+)*|[^\w\s]")


def _norm_formula(s):
    return re.sub(r"\s+|\\[,;: !]", "", s.strip("$`"))


def tokens(corpo):
    """Lista de dicts: n (normalizado), r (bruto), bl (bloco), tb (tipo do bloco),
    pal (é palavra), b/i/s (negrito/itálico/riscado), l (url do link), extra (legenda)."""
    bls, cercas = blocos(corpo)
    out = []
    for k, (tipo, texto) in enumerate(bls):
        base = {"bl": k, "tb": tipo, "b": False, "i": False, "s": False, "l": None, "pal": False}
        if tipo == "imagem":
            leg = re.sub(r"^(Gráfico|Diagrama|Infográfico):\s*", "", texto).strip()
            out.append({**base, "n": "⟦IMG⟧", "r": "⟦IMG⟧", "extra": leg})
            continue
        if tipo in ("formula", "codigo"):
            out.append({**base, "n": f"⟦{tipo.upper()}:{_norm_formula(texto)}⟧", "r": texto})
            continue
        if tipo in ("hr", "tabela") or tipo.isupper():
            nome = tipo.upper()
            out.append({**base, "n": f"⟦{nome}⟧", "r": f"⟦{nome}⟧", "extra": texto})
            continue
        texto = re.sub(r"\[([^\]]+)\]\(([^)\s]*)\)", lambda m: f"\x01{m.group(2)}\x02{m.group(1)}\x03",
                       texto)
        b = i = s = False
        link = None
        for m in RE_TOK.finditer(texto):
            t = m.group(0)
            if t in ("**", "__"):
                b = not b
            elif t in ("*", "_"):
                i = not i
            elif t == "~~":
                s = not s
            elif t.startswith("\x01"):
                link = t[1:-1]
            elif t == "\x03":
                link = None
            else:
                tok = {**base, "b": b, "i": i, "s": s, "l": link, "r": t}
                if t.startswith("\x00"):
                    bruto = cercas[int(t.strip("\x00"))]
                    tok.update(n=f"⟦FORMULA:{_norm_formula(bruto)}⟧", r=bruto)
                elif t.startswith("`"):
                    tok["n"] = "`" + t.strip("`")
                elif t in ASPAS:
                    tok["n"] = ASPAS[t]
                elif t in TRACOS:
                    tok["n"] = "—"
                elif t in ("...", "…"):
                    tok["n"] = "…"
                elif re.match(r"[^\W_]", t):
                    tok.update(n=t.casefold().replace("’", "'").replace("–", "-"), pal=True)
                else:
                    tok["n"] = t
                out.append(tok)
    return out, bls


SEM_ESPACO_ANTES = set(".,;:!?)]}»”’%…/")
SEM_ESPACO_DEPOIS = set("([{«“‘/")


def juntar(toks):
    """Texto legível a partir dos tokens (só para exibição no JSON e no laudo)."""
    s, abertas = "", {"'": False, '"': False}
    for t in toks:
        r = t["r"]
        fecha_reta = r in abertas and abertas[r]
        if s and not (r[:1] in SEM_ESPACO_ANTES or fecha_reta or s[-1] in SEM_ESPACO_DEPOIS
                      or (s[-1] in abertas and abertas[s[-1]])):
            s += " "
        if r in abertas:
            abertas[r] = not abertas[r]
        s += r
    return s


def alinhar(a, b):
    return difflib.SequenceMatcher(None, [t["n"] for t in a], [t["n"] for t in b],
                                   autojunk=False).get_opcodes()


def similaridade(a, b):
    pa, pb = [t["n"] for t in a if t["pal"]], [t["n"] for t in b if t["pal"]]
    return round(difflib.SequenceMatcher(None, pa, pb, autojunk=False).ratio(), 3)


# ---------------------------------------------------------------- operações


def _natureza_texto(classe, antes, depois):
    pals = [t for t in antes + depois if t["pal"]]
    if AVISO_LEGAL.search(juntar(depois)):  # GATE A (2026-11-15): aviso legal fica fora do estilo
        return "aviso-legal"
    if classe == "pontuacao":
        return "estilo"
    if any(t["l"] for t in depois) and not any(t["l"] for t in antes):
        return "marketing"
    if classe == "subtitulo_h2":
        return "estilo"
    if any(re.search(r"\d", t["r"]) for t in pals):
        return "conteúdo/fato"
    if max(sum(t["pal"] for t in antes), sum(t["pal"] for t in depois)) > 40:
        return "ambíguo"
    return "estilo"


NATUREZA_ESPECIAL = {
    "imagem": "layout-substack", "separador": "layout-substack", "pullquote": "layout-substack",
    "tabela": "layout-substack", "cta": "marketing", "video": "marketing", "enquete": "marketing", "embed": "marketing",
}


def _classe_especial(tok):
    n = tok["n"]
    if n.startswith("⟦FORMULA"):
        return "formula"
    if n.startswith("⟦CODIGO"):
        return "codigo"
    return {"⟦IMG⟧": "imagem", "⟦HR⟧": "separador", "⟦CTA⟧": "cta", "⟦PULLQUOTE⟧": "pullquote",
            "⟦VIDEO⟧": "video", "⟦ENQUETE⟧": "enquete", "⟦EMBED⟧": "embed",
            "⟦TABELA⟧": "tabela"}.get(n, "especial")


def _trigramas(ws):
    return {tuple(ws[i:i + 3]) for i in range(len(ws) - 2)}


def operacoes(rasc, post, pub, vocab_unico):
    """Diferenças post.md -> publicado, com origem no rascunho para os sinais."""
    origem = [None] * len(post)  # índice no rascunho de cada token do post.md, se veio de lá
    if rasc:
        for tag, i1, i2, j1, j2 in alinhar(rasc, post):
            if tag == "equal":
                for d in range(i2 - i1):
                    origem[j1 + d] = i1 + d
    ops = []
    rasc_pal = [t["n"] for t in rasc if t["pal"]]
    rasc3 = _trigramas(rasc_pal)

    def janela_rascunho(i1, i2):
        antes = next((origem[k] for k in range(i1 - 1, -1, -1) if origem[k] is not None), None)
        depois = next((origem[k] for k in range(i2, len(post)) if origem[k] is not None), None)
        if antes is None or depois is None or depois - antes > JANELA_MAX:
            return None
        return [t["n"] for t in rasc[max(antes - 3, 0): depois + 4] if t["pal"]]

    def sinais(i1, i2, depois_toks):
        a_pal = [k for k in range(i1, i2) if post[k]["pal"]]
        d_pal = [t["n"] for t in depois_toks if t["pal"]]
        frac_pipe = (sum(origem[k] is None for k in a_pal) / len(a_pal)) if a_pal else None
        restaurou = None  # None = não dá para saber (sem âncora confiável no rascunho)
        if rasc and d_pal:
            jan = janela_rascunho(i1, i2)
            if jan is not None:
                restaurou = (" " + " ".join(d_pal) + " ") in (" " + " ".join(jan) + " ")
            if not restaurou and len(d_pal) >= 4:  # trecho longo: trigramas no rascunho inteiro
                tri = _trigramas(d_pal)
                fracao = len(tri & rasc3) / len(tri)
                restaurou = True if fracao >= 0.6 else (False if fracao < 0.2 else None)
        s = []
        if restaurou or (frac_pipe is not None and frac_pipe >= 0.5 and rasc):
            s.append("reversao")
        if d_pal and restaurou is False:
            s.append("acrescimo_autoral")
        origem_antes = (None if frac_pipe is None else
                        "pipeline" if frac_pipe >= 0.5 else "rascunho" if frac_pipe == 0 else "misto")
        return s, restaurou, origem_antes

    def contexto(i1, i2):
        return juntar(post[max(i1 - 6, 0):i1]) + " [[…]] " + juntar(post[i2:i2 + 6])

    def nova(classe, natureza, i1, i2, antes, depois, **extra):
        s, restaurou, origem_antes = sinais(i1, i2, depois)
        op = {"classe": classe, "natureza": natureza,
              "antes": juntar(antes), "depois": juntar(depois),
              "palavras_antes": sum(t["pal"] for t in antes),
              "palavras_depois": sum(t["pal"] for t in depois),
              "bloco_antes": antes[0]["bl"] if antes else None,
              "bloco_depois": depois[0]["bl"] if depois else None,
              "sinais": s, "restaurou_rascunho": restaurou, "origem_antes": origem_antes,
              "contexto": contexto(i1, i2)}
        op.update(extra)
        ops.append(op)

    mapa_ab = {}
    for tag, i1, i2, j1, j2 in alinhar(post, pub):
        if tag == "equal":
            for d in range(i2 - i1):
                mapa_ab[i1 + d] = j1 + d
            continue
        a, b = post[i1:i2], pub[j1:j2]
        # especiais saem como operações próprias; o resto do trecho é texto
        for lado, toks in (("antes", a), ("depois", b)):
            for t in toks:
                if t["n"].startswith("⟦"):
                    cl = _classe_especial(t)
                    par = [x for x in (b if lado == "antes" else a) if _classe_especial(x) == cl
                           and x["n"].startswith("⟦")]
                    if lado == "depois" and par:
                        continue  # substituição de especial já registrada pelo lado "antes"
                    # fórmula e código, trocados, acrescentados ou cortados, são conteúdo (GATE A)
                    nat = NATUREZA_ESPECIAL.get(cl, "conteúdo/fato")
                    nova(cl, nat, i1, i2, [t] if lado == "antes" else par[:1],
                         [t] if lado == "depois" else par[:1],
                         tipo="substituicao" if par else ("remocao" if lado == "antes" else "insercao"))
        ta = [t for t in a if not t["n"].startswith("⟦")]
        tb = [t for t in b if not t["n"].startswith("⟦")]
        if not ta and not tb:
            continue
        if all(not t["pal"] for t in ta + tb):
            classe = "pontuacao"
        elif all(t["tb"] == "titulo" for t in ta + tb if t["pal"]):
            classe = "subtitulo_h2"
        else:
            classe = {"replace": "substituicao", "delete": "remocao", "insert": "insercao"}[tag]
        extra = {}
        if classe == "substituicao":  # erro de digitação no site: palavra única no corpus, parecida
            for t in tb:
                if t["pal"] and t["n"] in vocab_unico and difflib.get_close_matches(
                        t["n"], [x["n"] for x in ta if x["pal"]], n=1, cutoff=0.8):
                    extra["obs"] = f"possível erro de digitação no site: '{t['r']}'"
        nova(classe, _natureza_texto(classe, ta, tb), i1, i2, ta, tb, **extra)

    # divisão e fusão de parágrafo, e formatação, sobre os tokens iguais
    chaves = sorted(mapa_ab)
    for k, k2 in zip(chaves, chaves[1:]):
        if k2 != k + 1 or mapa_ab[k2] != mapa_ab[k] + 1:
            continue
        mesmo_a = post[k]["bl"] == post[k2]["bl"]
        mesmo_b = pub[mapa_ab[k]]["bl"] == pub[mapa_ab[k2]]["bl"]
        if mesmo_a == mesmo_b:
            continue
        classe = "divisao_paragrafo" if mesmo_a else "fusao_paragrafo"
        restaurou = None
        if origem[k] is not None and origem[k2] == origem[k] + 1:
            restaurou = (rasc[origem[k]]["bl"] != rasc[origem[k2]]["bl"]) == (classe == "divisao_paragrafo")
        novo_bloco = [t for t in pub if t["bl"] == pub[mapa_ab[k2]]["bl"]]
        obs = None
        if classe == "divisao_paragrafo" and all(not t["pal"] for t in novo_bloco):
            obs = "parágrafo só com pontuação no site (provável deslize)"
        ops.append({"classe": classe, "natureza": "ambíguo" if obs else "estilo",
                    "antes": juntar(post[max(k - 8, 0):k + 1]), "depois": juntar(post[k2:k2 + 8]),
                    "palavras_antes": 0, "palavras_depois": 0,
                    "bloco_antes": post[k]["bl"], "bloco_depois": pub[mapa_ab[k2]]["bl"],
                    "sinais": ["reversao"] if restaurou else [], "restaurou_rascunho": restaurou,
                    "origem_antes": None, "contexto": juntar(post[max(k - 8, 0):k2 + 8]),
                    **({"obs": obs} if obs else {})})

    def formatacao(attr, nome):
        corrida = []

        def fecha():
            if not corrida:
                return
            adicionou = pub[mapa_ab[corrida[0]]][attr] and not post[corrida[0]][attr]
            restaurou = None
            if rasc and all(origem[k] is not None for k in corrida):
                restaurou = all(bool(rasc[origem[k]][attr]) == adicionou for k in corrida)
            texto = juntar([post[k] for k in corrida])
            classe = f"{nome}_{'adicionado' if adicionou else 'removido'}"
            ops.append({"classe": classe,
                        "natureza": "marketing" if attr == "l" else "estilo",
                        "antes": "" if adicionou else texto, "depois": texto if adicionou else "",
                        "palavras_antes": 0, "palavras_depois": 0,
                        "bloco_antes": post[corrida[0]]["bl"], "bloco_depois": pub[mapa_ab[corrida[0]]]["bl"],
                        "sinais": ["reversao"] if restaurou else [], "restaurou_rascunho": restaurou,
                        "origem_antes": None, "contexto": juntar(post[max(corrida[0] - 6, 0):corrida[-1] + 7])})
            corrida.clear()

        anterior = None
        for k in chaves:
            mudou = bool(post[k][attr]) != bool(pub[mapa_ab[k]][attr]) and post[k]["tb"] != "titulo"
            sentido = bool(pub[mapa_ab[k]][attr]) if mudou else None
            if not mudou or (corrida and (k != corrida[-1] + 1 or sentido != anterior)):
                fecha()
            if mudou:
                corrida.append(k)
                anterior = sentido
        fecha()

    formatacao("b", "negrito")
    formatacao("i", "italico")
    formatacao("s", "riscado")
    formatacao("l", "link")

    tipograf = Counter()
    for k in chaves:
        ra, rb = post[k]["r"], pub[mapa_ab[k]]["r"]
        if ra != rb and post[k]["n"] in ("'", '"'):
            tipograf["aspas"] += 1
        elif ra != rb and post[k]["n"] == "—":
            tipograf["travessao"] += 1
        elif ra != rb and post[k]["n"] == "…":
            tipograf["reticencias"] += 1
        elif post[k]["n"] == "⟦IMG⟧" and post[k]["extra"] != pub[mapa_ab[k]]["extra"]:
            nova("legenda", "estilo" if pub[mapa_ab[k]]["extra"] else "layout-substack", k, k + 1,
                 [{**post[k], "r": post[k]["extra"]}],
                 [{**pub[mapa_ab[k]], "r": pub[mapa_ab[k]]["extra"]}])
    for nome, n in tipograf.items():  # troca de caractere sem mudar o texto; resumida por post
        ops.append({"classe": f"tipografia_{nome}", "natureza": "layout-substack", "antes": "",
                    "depois": "", "palavras_antes": 0, "palavras_depois": 0, "bloco_antes": None,
                    "bloco_depois": None, "sinais": [], "restaurou_rascunho": None,
                    "origem_antes": None, "contexto": "", "ocorrencias": n})
    for i, op in enumerate(ops, 1):
        op["id"] = i
    return ops


# ---------------------------------------------------------------- execução


def base_post_md(slug_repo, pub):
    """O autor parte da versão que existia quando publicou, não necessariamente da atual
    (caso real: 2026-09-01 foi regerado do zero no dia seguinte à publicação). Escolhe, no
    histórico do git, a versão do post.md mais próxima do publicado; empate fica com a atual."""
    caminho = f"posts/{slug_repo}/post.md"
    atual = (RAIZ / caminho).read_text()
    commits = subprocess.run(["git", "log", "--all", "--format=%h", "--", caminho], cwd=RAIZ,
                             capture_output=True, text=True, check=True).stdout.split()
    melhor = ("atual", atual, similaridade(tokens(ler_texto(atual)[1])[0], pub))
    sim_atual = melhor[2]
    for h in commits:
        r = subprocess.run(["git", "show", f"{h}:{caminho}"], cwd=RAIZ, capture_output=True, text=True)
        if r.returncode != 0 or r.stdout == atual:
            continue
        sim = similaridade(tokens(ler_texto(r.stdout)[1])[0], pub)
        if sim > melhor[2] + 0.005:
            melhor = (h, r.stdout, sim)
    return melhor[0], melhor[1], sim_atual, melhor[2]


def processar(item, vocab_unico):
    meta_pub, corpo_pub = ler(f"estilo/corpus/publicados/{item['slug_site']}.md")
    pub, _ = tokens(corpo_pub)
    commit, texto_post, sim_atual, sim_base = base_post_md(item["slug_repo"], pub)
    meta_post, corpo_post = ler_texto(texto_post)
    h1 = re.match(r"\s*# ([^\n]+)\n", corpo_post)  # no Substack o título fica fora do corpo
    if h1:
        corpo_post = corpo_post[h1.end():]
    rasc = tokens(ler(item["rascunho"])[1])[0] if item["rascunho"] else []
    post, _ = tokens(corpo_post)
    ops = operacoes(rasc, post, pub, vocab_unico)
    for campos, campo_pub, classe in ((("titulo", "título", "title"), "titulo", "titulo_post"),
                                      (("subtitulo", "subtítulo", "subtitle"), "subtitulo", "subtitulo_post")):
        a = next((str(meta_post[c]) for c in campos if meta_post.get(c)), "")
        if not a and classe == "titulo_post" and h1:
            a = h1.group(1)
        a, b = a.strip(), (meta_pub.get(campo_pub) or "").strip()
        if a != b:
            # GATE A (2026-11-15): troca de título e subtítulo é estilo de manchete
            ops.append({"id": len(ops) + 1, "classe": classe, "natureza": "estilo", "antes": a,
                        "depois": b, "palavras_antes": len(a.split()), "palavras_depois": len(b.split()),
                        "bloco_antes": None, "bloco_depois": None, "sinais": [],
                        "restaurou_rascunho": None, "origem_antes": None, "contexto": ""})
    for d in (json.loads(DECISOES.read_text()) if DECISOES.exists() else []):
        if d["slug_repo"] != item["slug_repo"]:
            continue
        for op in ops:
            if op["classe"] == d["classe"] and (d["trecho"] in op["antes"] or d["trecho"] in op["depois"]):
                op["natureza"], op["natureza_fonte"] = d["natureza"], d["motivo"]
    resultado = {
        "slug_repo": item["slug_repo"], "slug_site": item["slug_site"],
        "linha_editorial": meta_post.get("linha_editorial"), "rascunho": item["rascunho"],
        "rascunho_tipo": item["rascunho_tipo"],
        "post_md_base": {"commit": commit, "similaridade_base": sim_base,
                         "similaridade_versao_atual": sim_atual},
        "palavras": {"rascunho": sum(t["pal"] for t in rasc), "post_md": sum(t["pal"] for t in post),
                     "publicado": sum(t["pal"] for t in pub)},
        "similaridade": {"rascunho_post_md": similaridade(rasc, post) if rasc else None,
                         "post_md_publicado": similaridade(post, pub),
                         "rascunho_publicado": similaridade(rasc, pub) if rasc else None},
        "resumo_classe": dict(Counter(o["classe"] for o in ops).most_common()),
        "resumo_natureza": dict(Counter(o["natureza"] for o in ops).most_common()),
        "sinais": dict(Counter(s for o in ops for s in o["sinais"])),
        "operacoes": ops,
    }
    (SAIDA / f"{item['slug_repo']}.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=1) + "\n")
    return resultado


def main(alvo=None):
    mapa = [i for i in json.loads(MAPA.read_text()) if i["slug_repo"]]
    if alvo:
        mapa = [i for i in mapa if i["slug_repo"] == alvo]
        if not mapa:
            raise SystemExit(f"slug não encontrado no mapa: {alvo}")
    # vocabulário de todo o corpus (para a suspeita de erro de digitação)
    vocab = Counter()
    for item in json.loads(MAPA.read_text()):
        vocab.update(t["n"] for t in tokens(ler(f"estilo/corpus/publicados/{item['slug_site']}.md")[1])[0]
                     if t["pal"])
        if item["slug_repo"]:
            vocab.update(t["n"] for t in tokens(ler(f"posts/{item['slug_repo']}/post.md")[1])[0] if t["pal"])
    unico = {w for w, n in vocab.items() if n == 1}
    SAIDA.mkdir(parents=True, exist_ok=True)
    resumo = []
    for item in mapa:
        r = processar(item, unico)
        resumo.append({k: r[k] for k in ("slug_repo", "linha_editorial", "rascunho_tipo", "palavras",
                                          "similaridade", "resumo_classe", "resumo_natureza", "sinais")})
        s = r["similaridade"]
        print(f"{r['slug_repo'][:44]:44} r→p={s['rascunho_post_md']} p→s={s['post_md_publicado']} "
              f"r→s={s['rascunho_publicado']} ops={len(r['operacoes'])} sinais={r['sinais']}")
    if not alvo:
        (SAIDA / "_resumo.json").write_text(json.dumps(resumo, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
