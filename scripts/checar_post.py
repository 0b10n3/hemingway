#!/usr/bin/env python3
"""Checagem mecânica de um post: o que não precisa de LLM.

  python3 scripts/checar_post.py <slug | caminho/post.md | caminho/publicado.md>

BLOQUEANTE (o gate da etapa 10 não aprova; a colheita aponta no site):
  - marcador do processo no texto: [VERIFICAR, [FAIXA, [PREENCHER, [LINK, [TODO;
  - jargão do pipeline no texto ("na etapa de pesquisa", "post-substack"...);
  - placeholder órfão entre post.md e graficos.md/diagramas.md/infograficos.md (só post.md);
  - frontmatter mínimo ausente (só post.md).
AVISO (vai para a revisão e para o gate, não bloqueia):
  - parágrafo médio ou parágrafo isolado acima do limite;
  - travessão acima do limite por mil palavras, ou em título/subtítulo;
  - H2 com rótulo de movimento ("Fechamento:", "Conclusão");
  - exclamação no corpo (aspas retas não: o Substack converte ao colar);
  - mais de uma antítese "não é X. É Y." na mesma seção;
  - bloco graf-NN sem rangemode="tozero" e sem exceção escrita.

Os limites vêm de estilo/voz.fingerprint.json (metas_publicado): uma fonte só para o número.
Sai com código 1 se houver bloqueante. Só stdlib; usa os blocos de diff_edicoes.py.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import diff_edicoes as D  # noqa: E402

RAIZ = D.RAIZ
METAS = json.loads((RAIZ / "estilo" / "voz.fingerprint.json").read_text())["metas_publicado"]
PALAVRA = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*")
MARCADOR = re.compile(r"(?<!\[)\[(VERIFICAR|FAIXA|PREENCHER|LINK|TODO)\b[^\]\n]{0,120}")
JARGAO = re.compile(r"\bna etapa (?:de |da |\d)|\betapa de (?:pesquisa|verifica\w*|revis\w*|consolida\w*)|"
                    r"\bpost-substack\b|\bprocesso/0\d|\bgate humano\b", re.I)
ROTULO_H2 = re.compile(r"^(fechamento|abertura|gancho|movimento \d+|conclus[ãa]o)\b\s*[:—–-]?", re.I)
ANTITESE = re.compile(r"\bn[ãa]o (?:é|são|há|foi|era|está)\b[^.!?\n]{1,90}[.;]\s+(?:É|São|Há|Foi|Era|Está)\b")
CAMPOS = (("titulo", "título"), ("subtitulo", "subtítulo"), ("data",), ("linha_editorial",), ("status",))


def _resolver(alvo):
    p = Path(alvo)
    if not p.exists():
        p = RAIZ / "posts" / alvo / "post.md"
    if not p.exists():
        raise SystemExit(f"não encontrado: {alvo}")
    return p.resolve()


def checar(caminho):
    """Devolve (bloqueantes, avisos): listas de strings legíveis."""
    texto = caminho.read_text()
    meta, corpo = D.ler_texto(texto)
    eh_post = caminho.name == "post.md"
    bloq, aviso = [], []

    sem_codigo = re.sub(r"```.*?```|\$\$.*?\$\$", " ", corpo, flags=re.S)
    for m in MARCADOR.finditer(sem_codigo):
        bloq.append(f"marcador do processo no texto: {m.group(0)[:80]}")
    for m in JARGAO.finditer(sem_codigo):
        ini = max(m.start() - 40, 0)
        bloq.append(f"jargão do pipeline no texto: …{sem_codigo[ini:m.end() + 30].strip()}…")

    if eh_post:
        for campos in CAMPOS:
            if not any(meta.get(c) for c in campos):
                bloq.append(f"frontmatter sem `{campos[0]}`")
        usados = set(re.findall(r"\]\(((?:graf|diag|info)-\d+)\)", corpo))
        definidos = set()
        for nome in ("graficos.md", "diagramas.md", "infograficos.md"):
            f = caminho.parent / nome
            if f.exists():
                spec = f.read_text()
                definidos |= set(re.findall(r"^##\s+((?:graf|diag|info)-\d+)\b", spec, re.M))
                for bloco in re.split(r"^(?=##\s+graf-\d+)", spec, flags=re.M):
                    nome_bloco = re.match(r"##\s+(graf-\d+)", bloco)
                    if nome_bloco and "rangemode" not in bloco and not re.search(r"exce[çc][ãa]o", bloco, re.I):
                        aviso.append(f"{nome_bloco.group(1)}: sem rangemode=\"tozero\" e sem exceção escrita (Tufte)")
        for p in sorted(usados - definidos):
            bloq.append(f"placeholder sem bloco de spec: {p}")
        for p in sorted(definidos - usados):
            bloq.append(f"bloco de spec sem placeholder no post: {p}")

    bls, _ = D.blocos(corpo)
    pars = [t for tipo, t in bls if tipo == "paragrafo"]
    prosa = " ".join(t for tipo, t in bls if tipo in ("paragrafo", "item"))
    palavras = len(PALAVRA.findall(re.sub(r"\]\([^)]*\)", "]", prosa))) or 1
    tamanhos = [len(PALAVRA.findall(p)) for p in pars]
    lim_par = METAS["paragrafo_media_palavras"]
    if tamanhos and sum(tamanhos) / len(tamanhos) > lim_par["aviso_acima"]:
        aviso.append(f"parágrafo médio de {sum(tamanhos) / len(tamanhos):.0f} palavras "
                     f"(alvo ~{lim_par['alvo']}; regra 1)")
    for p, n in zip(pars, tamanhos):
        if n > lim_par["maximo_paragrafo"]:
            aviso.append(f"parágrafo de {n} palavras: «{p[:60]}…» (regra 1)")

    tracos = prosa.count("—") + len(re.findall(r"\s[–-]\s", prosa))
    lim_tr = METAS["travessao_por_mil"]
    if 1000 * tracos / palavras > lim_tr["aviso_acima"]:
        aviso.append(f"travessão: {1000 * tracos / palavras:.1f} por mil palavras (alvo ≤{lim_tr['alvo']}; regra 3)")
    titulos = [t for tipo, t in bls if tipo == "titulo"] + [str(meta.get(c, "")) for c in
                                                           ("titulo", "título", "subtitulo", "subtítulo")]
    for t in titulos:
        if "—" in t or re.search(r"\s[–-]\s", t):
            aviso.append(f"travessão em título ou subtítulo: «{t[:70]}» (regra 3)")
        if t and ROTULO_H2.match(t.strip()):
            aviso.append(f"H2 com rótulo de movimento: «{t[:70]}» (regra 5)")

    exclamacoes = re.sub(r"!\[", "", prosa).count("!")
    if exclamacoes:
        aviso.append(f"exclamação no corpo: {exclamacoes} (regra 6)")

    secoes = re.split(r"^#{2,3}\s.*$", re.sub(r"```.*?```", " ", corpo, flags=re.S), flags=re.M)
    for i, sec in enumerate(secoes):
        achadas = ANTITESE.findall(sec)
        if len(achadas) > 1:
            aviso.append(f"{len(achadas)} antíteses 'não é X. É Y.' na seção {i} (teto: ~1 por seção; regra 20)")
    return bloq, aviso


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    caminho = _resolver(sys.argv[1])
    bloq, aviso = checar(caminho)
    print(f"checar_post: {caminho.relative_to(RAIZ)}")
    for b in bloq:
        print(f"  BLOQUEANTE  {b}")
    for a in aviso:
        print(f"  aviso       {a}")
    if not bloq and not aviso:
        print("  ok")
    sys.exit(1 if bloq else 0)


if __name__ == "__main__":
    main()
