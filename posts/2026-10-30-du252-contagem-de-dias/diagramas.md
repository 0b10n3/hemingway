# Diagramas — "Você está contando os dias úteis errado (e isso está custando dinheiro)"

Uma peça, decidida em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN") e
posicionada em `processo/04-draft-v2.md`, seção "ANBIMA ou B3? Duas perguntas diferentes". Os
dias e as contagens vêm de `processo/03-pesquisa.md` §6 e foram conferidos na etapa 7
(`processo/07-verificacao.md`, l. 170–181). Ferramenta: Plotly, com a grade feita em
`add_shape`/`add_annotation`, mesmo padrão de `graf-NN` e dos diagramas do post dos samurais
(`posts/2026-10-27-samurais-e-duelos/diagramas.md`). Os tokens são lidos em runtime de
`../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do repositório
(`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Os gráficos do post (dias úteis por ano e o CDB em quatro réguas) estão em `graficos.md`.
Nenhum `info-NN`: o critério de gatilho falha, porque cada peça carrega a própria síntese
(`02-estrutura.md`).

## Dados

O CSV sai dos dois calendários do pacote `bizdays` 1.0.19 (`ANBIMA.cal` e `B3.cal`), não é
digitado. O bloco confere o resultado contra a lista dia a dia de `03-pesquisa.md` §6, que a
etapa 7 confirmou contra o calendário ANBIMA de 2026 e o OC 041/2026-VNC da B3. Mesma
dependência do bloco "Dados" de `graficos.md` (`pip install bizdays==1.0.19`). É o único bloco
deste arquivo que importa `bizdays`.

```python
import csv
import datetime as dt
import os
from importlib.metadata import version

from bizdays import Calendar

assert version("bizdays") == "1.0.19", version("bizdays")

POST_DIR = "posts/2026-10-30-du252-contagem-de-dias"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)
anbima, b3 = Calendar.load("ANBIMA"), Calendar.load("B3")
assert b3.enddate >= dt.date(2026, 12, 31)   # o B3.cal do pacote vai só até o fim de 2026

rows = []
for dia in range(1, 32):
    d = dt.date(2026, 12, dia)
    util, pregao = int(anbima.isbizday(d)), int(b3.isbizday(d))
    assert util or not pregao                # não existe pregão fora de dia útil
    estado = ("util_e_pregao" if pregao else "util_sem_pregao") if util else "nenhum"
    rows.append({"data": d.isoformat(), "dia_semana": d.weekday(),   # 0 = segunda
                 "dia_util_anbima": util, "pregao_b3": pregao, "estado": estado})

# confere com processo/03-pesquisa.md §6 ("Dezembro de 2026")
por_estado = {e: [int(r["data"][-2:]) for r in rows if r["estado"] == e]
              for e in ("util_e_pregao", "util_sem_pregao", "nenhum")}
assert por_estado["util_e_pregao"] == [1, 2, 3, 4, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18,
                                       21, 22, 23, 28, 29, 30]
assert por_estado["util_sem_pregao"] == [24, 31]
assert por_estado["nenhum"] == [5, 6, 12, 13, 19, 20, 25, 26, 27]
assert sum(r["dia_util_anbima"] for r in rows) == 22 and sum(r["pregao_b3"] for r in rows) == 20

with open(os.path.join(out, "diag-01.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
```

## diag-01

**Onde entra:** "ANBIMA ou B3? Duas perguntas diferentes", logo depois do parágrafo "Em
números: dezembro de 2026 tem 22 dias úteis no calendário ANBIMA e 20 dias de pregão no da B3.
Se você acumular os juros…" e antes da nota histórica sobre os feriados de São Paulo.

**Por que é diag (raciocínio de `02-estrutura.md`):** relação estrutural, que diz quais dias
pertencem a qual calendário, sem métrica central. Isso dá diag pelo critério 2. Torna visível
que a diferença está em dois dias específicos e não espalhada no ano. graf perde porque não há
série a comparar, e a contagem 22 × 20 cabe na frase. info perde porque é uma peça só.

**Pergunta que o diagrama responde:** onde estão, em dezembro de 2026, os dois dias em que o
juro corre e a bolsa não abre?

**Fonte dos dados:**
- Dias úteis: calendário de feriados nacionais da ANBIMA para 2026
  ([anbima.com.br/feriados/fer_nacionais/2026.asp](https://www.anbima.com.br/feriados/fer_nacionais/2026.asp),
  acesso em 2026-10-30). Em dezembro, o único feriado é 25/12. O critério de dia útil é a
  Resolução CMN nº 4.880/2020 (`03-pesquisa.md` §6).
- Dias de pregão: B3, Ofício Circular 041/2026-VNC (errata, 30/06/2026), "Calendário de
  feriados em 2026"
  ([PDF](https://www.b3.com.br/data/files/20/57/01/AA/06A1F910ADC36BE9AC094EA8/OC%20041-2026-VNC%20ERRATA%20-%20CALENDARIO%20DE%20FERIADOS%20EM%202026_PT.pdf),
  acesso em 2026-10-30). Ele registra 24/12 e 31/12 como "expediente interno nas instituições
  bancárias", sem sessão de negociação.
- O CSV sai do `ANBIMA.cal` e do `B3.cal` do pacote `bizdays` 1.0.19, que batem com as duas
  fontes oficiais (`07-verificacao.md`, l. 170–171 e 181).

**Dados:** `posts/2026-10-30-du252-contagem-de-dias/graficos/dados/diag-01.csv`, 31 linhas
(1 a 31/12/2026). Colunas: `data`, `dia_semana` (0 = segunda), `dia_util_anbima` (1/0),
`pregao_b3` (1/0) e `estado` (`util_e_pregao`, `util_sem_pregao` ou `nenhum`).

**Código Plotly executável** (gera `figuras/diag-01.svg` e `figuras/diag-01.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-10-30-du252-contagem-de-dias"
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

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/diag-01.csv"))
df["dia"] = df["data"].str[-2:].astype(int)
# Semana começando na segunda: linha = semana do mês, coluna = dia da semana (0 = segunda).
desloc = int(df.loc[df["dia"] == 1, "dia_semana"].iloc[0])
df["linha"] = (df["dia"] - 1 + desloc) // 7
n_linhas = int(df["linha"].max()) + 1
n_util, n_pregao = int(df["dia_util_anbima"].sum()), int(df["pregao_b3"].sum())
conta = df["estado"].value_counts()
sem_pregao = df.loc[df["estado"] == "util_sem_pregao", "dia"].tolist()

# Três estados. Cada um se distingue por mais que cor (DESIGN.md §8, 1.4.1): o "sem pregão"
# vem escrito na célula, os fins de semana têm o nome da coluna e o Natal vem escrito.
ESTILO = {
    "util_e_pregao": dict(fill=mint, line=forest, num=ink),
    "util_sem_pregao": dict(fill=forest, line=forest, num=bg),
    "nenhum": dict(fill=bg, line=mist, num=slate),
}
ROTULO = {25: "Natal"}  # o único feriado nacional de dezembro (ANBIMA, feriados de 2026)
G = 0.05                # meio vão entre células

fig = go.Figure()

for j, nome in enumerate(["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]):
    fig.add_annotation(x=j + 0.5, y=0.12, yanchor="bottom", showarrow=False, text=nome,
                       font=dict(color=ink if j < 5 else slate, size=16, family=font_body))

for _, r in df.iterrows():
    e = ESTILO[r["estado"]]
    x0, y1 = int(r["dia_semana"]), -int(r["linha"])
    fig.add_shape(type="rect", x0=x0 + G, x1=x0 + 1 - G, y0=y1 - 1 + G, y1=y1 - G,
                  fillcolor=e["fill"], line=dict(color=e["line"], width=1.5), layer="below")
    destaque = r["estado"] == "util_sem_pregao"
    fig.add_annotation(x=x0 + 0.15, y=y1 - 0.12, xanchor="left", yanchor="top",
                       showarrow=False, text=f"<b>{r['dia']}</b>" if destaque else str(r["dia"]),
                       font=dict(color=e["num"], size=18, family=font_data))
    baixo = "sem<br>pregão" if destaque else ROTULO.get(int(r["dia"]))
    if baixo:
        fig.add_annotation(x=x0 + 0.15, y=y1 - 1 + 0.1, xanchor="left", yanchor="bottom",
                           showarrow=False, align="left", text=baixo,
                           font=dict(color=e["num"], size=12, family=font_body))

# Legenda à direita da grade, com as contagens lidas do CSV.
LX = 7.55
ITENS = [
    ("util_e_pregao", f"<b>Dia útil e dia de pregão: {conta['util_e_pregao']}</b><br>"
                      "o juro corre e a bolsa abre"),
    ("util_sem_pregao", f"<b>Dia útil sem pregão: {conta['util_sem_pregao']}</b><br>"
                        "o juro corre, a bolsa não abre<br>"
                        f"({' e '.join(str(d) for d in sem_pregao)} de dezembro)"),
    ("nenhum", f"<b>Nem um nem outro: {conta['nenhum']}</b><br>fins de semana e Natal"),
]
for k, (estado, texto) in enumerate(ITENS):
    e = ESTILO[estado]
    yt = -0.15 - k * 1.2
    fig.add_shape(type="rect", x0=LX, x1=LX + 0.42, y0=yt - 0.42, y1=yt,
                  fillcolor=e["fill"], line=dict(color=e["line"], width=1.5))
    fig.add_annotation(x=LX + 0.62, y=yt + 0.04, xanchor="left", yanchor="top",
                       showarrow=False, align="left", text=texto,
                       font=dict(color=ink, size=15, family=font_body))
fig.add_shape(type="line", x0=LX, x1=11.1, y0=-3.75, y1=-3.75, line=dict(color=mist, width=1))
fig.add_annotation(
    x=LX, y=-3.95, xanchor="left", yanchor="top", showarrow=False, align="left",
    text=f"ANBIMA: <b>{n_util} dias úteis</b> "
         f"({conta['util_e_pregao']} + {conta['util_sem_pregao']})<br>"
         f"B3: <b>{n_pregao} dias de pregão</b>",
    font=dict(color=forest, size=16, family=font_body),
)

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-14, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Fontes: ANBIMA, feriados nacionais de 2026; B3, Ofício Circular 041/2026-VNC "
         "(errata, 30/06/2026). Dia útil: Resolução CMN nº 4.880/2020.<br>"
         "Semana começando na segunda-feira.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=566,
    margin=dict(l=24, r=24, t=62, b=60),
    xaxis=dict(visible=False, range=[-0.05, 11.2]),
    yaxis=dict(visible=False, range=[-n_linhas - 0.05, 0.6], scaleanchor="x", scaleratio=1),
    title=dict(text="Dezembro de 2026: em dois dias, o juro corre e a bolsa não abre",
               font=dict(color=ink, size=22, family=font_display), x=0.027, xanchor="left",
               y=0.965, yanchor="top"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "diag-01.svg"))
fig.write_image(os.path.join(out_dir, "diag-01.png"), scale=2)
```

**Escolha de layout:** grade de calendário de 7 colunas por 5 semanas, **começando na
segunda-feira**. Começar na segunda põe sábado e domingo juntos na borda direita, como um bloco
só, e deixa os cinco dias de semana contíguos. Assim, o que interrompe a semana útil (24, 25 e
31) salta à vista dentro do bloco, em vez de competir com fins de semana partidos nas duas
bordas, como acontece na folhinha que começa no domingo. É também a convenção do `numpy` e do
`bizdays` (`weekday()`, 0 = segunda), que aparecem no texto. 24 e 31 caem na mesma coluna
(quinta-feira), um embaixo do outro, e o leitor vê o padrão, véspera de Natal e último dia útil
do ano. A legenda fica à direita, com as contagens: 20 + 2 = 22 dias úteis, 20 pregões. Os
dias de novembro e janeiro que completariam a primeira e a última semana ficam em branco,
porque não pertencem à conta. Descartados: (1) a folhinha começando no domingo, que separa o
fim de semana; (2) uma linha do tempo de 31 dias, que perde a leitura por semana e espalha os
dois dias; (3) duas grades lado a lado, ANBIMA e B3, que obrigam o leitor a achar a diferença
comparando 62 células em vez de ver dois dias marcados numa grade só.

**Anotação:** as duas células do achado, 24 e 31, têm o rótulo "sem pregão" escrito dentro,
número em negrito e fundo `forest`. A anotação fica no próprio dado, sem seta. A legenda
repete o achado em palavras ("o juro corre, a bolsa não abre", "24 e 31 de dezembro"), e o
título dá a resposta à pergunta.

**Gate de Tufte:** sem eixo, sem barra nem área codificando grandeza: cada célula é um dia, do
mesmo tamanho, e a cor marca estado, não quantidade. Lie Factor não se aplica. Sem 3D, sombra,
textura nem moldura. Cantos retos (DESIGN.md §4.3).

**Acessibilidade (DESIGN.md §8, 1.4.1):** nenhum estado depende só de cor. "Sem pregão" vem
escrito nas duas células. Os fins de semana se reconhecem pela coluna ("sáb", "dom"), e o
Natal vem escrito. Os dias úteis com pregão são as células restantes, todas com contorno
`forest`. Os dias sem nenhum dos dois têm contorno `mist`.

**Tokens usados:** `color.neutral.chalk` (fundo, células de "nem um nem outro", número sobre
`forest`), `color.neutral.mint` (dias úteis com pregão), `color.forest.500` (dias úteis sem
pregão, contornos, contagens), `color.neutral.mist` (contorno dos dias sem nenhum dos dois,
divisor da legenda), `color.neutral.ink` (números, legenda, título), `color.neutral.slate`
(fins de semana, rodapé); `typography.fontFamily.display` (título), `.body` (rótulos, legenda,
rodapé), `.data` (números dos dias). Sem `lime`: o achado é uma diferença de calendário, não
uma conquista.

**Alt-text (para o placeholder `diag-01` em `post.md`):**

> Calendário de dezembro de 2026, com a semana começando na segunda-feira e três tipos de dia.
> Dia útil e dia de pregão, quando o juro corre e a bolsa abre: 1 a 4, 7 a 11, 14 a 18, 21 a
> 23 e 28 a 30, vinte dias. Dia útil sem pregão, quando o juro corre e a bolsa não abre: 24 e
> 31, as duas quintas-feiras da véspera de Natal e do último dia útil do ano, em destaque. Nem
> dia útil nem pregão: os fins de semana (5 e 6, 12 e 13, 19 e 20, 26 e 27) e o Natal, dia 25,
> nove dias. No total, 22 dias úteis no calendário ANBIMA e 20 dias de pregão na B3. Fontes:
> ANBIMA, feriados nacionais de 2026, e B3, Ofício Circular 041/2026-VNC.

**Legenda:**

> Dezembro de 2026 tem 22 dias úteis no calendário ANBIMA e 20 dias de pregão na B3. A
> diferença inteira está em dois dias, 24 e 31: o juro corre, a bolsa não abre. Fontes: ANBIMA,
> feriados nacionais de 2026; B3, Ofício Circular 041/2026-VNC.

**Placeholder sugerido para `post.md` (etapa 9):**

```markdown
![Diagrama: calendário de dezembro de 2026. Dos 22 dias úteis do calendário ANBIMA, 20 têm pregão na B3; os outros dois, 24 e 31 de dezembro, são dia útil sem pregão: o juro corre e a bolsa não abre. Fins de semana e o Natal (25) não são nem um nem outro.](diag-01)
```
