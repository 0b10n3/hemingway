# Gráficos — O Papel do CDB na Transformação de Prazos

Uma peça, decidida em `processo/02-estrutura.md` (seção 4) e posicionada em
`processo/04-draft-v1.md` linha 87, no fim de "CDB não é CDI". Checklist de craft
(`references/checklist-graficos.md`) aplicado abaixo: anotação direta no ponto de interesse,
avaliação de revelação progressiva, contraste avaliado quanto a ser genuíno. Tokens de marca
lidos em runtime de `marca/tokens.json` (skill `marca-syntaxis`) — nenhuma cor hardcoded fora
do arquivo de origem.

## graf-01

**Pergunta que o gráfico responde:** quanto o percentual do CDI pago por um CDB pós-fixado
(90%, 100% ou 110%) muda o capital acumulado ao longo do tempo?

**Fonte dos dados:** simulação própria, não é dado de mercado histórico ou atual — os três
percentuais (90/100/110% do CDI) já foram confirmados como cenário ilustrativo, não estatística
de mercado, em `processo/07-verificacao.md` item 9 ("os três valores tratados como cenários
ilustrativos de comparação, não como dado histórico"). Premissas explícitas, para
reprodutibilidade:
- CDI assumido: 10,00% a.a. (número redondo hipotético — não é a taxa vigente em nenhuma data
  específica; o post já evita ler os percentuais como taxa de mercado atual, e este gráfico
  segue a mesma cautela).
- Capital inicial: R$ 10.000,00.
- Horizonte: 24 meses — mesmo prazo do exemplo hipotético usado depois, na seção "Onde o CDB
  entra na sua carteira" (compra de imóvel em dois anos), para manter coerência de escala
  entre o gráfico e o resto do post.
- Capitalização mensal simplificada: `capital(m) = capital(m-1) × (1 + pct_do_cdi × cdi_mensal)`,
  com `cdi_mensal = (1 + cdi_anual)^(1/12) − 1`. Simplificação pedagógica deliberada: o mercado
  real capitaliza por dias úteis (base 252, pro-rata die); a capitalização mensal aqui não
  muda a conclusão qualitativa (o efeito comparativo do percentual do CDI) e é mais legível no
  eixo do gráfico.

**Dados:** `graficos/dados/graf-01.csv` (25 linhas, mês 0 a 24, uma coluna por cenário).

**Código Plotly executável** (testado com `python3` nesta etapa — gera
`figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os
import pandas as pd
import plotly.graph_objects as go

POST_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
    if "__file__" in dir() else "."
# Caminhos relativos à raiz do post (posts/<slug>/); ajuste POST_DIR se rodar de outro lugar.
POST_DIR = "posts/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos"
TOKENS_PATH = "marca/tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

# Cores lidas de marca/tokens.json em runtime — fonte única, nenhum hex duplicado aqui.
bg = tokens["neutrals"]["obsidian"]["hex"]
grid = tokens["dataviz"]["grid_line"]
axis_text = tokens["dataviz"]["axis_text"]
text_high = tokens["text"]["high"]["hex"]
text_medium = tokens["text"]["medium"]["hex"]
cat = dict(zip(tokens["dataviz"]["categorical_names"], tokens["dataviz"]["categorical"]))
volt_hero = tokens["volt"]["500"]["hex"]

cor_90 = cat["Teal"]
cor_100 = volt_hero          # série principal / cenário mais comum — recebe o tom "hero"
cor_110 = cat["Sky"]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))

fig = go.Figure()

series = [
    ("capital_90pct_cdi", "90% do CDI", cor_90, 2),
    ("capital_100pct_cdi", "100% do CDI", cor_100, 3),
    ("capital_110pct_cdi", "110% do CDI", cor_110, 2),
]

for col, label, color, width in series:
    fig.add_trace(go.Scatter(
        x=df["mes"], y=df[col],
        mode="lines",
        name=label,
        line=dict(color=color, width=width),
        hovertemplate=f"{label}: R$ %{{y:,.2f}}<extra></extra>",
    ))
    # Rótulo direto no fim de cada linha — evita obrigar o leitor a caçar a legenda.
    valor_fmt = f"{df[col].iloc[-1]:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    fig.add_annotation(
        x=df["mes"].iloc[-1], y=df[col].iloc[-1],
        text=f"<b>{label}</b><br>R$ {valor_fmt}",
        showarrow=False,
        xanchor="left",
        xshift=10,
        align="left",
        font=dict(color=color, size=12, family="Inter, sans-serif"),
    )

# Anotação direta no ponto de interesse — o número que a pergunta do gráfico responde.
# Evita "R$" duas vezes na mesma string de anotação: Plotly/MathJax trata um par de "$"
# como delimitador de fórmula e quebra a renderização do texto.
fig.add_annotation(
    x=6, y=13200,
    text=(
        "Diferença ao final de 24 meses entre 110% e 90% do CDI: R$ 459,50<br>"
        "sobre um capital inicial de dez mil reais aplicados"
    ),
    showarrow=False,
    align="left",
    xanchor="left",
    font=dict(color=text_high, size=12, family="Inter, sans-serif"),
    bgcolor=tokens["neutrals"]["carbon"]["hex"],
    bordercolor=grid,
    borderwidth=1,
    borderpad=8,
)

fig.update_layout(
    title=dict(
        text="Quanto o percentual do CDI muda o resultado de um CDB pós-fixado",
        font=dict(color=text_high, size=17, family="Space Grotesk, sans-serif"),
        x=0.02, xanchor="left",
    ),
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    font=dict(color=text_medium, family="Inter, sans-serif"),
    xaxis=dict(
        title="Meses desde a aplicação",
        gridcolor=grid, zerolinecolor=grid, color=axis_text,
        range=[0, 30],
    ),
    yaxis=dict(
        title="Capital acumulado (R$)",
        gridcolor=grid, zerolinecolor=grid, color=axis_text,
        tickprefix="R$ ", tickformat=",.0f",
    ),
    legend=dict(
        orientation="h", yanchor="bottom", y=1.02, xanchor="left", x=0,
        font=dict(color=text_medium),
    ),
    margin=dict(l=70, r=140, t=70, b=60),
    width=900, height=560,
)

os.makedirs(os.path.join(POST_DIR, "figuras"), exist_ok=True)
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.svg"))
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** linha (série temporal contínua) — a pergunta é
sobre trajetória de crescimento composto ao longo do tempo, não sobre comparação pontual entre
categorias, então um gráfico de barras foi descartado (esconderia a curvatura do juro
composto, que é justamente o que distingue 90/100/110% de forma crescente, não linear).

*Nota sobre revelação progressiva (checklist):* as três linhas formam um leque estreito e
monotônico — nunca se cruzam, mantêm a mesma ordem do início ao fim — e o rótulo direto no
fim de cada uma já desambigua sem exigir leitura cruzada com a legenda. Avaliada a divisão em
2-3 gráficos sequenciais por linha; descartada porque o ponto do gráfico é justamente a
comparação simultânea entre os três cenários — fragmentar em gráficos separados destruiria a
pergunta que o gráfico responde, não apenas simplificaria a leitura.

*Nota sobre contraste genuíno (checklist):* não há par antes/depois aqui — é uma comparação de
três cenários paralelos ao longo do mesmo eixo, não dois estados do mesmo objeto. Nenhum
contraste binário foi forçado.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linhas mostrando o crescimento de R$ 10.000,00 aplicados em CDB pós-fixado ao
> longo de 24 meses, em três cenários: 90%, 100% e 110% do CDI (CDI hipotético de 10% ao ano).
> As três curvas seguem trajetória de juro composto, sempre na mesma ordem, terminando em R$
> 11.872,34 (90%), R$ 12.100,00 (100%) e R$ 12.331,84 (110%) — uma diferença de R$ 459,50 entre
> o cenário mais baixo e o mais alto ao final do período.

**Legenda (para exibição junto à figura em `post.md`):**

> Simulação ilustrativa de um CDB pós-fixado a 90%, 100% e 110% do CDI (CDI hipotético de 10%
> a.a.), R$ 10.000,00 aplicados por 24 meses. Não é projeção de rentabilidade real — os
> percentuais variam conforme a instituição emissora e a taxa DI muda diariamente.
