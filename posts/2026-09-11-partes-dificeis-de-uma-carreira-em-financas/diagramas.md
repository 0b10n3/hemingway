# Diagramas — 2026-09-11-partes-dificeis-de-uma-carreira-em-financas

## `diag-01`

**Pergunta que o diagrama responde:** qual é a cadeia mecânica pela qual escolher um difícil
com propósito vira significado, segundo o argumento de Peterson usado no post?

**Fonte dos dados:** não se aplica — é relação estrutural (fluxo de cinco elos), sem métrica
central, decidida na etapa 2 pelo critério "duas linhas, dois blocos... sem métrica real por
trás". Os cinco elos e as legendas de apoio vêm do próprio texto do post
(`processo/04-draft-v1.md`, seção "Dificuldades com significado") — não há número a citar.

**Escolha de layout:** fluxo linear horizontal de 5 nós com seta entre cada par — a cadeia é
sequencial e cada elo depende do anterior (não é rede, não é hierarquia), então layout linear é
a leitura mais direta; descartado layout circular (sugeriria ciclo, mas a cadeia do texto é
unidirecional, de responsabilidade a significado, sem retorno).

**O que o diagrama acrescenta à prosa (achado da etapa 5):** a crítica estrutural apontou que
uma legenda repetindo só os cinco nomes dos elos duplicaria o parágrafo anterior sem
acrescentar nada. Por isso cada nó carrega, abaixo do nome, um exemplo concreto tirado do
próprio texto (não repetido na prosa da seção 4 nesses termos) — o diagrama funciona como
resumo operacional da cadeia, não como ilustração redundante dela.

**Alt-text:** "Diagrama: cadeia de quatro setas ligando Responsabilidade (assumir um objetivo
real), Dificuldade (entender a demonstração antes da fórmula), Competência (perceber quando a
premissa quebra), Contribuição (o que o mercado raramente reforça) e Significado (a carreira
que sustenta), com o último nó em destaque na cor de acento da marca."

**Código Plotly executável** (autocontido — salve o bloco abaixo como `.py` e rode com cwd em
`posts/2026-09-11-partes-dificeis-de-uma-carreira-em-financas/`; lê os tokens de
`../../../../brand/tokens/syntaxis.tokens.json` em runtime, sem hex hardcoded fora do arquivo
de tokens; exporta `figuras/diag-01.svg` e `figuras/diag-01.png` — já testado nesta etapa,
arquivos presentes em `figuras/`):

```python
"""diag-01 — cadeia de Peterson: responsabilidade -> significado.
Tokens lidos em runtime de brand/tokens/syntaxis.tokens.json (fonte única, CLAUDE.md).
"""
import json
import plotly.graph_objects as go

TOKENS_PATH = "../../../../brand/tokens/syntaxis.tokens.json"
with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)


def resolve(path):
    node = tokens
    for part in path.split("."):
        node = node[part]
    val = node["$value"]
    if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
        return resolve(val[1:-1])
    return val


forest_500 = resolve("color.forest.500")
forest_100 = resolve("color.forest.100")
lime_500 = resolve("color.lime.500")
ink = resolve("color.neutral.ink")
chalk = resolve("color.neutral.chalk")
slate = resolve("color.neutral.slate")
font_display = resolve("typography.fontFamily.display")[0]
font_body = resolve("typography.fontFamily.body")[0]

nodes = [
    ("Responsabilidade", "assumir um<br>objetivo real"),
    ("Dificuldade", "entender a demonstração<br>antes da fórmula"),
    ("Competência", "perceber quando<br>a premissa quebra"),
    ("Contribuição", "o que o mercado<br>raramente reforça"),
    ("Significado", "a carreira<br>que sustenta"),
]

n = len(nodes)
box_w, gap = 1.0, 0.35
xs = [i * (box_w + gap) for i in range(n)]
y0, y1 = 0.0, 1.0

fig = go.Figure()

for i, (title, caption) in enumerate(nodes):
    is_last = i == n - 1
    fill = lime_500 if is_last else forest_100

    # radius none — sistema de cantos retos, DESIGN.md §4.4-4.5
    fig.add_shape(
        type="rect",
        x0=xs[i], x1=xs[i] + box_w, y0=y0, y1=y1,
        line=dict(color=forest_500, width=2),
        fillcolor=fill,
        layer="below",
    )
    fig.add_annotation(
        x=xs[i] + box_w / 2, y=y1 * 0.62,
        text=f"<b>{title}</b>",
        showarrow=False,
        font=dict(family=font_display, size=17, color=ink),
        align="center",
    )
    fig.add_annotation(
        x=xs[i] + box_w / 2, y=y1 * 0.30,
        text=caption,
        showarrow=False,
        font=dict(family=font_body, size=12, color=slate),
        align="center",
    )

    if not is_last:
        fig.add_annotation(
            x=xs[i + 1], y=(y0 + y1) / 2,
            ax=xs[i] + box_w, ay=(y0 + y1) / 2,
            xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=2, arrowsize=1.2, arrowwidth=2,
            arrowcolor=forest_500, text="",
        )

fig.update_xaxes(visible=False, range=[-0.15, xs[-1] + box_w + 0.15])
fig.update_yaxes(visible=False, range=[-0.15, 1.15])
fig.update_layout(
    width=1200, height=280,
    plot_bgcolor=chalk, paper_bgcolor=chalk,
    margin=dict(l=20, r=20, t=20, b=20),
    showlegend=False,
)

fig.write_image("figuras/diag-01.svg")
fig.write_image("figuras/diag-01.png", scale=2)
```

Gate de Tufte (checklist-graficos.md): sem 3D, sombra, textura ou moldura; grid ausente por
não haver eixo numérico; dimensão visual = dimensão dos dados (retângulos de largura igual,
sem área codificando magnitude, já que não há métrica); único acento de cor (lime) reservado
ao nó de chegada ("Significado"), consistente com a regra de marca de que lime é o único
acento de ação/conquista do sistema — não decorativo, marca o ponto de chegada do argumento.
