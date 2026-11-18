# Diagramas — "Cara, eu ganho. Coroa, eu não perco."

Duas peças, decididas em `processo/02-estrutura.md` ("Visuais — critério da etapa 2") e
posicionadas em `processo/04-draft-v2.md` (placeholders `diag-01`, em "Uma NTN-F feita de LTNs",
logo depois da tabela da réplica, e `diag-02`, em "A moeda aparece", logo depois do parágrafo do
arredondamento). São duas figuras, e não um painel duplo, pelo motivo registrado em
`02-estrutura.md`: cada uma ilustra a tabela de uma subseção, e o painel duplo encolhe na largura
do celular. Ferramenta: Plotly (caixas e trilhos via `add_shape`, textos e pontas de seta via
`add_annotation`), mesmo padrão de `graf-NN`. Tokens lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Os blocos rodam a partir da raiz do repositório
(`pipelines/hemingway/`) e foram testados com `python3` nesta etapa.

Nenhum `graf-NN` nem `info-NN`: não há série real (o exemplo é estilizado por decisão do autor), e
cada peça responde à própria pergunta.

**Números.** Todos vêm do cálculo próprio conferido em `processo/07-verificacao.md` (tabela
"Números, item a item") e em
`_revisoes/2026-11-18_2026-11-18-cara-eu-ganho-coroa-eu-nao-perco_calculo.md`, com as correções
C1 a C12 aceitas pelo autor (sem a convenção do Tesouro). Cada bloco tem um `assert` que confere
a aritmética exibida antes de desenhar.

**Formato para o celular.** As duas figuras são verticais (760 × 925 e 760 × 1.122 px, exportadas
em escala 2), com o tempo descendo pela esquerda. Uma linha do tempo horizontal com quatro datas
espremeria os valores na largura do celular. Conferido reduzindo os PNG a 343 px de largura (tela
de 375 px menos as margens): nada cortado, nenhum texto sobreposto; o menor texto fora do rodapé
fica perto de 9 px.

**Nota de renderização:** Montserrat, Source Sans 3 e IBM Plex Mono não estão instaladas neste
ambiente com esses nomes (a IBM Plex Mono existe só como "BlexMono Nerd Font"). O PNG saiu com as
fontes de reserva da pilha: Arial (Arimo) na manchete, a sans do sistema (Noto Sans) no corpo e
Courier New (Cousine) nos números. O SVG guarda a pilha completa e renderiza nas fontes da marca
onde elas existirem. Se o autor quiser o PNG nas fontes da marca, basta instalá-las e rodar os
blocos de novo.

## diag-01

**Pergunta que o diagrama responde:** como três LTNs, uma por data de pagamento, formam a mesma
NTN-F, e por que o preço dela é a soma do custo dos três lotes?

**Fonte dos dados:** cálculo próprio, com taxas ilustrativas (14,00%, 14,30% e 14,55% ao ano nos
vértices de 126, 252 e 378 dias úteis). Itens 4 a 9 de `processo/07-verificacao.md`. As
quantidades aparecem com quatro casas (0,0488 / 0,0488 / 1,0488), e o rodapé dá as exatas
(0,0488088482 e 1,0488088482, C1): com as de quatro casas, dois dos três custos não fecham no
centavo, e o rodapé evita que o leitor que refizer a conta ache um erro.

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
card = c["neutral"]["white"]["$value"]   # theme.light.card
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # ênfase: traço do que soma para o preço
grove_text = c["grove"]["700"]["$value"]  # texto em ênfase: grove.700 passa 4,5:1 sobre Chalk/branco
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Números: cálculo próprio conferido em processo/07-verificacao.md (itens 4 a 9, C1 aceita).
VERTICES = [  # (dias úteis, taxa, quantidade exibida, fluxo, custo hoje), por título
    ("126 du", "14,00%", "0,0488", "48,81", "45,71"),
    ("252 du", "14,30%", "0,0488", "48,81", "42,70"),
    ("378 du", "14,55%", "1,0488", "1.048,81", "855,47"),
]
PRECO = "943,88"
# Conferência: a soma exibida dos custos fecha no preço exibido.
assert sum(int(v[4].replace(",", "")) for v in VERTICES) == int(PRECO.replace(",", ""))

W, H = 760, 925
X_AXIS = 104                 # linha do tempo
NL, NR = 130, 334            # coluna NTN-F
EQ = 364                     # sinal de igual
LL, LR = 394, 690            # coluna réplica (LTNs)
RAIL = 724                   # trilho que leva os custos até "hoje"
Y_HOJE = 262
ROWS = [440, 600, 760]       # centro de cada data
HALF = 70                    # meia altura das caixas de LTN

fig = go.Figure()


def text(x, y, t, size, color=ink, family=font_body, **kw):
    fig.add_annotation(x=x, y=y, text=t, showarrow=False,
                       font=dict(size=size, color=color, family=family), **kw)


def rect(x0, y0, x1, y1, color, width=2):
    fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1, fillcolor=card,
                  line=dict(color=color, width=width), layer="below")


def seg(x0, y0, x1, y1, color, width=2, dash="solid"):
    fig.add_shape(type="line", x0=x0, y0=y0, x1=x1, y1=y1,
                  line=dict(color=color, width=width, dash=dash))


def arrow(x0, y0, x1, y1, color, width=2):
    fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=2, arrowsize=1.2, arrowwidth=width,
                       arrowcolor=color, text="")


# Manchete e linha de apoio
text(24, 44, "<b>Três LTNs, a mesma NTN-F</b>", 34, ink, font_display, xanchor="left")
text(24, 104, "Cada fluxo da NTN-F é um lote de LTN da mesma data,<br>"
              "e o preço da NTN-F é a soma do custo dos três lotes.",
     20, slate, xanchor="left", align="left")

# Cabeçalhos das colunas
text((NL + NR) / 2, 176, "<b>NTN-F</b> (um título)", 21)
text((LL + LR) / 2, 176, "<b>Réplica</b> (três LTNs)", 21)

# Linha do tempo: vertical, o tempo desce. Sem escala: as datas são só ordem.
seg(X_AXIS, Y_HOJE, X_AXIS, ROWS[-1] + HALF, slate)
arrow(X_AXIS, ROWS[-1] + HALF - 20, X_AXIS, ROWS[-1] + HALF + 18, slate)
fig.add_trace(go.Scatter(x=[X_AXIS] * 4, y=[Y_HOJE] + ROWS, mode="markers",
                         marker=dict(size=13, color=slate), hoverinfo="skip", showlegend=False))
for y, lab in zip([Y_HOJE] + ROWS, ["hoje"] + [v[0] for v in VERTICES]):
    text(X_AXIS - 14, y, f"<b>{lab}</b>", 21, ink, xanchor="right")

# Hoje: o preço da NTN-F igual à soma dos custos (o ponto do diagrama, em grove)
rect(NL, Y_HOJE - 54, NR, Y_HOJE + 54, grove, 2.5)
text((NL + NR) / 2, Y_HOJE - 24, "preço justo", 20, slate)
text((NL + NR) / 2, Y_HOJE + 18, f"<b>R$ {PRECO}</b>", 30, grove_text, font_data)
text(EQ, Y_HOJE, "<b>=</b>", 34, grove_text)
rect(LL, Y_HOJE - 54, LR, Y_HOJE + 54, grove, 2.5)
text((LL + LR) / 2, Y_HOJE - 28, "soma do custo dos lotes", 20, slate)
text((LL + LR) / 2, Y_HOJE + 2, " + ".join(v[4] for v in VERTICES), 20, ink, font_data)
text((LL + LR) / 2, Y_HOJE + 32, f"<b>= R$ {PRECO}</b>", 24, grove_text, font_data)

# A NTN-F é um objeto só, com três pagamentos; a réplica são três caixas separadas
rect(NL, ROWS[0] - HALF, NR, ROWS[-1] + HALF, slate)
for y0, y1 in zip(ROWS, ROWS[1:]):
    seg(NL + 16, (y0 + y1) / 2, NR - 16, (y0 + y1) / 2, mist, 1.5, "dot")

for y, (_, taxa, qtd, fluxo, custo) in zip(ROWS, VERTICES):
    text((NL + NR) / 2, y - 18, "paga", 20, slate)
    text((NL + NR) / 2, y + 16, f"<b>R$ {fluxo}</b>", 24, ink, font_data)
    text(EQ, y, "=", 30, slate)
    rect(LL, y - HALF + 4, LR, y + HALF - 4, slate)
    text((LL + LR) / 2, y - 34, f"<b>{qtd} LTN</b> a {taxa}", 21, ink, font_data)
    text((LL + LR) / 2, y, f"paga R$ {fluxo}", 20, slate)
    text((LL + LR) / 2, y + 34, f"custa hoje <b>R$ {custo}</b>", 21, grove_text)
    seg(LR, y + 34, RAIL, y + 34, grove, 2.5)

# Trilho: os três custos sobem até "hoje" e somam o preço
seg(RAIL, ROWS[-1] + 34, RAIL, Y_HOJE, grove, 2.5)
arrow(RAIL, Y_HOJE, LR + 2, Y_HOJE, grove, 2.5)

# Rodapé
text(18, 884, "Valores em R$, por título; du = dias úteis. Cálculo próprio, taxas ilustrativas.<br>"
              "Quantidade de LTN = fluxo ÷ 1.000 (exatas: 0,0488088482 e 1,0488088482).",
     17, slate, xanchor="left", align="left")

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=W, height=H,
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis=dict(visible=False, range=[0, W], fixedrange=True),
    yaxis=dict(visible=False, range=[H, 0], fixedrange=True),  # y cresce para baixo
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** duas colunas sobre uma linha do tempo vertical. À esquerda, a NTN-F é uma
caixa só, com os três pagamentos dentro; à direita, a réplica são três caixas separadas, uma por
data. A forma diz "um título = três lotes" antes de o leitor ler um número. Em cada data, um "="
liga o pagamento da NTN-F ao do lote de LTN. No topo, na linha de hoje, o preço justo e a soma dos
custos. Ênfase da marca: o que soma para o preço está em `grove` (as duas caixas de hoje, o custo
de cada lote e o trilho que leva os três custos até hoje, com a ponta de seta na soma); os fluxos
são contexto, em `slate`/`ink`. Texto em ênfase usa `grove.700`, porque `grove.500` não passa
4,5:1 como texto. Sem `lime`: não há ação nem conquista a marcar. Descartados: a linha do tempo
horizontal com setas de fluxo para cima e para baixo (o diagrama de fluxo de caixa clássico),
porque quatro colunas de rótulos não cabem na largura do celular; setas com comprimento
proporcional ao valor, porque o principal (R$ 1.048,81) é 21 vezes o cupom e as setas de cupom
sumiriam; o PU de cada LTN, que está na tabela logo acima e não muda a forma.

**Gate de Tufte (etapa 9):** sem eixo numérico, então `rangemode="tozero"` não se aplica: os
`range` só enquadram o desenho em pixels. Nenhuma altura, área ou comprimento codifica valor
(todas as caixas de LTN têm o mesmo tamanho, e o espaçamento entre as datas é igual, sem escala de
tempo). Lie Factor: não se aplica. Sem 3D, sombra, textura ou moldura.

**Alt-text (para o placeholder `diag-01` em `post.md`, 123 caracteres):**

> Diagrama: a NTN-F paga R$ 48,81, R$ 48,81 e R$ 1.048,81; três lotes de LTN das mesmas datas
> pagam igual e custam R$ 943,88.

O texto atual do placeholder em `04-draft-v2.md` ("os três fluxos da NTN-F hipotética e as três
LTNs das mesmas datas que os replicam, com quantidade e custo de cada lote") tem 130 caracteres e
dispara o aviso de `scripts/checar_post.py`. Ele passa a ser a legenda.

**Legenda:**

> Diagrama: os três fluxos da NTN-F hipotética e as três LTNs das mesmas datas que os replicam,
> com quantidade e custo de cada lote.

## diag-02

**Pergunta que o diagrama responde:** de onde vem o dinheiro da mesa hoje, e por que ela não fica
devendo em nenhuma das três datas?

**Fonte dos dados:** cálculo próprio, itens 12 a 18 de `processo/07-verificacao.md` e correções
C4 e C5 aceitas. Hoje: compra de 100.000 NTN-F por −R$ 94.368.087,53, venda das LTNs da réplica
por +R$ 94.388.697,41, líquido de +R$ 20.609,88; separada a reserva de R$ 302,60, sobra o lucro
travado de R$ 20.307,28. Em cada data: a NTN-F paga 100.000 × 48,808848 (R$ 4.880.884,82, e R$
104.880.884,82 no vencimento), as LTNs cobram R$ 4.881.000,00 (R$ 104.881.000,00 no vencimento),
e faltam R$ 115,18, que a reserva cobre (C4: "a mesa deve 4.881.000 e recebe 4.880.884,82"). Os
valores brutos das datas não estão no corpo do texto; estão no laudo da etapa 7, e o diagrama os
mostra para que os R$ 115,18 de cada data apareçam como conta, não como afirmação (C5).

**Código Plotly executável** (gera `figuras/diag-02.svg` e `figuras/diag-02.png`):

```python
import json
import os
from decimal import Decimal

import plotly.graph_objects as go

POST_DIR = "posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
card = c["neutral"]["white"]["$value"]   # theme.light.card
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # ênfase: traço da reserva que cobre as datas
grove_text = c["grove"]["700"]["$value"]  # texto em ênfase: grove.700 passa 4,5:1 sobre branco
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Números: processo/07-verificacao.md, itens 12 a 18 e C4/C5 aceitas. Fluxos da mesa, em R$.
# Em cada data: +100.000 × 48,808848 (NTN-F) − lote × 1.000 (LTNs) + 115,18 (reserva) = 0,00.
HOJE = [  # (rótulo, valor, ênfase)
    ("compra 100.000 NTN-F", "−94.368.087,53", False),
    ("vende as LTNs da réplica", "+94.388.697,41", False),
    ("líquido na montagem", "+20.609,88", False),
    ("separa a reserva", "−302,60", True),
    ("<b>lucro travado</b>", "<b>+20.307,28</b>", True),
]
DATAS = [  # (vértice, NTN-F paga, lote de LTN, LTNs cobram)
    ("126 du", "+4.880.884,82", "4.881", "−4.881.000,00"),
    ("252 du", "+4.880.884,82", "4.881", "−4.881.000,00"),
    ("378 du", "+104.880.884,82", "104.881", "−104.881.000,00"),
]
FALTA = "115,18"


def brl(s):  # "−94.368.087,53" → Decimal("-94368087.53")
    s = s.replace("<b>", "").replace("</b>", "").replace("−", "-")
    return Decimal(s.replace(".", "").replace(",", "."))


# Conferência: cada caixa fecha. Hoje, a montagem dá o lucro; em cada data, o saldo é zero.
v = [brl(x[1]) for x in HOJE]
assert v[0] + v[1] == v[2] and v[2] + v[3] == v[4]
assert all(brl(ntnf) + brl(ltn) + brl(FALTA) == 0 for _, ntnf, _, ltn in DATAS)

W = 760
X_AXIS = 104                 # linha do tempo
BL, BR = 130, 690            # caixas
TL, TR = BL + 18, BR - 18    # texto: rótulo à esquerda, valor alinhado à direita
RAIL = 724                   # trilho da reserva
LH = 34                      # altura de linha

fig = go.Figure()


def text(x, y, t, size, color=ink, family=font_body, **kw):
    fig.add_annotation(x=x, y=y, text=t, showarrow=False,
                       font=dict(size=size, color=color, family=family), **kw)


def rect(x0, y0, x1, y1, color, width=2):
    fig.add_shape(type="rect", x0=x0, y0=y0, x1=x1, y1=y1, fillcolor=card,
                  line=dict(color=color, width=width), layer="below")


def seg(x0, y0, x1, y1, color, width=2, dash="solid"):
    fig.add_shape(type="line", x0=x0, y0=y0, x1=x1, y1=y1,
                  line=dict(color=color, width=width, dash=dash))


def arrow(x0, y0, x1, y1, color, width=2):
    fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=2, arrowsize=1.2, arrowwidth=width,
                       arrowcolor=color, text="")


def ledger(y, label, value, emph=False, size=22):
    color = grove_text if emph else ink
    text(TL, y, label, size, color if emph else slate, xanchor="left")
    text(TR, y, value, size, color, font_data, xanchor="right")


# Manchete e linha de apoio
text(24, 44, "<b>Ganha hoje, não perde depois</b>", 34, ink, font_display, xanchor="left")
text(24, 104, "A mesa compra 100.000 NTN-F e vende a réplica. Nas três datas,<br>"
              "a NTN-F paga as LTNs, e a reserva cobre o que falta.",
     20, slate, xanchor="left", align="left")
text(TL, 172, "Fluxos da mesa, em R$", 19, slate, xanchor="left")

# Hoje: montagem
top = 196
y_hoje = [top + 32 + i * LH for i in range(2)] + [top + 32 + 2 * LH + 14 + i * LH for i in range(2)]
y_hoje.append(y_hoje[-1] + LH + 16)
bottom = y_hoje[-1] + 30
rect(BL, top, BR, bottom, slate)
for y, (lab, val, emph) in zip(y_hoje, HOJE):
    ledger(y, lab, val, emph, 25 if "lucro" in lab else 22)
seg(TL, y_hoje[1] + 23, TR, y_hoje[1] + 23, mist, 1.5)
seg(TL, y_hoje[3] + 24, TR, y_hoje[3] + 24, mist, 1.5)
y_reserva = y_hoje[3]
centers = [(top + bottom) / 2]

# Datas: a NTN-F paga, as LTNs cobram, a reserva cobre os R$ 115,18 do arredondamento
y = bottom + 34
y_cobre = []
for vert, ntnf, lote, ltn in DATAS:
    b_top = y
    rows = [b_top + 30 + i * LH for i in range(3)]
    rows.append(rows[-1] + LH + 12)
    b_bot = rows[-1] + 28
    rect(BL, b_top, BR, b_bot, slate)
    ledger(rows[0], "a NTN-F paga", ntnf)
    ledger(rows[1], f"{lote} LTNs vencem", ltn)
    ledger(rows[2], "a reserva cobre o que falta", f"+{FALTA}", True)
    seg(TL, rows[2] + 22, TR, rows[2] + 22, mist, 1.5)
    ledger(rows[3], "saldo na data", "<b>0,00</b>")
    y_cobre.append(rows[2])
    centers.append((b_top + b_bot) / 2)
    y = b_bot + 26

# Trilho da reserva: sai de "hoje" e entrega R$ 115,18 em cada data
seg(BR, y_reserva, RAIL, y_reserva, grove, 2.5)
seg(RAIL, y_reserva, RAIL, y_cobre[-1], grove, 2.5)
for yc in y_cobre:
    arrow(RAIL, yc, BR + 2, yc, grove, 2.5)

# Linha do tempo: vertical, o tempo desce. Sem escala: as datas são só ordem.
seg(X_AXIS, centers[0], X_AXIS, centers[-1] + 40, slate)
arrow(X_AXIS, centers[-1] + 30, X_AXIS, centers[-1] + 70, slate)
fig.add_trace(go.Scatter(x=[X_AXIS] * 4, y=centers, mode="markers",
                         marker=dict(size=13, color=slate), hoverinfo="skip", showlegend=False))
for yc, lab in zip(centers, ["hoje"] + [d[0] for d in DATAS]):
    text(X_AXIS - 14, yc, f"<b>{lab}</b>", 21, ink, xanchor="right")

# Rodapé (um "R$" por anotação: dois cifrões na mesma string viram LaTeX no Plotly)
foot = y + 20
text(18, foot, "Cálculo próprio; du = dias úteis. Lotes arredondados para cima: 4.881, 4.881<br>"
               "e 104.881 LTNs. A reserva de R$ 302,60 é o valor hoje dos 115,18 de cada data.",
     17, slate, xanchor="left", align="left")

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=W, height=int(foot + 50),
    margin=dict(l=0, r=0, t=0, b=0),
    xaxis=dict(visible=False, range=[0, W], fixedrange=True),
    yaxis=dict(visible=False, range=[foot + 50, 0], fixedrange=True),  # y cresce para baixo
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-02.svg"))
fig.write_image(os.path.join(out_dir, "diag-02.png"), scale=2)
```

**Escolha de layout:** a mesma linha do tempo vertical do `diag-01`, com uma caixa por data em
forma de extrato: rótulo à esquerda, valor com sinal à direita, do ponto de vista da mesa. Hoje, a
montagem fecha no lucro travado; em cada data, a NTN-F paga, as LTNs vencem, a reserva cobre os R$
115,18, e o saldo da data é 0,00. Um trilho sai da linha "separa a reserva" e entrega os R$ 115,18
em cada data, que é o que a C5 pediu para o próprio desenho mostrar. Ênfase da marca em `grove`:
a reserva, o trilho e o lucro travado; o resto é contexto. Manchete trocada em relação à sugestão
de `02-estrutura.md` ("Dinheiro hoje, nada a pagar depois"): com a C5, há R$ 115,18 a pagar em cada
data, cobertos pela reserva, e "nada a pagar" ficaria errado. "Ganha hoje, não perde depois" é a
moeda do título dita pela mesa, e o saldo zero de cada data a sustenta. Descartados: duas colunas
(NTN-F e LTNs) com setas de uma para a outra em cada data, porque os valores de nove dígitos não
cabem lado a lado na largura do celular; omitir os valores brutos e mostrar só o líquido de cada
data, porque aí os R$ 115,18 apareceriam sem a conta que os produz.

**Gate de Tufte (etapa 9):** sem eixo numérico; `rangemode="tozero"` não se aplica. Nenhuma
dimensão visual codifica valor: as três caixas das datas têm o mesmo tamanho, embora o vencimento
movimente 21 vezes mais dinheiro, e o espaçamento entre as datas não é escala de tempo. Lie
Factor: não se aplica. Sem 3D, sombra, textura ou moldura.

**Alt-text (para o placeholder `diag-02` em `post.md`, 119 caracteres):**

> Diagrama: a mesa trava R$ 20.307,28 hoje; em cada data, a NTN-F paga as LTNs e a reserva cobre
> os R$ 115,18 que faltam.

A legenda nova da C5 tem 202 caracteres e, posta no placeholder, dispararia o aviso de
`scripts/checar_post.py`. Por isso fica como legenda, e o placeholder leva o alt-text acima.

**Legenda (C5):**

> Diagrama: os fluxos da carteira de arbitragem. A mesa recebe dinheiro hoje e, nas três datas, a
> NTN-F comprada paga as LTNs vendidas, menos os R$ 115,18 de cada data, cobertos pela reserva de
> R$ 302,60.
