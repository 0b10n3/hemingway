# Diagramas — "As partes difíceis de uma carreira em finanças" (slug de teste, pipeline v2)

Uma peça, `diag-01`. Decidida em `processo/02-estrutura.md` ("Visual — critério, não gosto",
item 2): a cadeia de Peterson (responsabilidade → dificuldade → competência → contribuição →
significado, seção 4 do post) é relação estrutural em sequência causal, sem número por trás —
por isso diagrama, não gráfico. Posicionada em `processo/04-draft-v2.md`, linha 127, logo após
o parágrafo que descreve o padrão que Peterson repete "de livro em palestra, de palestra em
entrevista". Sem `graf-NN` neste post (nenhuma série numérica no texto — `02-estrutura.md`
item 1) e sem `info-NN` (a própria `02-estrutura.md`, item 3, já registra que `diag-01` carrega
a síntese sozinho; confirmado de novo aqui: não há um segundo dado disperso que precise de
leitura conjunta com este diagrama para fazer sentido).

Ferramenta: Plotly, nós e setas via `add_shape`/`add_annotation` — mesmo padrão de `graf-NN`,
decisão já registrada em `pesquisa/auditoria-2026/02-processo-visual.md` (sem dependência de
sistema nova; 5 nós não justifica layout automático, ver critério de reabertura em
`SKILL.md`). Tokens de marca lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`
(cores: `color.grove.500`, `color.lime.500`, `color.neutral.{chalk,ink,slate,white}`;
tipografia: `typography.fontFamily.{display,body}` — trio corrente Montserrat/Source Sans 3/IBM
Plex Mono, `brand/DESIGN.md` v3.1 §4.2), nunca hardcoded fora do JSON.

## diag-01

**Pergunta que o diagrama responde:** qual é a sequência de causa e efeito, segundo o padrão
que Peterson repete, entre assumir um fardo voluntário e chegar a algo com significado?

Sem seção de fonte de dados: não há número embutido no diagrama — é um padrão conceitual, não
uma série (ver `processo/07-verificacao.md`, item 2, que confirma a citação-base de Peterson —
"a terrível responsabilidade da vida" / "transformar o caos do potencial em ordem habitável",
*12 Rules for Life*, 2018, Regra 1 — mas a cadeia de cinco elos em si é, no próprio texto do
post, apresentada como leitura do autor sobre um padrão recorrente de Peterson, não uma citação
única e numerada a rastrear).

**Código Plotly executável** (testado com `python3` nesta etapa — gera `figuras/diag-01.svg` e
`figuras/diag-01.png`):

```python
import json
import os
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-11-partes-dificeis-de-uma-carreira-em-financas-teste-pipeline-v2"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

bg = tokens["color"]["neutral"]["chalk"]["$value"]
text_high = tokens["color"]["neutral"]["ink"]["$value"]
grove500 = tokens["color"]["grove"]["500"]["$value"]
lime500 = tokens["color"]["lime"]["500"]["$value"]
slate = tokens["color"]["neutral"]["slate"]["$value"]
white = tokens["color"]["neutral"]["white"]["$value"]
ink = tokens["color"]["neutral"]["ink"]["$value"]
font_display = tokens["typography"]["fontFamily"]["display"]["$value"][0]
font_body = tokens["typography"]["fontFamily"]["body"]["$value"][0]

fig = go.Figure()

NODE_W, NODE_H = 2.5, 1.3
GAP = 0.55

labels = ["Responsabilidade", "Dificuldade", "Competência", "Contribuição", "Significado"]
n = len(labels)
xs = [i * (NODE_W + GAP) for i in range(n)]
y = 0

for i, (x, label) in enumerate(zip(xs, labels)):
    is_last = i == n - 1
    # Lime só no elo final (acento único de "conquista", DESIGN.md v3.1 §4.3) —
    # os quatro elos intermediários ficam em Grove (estrutura em movimento).
    fill = lime500 if is_last else grove500
    text_color = ink if is_last else white
    fig.add_shape(
        type="rect",
        x0=x - NODE_W / 2, x1=x + NODE_W / 2,
        y0=y - NODE_H / 2, y1=y + NODE_H / 2,
        line=dict(color=fill, width=1.5),
        fillcolor=fill,
        layer="below",
    )
    fig.add_annotation(
        x=x, y=y, text=label, showarrow=False,
        font=dict(color=text_color, size=14, family=font_body),
        align="center",
    )
    if i < n - 1:
        x0 = x + NODE_W / 2 + 0.06
        x1 = xs[i + 1] - NODE_W / 2 - 0.06
        fig.add_annotation(
            x=x1, y=y, ax=x0, ay=y, xref="x", yref="y", axref="x", ayref="y",
            showarrow=True, arrowhead=2, arrowsize=1.1, arrowwidth=2,
            arrowcolor=slate, text="",
        )

# Anotação apontando para o ponto de chegada da cadeia — o elo que a peça existe para destacar
fig.add_annotation(
    x=xs[-1], y=y + NODE_H / 2 + 0.45,
    text="onde a cadeia chega",
    showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=1.5,
    arrowcolor=text_high, ax=0, ay=-30,
    font=dict(color=text_high, size=12, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    width=1200,
    height=420,
    margin=dict(l=40, r=40, t=90, b=40),
    xaxis=dict(visible=False, range=[-1.0, xs[-1] + NODE_W / 2 + 1.0]),
    yaxis=dict(visible=False, range=[-1.6, 1.9]),
    title=dict(
        text="A cadeia de Peterson: do fardo assumido ao significado",
        font=dict(color=text_high, size=18, family=font_display),
        x=0.02, xanchor="left",
    ),
)

os.makedirs(os.path.join(POST_DIR, "figuras"), exist_ok=True)
fig.write_image(os.path.join(POST_DIR, "figuras/diag-01.svg"))
fig.write_image(os.path.join(POST_DIR, "figuras/diag-01.png"), scale=2)
```

**Escolha de layout justificada:** cadeia linear, um nó por elo, da esquerda para a direita —
não um layout de força automática, porque com cinco nós numa sequência estritamente causal (sem
ramificação, sem ciclo) a disposição manual em linha reta já é a leitura mais direta possível;
um algoritmo de grafo introduziria variação de posição sem nenhum ganho de clareza.

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Diagrama de fluxo linear com cinco elos em sequência: "Responsabilidade" leva a
> "Dificuldade", que leva a "Competência", que leva a "Contribuição", que leva a "Significado"
> — o último elo destacado em verde-lima, com a nota "onde a cadeia chega". Ilustra o padrão
> que Jordan Peterson repete em livros, palestras e entrevistas sobre como assumir um fardo
> voluntário se converte, passo a passo, em algo com significado.

**Legenda (para exibição junto à figura em `post.md`):**

> O padrão que Peterson repete, de livro em palestra, de palestra em entrevista: assumir uma
> responsabilidade real empurra você para a dificuldade que ela exige; a dificuldade,
> enfrentada, vira competência; a competência se converte em contribuição; e é a contribuição
> que chega a significado.
