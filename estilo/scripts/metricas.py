#!/usr/bin/env python3
"""Camada quantitativa da forja de voz — ver estilo/estilo-autoral.md §metodologia.

Lê _arquivo/amostras/proprias/**, calcula métricas por texto e agregadas
(geral + por gênero), grava estilo/metricas.json. Python puro (stdlib), sem
dependência de pacote pip. PDFs são convertidos via o binário `pdftotext`
(poppler-utils) por subprocess — se ausente, o arquivo é listado em
"arquivos_pulados" e o resto do corpus segue normalmente.

Todas as métricas aqui são heurísticas de regex, não análise linguística
real (não há tokenizador ou parser sintático). Servem para ancorar o
julgamento qualitativo dos extratores (Fase 2.2), não como medição
definitiva — eixos marcados "aproximado" no relatório devem ser lidos com
essa reserva, sobretudo passiva e siglas.

Uso: python3 estilo/scripts/metricas.py
"""

import json
import re
import statistics
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CORPUS_DIR = REPO_ROOT / "_arquivo" / "amostras" / "proprias"
OUT_PATH = REPO_ROOT / "estilo" / "metricas.json"

WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:'[A-Za-zÀ-ÖØ-öø-ÿ]+)?")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?…])\s+(?=[A-ZÀ-Ú0-9\"“(])")
NUMBER_RE = re.compile(r"\d+(?:[.,]\d+)*%?")
ACRONYM_RE = re.compile(r"\b[A-ZÀ-Ú]{2,}S?\b")
HEADER_RE = re.compile(r"^#{1,6}\s+.+$", re.MULTILINE)
IMAGE_PLACEHOLDER_RE = re.compile(r"<!--\s*image\s*-->", re.IGNORECASE)

CONECTIVOS = [
    "além disso", "portanto", "no entanto", "contudo", "porém", "todavia",
    "por outro lado", "ou seja", "isto é", "por exemplo", "na verdade",
    "de fato", "ainda assim", "mesmo assim", "apesar de", "embora",
    "assim sendo", "dessa forma", "desse modo", "em suma", "enfim",
    "logo", "consequentemente", "ademais", "outrossim",
]
CONTRA_ARGUMENTO = [
    "mas", "porém", "contudo", "no entanto", "ainda que", "apesar de",
    "por outro lado", "todavia", "ao contrário", "entretanto",
]
FORMULA_HINTS = re.compile(r"[=∑∫√≤≥≈±]|\$[^$]+\$|\\frac|\\sum|\\int")
PASSIVA_RE = re.compile(
    r"\b(?:foi|foram|é|são|era|eram|será|serão|sendo|seja|sejam)\s+\w*(?:ad[oa]s?|id[oa]s?)\b",
    re.IGNORECASE,
)
PRIMEIRA_SING_RE = re.compile(r"\b(eu|meu|minha|meus|minhas|comigo|me)\b", re.IGNORECASE)
PRIMEIRA_PLUR_RE = re.compile(r"\b(nós|nosso|nossa|nossos|nossas|conosco|nos)\b", re.IGNORECASE)


def extrair_texto_pdf(caminho: Path) -> str | None:
    try:
        resultado = subprocess.run(
            ["pdftotext", "-layout", str(caminho), "-"],
            capture_output=True, text=True, timeout=60, check=True,
        )
        return resultado.stdout
    except (FileNotFoundError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return None


def limpar_markdown(texto: str) -> str:
    texto = IMAGE_PLACEHOLDER_RE.sub("", texto)
    texto = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", texto)  # imagens md
    texto = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", texto)  # links -> texto
    return texto


def blocos_entre_headers(texto: str) -> list[int]:
    posicoes = [m.start() for m in HEADER_RE.finditer(texto)]
    if not posicoes:
        return []
    posicoes.append(len(texto))
    tamanhos = []
    for i in range(len(posicoes) - 1):
        trecho = texto[posicoes[i]:posicoes[i + 1]]
        trecho_sem_header = HEADER_RE.sub("", trecho, count=1)
        n = len(WORD_RE.findall(trecho_sem_header))
        if n > 0:
            tamanhos.append(n)
    return tamanhos


def percentil(dados: list[float], p: float) -> float:
    if not dados:
        return 0.0
    dados_ordenados = sorted(dados)
    k = (len(dados_ordenados) - 1) * p
    f, c = int(k), min(int(k) + 1, len(dados_ordenados) - 1)
    if f == c:
        return dados_ordenados[f]
    return dados_ordenados[f] + (dados_ordenados[c] - dados_ordenados[f]) * (k - f)


def contar_ocorrencias(texto_lower: str, termos: list[str]) -> int:
    return sum(len(re.findall(r"\b" + re.escape(t) + r"\b", texto_lower)) for t in termos)


def metricas_de_texto(texto_bruto: str, is_markdown: bool) -> dict:
    texto = limpar_markdown(texto_bruto) if is_markdown else texto_bruto
    palavras = WORD_RE.findall(texto)
    n_palavras = len(palavras)
    palavras_lower = [p.lower() for p in palavras]
    texto_lower = texto.lower()

    frases = [f.strip() for f in SENTENCE_SPLIT_RE.split(texto) if f.strip()]
    tam_frases = [len(WORD_RE.findall(f)) for f in frases if WORD_RE.findall(f)]

    paragrafos = [p.strip() for p in re.split(r"\n\s*\n", texto) if p.strip()]
    tam_paragrafos = [len(WORD_RE.findall(p)) for p in paragrafos if WORD_RE.findall(p)]

    tipos = set(palavras_lower)
    freq = {}
    for p in palavras_lower:
        freq[p] = freq.get(p, 0) + 1
    hapax = sum(1 for c in freq.values() if c == 1)

    por_mil = (lambda n: round(n / n_palavras * 1000, 2)) if n_palavras else (lambda n: 0.0)

    pontuacao = {
        sinal: por_mil(texto.count(sinal))
        for sinal in [".", ",", ";", ":", "—", "-", "(", ")", '"', "!", "?", "…"]
    }

    blocos = blocos_entre_headers(texto) if is_markdown else []

    return {
        "palavras": n_palavras,
        "frases": {
            "total": len(tam_frases),
            "mediana": statistics.median(tam_frases) if tam_frases else 0,
            "p10": round(percentil(tam_frases, 0.10), 1),
            "p90": round(percentil(tam_frases, 0.90), 1),
            "desvio_padrao": round(statistics.pstdev(tam_frases), 2) if len(tam_frases) > 1 else 0.0,
        },
        "paragrafos": {
            "total": len(tam_paragrafos),
            "media_palavras": round(statistics.mean(tam_paragrafos), 1) if tam_paragrafos else 0,
        },
        "lexico": {
            "type_token_ratio": round(len(tipos) / n_palavras, 4) if n_palavras else 0.0,
            "hapax_legomena": hapax,
            "hapax_por_mil": por_mil(hapax),
        },
        "pontuacao_por_mil_palavras": pontuacao,
        "conectivos_por_mil": por_mil(contar_ocorrencias(texto_lower, CONECTIVOS)),
        "marcadores_contra_argumento_por_mil": por_mil(contar_ocorrencias(texto_lower, CONTRA_ARGUMENTO)),
        "primeira_pessoa": {
            "singular_por_mil": por_mil(len(PRIMEIRA_SING_RE.findall(texto))),
            "plural_por_mil": por_mil(len(PRIMEIRA_PLUR_RE.findall(texto))),
        },
        "perguntas_por_mil": por_mil(texto.count("?")),
        "numeros_por_mil": por_mil(len(NUMBER_RE.findall(texto))),
        "siglas_por_mil": por_mil(len(ACRONYM_RE.findall(texto))),
        "indicios_formula_por_mil": por_mil(len(FORMULA_HINTS.findall(texto))),
        "voz_passiva_aproximada_por_mil": por_mil(len(PASSIVA_RE.findall(texto))),
        "bloco_medio_antes_de_subtitulo": {
            "n_blocos": len(blocos),
            "media_palavras": round(statistics.mean(blocos), 1) if blocos else None,
        },
    }


def agregar(lista_metricas: list[dict]) -> dict:
    if not lista_metricas:
        return {}
    total_palavras = sum(m["palavras"] for m in lista_metricas)

    def media_ponderada(caminho_chaves):
        valores, pesos = [], []
        for m in lista_metricas:
            v = m
            for k in caminho_chaves:
                v = v[k]
            if v is not None:
                valores.append(v)
                pesos.append(m["palavras"])
        if not valores:
            return None
        return round(sum(v * w for v, w in zip(valores, pesos)) / sum(pesos), 2) if sum(pesos) else None

    return {
        "textos": len(lista_metricas),
        "palavras_total": total_palavras,
        "frase_mediana_media_ponderada": media_ponderada(["frases", "mediana"]),
        "frase_desvio_padrao_media_ponderada": media_ponderada(["frases", "desvio_padrao"]),
        "paragrafo_media_palavras_media_ponderada": media_ponderada(["paragrafos", "media_palavras"]),
        "type_token_ratio_media": media_ponderada(["lexico", "type_token_ratio"]),
        "conectivos_por_mil_media": media_ponderada(["conectivos_por_mil"]),
        "marcadores_contra_argumento_por_mil_media": media_ponderada(["marcadores_contra_argumento_por_mil"]),
        "primeira_pessoa_singular_por_mil_media": media_ponderada(["primeira_pessoa", "singular_por_mil"]),
        "primeira_pessoa_plural_por_mil_media": media_ponderada(["primeira_pessoa", "plural_por_mil"]),
        "perguntas_por_mil_media": media_ponderada(["perguntas_por_mil"]),
        "numeros_por_mil_media": media_ponderada(["numeros_por_mil"]),
        "siglas_por_mil_media": media_ponderada(["siglas_por_mil"]),
        "voz_passiva_aproximada_por_mil_media": media_ponderada(["voz_passiva_aproximada_por_mil"]),
    }


def main() -> int:
    if not CORPUS_DIR.exists():
        print(f"Diretório não encontrado: {CORPUS_DIR}", file=sys.stderr)
        return 1

    por_arquivo = {}
    por_genero: dict[str, list[dict]] = {}
    pulados = []

    arquivos = sorted(
        p for p in CORPUS_DIR.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".pdf"} and p.name != ".gitkeep"
    )

    for caminho in arquivos:
        genero = caminho.relative_to(CORPUS_DIR).parts[0]
        rel = str(caminho.relative_to(REPO_ROOT))

        if caminho.suffix.lower() == ".pdf":
            texto = extrair_texto_pdf(caminho)
            if texto is None:
                pulados.append({"arquivo": rel, "motivo": "pdftotext indisponível ou falhou"})
                continue
            m = metricas_de_texto(texto, is_markdown=False)
        else:
            texto = caminho.read_text(encoding="utf-8")
            m = metricas_de_texto(texto, is_markdown=True)

        m["genero"] = genero
        por_arquivo[rel] = m
        por_genero.setdefault(genero, []).append(m)

    saida = {
        "gerado_por": "estilo/scripts/metricas.py",
        "metodologia": (
            "Heurísticas de regex sobre stdlib Python, sem NLP real. "
            "Ancoragem quantitativa para a extração qualitativa (subagente "
            "extrator-de-estilo), não medição linguística definitiva."
        ),
        "arquivos_pulados": pulados,
        "por_arquivo": por_arquivo,
        "agregado_geral": agregar(list(por_arquivo.values())),
        "agregado_por_genero": {g: agregar(ms) for g, ms in por_genero.items()},
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(saida, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {len(por_arquivo)} arquivo(s) processado(s), {len(pulados)} pulado(s).")
    print(f"Escrito em {OUT_PATH.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
