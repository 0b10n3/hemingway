# Gráficos — "A barriga da curva"

Duas peças, decididas em `processo/02-estrutura.md` ("Onde entra graf-NN / diag-NN / info-NN" e
"Revisão pós-etapa 5") e posicionadas em `processo/04-draft-v2.md`. A linha contínua tracejada
saiu do graf-01 por decisão do autor (crítica M2, `processo/05-critica.md`; `estado.json`,
aprovações): ela desenhava o erro (a taxa cotada usada como instantânea) como se fosse um motor.
Os números conferem com `processo/07-verificacao.md` (seção 1 e "Para a etapa 8") e com
`_revisoes/2026-11-04_2026-11-02-a-barriga-da-curva_calculo.md`. O checklist de craft
(`.claude/agents/references/checklist-graficos.md`) foi aplicado. Os tokens de marca são lidos em
runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do
repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa (plotly + kaleido).

Não há `diag-NN` nem `info-NN`: cada peça carrega uma ideia só (`02-estrutura.md`).

## Dados

Os CSVs saem do cálculo, não são digitados. O bloco abaixo regenera `graficos/dados/graf-01.csv`,
`graficos/dados/graf-02.csv` e `graficos/dados/graf-02-viradas.csv` e confere o resultado contra
os números do texto e da etapa 7. Se a fórmula ou um parâmetro mudar, um `assert` falha. Só
biblioteca padrão.

```python
import csv
import math
import os

POST_DIR = "posts/2026-11-02-a-barriga-da-curva"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)
C = 1000.0


def gravar(nome, linhas):
    with open(os.path.join(out, nome), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0]))
        w.writeheader()
        w.writerows(linhas)


# graf-01 — R$ 1.000 a 14% a.a., t de 0 a 2 anos em passos de 0,01 ano (inclui 0,5 e 1 exatos).
i = 0.14
g1 = []
for k in range(201):
    t = k / 100
    simples, composto = C * (1 + i * t), C * (1 + i) ** t
    g1.append({"t_anos": f"{t:.2f}", "simples": f"{simples:.4f}", "composto": f"{composto:.4f}",
               "simples_menos_composto": f"{simples - composto:.4f}"})
gravar("graf-01.csv", g1)

# Máximo exato da distância: d/dt [C(1+it) − C(1+i)^t] = 0  →  (1+i)^t = i / ln(1+i).
L = math.log(1 + i)
t_max = math.log(i / L) / L
gap = lambda t: C * (1 + i * t) - C * (1 + i) ** t
meio = {r["t_anos"]: r for r in g1}["0.50"]
# confere com processo/07-verificacao.md (seção 1) e _revisoes/..._calculo.md
assert f"{t_max:.4f}" == "0.5055" and f"{gap(t_max):.4f}" == "2.2924"
assert (f"{float(meio['simples']):.2f}", f"{float(meio['composto']):.2f}") == ("1070.00", "1067.71")
assert f"{gap(0.5):.4f}" == "2.2922"
assert f"{gap(0.5) / (C * 1.14 ** 0.5) * 100:.3f}" == "0.215"     # % do montante
assert f"{C * (1 + i):.2f}" == "1140.00" and abs(gap(1)) < 1e-9
assert f"{gap(2):.2f}" == "-19.60"                                # = juro sobre juro em 2 anos
assert all(float(r["simples_menos_composto"]) > 0 for r in g1 if 0 < float(r["t_anos"]) < 1)
assert all(float(r["simples_menos_composto"]) < 0 for r in g1 if float(r["t_anos"]) > 1)

# graf-02 — parcela do juro sobre juro no juro total, R$ 1.000 a 6%, 10% e 14% a.a., 1 a 30 anos.
# juro total = C[(1+i)^t − 1]; juro linear = C·i·t; juro sobre juro = total − linear.
TAXAS = (0.06, 0.10, 0.14)


def parcela(r, t):
    total = (1 + r) ** t - 1
    return (total - r * t) / total


g2 = [{"prazo_anos": t, **{f"taxa_{round(r * 100)}": f"{parcela(r, t) * 100:.4f}" for r in TAXAS}}
      for t in range(1, 31)]
gravar("graf-02.csv", g2)


def virada(r):
    # prazo contínuo em que juro sobre juro = juro linear, i.e. (1+r)^t = 1 + 2rt (parcela = 50%)
    lo, hi = 1.0, 60.0
    for _ in range(100):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if parcela(r, mid) < 0.5 else (lo, mid)
    return lo


vir = [{"taxa_pct": round(r * 100), "virada_anos": f"{virada(r):.4f}",
        "primeiro_ano_inteiro_acima_50": next(t for t in range(1, 61) if parcela(r, t) > 0.5)}
       for r in TAXAS]
gravar("graf-02-viradas.csv", vir)

# confere com processo/07-verificacao.md (seção 1 e "Para a etapa 8"). A 6%, a virada é
# 22,3946 anos: 22,39 com duas casas (a etapa 7 imprimiu 22,395, que arredondado de novo dá 22,40).
assert [f"{float(v['virada_anos']):.2f}" for v in vir] == ["22.39", "14.02", "10.42"]
assert [v["primeiro_ano_inteiro_acima_50"] for v in vir] == [23, 15, 11]
assert [f"{parcela(r, 10) * 100:.1f}" for r in TAXAS] == ["24.1", "37.3", "48.3"]
assert g2[0]["taxa_14"] == "0.0000"                               # em 1 ano, não há juro sobre juro
assert f"{C * (1.14 ** 2 - 1):.2f}" == "299.60" and f"{C * 0.14 * 2:.2f}" == "280.00"
print("ok", t_max, gap(t_max), [v["virada_anos"] for v in vir], [g2[-1][k] for k in g2[-1]])
```

## graf-01

**Onde entra:** "A barriga da curva", no lugar do marcador `> [graf-01]`: depois de "Quem fez
cálculo reconhece a desigualdade de Bernoulli…; quem não fez pode confiar no desenho." e antes de
"O espaço entre a corda e a curva, abaixo de um período, é a barriga deste texto."

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica (montante em R$ por prazo),
critério 1. diag perde porque tiraria os números (R$ 1.070,00 × R$ 1.067,71, R$ 1.140,00), que
são o argumento. info perde porque é uma ideia só.

**Pergunta que o gráfico responde:** com o mesmo 14% ao ano, de que lado fica o juro simples em
relação ao composto, antes e depois de um ano?

**Fonte dos dados:** cálculo próprio. R$ 1.000 a 14% ao ano; simples = 1.000 × (1 + 0,14 t),
composto = 1.000 × 1,14^t, t em anos, de 0 a 2 em passos de 0,01. Recálculo da etapa 7
(`07-verificacao.md`, seção 1, l. 109–113): máximo da distância em t = 0,5055 ano
(R$ 2,2924); em t = 0,5, R$ 1.070,00 × R$ 1.067,71 (R$ 2,2922, 0,215% do montante); encontro
em t = 1, R$ 1.140,00.

**Dados:** `posts/2026-11-02-a-barriga-da-curva/graficos/dados/graf-01.csv`, 201 linhas (t = 0,00
a 2,00). Colunas: `t_anos`, `simples`, `composto`, `simples_menos_composto` (R$, quatro casas).

**Decisão de escala: dois painéis, não eixo recortado.** A distância máxima entre a reta e a
curva é R$ 2,29 num montante de R$ 1.068, ou 0,215%. Em escala natural, ela ocupa menos de um
pixel. Há duas saídas:

- **Eixo y recortado** (por exemplo, R$ 1.060 a R$ 1.075 em volta dos seis meses): mostra a
  barriga, mas perde o resto do argumento. Ou a janela de tempo encolhe e o encontro em um ano e
  a ultrapassagem depois saem do quadro, ou a escala volta a esmagar a barriga. E o aviso de
  recorte é texto que o leitor pode não ler: a figura sozinha diria que a diferença é grande.
- **Painel inferior com a diferença simples − composto em R$** (escolhido): o painel de cima
  fica em escala natural e diz a verdade sobre o tamanho (as duas linhas quase se confundem
  antes de um ano). O painel de baixo amplia só a diferença, numa grandeza com zero real, e
  mostra as três coisas que o texto diz: positiva até um ano (a barriga, até R$ 2,29), zero em
  um ano, negativa depois (−R$ 19,60 em dois anos). O título do painel de baixo avisa que a
  escala é ampliada. Bônus: os R$ 19,60 de dois anos são, por identidade, o juro sobre juro da
  seção seguinte (R$ 299,60 − R$ 280,00), que o graf-02 retoma.

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

POST_DIR = "posts/2026-11-02-a-barriga-da-curva"
TOKENS_PATH = "../../brand/tokens/syntaxis.tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)
c = tokens["color"]
bg = c["neutral"]["chalk"]["$value"]
ink = c["neutral"]["ink"]["$value"]
slate = c["neutral"]["slate"]["$value"]
mist = c["neutral"]["mist"]["$value"]
grove = c["grove"]["500"]["$value"]       # a série que é o ponto (DESIGN.md §10)
grove_fill = c["grove"]["100"]["$value"]  # preenchimento da barriga, degrau de tom da mesma rampa
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")


def brl(v):
    # 1070.0 -> "1.070,00"
    return f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# "R&#36;", não "R$": dois "$" no mesmo texto viram LaTeX no Plotly.
RS = "R&#36;"


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))
row = df.set_index(df["t_anos"].round(2))
meio, um, dois = row.loc[0.5], row.loc[1.0], row.loc[2.0]
barriga = df[df["t_anos"] <= 1]
depois = df[df["t_anos"] >= 1]
pct_meio = meio["simples_menos_composto"] / meio["composto"] * 100
assert (brl(meio["simples"]), brl(meio["composto"]), brl(um["simples"])) == \
       ("1.070,00", "1.067,71", "1.140,00")

fig = make_subplots(rows=2, cols=1, shared_xaxes=True, row_heights=[0.56, 0.44],
                    vertical_spacing=0.13)

# --- Painel de cima: montante em escala natural (a distância some) ---
fig.add_trace(go.Scatter(x=df["t_anos"], y=df["composto"], mode="lines",
                         line=dict(color=slate, width=2.5), showlegend=False,
                         hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=df["t_anos"], y=df["simples"], mode="lines",
                         line=dict(color=grove, width=2.5), showlegend=False,
                         hoverinfo="skip"), row=1, col=1)
fig.add_trace(go.Scatter(x=[0.5, 0.5, 1.0], y=[meio["simples"], meio["composto"], um["simples"]],
                         mode="markers", marker=dict(color=ink, size=8), showlegend=False,
                         hoverinfo="skip"), row=1, col=1)
# Rótulo direto na ponta de cada linha, no lugar de legenda.
fig.add_annotation(x=2, y=dois["composto"], xanchor="left", xshift=8, yshift=16, showarrow=False,
                   align="left", text=f"<b>composto</b><br>{RS} {brl(dois['composto'])}",
                   font=dict(color=slate, size=14, family=font_body), row=1, col=1)
fig.add_annotation(x=2, y=dois["simples"], xanchor="left", xshift=8, yshift=-22,
                   showarrow=False, align="left",
                   text=f"<b>simples</b><br>{RS} {brl(dois['simples'])}",
                   font=dict(color=grove, size=14, family=font_body), row=1, col=1)
fig.add_annotation(x=0.5, y=meio["simples"], ax=-20, ay=-62, showarrow=True, arrowhead=0,
                   arrowwidth=1, arrowcolor=ink, xanchor="right", align="right",
                   text=f"<b>6 meses</b><br>simples {RS} {brl(meio['simples'])}"
                        f"<br>composto {RS} {brl(meio['composto'])}",
                   font=dict(color=ink, size=14, family=font_body), row=1, col=1)
fig.add_annotation(x=1.0, y=um["simples"], ax=40, ay=58, showarrow=True, arrowhead=0,
                   arrowwidth=1, arrowcolor=ink, xanchor="left", align="left",
                   text=f"<b>1 ano</b><br>as duas valem {RS} {brl(um['simples'])}",
                   font=dict(color=ink, size=14, family=font_body), row=1, col=1)

# --- Painel de baixo: a diferença simples − composto, em escala ampliada ---
fig.add_trace(go.Scatter(x=barriga["t_anos"], y=barriga["simples_menos_composto"], mode="lines",
                         line=dict(color=grove, width=2.5, simplify=False), fill="tozeroy",
                         fillcolor=grove_fill, showlegend=False, hoverinfo="skip"), row=2, col=1)
fig.add_trace(go.Scatter(x=depois["t_anos"], y=depois["simples_menos_composto"], mode="lines",
                         line=dict(color=slate, width=2.5, simplify=False), fill="tozeroy", fillcolor=mist,
                         showlegend=False, hoverinfo="skip"), row=2, col=1)
fig.add_hline(y=0, line=dict(color=ink, width=1.5), row=2, col=1)
fig.add_trace(go.Scatter(x=[0.5, 1.0, 2.0],
                         y=[meio["simples_menos_composto"], 0, dois["simples_menos_composto"]],
                         mode="markers", marker=dict(color=ink, size=8), showlegend=False,
                         hoverinfo="skip"), row=2, col=1)
fig.add_annotation(x=0.5, y=meio["simples_menos_composto"], ax=70, ay=-26, showarrow=True,
                   arrowhead=0, arrowwidth=1, arrowcolor=grove, xanchor="left", align="left",
                   text=f"<b>a barriga: o simples paga até {RS} {brl(meio['simples_menos_composto'])}"
                        f" a mais</b><br>({brl(pct_meio)}% do montante, perto de 6 meses)",
                   font=dict(color=grove, size=14, family=font_body), row=2, col=1)
fig.add_annotation(x=2.0, y=dois["simples_menos_composto"], ax=-24, ay=-6, showarrow=True,
                   arrowhead=0, arrowwidth=1, arrowcolor=slate, xanchor="right", align="right",
                   text=f"<b>2 anos: o composto paga {RS} {brl(-dois['simples_menos_composto'])}"
                        " a mais</b>",
                   font=dict(color=slate, size=14, family=font_body), row=2, col=1)

# Guia vertical em 1 ano, atravessando os dois painéis.
for r in (1, 2):
    fig.add_vline(x=1, line=dict(color=mist, width=1.5, dash="dot"), layer="below", row=r, col=1)

# Título de cada painel (o aviso de escala mora no do painel de baixo).
for y, txt in ((1.0, f"Montante de {RS} 1.000 a 14% ao ano, em {RS}"),
               (0.44 - 0.13 / 2 + 0.065, f"Diferença simples − composto, em {RS} "
                                          "<b>(escala ampliada: no painel de cima ela não "
                                          "aparece)</b>")):
    fig.add_annotation(xref="paper", yref="paper", x=0, y=y, yanchor="bottom", xanchor="left",
                       showarrow=False, align="left", text=txt, yshift=6,
                       font=dict(color=slate, size=14, family=font_body))

fig.add_annotation(xref="paper", yref="paper", x=-0.085, y=0, yshift=-46, xanchor="left",
                   yanchor="top", showarrow=False, align="left",
                   text="Fonte: cálculo próprio. Simples: 1.000 × (1 + 0,14 t); composto: "
                        "1.000 × 1,14<sup>t</sup>, com t em anos.",
                   font=dict(color=slate, size=13, family=font_body))

tick_t = [0, 0.5, 1, 1.5, 2]
tick_txt = ["0", "6 meses", "1 ano", "18 meses", "2 anos"]
fig.update_xaxes(range=[-0.03, 2.03], tickvals=tick_t, ticktext=tick_txt, showgrid=False,
                 zeroline=False, showline=False, ticks="",
                 tickfont=dict(color=slate, size=14, family=font_data))
fig.update_xaxes(showticklabels=False, row=1, col=1)  # o eixo de tempo fica só embaixo
# Painel de cima começa no capital, não em zero: ver "Gate de Tufte" em graficos.md.
fig.update_yaxes(range=[990, 1310], tickvals=[1000, 1100, 1200, 1300],
                 ticktext=["1.000", "1.100", "1.200", "1.300"], row=1, col=1)
fig.update_yaxes(range=[-22, 5], tickvals=[-20, -15, -10, -5, 0],
                 ticktext=["−20", "−15", "−10", "−5", "0"], row=2, col=1)
fig.update_yaxes(gridcolor=mist, gridwidth=1, zeroline=False, showline=False,
                 tickfont=dict(color=slate, size=14, family=font_data))

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=720,
    margin=dict(l=76, r=128, t=104, b=92),
    title=dict(text="Antes de um ano, o juro simples rende mais que o composto",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.965, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** linhas em dois painéis com o eixo de tempo compartilhado (marcado em "6
meses", "1 ano", "18 meses", "2 anos", que é como o texto fala do prazo). Em cima, o montante dos
dois motores com rótulo direto na ponta de cada linha. Embaixo, a diferença simples − composto,
com a área positiva (a barriga) em `grove.100` sob a linha `grove.500` e a área negativa em
`mist` sob a linha `slate`. Uma guia pontilhada em um ano atravessa os dois painéis. Descartados:
(1) eixo y recortado (ver "Decisão de escala"); (2) só o painel da diferença, que esconde do
leitor que a diferença é pequena perto do montante, e esse tamanho também é informação (é por
isso que ninguém a vê na tela do banco); (3) eixo y logarítmico, que não ajuda, porque a
distância é pequena em qualquer escala do montante; (4) a linha contínua tracejada (cortada pelo
autor, M2).

**Anotação:** (1) em cima, seis meses, com os dois montantes do texto (R$ 1.070,00 simples ×
R$ 1.067,71 composto) e dois marcadores quase sobrepostos, sobreposição que é o próprio
argumento de escala; (2) em cima, um ano: "as duas valem R$ 1.140,00"; (3) embaixo, o pico da
barriga: "o simples paga até R$ 2,29 a mais (0,21% do montante, perto de 6 meses)"; (4)
embaixo, dois anos: "o composto paga R$ 19,60 a mais". O marcador do pico fica em t = 0,5 (o
ponto que o texto usa); o máximo exato, em t = 0,5055, vale R$ 2,2924, e as duas coisas
arredondam para R$ 2,29, por isso a anotação diz "perto de 6 meses". Os rótulos "composto
R$ 1.299,60" e "simples R$ 1.280,00" na ponta direita fazem o papel da legenda.

**Gate de Tufte:**
- **Painel de cima sem zero, por exceção justificada.** O eixo começa no capital (R$ 1.000),
  não em zero. A exceção não exagera nada: mesmo com o eixo a partir do capital, a distância
  entre as linhas continua abaixo de 1% da altura do painel, e o painel existe justamente para
  mostrar que ela é pequena. Com zero, a curvatura do composto também sumiria, e o desenho da
  corda sobre a curva ficaria ilegível.
- **Painel de baixo com zero real** (linha `ink` em zero, as duas áreas partem dela). A escala
  é linear e o Lie Factor é 1,0 dentro do painel. Os dois painéis têm escalas diferentes, e isso
  está escrito no título do painel de baixo: "escala ampliada: no painel de cima ela não
  aparece".
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`.
- Duas séries de montante e uma de diferença: abaixo do limiar de três séries competindo.
- Acessibilidade (DESIGN.md §8, 1.4.1): simples e composto se distinguem por rótulo direto na
  ponta de cada linha, não só pela cor. O lado da barriga é dado pelo sinal (acima ou abaixo do
  zero) e pelas anotações, não só pelo tom do preenchimento.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo),
`color.grove.500` (juro simples, a série que é o ponto, e a barriga com a anotação do pico),
`color.grove.100` (preenchimento da barriga, degrau de tom da mesma rampa), `color.neutral.slate`
(juro composto, a diferença depois de um ano, eixos, títulos dos painéis, rodapé),
`color.neutral.mist` (grid, área depois de um ano, guia de um ano), `color.neutral.ink` (título,
marcadores, zero, anotações de seis meses e de um ano); `typography.fontFamily.display` (título),
`.body` (anotações, rótulos, rodapé), `.data` (eixos). Sem `lime`: a barriga não é conquista.
Ênfase no simples e não no composto porque a pergunta é sobre o lado do simples: o padrão de
mercado é o composto (contexto), e a surpresa é a reta por cima dele.

**Título no gráfico:** "Antes de um ano, o juro simples rende mais que o composto"

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Gráfico em dois painéis com R$ 1.000 a 14% ao ano, de zero a dois anos. No painel de cima, o
> montante em reais: a reta do juro simples e a curva do juro composto saem juntas de R$ 1.000,
> quase se confundem até um ano e se encontram em R$ 1.140,00. Em seis meses, o simples vale
> R$ 1.070,00 e o composto R$ 1.067,71. Depois de um ano, a curva passa por cima da reta e
> termina em R$ 1.299,60, contra R$ 1.280,00 do simples. O painel de baixo amplia a diferença
> simples menos composto: positiva entre zero e um ano, com pico de R$ 2,29 perto de seis meses
> (0,21% do montante), zero em um ano e negativa depois, até menos R$ 19,60 em dois anos.
> Cálculo próprio.

**Legenda:**

> Com o mesmo 14% ao ano, a reta do juro simples passa por cima da curva do composto entre zero
> e um ano, com a maior distância perto de seis meses (R$ 1.070,00 contra R$ 1.067,71). As duas
> se encontram em R$ 1.140,00 em um ano, e daí em diante o composto passa à frente. A diferença
> é tão pequena perto do montante que o painel de baixo a mostra em escala ampliada. Fonte:
> cálculo próprio.

**Placeholder sugerido para `post.md` (etapa 9):**

```markdown
![Gráfico: R$ 1.000 a 14% ao ano, de zero a dois anos, nos dois motores. Entre zero e um ano, a reta do juro simples fica acima da curva do composto, com a maior distância perto de seis meses (R$ 1.070,00 contra R$ 1.067,71, uma diferença de R$ 2,29). As duas se encontram em um ano, em R$ 1.140,00, e a curva passa por cima da reta dali em diante: em dois anos, o composto paga R$ 19,60 a mais.](graf-01)
```

## graf-02

**Onde entra:** "A bola de neve demora a rolar", no lugar do marcador `> [graf-02]`: depois de
"Em dois anos a 14% ao ano, R$ 1.000 rendem R$ 299,60. Desses, R$ 280,00 são juro linear. O juro
sobre juro responde por R$ 19,60." e antes de "A virada, o prazo em que o juro sobre juro passa a
valer mais que o juro linear, chega depois de uma década a 14% ao ano." (ou "O cruzamento…", se a
etapa 9 aplicar o opcional 33 de `06-revisao.md`).

**Por que é graf (raciocínio de `02-estrutura.md`):** série numérica por prazo, critério 1. A
virada é o argumento e cai no cruzamento com 50%. A alternativa de barras empilhadas (capital +
juro linear + juro sobre juro a 14%) perdeu porque mostra uma taxa só e esconde a comparação 6% ×
14%. O conteúdo do "embedded content" do rascunho não veio no arquivo; a peça foi reconstruída
pela fórmula do texto.

**Pergunta que o gráfico responde:** em quantos anos o juro sobre juro passa a valer mais que o
juro linear, a 6%, 10% e 14% ao ano?

**Fonte dos dados:** cálculo próprio. R$ 1.000 a juros compostos; juro total = 1.000 × [(1 + i)^t
− 1]; juro linear = 1.000 × i t; juro sobre juro = 1.000 × [(1 + i)^t − 1 − i t] (a fórmula do
bloco de equação do texto); parcela = juro sobre juro ÷ juro total. A virada é a solução de
(1 + i)^t = 1 + 2 i t, por bisseção. Recálculo da etapa 7 (`07-verificacao.md`, seção 1, l. 137,
e "Para a etapa 8"): 14% → 10,42 anos, 10% → 14,02, 6% → 22,39 (ver "Divergência" abaixo);
em anos inteiros, 11º, 15º e 23º ano; parcela em 10 anos, 48,3% / 37,3% / 24,1%.

**Divergência numérica:** a virada a 6% é **22,3946 anos**, ou seja **22,39** com duas casas. O
"22,40" do pedido da etapa 8 e o "22,40" da tabela da seção 1 de `07-verificacao.md` vêm de
arredondar duas vezes (o registro de cálculo imprime 22,395, que arredondado de novo dá 22,40). O
texto do post não é afetado ("mais de duas" décadas). A figura usa 22,39.

**Dados:** `posts/2026-11-02-a-barriga-da-curva/graficos/dados/graf-02.csv`, 30 linhas (prazo de
1 a 30 anos), colunas `prazo_anos`, `taxa_6`, `taxa_10`, `taxa_14` (parcela do juro sobre juro no
juro total, em %, quatro casas); `graficos/dados/graf-02-viradas.csv`, 3 linhas, colunas
`taxa_pct`, `virada_anos` (prazo contínuo, quatro casas) e `primeiro_ano_inteiro_acima_50`.

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

```python
import json
import os

import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-11-02-a-barriga-da-curva"
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


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02.csv"))
vir = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02-viradas.csv")).set_index("taxa_pct")
assert list(vir.index) == [6, 10, 14]

# 14% é a taxa do post inteiro (abertura, graf-01): ênfase. 10% e 6% são contexto.
ESTILO = {14: (grove, 3.0), 10: (slate, 2.0), 6: (slate, 2.0)}

fig = go.Figure()
fig.add_hline(y=50, line=dict(color=ink, width=1.5, dash="dash"), layer="below")
fig.add_annotation(xref="paper", x=1, y=50, xanchor="right", yanchor="top", yshift=-4,
                   showarrow=False, align="right",
                   text="<b>50%: juro sobre juro<br>= juro linear</b>",
                   font=dict(color=ink, size=14, family=font_body))

for taxa in (6, 10, 14):
    cor, larg = ESTILO[taxa]
    col = f"taxa_{taxa}"
    fig.add_trace(go.Scatter(x=df["prazo_anos"], y=df[col], mode="lines",
                             line=dict(color=cor, width=larg), showlegend=False,
                             hoverinfo="skip"))
    # rótulo direto na ponta da linha, no lugar de legenda
    fim = df.iloc[-1]
    fig.add_annotation(x=fim["prazo_anos"], y=fim[col], xanchor="left", xshift=8,
                       showarrow=False, align="left",
                       text=f"<b>{taxa}% a.a.</b>  {num(fim[col], 0)}%",
                       font=dict(color=cor, size=15, family=font_body))
    # a virada: onde a linha cruza 50%
    t = vir.loc[taxa, "virada_anos"]
    fig.add_trace(go.Scatter(x=[t], y=[50], mode="markers", showlegend=False, hoverinfo="skip",
                             marker=dict(color=cor, size=11, line=dict(color=bg, width=1.5))))
    fig.add_annotation(x=t, y=50, ax=0, ay=-112 if taxa == 14 else 150, showarrow=True,
                       arrowhead=0, arrowwidth=1, arrowcolor=cor, standoff=6,
                       yanchor="bottom" if taxa == 14 else "top", align="center",
                       text=f"<b>{taxa}%: {num(t, 2)} anos</b>",
                       font=dict(color=cor, size=15, family=font_data))

# O ponto do texto: em 2 anos a 14%, R$ 19,60 de R$ 299,60 (6,5%).
dois = df[df["prazo_anos"] == 2].iloc[0]
fig.add_trace(go.Scatter(x=[2], y=[dois["taxa_14"]], mode="markers", showlegend=False,
                         hoverinfo="skip", marker=dict(color=grove, size=9)))
fig.add_annotation(x=2, y=dois["taxa_14"], ax=-4, ay=-200, showarrow=True, arrowhead=0,
                   arrowwidth=1, arrowcolor=grove, xanchor="left", yanchor="bottom", align="left",
                   text=f"<b>2 anos a 14%:</b><br><b>{num(dois['taxa_14'], 1)}% do juro</b><br>"
                        "(R&#36; 19,60 de R&#36; 299,60)",
                   font=dict(color=grove, size=14, family=font_body))

fig.add_annotation(
    xref="paper", yref="paper", x=-0.075, y=0, yshift=-50, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Fonte: cálculo próprio. R&#36; 1.000 a juros compostos. Juro sobre juro = "
         "1.000 × [(1 + i)<sup>t</sup> − 1 − i t]; juro linear = 1.000 × i t.<br>"
         "Parcela = juro sobre juro ÷ juro total. Viradas em prazo contínuo; em anos inteiros, "
         "o juro sobre juro passa à frente<br>no 11º ano a 14%, no 15º a 10% e no 23º a 6%.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_xaxes(range=[0.5, 30.5], tickvals=[1, 5, 10, 15, 20, 25, 30],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 title=dict(text="prazo, em anos", font=dict(color=slate, size=13,
                                                              family=font_body)),
                 showgrid=False, zeroline=False, showline=False, ticks="")
fig.update_yaxes(range=[0, 100], tickvals=[0, 25, 50, 75, 100],
                 ticktext=["0%", "25%", "50%", "75%", "100%"],
                 tickfont=dict(color=slate, size=14, family=font_data),
                 title=dict(text="parcela do juro sobre juro no juro total",
                            font=dict(color=slate, size=13, family=font_body)),
                 gridcolor=mist, gridwidth=1, zeroline=False, showline=False)
fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=640,
    margin=dict(l=76, r=150, t=96, b=146),
    title=dict(text="O juro sobre juro leva mais de uma década para passar à frente",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.96, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
```

**Escolha de tipo:** três linhas num painel só, prazo de 1 a 30 anos no eixo x, parcela de 0% a
100% no y, com a referência tracejada em 50% e um marcador em cada cruzamento. O argumento é a
comparação de quando cada taxa cruza a mesma linha. As três linhas não se cruzam entre si (a
parcela cresce com a taxa em qualquer prazo), e cada uma tem rótulo direto na ponta, por isso
três séries não chegam a brigar. Descartados: (1) barras empilhadas a 14% (ver acima); (2)
*small multiples*, um painel por taxa, que quebram exatamente a comparação de prazos no mesmo
eixo; (3) o montante em R$ no eixo y, em que a parcela teria que ser lida de cabeça; (4) eixo x
em escala log, que distorce a leitura de "uma década" e "duas décadas".

**Anotação:** (1) as três viradas, cada uma com marcador sobre a linha de 50% e o prazo
contínuo ("14%: 10,42 anos", "10%: 14,02 anos", "6%: 22,39 anos"); (2) a referência em 50% com
o nome do que ela marca ("juro sobre juro = juro linear"); (3) o ponto de dois anos a 14%, que
liga a figura à frase anterior do texto: 6,5% do juro, R$ 19,60 de R$ 299,60; (4) o valor de cada
linha em 30 anos na própria etiqueta da ponta (92%, 82%, 62%). Os anos inteiros (11º, 15º, 23º)
ficam no rodapé.

**Gate de Tufte:**
- Eixo y de 0% a 100%, com zero: a grandeza é uma parcela, e o topo do eixo é o juro total
  inteiro. Sem exceção a justificar.
- Lie Factor 1,0: escala linear nos dois eixos, e a ênfase do 14% é de cor e espessura de linha,
  não de grandeza.
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`, a cada 25%.
- Três séries: no limiar do checklist. Revelação progressiva e *small multiples* foram
  considerados e recusados (ver "Escolha de tipo"): as linhas não se cruzam, têm rótulo direto,
  e a comparação no mesmo eixo é a pergunta.
- Acessibilidade (DESIGN.md §8, 1.4.1): 10% e 6% têm a mesma cor e se distinguem pelo rótulo na
  ponta e pela posição (a de 10% fica sempre acima da de 6%). Nenhuma leitura depende só da cor.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo e
contorno dos marcadores), `color.grove.500` (14%, a taxa do post inteiro, com sua virada e a
anotação de dois anos), `color.neutral.slate` (10% e 6%, eixos, rodapé), `color.neutral.ink`
(título, linha de 50% e o rótulo dela), `color.neutral.mist` (grid);
`typography.fontFamily.display` (título), `.body` (rótulos, anotações, rodapé), `.data` (eixos e
os prazos das viradas). Sem `lime`.

**Título no gráfico:** "O juro sobre juro leva mais de uma década para passar à frente"

**Alt-text (para o placeholder `graf-02` em `post.md`):**

> Gráfico de linhas com a parcela do juro sobre juro no juro total de R$ 1.000 aplicados a
> juros compostos de 6%, 10% e 14% ao ano, em prazos de 1 a 30 anos. As três linhas começam em
> zero no primeiro ano e sobem devagar. Em dois anos a 14%, o juro sobre juro é 6,5% do juro
> total: R$ 19,60 de R$ 299,60. Uma linha tracejada em 50% marca o prazo em que o juro sobre
> juro passa a valer o mesmo que o juro linear. A 14%, isso acontece em 10,42 anos; a 10%, em
> 14,02; a 6%, em 22,39. Em 30 anos, o juro sobre juro é 92% do juro total a 14%, 82% a 10% e
> 62% a 6%. Cálculo próprio.

**Legenda:**

> Quanto do juro total é juro sobre juro, para R$ 1.000 a 6%, 10% e 14% ao ano. Ele só passa a
> valer mais que o juro linear depois de 10,42 anos a 14%, 14,02 a 10% e 22,39 a 6%. Em dois
> anos a 14%, são R$ 19,60 de R$ 299,60. Fonte: cálculo próprio.

**Placeholder sugerido para `post.md` (etapa 9):**

```markdown
![Gráfico: parcela do juro sobre juro no juro total de R$ 1.000 aplicados a juros compostos de 6%, 10% e 14% ao ano, em prazos de 1 a 30 anos. Em dois anos a 14%, é 6,5% do juro (R$ 19,60 de R$ 299,60). O juro sobre juro só passa a valer mais que o juro linear depois de 10,42 anos a 14%, 14,02 anos a 10% e 22,39 anos a 6%.](graf-02)
```
