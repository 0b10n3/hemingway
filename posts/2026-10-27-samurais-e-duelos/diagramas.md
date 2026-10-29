# Diagramas — "Samurais e duelos no mercado financeiro"

Duas peças, decididas em `processo/02-estrutura.md` ("Visuais: onde e por quê") e posicionadas
em `processo/04-draft-v2.md`: a abertura (diag-01) e a seção "Os cinco anéis numa
segunda-feira" (diag-02). As datas e as idades do diag-01 seguem `processo/07-verificacao.md`
("Contas" e "Fora do escopo desta etapa"). O texto das células do diag-02 é o da tabela depois
das etapas 6 e 7. Ferramenta: Plotly. A linha do tempo usa `add_shape`/`add_annotation` e a
tabela usa `go.Table`, mesmo padrão de `graf-NN` e dos diagramas do post da debênture
(`posts/2026-10-15-renda-fixa-condicoes-variaveis/diagramas.md`, na branch
`post/2026-10-15-renda-fixa-condicoes-variaveis`). Os tokens são lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Nenhum `info-NN`. O critério de gatilho falha: cada peça carrega a própria síntese
(`02-estrutura.md`).

## diag-01

**Onde entra:** abertura, logo depois de "Só perto dos 50 sentiu que tinha entendido o
Caminho." (parágrafo próprio desde a etapa 6) e antes de "No mercado financeiro um sujeito
invicto…".

**Por que é diag (raciocínio de `02-estrutura.md`):** sugestão do autor ("Linha do tempo de
Musashi… destacando os 30 anos entre Ganryūjima e a caverna"). São datas sem métrica central,
o que dá diag pelo critério 2 ("linha do tempo sem métrica central"). graf perde: a única
grandeza é o tempo, e não há série a comparar. info perde: uma peça só carrega a ideia. Fica
nesse ponto porque o leitor acaba de receber as idades do prefácio (13, 30, 50) e vê as datas
sobre a mesma linha que mostra o vão de três décadas.

**Pergunta que o diagrama responde:** quanto tempo passou entre o duelo mais famoso de Musashi
e o livro, e onde caem nessa vida as idades que o prefácio conta?

**Fonte dos dados:**
- Idades na contagem japonesa, a do próprio Musashi no prefácio: idade = ano − 1584 + 1.
  Resultados: 13 → 1596, 29 → 1612, ~50 → ~1633, 60 → 1643 e 62 → 1645. Conferido em
  `processo/07-verificacao.md`, "Contas". O 62 bate com o 享年62 da ja.wikipedia. 1597 e 1634
  só fecham pela conta ocidental e não entram (`03-pesquisa.md`, D15).
- Nascimento em 1584: é a corrente majoritária (Kotobank, *Sekai Daihyakka*). Existe a
  alternativa 1582 (Uozumi), que deslocaria tudo em dois anos (`03-pesquisa.md`, D16). A peça
  usa 1584, como o texto.
- 1612 (Ganryūjima) vem de fontes tardias: 武公伝 (1755) e 二天記 (1776). É a data da tradição
  (`03-pesquisa.md`, D1; `07-verificacao.md`, item 1.2). A nota da peça diz isso.
- 1643: o prefácio registra o 10º mês, quando Musashi sobe ao Reigandō para começar o livro.
- 1645: entrega do livro e *Dokkōdō* em 正保2年5月12日 (≈ 06/06/1645). Morte em 正保2年5月19日 =
  13/06/1645 (ja.wikisource 獨行道; ja.wikipedia 宮本武蔵; `03-pesquisa.md` §1.2, acesso em
  2026-10-26).
- 1643 − 1612 = 31 ("três décadas", `07-verificacao.md`, "Contas").

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import plotly.graph_objects as go

POST_DIR = "posts/2026-10-27-samurais-e-duelos"
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


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

NASC = 1584
DUELO, LIVRO = 1612, 1643
# (ano, idade na contagem japonesa, rótulo, lado: +1 acima / -1 abaixo, âncora, aproximado)
EVENTOS = [
    (1584, None, "nasce", -1, "left", False),
    (1596, 13, "primeiro duelo", +1, "center", False),
    (1612, 29, "Ganryūjima:<br>duelo com Kojirō", -1, "right", False),
    (1633, 50, "sente que entendeu<br>o Caminho", +1, "center", True),
    (1643, 60, "Reigandō:<br>começa o livro", -1, "left", False),
    (1645, 62, "entrega o livro,<br>escreve o <i>Dokkōdō</i><br>e morre, em 13 de junho", +1,
     "left", False),
]
# Convenção única da peça: contagem japonesa, a do próprio Musashi (07-verificacao.md, "Contas").
for ano, idade, *_ in EVENTOS:
    assert idade is None or idade == ano - NASC + 1, (ano, idade)
assert LIVRO - DUELO == 31

fig = go.Figure()

# O vão de três décadas: faixa mint atrás de tudo, de 1612 a 1643.
H = 2.75
fig.add_shape(type="rect", x0=DUELO, x1=LIVRO, y0=-H, y1=H, fillcolor=mint,
              line=dict(width=0), layer="below")
fig.add_annotation(x=(DUELO + LIVRO) / 2, y=-H + 0.15, yanchor="bottom", showarrow=False,
                   align="center",
                   text=f"<b>{LIVRO - DUELO} anos</b><br>entre o duelo e o livro",
                   font=dict(color=forest, size=19, family=font_display))

# Linha de base: a vida inteira em slate; o vão em forest, mais grosso.
fig.add_shape(type="line", x0=NASC, x1=1645, y0=0, y1=0, line=dict(color=slate, width=2))
fig.add_shape(type="line", x0=DUELO, x1=LIVRO, y0=0, y1=0, line=dict(color=forest, width=6))

STEM, GAP = 0.9, 0.08
for ano, idade, rotulo, lado, ancora, aprox in EVENTOS:
    fig.add_shape(type="line", x0=ano, x1=ano, y0=0, y1=lado * STEM,
                  line=dict(color=slate, width=1))
    til = "~" if aprox else ""
    cab = f"{til}{ano}" + (f" · {til}{idade} anos" if idade else "")
    fig.add_annotation(
        x=ano, y=lado * (STEM + GAP), xanchor=ancora, yanchor="bottom" if lado > 0 else "top",
        xshift={"left": 8, "right": -8, "center": 0}[ancora], showarrow=False,
        align={"left": "left", "right": "right", "center": "center"}[ancora],
        text=f"<span style='font-family:{font_data}'><b>{cab}</b></span><br>{rotulo}",
        font=dict(color=ink, size=17, family=font_body),
    )

# Marcadores quadrados (sistema de cantos retos); vazado = data aproximada.
cheios = [e for e in EVENTOS if not e[5]]
fig.add_trace(go.Scatter(x=[e[0] for e in cheios], y=[0] * len(cheios), mode="markers",
                         marker=dict(symbol="square", size=11, color=forest,
                                     line=dict(color=ink, width=1)),
                         showlegend=False, hoverinfo="skip"))
fig.add_trace(go.Scatter(x=[e[0] for e in EVENTOS if e[5]], y=[0], mode="markers",
                         marker=dict(symbol="square-open", size=11, color=forest,
                                     line=dict(width=2)),
                         showlegend=False, hoverinfo="skip"))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-14, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Idades na contagem japonesa, a que o próprio Musashi usa no livro (idade = ano − 1584 + 1). "
         "Marcador vazado: data aproximada.<br>"
         "A data de 1612 vem de fontes do século XVIII e é a da tradição.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=500,
    margin=dict(l=24, r=24, t=64, b=64),
    xaxis=dict(visible=False, range=[1580.5, 1667]),
    yaxis=dict(visible=False, range=[-H - 0.1, H + 0.1]),
    title=dict(text="Entre Ganryūjima e o livro, passaram-se três décadas",
               font=dict(color=ink, size=22, family=font_display), x=0.03, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** linha do tempo horizontal, em escala proporcional ao ano, com os seis
marcos alternando acima e abaixo da linha para os rótulos não colidirem. 1643 e 1645 ficam a
dois anos um do outro e por isso vão em lados opostos. O vão 1612→1643 tem dois sinais: um
trecho mais grosso em `forest` na linha de base e uma faixa `mint` atrás, com "31 anos entre o
duelo e o livro" dentro. Os rótulos de 1612 e 1643 ficam do lado de fora da faixa, alinhados
às bordas, e a faixa fica só com o que está dentro do intervalo (~1633). Os marcadores são
quadrados (cantos retos, DESIGN.md §4.3). O de ~1633 é vazado porque o prefácio diz "por volta
dos 50". Descartados: eixo com ticks de década (ruído, porque cada marco já leva o ano escrito)
e uma linha vertical do tipo "biografia em cartões" (perde a proporção do tempo, que é o
argumento: o vão ocupa metade da vida adulta).

**Gate de Tufte:** sem eixo visível nem barra. A posição horizontal é proporcional ao ano, e o
comprimento da faixa `mint` (31 anos) tem exatamente a largura do intervalo, com Lie Factor 1,0
por construção. Sem 3D, sombra nem moldura.

**Tokens usados:** `color.neutral.chalk` (fundo), `color.neutral.mint` (faixa do vão),
`color.forest.500` (vão na linha de base, marcadores, rótulo "31 anos"),
`color.neutral.slate` (linha da vida, hastes, nota), `color.neutral.ink` (rótulos, contorno dos
marcadores, título); `typography.fontFamily.display` (título, "31 anos"), `.body` (rótulos),
`.data` (anos e idades). Sem `lime`: não há ação nem conquista a marcar.

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Linha do tempo da vida de Miyamoto Musashi, de 1584 a 1645, com as idades na contagem
> japonesa, a que ele usa no livro. 1584: nasce. 1596, aos 13 anos: primeiro duelo. 1612, aos
> 29: Ganryūjima, o duelo com Kojirō. Por volta de 1633, perto dos 50: sente que entendeu o
> Caminho. 1643, aos 60: sobe ao Reigandō e começa o livro. 1645, aos 62: entrega o livro,
> escreve o Dokkōdō e morre, em 13 de junho. O trecho de 1612 a 1643 está em destaque: 31 anos,
> três décadas, entre o duelo e o livro. A data de 1612 vem de fontes do século XVIII e é a da
> tradição.

**Legenda:**

> Entre Ganryūjima e o livro, passaram-se três décadas: 31 anos entre o duelo de 1612 e o
> retiro de 1643. Idades na contagem japonesa, como no próprio livro. A data de 1612 é a da
> tradição, registrada em fontes do século XVIII.

## diag-02

**Onde entra:** seção "Os cinco anéis numa segunda-feira". Substitui a tabela Markdown, que a
Substack não renderiza.

**Por que é diag (raciocínio de `02-estrutura.md`):** é uma comparação estrutural (5 anéis × 4
colunas de texto), sem métrica, o que dá diag pelo critério 2, mesmo tratamento das tabelas sem
número do post da debênture. graf perde: não há número. info perde: a tabela já é a síntese
numa peça só, e o critério de gatilho do infográfico ("nenhuma peça isolada carrega a síntese
sozinha") falha justamente porque esta carrega. O texto das células é o do autor, sem edição
nesta etapa.

**Pergunta que o diagrama responde:** para cada anel, o que Musashi escreveu, como isso se lê
numa carreira em finanças e que pergunta levar para esta semana?

**Fonte dos dados:** sem cifra. A coluna "O que Musashi escreveu" foi conferida contra o
original japonês em `processo/07-verificacao.md`, item 11 (koten.net 103–105, 238, 310, 324,
401–410, 501), com "distinguir ganho de perda" já na forma da etapa 6
(`processo/06-revisao.md`, l. 210). As colunas 3 e 4 são leitura do autor.

**Código Plotly executável** (gera `figuras/diag-02.svg` e `figuras/diag-02.png`):

```python
import json
import os
import textwrap

import plotly.graph_objects as go

POST_DIR = "posts/2026-10-27-samurais-e-duelos"
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


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

# Conteúdo: tabela "Os cinco anéis numa segunda-feira" depois das etapas 6–7, verbatim.
# As quebras <br> só distribuem o texto nas células (textwrap, sem mudar palavra).
ROWS = [
    ("Terra", "Chi",
     "Conhecer as medidas e as ferramentas; distinguir ganho de perda; não fazer nada inútil",
     "Auditoria honesta de para onde vai sua energia — inclusive o que a IA faz por você",
     "Quantas horas desta semana exigiram cabeça de verdade?"),
    ("Água", "Sui",
     "Adaptar-se como a água; vencer o eu de ontem; mil dias para forjar, dez mil para polir",
     "Contornar a pedra em vez de virar pedra; constância sem promessa de retorno em um ano",
     "Qual obstáculo você está esperando sair do caminho sozinho?"),
    ("Fogo", "Ka",
     "Tomar a iniciativa; quando a luta trava, abandonar a abordagem e recomeçar",
     "O desconforto com o próprio estado como combustível — mirado no hábito, não em você",
     "Que impasse você está tentando resolver empurrando mais forte?"),
    ("Vento", "Fū",
     "Criticar as escolas rivais; conhecer os outros para conhecer a si mesmo",
     "Aprendiz permanente; estudar como outras casas resolvem o mesmo problema",
     "O que você aprendeu este mês que não é o jeito da sua casa?"),
    ("Vazio", "Kū",
     "Dissipar a confusão acumulando prática, dia após dia",
     "Não há linha de chegada: o atrito fica, o sofrimento inútil não",
     "Que esforço você está fazendo esperando que um dia acabe?"),
]
WRAP = 23  # caracteres por linha nas colunas de texto, calibrado para 900 px e fonte 18


def wrap(t):
    linhas = textwrap.wrap(t, WRAP, break_long_words=False)
    assert " ".join(linhas) == t  # quebra não muda o texto
    return "<br>".join(linhas)


def pad(row):
    # Plotly desloca verticalmente célula com menos linhas que as vizinhas; igualar alinha tudo
    k = max(t.count("<br>") for t in row)
    return [t + "<br> " * (k - t.count("<br>")) for t in row]


rows = [pad([f"<b>{anel}</b><br>(<i>{jp}</i>)", wrap(a), wrap(b), wrap(q)])
        for anel, jp, a, b, q in ROWS]
values = [[r[j] for r in rows] for j in range(4)]
n = len(rows)

# A coluna da pergunta é a que vai para a segunda-feira: fundo mint, o resto em branco.
fills = [[white] * n, [white] * n, [white] * n, [mint] * n]

fig = go.Figure(go.Table(
    columnwidth=[0.46, 1, 1, 1],
    header=dict(
        values=["<b>Anel</b>", "<b>O que Musashi<br>escreveu</b>",
                "<b>O que eu leio<br>para a carreira</b>", "<b>Pergunta para<br>esta semana</b>"],
        fill_color=forest, line_color=forest, align="left", height=60,
        font=dict(color=bg, size=18, family=font_display),
    ),
    cells=dict(
        values=values, fill_color=fills, line_color=mist, align="left", height=34,
        font=dict(color=[forest, ink, ink, ink], size=18, family=font_body),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-14, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Segunda coluna: síntese do <i>Livro dos Cinco Anéis</i> (<i>Gorin no Sho</i>, 1645). "
         "Terceira e quarta: leitura de carreira, interpretação, não tradução.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=900, height=750,
    margin=dict(l=24, r=24, t=72, b=56),
    title=dict(text="Cinco anéis, cinco perguntas para esta semana",
               font=dict(color=ink, size=22, family=font_display), x=0.03, xanchor="left"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-02.svg"))
fig.write_image(os.path.join(out_dir, "diag-02.png"), scale=2)
```

**Escolha de layout:** `go.Table` de quatro colunas, com o mesmo cabeçalho do rascunho, lida da
esquerda para a direita como o texto: o anel → o que Musashi escreveu → a leitura → a pergunta.
A coluna da pergunta tem fundo `mint` porque é a que o leitor leva para a segunda-feira (o
título da seção). O nome do anel vai em `forest` negrito, com o termo japonês em itálico de
palavra estrangeira, não de ênfase. Para a largura de e-mail, a figura tem 900 px e fonte 18:
num corpo de e-mail de cerca de 600 px, o texto das células fica perto de 12 px. As quebras de
linha são automáticas (`textwrap`, 23 caracteres), e um `assert` garante que nenhuma palavra
mudou. Células com menos linhas que as vizinhas recebem linhas vazias, porque o Plotly desloca
o texto delas na vertical (mesmo recurso do post da debênture). Descartados: cinco cartões
empilhados, um por anel (cabem melhor no celular, mas perdem a leitura por coluna, que separa
"o que Musashi escreveu" de "o que eu leio", o contrato do texto), e a tabela em duas imagens
(divide a síntese que justifica a peça).

**Tokens usados:** `color.neutral.chalk` (fundo), `color.forest.500` (cabeçalho, nome do
anel), `color.neutral.white` (células: superfície elevada sobre o chalk), `color.neutral.mint`
(coluna da pergunta), `color.neutral.mist` (hairlines), `color.neutral.ink` (texto),
`color.neutral.slate` (nota); `typography.fontFamily.display` (título, cabeçalho), `.body`
(células, nota). Sem `lime`: a pergunta é convite, não conquista, e o `mint` basta para guiar o
olho.

**Alt-text (para o placeholder `diag-02` em `post.md`):**

> Tabela com os cinco anéis do livro de Musashi em quatro colunas: o anel, o que Musashi
> escreveu, o que o autor lê para a carreira e uma pergunta para esta semana. Terra (Chi):
> conhecer as medidas e as ferramentas, distinguir ganho de perda, não fazer nada inútil. A
> leitura é uma auditoria honesta de para onde vai sua energia, inclusive o que a IA faz por
> você. Pergunta: quantas horas desta semana exigiram cabeça de verdade? Água (Sui):
> adaptar-se como a água, vencer o eu de ontem, mil dias para forjar e dez mil para polir. A
> leitura é contornar a pedra em vez de virar pedra, com constância sem promessa de retorno em
> um ano. Pergunta: qual obstáculo você está esperando sair do caminho sozinho? Fogo (Ka):
> tomar a iniciativa e, quando a luta trava, abandonar a abordagem e recomeçar. A leitura é o
> desconforto com o próprio estado como combustível, mirado no hábito, não em você. Pergunta:
> que impasse você está tentando resolver empurrando mais forte? Vento (Fū): criticar as
> escolas rivais, conhecer os outros para conhecer a si mesmo. A leitura é ser aprendiz
> permanente e estudar como outras casas resolvem o mesmo problema. Pergunta: o que você
> aprendeu este mês que não é o jeito da sua casa? Vazio (Kū): dissipar a confusão acumulando
> prática, dia após dia. A leitura é que não há linha de chegada: o atrito fica, o sofrimento
> inútil não. Pergunta: que esforço você está fazendo esperando que um dia acabe?

**Legenda:**

> Os cinco anéis numa segunda-feira: o que Musashi escreveu, a leitura de carreira e uma
> pergunta para esta semana. A segunda coluna resume o *Livro dos Cinco Anéis*; a terceira e a
> quarta são interpretação, não tradução.
