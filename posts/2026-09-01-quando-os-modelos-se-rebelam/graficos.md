# Gráficos — "Quando os Modelos se Rebelam"

Uma peça, decidida em `processo/02-estrutura.md` (seção 3) e posicionada em
`processo/04-draft-v1.md`, logo após a descrição do circuit breaker do pregão de 18/05/2017
("Joesley Day"). Checklist de craft (`.claude/skills/prompts-visuais/references/checklist-graficos.md`)
aplicado abaixo. Tokens de marca lidos em runtime de `../../brand/tokens/skill_test.tokens.json`
(skill `marca-syntaxis`) — nenhuma cor hardcoded fora do arquivo de origem.

## graf-01

**Pergunta que o gráfico responde:** o que aconteceu, no mesmo pregão, com os dois preços que
a hipótese de continuidade do Black–Scholes pressupõe bem-comportados — o índice de ações e o
câmbio — quando a premissa quebrou de uma vez só?

**Fonte dos dados:** `processo/07-verificacao.md` (etapa 7), corrigida frente à rodada
anterior. Dólar (PTAX, fechamento): Banco Central, API SGS série 1
(`api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados`) — **R$3,1283 (17/05/2017) → R$3,3805
(18/05/2017), +8,06%** (recalculado; nesta rodada as cotações usam quatro casas decimais para
que a conta interna do gráfico feche exatamente com o "8,06%" reportado pela imprensa — a
rodada anterior usava R$3,14→R$3,38, que só dá 7,64%, imprecisão sinalizada pela etapa 7 e
corrigida aqui). Ibovespa (fechamento): 67.540 (17/05) → 61.597 (18/05), -8,80% — cruzado entre
espelho de dados de mercado e imprensa financeira da época (InfoMoney), convergente. Mínima
intradiária do Ibovespa (-10,47%, índice em 60.470 pontos, ponto que acionou o primeiro circuit
breaker desde 2008) reconfirmada nesta rodada via InfoMoney.

**Dados:** `posts/2026-09-01-quando-os-modelos-se-rebelam/graficos/dados/graf-01.csv` — cinco
pontos, dois painéis (Ibovespa: fechamento 17/05, mínima intradiária 18/05, fechamento 18/05;
Dólar: fechamento 17/05, fechamento 18/05), todos como variação percentual em relação ao
fechamento do dia anterior.

**Código Plotly executável** (testado com `python3` nesta etapa — gera `figuras/graf-01.svg`
e `figuras/graf-01.png`):

```python
import json
import os
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

POST_DIR = "posts/2026-09-01-quando-os-modelos-se-rebelam"
TOKENS_PATH = "../../brand/tokens/skill_test.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
text_medium = tokens["color"]["neutral"]["slate"]["$value"]
grid = tokens["color"]["neutral"]["mist"]["$value"]
forest = tokens["color"]["forest"]["500"]["$value"]
grove = tokens["color"]["grove"]["500"]["$value"]
error_text = tokens["color"]["semantic"]["errorText"]["$value"]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Ibovespa", "Dólar (PTAX)"),
    horizontal_spacing=0.12,
)

for i, painel in enumerate(["Ibovespa", "Dólar (PTAX)"], start=1):
    sub = df[df["painel"] == painel].sort_values("ordem")
    colors = [error_text if v < 0 else (forest if v == 0 else grove) for v in sub["variacao_pct"]]
    fig.add_trace(
        go.Bar(
            x=sub["ponto"], y=sub["variacao_pct"],
            marker_color=colors,
            text=[f"{v:+.2f}%" if v != 0 else "0,00%" for v in sub["variacao_pct"]],
            textposition="outside",
            textfont=dict(family="Space Mono, monospace", size=13, color=text_high),
            showlegend=False,
        ),
        row=1, col=i,
    )

fig.update_layout(
    plot_bgcolor=bg,
    paper_bgcolor=bg,
    font=dict(family="Hanken Grotesk, sans-serif", color=text_high, size=13),
    title=dict(
        text="18 de maio de 2017 — o pregão em que não existiu preço no meio do caminho",
        font=dict(family="Space Grotesk, sans-serif", size=18, color=text_high),
        x=0.02, xanchor="left",
    ),
    margin=dict(l=60, r=40, t=90, b=60),
    width=1200, height=560,
    annotations=list(fig.layout.annotations) + [
        dict(
            text="Variação % em relação ao fechamento do dia anterior (17/05/2017)",
            showarrow=False, x=0, y=-0.16, xref="paper", yref="paper",
            font=dict(size=12, color=text_medium), xanchor="left",
        ),
        dict(
            text="Fonte: Banco Central (SGS série 1, PTAX) e Ibovespa (B3), verificado etapa 7",
            showarrow=False, x=0, y=-0.22, xref="paper", yref="paper",
            font=dict(size=11, color=text_medium), xanchor="left",
        ),
    ],
)

fig.update_yaxes(gridcolor=grid, zerolinecolor=text_medium, zerolinewidth=1, ticksuffix="%", title=None)
fig.update_xaxes(showgrid=False)

fig.add_annotation(
    x="Mínima intradiária 18/05", y=-10.47, xref="x1", yref="y1",
    text="1º circuit breaker<br>desde 2008",
    showarrow=True, arrowhead=2, arrowcolor=text_medium,
    ax=40, ay=-40,
    font=dict(size=11, color=text_high),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de encoding justificada (checklist Tufte):** barras, não linha — são dois pontos
discretos por painel (mais um terceiro no Ibovespa, a mínima intradiária), não uma série
temporal densa; eixo Y em variação percentual, com zero explícito, nunca cortado — nenhuma
distorção de escala. Cor por sinal (vermelho para queda, verde para alta) reforça o que o
número já diz, não substitui o número. Anotação direta (`add_annotation`) aponta o ponto de
interesse (mínima intradiária, gatilho do circuit breaker) além da legenda de eixo — checklist
"anotação direta, não só legenda" de `checklist-graficos.md`.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Gráfico de barras em dois painéis mostrando a variação percentual do Ibovespa e do dólar no
> pregão de 18 de maio de 2017. O Ibovespa caiu 10,47% na mínima intradiária — acionando o
> primeiro circuit breaker desde 2008 — e fechou o dia em -8,80%. O dólar subiu 8,06% no mesmo
> pregão.

**Legenda (para exibição junto à figura em `post.md`):**

> No pregão seguinte ao vazamento Joesley/Temer, o Ibovespa chegou a cair 10,47% — acionando o
> primeiro circuit breaker desde 2008 — e fechou a -8,80%; o dólar subiu 8,06% no mesmo dia
> (Banco Central, SGS série 1).
