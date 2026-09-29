# Gráficos — "O Certificado Não Muda o Devedor"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN")
e posicionadas em `processo/04-draft-v1.md` (placeholders `[graf-01]` e `[graf-02]`). Tokens de
marca lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir
da raiz do repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

**Por que tabela e não curva.** As duas peças são tabelas no rascunho do autor, e a Substack
não renderiza tabela markdown. A restrição é de renderização, não de conteúdo: a tabela vira
imagem (`go.Table`) com as mesmas linhas e colunas. Transformar em curva mudaria o que o autor
mostra (quatro cenários discretos, quatro prazos discretos) e é decisão dele, não desta etapa.
Descartados: gráfico de linha perda da carteira → perda da sênior (graf-01) e taxa de empate ×
prazo (graf-02). Os dois seriam legítimos, mas reescrevem a peça.

## Dados (comum a graf-01 e graf-02)

Os dois CSVs são gerados pelas fórmulas do texto, não digitados. O bloco abaixo regenera
`graficos/dados/graf-01.csv` e `graficos/dados/graf-02.csv` e confere contra a tabela do
rascunho e contra `processo/07-verificacao.md` (item 1.3); se a fórmula quebrar, o `assert` falha.

```python
import csv
import os

POST_DIR = "posts/2026-09-28-o-certificado-nao-muda-o-devedor"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)

# graf-01 — subordinação. Carteira R$ 100 mi, subordinada S = 20%.
# perda da sênior = max(0, L - S) / (1 - S); perda da subordinada = min(L, S) / S
S = 0.20
rows01 = []
for L in (0.05, 0.15, 0.20, 0.30):
    rows01.append({
        "perda_carteira_pct": round(L * 100, 4),
        "perda_subordinada_pct": round(min(L, S) / S * 100, 4),
        "perda_senior_pct": round(max(0.0, L - S) / (1 - S) * 100, 4),
    })
assert [r["perda_subordinada_pct"] for r in rows01] == [25, 75, 100, 100]
assert [r["perda_senior_pct"] for r in rows01] == [0, 0, 0, 12.5]

# graf-02 — empate isento × tributado, bullet, capitalização anual, IPCA constante.
# regra de bolso: r_i / (1 - t)
# empate: 1 + r_t = [((1+pi)(1+r_i))^T - 1) / (1 - t) + 1]^(1/T) / (1 + pi)
PI, RI = 0.04, 0.07
rows02 = []
for T, t in ((1, 0.175), (2, 0.15), (5, 0.15), (10, 0.15)):
    bolso = RI / (1 - t)
    empate = ((((1 + PI) * (1 + RI)) ** T - 1) / (1 - t) + 1) ** (1 / T) / (1 + PI) - 1
    rows02.append({
        "prazo_anos": T,
        "aliquota_pct": t * 100,
        "regra_bolso_real_pct": round(bolso * 100, 4),
        "empate_correto_real_pct": round(empate * 100, 4),
    })
# confere com 07-verificacao.md, item 1.3
assert [r["empate_correto_real_pct"] for r in rows02] == [9.3007, 8.8018, 8.5196, 8.1795]

for name, rows in (("graf-01.csv", rows01), ("graf-02.csv", rows02)):
    with open(os.path.join(out, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
```

## graf-01

**Pergunta que o gráfico responde:** numa carteira com 20% de subordinação, a partir de que
perda a série sênior começa a perder?

**Fonte dos dados:** exemplo hipotético do texto (cálculo próprio). Carteira de R$ 100 mi,
sênior de R$ 80 mi, subordinada de R$ 20 mi; perda da sênior = max(0, L − S)/(1 − S), perda da
subordinada = min(L, S)/S. Conferido em `processo/07-verificacao.md`, itens 1.7-1.8 ([OK]).

**Dados:** `posts/2026-09-28-o-certificado-nao-muda-o-devedor/graficos/dados/graf-01.csv`

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-28-o-certificado-nao-muda-o-devedor"
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
    return f"{v:.1f}".rstrip("0").rstrip(".").replace(".", ",") + "%"


cols = ["perda_carteira_pct", "perda_subordinada_pct", "perda_senior_pct"]
values = [[pct(v) for v in df[col]] for col in cols]

# Destaque: a única célula em que a sênior perde (perda da carteira passa do colchão de 20%).
hit = df.index[df["perda_senior_pct"] > 0].tolist()
fills = [[white] * len(df) for _ in cols]
fonts = [[ink] * len(df) for _ in cols]
for i in hit:
    fills[2][i] = lime
    fonts[2][i] = lime_text

fig = go.Figure(go.Table(
    columnwidth=[1, 1, 1],
    header=dict(
        values=["<b>Perda na carteira</b>", "<b>Perda da subordinada</b><br>(R$ 20 mi)",
                "<b>Perda da sênior</b><br>(R$ 80 mi)"],
        fill_color=forest, line_color=forest, align="center", height=56,
        font=dict(color=bg, size=17, family=font_body),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="center", height=46,
        font=dict(color=fonts, size=19, family=font_data),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

# Anotação apontando para a célula destacada (última linha, coluna da sênior).
fig.add_annotation(
    xref="paper", yref="paper", x=0.83, y=0.02, ax=-60, ay=48, showarrow=True,
    arrowhead=2, arrowwidth=1.5, arrowcolor=lime_text, xanchor="right", align="right",
    text="A sênior só perde quando a perda da carteira passa de 20%, o tamanho da subordinada.",
    font=dict(color=lime_text, size=15, family=font_body),
)
fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-92, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Exemplo hipotético (cálculo próprio): carteira de R$ 100 mi. "
         "Perda da sênior = max(0, L − S) / (1 − S).<br>Ignora fundo de reserva, "
         "excesso de spread e o momento das perdas.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=500,
    margin=dict(l=40, r=40, t=80, b=170),
    title=dict(text="A subordinada absorve as primeiras perdas",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** tabela-imagem com quatro linhas, igual ao rascunho (ver "Por que tabela e
não curva" acima). Descartado: linha contínua perda da carteira → perda da sênior.

**Anotação:** a única célula em que a sênior perde (30% → 12,5%) tem fundo `lime.300` e uma
seta (`add_annotation`) com o achado: a sênior só perde depois que a perda passa de 20%.
Gate de Tufte: sem eixo, sem 3D, sem sombra; a ênfase é só cor de fundo numa célula, então
não há Lie Factor a declarar.

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Tabela com quatro cenários de perda numa carteira de R$ 100 milhões, com série sênior de
> R$ 80 milhões e subordinada de R$ 20 milhões. Perda de 5% na carteira: a subordinada perde
> 25% e a sênior, nada. Perda de 15%: subordinada perde 75%, sênior nada. Perda de 20%:
> subordinada perde 100%, sênior nada. Perda de 30%: subordinada perde 100% e a sênior, 12,5%.
> A sênior só perde quando a perda da carteira passa de 20%, o tamanho da subordinada.

**Legenda:**

> A subordinada absorve as primeiras perdas. Com 20% de subordinação, a sênior só começa a
> perder quando a perda da carteira passa de 20%. Exemplo hipotético.

## graf-02

**Pergunta que o gráfico responde:** que taxa real uma debênture tributada precisa pagar, em
cada prazo, para empatar com um CRA isento a IPCA + 7%, e quanto isso difere da regra de bolso?

**Fonte dos dados:** cálculo próprio, fórmula fechada do texto (papel bullet, capitalização
anual, IPCA constante de 4% a.a., alíquota da tabela regressiva: 17,5% em 1 ano, 15% em 2 anos
ou mais). Conferido em `processo/07-verificacao.md`, itens 1.1-1.4 e 1.6 ([OK]); o cruzamento
das duas colunas fica em T ≈ 9,04 anos (item 1.4).

**Dados:** `posts/2026-09-28-o-certificado-nao-muda-o-devedor/graficos/dados/graf-02.csv`

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-09-28-o-certificado-nao-muda-o-devedor"
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


def num(v, casas):
    return f"{v:.{casas}f}".replace(".", ",")


def aliq(v):
    return num(v, 1).removesuffix(",0") + "%"


def prazo(t):
    return f"{t} ano" if t == 1 else f"{t} anos"


values = [
    [prazo(t) for t in df["prazo_anos"]],
    [aliq(v) for v in df["aliquota_pct"]],
    ["IPCA + " + num(v, 2) + "%" for v in df["regra_bolso_real_pct"]],
    ["IPCA + " + num(v, 2) + "%" for v in df["empate_correto_real_pct"]],
]

# Destaque: o prazo em que o empate correto fica abaixo da regra de bolso (os erros se inverteram).
hit = df.index[df["empate_correto_real_pct"] < df["regra_bolso_real_pct"]].tolist()
fills = [[white] * len(df) for _ in values]
fonts = [[ink] * len(df) for _ in values]
for i in hit:
    fills[3][i] = lime
    fonts[3][i] = lime_text

fig = go.Figure(go.Table(
    columnwidth=[0.8, 0.9, 1.2, 1.2],
    header=dict(
        values=["<b>Prazo</b>", "<b>Alíquota de IR</b>", "<b>Regra de bolso</b><br>IPCA + [7% ÷ (1 − t)]",
                "<b>Empate correto</b><br>fórmula do texto"],
        fill_color=forest, line_color=forest, align="center", height=56,
        font=dict(color=bg, size=17, family=font_body),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="center", height=46,
        font=dict(color=fonts, size=19, family=font_data),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

# Anotação apontando para a célula destacada (10 anos, empate correto).
fig.add_annotation(
    xref="paper", yref="paper", x=0.86, y=0.02, ax=-60, ay=48, showarrow=True,
    arrowhead=2, arrowwidth=1.5, arrowcolor=lime_text, xanchor="right", align="right",
    text="Até perto de 9 anos, o empate correto fica acima da regra de bolso. Aos 10, abaixo.",
    font=dict(color=lime_text, size=15, family=font_body),
)
fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-92, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Taxa real que uma debênture tributada precisa pagar para empatar com um CRA isento a IPCA + 7%, IPCA de 4% a.a.<br>"
         "Cálculo próprio. Capitalização anual e IPCA constante; papel bullet.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=500,
    margin=dict(l=40, r=40, t=80, b=170),
    title=dict(text="Quanto a debênture tributada precisa pagar para empatar",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
```

**Escolha de tipo:** tabela-imagem com quatro prazos, igual ao rascunho. Descartado: curva de
empate × prazo com a regra de bolso como linha horizontal. Mostraria o cruzamento perto de 9
anos de forma contínua, mas é mudança de conteúdo; fica como sugestão ao autor, não como peça.

**Anotação:** a célula de 10 anos do empate correto (8,18%, abaixo dos 8,24% da regra de bolso)
tem fundo `lime.300` e seta com o achado: até perto de 9 anos o empate fica acima da regra de
bolso; aos 10, abaixo. Gate de Tufte: sem eixo nem ênfase de área; nenhum Lie Factor a declarar.

**Alt-text (para o placeholder `graf-02` em `post.md`):**

> Tabela com a taxa real que uma debênture tributada precisa pagar para empatar com um CRA
> isento a IPCA + 7%, com IPCA de 4% ao ano. Em 1 ano, alíquota de 17,5%: a regra de bolso diz
> IPCA + 8,48%, o empate correto é IPCA + 9,30%. Em 2 anos, alíquota de 15%: regra de bolso
> IPCA + 8,24%, empate IPCA + 8,80%. Em 5 anos: IPCA + 8,24% contra IPCA + 8,52%. Em 10 anos:
> IPCA + 8,24% contra IPCA + 8,18%. Até perto de 9 anos o empate correto fica acima da regra de
> bolso; aos 10, abaixo.

**Legenda:**

> Quanto a debênture tributada precisa pagar para empatar com um CRA a IPCA + 7%. Cálculo
> próprio; capitalização anual e IPCA constante de 4% a.a.
