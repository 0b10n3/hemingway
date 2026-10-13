# Diagramas — "Coqueiros e cacaueiros"

Uma peça, decidida em `processo/02-estrutura.md` ("Visuais: onde e por quê", mantida no
adendo pós-crítica) e posicionada em `processo/04-draft-v3.md` (placeholder `diag-01`, logo
depois da definição de cacaueiros). Ferramenta: Plotly (quadrantes via `add_shape`, eixos e
rótulos via `add_annotation`), mesmo padrão de `graf-NN`. Tokens lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. O bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Nenhum `graf-NN` nem `info-NN`: os eixos são conceituais, não há série numérica real, e uma
peça só carrega a síntese (mesma conclusão de `02-estrutura.md`).

## diag-01

**Pergunta que o diagrama responde:** se coqueiros e cacaueiros entregam valor alto, em que
eles diferem?

**Fonte dos dados:** nenhum número embutido. Rótulos e definições vêm do próprio rascunho
(`processo/04-draft-v3.md`, parágrafos que definem "coqueiros" e "cacaueiros"), encurtados.

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-10-12-coqueiros-e-cacaueiros"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
mint = c["neutral"]["mint"]["$value"]
forest = c["forest"]["500"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body = stack("display"), stack("body")

fig = go.Figure()

# Plano conceitual 0-10 x 0-10, sem escala: os eixos não medem nada, só ordenam baixo -> alto.
# Quadrantes de cima (os dois que o autor nomeou) com o mesmo tratamento: mint + hairline
# forest. "Nenhuma é melhor que a outra" — nenhum dos dois ganha cor própria nem acento lime.
# Quadrantes de baixo: sem preenchimento, hairline mist, só a descrição neutra dos eixos.
GAP = 0.08
QUAD = {
    "coqueiros": (0, 5 - GAP, 5 + GAP, 10),
    "cacaueiros": (5 + GAP, 10, 5 + GAP, 10),
    "inf_esq": (0, 5 - GAP, 0, 5 - GAP),
    "inf_dir": (5 + GAP, 10, 0, 5 - GAP),
}


def quad(key, fill, line):
    x0, x1, y0, y1 = QUAD[key]
    fig.add_shape(type="rect", x0=x0, x1=x1, y0=y0, y1=y1, fillcolor=fill,
                  line=dict(color=line, width=1), layer="below")


def text(x, y, t, color, size, family=font_body, **kw):
    fig.add_annotation(x=x, y=y, text=t, showarrow=False, align="center",
                       font=dict(color=color, size=size, family=family), **kw)


quad("coqueiros", mint, forest)
quad("cacaueiros", mint, forest)
quad("inf_esq", bg, mist)
quad("inf_dir", bg, mist)

# Rótulos e definições: texto do próprio rascunho (processo/04-draft-v3.md), encurtado.
text(2.5, 8.1, "Coqueiros", forest, 28, family=font_display)
text(2.5, 6.6, "entregam valor relevante<br>com pouco ou nenhum<br>gasto de energia", ink, 16)
text(7.5, 8.1, "Cacaueiros", forest, 28, family=font_display)
text(7.5, 6.6, "também entregam muito valor,<br>mas pedem cultivo deliberado:<br>estudo, prática, manutenção", ink, 16)
text(2.5, 2.5, "valor baixo, energia baixa", slate, 14)
text(7.5, 2.5, "valor baixo, energia alta", slate, 14)


def axis_arrow(x0, y0, x1, y1):
    fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=2, arrowsize=1.1, arrowwidth=1.5,
                       arrowcolor=slate, text="")


# Eixos: setas sem ticks; só os extremos baixo/alto e o nome do eixo.
axis_arrow(0, -0.55, 10.3, -0.55)
axis_arrow(-0.55, 0, -0.55, 10.3)
text(0, -1.05, "baixa", slate, 14, xanchor="left")
text(10, -1.05, "alta", slate, 14, xanchor="right")
text(5, -1.05, "Energia de manutenção que a skill consome", ink, 16)
text(-1.05, 0, "baixo", slate, 14, textangle=-90, yanchor="bottom")
text(-1.05, 10, "alto", slate, 14, textangle=-90, yanchor="top")
text(-1.05, 5, "Valor que a skill entrega", ink, 16, textangle=-90)

fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-50, xanchor="left", yanchor="top",
                   showarrow=False, align="left",
                   text="Eixos conceituais, sem escala: a posição compara, não mede.",
                   font=dict(color=slate, size=13, family=font_body))

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=820, height=820,
    margin=dict(l=70, r=30, t=80, b=100),
    xaxis=dict(visible=False, range=[-1.4, 10.4]),
    yaxis=dict(visible=False, range=[-1.4, 10.4]),
    title=dict(text="Valor alto nos dois, energia de manutenção oposta",
               font=dict(color=ink, size=22, family=font_display), x=0.03, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** matriz 2×2 sem escala, como o autor sugeriu no apêndice do rascunho.
Os dois quadrantes de cima, os únicos que o autor nomeou, recebem o mesmo tratamento (`mint`
com hairline `forest`, nome em display `forest`): o texto diz "Nenhuma é melhor que a outra",
então nenhum ganha cor própria, e o `lime` fica de fora (não há ação nem conquista a marcar).
Os de baixo ficam sem preenchimento, com hairline `mist` e só a descrição neutra dos eixos em
`slate`, sem metáfora. Eixos são setas sem ticks, com os extremos "baixa/alta" e "baixo/alto"
e uma nota de que a posição compara e não mede. Descartados: pontos com coordenadas (dado
inventado com cara de gráfico), seta cacaueiro → coqueiro (antecipa "Não fique esperando um
coqueiro", descartada na etapa 2) e rótulos nos quadrantes inferiores.

**Gate de Tufte (etapa 9):** sem `rangemode="tozero"` por exceção justificada. Não há série
numérica nem barra: os eixos são conceituais, sem escala e sem ticks (`visible=False`), e o
`range=[-1.4, 10.4]` só enquadra o plano 0-10 com margem para setas e rótulos. Não há o que
truncar. Lie Factor: não se aplica, porque nenhum tamanho, área ou posição codifica dado (os
quadrantes têm o mesmo tamanho por construção, e a nota no rodapé diz que a posição compara e
não mede). Sem 3D, sombra, textura ou moldura: as bordas `width=1` são hairlines dos
quadrantes, não moldura da figura.

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Diagrama: matriz de dois eixos, sem escala. No eixo horizontal, a energia de manutenção que
> a skill consome, de baixa a alta; no vertical, o valor que ela entrega, de baixo a alto. No
> alto à esquerda, valor alto e energia baixa, ficam os coqueiros: entregam valor relevante
> com pouco ou nenhum gasto de energia. No alto à direita, valor alto e energia alta, ficam os
> cacaueiros: também entregam muito valor, mas pedem cultivo deliberado. Os dois quadrantes de
> baixo, valor baixo, ficam sem nome.

**Legenda:**

> Valor alto nos dois, energia de manutenção oposta. Coqueiros e cacaueiros entregam valor
> alto; o que os separa é quanta energia a skill consome para continuar dando resultado.
