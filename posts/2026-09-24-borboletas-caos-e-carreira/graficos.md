# Gráficos — "Borboletas, caos e carreira"

Uma peça, decidida em `processo/02-estrutura.md` ("Visual: onde e por quê") e posicionada em
`processo/04-draft-v1.md`, logo após o parágrafo "Depois de 14 passos: 0,0010 contra 0,7630",
antes da frase de fechamento sobre previsão do tempo — mesma posição já marcada pelo próprio
autor no rascunho (`[chart: ...]`). Checklist de craft
(`.claude/agents/references/checklist-graficos.md`) aplicado abaixo. Tokens de marca lidos em
runtime de `../../brand/tokens/syntaxis.tokens.json` — nenhuma cor hardcoded fora do arquivo de
origem. Script testado com `python3` a partir da raiz do repositório (`pipelines/hemingway/`),
mesma convenção dos demais `graficos.md` do pipeline. Sem `diagramas.md`/`infograficos.md`
neste post — `processo/02-estrutura.md` não decidiu nenhum `diag-NN`, e o padrão do pipeline é
não ter infográfico (nenhuma síntese aqui exige combinar peças isoladas, porque há só uma peça).

## graf-01

**Pergunta que o gráfico responde:** como uma diferença de 0,0001 na condição inicial do mapa
logístico (x₀ = 0,2000 vs. x₀ = 0,2001) evolui, passo a passo, de invisível para completamente
divergente?

**Fonte dos dados:** não é dado observacional — é a recorrência do mapa logístico
(x_seguinte = 4·x·(1−x)), popularizada por Robert May, "Simple mathematical models with very
complicated dynamics", *Nature*, vol. 261, pp. 459–467, 10/06/1976 (atribuição confirmada em
`processo/07-verificacao.md`, etapa 7, item 4). Os 21 valores (passos 0 a 20, para os dois
pontos de partida) foram recalculados nesta etapa em Python a partir da própria fórmula — os
três pontos que o texto cita (passos 5, 10 e 14) batem exatamente com o recálculo já feito e
registrado em `processo/07-verificacao.md`, etapa 7, item 1 (data: 2026-09-23). Nenhuma fonte
externa a verificar: é aritmética determinística, não medição.

**Dados:** `posts/2026-09-24-borboletas-caos-e-carreira/graficos/dados/graf-01.csv` — 21 passos
(0 a 20, cobrindo os "pelo menos 20 passos" da spec do autor), com o valor de x em cada passo
para os dois pontos de partida.

```csv
passo,x0_0200,x0_0201
0,0.2,0.2001
1,0.64,0.64024
2,0.9216,0.921331
3,0.289014,0.289921
4,0.821939,0.823467
5,0.585421,0.581477
6,0.970813,0.973446
7,0.113339,0.103396
8,0.401974,0.37082
9,0.961563,0.93325
10,0.147837,0.249178
11,0.503924,0.748353
12,0.999938,0.753283
13,0.000246,0.743391
14,0.000985,0.763044
15,0.003936,0.723231
16,0.015682,0.800671
17,0.061745,0.638388
18,0.23173,0.923395
19,0.712124,0.282947
20,0.820014,0.811553
```

**Código Plotly executável** (testado com `python3` nesta etapa, a partir da raiz do
repositório — gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os
import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-24-borboletas-caos-e-carreira"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
text_medium = tokens["color"]["neutral"]["slate"]["$value"]
grid = tokens["color"]["neutral"]["mist"]["$value"]
forest = tokens["color"]["forest"]["500"]["$value"]
grove = tokens["color"]["grove"]["500"]["$value"]
lime_text = tokens["color"]["lime"]["700"]["$value"]  # lime-500 nunca é texto sobre claro; usar 700 (AA)
font_display = tokens["typography"]["fontFamily"]["display"]["$value"][0]
font_body = tokens["typography"]["fontFamily"]["body"]["$value"][0]
font_data = tokens["typography"]["fontFamily"]["data"]["$value"][0]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv")).sort_values("passo")

fig = go.Figure()

# x0 = 0,2000 — Forest (âncora institucional, a trajetória "de referência")
fig.add_trace(go.Scatter(
    x=df["passo"], y=df["x0_0200"],
    mode="lines+markers", line=dict(color=forest, width=2.5),
    marker=dict(color=forest, size=6),
    name="x₀ = 0,2000",
))
# x0 = 0,2001 — Grove (a trajetória "quase igual" que diverge)
fig.add_trace(go.Scatter(
    x=df["passo"], y=df["x0_0201"],
    mode="lines+markers", line=dict(color=grove, width=2.5, dash="dot"),
    marker=dict(color=grove, size=6),
    name="x₀ = 0,2001",
))

fig.update_layout(
    plot_bgcolor=bg,
    paper_bgcolor=bg,
    font=dict(family=font_body, color=text_high, size=13),
    title=dict(
        text="Uma diferença de 0,0001 no ponto de partida — 20 passos do mapa logístico",
        font=dict(family=font_display, size=18, color=text_high),
        x=0.02, xanchor="left",
    ),
    legend=dict(orientation="h", y=1.14, x=0, xanchor="left", font=dict(size=12)),
    margin=dict(l=60, r=40, t=110, b=120),
    width=1100, height=620,
)

fig.update_xaxes(
    title="Passo da recorrência (x_seguinte = 4·x·(1−x))",
    dtick=2,
    gridcolor=grid,
)
# Eixo Y começa em zero por padrão (Gate de Tufte) — série já é 0 a 1 por construção do
# mapa logístico, não há razão para recortar, e recortar esconderia a amplitude real do caos.
fig.update_yaxes(
    title="x (valor da iteração)",
    range=[0, 1.05],
    gridcolor=grid,
    rangemode="tozero",
)

# Anotação 1: os dois primeiros passos, praticamente coladas.
fig.add_annotation(
    x=5, y=df.loc[df["passo"] == 5, "x0_0200"].iloc[0],
    text="passo 5: 0,5854 vs. 0,5815<br>ainda quase idênticas",
    showarrow=True, arrowhead=2, arrowcolor=text_medium,
    ax=-40, ay=-55,
    font=dict(size=11, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)
# Anotação 2: o ponto de virada (passo 14) — onde a leitura do gráfico se decide.
fig.add_annotation(
    x=14, y=df.loc[df["passo"] == 14, "x0_0201"].iloc[0],
    text="passo 14: 0,0010 vs. 0,7630<br>divergência completa",
    showarrow=True, arrowhead=2, arrowcolor=lime_text,
    ax=30, ay=-70,
    font=dict(size=11, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)

fig.add_annotation(
    text="Mesma fórmula (x_seguinte = 4·x·(1−x)), dois pontos de partida quase idênticos (0,2000 e 0,2001) — a diferença de 0,0001 some visualmente até por volta do décimo passo e domina o gráfico depois do décimo quarto.",
    showarrow=False, x=0, y=-0.22, xref="paper", yref="paper",
    font=dict(size=11, color=text_medium, family=font_body), xanchor="left", align="left",
)
fig.add_annotation(
    text="Fonte: recorrência do mapa logístico (Robert May, Nature, 1976), recalculada em processo/07-verificacao.md (etapa 7, item 1), 2026-09-23.",
    showarrow=False, x=0, y=-0.30, xref="paper", yref="paper",
    font=dict(size=10, color=text_medium, family=font_data), xanchor="left",
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** duas linhas sobre o mesmo eixo de passos é a forma
mais direta de mostrar uma trajetória (série ordenada, não categórica) e de deixar o próprio
traçado contar a história — coladas, depois separando, depois em lados opostos do intervalo
[0,1]. Descartado: gráfico de barras pareadas por passo (esconderia a continuidade da
trajetória, que é o ponto — o leitor precisa ver as duas linhas "andando juntas" antes de
"andarem separadas", não comparar barras isoladas passo a passo); gráfico de área da diferença
absoluta |x₁−x₂| (responderia "quanto" mas não "onde cada trajetória está indo" — perderia a
leitura de que ambas seguem dentro do mesmo intervalo [0,1], só que em pontos cada vez mais
distantes um do outro, que é o que sustenta a analogia de carreira do texto).

**Anotação:** duas `add_annotation` diretas — uma no passo 5 (ainda quase coladas, ancorando o
"antes"), outra no passo 14 (divergência completa, o "depois" que a pergunta do gráfico
responde) — não deixadas só para a legenda ou para o leitor inferir da forma da curva.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linhas com duas trajetórias do mapa logístico (x seguinte = 4x(1−x)) ao longo de
> 20 passos, partindo de x₀ = 0,2000 e x₀ = 0,2001 — uma diferença de uma parte em duas mil. As
> duas curvas ficam praticamente coladas até por volta do décimo passo (no passo 5: 0,5854
> contra 0,5815) e divergem por completo a partir do décimo quarto (0,0010 contra 0,7630),
> terminando em pontos opostos do intervalo entre 0 e 1.

**Legenda (para exibição junto à figura em `post.md`):**

> Duas trajetórias da mesma fórmula, partindo de pontos quase idênticos (0,2000 e 0,2001) —
> coladas nos primeiros passos, irreconhecíveis depois do décimo quarto. A mesma sensibilidade
> às condições iniciais que torna o clima imprevisível além de uma semana ou dez dias
> (`processo/07-verificacao.md`, etapa 7, item 1).
