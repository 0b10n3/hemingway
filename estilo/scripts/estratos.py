#!/usr/bin/env python3
"""Métricas de forma por estrato — irmão de metricas.py, para a deriva de estilo (Fase B3).

  python3 estilo/scripts/estratos.py

Estratos: publicados anteriores ao pipeline (15), rascunhos de verdade (13; as 3 transcrições
ficam fora), post.md que serviu de base à publicação (16) e publicados da era pipeline (16).
Mede forma, não conteúdo: frase, parágrafo, pessoa, conectivos, pontuação, ênfase, perguntas,
H2 e glosa de sigla. A pergunta é direcional: nos 13 posts com rascunho de verdade, o pipeline
afasta o texto do autor (rascunho -> post.md) e o autor puxa de volta (post.md -> site)?

Grava pesquisa/epico-revisao-editorial/dados/b3-estratos.json. Só stdlib; usa os blocos e os
tokens de scripts/diff_edicoes.py e a lista de conectivos de metricas.py.
"""
import json
import re
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ / "scripts"))
sys.path.insert(0, str(RAIZ / "estilo" / "scripts"))
import diagnostico_edicoes as G  # noqa: E402
import diff_edicoes as D  # noqa: E402
from metricas import CONECTIVOS  # noqa: E402

SAIDA = RAIZ / "pesquisa" / "epico-revisao-editorial" / "dados" / "b3-estratos.json"
PALAVRA = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
FIM_FRASE = re.compile(r"(?<=[.!?…])[\"”’)]*\s+(?=[\"“‘(]?[A-ZÀ-Ú0-9])")


def _conta(rx, texto):
    return len(re.findall(rx, texto, re.I))


def metricas(corpo):
    bls, _ = D.blocos(corpo)
    prosa = [t for tipo, t in bls if tipo in ("paragrafo", "item")]
    pars = [t for tipo, t in bls if tipo == "paragrafo"]
    texto = "\n".join(prosa)
    limpo = re.sub(r"\]\([^)]*\)", "]", texto)
    w = len(PALAVRA.findall(limpo)) or 1
    frases = [len(PALAVRA.findall(f)) for p in pars for f in FIM_FRASE.split(p) if PALAVRA.search(f)]
    pal_par = [len(PALAVRA.findall(p)) for p in pars]
    siglas = {}
    for m in re.finditer(r"\b[A-Z]{2,}[a-z]?\b", limpo):
        siglas.setdefault(m.group(0), m.start())
    glosadas = sum(1 for s, i in siglas.items() if "(" in limpo[max(i - 4, 0):i + len(s) + 4]
                   or re.search(r"\)", limpo[max(i - 3, 0):i]))
    por_mil = lambda n: round(1000 * n / w, 2)  # noqa: E731
    return {
        "palavras": w,
        "frase_media": round(statistics.mean(frases), 1) if frases else None,
        "frase_cv": round(statistics.pstdev(frases) / statistics.mean(frases), 2) if len(frases) > 1 else None,
        "paragrafo_media": round(statistics.mean(pal_par), 1) if pal_par else None,
        "paragrafo_cv": round(statistics.pstdev(pal_par) / statistics.mean(pal_par), 2) if len(pal_par) > 1 else None,
        "pct_paragrafo_1_frase": round(100 * sum(len([f for f in FIM_FRASE.split(p) if PALAVRA.search(f)]) <= 1
                                                for p in pars) / len(pars), 1) if pars else None,
        "eu_por_mil": por_mil(_conta(r"\b(eu|meu|minha|meus|minhas|me|mim|comigo)\b", limpo)),
        "nos_por_mil": por_mil(_conta(r"\b(nós|nosso|nossa|nossos|nossas|conosco|a gente)\b", limpo)),
        "voce_por_mil": por_mil(_conta(r"\b(você|vocês|te|contigo)\b", limpo)),
        "conectivos_por_mil": por_mil(sum(_conta(r"\b" + re.escape(c) + r"\b", limpo) for c in CONECTIVOS)),
        "travessao_por_mil": por_mil(limpo.count("—") + len(re.findall(r"\s[-–]\s", limpo))),
        "dois_pontos_por_mil": por_mil(limpo.count(":")),
        "parenteses_por_mil": por_mil(limpo.count("(")),
        "aspas_duplas_por_mil": por_mil(len(re.findall(r"[“\"][^”\"\n]{1,80}[”\"]", limpo))),
        "aspas_simples_por_mil": por_mil(len(re.findall(r"(?<![\w’'])['‘][^'‘’\n]{2,60}['’](?!\w)", limpo))),
        "negrito_por_mil": por_mil(limpo.count("**") // 2),
        "italico_por_mil": por_mil(len(re.findall(r"(?<![*\w])[*_](?=\S)[^*_\n]{1,80}(?<=\S)[*_](?![*\w])", limpo))),
        "perguntas_por_mil": por_mil(limpo.count("?")),
        "exclamacoes_por_mil": por_mil(limpo.count("!")),
        "h2_por_mil": por_mil(sum(1 for tipo, _ in bls if tipo == "titulo")),
        "pct_siglas_glosadas": round(100 * glosadas / len(siglas), 1) if siglas else None,
        # para testar as regras 6, 8 e 9 e o §8 do guia v1 (B4)
        "citacao_autor_ano_por_mil": por_mil(len(re.findall(
            r"\b[A-ZÀ-Ú][\wà-ú]+(?:(?:,| e| &) [A-ZÀ-Ú][\wà-ú]+)*,? \((?:19|20)\d{2}\)"
            r"|\([A-ZÀ-Ú][\wà-ú]+[^()\n]{0,40}(?:19|20)\d{2}\)", limpo))),
        "instituicoes_por_mil": por_mil(len(re.findall(
            r"\b(CVM|Banco Central|BCB|Bacen|B3|Copom|CMN|Conselho Monetário Nacional|Tesouro Nacional|Anbima|FGC)\b", limpo))),
        "reticencias_por_mil": por_mil(limpo.count("…") + limpo.count("...")),
        "imagens": sum(1 for tipo, _ in bls if tipo == "imagem"),
        "refere_visual_por_mil": por_mil(_conta(r"\b(gráfico|diagrama|figura|imagem) (abaixo|acima|a seguir)|\bveja (o|a) (gráfico|diagrama|figura)", limpo)),
        "tem_cta_botao": int("[[CTA" in corpo),
    }


def _voz(slug):
    p = RAIZ / "posts" / slug / "processo" / "01-briefing.md"
    t = p.read_text() if p.exists() else ""
    m = re.search(r"\*\*\s*(Ensa[íi]stica|Explicativa)", t) or \
        re.search(r"voz\W+(?:\w+\W+){0,3}?(ensa[íi]stica|explicativa)", t, re.I)
    return ("explicativa" if m.group(1).lower().startswith("expl") else "ensaística") if m else None


def main():
    docs = []
    for item in G.MAPA:
        site = metricas(D.ler(f"estilo/corpus/publicados/{item['slug_site']}.md")[1])
        if item["epoca"] == "pre-pipeline":
            docs.append({"estrato": "pre", "slug": item["slug_site"], **site})
            continue
        slug = item["slug_repo"]
        ed = json.loads((D.SAIDA / f"{slug}.json").read_text())
        base = G.mostrar(ed["post_md_base"]["commit"], f"posts/{slug}/post.md")
        comum = {"slug": slug, "linha": ed["linha_editorial"] or "—", "voz": _voz(slug),
                 "rascunho_tipo": item["rascunho_tipo"]}
        docs.append({"estrato": "post", **comum, **metricas(G.corpo_post(base))})
        docs.append({"estrato": "site", **comum, **site})
        if item["rascunho_tipo"] == "rascunho":
            docs.append({"estrato": "rascunho", **comum, **metricas(D.ler(item["rascunho"])[1])})
    nomes = [k for k in docs[0] if k not in ("estrato", "slug", "linha", "voz", "rascunho_tipo")]

    def media(filtro, k):
        vals = [d[k] for d in docs if filtro(d) and d[k] is not None]
        return round(statistics.mean(vals), 2) if vals else None

    estratos = {e: {k: media(lambda d, e=e: d["estrato"] == e, k) for k in nomes}
                for e in ("pre", "rascunho", "post", "site")}
    grupos = {f"{e}|{campo}={valor}": {k: media(lambda d, e=e, c=campo, v=valor: d["estrato"] == e and d.get(c) == v, k)
                                       for k in nomes}
              for e in ("post", "site") for campo, valor in
              (("linha", "Spoiler"), ("linha", "Notas de um Professor"), ("voz", "ensaística"), ("voz", "explicativa"))}
    # direção, nos 13 posts com rascunho de verdade
    trios = {}
    for d in docs:
        if d.get("rascunho_tipo") == "rascunho":
            trios.setdefault(d["slug"], {})[d["estrato"]] = d
    direcao = {}
    for k in nomes:
        if k == "palavras":
            continue
        r_p = s_p = volta = 0
        n = 0
        for t in trios.values():
            r, p, s = (t[x][k] for x in ("rascunho", "post", "site"))
            if None in (r, p, s):
                continue
            n += 1
            r_p += p > r
            s_p += s < p
            volta += (p - r) * (s - p) < 0
        direcao[k] = {"posts": n, "pipeline_aumenta": r_p, "autor_diminui": s_p, "autor_puxa_de_volta": volta}
    vozes = {d["slug"]: d["voz"] for d in docs if d["estrato"] == "post"}
    SAIDA.parent.mkdir(parents=True, exist_ok=True)
    SAIDA.write_text(json.dumps({"estratos": estratos, "grupos": grupos, "direcao": direcao,
                                 "voz_declarada": vozes, "por_documento": docs}, ensure_ascii=False, indent=1) + "\n")
    print(f"{'métrica':24} {'pré':>7} {'rasc':>7} {'post':>7} {'site':>7} | n  pipe↑ autor↓ volta")
    for k in nomes:
        e = estratos
        dr = direcao.get(k, {})
        print(f"{k:24} {e['pre'][k]!s:>7} {e['rascunho'][k]!s:>7} {e['post'][k]!s:>7} {e['site'][k]!s:>7} | "
              f"{dr.get('posts', ''):2} {dr.get('pipeline_aumenta', ''):5} {dr.get('autor_diminui', ''):6} {dr.get('autor_puxa_de_volta', ''):5}")
    print("voz declarada:", vozes)


if __name__ == "__main__":
    main()
