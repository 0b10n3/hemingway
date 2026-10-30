# Gráficos — "Você está contando os dias úteis errado (e isso está custando dinheiro)"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN")
e posicionadas em `processo/04-draft-v2.md`. A janela do graf-01 (2001–2030) é decisão do autor
na crítica M-7 (`processo/05-critica.md`; `estado.json`, aprovações). O rodapé do graf-01 e o
218,18 do graf-02 vêm de `processo/07-verificacao.md` ("Para a etapa 8" e O-1). Os números
foram conferidos em `_revisoes/2026-10-30_2026-10-30-du252-contagem-de-dias_calculo.md`. O
checklist de craft (`.claude/agents/references/checklist-graficos.md`) foi aplicado. Os tokens
de marca são lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a
partir da raiz do repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

O diagrama do post (calendário de dezembro de 2026) está em `diagramas.md`. Não há `info-NN`:
cada peça carrega a própria ideia (`02-estrutura.md`).

## Dados

Os dois CSVs saem do cálculo, não são digitados. O bloco abaixo regenera
`graficos/dados/graf-01.csv` e `graficos/dados/graf-02.csv` e confere o resultado contra os
números da etapa 7. Se o calendário, a fórmula ou um parâmetro mudar, um `assert` falha.

**Dependência:** `bizdays` 1.0.19 (`pip install bizdays==1.0.19`). O calendário vem dentro do
pacote, no arquivo `ANBIMA.cal` (feriados nacionais ANBIMA até 2099). É o único bloco que
importa `bizdays`: os blocos dos gráficos leem só os CSVs versionados.

```python
import csv
import datetime as dt
import os
from decimal import ROUND_HALF_UP, Decimal as D, getcontext
from importlib.metadata import version

from bizdays import Calendar

assert version("bizdays") == "1.0.19", version("bizdays")
getcontext().prec = 40

POST_DIR = "posts/2026-10-30-du252-contagem-de-dias"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)
anbima = Calendar.load("ANBIMA")

# graf-01 — dias úteis por ano no calendário ANBIMA, 2001-2030.
# 2027-2030 são projeção: o ANBIMA.cal já traz esses feriados pelas regras de hoje, mas uma lei
# nova pode mudar a conta (como a Lei 14.759/2023 mudou a partir de 2024).
ULTIMO_OBSERVADO = 2026
g1 = []
for ano in range(2001, 2031):
    du = len(anbima.seq(f"{ano}-01-01", f"{ano}-12-31"))
    rend = (D("1.12") ** (D(du) / 252) - 1) * 100       # 12% a.a. base 252 num ano de du dias
    g1.append({"ano": ano, "dias_uteis": du, "projecao": int(ano > ULTIMO_OBSERVADO),
               "rendimento_12aa_pct": str(rend.quantize(D("0.0001"), ROUND_HALF_UP))})

# confere com processo/07-verificacao.md (l. 141-144) e _revisoes/..._calculo.md
ETAPA7 = {2001: 250, 2002: 253, 2003: 253, 2004: 252, 2005: 251, 2006: 249, 2007: 250,
          2008: 254, 2009: 250, 2010: 251, 2011: 251, 2012: 251, 2013: 253, 2014: 253,
          2015: 250, 2016: 251, 2017: 249, 2018: 250, 2019: 253, 2020: 251, 2021: 251,
          2022: 251, 2023: 249, 2024: 253, 2025: 252, 2026: 249, 2027: 251, 2028: 248,
          2029: 249, 2030: 252}
assert {r["ano"]: r["dias_uteis"] for r in g1} == ETAPA7
dus = [r["dias_uteis"] for r in g1]
assert [r["ano"] for r in g1 if r["dias_uteis"] == 252] == [2004, 2025, 2030]
assert sum(d < 252 for d in dus) == 20 and sum(d > 252 for d in dus) == 7
assert sum(dus) / len(dus) == 251.0 and (min(dus), max(dus)) == (248, 254)
r = {x["dias_uteis"]: x["rendimento_12aa_pct"] for x in g1}
assert (r[249], r[253]) == ("11.8490", "12.0504")      # 11,85% (2026) e 12,05% (2024)

with open(os.path.join(out, "graf-01.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(g1[0]))
    w.writeheader()
    w.writerows(g1)

# graf-02 — CDB prefixado de R$ 100.000 a 12% a.a., 01/10/2026 a 01/12/2026, em quatro réguas.
# Sem truncamento (Nota de rigor do texto). A diferença é entre resgates já arredondados ao
# centavo: é a conta que o leitor refaz na tabela (O-1 da etapa 7: 218,18, não 218,19).
V, TAXA = D(100000), D("0.12")
ini, fim = "2026-10-01", "2026-12-01"
du = anbima.bizdays(ini, fim)            # (ini, fim], com as duas pontas em dia útil
dc = (dt.date.fromisoformat(fim) - dt.date.fromisoformat(ini)).days
assert (du, dc) == (40, 61), (du, dc)
CALCULOS = [
    ("DU/252, composto (o contratado)", "1,12^(40/252)", (1 + TAXA) ** (D(du) / 252)),
    ("DC/365, composto", "1,12^(61/365)", (1 + TAXA) ** (D(dc) / 365)),
    ("DC/360, composto", "1,12^(61/360)", (1 + TAXA) ** (D(dc) / 360)),
    ("DC/360, linear", "1 + 0,12 × 61/360", 1 + TAXA * D(dc) / 360),
]
cent = D("0.01")
r0 = (V * CALCULOS[0][2]).quantize(cent, ROUND_HALF_UP)
g2 = []
for i, (calc, formula, fator) in enumerate(CALCULOS):
    resgate = (V * fator).quantize(cent, ROUND_HALF_UP)
    g2.append({"calculo": calc, "formula": formula,
               "fator": str(fator.quantize(D("0.00000001"), ROUND_HALF_UP)),
               "resgate": str(resgate), "diferenca": "" if i == 0 else str(resgate - r0),
               "contratado": int(i == 0)})

# confere com o texto (tabela do CDB) depois da correção O-1
assert [x["fator"] for x in g2] == ["1.01815145", "1.01912036", "1.01938848", "1.02033333"]
assert [x["resgate"] for x in g2] == ["101815.15", "101912.04", "101938.85", "102033.33"]
assert [x["diferenca"] for x in g2] == ["", "96.89", "123.70", "218.18"]

with open(os.path.join(out, "graf-02.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(g2[0]))
    w.writeheader()
    w.writerows(g2)
```

## graf-01

**Onde entra:** "Por que o relógio para no sábado", no lugar do marcador `[graf-01 — …]`: depois
de "Quase três décadas depois, o calendário continua não colaborando:" e antes de "Entre 2001 e
2030, só três anos têm exatamente 252 dias úteis: 2004, 2025 e 2030."

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica real, dias úteis por ano
no calendário ANBIMA, o que dá graf pelo critério 1. diag perde porque há métrica. info perde
porque é uma ideia só. A janela foi ampliada de 2024–2028 para 2001–2030 por decisão do autor
(M-7): com cinco anos, o "quase nunca" do subtítulo ficava sem sustentação visível.

**Pergunta que o gráfico responde:** com que frequência um ano tem os 252 dias úteis da
convenção?

**Fonte dos dados:** cálculo próprio a partir do calendário ANBIMA, no arquivo `ANBIMA.cal` do
pacote `bizdays` 1.0.19 ([PyPI](https://pypi.org/project/bizdays/1.0.19/);
[arquivo no repositório do pacote](https://raw.githubusercontent.com/wilsonfreitas/python-bizdays/master/bizdays/ANBIMA.cal),
acesso em 2026-10-30). Série conferida na etapa 7 (`processo/07-verificacao.md`, l. 141–144):
2014–2024 batem com a suíte de testes do `bizdays`, e 2026 com a página oficial da ANBIMA
([feriados nacionais de 2026](https://www.anbima.com.br/feriados/fer_nacionais/2026.asp),
acesso em 2026-10-30; `03-pesquisa.md` §0). **2027–2030 são projeção** pelo calendário
vigente, e a figura diz isso no rodapé e na faixa. O rendimento do eixo da direita é cálculo
próprio derivado: 1,12^(du/252) − 1.

**Dados:** `posts/2026-10-30-du252-contagem-de-dias/graficos/dados/graf-01.csv`, 30 linhas
(2001 a 2030). Colunas: `ano`, `dias_uteis`, `projecao` (1 para 2027–2030) e
`rendimento_12aa_pct` (rendimento de 12% a.a. base 252 num ano com aquele número de dias úteis,
em %, quatro casas).

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

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

CONV = 252  # a convenção: "ao ano, base 252"
df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))
obs, proj = df[df["projecao"] == 0], df[df["projecao"] == 1]
exatos = df[df["dias_uteis"] == CONV]
abaixo, acima = int((df["dias_uteis"] < CONV).sum()), int((df["dias_uteis"] > CONV).sum())
media = df["dias_uteis"].mean()
# rendimento por número de dias úteis, lido do próprio CSV (248 a 254 aparecem todos na série)
rend = df.groupby("dias_uteis")["rendimento_12aa_pct"].first()
niveis = list(range(int(df["dias_uteis"].min()), int(df["dias_uteis"].max()) + 1))
assert list(rend.index) == niveis
ano_corrente = df[df["ano"] == 2026].iloc[0]


def num(v, casas):
    return f"{v:.{casas}f}".replace(".", ",")


fig = go.Figure()

# Faixa da projeção (2027-2030), atrás de tudo.
p0, p1 = proj["ano"].min() - 0.5, proj["ano"].max() + 0.5
fig.add_vrect(x0=p0, x1=p1, fillcolor=mint, line_width=0, layer="below")
fig.add_annotation(xref="x", yref="paper", x=(p0 + p1) / 2, y=1, yanchor="bottom",
                   showarrow=False, align="center", text="projeção pelo<br>calendário vigente",
                   font=dict(color=forest, size=14, family=font_body))

# Barras partem de 252: o comprimento é a diferença para a convenção, para cima ou para baixo.
# Observado: cheia. Projeção: vazada (mesma convenção do marcador vazado nos posts anteriores).
fig.add_trace(go.Bar(x=obs["ano"], y=obs["dias_uteis"] - CONV, base=CONV, width=0.72,
                     marker=dict(color=forest, line=dict(width=0)),
                     showlegend=False, hoverinfo="skip"))
fig.add_trace(go.Bar(x=proj["ano"], y=proj["dias_uteis"] - CONV, base=CONV, width=0.72,
                     marker=dict(color=mint, line=dict(color=forest, width=2)),
                     showlegend=False, hoverinfo="skip"))

# A linha da convenção, por cima das barras.
fig.add_hline(y=CONV, line=dict(color=ink, width=2), layer="above")

# Os anos com exatamente 252: barra de comprimento zero, então o ano vira um marcador na linha.
for _, row in exatos.iterrows():
    vazado = bool(row["projecao"])
    fig.add_trace(go.Scatter(
        x=[row["ano"]], y=[CONV], mode="markers", showlegend=False, hoverinfo="skip",
        marker=dict(symbol="square-open" if vazado else "square", size=13,
                    color=forest, line=dict(color=forest if vazado else ink, width=2))))
    fig.add_annotation(x=row["ano"], y=CONV, ax=0, ay=-118, showarrow=True, arrowhead=0,
                       arrowwidth=1, arrowcolor=ink, standoff=8,
                       text=f"<b>{int(row['ano'])}</b>",
                       font=dict(color=ink, size=16, family=font_data))
fig.add_annotation(xref="x", yref="y", x=2014.5, y=254.55, showarrow=False, align="center",
                   text=f"<b>Exatamente {CONV}: {len(exatos)} anos em {len(df)}</b>",
                   font=dict(color=ink, size=16, family=font_body))

# O ano corrente, o da LTN da abertura do texto.
fig.add_annotation(
    x=int(ano_corrente["ano"]), y=int(ano_corrente["dias_uteis"]), ax=-205, ay=52,
    showarrow=True, arrowhead=2, arrowwidth=1.5, arrowcolor=forest, standoff=2,
    xanchor="right", align="right",
    text=f"<b>{int(ano_corrente['ano'])}, o ano corrente: "
         f"{int(ano_corrente['dias_uteis'])} dias úteis.</b><br>"
         f"Os 12% ao ano rendem {num(ano_corrente['rendimento_12aa_pct'], 2)}%.",
    font=dict(color=forest, size=15, family=font_body),
)

# Rodapé alinhado à borda esquerda da figura (paper x negativo = dentro da margem l).
fig.add_annotation(
    xref="paper", yref="paper", x=-0.075, y=0, yshift=-52, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Fonte: cálculo próprio a partir do calendário ANBIMA "
         f"(<span style='font-family:{font_data}'>ANBIMA.cal</span>, pacote bizdays 1.0.19); "
         "2027–2030 projetados pelo calendário vigente.<br>"
         "Barras partem de 252, a convenção: o comprimento é a diferença em dias úteis. "
         "Eixo da direita: quanto rendem 12% a.a. base 252<br>"
         "num ano com aquele número de dias úteis, 1,12<sup>du/252</sup> − 1. "
         f"Em 2001–2030: {abaixo} anos abaixo de 252, {acima} acima, média de "
         f"{num(media, 1)} dias úteis.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=620,
    margin=dict(l=70, r=78, t=112, b=138), bargap=0,
    title=dict(text=f"De 2001 a 2030, só três anos têm os {CONV} dias úteis da convenção",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.965, yanchor="top"),
    font=dict(family=font_body, color=ink),
    yaxis2=dict(overlaying="y", side="right", matches="y", tickvals=niveis,
                ticktext=[f"<b>{num(rend[n], 2)}%</b>" if n == CONV else f"{num(rend[n], 2)}%"
                          for n in niveis],
                tickfont=dict(color=slate, size=13, family=font_data), showgrid=False,
                zeroline=False, showline=False,
                title=dict(text="rendimento de 12% a.a.",
                           font=dict(color=slate, size=13, family=font_body))),
)
# Trace invisível no eixo da direita: sem dado, o Plotly não desenha o eixo.
fig.add_trace(go.Scatter(x=[df["ano"].min()], y=[CONV], yaxis="y2", mode="markers",
                         marker=dict(opacity=0), showlegend=False, hoverinfo="skip"))
fig.update_xaxes(
    range=[2000.4, 2030.6], tickvals=[2001, 2005, 2010, 2015, 2020, 2025, 2030],
    tickfont=dict(color=slate, size=14, family=font_data),
    showgrid=False, zeroline=False, showline=False, ticks="",
)
# Eixo sem zero, por construção: as barras partem de 252 (ver "Gate de Tufte" abaixo).
fig.update_layout(yaxis=dict(
    range=[247.25, 254.95], tickvals=niveis,
    ticktext=[f"<b>{n}</b>" if n == CONV else str(n) for n in niveis],
    tickfont=dict(color=slate, size=14, family=font_data),
    title=dict(text="dias úteis no ano", font=dict(color=slate, size=13, family=font_body)),
    gridcolor=mist, gridwidth=1, zeroline=False, showline=False,
))

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** barras verticais por ano que **partem da linha de 252**, para cima nos anos
mais longos que a convenção e para baixo nos mais curtos. O comprimento de cada barra é o que a
pergunta mede: quantos dias úteis o ano tem a mais ou a menos que 252. Os três anos com
exatamente 252 têm barra de comprimento zero e aparecem como um marcador sobre a linha. O
"quase nunca" fica visível como ausência: em 30 anos, só três ficam sem barra. O eixo da
direita traduz cada nível em rendimento (249 → 11,85%, 253 → 12,05%), e assim a peça entrega o
que `02-estrutura.md` pedia ("o rendimento efetivo anotado em cada barra") sem 30 rótulos
brigando. 2027–2030 têm barra vazada e faixa `mint`, por serem projeção. Descartados: (1)
barras a partir de zero, até 250, em que diferenças de 1 a 4 dias ocupam menos de 2% da
altura e somem; (2) barras a partir de zero com eixo truncado em 247, que exagera a diferença
sem dizer de onde a barra parte; (3) o rendimento escrito em cada barra, como previa a etapa 2
para 5 anos, que com 30 anos vira ruído; (4) histograma de frequência (quantos anos com 249,
250…), que responde à pergunta mas perde o "o ano é que muda de tamanho" e a posição de 2026.

**Anotação:** (1) os três anos com 252 (2004, 2025, 2030) têm marcador na linha e rótulo com
seta, sob o título "Exatamente 252: 3 anos em 30". O de 2030 é vazado, como as barras da
projeção. (2) 2026, o ano corrente e o da LTN da abertura, tem seta com "249 dias úteis. Os
12% ao ano rendem 11,85%". (3) A faixa da projeção tem o nome escrito no alto. As contagens
(20 abaixo, 7 acima, média 251,0) ficam no rodapé, lidas do CSV. Uma linha de média em 251
ficou de fora: a um dia útil da linha de 252, ela se confundia com as barras de 251.

**Gate de Tufte:**
- **Eixo de barras sem zero, por exceção justificada.** A barra não codifica "dias úteis no
  ano": codifica a diferença para 252, e o zero dessa grandeza é a própria linha de 252, onde
  toda barra começa. O eixo mostra os valores absolutos (248 a 254) só para leitura. Uma barra
  de 249 tem três unidades de comprimento, a de 253 tem uma. O rodapé diz de onde as barras
  partem.
- **Lie Factor:** comprimento de barra proporcional a |du − 252|, numa escala linear. O Lie
  Factor é 1,0 por construção. A faixa `mint` marca uma janela de anos e tem a largura exata
  dela. Os marcadores dos anos com 252 têm tamanho fixo e não codificam grandeza.
- Sem 3D, sombra, textura nem moldura. Só grid horizontal, em `mist`, um por dia útil.
- Uma série, com observado e projeção distinguidos por preenchimento e pela faixa nomeada.
  Abaixo do limiar de três séries: não há caso para *small multiples* nem para revelação
  progressiva.
- Acessibilidade (DESIGN.md §8, 1.4.1): a direção da barra (para cima ou para baixo) carrega o
  "acima ou abaixo de 252" sem depender de cor. A projeção se distingue por preenchimento
  (cheia × vazada) e pela faixa com nome, não só pelo tom.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo),
`color.forest.500` (barras, marcadores, anotação de 2026, nome da faixa),
`color.neutral.mint` (faixa da projeção e miolo das barras vazadas), `color.neutral.ink`
(linha de 252, rótulos dos anos com 252, título), `color.neutral.slate` (eixos, rodapé),
`color.neutral.mist` (grid); `typography.fontFamily.display` (título), `.body` (anotações,
rodapé), `.data` (anos, dias úteis, rendimentos). Sem `lime`: acertar 252 não é conquista, é o
acaso do calendário.

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Gráfico de barras com os dias úteis de cada ano no calendário ANBIMA, de 2001 a 2030. As
> barras partem de uma linha horizontal em 252, a convenção da taxa "ao ano, base 252": sobem
> nos anos com mais dias úteis e descem nos anos com menos. Só três anos têm exatamente 252 e
> ficam sem barra, como um ponto sobre a linha: 2004, 2025 e 2030. Vinte anos ficam abaixo de
> 252 e sete acima, entre 248 dias úteis (2028) e 254 (2008), com média de 251. Em 2026, o
> ano corrente, são 249 dias úteis, e 12% ao ano base 252 rendem 11,85% no ano. Um eixo à
> direita traduz cada número de dias úteis em rendimento, de 11,80% (248) a 12,10% (254). Os
> anos de 2027 a 2030 são projeção pelo calendário vigente. Cálculo próprio a partir do
> calendário ANBIMA.

**Legenda:**

> Em 30 anos, só três têm os 252 dias úteis da convenção: 2004, 2025 e 2030. Vinte ficam
> abaixo e sete acima, com média de 251. Em 2026, com 249 dias úteis, os 12% ao ano rendem
> 11,85%. Fonte: cálculo próprio a partir do calendário ANBIMA (`ANBIMA.cal`, pacote bizdays
> 1.0.19); 2027–2030 projetados pelo calendário vigente.

**Placeholder sugerido para `post.md` (etapa 9):**

```markdown
![Gráfico: dias úteis por ano no calendário ANBIMA, 2001–2030, em barras que partem da convenção de 252. Só 2004, 2025 e 2030 têm exatamente 252; vinte anos ficam abaixo e sete acima, com média de 251. Em 2026, com 249 dias úteis, 12% ao ano rendem 11,85%. 2027–2030 projetados pelo calendário vigente.](graf-01)
```

## graf-02

**Onde entra:** "Quanto custa a régua errada", no lugar da tabela Markdown do CDB (a Substack
não renderiza tabela): depois de "Agora veja o que acontece quando o mesmo número, 12%, é lido
com réguas e motores diferentes:" (ou "Veja o que acontece…", se a etapa 9 aplicar o opcional
da l. 122 de `06-revisao.md`) e antes de "Num CDB de R$ 100 mil, a régua errada promete entre
R$ 97 e R$ 218…".

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica (quatro leituras do mesmo
12%: fator, resgate, diferença), o que dá graf pelo critério 1. Fica em formato de tabela para
preservar as cinco colunas do autor (precedente: graf-01 e graf-02 do CRA). Virar barras
perderia a fórmula e o fator, e isso seria mudança de conteúdo, não de formato.

**Pergunta que o gráfico responde:** quanto o mesmo 12% ao ano paga em dois meses, conforme a
régua e o motor com que é lido?

**Fonte dos dados:** cálculo próprio, sem truncamento, conferido na etapa 7
(`_revisoes/2026-10-30_2026-10-30-du252-contagem-de-dias_calculo.md`, seção 5). A contagem de
40 dias úteis sai do mesmo `ANBIMA.cal` do graf-01. A diferença da linha DC/360 linear é
**+ R$ 218,18** (102.033,33 − 101.815,15), com a correção bloqueante O-1 de
`processo/07-verificacao.md`. O texto do rascunho trazia 218,19.

**Dados:** `posts/2026-10-30-du252-contagem-de-dias/graficos/dados/graf-02.csv`, 4 linhas.
Colunas: `calculo`, `formula` (a do autor, com `^` para potência), `fator` (oito casas),
`resgate` (ao centavo), `diferenca` (resgate menos o do contratado; vazio na linha do
contratado) e `contratado` (1 na linha DU/252).

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

```python
import json
import os
import re

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
white = c["neutral"]["white"]["$value"]
forest = c["forest"]["500"]["$value"]
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02.csv"), dtype=str,
                 keep_default_na=False)
assert df["contratado"].tolist() == ["1", "0", "0", "0"]


def brl(s):
    # "101815.15" -> "101.815,15"
    inteiro, dec = s.split(".")
    return f"{int(inteiro):,}".replace(",", ".") + "," + dec


def potencia(s):
    # "1,12^(40/252)" -> 1,12 com o expoente sobrescrito
    return re.sub(r"\^\((.+?)\)", r"<sup>\1</sup>", s)


fatores = [x.replace(".", ",") for x in df["fator"]]
resgates = ["R$ " + brl(x) for x in df["resgate"]]
difs = ["—" if x == "" else "+ R$ " + brl(x) for x in df["diferenca"]]
# Quebra antes do parêntese só na exibição, para a coluna não espremer as de número.
calcs = [x.replace(" (", "<br>(") for x in df["calculo"]]
formulas = [potencia(x) for x in df["formula"]]

# A linha do contratado é a única em destaque: fundo mint e negrito (o negrito do rascunho saiu
# do texto pela regra 4 e mora aqui). Destaque por peso e rótulo, não só por cor (DESIGN.md §8).
dest = df["contratado"] == "1"


def b(vals):
    return [f"<b>{v}</b>" if d else v for v, d in zip(vals, dest)]


fills = [mint if d else white for d in dest]

fig = go.Figure(go.Table(
    columnwidth=[1.2, 1.35, 1.0, 1.25, 1.05],
    header=dict(
        values=["<b>Cálculo</b>", "<b>Fórmula</b>", "<b>Fator</b>", "<b>Valor de resgate</b>",
                "<b>Diferença</b>"],
        fill_color=forest, line_color=forest, align=["left", "left", "right", "right", "right"],
        height=46, font=dict(color=bg, size=16, family=font_display),
    ),
    cells=dict(
        values=[b(calcs), b(formulas), b(fatores), b(resgates), b(difs)],
        fill_color=[fills] * 5, line_color=mist, height=44,
        align=["left", "left", "right", "right", "right"],
        font=dict(color=[[forest if d else ink for d in dest]] + [ink] * 4, size=16,
                  family=[font_body, font_data, font_data, font_data, font_data]),
    ),
    domain=dict(x=[0, 1], y=[0, 1]),
))

fig.add_annotation(
    xref="paper", yref="paper", x=0, y=1, yshift=10, xanchor="left", yanchor="bottom",
    showarrow=False, align="left",
    text="CDB prefixado de R$ 100.000 a 12% ao ano, de 01/10/2026 a 01/12/2026: "
         "40 dias úteis, 61 dias corridos.",
    font=dict(color=slate, size=15, family=font_body),
)
fig.add_annotation(
    xref="paper", yref="paper", x=0, y=0, yshift=-10, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Diferença: valor de resgate da linha menos o do contratado (DU/252, composto). "
         "Cálculo próprio, sem truncamento.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, width=900, height=380,
    margin=dict(l=24, r=24, t=92, b=44),
    title=dict(text="A régua errada promete até R$ 218,18 que o contrato não paga",
               font=dict(color=ink, size=22, family=font_display), x=0.027, xanchor="left",
               y=0.95, yanchor="top"),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
```

**Escolha de tipo:** `go.Table` com as cinco colunas do autor, na ordem dele: cálculo →
fórmula → fator → resgate → diferença. A linha do contratado tem fundo `mint`, negrito e o
nome do cálculo em `forest`. É a única linha que estava em negrito no rascunho, e o negrito sai
do texto pela regra 4 (`06-revisao.md`). Os números usam a fonte de dados (monoespaçada),
alinhados à direita, para que as casas fiquem na mesma coluna e a diferença se leia de cima
para baixo. A fórmula tem o expoente sobrescrito, como no bloco de equação do texto. O cenário
(valor, taxa, datas, 40 DU, 61 DC) vai no subtítulo, porque sem ele o leitor que chega pela
imagem não sabe de que CDB se trata. Descartados: barras da diferença (perdem fórmula e fator,
mudança de conteúdo, `02-estrutura.md`) e a lista de taxas equivalentes dentro da peça (fica
em prosa, lista nativa da Substack, `02-estrutura.md`).

**Anotação:** numa tabela, o ponto de interesse é uma linha, e o destaque dela faz o papel da
seta: fundo `mint`, negrito e o rótulo "(o contratado)" no próprio texto. O título entrega o
achado (até R$ 218,18), e o subtítulo dá o cenário.

**Gate de Tufte:** tabela sem eixo, então não há `rangemode` a declarar. Nenhuma área ou cor
codifica grandeza: o `mint` marca função (a linha de referência), não tamanho. Lie Factor não
se aplica. Sem 3D, sombra, textura nem moldura: só hairlines em `mist`.

**Tokens usados:** `color.neutral.chalk` (fundo, texto do cabeçalho), `color.forest.500`
(cabeçalho, nome do contratado), `color.neutral.white` (células: superfície elevada sobre o
chalk), `color.neutral.mint` (linha do contratado), `color.neutral.mist` (hairlines),
`color.neutral.ink` (texto, título), `color.neutral.slate` (subtítulo, nota);
`typography.fontFamily.display` (título, cabeçalho), `.body` (nome do cálculo, subtítulo,
nota), `.data` (fórmulas e números). Sem `lime`: a linha do contratado é a referência, não uma
conquista.

**Alt-text (para o placeholder `graf-02` em `post.md`):**

> Tabela com o mesmo CDB prefixado calculado de quatro jeitos: R$ 100.000 a 12% ao ano, de
> 1º de outubro a 1º de dezembro de 2026, 40 dias úteis e 61 dias corridos. Colunas: cálculo,
> fórmula, fator, valor de resgate e diferença. A primeira linha, em destaque, é o contratado:
> dias úteis sobre 252, juro composto, 1,12 elevado a 40/252, fator 1,01815145, resgate de
> R$ 101.815,15. Dias corridos sobre 365, composto, 1,12 elevado a 61/365: fator 1,01912036,
> resgate de R$ 101.912,04, R$ 96,89 a mais. Dias corridos sobre 360, composto, 1,12 elevado a
> 61/360: fator 1,01938848, resgate de R$ 101.938,85, R$ 123,70 a mais. Dias corridos sobre
> 360, linear, 1 mais 0,12 vezes 61/360: fator 1,02033333, resgate de R$ 102.033,33, R$ 218,18
> a mais. Cálculo próprio, sem truncamento.

**Legenda:**

> O mesmo 12% ao ano, lido com quatro réguas, num CDB de R$ 100 mil por dois meses: só o
> DU/252 composto entrega o contratado, R$ 101.815,15. As outras três prometem entre R$ 96,89
> e R$ 218,18 a mais, que o contrato não vai pagar. Cálculo próprio, sem truncamento.

**Placeholder sugerido para `post.md` (etapa 9):**

```markdown
![Gráfico: tabela com o mesmo CDB de R$ 100 mil a 12% ao ano, de 01/10 a 01/12/2026, em quatro réguas. Contratado (DU/252, composto, 1,12^(40/252)): R$ 101.815,15. DC/365 composto: + R$ 96,89. DC/360 composto: + R$ 123,70. DC/360 linear: + R$ 218,18.](graf-02)
```
