# Gráficos — "O Agro é POP, o Agro é Produto Financeiro!"

Uma peça, decidida em `processo/02-estrutura.md` ("Onde entra graf-NN/diag-NN/info-NN") e
posicionada em `processo/04-draft-v2.md`, na seção "O lado de quem compra" / "Por que essa
conta erra". Checklist de craft (`.claude/agents/references/checklist-graficos.md`) aplicado
abaixo. Tokens de marca lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`
(`marca-syntaxis`, v2.7.0/DESIGN.md v3.1) — nenhuma cor hardcoded fora do arquivo de origem.
Script testado com `python3` a partir da raiz do repositório (`pipelines/hemingway/`), mesma
convenção dos demais `graficos.md` do pipeline.

## graf-01

**Pergunta que o gráfico responde:** por que comparar LCA e CDB dividindo a taxa da LCA por
(1 − IR) exagera quanto o CDB precisa pagar — e o exagero cresce com o prazo?

**Fonte dos dados:** `posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro/processo/07-verificacao.md`
(etapa 7, item 2) — fórmulas e tabela conferidas, sem divergência frente ao rascunho. Premissas:
CDI de 14% a.a. (valor didático, não a taxa do dia — decisão do autor no gate humano, etapa 10:
o argumento é sobre a forma da conta, não sobre o nível atual de juros), LCA a 90% do CDI, IR
do CDB regressivo por prazo (20% até 6 meses, 17,5% até 1 ano, 15% acima de 2 anos — Lei
nº 11.033/2004, tabela regressiva de renda fixa).

**Dados:** `posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro/graficos/dados/graf-01.csv`
— cinco prazos (6 meses, 1 ano, 2 anos, 3 anos, 5 anos), com o percentual do CDI da regra
linear e do break-even real por juros compostos em cada um.

```csv
prazo_label,prazo_meses,ir_cdb_pct,regra_linear_pct_cdi,breakeven_real_pct_cdi
6 meses,6,20.0,112.5,111.7
1 ano,12,17.5,109.1,107.8
2 anos,24,15.0,105.9,103.9
3 anos,36,15.0,105.9,103.0
5 anos,60,15.0,105.9,101.6
```

**Código Plotly executável** (testado com `python3` nesta etapa, a partir da raiz do
repositório — gera `figuras/graf-01.svg` e `figuras/graf-01.png`; os valores de entrada
(`CDI_AA`, `LCA_PCT_CDI`, a tabela de IR e a tabela de break-even) estão isolados no topo do
script para o recálculo do `[VERIFICAR]` acima ser só trocar números, não reescrever código):

```python
import json
import os
import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

# --- Premissas (isoladas para recálculo — ver [VERIFICAR] no spec) ---------------------
# CDI e taxa da LCA usados nesta rodada; a tabela de dados em graficos/dados/graf-01.csv já
# reflete o cálculo de fórmula (break-even por juros compostos, ver processo/04-draft-v2.md,
# seção "Por que essa conta erra") com estes dois parâmetros. Trocar aqui não recalcula o CSV
# sozinho — é o ponteiro para onde o recálculo do [VERIFICAR] tem que entrar.
CDI_AA = 0.14
LCA_PCT_CDI = 0.90

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
text_medium = tokens["color"]["neutral"]["slate"]["$value"]
grid = tokens["color"]["neutral"]["mist"]["$value"]
forest = tokens["color"]["forest"]["500"]["$value"]
grove = tokens["color"]["grove"]["500"]["$value"]
font_display = tokens["typography"]["fontFamily"]["display"]["$value"][0]
font_body = tokens["typography"]["fontFamily"]["body"]["$value"][0]
font_data = tokens["typography"]["fontFamily"]["data"]["$value"][0]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv")).sort_values("prazo_meses")

fig = go.Figure()

# "Regra linear" (o gross-up ingênuo) primeiro — o erro que o texto desmonta. shape="hv"
# porque a regra muda em degraus, seguindo as três faixas de IR regressivo do CDB, não uma
# curva contínua.
fig.add_trace(go.Scatter(
    x=df["prazo_meses"], y=df["regra_linear_pct_cdi"],
    mode="lines+markers", line=dict(color=forest, width=2.5, shape="hv"),
    marker=dict(color=forest, size=7),
    name="Regra linear (Taxa LCA / (1 − IR))",
))
# "Break-even real" — a curva correta, capitalização composta ao longo do prazo.
# fill="tonexty" pinta só a área entre as duas linhas (o erro), não um bloco decorativo.
fig.add_trace(go.Scatter(
    x=df["prazo_meses"], y=df["breakeven_real_pct_cdi"],
    mode="lines+markers", line=dict(color=grove, width=2.5, shape="linear"),
    marker=dict(color=grove, size=7),
    name="Break-even real (juros compostos)",
    fill="tonexty", fillcolor="rgba(45, 158, 103, 0.15)",  # grove.500 em baixa opacidade, só a área do erro
))

fig.update_layout(
    plot_bgcolor=bg,
    paper_bgcolor=bg,
    font=dict(family=font_body, color=text_high, size=13),
    title=dict(
        text="Quanto a regra linear superestima o CDB equivalente à LCA — e por quê",
        font=dict(family=font_display, size=18, color=text_high),
        x=0.02, xanchor="left",
    ),
    legend=dict(orientation="h", y=1.12, x=0, xanchor="left", font=dict(size=12), traceorder="normal"),
    margin=dict(l=60, r=40, t=110, b=110),
    width=1100, height=620,
)

fig.update_xaxes(
    title=None,
    tickmode="array",
    tickvals=df["prazo_meses"],
    ticktext=df["prazo_label"],
    showgrid=False,
)
# Eixo Y sem começar em zero (exceção declarada, checklist-graficos.md "Gate de Tufte"):
# toda a série real fica entre 100% e 113% do CDI — zero não é o ponto de comparação
# relevante aqui (não é "valor vs. nenhum retorno", é uma leitura contra a outra dentro de
# uma faixa estreita). Forçar rangemode="tozero" comprimiria as duas linhas numa fita de
# poucos pixels no topo do gráfico e esconderia o próprio achado (o tamanho do erro).
fig.update_yaxes(
    title="% do CDI",
    gridcolor=grid,
    ticksuffix="%",
    range=[98, 116],
    dtick=4,
)

gap_6m = df.loc[df["prazo_meses"] == 6, "regra_linear_pct_cdi"].iloc[0] - df.loc[df["prazo_meses"] == 6, "breakeven_real_pct_cdi"].iloc[0]
gap_5a = df.loc[df["prazo_meses"] == 60, "regra_linear_pct_cdi"].iloc[0] - df.loc[df["prazo_meses"] == 60, "breakeven_real_pct_cdi"].iloc[0]

# Anotação do ponto de interesse: o erro cresce de 0,8 p.p. (6 meses) para 4,3 p.p. (5 anos).
fig.add_annotation(
    x=36, y=104.6,
    text=f"o erro cresce de {gap_6m:.1f} p.p. em 6 meses<br>para {gap_5a:.1f} p.p. em 5 anos",
    showarrow=True, arrowhead=2, arrowcolor=text_medium,
    ax=0, ay=55,
    font=dict(size=12, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)

fig.add_annotation(
    text="Área sombreada = quanto a regra linear (gross-up simples) exagera o CDB equivalente frente ao break-even por juros compostos.<br>"
         f"CDI {CDI_AA:.0%} a.a. · LCA a {LCA_PCT_CDI:.0%} do CDI · IR do CDB regressivo por prazo (20% até 6m, 17,5% até 1a, 15% acima de 2a).",
    showarrow=False, x=0, y=-0.22, xref="paper", yref="paper",
    font=dict(size=11, color=text_medium, family=font_body), xanchor="left", align="left",
)
fig.add_annotation(
    text="Fonte: processo/07-verificacao.md (etapa 7, item 2) — CDI de 14% a.a. é valor didático, não a taxa do dia.",
    showarrow=False, x=0, y=-0.31, xref="paper", yref="paper",
    font=dict(size=10, color=text_medium, family=font_data), xanchor="left",
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** duas linhas sobre o mesmo eixo de prazo, com área
preenchida entre elas — a forma mais direta de mostrar que o erro (a distância vertical) não é
constante, e sim cresce com o prazo, que é exatamente o argumento do texto. Descartado:
gráfico de barras pareadas por prazo (esconderia a trajetória contínua do break-even real, que
é uma curva de juros compostos, não pontos isolados); gráfico de barras só do gap em p.p.
(responderia "quanto é o erro" mas não "por que ele cresce" — perderia a leitura das duas taxas
em si, que o leitor precisa ver lado a lado para entender que a regra linear é *constante em
degraus* enquanto o break-even real é *decrescente contínuo*).

**Anotação:** `add_annotation` aponta diretamente para a faixa entre as linhas na região de
maior gap (2-5 anos), com o valor exato de crescimento do erro (0,8 p.p. → 4,3 p.p.) — o ponto
que a pergunta do gráfico responde, não deixado só para a legenda ou o eixo.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linhas mostrando duas curvas em percentual do CDI ao longo do prazo (6 meses a 5
> anos): a regra linear ingênua (Taxa LCA dividida por 1 menos IR), que muda em degraus
> seguindo as faixas de IR regressivo do CDB, e o break-even real por juros compostos, que cai
> de forma contínua. A área entre as duas linhas — o erro da regra linear — cresce de 0,8
> pontos percentuais em 6 meses para 4,3 pontos percentuais em 5 anos.

**Legenda (para exibição junto à figura em `post.md`):**

> Com CDI a 14% a.a. e LCA a 90% do CDI, a regra linear (Taxa LCA / (1 − IR)) superestima o CDB
> equivalente cada vez mais quanto mais longo o prazo — o erro passa de 0,8 p.p. em 6 meses
> para 4,3 p.p. em 5 anos, porque o IR do CDB é uma mordida única no resgate, mas a diferença
> de taxa entre os dois papéis capitaliza todos os dias (`processo/07-verificacao.md`, etapa 7).
