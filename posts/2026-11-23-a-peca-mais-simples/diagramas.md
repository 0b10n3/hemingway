# Diagramas — "A Peça Mais Simples"

Uma peça, feita no gate (2026-11-24) a pedido do autor: a Substack não renderiza tabela markdown,
então a tabela de "Cinco títulos, um devedor" vira imagem (`go.Table`), mesmo padrão de
`posts/2026-10-15-renda-fixa-condicoes-variaveis/diagramas.md`. Conteúdo verbatim do `post.md`; as
quebras `<br>` só distribuem o texto nas células. A outra tabela do post (os cenários) é numérica e
virou o `graf-03`, em `graficos.md`. Tokens lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`.
O bloco roda a partir da raiz do repositório (`pipelines/hemingway/`) e foi testado com `python3`.

## diag-01

**Onde entra:** "Cinco títulos, um devedor", no lugar da tabela, depois de "Na prateleira do Tesouro
Direto, as respostas formam cinco papéis principais:".

**Pergunta que o diagrama responde:** o que muda de um título público para outro, e o que fica igual?

**Fonte dos dados:** Decreto nº 12.814/2026 (características dos títulos) e Tesouro Direto (nomes
comerciais), conferidos em `processo/07-verificacao.md`. Sem número de mercado.

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-11-23-a-peca-mais-simples"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
white = c["neutral"]["white"]["$value"]
mint = c["neutral"]["mint"]["$value"]
forest = c["forest"]["500"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body = stack("display"), stack("body")

# Conteúdo: a tabela de "Cinco títulos, um devedor" em post.md, verbatim.
rows = [
    ("LFT", "Tesouro Selic", "Selic acumulada", "não tem"),
    ("LTN", "Tesouro Prefixado", "taxa fixa, pelo deságio", "não tem"),
    ("NTN-F", "Tesouro Prefixado<br>com Juros Semestrais", "taxa fixa", "10% ao ano,<br>em duas parcelas"),
    ("NTN-B Principal", "Tesouro IPCA+", "IPCA + taxa fixa", "não tem"),
    ("NTN-B", "Tesouro IPCA+<br>com Juros Semestrais", "IPCA + taxa fixa", "6% ao ano,<br>em duas parcelas"),
]
n = len(rows)


def pad(row):
    # Plotly desloca verticalmente célula com menos linhas que as vizinhas; igualar alinha tudo
    k = max(t.count("<br>") for t in row)
    return [t + "<br> " * (k - t.count("<br>")) for t in row]


rows = [pad(r) for r in rows]
# primeira coluna sem <b>: o negrito cai na fonte reserva e desce alguns pixels em relação às vizinhas
values = [[r[0] for r in rows]] + [[r[j] for r in rows] for j in (1, 2, 3)]

# Destaque: a LTN, o título do texto ("A LTN é o mais simples dos cinco").
key = [1]
fills = [[mint if i in key else white for i in range(n)] for _ in range(4)]

fig = go.Figure(go.Table(
    columnwidth=[0.75, 1.15, 1.0, 0.95],
    header=dict(
        values=["<b>Título</b>", "<b>Nome no Tesouro Direto</b>", "<b>O que remunera</b>", "<b>Cupom</b>"],
        fill_color=forest, line_color=forest, align="left", height=48,
        font=dict(color=bg, size=19, family=font_display),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="left", height=40,
        font=dict(color=[forest, ink, ink, ink], size=17, family=font_body),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-18, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Em destaque: a LTN, o mais simples dos cinco.<br>"
         "Fontes: Decreto nº 12.814/2026 (características dos títulos); Tesouro Direto (nomes comerciais).",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=1000, height=470,
    margin=dict(l=40, r=40, t=80, b=80),
    title=dict(text="Muda o indexador e o cupom. O devedor é o mesmo: o Tesouro.",
               font=dict(color=ink, size=22, family=font_display), x=0.04, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** `go.Table` de quatro colunas, título à esquerda em `forest`, sem negrito (o
negrito cai na fonte reserva e desce alguns pixels em relação às vizinhas). Linha da LTN em `mint`:
é o título do texto. A manchete carrega a tese da seção ("Muda o indexador e o cupom. O devedor é o
mesmo: o Tesouro."), em vez de repetir o H2 que fica logo acima. Descartado: lista em texto (perde a
comparação por coluna).

**Tokens usados:** `color.neutral.chalk` (fundo, texto do cabeçalho), `color.forest.500` (cabeçalho e
coluna dos títulos), `color.neutral.mint` (linha da LTN), `color.neutral.white` (células),
`color.neutral.mist` (bordas), `color.neutral.ink` (texto), `color.neutral.slate` (rodapé);
`typography.fontFamily.display` (manchete, cabeçalho) e `.body` (células, rodapé). Sem `lime`.

**Alt-text (placeholder `diag-01`, 120 caracteres):**

> Tabela dos cinco títulos do Tesouro Direto (LFT, LTN, NTN-F, NTN-B Principal e NTN-B): o que cada um remunera e o cupom.

**Legenda:**

> O que muda de um título para outro é o indexador e o cupom; o devedor é sempre o Tesouro.
