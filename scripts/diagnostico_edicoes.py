#!/usr/bin/env python3
"""Diagnóstico da Fase B do épico de revisão editorial (somente leitura).

  python3 scripts/diagnostico_edicoes.py atribuicao   # B1: que etapa escreveu o que o autor desfaz
  python3 scripts/diagnostico_edicoes.py antislop     # B2: o que o pipeline escreve muito mais que o autor

Lê o corpus da Fase A (estilo/corpus/) e o histórico do git; grava JSON em
pesquisa/epico-revisao-editorial/dados/. Não altera nada no pipeline.

B1 reconstrói, para cada token do post.md que serviu de base à publicação, a etapa que o
escreveu: rascunho -> etapa 4 (último 04-draft-v*) -> etapas 6–9 (post.md no commit da
consolidação) -> etapa 10 (gate e parecer). O trecho escrito entre 6 e 9 é atribuído à etapa 6
ou 7 quando aparece no laudo dela (06-revisao*, 07-verificacao*), e à 9 nos demais casos.

B2 compara n-gramas (1 a 4 tokens, pontuação incluída) do texto escrito pelo pipeline com o
texto só do autor: rascunhos de verdade, posts anteriores ao pipeline e acréscimos autorais.
Exige dispersão (o n-grama aparece em vários posts) para não confundir tema com tique.
"""
import json
import math
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diff_edicoes as D  # noqa: E402

RAIZ = D.RAIZ
DADOS = RAIZ / "pesquisa" / "epico-revisao-editorial" / "dados"
MAPA = json.loads(D.MAPA.read_text())


def git(*args):
    return subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True)


def mostrar(commit, caminho):
    if commit in (None, "atual"):
        p = RAIZ / caminho
        return p.read_text() if p.exists() else None
    r = git("show", f"{commit}:{caminho}")
    return r.stdout if r.returncode == 0 else None


def corpo_post(texto):
    corpo = D.ler_texto(texto)[1]
    h1 = re.match(r"\s*# ([^\n]+)\n", corpo)
    return corpo[h1.end():] if h1 else corpo


def toks(texto, post=True):
    return D.tokens(corpo_post(texto) if post else D.ler_texto(texto)[1])[0] if texto else []


def mapa_iguais(origem, destino):
    """índice no destino -> índice na origem, para tokens iguais."""
    m = {}
    for tag, i1, i2, j1, j2 in D.alinhar(origem, destino):
        if tag == "equal":
            for d in range(i2 - i1):
                m[j1 + d] = i1 + d
    return m


def palavras(ts):
    return " " + " ".join(t["n"] for t in ts if t["pal"]) + " "


# ---------------------------------------------------------------- versões de um post

def versoes(item):
    slug = item["slug_repo"]
    ed = json.loads((D.SAIDA / f"{slug}.json").read_text())
    base = ed["post_md_base"]["commit"]
    ref = "HEAD" if base == "atual" else base
    v9_commit = None
    for linha in git("log", "--format=%h %s", ref, "--", f"posts/{slug}/post.md").stdout.splitlines():
        h, assunto = linha.split(" ", 1)
        if re.search(r"consolida|etapa 9\b|montagem", assunto, re.I) and not re.search(r"9a|parecer", assunto, re.I):
            v9_commit = h
            break
    arquivos = git("ls-tree", "--name-only", ref, f"posts/{slug}/processo/").stdout.split()
    drafts = sorted((f for f in arquivos if re.search(r"/04-draft-v\d+\.md$", f)),
                    key=lambda f: int(re.search(r"v(\d+)\.md$", f).group(1)))
    laudo = lambda padrao: " ".join(  # noqa: E731
        palavras(toks(mostrar(ref if base != "atual" else "atual", f), post=False))
        for f in arquivos if re.search(padrao, f))
    return {
        "ed": ed, "base_commit": base, "v9_commit": v9_commit, "v4_arquivo": drafts[-1] if drafts else None,
        "rasc": toks((RAIZ / item["rascunho"]).read_text(), post=False),
        "v4": toks(mostrar(ref if base != "atual" else "atual", drafts[-1])) if drafts else [],
        "v9": toks(mostrar(v9_commit, f"posts/{slug}/post.md")) if v9_commit else [],
        "base": toks(mostrar(base, f"posts/{slug}/post.md")),
        "pub": D.tokens(D.ler(f"estilo/corpus/publicados/{item['slug_site']}.md")[1])[0],
        "laudo6": laudo(r"/06-revis"), "laudo7": laudo(r"/07-verif"),
    }


def proveniencia(v):
    """Rótulo da etapa que escreveu cada token da base, e os mapas da cadeia."""
    rasc, v4, v9, base = v["rasc"], v["v4"], v["v9"], v["base"]
    lab_r = ["rascunho"] * len(rasc)
    m4r = mapa_iguais(rasc, v4) if v4 else {}
    lab4 = [lab_r[m4r[j]] if j in m4r else "etapa 4" for j in range(len(v4))]
    if v9:
        orig, lab_orig, novo = (v4, lab4, "etapas 6–9") if v4 else (rasc, lab_r, "etapas 4–9")
        m9 = mapa_iguais(orig, v9)
        lab9 = [lab_orig[m9[j]] if j in m9 else novo for j in range(len(v9))]
        mb9 = mapa_iguais(v9, base)
        lab = [lab9[mb9[j]] if j in mb9 else "etapa 10" for j in range(len(base))]
    else:
        m9, mb9 = {}, mapa_iguais(v4, base) if v4 else mapa_iguais(rasc, base)
        lab_orig = lab4 if v4 else lab_r
        lab = [lab_orig[mb9[j]] if j in mb9 else "etapas 6–10" for j in range(len(base))]
    # etapas 6–9: atribui à 6 ou à 7 quando o trecho aparece no laudo da etapa
    k = 0
    while k < len(lab):
        if lab[k] != "etapas 6–9":
            k += 1
            continue
        fim = k
        while fim < len(lab) and lab[fim] == "etapas 6–9":
            fim += 1
        janela = base[k:fim]
        if sum(t["pal"] for t in janela) < 3:
            janela = base[max(k - 3, 0):min(fim + 3, len(base))]
        alvo = palavras(janela)
        rotulo = ("etapa 6" if len(alvo.split()) >= 3 and alvo in v["laudo6"] else
                  "etapa 7" if len(alvo.split()) >= 3 and alvo in v["laudo7"] else "etapa 9")
        for j in range(k, fim):
            lab[j] = rotulo
        k = fim
    return lab, {"m4r": m4r, "m94": m9 if v9 else {}, "mb9": mb9}


def atribuicao():
    ORDEM = ["rascunho", "etapa 4", "etapa 6", "etapa 7", "etapa 9", "etapa 10", "etapas 4–9", "etapas 6–10"]
    total = {"palavras": defaultdict(lambda: [0, 0]), "travessao": defaultdict(lambda: [0, 0]),
             "aspas_simples": defaultdict(lambda: [0, 0])}
    matriz, negrito, por_post = Counter(), Counter(), []
    for item in (i for i in MAPA if i["slug_repo"]):
        v = versoes(item)
        lab, mapas = proveniencia(v)
        base, pub = v["base"], v["pub"]
        vivo = set(mapa_iguais(base, pub).values())  # índices da base que sobrevivem no site
        sob = {"palavras": defaultdict(lambda: [0, 0]), "travessao": defaultdict(lambda: [0, 0]),
               "aspas_simples": defaultdict(lambda: [0, 0])}
        for k, t in enumerate(base):
            chave = "palavras" if t["pal"] else "travessao" if t["n"] == "—" else \
                "aspas_simples" if t["r"] in ("'", "‘", "’") else None
            if chave and t["tb"] != "titulo":
                for d in (sob[chave], total[chave]):
                    d[lab[k]][0] += 1
                    d[lab[k]][1] += k in vivo
        for op in v["ed"]["operacoes"]:
            pos = op.get("pos_antes")
            if op["natureza"] != "estilo" or not pos:
                continue
            i1, i2 = pos
            faixa = lab[i1:i2] or lab[max(i1 - 1, 0):i1]
            if op["classe"] in ("negrito_adicionado", "italico_adicionado"):
                if op["restaurou_rascunho"]:
                    attr = "b" if op["classe"].startswith("negrito") else "i"
                    j9 = mapas["mb9"].get(i1)
                    j4 = mapas["m94"].get(j9) if j9 is not None else None
                    quem = "etapas 6–9" if (j4 is not None and v["v4"][j4][attr]) else "etapa 4"
                    rot = f"devolve o que a {quem} tirou"
                else:
                    rot = "novo (autor)"
                negrito[(op["classe"], rot)] += 1
                continue
            if op["classe"] == "divisao_paragrafo":
                rot = "rascunho" if all(x == "rascunho" for x in faixa[:1] + faixa[-1:]) else Counter(faixa).most_common(1)[0][0]
            else:
                rot = Counter(faixa).most_common(1)[0][0] if faixa else "?"
            matriz[(op["classe"], rot)] += 1
        por_post.append({"slug_repo": item["slug_repo"], "rascunho_tipo": item["rascunho_tipo"],
                         "base_commit": v["base_commit"], "v9_commit": v["v9_commit"], "v4_arquivo": v["v4_arquivo"],
                         "tokens_por_etapa": dict(Counter(lab)),
                         "sobrevivencia": {c: dict(d) for c, d in sob.items()}})
    def taxa(d):
        return {k: {"total": n, "sobrevive": s, "taxa": round(s / n, 3) if n else None}
                for k, (n, s) in sorted(d.items(), key=lambda kv: ORDEM.index(kv[0]) if kv[0] in ORDEM else 99)}
    saida = {"sobrevivencia": {c: taxa(d) for c, d in total.items()},
             "matriz_classe_etapa": [{"classe": c, "etapa": e, "n": n} for (c, e), n in sorted(matriz.items())],
             "enfase_adicionada": [{"classe": c, "origem": e, "n": n} for (c, e), n in sorted(negrito.items())],
             "por_post": por_post}
    DADOS.mkdir(parents=True, exist_ok=True)
    (DADOS / "b1-atribuicao.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n")
    for c, d in saida["sobrevivencia"].items():
        print(c, {k: f"{x['sobrevive']}/{x['total']} ({x['taxa']})" for k, x in d.items()})
    print("matriz:", sorted(matriz.items(), key=lambda kv: -kv[1])[:30])
    print("ênfase:", dict(negrito))


# ---------------------------------------------------------------- B2: antislop calibrado pelo autor

SONDAS = {  # frente D (pesquisa/frente-d-antipadroes-ia-ptbr.md) + construções observadas na Fase A
    "D1 abertura clichê": r"\bno mundo (atual|de hoje)|cenário cada vez mais|vivemos (em )?uma era|desde os primórdios",
    "D2 conectivo formal": r"\b(além disso|não obstante|vale ressaltar|cabe destacar|dessa forma|desse modo|"
                           r"é importante (ressaltar|destacar|notar)|é fundamental destacar|portanto)\b",
    "D3 tríade 'x, y e z'": r"\b\w{4,}, \w{4,} e \w{4,}\b",
    "D4 hedging": r"\b(pode-se dizer|de certa (forma|maneira)|em certa medida|até certo ponto)\b",
    "D5 fecho genérico": r"\b(em resumo|em suma|concluindo|diante do exposto)\b",
    "D7 adjetivo vazio": r"\b(crucial|fundamental|essencial|vital|notável|significativ[oa]s?|robust[oa]s?|abrangente|holístic[oa])\b",
    "D8 passiva analítica": r"\b(foi|foram|é|são) (constatad|realizad|observad|verificad|considerad)[oa]s?\b",
    "D9 analogia genérica": r"\b(quebra-cabeça|jornada|ensinar a pescar)\b",
    "D11 pergunta-muleta": r"\b(o que isso significa|será que|por que isso importa|como resolver isso)\b",
    "D12 léxico de IA": r"\b(mergulh\w+|panorama|cenário|moldar|molda)\b",
    "D12 'não é x, é y'": r"\bnão (é|são) (apenas |só |um |uma )?[^.,;:?!]{1,40}[,.;—] *(é|são|mas)\b",
    "D12 gerúndio pendurado": r", \w+ndo\b[^.;:?!]{0,60}[.]",
    "A travessão": r"—",
    "A dois-pontos": r":",
    "A aspas simples de ênfase": r"(?<![\w’'])['‘][^'‘’\n]{2,40}['’](?!\w)",
    "A 'é justamente/exatamente'": r"\b(é|está) (justamente|exatamente|precisamente)\b",
    "A 'ou seja / isto é'": r"\b(ou seja|isto é)\b",
    "A 'na prática'": r"\bna prática\b",
    "A 'o ponto é / a questão é'": r"\b(o ponto|a questão|a pergunta|a resposta) (é|está)\b",
}


def _textos_autor(so_rascunhos=False):
    """Texto só do autor. so_rascunhos=True controla o tema: só os rascunhos dos mesmos posts."""
    docs = []
    for item in MAPA:
        if item["epoca"] == "pre-pipeline" and not so_rascunhos:
            docs.append((item["slug_site"], D.tokens(D.ler(f"estilo/corpus/publicados/{item['slug_site']}.md")[1])[0]))
        elif item["rascunho_tipo"] == "rascunho":
            docs.append((item["slug_repo"], D.tokens(D.ler(item["rascunho"])[1])[0]))
    for f in sorted(D.SAIDA.glob("2026-*.json")):  # acréscimos autorais
        ed = json.loads(f.read_text())
        for op in ed["operacoes"]:
            if "acrescimo_autoral" in op["sinais"] and op["natureza"] == "estilo":
                docs.append((ed["slug_repo"], D.tokens(op["depois"])[0]))
    return docs


def _ngramas(seq, n):
    return (tuple(seq[i:i + n]) for i in range(len(seq) - n + 1))


def antislop():
    pipe_segs = []  # (post, tokens de um trecho contínuo escrito pelo pipeline)
    for item in (i for i in MAPA if i["slug_repo"]):
        v = versoes(item)
        lab, _ = proveniencia(v)
        vivo = set(mapa_iguais(v["base"], v["pub"]).values())
        atual = []
        for k, (t, l) in enumerate(zip(v["base"], lab)):
            if l != "rascunho" and t["tb"] not in ("titulo",):
                atual.append({**t, "vivo": k in vivo})
            elif atual:
                pipe_segs.append((item["slug_repo"], atual)); atual = []
        if atual:
            pipe_segs.append((item["slug_repo"], atual))
    sobrevive = Counter()  # n-grama do pipeline que ficou inteiro no site
    for _, ts in pipe_segs:
        ts = [t for t in ts if t["n"] not in ("'", '"') and not t["n"].startswith("⟦")]
        for n in range(1, 5):
            for i in range(len(ts) - n + 1):
                if all(t["vivo"] for t in ts[i:i + n]):
                    sobrevive[tuple(t["n"] for t in ts[i:i + n])] += 1
    autor = _textos_autor()
    rascunhos = _textos_autor(so_rascunhos=True)

    def contar(docs):
        c, onde, total, palavras_ = Counter(), defaultdict(set), 0, 0
        for doc, ts in docs:
            seq = [t["n"] for t in ts if t["n"] not in ("'", '"') and not t["n"].startswith("⟦")]
            total += len(seq)
            palavras_ += sum(t["pal"] for t in ts)
            for n in range(1, 5):
                for g in _ngramas(seq, n):
                    c[g] += 1
                    onde[g].add(doc)
        return c, onde, total, palavras_

    cp, op_, np_, wp = contar(pipe_segs)
    ca, oa, na, wa = contar(autor)
    cr, or_, nr, _ = contar(rascunhos)

    def listas(ca, oa, na):
        razao = lambda g: ((cp[g] + 0.5) / np_) / ((ca[g] + 0.5) / na)  # noqa: E731
        sobre = [g for g in cp if cp[g] >= 6 and len(op_[g]) >= 4 and not any(re.search(r"\d", x) for x in g)
                 and razao(g) >= 3]
        sob = [g for g in ca if ca[g] >= 8 and len(oa[g]) >= 4 and not any(re.search(r"\d", x) for x in g)
               and razao(g) <= 1 / 3]
        fmt = lambda g: {"ngrama": " ".join(g), "pipeline": cp[g], "autor": ca[g], "posts_pipeline": len(op_[g]),  # noqa: E731
                         "posts_autor": len(oa[g]), "razao": round(razao(g), 2),
                         "sobrevive_no_site": round(sobrevive[g] / cp[g], 2) if cp[g] else None}
        sobre.sort(key=lambda g: -razao(g) * math.log(cp[g]))
        sob.sort(key=lambda g: razao(g) / math.log(ca[g]))
        return [fmt(g) for g in sobre[:80]], [fmt(g) for g in sob[:60]]

    sobre_todos, sub_todos = listas(ca, oa, na)
    sobre_ctrl, sub_ctrl = listas(cr, or_, nr)
    # lista calibrada: o pipeline escreve muito mais que o autor E o autor corta no site
    calibrada = [x for x in sobre_ctrl if x["sobrevive_no_site"] is not None and x["sobrevive_no_site"] < 0.7]

    texto_pipe = " ".join(D.juntar(ts) for _, ts in pipe_segs)
    texto_autor = " ".join(D.juntar(ts) for _, ts in autor)
    texto_site = " ".join(D.juntar(D.tokens(D.ler(f"estilo/corpus/publicados/{i['slug_site']}.md")[1])[0])
                          for i in MAPA if i["slug_repo"])
    wsite = len(re.findall(r"[^\W\d_]+", texto_site))
    sondas = []
    for nome, padrao in SONDAS.items():
        rx = re.compile(padrao, re.I)
        a, b, s = len(rx.findall(texto_pipe)), len(rx.findall(texto_autor)), len(rx.findall(texto_site))
        sondas.append({"sonda": nome, "pipeline_por_mil": round(1000 * a / wp, 2), "autor_por_mil": round(1000 * b / wa, 2),
                       "site_pipeline_por_mil": round(1000 * s / wsite, 2), "pipeline_n": a, "autor_n": b,
                       "razao": round(((a + 0.5) / wp) / ((b + 0.5) / wa), 2)})
    saida = {"tamanho": {"pipeline_palavras": wp, "autor_palavras": wa, "site_pipeline_palavras": wsite,
                         "trechos_pipeline": len(pipe_segs), "docs_autor": len(autor)},
             "sondas": sondas,
             "lista_calibrada": {"criterio": "razão >= 3 contra os rascunhos dos mesmos posts, em >= 4 posts, "
                                              "e < 70% das ocorrências inteiras no site", "itens": calibrada},
             "controlado_por_tema": {"descricao": "pipeline x rascunhos dos mesmos 13 posts (+ acréscimos)",
                                     "sobre_representados": sobre_ctrl, "sub_representados": sub_ctrl},
             "contra_todo_o_autor": {"descricao": "pipeline x rascunhos + 15 posts pré-pipeline + acréscimos",
                                     "sobre_representados": sobre_todos, "sub_representados": sub_todos}}
    DADOS.mkdir(parents=True, exist_ok=True)
    (DADOS / "b2-antislop.json").write_text(json.dumps(saida, ensure_ascii=False, indent=1) + "\n")
    print(saida["tamanho"])
    for s in sondas:
        print(f"{s['sonda']:30} pipe={s['pipeline_por_mil']:6} autor={s['autor_por_mil']:6} site={s['site_pipeline_por_mil']:6} razão={s['razao']}")
    print("CALIBRADA:", [(x["ngrama"], x["pipeline"], x["autor"], x["razao"], x["sobrevive_no_site"]) for x in calibrada])
    c = saida["controlado_por_tema"]
    print("SOBRE (controlado):", [(x["ngrama"], x["pipeline"], x["autor"], x["razao"]) for x in c["sobre_representados"][:50]])
    print("SUB (controlado):", [(x["ngrama"], x["pipeline"], x["autor"], x["razao"]) for x in c["sub_representados"][:40]])


if __name__ == "__main__":
    {"atribuicao": atribuicao, "antislop": antislop}.get(sys.argv[1] if len(sys.argv) > 1 else "",
                                                         lambda: sys.exit(__doc__))()
