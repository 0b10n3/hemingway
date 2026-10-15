# Diagramas — "Renda Fixa, Condições Variáveis"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN")
e posicionadas em `processo/04-draft-v2.md` (seções "O que é uma debênture" e "O lugar na
fila"). As duas são tabelas do autor: a Substack não renderiza tabela markdown, então viram
imagem (`go.Table`), mesmo padrão de `diag-02` do post do CRA
(`posts/2026-09-28-o-certificado-nao-muda-o-devedor/diagramas.md`). Conteúdo verbatim do draft
v2; as quebras `<br>` só distribuem o texto nas células. Tokens lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Nenhum `info-NN`: cada peça carrega sua ideia sozinha (mesma conclusão de `02-estrutura.md`).

## diag-01

**Pergunta que o diagrama responde:** o que muda para o investidor entre LCA, CRA de devedor
único e debênture: quem emite, contra quem é o crédito, o que fica no meio, o IR e quem decide
uma renegociação?

**Fonte dos dados:** única cifra é a referência à Lei nº 12.431/2011 (incentivada, alíquota zero
para pessoa física), conferida em `processo/07-verificacao.md`, item 2.22; tabela regressiva,
item 2.25; debênture, escritura e agente fiduciário (Lei nº 6.404/1976, arts. 52, 61 e 68),
itens 2.1-2.6. As colunas LCA e CRA repetem o que o post do CRA verificou
(`posts/2026-09-28-o-certificado-nao-muda-o-devedor/processo/07-verificacao.md`). A linha
"Quem decide uma renegociação" segue o ajuste C-05 do draft v2 ("os credores que o plano
reúne").

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

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
mint = c["neutral"]["mint"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Conteúdo: tabela do draft (processo/04-draft-v2.md, "O que é uma debênture"), verbatim.
rows = [
    ("Quem emite", "Banco", "Securitizadora", "A própria empresa"),
    ("Contra quem é<br>o seu crédito", "O banco",
     "Um patrimônio separado,<br>que é credor da empresa", "A empresa, diretamente"),
    ("O que fica no meio", "FGC, até o limite",
     "Patrimônio separado<br>e agente fiduciário", "Escritura e<br>agente fiduciário"),
    ("IR para pessoa física", "Isento", "Isento",
     "Tabela regressiva; isento se<br>incentivada (Lei nº 12.431)"),
    ("Quem decide uma<br>renegociação", "Ninguém: o banco paga,<br>ou o FGC cobre",
     "Assembleia de titulares",
     "Assembleia de debenturistas e,<br>numa recuperação, os credores<br>que o plano reúne"),
]
n = len(rows)


def pad(row):
    # Plotly desloca verticalmente célula com menos linhas que as vizinhas; igualar alinha tudo
    k = max(t.count("<br>") for t in row)
    return [t + "<br> " * (k - t.count("<br>")) for t in row]


rows = [pad(r) for r in rows]
values = [["<b>" + r[0] + "</b>" for r in rows]] + [[r[j] for r in rows] for j in (1, 2, 3)]

# Destaque: as duas linhas que a seção seguinte cobra ("Se não há rede, o que protege o
# debenturista?") — contra quem é o crédito e o que fica no meio.
key = [1, 2]
fills = [[mint if i in key else white for i in range(n)] for _ in range(4)]

fig = go.Figure(go.Table(
    columnwidth=[0.8, 0.9, 1.05, 1.2],
    header=dict(
        values=["", "<b>LCA</b>", "<b>CRA de devedor único</b>", "<b>Debênture</b>"],
        fill_color=forest, line_color=forest, align="left", height=48,
        font=dict(color=bg, size=19, family=font_display),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="left", height=40,
        font=dict(color=[forest, ink, ink, ink], size=16, family=font_body),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-20, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Em destaque: contra quem é o seu crédito e o que fica no meio. Na debênture, o crédito é contra a empresa, sem FGC no caminho.<br>"
         "Fontes: Lei nº 6.404/1976, arts. 52, 61 e 68; Lei nº 12.431/2011; Lei nº 11.076/2004 (LCA); Lei nº 14.430/2022 (patrimônio separado).",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=530,
    margin=dict(l=40, r=40, t=80, b=90),
    title=dict(text="LCA, CRA e debênture: o que fica entre você e quem deve",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** `go.Table` de quatro colunas, atributos à esquerda em `forest` negrito,
continuação direta do `diag-02` do post do CRA (LCI/LCA × CRI/CRA), agora com a debênture como
terceira coluna. Duas linhas em `mint`: contra quem é o crédito e o que fica no meio, que é o
que a seção "O que fica entre você e a empresa" cobra ("Se não há rede..."). Células com menos
linhas que as vizinhas recebem linhas vazias porque o Plotly desloca verticalmente o texto
delas. Descartado: três cartões lado a lado com shapes (mais código, mesma leitura).

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Tabela comparando LCA, CRA de devedor único e debênture em cinco atributos. Quem emite:
> banco, securitizadora, a própria empresa. Contra quem é o seu crédito: o banco; um patrimônio
> separado, que é credor da empresa; a empresa, diretamente. O que fica no meio: FGC, até o
> limite; patrimônio separado e agente fiduciário; escritura e agente fiduciário. IR para pessoa
> física: isento, isento, e tabela regressiva na debênture, isenta se incentivada pela Lei nº
> 12.431. Quem decide uma renegociação: ninguém na LCA, porque o banco paga ou o FGC cobre;
> assembleia de titulares no CRA; assembleia de debenturistas na debênture e, numa recuperação,
> os credores que o plano reúne. Na debênture, o crédito é contra a empresa, sem FGC no meio.

**Legenda:**

> LCA, CRA e debênture lado a lado. Na debênture, o seu crédito é contra a própria empresa, e o
> que fica no meio é a escritura e o agente fiduciário, sem FGC.

## diag-02

**Pergunta que o diagrama responde:** onde cada espécie ou garantia de debênture fica de fato
na recuperação judicial e na falência, comparado com o que o nome sugere?

**Fonte dos dados:** sem cifra. Lei nº 6.404/1976, art. 58 (espécies), e Lei nº 11.101/2005,
arts. 41 (classes na recuperação), 49, § 3º (garantia fiduciária fora da recuperação) e 83,
caput e § 6º (ordem na falência; privilégio geral e especial viram quirografários desde a Lei
nº 14.112/2020). Conferido em `processo/07-verificacao.md`, itens 2.4-2.5 e 2.10-2.13
(Confere).

**Código Plotly executável** (gera `figuras/diag-02.svg` e `figuras/diag-02.png`):

```python
import json
import os

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
mint = c["neutral"]["mint"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Conteúdo: tabela do draft (processo/04-draft-v2.md, "O lugar na fila"), verbatim.
rows = [
    ("Garantia real<br>(hipoteca, penhor)", "Preferência sobre um bem",
     "Classe II até o valor do bem;<br>o excedente vota na classe III",
     "Segunda na fila, até o valor<br>do bem, antes do Fisco"),
    ("Garantia flutuante", "Privilégio sobre o<br>ativo da empresa", "Classe III",
     "Quirografária desde 2020"),
    ("Quirografária", "Sem preferência",
     "Classe III, ao lado de bancos<br>sem garantia e fornecedores",
     "Depois de trabalhistas,<br>garantia real e Fisco"),
    ("Subordinada", "Recebe depois<br>dos quirografários", "Classe III",
     "Última classe de credores;<br>depois dela, só os acionistas"),
    ("Alienação ou<br>cessão fiduciária", "O bem é do credor<br>até a quitação",
     "Em regra, fora<br>da recuperação", "O bem não entra<br>na fila comum"),
]
n = len(rows)


def pad(row):
    # Plotly desloca verticalmente célula com menos linhas que as vizinhas; igualar alinha tudo
    k = max(t.count("<br>") for t in row)
    return [t + "<br> " * (k - t.count("<br>")) for t in row]


rows = [pad(r) for r in rows]
values = [["<b>" + r[0] + "</b>" for r in rows]] + [[r[j] for r in rows] for j in (1, 2, 3)]

# Destaque: a garantia flutuante, "o caso mais curioso" do texto — o nome sugere privilégio,
# a falência a trata como quirografária desde 2020.
key = [1]
fills = [[mint if i in key else white for i in range(n)] for _ in range(4)]

fig = go.Figure(go.Table(
    columnwidth=[0.85, 0.95, 1.2, 1.2],
    header=dict(
        values=["<b>Espécie ou garantia</b>", "<b>O que o nome sugere</b>",
                "<b>Na recuperação judicial</b>", "<b>Na falência</b>"],
        fill_color=forest, line_color=forest, align="left", height=48,
        font=dict(color=bg, size=17, family=font_display),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="left", height=40,
        # coluna "o que o nome sugere" em slate: é a promessa; as duas últimas são a fila real
        font=dict(color=[forest, slate, ink, ink], size=16, family=font_body),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-20, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Em destaque: a garantia flutuante. O nome sugere privilégio; desde a Lei nº 14.112/2020, na falência ela é quirografária (art. 83, § 6º).<br>"
         "Fontes: Lei nº 6.404/1976, art. 58 (espécies); Lei nº 11.101/2005, arts. 41, 49, § 3º, e 83.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1100, height=530,
    margin=dict(l=40, r=40, t=80, b=90),
    title=dict(text="A espécie promete; a Lei de Falências decide o lugar na fila",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-02.svg"))
fig.write_image(os.path.join(out_dir, "diag-02.png"), scale=2)
```

**Escolha de layout:** `go.Table` de quatro colunas, lida da esquerda para a direita como o
texto a lê: espécie → o que o nome sugere → classe na recuperação → lugar na falência. A coluna
"O que o nome sugere" fica em `slate` (a promessa) e as duas últimas em `ink` (o que a lei
entrega), sem acrescentar palavra. Uma linha em `mint`: a garantia flutuante, que o texto chama
de "o caso mais curioso". Descartado: escada vertical da ordem do art. 83 com as espécies
penduradas nos degraus. Mostraria a fila da falência, mas perderia a coluna da recuperação
judicial e a da promessa, que são o ponto da peça.

**Alt-text (para o placeholder `diag-02` em `post.md`):**

> Tabela com cinco espécies ou garantias de debênture, o que o nome sugere e onde cada uma fica
> na recuperação judicial e na falência. Garantia real, como hipoteca ou penhor: o nome sugere
> preferência sobre um bem; na recuperação, vota na classe II até o valor do bem, e o excedente
> na classe III; na falência, é a segunda na fila, até o valor do bem, antes do Fisco. Garantia
> flutuante: sugere privilégio sobre o ativo da empresa; na recuperação, classe III; na
> falência, quirografária desde 2020. Quirografária: sem preferência; classe III, ao lado de
> bancos sem garantia e fornecedores; na falência, recebe depois de trabalhistas, garantia real
> e Fisco. Subordinada: recebe depois dos quirografários; classe III; na falência, é a última
> classe de credores, e depois dela só os acionistas. Alienação ou cessão fiduciária: o bem é do
> credor até a quitação; em regra fica fora da recuperação; na falência, o bem não entra na fila
> comum.

**Legenda:**

> O lugar na fila. A espécie da Lei das S.A. promete; a Lei de Recuperação e Falências decide.
> A garantia flutuante, que sugere privilégio, é quirografária na falência desde 2020.
