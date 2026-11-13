# Diagramas — "Should I stay"

Uma peça, decidida em `processo/02-estrutura.md` ("Revisão pós-etapa 5", item 8, que
substitui a versão de duas curvas da primeira parte do arquivo) e posicionada em
`processo/04-draft-v2.md` (placeholder `diag-01`, seção "Agora, o dado que me incomoda", logo
depois do parágrafo da condição de horizonte). Ferramenta: Plotly (curva via `go.Scatter`,
eixos e rótulos via `add_annotation`, divisa via `add_shape`), mesmo padrão de `graf-NN`.
Tokens lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`. O bloco roda a partir da
raiz do repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Nenhum `graf-NN` nem `info-NN`: não há série numérica real, e uma peça só carrega a síntese.

## diag-01

**Pergunta que o diagrama responde:** em que momento a dúvida semanal deixa de ser custo do
clima e vira sinal de saída?

**Fonte dos dados:** nenhum número embutido. A curva é forma conceitual (sobe côncava e fica
plana), sem escala. Rótulos de `processo/02-estrutura.md`, item 8; título da frase do autor
em `processo/04-draft-v2.md` ("olhe a derivada, não o nível").

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-11-13-should-i-stay"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # ênfase: o trecho que é o ponto (traço, não texto)
grove_text = c["grove"]["700"]["$value"]  # texto na cor de ênfase: grove.700 passa 4,5:1 sobre Chalk
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body = stack("display"), stack("body")

# Forma conceitual, sem dado: sobe côncava até T_FLAT e fica plana depois.
# Derivada contínua (zero em T_FLAT), para a virada ser "achatar", não "bater no teto".
T_FLAT, T_END, Y0, Y1 = 6.0, 10.0, 1.0, 8.0
N = 200
ts_up = [T_FLAT * i / N for i in range(N + 1)]
ys_up = [Y0 + (Y1 - Y0) * (1 - (1 - t / T_FLAT) ** 2) for t in ts_up]
ts_flat = [T_FLAT, T_END]
ys_flat = [Y1, Y1]

fig = go.Figure()
# Trecho subindo: contexto, slate. Trecho plano: o ponto do diagrama, grove.500.
# Cor nunca sozinha (SC 1.4.1): cada trecho tem rótulo direto adjacente.
fig.add_trace(go.Scatter(x=ts_up, y=ys_up, mode="lines", line=dict(color=slate, width=3),
                         hoverinfo="skip", showlegend=False))
fig.add_trace(go.Scatter(x=ts_flat, y=ys_flat, mode="lines", line=dict(color=grove, width=4),
                         hoverinfo="skip", showlegend=False))

# Divisa entre os trechos: hairline mist tracejada, onde a derivada chega a zero.
fig.add_shape(type="line", x0=T_FLAT, x1=T_FLAT, y0=0, y1=Y1,
              line=dict(color=mist, width=1.5, dash="dot"), layer="below")


def text(x, y, t, color, size, family=font_body, **kw):
    fig.add_annotation(x=x, y=y, text=t, showarrow=False, font=dict(color=color, size=size, family=family), **kw)


# Rótulos dos trechos (texto de 02-estrutura.md, "Revisão pós-etapa 5", item 8).
text(1.4, 3.4, "<b>subindo</b>: clima ruim é custo", slate, 17, xanchor="left")
text(8.0, 8.55, "<b>plana</b>: a dúvida semanal<br>vira sinal", grove_text, 17, yanchor="bottom")
text(T_FLAT + 0.12, 0.35, "a curva achata", slate, 13, xanchor="left", yanchor="bottom")


def axis_arrow(x0, y0, x1, y1):
    fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=2, arrowsize=1.1, arrowwidth=1.5,
                       arrowcolor=slate, text="")


# Eixos: setas sem ticks e sem números; só o nome de cada eixo.
axis_arrow(0, 0, 10.4, 0)
axis_arrow(0, 0, 0, 10.4)
text(10.4, -0.45, "tempo", ink, 16, xanchor="right", yanchor="top")
text(-0.45, 5.2, "capital de carreira transferível", ink, 16, textangle=-90, xanchor="right")

fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-40, xanchor="left", yanchor="top",
                   showarrow=False, align="left",
                   text="Eixos sem escala: a forma mostra a virada, não mede nada.",
                   font=dict(color=slate, size=13, family=font_body))

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=620,
    margin=dict(l=60, r=30, t=80, b=80),
    xaxis=dict(visible=False, range=[-1.2, 10.6]),
    yaxis=dict(visible=False, range=[-1.0, 10.6]),
    title=dict(text="Olhe a derivada, não o nível",
               font=dict(color=ink, size=22, family=font_display), x=0.03, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** uma curva só, sobre a trajetória do leitor, porque a regra é um
critério sobre a própria taxa, não uma comparação entre casas. A forma sobe côncava e chega à
horizontal com derivada contínua (zero no ponto de virada), para a virada ler como "achatar" e
não como "bater no teto". Ênfase da marca: o trecho plano, que é o ponto do diagrama, em
`grove.500`; o trecho subindo é contexto, em `slate`. Cada trecho tem rótulo direto (a cor
nunca carrega a distinção sozinha, SC 1.4.1); o rótulo em ênfase usa `grove.700`, porque
`grove.500` não passa 4,5:1 como texto sobre Chalk. Uma hairline `mist` pontilhada marca onde
a curva achata. Sem `lime`: não há ação nem conquista a marcar. Descartados: as duas curvas
(duas casas) da primeira versão de `02-estrutura.md`, substituídas no item 8; uma segunda
curva "trocar de casa" começando mais baixo, porque a condição de horizonte fica em prosa
(decisão do item 8); números ou ticks nos eixos, que seriam escala inventada.

**Gate de Tufte (etapa 9):** sem `rangemode="tozero"` por exceção justificada. Não há série
numérica: os eixos são conceituais, sem ticks (`visible=False`), e os `range` só enquadram a
forma com margem para setas e rótulos. A curva começa acima do eixo para não sugerir "capital
zero" no início, o que não é afirmação de dado. Lie Factor: não se aplica, porque nenhuma
altura, área ou inclinação codifica número (a nota de rodapé diz que a forma não mede). Sem
3D, sombra, textura ou moldura.

**Nota de renderização:** Montserrat e Source Sans 3 não estão instaladas neste ambiente; o PNG
saiu com a fonte de fallback da pilha (Arial / sans-serif). O SVG guarda a pilha completa e
renderiza nas fontes da marca onde elas existirem.

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Diagrama: uma curva de capital de carreira transferível ao longo do tempo, sem números nos
> eixos. No trecho em que ela sobe, o clima ruim é custo. No trecho em que ela fica plana, a
> dúvida semanal vira sinal de saída.

**Legenda:**

> Olhe a derivada, não o nível. Enquanto o capital de carreira transferível sobe, clima ruim é
> custo; quando a curva achata, a dúvida que volta toda semana vira sinal.
