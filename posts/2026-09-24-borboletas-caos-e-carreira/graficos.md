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

**Nota de refação (gate humano, etapa 10, 2026-09-25):** o autor pediu para trocar a forma
visual deste `graf-01` — de duas linhas de série temporal para um **cobweb plot** (diagrama de
teia de aranha / staircase), a forma clássica de visualizar a iteração de um mapa 1D. A
pergunta que o gráfico responde e a fonte dos dados não mudaram; só a forma. Versão anterior
(duas linhas ao longo do tempo) fica registrada no histórico do git, não neste arquivo.

## graf-01

**Pergunta que o gráfico responde:** como uma diferença de 0,0001 na condição inicial do mapa
logístico (x₀ = 0,2000 vs. x₀ = 0,2001) evolui, passo a passo, de invisível para completamente
divergente — visto no espaço de fase do próprio mapa (a curva f(x) = 4x(1−x) e a diagonal
y = x), não ao longo do tempo?

**Fonte dos dados:** não é dado observacional — é a recorrência do mapa logístico
(x_seguinte = 4·x·(1−x)), popularizada por Robert May, "Simple mathematical models with very
complicated dynamics", *Nature*, vol. 261, pp. 459–467, 10/06/1976 (atribuição confirmada em
`processo/07-verificacao.md`, etapa 7, item 4). Os 21 valores (passos 0 a 20, para os dois
pontos de partida) foram recalculados nesta etapa em Python a partir da própria fórmula — os
três pontos que o texto cita (passos 5, 10 e 14) batem exatamente com o recálculo já feito e
registrado em `processo/07-verificacao.md`, etapa 7, item 1 (data: 2026-09-23). Nenhuma fonte
externa a verificar: é aritmética determinística, não medição. A curva f(x) = 4x(1−x) e a
diagonal y = x plotadas no cobweb não são dado novo — são a própria fórmula já verificada,
desenhada por inteiro em vez de amostrada só nos 21 passos.

**Dados:** `posts/2026-09-24-borboletas-caos-e-carreira/graficos/dados/graf-01.csv` — 21 passos
(0 a 20, cobrindo os "pelo menos 20 passos" da spec do autor), com o valor de x em cada passo
para os dois pontos de partida. Mesmo arquivo da versão anterior deste gráfico — o caminho em
degraus do cobweb é derivado dele, não de um CSV novo.

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
import numpy as np
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


def cobweb_path(xs):
    """Caminho em degraus: (x0,0) -> (x0,f(x0)) -> (f(x0),f(x0)) -> ... alternando
    vertical (sobe até a curva) e horizontal (leva até a diagonal)."""
    px, py = [xs[0]], [0.0]
    for i in range(len(xs) - 1):
        px.append(xs[i]); py.append(xs[i + 1])       # vertical: sobe até a curva
        px.append(xs[i + 1]); py.append(xs[i + 1])   # horizontal: leva até y=x
    return px, py


x_curve = np.linspace(0, 1, 300)
y_curve = 4 * x_curve * (1 - x_curve)

fig = go.Figure()

# A curva do mapa e a diagonal de referência — o "tabuleiro" do cobweb plot.
fig.add_trace(go.Scatter(
    x=x_curve, y=y_curve, mode="lines",
    line=dict(color=text_high, width=2),
    name="f(x) = 4x(1−x)",
))
fig.add_trace(go.Scatter(
    x=[0, 1], y=[0, 1], mode="lines",
    line=dict(color=text_medium, width=1, dash="dot"),
    name="y = x",
))

path_ends = {}
for col, color, dash, label in [
    ("x0_0200", forest, "solid", "x₀ = 0,2000"),
    ("x0_0201", grove, "dot", "x₀ = 0,2001"),
]:
    xs = df[col].tolist()
    px, py = cobweb_path(xs)
    fig.add_trace(go.Scatter(
        x=px, y=py, mode="lines",
        line=dict(color=color, width=1.5, dash=dash),
        opacity=0.85, name=label,
    ))
    path_ends[col] = (xs[0], xs[-1])
    # Marcador no ponto de partida (quase colado ao da outra trajetória).
    fig.add_trace(go.Scatter(
        x=[xs[0]], y=[0], mode="markers",
        marker=dict(color=color, size=7, symbol="circle"),
        showlegend=False,
    ))

fig.update_layout(
    plot_bgcolor=bg,
    paper_bgcolor=bg,
    font=dict(family=font_body, color=text_high, size=13),
    title=dict(
        text="Duas condições iniciais quase idênticas, o mesmo mapa — cobweb plot, 20 iterações",
        font=dict(family=font_display, size=18, color=text_high),
        x=0.02, xanchor="left", y=0.98, yanchor="top",
    ),
    legend=dict(orientation="h", y=0.9, x=0, xanchor="left", font=dict(size=12)),
    margin=dict(l=60, r=40, t=130, b=260),
    width=900, height=1190,  # l+r=100, t+b=390 -> área de plot 800x800 (quadrada, exigido pelo scaleanchor abaixo)
)

fig.update_xaxes(title="x_n", range=[0, 1.02], gridcolor=grid, dtick=0.2)
fig.update_yaxes(
    title="x_(n+1)", range=[0, 1.02], gridcolor=grid, dtick=0.2,
    scaleanchor="x", scaleratio=1,  # aspecto 1:1 — sem isso a diagonal y=x mentiria sobre o ângulo.
)

# Anotação 1: os primeiros passos colam na mesma região da curva.
fig.add_annotation(
    x=df.loc[1, "x0_0200"], y=df.loc[2, "x0_0200"],
    text="passos 1–2: as duas trajetórias<br>colam no mesmo degrau",
    showarrow=True, arrowhead=2, arrowcolor=text_medium,
    ax=-70, ay=-20,
    font=dict(size=11, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)
# Anotação 2: no passo 14, x0=0,2000 despenca perto de zero.
fig.add_annotation(
    x=df.loc[14, "x0_0200"], y=df.loc[15, "x0_0200"],
    text="passo 14 (x₀=0,2000): 0,0010",
    showarrow=True, arrowhead=2, arrowcolor=lime_text,
    ax=90, ay=-30,
    font=dict(size=11, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)
# Anotação 3: no mesmo passo 14, x0=0,2001 está do outro lado do quadrado.
fig.add_annotation(
    x=df.loc[14, "x0_0201"], y=df.loc[15, "x0_0201"],
    text="passo 14 (x₀=0,2001): 0,7630<br>mesma fórmula, destino oposto",
    showarrow=True, arrowhead=2, arrowcolor=lime_text,
    ax=-40, ay=-50,
    font=dict(size=11, color=text_high, family=font_body),
    bgcolor=bg, bordercolor=grid, borderwidth=1,
)

fig.add_annotation(
    text=("Cada degrau é um passo da recorrência (x_seguinte = 4·x·(1−x)): sobe até a curva preta,<br>"
          "vira na diagonal pontilhada. As duas trajetórias (0,2000 e 0,2001) desenham o mesmo<br>"
          "degrau nos primeiros passos e se separam por completo depois do décimo quarto."),
    showarrow=False, x=0, y=-0.16, xref="paper", yref="paper",
    font=dict(size=12, color=text_medium, family=font_body), xanchor="left", align="left",
)
fig.add_annotation(
    text=("Fonte: recorrência do mapa logístico (Robert May, Nature, 1976), recalculada em<br>"
          "processo/07-verificacao.md (etapa 7, item 1), 2026-09-23."),
    showarrow=False, x=0, y=-0.28, xref="paper", yref="paper",
    font=dict(size=10, color=text_medium, family=font_data), xanchor="left",
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** cobweb plot é a forma canônica de visualizar a
iteração de um mapa 1D (x_seguinte = f(x)) — em vez de mostrar só o valor de x contra o tempo,
mostra o mecanismo geométrico: sobe até a curva (aplica f), vira na diagonal (usa a saída como
nova entrada), repete. É a forma que o próprio campo (dinâmica de sistemas, popularizada por
Robert May) usa para este tipo de mapa, e conecta o "porquê" a uma imagem, não só ao número.
Duas trajetórias sobrepostas foi testado antes de decidido (renderizado e inspecionado nesta
etapa): os dois degraus desenham praticamente a mesma escada nos primeiros ~10 passos —
tracejado vs. sólido é a única diferença visível — e só depois se separam em regiões opostas do
quadrado [0,1]×[0,1], o que demonstra a sensibilidade a condições iniciais de forma estrutural
(a mesma pergunta do `graf-01` anterior), não só textual. Descartado: cobweb de uma trajetória
só com a divergência descrita em legenda — perderia exatamente o que a pergunta pede: ver as
duas trajetórias colarem e depois se separarem, não ler sobre isso. Descartado também manter a
forma anterior (duas linhas de série temporal): foi a decisão do autor no gate humano, não uma
falha de craft da versão anterior — mas o cobweb, testado aqui, também se defende sozinho: o
mesmo achado (colado → separado) fica ainda mais direto porque o "onde" no espaço de fase é o
próprio argumento, não uma leitura de eixo X como tempo.

**Anotação:** três `add_annotation` diretas sobre o gráfico — uma nos passos 1–2 (onde os dois
degraus ainda colam, ancorando o "antes"), duas no passo 14, uma para cada trajetória, apontando
para os dois cantos opostos do quadrado onde cada uma termina (o "depois" que a pergunta do
gráfico responde) — mais a legenda de rodapé explicando a mecânica do cobweb em si (subir até a
curva, virar na diagonal), necessária porque o formato é menos familiar ao leitor do que uma
linha do tempo.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Cobweb plot (diagrama de teia de aranha) do mapa logístico: a curva f(x) = 4x(1−x), a
> diagonal y = x, e duas trajetórias em degraus partindo de x₀ = 0,2000 e x₀ = 0,2001 — uma
> diferença de uma parte em duas mil. Os dois caminhos desenham a mesma escada nos primeiros
> passos, praticamente sobrepostos, e se separam por completo a partir do décimo quarto: um
> termina perto de zero (0,0010), o outro no lado oposto do quadrado (0,7630).

**Legenda (para exibição junto à figura em `post.md`):**

> Duas trajetórias da mesma fórmula (x_seguinte = 4x(1−x)), partindo de pontos quase idênticos
> (0,2000 e 0,2001), desenhadas como cobweb plot: sobe até a curva, vira na diagonal, repete.
> Os degraus colam nos primeiros passos e se separam por completo depois do décimo quarto — a
> mesma sensibilidade às condições iniciais que torna o clima imprevisível além de uma semana
> ou dez dias (`processo/07-verificacao.md`, etapa 7, item 1).
