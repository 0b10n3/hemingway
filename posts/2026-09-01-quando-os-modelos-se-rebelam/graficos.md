# Gráficos — "Quando os Modelos se Rebelam"

Uma peça, decidida em `processo/02-estrutura.md` (seção 3) e posicionada em
`processo/04-draft-v1.md`, logo após os números do pregão de 18/05/2017 ("Joesley Day").
Checklist de craft (`.claude/skills/prompts-visuais/references/checklist-graficos.md`)
aplicado abaixo. Tokens de marca lidos em runtime de
`../../brand/tokens/skill_test.tokens.json` (skill `marca-syntaxis`) — nenhuma cor
hardcoded fora do arquivo de origem.

## graf-01

**Pergunta que o gráfico responde:** o que aconteceu, no mesmo pregão, com os dois preços que
a hipótese de continuidade do Black–Scholes pressupõe bem-comportados — o índice de ações e o
câmbio — quando a premissa quebrou de uma vez só?

**Fonte dos dados:** confirmada em `processo/07-verificacao.md` (itens reconfirmados contra
`03-pesquisa.md`) — InfoMoney e Suno, cobertura do pregão de 18/05/2017, acesso 31/08/2026.
Queda intradiária do Ibovespa de -10,47% (mínima), fechamento a -8,80% (maior queda diária
desde 22/10/2008), primeiro *circuit breaker* desde 2008. Alta do dólar de 8,06%, de R$ 3,14
para R$ 3,38 (cotações arredondadas do texto) — a verificação técnica apontou que 8,06% só
bate matematicamente contra cotações com mais casas decimais (R$ 3,1283 → R$ 3,3805, a
precisão usada de fato pela imprensa financeira); o percentual em si (8,06%) está correto e é
o número usado no gráfico e no corpo do texto.

**Dados:** `posts/2026-09-01-quando-os-modelos-se-rebelam/graficos/dados/graf-01.csv` — cinco
pontos, dois painéis (Ibovespa: fechamento 17/05, mínima intradiária 18/05, fechamento 18/05;
Dólar: fechamento 17/05, fechamento 18/05), todos como variação percentual em relação ao
fechamento do dia anterior — não como nível absoluto do índice/câmbio, porque a pesquisa e a
verificação técnica confirmaram os percentuais contra fonte primária, mas não os pontos
absolutos do Ibovespa naquele pregão (evitando `[VERIFICAR]` desnecessário: o gráfico usa só
o que foi verificado).

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

# Cores lidas de brand/tokens/skill_test.tokens.json em runtime — fonte única, nenhum hex
# duplicado aqui (formato DTCG: cada token primitivo tem "$value").
bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
text_medium = tokens["color"]["neutral"]["slate"]["$value"]
grid = tokens["color"]["neutral"]["mist"]["$value"]
grove = tokens["color"]["grove"]["500"]["$value"]
error_text = tokens["color"]["semantic"]["errorText"]["$value"]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))

fig = make_subplots(
    rows=1, cols=2,
    column_widths=[0.6, 0.4],
    subplot_titles=("Ibovespa", "Dólar (USD/BRL)"),
    horizontal_spacing=0.1,
)

# Painel 1 — Ibovespa: variação % em relação ao fechamento do dia anterior (17/05/2017).
ibov = df[df["painel"] == "Ibovespa"].sort_values("ordem")
bar_colors_ibov = [text_medium if v == 0 else error_text for v in ibov["valor_pct"]]
fig.add_trace(
    go.Bar(
        x=ibov["categoria"], y=ibov["valor_pct"],
        marker_color=bar_colors_ibov,
        text=[f"{v:+.2f}%".replace("+0.00%", "0%") for v in ibov["valor_pct"]],
        textposition="outside",
        hovertemplate="%{x}: %{y:+.2f}%<extra></extra>",
        showlegend=False,
    ),
    row=1, col=1,
)
fig.add_annotation(
    x="Mínima intradiária 18/05", y=-10.47,
    ax="Fechamento 17/05", ay=-4.5, axref="x", ayref="y",
    text="1º <i>circuit breaker</i><br>desde 2008",
    showarrow=True, arrowhead=2, arrowcolor=error_text, arrowwidth=1.5,
    font=dict(color=error_text, size=11, family="Hanken Grotesk, sans-serif"),
    align="left", xanchor="left",
    row=1, col=1,
)
fig.add_annotation(
    x="Fechamento 18/05", y=-8.80,
    ax="Fechamento 17/05", ay=-7.6, axref="x", ayref="y",
    text="maior queda diária<br>desde out/2008",
    showarrow=True, arrowhead=2, arrowcolor=error_text, arrowwidth=1.5,
    font=dict(color=error_text, size=11, family="Hanken Grotesk, sans-serif"),
    align="left", xanchor="left",
    row=1, col=1,
)

# Painel 2 — Dólar: variação % do fechamento de 17/05 para o fechamento de 18/05.
# Cotações-fonte com precisão maior que as duas casas citadas no corpo do texto
# (R$3,14 -> R$3,38, que arredondado dá 7,64%): R$3,1283 -> R$3,3805 = +8,06%,
# a cifra consistentemente reportada pela imprensa financeira (ver 07-verificacao.md).
dolar = df[df["painel"] == "Dólar (USD/BRL)"].sort_values("ordem")
fig.add_trace(
    go.Bar(
        x=dolar["categoria"], y=dolar["valor_pct"],
        marker_color=[text_medium, grove],
        text=[f"{v:+.2f}%".replace("+0.00%", "0%") for v in dolar["valor_pct"]],
        textposition="outside",
        hovertemplate="%{x}: %{y:+.2f}%<extra></extra>",
        showlegend=False,
    ),
    row=1, col=2,
)

fig.update_layout(
    title=dict(
        text="18 de maio de 2017: o dia em que não existiu preço no meio do caminho",
        font=dict(color=text_high, size=17, family="Space Grotesk, sans-serif"),
        x=0.02, xanchor="left",
    ),
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    font=dict(color=text_medium, family="Hanken Grotesk, sans-serif"),
    showlegend=False,
    margin=dict(l=60, r=40, t=90, b=60),
    width=980, height=520,
)
fig.update_yaxes(
    title="Variação vs. fechamento anterior",
    gridcolor=grid, zerolinecolor=text_high, zerolinewidth=1.5, color=text_medium,
    ticksuffix="%", rangemode="tozero", row=1, col=1,
)
fig.update_yaxes(
    gridcolor=grid, zerolinecolor=text_high, zerolinewidth=1.5, color=text_medium,
    ticksuffix="%", rangemode="tozero", row=1, col=2,
)
fig.update_xaxes(gridcolor=grid, color=text_medium, row=1, col=1)
fig.update_xaxes(gridcolor=grid, color=text_medium, row=1, col=2)
for ann in fig.layout.annotations[:2]:
    ann.font.family = "Space Grotesk, sans-serif"
    ann.font.size = 13
    ann.font.color = text_high

os.makedirs(os.path.join(POST_DIR, "figuras"), exist_ok=True)
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.svg"))
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** barras, eixo zerado (Tufte — variação percentual
a partir de 0%, sem truncar o eixo) — a pergunta é uma comparação pontual entre poucos
estados discretos (fechamento anterior vs. mínima vs. fechamento), não uma trajetória
contínua, então linha foi descartada. Dois painéis (small multiples) em vez de um único
gráfico com dois eixos Y sobrepostos — Ibovespa (%) e dólar (%) têm a mesma unidade, mas
misturar as duas séries num único painel obrigaria uma legenda para distinguir cores e
competiria visualmente com as anotações; separar em dois painéis do mesmo tipo é a solução
que o checklist recomenda para séries que não devem ser lidas uma contra a outra no mesmo
eixo, só em paralelo.

*Nota sobre anotação (checklist):* os dois pontos de interesse do painel Ibovespa (mínima
intradiária, que aciona o circuit breaker; fechamento, a maior queda desde 2008) têm anotação
direta apontando para o dado, não só a legenda do eixo — a barra do dólar não precisa de
anotação além do rótulo de valor, porque não há um segundo evento a destacar nela.

*Nota sobre revelação progressiva:* cada painel tem no máximo 3 categorias de uma única
série — não há disputa visual de 3+ séries que justifique dividir mais.

*Nota sobre contraste genuíno:* o "antes/depois" (fechamento anterior vs. fechamento do dia)
é o par real que a pergunta do gráfico pede — não é um molde forçado sobre um conteúdo
conceitual.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Dois gráficos de barras lado a lado sobre o pregão de 18 de maio de 2017. À esquerda, o
> Ibovespa: 0% no fechamento do dia anterior, -10,47% na mínima intradiária (ponto em que o
> primeiro *circuit breaker* desde 2008 foi acionado) e -8,80% no fechamento (a maior queda
> diária desde outubro de 2008). À direita, o dólar frente ao real: 0% no fechamento anterior
> e +8,06% no fechamento do dia 18.

**Legenda (para exibição junto à figura em `post.md`):**

> Ibovespa e dólar (USD/BRL), variação percentual sobre o fechamento do dia anterior —
> 17-18/05/2017, o pregão do "Joesley Day" (InfoMoney, Suno). A queda intradiária do Ibovespa
> acionou o primeiro *circuit breaker* desde 2008.
