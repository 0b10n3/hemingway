# Gráficos — "Renda Fixa, Condições Variáveis"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN")
e posicionadas em `processo/04-draft-v2.md` (seções "Percentual do CDI não é CDI mais spread" e
"Pós-fixado também oscila"). Tokens de marca lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

**Por que tabela e não curva.** Mesma restrição do post do CRA
(`posts/2026-09-28-o-certificado-nao-muda-o-devedor/graficos.md`): as duas peças são tabelas
no rascunho, e a Substack não renderiza tabela markdown. A tabela vira imagem (`go.Table`) com
as mesmas linhas, colunas e números. O autor cogitou um gráfico de linha para graf-01 (spread ×
nível do CDI) e preferiu a tabela; a escolha dele fica (`02-estrutura.md`). Descartados: curva
spread equivalente × CDI (graf-01) e curva PU × spread exigido (graf-02). Os dois seriam
legítimos, mas reescrevem a peça.

**Layout comum.** Tabela à esquerda, achado à direita com seta para a célula destacada em
`lime.300`. O achado fica fora da tabela porque as células de interesse do graf-01 não estão na
última linha nem na última coluna: uma seta vinda de baixo ou de dentro cruzaria outros números.
A seta para na borda da tabela, na altura das linhas destacadas; o fundo `lime.300` marca a célula.

## Dados (comum a graf-01 e graf-02)

Os dois CSVs são gerados pelas fórmulas do texto, não digitados. O bloco abaixo regenera
`graficos/dados/graf-01.csv` e `graficos/dados/graf-02.csv` e confere célula a célula contra a
tabela do rascunho (`processo/04-draft-v2.md`) e contra `processo/07-verificacao.md` (itens 1.1
e 1.5); se a fórmula quebrar, o `assert` falha.

```python
import csv
import os

POST_DIR = "posts/2026-10-15-renda-fixa-condicoes-variaveis"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)

# graf-01 — percentual do CDI -> CDI + spread, CDI constante.
# d = (1 + c)^(1/252) - 1;  1 + s = (1 + p·d)^252 / (1 + c)
rows01 = []
for c in (0.15, 0.1365, 0.10, 0.08):
    d = (1 + c) ** (1 / 252) - 1
    row = {"cdi_pct": round(c * 100, 4)}
    for p in (1.05, 1.10, 1.20):
        row[f"spread_{round(p * 100)}_pct"] = round(((1 + p * d) ** 252 / (1 + c) - 1) * 100, 4)
    rows01.append(row)
# confere com a tabela do draft v2 (12 células, 07-verificacao.md item 1.1)
draft01 = [["0,70", "1,41", "2,83"], ["0,64", "1,29", "2,59"],
           ["0,48", "0,96", "1,92"], ["0,39", "0,77", "1,55"]]
for r, esperado in zip(rows01, draft01):
    got = [f"{r[k]:.2f}".replace(".", ",") for k in ("spread_105_pct", "spread_110_pct", "spread_120_pct")]
    assert got == esperado, (got, esperado)

# graf-02 — PU / PU par de um papel bullet a CDI + 1,5%, 5 anos (du = 1.260).
# PU / PU par = [(1 + s_contrato) / (1 + s_mercado)]^(du/252)
S_CONTRATO, DU = 0.015, 1260
rows02 = []
for s in (0.02, 0.03, 0.045, 0.06):
    rows02.append({
        "spread_mercado_pct": round(s * 100, 4),
        "pu_pct_par": round(((1 + S_CONTRATO) / (1 + s)) ** (DU / 252) * 100, 4),
    })
# confere com a tabela do draft v2 (07-verificacao.md item 1.5)
assert [f"{r['pu_pct_par']:.1f}".replace(".", ",") for r in rows02] == ["97,6", "92,9", "86,4", "80,5"]

for name, rows in (("graf-01.csv", rows01), ("graf-02.csv", rows02)):
    with open(os.path.join(out, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
```

## graf-01

**Pergunta que o gráfico responde:** quanto vale, em CDI mais spread, um papel que paga um
percentual do CDI, conforme o nível dos juros?

**Fonte dos dados:** cálculo próprio, fórmula do texto (CDI constante ao longo do prazo, 252
dias úteis). Nível de 13,65%: CDI efetivo com a meta Selic em 13,75% (BCB/SGS 4389 e 432,
acesso em 2026-10-15). Conferido em `processo/07-verificacao.md`, itens 1.1, 1.2 e 3.24
(Confere).

**Dados:** `posts/2026-10-15-renda-fixa-condicoes-variaveis/graficos/dados/graf-01.csv`

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-10-15-renda-fixa-condicoes-variaveis"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
white = c["neutral"]["white"]["$value"]
forest = c["forest"]["500"]["$value"]
lime = c["lime"]["300"]["$value"]
lime_text = c["lime"]["900"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))


def pct(v):
    return f"{v:.2f}".replace(".", ",") + "%"


spread_cols = ["spread_105_pct", "spread_110_pct", "spread_120_pct"]
values = [[pct(v) for v in df["cdi_pct"]]] + [["CDI + " + pct(v) for v in df[col]] for col in spread_cols]

# Destaque: os mesmos 110% do CDI com o CDI de hoje (13,65%) e com o CDI a 10% — o par que o
# texto lê ("viram CDI + 0,96% se o CDI cair para 10%").
hit = df.index[df["cdi_pct"].isin([13.65, 10.0])].tolist()
fills = [[white] * len(df) for _ in values]
fonts = [[ink] * len(df) for _ in values]
for i in hit:
    fills[2][i] = lime
    fonts[2][i] = lime_text

TABLE_X = 0.66
fig = go.Figure(go.Table(
    columnwidth=[0.9, 1, 1, 1],
    header=dict(
        values=["<b>CDI ao ano</b>", "<b>105% do CDI</b>", "<b>110% do CDI</b>", "<b>120% do CDI</b>"],
        fill_color=forest, line_color=forest, align="center", height=50,
        font=dict(color=bg, size=17, family=font_body),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="center", height=46,
        font=dict(color=fonts, size=19, family=font_data),
    ),
    domain=dict(x=[0, TABLE_X], y=[0, 1]),
))

# Anotação à direita da tabela, seta para a altura da divisa entre as duas linhas destacadas
# (vinda de fora para não cruzar a coluna de 120%).
fig.add_annotation(
    xref="paper", yref="paper", x=TABLE_X + 0.005, y=0.455, ax=50, ay=0, showarrow=True,
    arrowhead=2, arrowwidth=1.5, arrowcolor=lime_text, xanchor="left", align="left",
    text="Os mesmos 110% do CDI:<br>CDI + 1,29% com o CDI<br>a 13,65%, CDI + 0,96%<br>"
         "se o CDI cair para 10%.<br>O risco da empresa não<br>caiu. A compensação, sim.",
    font=dict(color=lime_text, size=15, family=font_body),
)
fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-30, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Spread equivalente: 1 + s = (1 + p·d)^252 / (1 + c), com d = (1 + c)^(1/252) − 1. "
         "CDI de 13,65%: meta Selic em 13,75%.<br>Cálculo próprio, com CDI constante ao longo do prazo.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=440,
    margin=dict(l=40, r=40, t=80, b=100),
    title=dict(text="O percentual do CDI é um spread que encolhe com os juros",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** tabela-imagem 4 × 3, igual ao rascunho (ver "Por que tabela e não curva"
acima). Descartado: linhas de spread equivalente × nível do CDI, uma por percentual.

**Anotação:** as duas células do 110% do CDI que o texto compara (13,65% → CDI + 1,29%; 10% →
CDI + 0,96%) têm fundo `lime.300` e uma seta (`add_annotation`) com o achado. Gate de Tufte:
sem eixo, sem 3D, sem sombra; a ênfase é só cor de fundo em duas células, então não há Lie
Factor a declarar.

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Tabela com o spread sobre o CDI equivalente a três percentuais do CDI, em quatro níveis de
> juros, com o CDI constante ao longo do prazo. Com o CDI a 15% ao ano: 105% do CDI equivale a
> CDI + 0,70%; 110%, a CDI + 1,41%; 120%, a CDI + 2,83%. Com o CDI a 13,65%: CDI + 0,64%,
> CDI + 1,29% e CDI + 2,59%. A 10%: CDI + 0,48%, CDI + 0,96% e CDI + 1,92%. A 8%: CDI + 0,39%,
> CDI + 0,77% e CDI + 1,55%. Os mesmos 110% do CDI que hoje valem CDI + 1,29% viram CDI + 0,96% se
> o CDI cair para 10%: o percentual do CDI é um spread que encolhe quando os juros caem.

**Legenda:**

> O percentual do CDI é um spread que encolhe com os juros. Cálculo próprio, com CDI constante
> ao longo do prazo.

## graf-02

**Pergunta que o gráfico responde:** quanto cai o preço de uma debênture a CDI + 1,5%, com
cinco anos pela frente, quando o mercado passa a exigir um spread maior do devedor?

**Fonte dos dados:** cálculo próprio, fórmula do texto (metodologia Anbima para debêntures
remuneradas pelo DI, papel bullet: a parte do DI se cancela). Prazo de cinco anos, du = 1.260.
Conferido em `processo/07-verificacao.md`, itens 1.5 e 1.6 (Confere). O denominador segue a
correção K-02 da verificação (PU par, não VNA).

**Dados:** `posts/2026-10-15-renda-fixa-condicoes-variaveis/graficos/dados/graf-02.csv`

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-10-15-renda-fixa-condicoes-variaveis"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
white = c["neutral"]["white"]["$value"]
forest = c["forest"]["500"]["$value"]
lime = c["lime"]["300"]["$value"]
lime_text = c["lime"]["900"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02.csv"))


def num(v):
    return f"{v:.1f}".replace(".", ",")


values = [["CDI + " + num(v) + "%" for v in df["spread_mercado_pct"]],
          [num(v) + "%" for v in df["pu_pct_par"]]]

# Destaque: o maior spread da tabela — o papel a CDI + 1,5% passa a valer 80,5% da curva.
hit = [int(df["spread_mercado_pct"].idxmax())]
fills = [[white] * len(df) for _ in values]
fonts = [[ink] * len(df) for _ in values]
for i in hit:
    fills[1][i] = lime
    fonts[1][i] = lime_text

TABLE_X = 0.6
fig = go.Figure(go.Table(
    columnwidth=[1.15, 1],
    header=dict(
        values=["<b>Spread exigido pelo mercado</b>", "<b>PU em % do valor na curva</b>"],
        fill_color=forest, line_color=forest, align="center", height=50,
        font=dict(color=bg, size=17, family=font_body),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="center", height=46,
        font=dict(color=fonts, size=19, family=font_data),
    ),
    domain=dict(x=[0, TABLE_X], y=[0, 1]),
))

# Anotação à direita da tabela, seta para a linha destacada (última linha, coluna do PU).
fig.add_annotation(
    xref="paper", yref="paper", x=TABLE_X + 0.005, y=0.19, ax=50, ay=0, showarrow=True,
    arrowhead=2, arrowwidth=1.5, arrowcolor=lime_text, xanchor="left", align="left",
    text="Com o mercado exigindo CDI + 6,0%,<br>o papel a CDI + 1,5% vale 80,5%<br>"
         "do valor na curva. Cada ponto a mais<br>de spread tira cerca de 5% do preço.",
    font=dict(color=lime_text, size=15, family=font_body),
)
fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-30, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Debênture a CDI + 1,5%, cinco anos até o vencimento. "
         "PU / PU par = [(1 + s contrato) / (1 + s mercado)]^(du/252), du = 1.260.<br>"
         "Cálculo próprio. Papel sem amortizações nem juros intermediários; "
         "com pagamentos periódicos, a sensibilidade é menor.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=440,
    margin=dict(l=40, r=40, t=80, b=100),
    title=dict(text="Pós-fixado também oscila: o preço segue o spread do devedor",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
```

**Escolha de tipo:** tabela-imagem 4 × 2, igual ao rascunho. Descartado: curva PU × spread
exigido. Mostraria a convexidade, mas o texto não fala dela e seria mudança de conteúdo.

**Anotação:** a célula de CDI + 6,0% (80,5%) tem fundo `lime.300` e seta com o achado: cada
ponto de spread a mais tira cerca de 5% do preço (duration de spread perto de cinco anos,
`07-verificacao.md` item 1.6). Gate de Tufte: sem eixo nem ênfase de área; nenhum Lie Factor a
declarar.

**Alt-text (para o placeholder `graf-02` em `post.md`):**

> Tabela com o preço de uma debênture a CDI + 1,5%, com cinco anos até o vencimento e sem
> pagamentos intermediários, em porcentagem do valor na curva, conforme o spread que o mercado
> passa a exigir. Se o mercado exige CDI + 2,0%, o papel vale 97,6% do valor na curva; CDI +
> 3,0%, 92,9%; CDI + 4,5%, 86,4%; CDI + 6,0%, 80,5%. Cada ponto percentual a mais de spread
> tira cerca de 5% do preço: pós-fixado não oscila com o CDI, mas oscila com o devedor.

**Legenda:**

> Pós-fixado também oscila: o preço segue o spread exigido do devedor. Cálculo próprio. Papel
> sem amortizações nem juros intermediários; com pagamentos periódicos, a sensibilidade é
> menor.
