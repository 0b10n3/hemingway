# Gráficos — O Mundo Invertido das Carreiras

## graf-01 — A ordem de referência e a ordem que eu segui

**Revisão (pedido do autor no gate):** a primeira versão tinha rótulo de texto completo ao
lado de cada marcador (a descrição inteira de base/topo, dobrada em várias linhas) mais
legenda no topo — carregado demais para uma ideia que é só "sobe" vs. "desce". Versão atual:
só os marcadores numerados, a seta de direção e os eixos (Base/Topo no y, os dois nomes de
trilha no x) — a descrição completa de cada nível migrou para o hover (`hovertext`), sem peso
visual na versão estática. Legenda removida (a cor de cada seta já distingue as trilhas, e os
rótulos do eixo x já nomeiam cada coluna).

**Pergunta que o gráfico responde:** qual é a ordem de referência para construir conhecimento
em finanças (base antes do topo) — e em que ordem o autor de fato a construiu?

**Fonte dos dados:** a trilha "ordem de referência" é elaboração própria a partir de três
fontes já verificadas em `processo/07-verificacao.md`: a estrutura de capítulos de John Hull,
*Options, Futures, and Other Derivatives* (juros e formação de preço a termo nos capítulos 4-6,
mecânica de opções bem mais adiante — capítulo 10 nas edições mais recentes); a ordem oficial
de áreas de tópico do currículo CFA Institute (Quantitative Methods, que inclui valor do
dinheiro no tempo, antecede Fixed Income); e o pré-requisito listado pela GFMI (Global
Financial Markets Institute) para o curso de VaR ("entender conceitos financeiros simples,
como valor presente"). A trilha "a ordem que eu segui" é relato autobiográfico do autor — ver
`_arquivo/transcricoes/2026-0817_O_Mundo_Invertido_das_Carreiras_em_Financas.md` e
`processo/02-estrutura.md`. A escala de nível (Base/Topo) é ordinal e ilustrativa, não uma
medida de mercado.

**Dados:** `graficos/dados/graf-01.csv` (versionado junto).

**Escolha de tipo de gráfico:** duas trilhas verticais lado a lado (bump chart de dois nós),
cada uma com seta indicando a direção percorrida — escolhida porque o ponto central do gráfico
é a direção (sobe vs. desce), não uma quantidade a comparar; um gráfico de barras esconderia a
direção, e um scatter sem seta exigiria que o leitor inferisse a ordem cronológica sozinho.
Descartado: gráfico de barras horizontais (não há "quantidade" a comparar, é uma sequência) e
Sankey (peso excessivo para só dois nós por trilha).

**Cor:** verde `functional.success` (`#1FE07A`, de `marca/tokens.json`) para a trilha de
referência (o caminho recomendado) e vermelho `functional.error` (`#FF6B6B`) para a trilha do
autor (o caminho que gerou a lacuna) — reaproveita o mesmo par semântico success/error já usado
no gráfico do post anterior, sem inventar cor nova.

**Anotação:** os marcadores numerados (1, 2) em cada trilha indicam a ordem cronológica
percorrida, e a seta (`add_annotation` com `arrowhead`) aponta diretamente a direção — sobe na
trilha de referência, desce na trilha do autor. O nível (base/topo) fica só nos rótulos do
eixo y, compartilhado pelas duas trilhas — não repetido ao lado de cada marcador. A descrição
completa de cada ponto (ex.: "valor do dinheiro no tempo, juros, dívida pública, mercado de
crédito") fica em `hovertext`, disponível em versão interativa sem pesar na imagem estática.
Contraste genuíno, não forçado: são duas trilhas reais e comparáveis no mesmo eixo (nível de
conhecimento), não um "antes/depois" artificial.

**Alt-text:** "Gráfico com duas trilhas verticais lado a lado. À esquerda, em verde, a ordem
de referência: começa na base (valor do dinheiro no tempo, juros, dívida pública, mercado de
crédito) e sobe até o topo (precificação de derivativos, VaR). À direita, em vermelho, a ordem
que o autor seguiu: começa no topo (precificação de opções, no mestrado) e só desce à base —
valor do dinheiro no tempo, juros, dívida pública, crédito — anos depois."

**Legenda (para usar sob o gráfico em `post.md`):** "A ordem de referência sobe da base ao
topo. A minha foi ao contrário — e a base só veio depois."

### Código (autocontido, testado com `python3`)

Salvo em `graficos/graf-01.py`, lê `graficos/dados/graf-01.csv` e `marca/tokens.json`, exporta
para `figuras/graf-01.svg` e `figuras/graf-01.png`. Testado nesta etapa com Python 3 + Plotly
6.9 + Kaleido — roda sozinho, sem preâmbulo, com `python3 graf-01.py` a partir de `graficos/`.

```python
"""
graf-01 — Duas trilhas: a ordem de referência e a ordem que eu segui.
Versão enxuta: só os marcadores numerados e a seta de direção por trilha —
descrição completa vive só no hover, não poluindo o gráfico estático.
Autocontido: lê o CSV ao lado (dados/graf-01.csv) e os tokens de marca/tokens.json,
exporta para ../figuras/graf-01.svg e .png. Rodar com: python3 graf-01.py
"""
import csv
import json
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

COLOR_REFERENCIA = tokens["functional"]["success"]["hex"]  # volt-500, caminho recomendado
COLOR_AUTOR = tokens["functional"]["error"]["hex"]          # caminho que o autor seguiu

# --- dados (posts/<slug>/graficos/dados/graf-01.csv, versionado junto) ---
with CSV_PATH.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

trilhas = {}
for r in rows:
    trilhas.setdefault(r["trilha"], []).append(r)
for t in trilhas:
    trilhas[t].sort(key=lambda r: int(r["ordem"]))

X_REFERENCIA, X_AUTOR = 0, 2
X_LABELS = ["Ordem de referência", "A ordem que eu segui"]

fig = go.Figure()

for trilha, x_pos, color, nome in (
    ("referencia", X_REFERENCIA, COLOR_REFERENCIA, "Ordem de referência"),
    ("autor", X_AUTOR, COLOR_AUTOR, "A ordem que eu segui"),
):
    pontos = trilhas[trilha]
    ys = [int(p["nivel_y"]) for p in pontos]
    fig.add_trace(
        go.Scatter(
            x=[x_pos] * len(pontos),
            y=ys,
            mode="markers+text",
            marker=dict(size=26, color=color, line=dict(color=tokens["neutrals"]["obsidian"]["hex"], width=2)),
            text=[p["ordem"] for p in pontos],
            textposition="middle center",
            textfont=dict(color=tokens["neutrals"]["obsidian"]["hex"], size=14, family="JetBrains Mono, monospace"),
            name=nome,
            hovertext=[p["rotulo_completo"] for p in pontos],
            hoverinfo="text",
            showlegend=False,
        )
    )
    # seta de direção conectando o primeiro ao segundo ponto da trilha (ordem 1 -> 2)
    p_ini, p_fim = pontos[0], pontos[1]
    fig.add_annotation(
        x=x_pos,
        y=int(p_fim["nivel_y"]),
        ax=x_pos,
        ay=int(p_ini["nivel_y"]),
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True,
        arrowhead=3,
        arrowsize=1.4,
        arrowwidth=4,
        arrowcolor=color,
        text="",
    )

fig.update_layout(
    title=dict(
        text="A ordem de referência — e a ordem que eu segui",
        font=dict(family="Space Grotesk, sans-serif", size=20, color=tokens["text"]["high"]["hex"]),
        x=0.5,
        xanchor="center",
        y=0.95,
    ),
    paper_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    plot_bgcolor=tokens["neutrals"]["obsidian"]["hex"],
    font=dict(family="Inter, sans-serif", color=tokens["text"]["medium"]["hex"]),
    margin=dict(l=60, r=60, t=110, b=70),
    xaxis=dict(
        tickmode="array",
        tickvals=[X_REFERENCIA, X_AUTOR],
        ticktext=X_LABELS,
        tickfont=dict(size=15, color=tokens["text"]["high"]["hex"]),
        range=[-1.0, 3.0],
        showgrid=False,
        zeroline=False,
    ),
    yaxis=dict(
        tickmode="array",
        tickvals=[1, 2],
        ticktext=["Base", "Topo"],
        tickfont=dict(size=15),
        range=[0.5, 2.5],
        gridcolor=tokens["dataviz"]["grid_line"],
        color=tokens["dataviz"]["axis_text"],
        zeroline=False,
    ),
    showlegend=False,
    width=1100,
    height=750,
)

OUT_DIR.mkdir(parents=True, exist_ok=True)
fig.write_image(str(OUT_DIR / "graf-01.svg"))
fig.write_image(str(OUT_DIR / "graf-01.png"), scale=2)
print("OK — figuras exportadas em", OUT_DIR)
```
