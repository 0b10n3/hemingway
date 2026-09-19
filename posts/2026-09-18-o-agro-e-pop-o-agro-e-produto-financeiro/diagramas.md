# Diagramas — "O Agro é POP, o Agro é Produto Financeiro!"

Uma peça, decidida em `processo/02-estrutura.md` ("Onde entra graf-NN/diag-NN/info-NN") e
posicionada em `processo/04-draft-v2.md`, na seção "O que é uma LCA" — sem série numérica, é
relação estrutural entre entidades (critério 2 da "Etapa 2" da skill). Ferramenta: Plotly (nós
via `add_shape`, setas via `add_annotation`), mesmo padrão de `graf-NN`. Tokens de marca lidos
em runtime de `../../brand/tokens/syntaxis.tokens.json`. Script testado com `python3` a partir
da raiz do repositório (`pipelines/hemingway/`).

## diag-01

**Pergunta que o diagrama responde:** quando alguém compra uma LCA, quais são as duas relações
de crédito distintas envolvidas, e com qual das duas o investidor de fato se relaciona?

Sem seção de fonte dos dados: não há número embutido no diagrama — é a estrutura de três
entidades e duas relações de crédito descrita no corpo do texto ("O que é uma LCA",
`processo/04-draft-v2.md`), com base na Lei nº 11.076/2004 já citada ali.

**Código Plotly executável** (testado com `python3` nesta etapa, a partir da raiz do
repositório — gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
text_medium = tokens["color"]["neutral"]["slate"]["$value"]
grid = tokens["color"]["neutral"]["mist"]["$value"]
forest = tokens["color"]["forest"]["500"]["$value"]
grove = tokens["color"]["grove"]["500"]["$value"]
white = tokens["color"]["neutral"]["white"]["$value"]
font_display = tokens["typography"]["fontFamily"]["display"]["$value"][0]
font_body = tokens["typography"]["fontFamily"]["body"]["$value"][0]

fig = go.Figure()

NODE_W, NODE_H = 3.0, 1.3

# Três entidades, esquerda → direita: produtor/cooperativa, banco (contraparte real do
# investidor), investidor. O banco é destacado em forest (âncora institucional / onde mora
# o risco de crédito); os dois extremos ficam em grove.
nodes = {
    "produtor": {"x": 1.5, "y": 3.0, "text": "Produtor /<br>cooperativa", "color": grove},
    "banco": {"x": 6.0, "y": 3.0, "text": "Banco<br>emissor", "color": forest},
    "investidor": {"x": 10.5, "y": 3.0, "text": "Investidor", "color": grove},
}


def add_node(n):
    x, y = n["x"], n["y"]
    fig.add_shape(
        type="rect",
        x0=x - NODE_W / 2, x1=x + NODE_W / 2,
        y0=y - NODE_H / 2, y1=y + NODE_H / 2,
        line=dict(color=n["color"], width=1.5),
        fillcolor=n["color"],
        layer="below",
    )
    fig.add_annotation(
        x=x, y=y, text=n["text"], showarrow=False,
        font=dict(color=white, size=14, family=font_body),
        align="center",
    )


for n in nodes.values():
    add_node(n)


def edge_point(cx, cy, w, h, tx, ty):
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hh = w / 2, h / 2
    scale_x = abs(hw / dx) if dx != 0 else float("inf")
    scale_y = abs(hh / dy) if dy != 0 else float("inf")
    scale = min(scale_x, scale_y)
    return cx + dx * scale, cy + dy * scale


def arrow(a, b, color, width, gap=0.15):
    """Seta de a para b (o sentido do crédito: quem empresta -> quem deve/recebe)."""
    na, nb = nodes[a], nodes[b]
    sx, sy = edge_point(na["x"], na["y"], NODE_W, NODE_H, nb["x"], nb["y"])
    ex, ey = edge_point(nb["x"], nb["y"], NODE_W, NODE_H, na["x"], na["y"])
    vx, vy = ex - sx, ey - sy
    length = (vx ** 2 + vy ** 2) ** 0.5
    ux, uy = (vx / length, vy / length) if length else (0, 0)
    sx2, sy2 = sx + ux * gap, sy + uy * gap
    ex2, ey2 = ex - ux * gap, ey - uy * gap
    fig.add_annotation(
        x=ex2, y=ey2, ax=sx2, ay=sy2, xref="x", yref="y", axref="x", ayref="y",
        showarrow=True, arrowhead=2, arrowsize=1.2, arrowwidth=width,
        arrowcolor=color, text="",
    )


# As duas relações de crédito, cada uma rotulada por cima da seta correspondente — o sentido
# da seta é o sentido do dinheiro (de quem empresta para quem recebe/deve): o investidor
# empresta ao banco (crédito 2, a própria LCA) e o banco empresta ao agro (crédito 1, o lastro).
arrow("investidor", "banco", color=grove, width=2.5)
fig.add_annotation(
    x=(nodes["investidor"]["x"] + nodes["banco"]["x"]) / 2, y=3.0 + NODE_H / 2 + 0.35,
    text="Crédito 2 — investidor empresta ao banco<br>(representado pela própria LCA)",
    showarrow=False, font=dict(color=text_high, size=12, family=font_body), align="center",
)

arrow("banco", "produtor", color=forest, width=2.5)
fig.add_annotation(
    x=(nodes["banco"]["x"] + nodes["produtor"]["x"]) / 2, y=3.0 + NODE_H / 2 + 0.35,
    text="Crédito 1 — banco empresta ao agro<br>(forma o lastro da LCA)",
    showarrow=False, font=dict(color=text_high, size=12, family=font_body), align="center",
)

fig.add_annotation(
    x=6.0, y=3.0 - NODE_H / 2 - 0.55,
    text="O investidor não tem relação de crédito direta com o produtor — a contraparte dele é sempre o banco.",
    showarrow=False, font=dict(color=text_medium, size=12, family=font_body),
    align="center",
)

fig.update_layout(
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    width=1100,
    height=520,
    margin=dict(l=40, r=40, t=90, b=40),
    xaxis=dict(visible=False, range=[-0.3, 12.3]),
    yaxis=dict(visible=False, range=[1.0, 5.0]),
    title=dict(
        text="Duas relações de crédito, uma LCA",
        font=dict(color=text_high, size=18, family=font_display),
        x=0.02, xanchor="left",
    ),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout justificada:** três nós numa linha só, sem layout automático de grafo —
com três entidades e duas setas, a disposição manual esquerda→direita comunica diretamente a
distinção que o texto faz (o investidor nunca chega ao produtor; passa sempre pelo banco). O
banco, ao centro e em `forest` (mais escuro que os dois extremos em `grove`), fica visualmente
marcado como o nó por onde as duas relações de crédito obrigatoriamente passam — reforça o
parágrafo do rascunho ("A contraparte é o banco emissor") sem precisar de anotação extra.

**Alt-text final (para o placeholder `diag-01` em `post.md`):**

> Diagrama de fluxo com três entidades em linha: produtor/cooperativa, banco emissor (em
> destaque) e investidor. Duas setas apontam da direita para a esquerda, cada uma rotulada com
> uma relação de crédito distinta — 'Crédito 2: investidor empresta ao banco, representado pela
> própria LCA' e 'Crédito 1: banco empresta ao agro, forma o lastro da LCA'. Uma nota abaixo do
> banco esclarece que o investidor não tem relação de crédito direta com o produtor — a
> contraparte dele é sempre o banco.

**Legenda (para exibição junto à figura em `post.md`):**

> Duas relações de crédito distintas formam uma LCA: o banco empresta ao agronegócio (o
> lastro) e o investidor empresta ao banco (a própria LCA). Quem compra LCA não vira credor do
> produtor rural — a contraparte é sempre o banco emissor.
