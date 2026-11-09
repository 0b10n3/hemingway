# Gráficos — "Frequência de Capitalização"

Duas peças, decididas em `processo/02-estrutura.md` ("Visuais — critério da etapa 2", com a
renumeração pela ordem de aparição: graf-01 = linha quebrada de Bernoulli, graf-02 = convergência
da efetiva a 14% para o teto) e posicionadas em `processo/04-draft-v2.md`. O "embedded content"
do rascunho não veio: os dois gráficos foram reconstruídos pela fórmula do texto, em cálculo
próprio. Os números conferem com a prosa e os alt-texts de `04-draft-v2.md`; a etapa 7 ainda não
rodou, e o bloco de dados abaixo fica como registro de cálculo para ela. O checklist de craft
(`.claude/agents/references/checklist-graficos.md`) foi aplicado. Os tokens de marca são lidos em
runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do
repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa (plotly + kaleido).

Não há `diag-NN` nem `info-NN`: cada peça carrega uma ideia só (`02-estrutura.md`).

## Dados

Os CSVs saem do cálculo, não são digitados. O bloco abaixo regenera `graficos/dados/graf-01.csv`
e `graficos/dados/graf-02.csv` e confere o resultado contra os números do texto. Se a fórmula ou
um parâmetro mudar, um `assert` falha. Só biblioteca padrão.

**Nota para a etapa 7 — o que "diária" quer dizer na prosa.** Os valores em R$ 1 milhão de
"Rende todo dia não é render mais" (mensal → diária R$ 887,05; diária → contínua R$ 44,72) saem
de m = 252, a capitalização em dias úteis. Com m = 365, seriam R$ 900,89 e R$ 30,88. Os dois
casos arredondam para 15,02% de efetiva, por isso o alt-text do graf-02 vale para ambos. O texto
não está errado (252 é a convenção da série), mas o leitor que refizer a conta com 365 não chega
aos mesmos reais. O gráfico mostra os dois pontos e os rotula juntos como "diária".

```python
import csv
import math
import os

POST_DIR = "posts/2026-11-09-frequencia-de-capitalizacao"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)


def gravar(nome, linhas):
    with open(os.path.join(out, nome), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)


# graf-01 — capital 1 a 100% ao ano, t de 0 a 1 em passos de 1/120 (contém todo nó k/m de
# m = 1, 2, 4, 12). Dentro do subperíodo k, o juro corre linear sobre o saldo do nó: é a corda
# S_k × (1 + (t − k/m)), com S_k = (1 + 1/m)^k. Contínuo: e^t.
M1 = (1, 2, 4, 12)
N = 120
g1 = []
for j in range(N + 1):
    linha = {"t_anos": f"{j / N:.6f}"}
    for m in M1:
        k = min(j * m // N, m - 1)          # aritmética inteira: o nó cai exato, sem erro de float
        linha[f"m{m}"] = f"{(1 + 1 / m) ** k * (1 + (j / N - k / m)):.6f}"
    linha["continua"] = f"{math.exp(j / N):.6f}"
    g1.append(linha)
gravar("graf-01.csv", g1)

fim = g1[-1]
# confere com 02-estrutura.md (nós 2; 2,25; 2,4414; 2,6130; 2,7183) e 04-draft-v2.md
assert [f"{float(fim[f'm{m}']):.4f}" for m in M1] == ["2.0000", "2.2500", "2.4414", "2.6130"]
assert f"{float(fim['continua']):.4f}" == "2.7183"
# cada linha quebrada fica abaixo (ou junto) da seguinte, e todas abaixo da curva
for r in g1:
    v = [float(r[f"m{m}"]) for m in M1] + [float(r["continua"])]
    assert all(a <= b + 1e-9 for a, b in zip(v, v[1:]))

# graf-02 — efetiva de 14% nominais: (1 + 0,14/m)^m − 1; teto contínuo e^0,14 − 1.
j = 0.14
M2 = (1, 2, 4, 12, 52, 252, 365)
teto = math.exp(j) - 1
g2 = [{"m": m, "efetiva_pct": f"{((1 + j / m) ** m - 1) * 100:.6f}",
       "distancia_teto_pp": f"{(teto - ((1 + j / m) ** m - 1)) * 100:.6f}",
       "teto_pct": f"{teto * 100:.6f}"} for m in M2]
gravar("graf-02.csv", g2)

ef = {r["m"]: float(r["efetiva_pct"]) / 100 for r in g2}
# confere com o alt-text e a prosa de 04-draft-v2.md
assert [f"{ef[m] * 100:.2f}" for m in (1, 2, 12, 252, 365)] == \
       ["14.00", "14.49", "14.93", "15.02", "15.02"]
assert f"{teto * 100:.2f}" == "15.03"
# R$ 1 milhão: anual→mensal 9.342,03; mensal→diária 887,05; diária→contínua 44,72.
# "Diária" na prosa é m = 252 (dias úteis); com m = 365, seriam 900,89 e 30,88.
assert f"{(ef[12] - ef[1]) * 1e6:.2f}" == "9342.03"
assert f"{(ef[252] - ef[12]) * 1e6:.2f}" == "887.05"
assert f"{(teto - ef[252]) * 1e6:.2f}" == "44.72"
# dobrar a frequência corta a distância ao teto quase pela metade
assert all(0.5 < ef_b / ef_a < 0.53 for ef_a, ef_b in
           [(teto - ef[1], teto - ef[2]), (teto - ef[2], teto - ef[4])])
print("ok", fim, [r["efetiva_pct"] for r in g2], teto)
```

## graf-01

**Onde entra:** "A escada de Bernoulli", no lugar do placeholder `graf-01`: depois de "Cada degrau
sobe menos que o anterior. Do anual para o semestral…" e antes de "Bernoulli mostrou, com o
binômio de Newton, que a escada nunca passa de 3."

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica real (o montante de 1 a
100% ao ano, em t ∈ [0, 1]), critério 1. O diagrama perde porque as alturas finais (2; 2,25;
2,44; 2,61; 2,718) são o argumento. Infográfico não cabe: a peça isolada carrega a ideia.

**Pergunta que o gráfico responde:** quando o capital é capitalizado mais vezes no ano, a linha
quebrada chega mais perto da curva e<sup>t</sup> sem nunca passar dela?

**Fonte dos dados:** cálculo próprio. Capital 1 a 100% ao ano, capitalizado m = 1, 2, 4, 12
vezes. Dentro do subperíodo k (de k/m a (k+1)/m), o juro corre linear sobre o saldo do nó:
S<sub>k</sub> × (1 + (t − k/m)), com S<sub>k</sub> = (1 + 1/m)<sup>k</sup>. É a corda do texto. A
curva é e<sup>t</sup>. Valores no fim do ano: 2; 2,25; 2,4414; 2,6130; 2,7183 (os mesmos de
`02-estrutura.md`).

**Dados:** `posts/2026-11-09-frequencia-de-capitalizacao/graficos/dados/graf-01.csv`, 121 linhas
(t = 0 a 1 em passos de 1/120, que contém todos os nós k/m). Colunas: `t_anos`, `m1`, `m2`, `m4`,
`m12`, `continua` (montante, seis casas).

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-11-09-frequencia-de-capitalizacao"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # a série que é o ponto (DESIGN.md §10)
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")


def num(v, casas):
    return f"{v:.{casas}f}".replace(".", ",")


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))
fim = df.iloc[-1]
assert [num(fim[k], 2) for k in ("m1", "m2", "m4", "m12")] == ["2,00", "2,25", "2,44", "2,61"]

fig = go.Figure()
# Linhas quebradas: contexto, em slate. Rótulo direto na ponta no lugar de legenda.
ROTULO = {1: "1 corda", 2: "2 cordas", 4: "4 cordas", 12: "12 cordas"}
for m in (1, 2, 4, 12):
    fig.add_trace(go.Scatter(x=df["t_anos"], y=df[f"m{m}"], mode="lines",
                             line=dict(color=slate, width=2, simplify=False),
                             showlegend=False, hoverinfo="skip"))
    fig.add_annotation(x=1, y=fim[f"m{m}"], xanchor="left", xshift=10, showarrow=False,
                       text=f"{ROTULO[m]}  <b>{num(fim[f'm{m}'], 2)}</b>",
                       font=dict(color=slate, size=14, family=font_body))
# A curva contínua: o ponto do gráfico, em grove.500, desenhada por cima.
fig.add_trace(go.Scatter(x=df["t_anos"], y=df["continua"], mode="lines",
                         line=dict(color=grove, width=3.5), showlegend=False, hoverinfo="skip"))
fig.add_annotation(x=1, y=fim["continua"], xanchor="left", xshift=10, showarrow=False,
                   text=f"<b>curva e<sup>t</sup>  {num(fim['continua'], 3)}</b>",
                   font=dict(color=grove, size=14, family=font_body))
# Marcadores nos valores finais.
fig.add_trace(go.Scatter(x=[1] * 5, y=[fim[k] for k in ("m1", "m2", "m4", "m12", "continua")],
                         mode="markers", showlegend=False, hoverinfo="skip",
                         marker=dict(color=[slate] * 4 + [grove], size=8,
                                     line=dict(color=bg, width=1.5))))

# Anotação 1: a curva fica por cima de toda linha quebrada.
t_a = 0.55
y_a = df.loc[(df["t_anos"] - t_a).abs().idxmin(), "continua"]
fig.add_annotation(x=t_a, y=y_a, ax=-70, ay=-70, showarrow=True, arrowhead=0, arrowwidth=1,
                   arrowcolor=grove, xanchor="right", align="right",
                   text="<b>capitalização contínua</b><br>nenhuma linha quebrada passa dela",
                   font=dict(color=grove, size=14, family=font_body))
# Anotação 2: o primeiro nó da linha de 2 cordas, onde o juro vira saldo e a linha dobra.
fig.add_annotation(x=0.5, y=1.5, ax=60, ay=60, showarrow=True, arrowhead=0, arrowwidth=1,
                   arrowcolor=ink, xanchor="left", align="left",
                   text="<b>6 meses, 2 cordas: o juro vira saldo</b><br>"
                        "e a linha dobra para cima; a de 1 corda segue reta",
                   font=dict(color=ink, size=14, family=font_body))

fig.add_annotation(xref="paper", yref="paper", x=-0.08, y=0, yshift=-58, xanchor="left",
                   yanchor="top", showarrow=False, align="left",
                   text="Fonte: cálculo próprio. Capital de 1 aplicado a 100% ao ano, capitalizado m vezes. "
                        "Dentro de cada subperíodo o juro corre linear<br>(a corda); em cada nó "
                        "k/m ele vira saldo. Valores no fim do ano: (1 + 1/m)<sup>m</sup>; "
                        "contínuo: e<sup>t</sup>.",
                   font=dict(color=slate, size=13, family=font_body))

fig.update_xaxes(range=[-0.02, 1.02], tickvals=[0, 0.25, 0.5, 0.75, 1],
                 ticktext=["0", "3 meses", "6 meses", "9 meses", "1 ano"],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 showgrid=False, zeroline=False, showline=False, ticks="")
# Eixo começa no capital (1), não em zero: ver "Gate de Tufte" em graficos.md.
fig.update_yaxes(range=[0.96, 2.82], tickvals=[1, 1.5, 2, 2.5],
                 ticktext=["1", "1,5", "2", "2,5"],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 title=dict(text="montante (capital inicial = 1)",
                            font=dict(color=slate, size=13, family=font_body)),
                 gridcolor=mist, gridwidth=1, zeroline=False, showline=False)
fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=640,
    margin=dict(l=84, r=170, t=84, b=120),
    title=dict(text="Mais cordas, mais perto da curva, nunca acima dela",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.96, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** cinco linhas num painel só, tempo de 0 a 1 ano (marcado em 3, 6 e 9 meses),
montante no y, rótulo direto na ponta de cada linha com o valor final. A comparação é de quem fica
abaixo de quem no mesmo eixo, e as linhas não se cruzam: saem juntas (a primeira corda é a mesma
reta em todas) e se separam nó a nó. Descartados: (1) *small multiples*, um painel por m, que
quebra justamente a comparação com a curva; (2) revelação progressiva (uma linha por vez), que o
texto já faz em prosa ("Com duas… Com quatro… Com doze…"), por isso o gráfico mostra o conjunto;
(3) barras com os valores finais, que perdem a forma da linha quebrada, a imagem da corda que o
texto retoma do post anterior; (4) incluir m = 52 e 365, que ficariam a menos de 0,03 da curva,
indistinguíveis dela nesta escala (a prosa dá os números).

**Anotação:** (1) a curva contínua, "nenhuma linha quebrada passa dela", apontando para e<sup>t</sup>
pouco depois de 6 meses; (2) o primeiro nó da linha de 2 cordas, em 6 meses: "o juro vira saldo e a
linha dobra para cima; a de 1 corda segue reta", que mostra o mecanismo; (3) o valor final de cada
linha no rótulo da ponta (2,00; 2,25; 2,44; 2,61; 2,718), que faz o papel da legenda.

**Gate de Tufte:**
- **Eixo y sem zero, por exceção justificada.** O eixo começa no capital (1), não em zero. A
  altura de cada linha acima da base é o juro acumulado, a grandeza que o texto compara (1 contra
  1,718), e o Lie Factor dessa grandeza é 1,0. Com zero, a metade de baixo do gráfico ficaria
  vazia sem informação, e as cordas de 12 e a curva (0,105 de distância) se colariam.
- Escala linear nos dois eixos. A ênfase da curva é de cor e espessura, não de grandeza.
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`.
- Cinco séries, acima do limiar de três: *small multiples* e revelação progressiva foram
  considerados e recusados (ver "Escolha de tipo"). As linhas não se cruzam, cada uma tem rótulo
  direto, e só uma tem cor.
- Acessibilidade (DESIGN.md §8, 1.4.1): as quatro linhas quebradas têm a mesma cor e se distinguem
  pelo rótulo na ponta e pela ordem vertical. A curva se distingue também pela espessura.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo e
contorno dos marcadores), `color.grove.500` (a curva e<sup>t</sup>, a série que é o ponto, e a sua
anotação), `color.neutral.slate` (as quatro linhas quebradas, eixos, rodapé), `color.neutral.ink`
(título, anotação do nó de 6 meses), `color.neutral.mist` (grid); `typography.fontFamily.display`
(título), `.body` (rótulos, anotações, rodapé), `.data` (eixos). Sem `lime`.

**Título no gráfico:** "Mais cordas, mais perto da curva, nunca acima dela"

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linhas com o montante de um capital de 1 aplicado a 100% ao ano, ao longo de um ano. Quatro
> linhas quebradas, feitas de 1, 2, 4 e 12 cordas, saem juntas de 1 e se separam a cada
> capitalização, quando o juro vira saldo e a linha dobra para cima. No fim do ano, terminam em
> 2; 2,25; 2,44 e 2,61. Por cima de todas, a curva contínua e elevado a t termina em 2,718. Cada
> linha quebrada fica abaixo da seguinte, e nenhuma passa da curva. Cálculo próprio.

**Legenda:**

> Capital de 1 aplicado a 100% ao ano, capitalizado 1, 2, 4 e 12 vezes. Dentro de cada subperíodo o juro
> corre em linha reta; a cada capitalização ele vira saldo e a linha dobra. Quanto mais cordas,
> mais perto da curva e<sup>t</sup>, que termina o ano em 2,718, sem nunca passar dela. Fonte:
> cálculo próprio.

**Placeholder:** o alt-text já em `04-draft-v2.md` (l. 83) bate com a figura e os números; não
precisa mudar.

## graf-02

**Onde entra:** "Rende todo dia não é render mais", no lugar do placeholder `graf-02`: depois de
"Volte aos 14% nominais e suba com eles a escada de Bernoulli." e antes de "Em R$ 1 milhão por um
ano, passar da capitalização anual para a mensal vale R$ 9.342,03."

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica real, a efetiva de 14%
nominais por frequência, com a assíntota e<sup>0,14</sup> − 1. Critério 1. Diagrama e infográfico
perdem pelo mesmo motivo do graf-01.

**Pergunta que o gráfico responde:** quanto a taxa efetiva de 14% nominais ao ano sobe a cada
aumento da frequência de capitalização, e quanto falta até o teto contínuo?

**Fonte dos dados:** cálculo próprio. Efetiva = (1 + 0,14/m)<sup>m</sup> − 1 para m = 1, 2, 4, 12,
52, 252, 365; teto = e<sup>0,14</sup> − 1 = 15,0274%. Efetivas: 14,0000%; 14,4900%; 14,7523%;
14,9342%; 15,0057%; 15,0229%; 15,0243%. Distâncias até o teto: 1,0274; 0,5374; 0,2751; 0,0932;
0,0216; 0,0045; 0,0031 p.p. (de 1 para 2 e de 2 para 4, a distância cai a 52% e 51%: "quase
exatamente pela metade", como diz o texto).

**Dados:** `posts/2026-11-09-frequencia-de-capitalizacao/graficos/dados/graf-02.csv`, 7 linhas.
Colunas: `m`, `efetiva_pct`, `distancia_teto_pp`, `teto_pct` (seis casas).

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

```python
import json
import math
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-11-09-frequencia-de-capitalizacao"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # a série que é o ponto (DESIGN.md §10)
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")


def num(v, casas):
    return f"{v:.{casas}f}".replace(".", ",")


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02.csv")).set_index("m")
teto = df["teto_pct"].iloc[0]
assert list(df.index) == [1, 2, 4, 12, 52, 252, 365] and num(teto, 2) == "15,03"

fig = go.Figure()
# O teto contínuo: referência tracejada.
fig.add_hline(y=teto, line=dict(color=ink, width=1.5, dash="dash"), layer="below")
fig.add_annotation(xref="paper", x=0, y=teto, xanchor="left", yanchor="bottom", yshift=4,
                   showarrow=False, align="left",
                   text=f"<b>teto contínuo: e<sup>0,14</sup> − 1 = {num(teto, 2)}%</b>",
                   font=dict(color=ink, size=14, family=font_body))
# A escada: a série que é o ponto.
fig.add_trace(go.Scatter(x=df.index, y=df["efetiva_pct"], mode="lines+markers",
                         line=dict(color=grove, width=3),
                         marker=dict(color=grove, size=10, line=dict(color=bg, width=1.5)),
                         showlegend=False, hoverinfo="skip"))

# Rótulo direto em cada degrau: nome, efetiva e quanto falta até o teto.
# (ax, ay, xanchor, yanchor) em pixels; posições conferidas no PNG para não haver sobreposição.
NOME = {1: "anual", 2: "semestral", 4: "trimestral", 12: "mensal", 52: "semanal"}
POS = {1: (24, 0, "left", "middle"), 2: (14, 34, "left", "top"), 4: (14, 34, "left", "top"),
       12: (14, 44, "left", "top"), 52: (14, 20, "left", "top")}
for m, (ax, ay, xa, ya) in POS.items():
    r = df.loc[m]
    fig.add_annotation(x=math.log10(m), y=r["efetiva_pct"], ax=ax, ay=ay, showarrow=True,
                       arrowhead=0, arrowwidth=1, arrowcolor=mist, standoff=6, xanchor=xa,
                       yanchor=ya, align="left",
                       text=f"<b>{NOME[m]}  {num(r['efetiva_pct'], 2)}%</b><br>"
                            f"falta {num(r['distancia_teto_pp'], 2)} p.p.",
                       font=dict(color=grove, size=14, family=font_body))
# 252 e 365 ficam a 44 px um do outro e empatam em 15,02%: um rótulo só, com duas guias.
d252, d365 = df.loc[252], df.loc[365]
assert num(d252["efetiva_pct"], 2) == num(d365["efetiva_pct"], 2) == "15,02"
assert max(d252["distancia_teto_pp"], d365["distancia_teto_pp"]) < 0.005
fig.add_annotation(x=math.log10(365), y=d365["efetiva_pct"], ax=0, ay=150, showarrow=True,
                   arrowhead=0, arrowwidth=1, arrowcolor=slate, standoff=6, xanchor="right",
                   yanchor="top", align="right",
                   text=f"<b>diária  {num(d365['efetiva_pct'], 2)}%</b><br>"
                        "252 ou 365 vezes: falta menos de 0,005 p.p.",
                   font=dict(color=grove, size=14, family=font_body))
# guia do 252 até o canto do mesmo rótulo: dx = log10(365/252) × (764 px / log10(520/0,8))
dx = round(math.log10(365 / 252) * 764 / math.log10(520 / 0.8))
fig.add_annotation(x=math.log10(252), y=d252["efetiva_pct"], ax=dx, ay=150, showarrow=True,
                   arrowhead=0, arrowwidth=1, arrowcolor=slate, standoff=6, text="")

fig.add_annotation(xref="paper", yref="paper", x=-0.085, y=0, yshift=-62, xanchor="left",
                   yanchor="top", showarrow=False, align="left",
                   text="Fonte: cálculo próprio. Taxa efetiva = (1 + 0,14/m)<sup>m</sup> − 1, "
                        "com m capitalizações por ano. Teto = e<sup>0,14</sup> − 1. O eixo "
                        "vertical<br>começa em 14%, a efetiva com uma capitalização no ano: "
                        "a altura de cada ponto é o que a frequência acrescenta.",
                   font=dict(color=slate, size=13, family=font_body))

fig.update_xaxes(type="log", range=[math.log10(0.8), math.log10(520)],
                 tickvals=list(df.index), ticktext=[str(m) for m in df.index],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 title=dict(text="capitalizações por ano, m (escala logarítmica)",
                            font=dict(color=slate, size=13, family=font_body)),
                 showgrid=False, zeroline=False, showline=False, ticks="")
# Eixo começa em 14%, não em zero: ver "Gate de Tufte" em graficos.md.
fig.update_yaxes(range=[13.9, 15.16], tickvals=[14, 14.25, 14.5, 14.75, 15],
                 ticktext=["14,00%", "14,25%", "14,50%", "14,75%", "15,00%"],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 title=dict(text="taxa efetiva ao ano", font=dict(color=slate, size=13,
                                                                 family=font_body)),
                 gridcolor=mist, gridwidth=1, zeroline=False, showline=False)
fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=640,
    margin=dict(l=96, r=40, t=84, b=140),
    title=dict(text="Cada degrau sobe menos que o anterior",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.96, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
```

**Escolha de tipo:** linha com marcadores, m em escala logarítmica no x (rótulos 1, 2, 4, 12, 52,
252, 365), efetiva no y, teto tracejado. Com m em escala linear, os quatro primeiros pontos se
amontoariam nos primeiros 3% do eixo; o log dá a cada dobra de frequência o mesmo espaço, que é a
unidade do argumento ("cada vez que se dobra a frequência…"). Cada ponto leva o nome da frequência,
a efetiva e quanto falta até o teto. Descartados: (1) eixo categórico com espaçamento igual, que
esconderia que de 12 para 52 e de 52 para 252 o salto em m é muito maior que de 1 para 2; (2)
barras, que pediriam zero no eixo e achatariam 14,00% a 15,02% numa mesma altura; (3) os ganhos em
R$ 1 milhão no gráfico, que a prosa dá logo em seguida.

**Anotação:** (1) o teto, com a fórmula e o valor (e<sup>0,14</sup> − 1 = 15,03%); (2) cada degrau
com a efetiva e a distância até o teto (1,03; 0,54; 0,28; 0,09; 0,02 p.p.), que mostra a distância
caindo pela metade a cada dobra; (3) 252 e 365 juntos, num rótulo só com duas guias: ficam a 44 px
um do outro e empatam em 15,02%, com menos de 0,005 p.p. até o teto. "Diária" cobre os dois, e o
252 é o que a prosa usa (ver a nota na seção "Dados").

**Gate de Tufte:**
- **Eixo y sem zero, por exceção justificada.** O eixo parte de 14%, a efetiva com uma
  capitalização no ano, que é o piso da série (a nominal). A grandeza que o gráfico mede é o que a
  frequência acrescenta aos 14%, e ela tem zero real em 14%; o Lie Factor dessa grandeza é 1,0. O
  rodapé diz isso por escrito. Com zero em 0%, os sete pontos ficariam numa faixa de 7% da altura
  e o degrau que encolhe, que é a pergunta, sumiria.
- Escala log no x, declarada no título do eixo.
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`.
- Uma série só, mais a referência do teto.
- Acessibilidade (DESIGN.md §8, 1.4.1): nada depende só da cor. O teto se distingue pelo traço
  tracejado e pelo rótulo.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo e
contorno dos marcadores), `color.grove.500` (a escada da efetiva e os rótulos dos degraus),
`color.neutral.ink` (título, teto e rótulo do teto), `color.neutral.slate` (guias do rótulo
"diária", eixos, rodapé), `color.neutral.mist` (grid, guias curtas dos rótulos);
`typography.fontFamily.display` (título), `.body` (rótulos, rodapé), `.data` (eixos). Sem `lime`.

**Título no gráfico:** "Cada degrau sobe menos que o anterior"

**Alt-text (para o placeholder `graf-02` em `post.md`):**

> Gráfico de linha com a taxa efetiva de 14% nominais ao ano conforme a frequência de
> capitalização, em escala logarítmica. Anual, 14,00%; semestral, 14,49%; trimestral, 14,75%;
> mensal, 14,93%; semanal, 15,01%; diária, 15,02%, tanto com 252 quanto com 365 capitalizações.
> Uma linha tracejada marca o teto contínuo de 15,03%. A distância até o teto cai quase pela
> metade a cada vez que a frequência dobra: 1,03, 0,54, 0,28 ponto percentual. Cálculo próprio.

**Legenda:**

> A mesma taxa nominal de 14% ao ano rende mais quanto mais vezes é capitalizada, mas cada degrau
> sobe menos que o anterior, e nenhum passa do teto contínuo de 15,03% (e<sup>0,14</sup> − 1). Da
> anual para a semestral, a efetiva ganha 0,49 ponto percentual; da diária para a contínua, menos
> de 0,005. Fonte: cálculo próprio.

**Placeholder:** o alt-text já em `04-draft-v2.md` (l. 155) bate com a figura e os números. Se a
etapa 9 quiser, o alt-text acima acrescenta trimestral, semanal e a queda da distância pela
metade; a mudança é opcional.
