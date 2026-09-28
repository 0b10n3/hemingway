# Diagramas — "O Certificado Não Muda o Devedor"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN")
e posicionadas em `processo/04-draft-v1.md` (placeholders `[diag-01]` e `[diag-02]`), com as
correções de `processo/07-verificacao.md`. Ferramenta: Plotly (nós via `add_shape`, setas via
`add_annotation`; tabela via `go.Table`), mesmo padrão de `graf-NN`. Tokens lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Nenhum `info-NN`: cada peça carrega sua ideia sozinha (mesma conclusão de `02-estrutura.md`).

## diag-01

**Pergunta que o diagrama responde:** num CRA real, quais são as três relações de crédito e
com qual delas o investidor de fato se relaciona?

**Fonte dos dados:** participantes e números da 73ª emissão de CRA da True Securitizadora (hoje
Opea): termo de securitização de 20/09/2023, emissão em 15/10/2023, três séries, R$ 1 bi,
Pentágono como agente fiduciário, lastro em debêntures da 9ª emissão da Raízen Energia S.A. com
fiança da Raízen S.A., regime fiduciário instituído (cl. 3.1.1 e 18.3). Ver
`processo/03-pesquisa.md` §1 e `processo/07-verificacao.md`, itens 2.5, 2.7 e 2.8 ([OK]).

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-09-28-o-certificado-nao-muda-o-devedor"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mint = c["neutral"]["mint"]["$value"]
white = c["neutral"]["white"]["$value"]
forest = c["forest"]["500"]["$value"]
grove = c["grove"]["500"]["$value"]
lime = c["lime"]["500"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

fig = go.Figure()

# Caixas: (x0, x1, y0, y1). A securitizadora é uma moldura em mint; o patrimônio separado
# fica dentro dela, em forest — é o nó por onde as três relações passam. Devedor e
# investidores em grove, como os extremos do diag-01 do post da LCA.
BOX = {
    "raizen": (0.3, 3.7, 2.2, 4.4),
    "secur": (4.6, 9.6, 1.2, 5.6),
    "ps": (5.3, 8.9, 2.6, 4.2),
    "invest": (10.5, 13.7, 2.2, 4.4),
    "pentagono": (10.5, 13.7, 5.5, 6.7),
}


def rect(key, fill, line, dash=None):
    x0, x1, y0, y1 = BOX[key]
    fig.add_shape(type="rect", x0=x0, x1=x1, y0=y0, y1=y1, fillcolor=fill,
                  line=dict(color=line, width=1.5, dash=dash), layer="below")


def mid(key):
    x0, x1, y0, y1 = BOX[key]
    return (x0 + x1) / 2, (y0 + y1) / 2


def text(x, y, t, color, size, family=font_body, **kw):
    fig.add_annotation(x=x, y=y, text=t, showarrow=False, align="center",
                       font=dict(color=color, size=size, family=family), **kw)


rect("secur", mint, forest)
rect("raizen", grove, grove)
rect("ps", forest, forest)
rect("invest", grove, grove)
rect("pentagono", white, forest)

x, y = mid("raizen")
text(x, y + 0.35, "<b>Raízen Energia S.A.</b>", white, 16)
text(x, y - 0.4, "devedora · debêntures da 9ª emissão<br>fiança da Raízen S.A.", white, 13)

text(BOX["secur"][0] + 0.2, BOX["secur"][3] - 0.35,
     "<b>True Securitizadora (hoje Opea)</b>", forest, 14, xanchor="left")
x, y = mid("ps")
text(x, y + 0.25, "<b>Patrimônio separado</b>", white, 16)
text(x, y - 0.35, "regime fiduciário · titular das debêntures", white, 13)
text(mid("ps")[0], 1.85, "isolado do balanço comum da securitizadora", slate, 13)

x, y = mid("invest")
text(x, y + 0.3, "<b>Titulares dos CRAs</b>", white, 16)
text(x, y - 0.35, "73ª emissão · 3 séries · R$ 1 bi", white, 13)

x, y = mid("pentagono")
text(x, y + 0.2, "<b>Pentágono</b>", forest, 15)
text(x, y - 0.25, "agente fiduciário", slate, 13)


def arrow(x0, y0, x1, y1, color, width=2.5, dash=None):
    fig.add_annotation(x=x1, y=y1, ax=x0, ay=y0, xref="x", yref="y", axref="x", ayref="y",
                       showarrow=True, arrowhead=2, arrowsize=1.1, arrowwidth=width,
                       arrowcolor=color, text="")


# Seta = quem empresta -> quem deve (mesmo sentido do diag-01 da LCA).
Y = 3.4
arrow(BOX["invest"][0] - 0.1, Y, BOX["ps"][1] + 0.1, Y, grove)    # relação 3
arrow(BOX["ps"][0] - 0.1, Y, BOX["raizen"][1] + 0.1, Y, forest)   # relação 1
# Pentágono fiscaliza a securitizadora (linha fina pontilhada, sem relação de crédito)
XF = BOX["secur"][1] - 0.6
fig.add_shape(type="line", x0=BOX["pentagono"][0], y0=6.1, x1=XF, y1=6.1,
              line=dict(color=slate, width=1.2, dash="dot"))
arrow(XF, 6.1, XF, BOX["secur"][3] + 0.05, slate, width=1.2)
text(XF - 0.15, 6.1, "representa os titulares<br>e fiscaliza a securitizadora", slate, 12,
     xanchor="right")


def badge(x, y, n):
    r = 0.26
    fig.add_shape(type="circle", x0=x - r, x1=x + r, y0=y - r, y1=y + r,
                  fillcolor=lime, line=dict(color=lime, width=0))
    text(x, y, f"<b>{n}</b>", ink, 15, family=font_data)


badge((BOX["raizen"][1] + BOX["ps"][0]) / 2 + 0.4, Y + 0.45, 1)
badge(BOX["ps"][1] - 0.05, BOX["ps"][2], 2)
badge((BOX["ps"][1] + BOX["invest"][0]) / 2, Y + 0.45, 3)

legend = (
    "<b>1</b>  A Raízen Energia deve ao patrimônio separado (as debêntures).<br>"
    "<b>2</b>  O patrimônio separado é titular do lastro, isolado do patrimônio comum da securitizadora.<br>"
    "<b>3</b>  Os titulares dos CRAs têm direito ao que o patrimônio separado receber."
)
fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-10, xanchor="left", yanchor="top",
                   showarrow=False, align="left", text=legend,
                   font=dict(color=ink, size=14, family=font_body))
fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-92, xanchor="left", yanchor="top",
                   showarrow=False, align="left",
                   text="Setas: de quem empresta para quem deve. Fonte: termo de securitização da "
                        "73ª emissão de CRA da True Securitizadora (out/2023).",
                   font=dict(color=slate, size=12, family=font_body))

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=1100, height=660,
    margin=dict(l=30, r=30, t=80, b=140),
    xaxis=dict(visible=False, range=[0, 14]),
    yaxis=dict(visible=False, range=[0.9, 7.0]),
    title=dict(text="Três relações de crédito, um CRA",
               font=dict(color=ink, size=22, family=font_display), x=0.03, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** quatro nós em linha, esquerda → direita, par direto do diag-01 do post
da LCA (`posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro/diagramas.md`): mesmo
sentido de seta (quem empresta → quem deve), mesmos extremos em `grove` e nó central em
`forest`. A peça nova, o patrimônio separado, fica dentro de uma moldura `mint` que é a
securitizadora, e isso desenha a relação 2 (isolamento) sem seta. As três relações são
marcadas com selos numerados em `lime.500` e explicadas numa lista abaixo, em vez de rótulos
sobre as setas: com a moldura no meio, não há espaço para rótulo de duas linhas entre as caixas
sem sobrepor. O agente fiduciário fica ao lado dos titulares, ligado à securitizadora por uma
linha pontilhada, porque fiscaliza e não é relação de crédito. Descartado: layout automático de
grafo (cinco nós não pedem).

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Diagrama de fluxo de um CRA real, a 73ª emissão da True Securitizadora, hoje Opea. À
> esquerda, a devedora Raízen Energia S.A., com debêntures da 9ª emissão e fiança da Raízen
> S.A. No centro, dentro da caixa da securitizadora, o patrimônio separado, sob regime
> fiduciário, titular das debêntures e isolado do balanço comum da securitizadora. À direita,
> os titulares dos CRAs (três séries, R$ 1 bilhão). Acima deles, a Pentágono, agente
> fiduciário, que representa os titulares e fiscaliza a securitizadora. Três relações
> numeradas: 1, a Raízen Energia deve ao patrimônio separado; 2, o patrimônio separado é
> titular do lastro, isolado da securitizadora; 3, os titulares dos CRAs têm direito ao que o
> patrimônio separado receber. O investidor não tem crédito contra a securitizadora nem
> diretamente contra a Raízen: tem direito ao fluxo do patrimônio separado.

**Legenda:**

> Três relações de crédito, um CRA. Na 73ª emissão da True/Opea, a Raízen Energia deve ao
> patrimônio separado, que é dono das debêntures e fica fora do balanço da securitizadora; o
> investidor tem direito ao que esse patrimônio receber.

## diag-02

**Pergunta que o diagrama responde:** em que LCI/LCA e CRI/CRA se parecem e em que diferem,
atributo por atributo?

**Fonte dos dados:** única cifra embutida é o limite do FGC (R$ 250 mil por CPF/CNPJ, por
instituição ou conglomerado), conferido em `processo/07-verificacao.md`, item 3.14. Demais
linhas: Lei nº 11.076/2004 (LCI/LCA) e Lei nº 14.430/2022, art. 27 (patrimônio separado),
itens 3.15 e seguintes da verificação.

**Por que tabela-imagem:** é a tabela do autor (marcador 4 do rascunho); a Substack não
renderiza tabela markdown. Mesmo texto, com duas correções: linha FGC ("por instituição ou
conglomerado", item 3.14 da verificação) e CMN por extenso.

**Código Plotly executável** (gera `figuras/diag-02.svg` e `figuras/diag-02.png`):

```python
import json
import os

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
mint = c["neutral"]["mint"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Conteúdo: tabela do rascunho (processo/04-draft-v1.md), com as correções de
# processo/07-verificacao.md (item 3.14, FGC "por instituição ou conglomerado") e a sigla
# do CMN por extenso.
rows = [
    ("Emissor", "Banco", "Companhia securitizadora"),
    ("Contra quem você<br>tem crédito", "O banco",
     "O patrimônio separado, que tem crédito<br>contra o devedor do lastro"),
    ("Onde fica o lastro", "No balanço do banco,<br>vinculado à emissão",
     "Fora do balanço comum da securitizadora,<br>em patrimônio separado"),
    ("FGC", "Sim, até R$ 250 mil por CPF/CNPJ,<br>por instituição ou conglomerado", "Não"),
    ("IR para pessoa física", "Isento", "Isento"),
    ("Quem regula o emissor", "Banco Central / CMN<br>(Conselho Monetário Nacional)",
     "CVM (o CMN define<br>o lastro admitido)"),
    ("Se o emissor quebrar", "Você é credor do banco,<br>com o FGC até o limite",
     "O patrimônio separado segue de pé;<br>o risco continua sendo o do devedor"),
]
n = len(rows)


def two_lines(t):
    # Plotly desloca verticalmente célula de uma linha em relação às de duas; igualar alinha tudo
    return t if "<br>" in t else t + "<br> "


values = [["<b>" + two_lines(r[0]) + "</b>" for r in rows],
          [two_lines(r[1]) for r in rows], [two_lines(r[2]) for r in rows]]

# Destaque: as duas linhas que o texto cobra do leitor — contra quem é o crédito (a tese
# do post: o certificado não muda o devedor) e a ausência de FGC no CRI/CRA.
key = [1, 3]
fills = [[mint if i in key else white for i in range(n)] for _ in range(3)]

fig = go.Figure(go.Table(
    columnwidth=[0.75, 1.1, 1.25],
    header=dict(
        values=["", "<b>LCI / LCA</b>", "<b>CRI / CRA</b>"],
        fill_color=forest, line_color=forest, align="left", height=48,
        font=dict(color=bg, size=19, family=font_display),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="left", height=62,
        font=dict(color=[forest, ink, ink], size=16, family=font_body),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-20, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Em destaque: contra quem é o seu crédito e se há FGC. No CRI/CRA, o risco é o do devedor do lastro, sem FGC.<br>"
         "Fontes: Lei nº 11.076/2004 (LCI/LCA); Lei nº 14.430/2022, art. 27 (patrimônio separado); FGC.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=660,
    margin=dict(l=40, r=40, t=80, b=90),
    title=dict(text="LCI/LCA × CRI/CRA: o mesmo IR, outro devedor",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-02.svg"))
fig.write_image(os.path.join(out_dir, "diag-02.png"), scale=2)
```

**Escolha de layout:** `go.Table` de três colunas, atributos à esquerda em `forest` negrito.
Duas linhas em `mint`: contra quem é o crédito (a tese do post) e FGC (o texto cobra: "não há
FGC para amortecer o erro de análise"). Células de uma linha recebem uma segunda linha vazia
porque o Plotly desloca verticalmente célula de uma linha em relação às de duas. Descartado:
cartões lado a lado com shapes (mais código, mesma leitura).

**Alt-text (para o placeholder `diag-02` em `post.md`):**

> Tabela comparando LCI/LCA e CRI/CRA em sete atributos. Emissor: banco, contra companhia
> securitizadora. Contra quem você tem crédito: o banco, contra o patrimônio separado, que tem
> crédito contra o devedor do lastro. Onde fica o lastro: no balanço do banco, vinculado à
> emissão, contra fora do balanço comum da securitizadora, em patrimônio separado. FGC: sim, até
> R$ 250 mil por CPF/CNPJ, por instituição ou conglomerado, contra não. IR para pessoa física:
> isento nos dois. Quem regula o emissor: Banco Central e Conselho Monetário Nacional, contra
> CVM, com o CMN definindo o lastro admitido. Se o emissor quebrar: você é credor do banco, com
> o FGC até o limite, contra o patrimônio separado segue de pé e o risco continua sendo o do
> devedor.

**Legenda:**

> LCI/LCA × CRI/CRA: o mesmo IR, outro devedor. No CRI/CRA, o seu crédito é contra um
> patrimônio separado, e o risco é o do devedor do lastro, sem FGC.
