# Gráficos — O Mundo Invertido dos Investimentos

## graf-01 — A régua da corrida

**Pergunta que o gráfico responde:** qual é a ordem natural de progressão de risco dos
produtos de investimento, mapeada à distância de uma corrida (5km → ultramaratona)?

**Fonte dos dados:** a régua em si (rung, distância, produto, posição ordinal de risco) é
elaboração própria a partir da analogia do autor — ver `_arquivo/transcricoes/2026-08-10_O_Mundo_Invertido_dos_Investimentos.md`
e `posts/2026-08-10-o-mundo-invertido-dos-investimentos/processo/02-estrutura.md`. A escala
de risco é ordinal e ilustrativa (1 a 5), não uma medida de mercado — o eixo x não representa
volatilidade nem qualquer métrica calculada.

A anotação sobre "onde a maioria dos iniciantes de fato entra" cita dado com fonte externa,
já confirmado em `processo/07-verificacao.md` §1: Chague & Giovannetti (2025), "As pandemias
de COVID-19 e de day trade no Brasil", *Revista Brasileira de Finanças* 23, e202515 —
968.512 pessoas fizeram day trade em contratos futuros entre 2020-2023, perda agregada de
R$ 9,9 bilhões. Acesso: 2026-08-10.
https://portal.fgv.br/en/noticias/brazilians-lost-r-99-billion-day-trade-during-covid-19-pandemic-according-study-fgv-eesp

**Dados:** `graficos/dados/graf-01.csv` (versionado junto a este arquivo).

**Escolha de tipo de gráfico:** barra horizontal, uma barra por degrau da régua, ordenada da
distância mais curta (base) à mais longa (topo) — escolhida porque o eixo y categórico com
rótulo de distância comunica a "escada" de forma mais direta que um scatter ou um gráfico de
linha (que sugeririam uma variável contínua, quando a régua é uma sequência ordinal de
categorias). Descartado: gráfico de pizza/rosca (não há "parte de um todo" aqui, é uma
progressão) e treemap (esconderia a ordem, que é o ponto central do gráfico).

**Cor:** gradiente de risco interpolado em espaço OKLab entre três âncoras que já existem em
`marca/tokens.json` — `functional.success` (baixo risco), `functional.warning` (risco médio)
e `functional.error` (risco alto) — sem nenhum hex novo inventado fora do arquivo de tokens.
A interpolação é feita em OKLab (não em RGB ingênuo) porque é para isso que o `tokens.json`
já publica o valor `oklch` de cada cor.

**Anotação:** dois pontos de interesse, com `add_annotation` apontando diretamente para cada
um (não só legenda) — o topo da régua (onde os dados de day trade mostram que a maioria dos
iniciantes de fato entra) e a base (onde a régua recomenda começar). É contraste genuíno, não
forçado: são dois estados reais e distintos (prescrito pela analogia vs. observado nos dados),
não um "antes/depois" artificial sobre um fenômeno que não tem dois estados.

**Alt-text:** "Gráfico de barras horizontais mostrando a régua de risco de investimento
mapeada à distância de corrida: de 5-10km (crédito bancário e Tesouro, risco 1, verde) até
maratona/ultramaratona (derivativos e day trade, risco 5, vermelho), passando por ETFs de
renda fixa, fundos e ações. Uma anotação no topo destaca que 968.512 pessoas fizeram day
trade no Brasil entre 2020-2023, com perda agregada de R$ 9,9 bilhões — indicando que é ali,
no degrau de maior risco, que a maioria dos iniciantes de fato começa, ao contrário do ponto
de entrada recomendado na base da régua."

**Legenda (para usar sob o gráfico em `post.md`):** "A régua de risco dos investimentos,
mapeada à distância de uma corrida — e o abismo entre onde a maioria começa e onde deveria."

### Código (autocontido, testado com `python3`)

Salvo em `graficos/graf-01.py`, lê `graficos/dados/graf-01.csv` e `marca/tokens.json`, exporta
para `figuras/graf-01.svg` e `figuras/graf-01.png`. Testado nesta etapa com Python 3.14 +
Plotly 6.9 + Kaleido — roda sozinho, sem preâmbulo, com `python3 graf-01.py` a partir de
`graficos/`.

```python
"""
graf-01 — A régua da corrida.
Autocontido: lê o CSV ao lado (dados/graf-01.csv) e os tokens de marca/tokens.json,
exporta para ../figuras/graf-01.svg e .png. Rodar com: python3 graf-01.py
"""
import csv
import json
import math
import textwrap
from pathlib import Path

import plotly.graph_objects as go

SCRIPT_DIR = Path(__file__).resolve().parent          # posts/<slug>/graficos
SLUG_DIR = SCRIPT_DIR.parent                           # posts/<slug>
REPO_ROOT = SLUG_DIR.parent.parent                     # raiz do repo
TOKENS_PATH = REPO_ROOT / "marca" / "tokens.json"
CSV_PATH = SCRIPT_DIR / "dados" / "graf-01.csv"
OUT_DIR = SLUG_DIR / "figuras"

# --- tokens: fonte única de cor (marca/tokens.json) ---
tokens = json.loads(TOKENS_PATH.read_text(encoding="utf-8"))


def parse_oklch(s: str):
    # "oklch(0.7969 0.2008 152.64)" -> (L, C, H_graus)
    inner = s.strip().removeprefix("oklch(").removesuffix(")")
    L, C, H = (float(x) for x in inner.split())
    return L, C, H


def oklch_to_oklab(L, C, H_deg):
    H = math.radians(H_deg)
    return L, C * math.cos(H), C * math.sin(H)


def oklab_to_srgb_hex(L, a, b):
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l_**3, m_**3, s_**3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bb = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s

    def gamma(c):
        c = max(0.0, min(1.0, c))
        return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

    r, g, bb = (round(max(0.0, min(1.0, gamma(c))) * 255) for c in (r, g, bb))
    return f"#{r:02X}{g:02X}{bb:02X}"


def oklab_lerp(c0, c1, t):
    return tuple(c0[i] + t * (c1[i] - c0[i]) for i in range(3))


# Gradiente de risco: success (baixo) -> warning (médio) -> error (alto),
# interpolado em OKLab (não em RGB ingênuo) — os três âncoras já existem em
# marca/tokens.json (functional.success/warning/error), nenhum hex novo é inventado.
anchor_success = oklch_to_oklab(*parse_oklch(tokens["functional"]["success"]["oklch"]))
anchor_warning = oklch_to_oklab(*parse_oklch(tokens["functional"]["warning"]["oklch"]))
anchor_error = oklch_to_oklab(*parse_oklch(tokens["functional"]["error"]["oklch"]))
stops = [(0.0, anchor_success), (0.5, anchor_warning), (1.0, anchor_error)]


def risk_color(risco_ordinal: int, n: int = 5) -> str:
    t = (risco_ordinal - 1) / (n - 1)
    for (t0, c0), (t1, c1) in zip(stops, stops[1:]):
        if t0 <= t <= t1:
            f = (t - t0) / (t1 - t0)
            return oklab_to_srgb_hex(*oklab_lerp(c0, c1, f))
    return oklab_to_srgb_hex(*stops[-1][1])


# --- dados (posts/<slug>/graficos/dados/graf-01.csv, versionado junto) ---
with CSV_PATH.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
rows.sort(key=lambda r: int(r["rung"]))

y_labels = [r["distancia_label"] for r in rows]
x_vals = [int(r["risco_ordinal"]) for r in rows]
produtos = [r["produto"] for r in rows]
produtos_wrapped = ["<br>".join(textwrap.wrap(p, width=28)) for p in produtos]
colors = [risk_color(int(r["risco_ordinal"])) for r in rows]

fig = go.Figure(
    go.Bar(
        x=x_vals,
        y=y_labels,
        orientation="h",
        marker=dict(color=colors, line=dict(color=tokens["neutrals"]["line_hi"]["hex"], width=1)),
        text=produtos_wrapped,
        customdata=produtos,
        textposition="outside",
        textfont=dict(color=tokens["text"]["high"]["hex"], family="Inter, sans-serif", size=13),
        hovertemplate="%{y}<br>%{customdata}<br>risco ordinal: %{x}<extra></extra>",
    )
)

fig.update_layout(
    title=dict(
        text="A régua da corrida: risco crescente, produto por produto",
        font=dict(family="Space Grotesk, sans-serif", size=20, color=tokens["text"]["high"]["hex"]),
        x=0.02,
        xanchor="left",
    ),
    paper_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    plot_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    font=dict(family="Inter, sans-serif", color=tokens["text"]["medium"]["hex"]),
    margin=dict(l=20, r=280, t=90, b=60),
    xaxis=dict(
        title="Nível de risco relativo (escala ordinal ilustrativa, não uma medida de mercado)",
        range=[0, 7.6],
        tickmode="array",
        tickvals=[1, 2, 3, 4, 5],
        gridcolor=tokens["dataviz"]["grid_line"],
        color=tokens["dataviz"]["axis_text"],
        zeroline=False,
    ),
    yaxis=dict(
        categoryorder="array",
        categoryarray=y_labels,  # rung 1 embaixo, rung 5 em cima (ordem do CSV)
        color=tokens["dataviz"]["axis_text"],
        gridcolor=tokens["neutrals"]["line"]["hex"],
    ),
    showlegend=False,
    width=1500,
    height=800,
)

# Ponto de interesse 1: onde a maioria dos iniciantes de fato entra (topo da régua).
# Fonte: Chague & Giovannetti (2025), "As pandemias de COVID-19 e de day trade no
# Brasil", Revista Brasileira de Finanças 23, e202515 — número já confirmado em
# processo/07-verificacao.md §1.
fig.add_annotation(
    x=x_vals[-1],
    y=y_labels[-1],
    text=(
        "968.512 pessoas fizeram day trade em contratos futuros só entre 2020-2023,<br>"
        "perda agregada de R$ 9,9 bi (Chague &amp; Giovannetti, 2025) —<br>"
        "é aqui que a maioria dos iniciantes de fato entra."
    ),
    showarrow=True,
    arrowhead=2,
    arrowcolor=tokens["functional"]["error"]["hex"],
    ax=-220,
    ay=-70,
    font=dict(color=tokens["functional"]["error"]["hex"], size=12, family="Inter, sans-serif"),
    align="left",
    bgcolor=tokens["neutrals"]["carbon"]["hex"],
    bordercolor=tokens["functional"]["error"]["hex"],
    borderwidth=1,
    borderpad=6,
)

# Ponto de interesse 2: onde a régua recomenda começar (base) — contraste real
# com o ponto de interesse 1, não forçado (dois estados de fato distintos:
# prescrito pela analogia vs. observado nos dados de day trade).
fig.add_annotation(
    x=x_vals[0] * 0.45,
    y=y_labels[0],
    text="Ponto de entrada recomendado",
    showarrow=True,
    arrowhead=2,
    arrowcolor=tokens["volt"]["500"]["hex"],
    ax=140,
    ay=-90,
    font=dict(color=tokens["volt"]["500"]["hex"], size=12, family="Inter, sans-serif"),
    bgcolor=tokens["neutrals"]["carbon"]["hex"],
    bordercolor=tokens["volt"]["500"]["hex"],
    borderwidth=1,
    borderpad=6,
)

OUT_DIR.mkdir(parents=True, exist_ok=True)
fig.write_image(str(OUT_DIR / "graf-01.svg"))
fig.write_image(str(OUT_DIR / "graf-01.png"), scale=2)
print("OK — figuras exportadas em", OUT_DIR)
```
