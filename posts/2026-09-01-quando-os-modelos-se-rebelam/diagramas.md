# Diagramas — "Quando os Modelos se Rebelam"

Uma peça. `diag-01` corresponde à composição de "precisão mecânica" dentro da colagem
editorial unificada (`.claude/skills/prompts-visuais/references/estilos-ilustracao.md`, "Quando
o argumento pede precisão mecânica"). Decidida em `processo/02-estrutura.md` (seção 4) e
posicionada em `processo/04-draft-v1.md`, logo após "a hipótese de liquidez é a premissa mais
invisível e mais letal de toda a modelagem financeira". Ferramenta: Plotly (nós e setas via
`add_shape`/`add_annotation`). Tokens de marca lidos em runtime de
`../../brand/tokens/skill_test.tokens.json`. Sem mudança de dado ou conceito frente à rodada
anterior — reafirmado, não recriado do zero (ver `processo/08-briefing-visual.md`).

## diag-01

**Pergunta que o diagrama responde:** por que a perda do LTCM não parou quando as posições
pararam de fazer sentido — o que exatamente fechou o ciclo que transformou uma divergência de
spread numa espiral de venda forçada?

**Fonte dos dados:** não há número embutido no diagrama (é mecanismo/fluxo, não série) — a
sequência causal (calote russo → fuga para liquidez → spreads divergem → chamadas de margem →
venda forçada → preços pioram → fecha o ciclo) está descrita e reconfirmada contra fonte
primária (President's Working Group on Financial Markets, 1999, lido na íntegra) em
`processo/07-verificacao.md`, seção 3.2.

**Código Plotly executável** (testado com `python3` nesta etapa — gera `figuras/diag-01.svg`
e `figuras/diag-01.png`):

```python
import json
import os
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-01-quando-os-modelos-se-rebelam"
TOKENS_PATH = "../../brand/tokens/skill_test.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
forest = tokens["color"]["forest"]["500"]["$value"]
grove500 = tokens["color"]["grove"]["500"]["$value"]
slate = tokens["color"]["neutral"]["slate"]["$value"]
lime700 = tokens["color"]["lime"]["700"]["$value"]
white = tokens["color"]["neutral"]["white"]["$value"]

fig = go.Figure()

NODE_W, NODE_H = 2.8, 1.1

# "trigger": True marca os dois nós de entrada (fora do ciclo, cor forest);
# os quatro nós do ciclo propriamente dito ficam em grove.
nodes = {
    "n1": {"x": 1.0, "y": 9.2, "text": "Calote russo<br>17/08/1998", "trigger": True},
    "n2": {"x": 4.4, "y": 9.2, "text": "Fuga global para<br>qualidade e liquidez", "trigger": True},
    "n3": {"x": 8.4, "y": 7.0, "text": "Spreads divergem,<br>em vez de convergir", "trigger": False},
    "n4": {"x": 8.4, "y": 4.0, "text": "Chamadas<br>de margem", "trigger": False},
    "n5": {"x": 4.4, "y": 4.0, "text": "LTCM vende para<br>cobrir a margem", "trigger": False},
    "n6": {"x": 4.4, "y": 7.0, "text": "Venda empurra os preços<br>contra as posições que restam", "trigger": False},
}


def add_node(n):
    x, y = n["x"], n["y"]
    fill = forest if n["trigger"] else grove500
    fig.add_shape(
        type="rect",
        x0=x - NODE_W / 2, x1=x + NODE_W / 2,
        y0=y - NODE_H / 2, y1=y + NODE_H / 2,
        line=dict(color=fill, width=1.5),
        fillcolor=fill,
        layer="below",
    )
    fig.add_annotation(
        x=x, y=y, text=n["text"], showarrow=False,
        font=dict(color=white, size=13, family="Hanken Grotesk, sans-serif"),
        align="center",
    )


for n in nodes.values():
    add_node(n)


def edge_point(cx, cy, w, h, tx, ty):
    """Ponto na borda do retângulo (centro cx,cy, meia-largura w/2, meia-altura h/2)
    na direção do ponto alvo (tx,ty)."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    hw, hh = w / 2, h / 2
    scale_x = abs(hw / dx) if dx != 0 else float("inf")
    scale_y = abs(hh / dy) if dy != 0 else float("inf")
    scale = min(scale_x, scale_y)
    return cx + dx * scale, cy + dy * scale


def arrow(a, b, color=slate, width=2, gap=0.12, label=None, label_xy=None):
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
        showarrow=True, arrowhead=2, arrowsize=1.1, arrowwidth=width,
        arrowcolor=color, text="",
    )
    if label:
        lx, ly = label_xy if label_xy else ((sx2 + ex2) / 2, (sy2 + ey2) / 2)
        fig.add_annotation(
            x=lx, y=ly, text=label, showarrow=False,
            font=dict(color=color, size=11, family="Hanken Grotesk, sans-serif"),
            align="center",
            bgcolor=bg,
        )


# Trilho de entrada (não faz parte do ciclo)
arrow("n1", "n2", color=slate)
arrow("n2", "n3", color=slate)

# O ciclo de liquidez, sentido horário
arrow("n3", "n4", color=slate)
arrow("n4", "n5", color=slate)
arrow("n5", "n6", color=slate)
arrow("n6", "n3", color=lime700, width=2.5, label="fecha o ciclo",
      label_xy=(6.4, 7.42))

fig.update_layout(
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    width=1080,
    height=620,
    margin=dict(l=40, r=40, t=90, b=40),
    xaxis=dict(visible=False, range=[-0.9, 10.2]),
    yaxis=dict(visible=False, range=[2.9, 10.2]),
    title=dict(
        text="O ciclo de liquidez que derrubou o LTCM (agosto-setembro de 1998)",
        font=dict(color=text_high, size=17, family="Space Grotesk, sans-serif"),
        x=0.02, xanchor="left",
    ),
)

os.makedirs(os.path.join(POST_DIR, "figuras"), exist_ok=True)
fig.write_image(os.path.join(POST_DIR, "figuras/diag-01.svg"))
fig.write_image(os.path.join(POST_DIR, "figuras/diag-01.png"), scale=2)
```

**Escolha de layout justificada:** dois nós de entrada (calote russo → fuga para liquidez)
alimentando um ciclo fechado de quatro nós, desenhado como retângulo (sentido horário) — não
um layout automático de grafo, porque com seis nós a disposição manual em "trilho + laço"
comunica diretamente a distinção mais importante do mecanismo: dois eventos acontecem uma vez
só (o calote, a fuga), mas quatro se retroalimentam (é o próprio ciclo que "fecha" e piora a
cada volta). Um layout de força automática (spring layout) esconderia essa distinção.

**Alt-text final (para o placeholder `diag-01` em `post.md`):**

> Diagrama de fluxo mostrando o ciclo de liquidez que derrubou o LTCM em 1998. Dois nós de
> entrada — "Calote russo, 17/08/1998" e "Fuga global para qualidade e liquidez" — alimentam
> um ciclo fechado de quatro etapas: "Spreads divergem, em vez de convergir", "Chamadas de
> margem", "LTCM vende para cobrir a margem" e "Venda empurra os preços contra as posições
> que restam", que por sua vez retroalimenta "Spreads divergem" — fechando o ciclo e
> agravando a cada volta.

**Legenda (para exibição junto à figura em `post.md`):**

> O calote russo de 17/08/1998 dispara uma fuga para liquidez que faz os spreads do LTCM
> divergirem em vez de convergir — e a venda forçada para cobrir margem só piora ainda mais
> os preços contra as posições que restam, fechando o ciclo (President's Working Group on
> Financial Markets, 1999).
