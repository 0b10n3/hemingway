# Gráficos — "Samurais e duelos no mercado financeiro"

Uma peça. Foi decidida em `processo/02-estrutura.md` ("Visuais: onde e por quê") e posicionada
em `processo/04-draft-v2.md` (Anel da Água). A forma da segunda linha é decisão do autor, na
nota "Para a etapa 8" do draft v2. A frase de ancoragem segue o texto depois da etapa 6
(`processo/06-revisao.md`, l. 136). O checklist de craft
(`.claude/agents/references/checklist-graficos.md`) foi aplicado. Os tokens de marca são lidos
em runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco roda a partir da raiz do
repositório (`pipelines/hemingway/`) e foi testado com `python3` nesta etapa.

Os diagramas do post (linha do tempo e tabela-síntese) estão em `diagramas.md`. Não há
`info-NN`: cada peça carrega a própria ideia (`02-estrutura.md`).

## Dados

O CSV sai da fórmula, não é digitado. O bloco abaixo regenera `graficos/dados/graf-01.csv` e
confere o resultado contra `processo/07-verificacao.md` ("Contas": 1,01³⁶⁵ = 37,7834). Se a
fórmula ou os parâmetros do cenário quebrarem, o `assert` falha.

```python
import csv
import math
import os

POST_DIR = "posts/2026-10-27-samurais-e-duelos"
out = os.path.join(POST_DIR, "graficos/dados")
os.makedirs(out, exist_ok=True)

# Linha 1 — a conta do texto: 1% ao dia, composto, dias corridos 0 a 365.
# Linha 2 — cenário ilustrativo (decisão do autor, processo/04-draft-v2.md, "Para a etapa 8"):
# a mesma curva vezes um fator de marcação m(t). m = 1 fora do semestre contra; dentro dele,
# m cai e volta a 1 de forma suave (sen², derivada zero nas duas pontas). m(365) = 1: como a
# marcação a mercado de um título que converge para a curva no vencimento. Determinístico.
TAXA = 0.01
SEM_INICIO, SEM_DIAS = 183, 182   # segundo semestre: dias 183 a 365
PROF = 0.6                        # no fundo (dia 274), m = 0,4: o valor marcado é 40% da curva

rows = []
for t in range(366):
    curva = (1 + TAXA) ** t
    if SEM_INICIO <= t <= SEM_INICIO + SEM_DIAS:
        m = 1 - PROF * math.sin(math.pi * (t - SEM_INICIO) / SEM_DIAS) ** 2
    else:
        m = 1.0
    rows.append({"dia": t, "curva": round(curva, 6), "m": round(m, 6),
                 "com_semestre_contra": round(curva * m, 6)})

# confere com processo/07-verificacao.md ("Contas": 1.01**365 = 37,7834)
fim = rows[-1]
assert f"{fim['curva']:.4f}" == "37.7834", fim
# mesma chegada: no dia 365 a marcação voltou à curva
assert fim["m"] == 1.0 and fim["com_semestre_contra"] == fim["curva"], fim
# o fundo do semestre fica no dia 274, com m = 0,4
fundo = min(rows, key=lambda r: r["m"])
assert fundo["dia"] == 274 and abs(fundo["m"] - 0.4) < 1e-6, fundo
# "em queda" (gloss de 06-revisao.md, l. 136): o valor marcado cai de fato, não só cresce menos.
# No dia 274 ele está abaixo do valor do dia 183, com a curva subindo 1% ao dia o tempo todo.
assert rows[274]["com_semestre_contra"] < rows[183]["com_semestre_contra"]
dias_em_queda = sum(rows[t]["com_semestre_contra"] < rows[t - 1]["com_semestre_contra"]
                    for t in range(1, 366))
assert dias_em_queda == 51, dias_em_queda
# fora do semestre, as duas linhas são a mesma
assert all(r["m"] == 1.0 for r in rows if r["dia"] < SEM_INICIO)

with open(os.path.join(out, "graf-01.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
```

## graf-01

**Onde entra:** Anel da Água, logo depois de "Tem dia de taxa negativa, tem semestre inteiro
de marcação a mercado contra você — o preço do título, atualizado todo dia pelo valor de
mercado, em queda." e antes de "Musashi não precisa dessa premissa."

**Por que é graf (raciocínio de `02-estrutura.md`):** há série numérica com métrica real, o
multiplicador acumulado dia a dia pela conta do próprio texto. Isso é graf pelo critério 1. A
ressalva do critério 2 ("duas linhas sem métrica real por trás → diagrama") não se aplica,
porque a métrica é real. Hipotético é só o cenário da segunda linha. info perde: uma peça
basta.

**Pergunta que o gráfico responde:** o que a conta de 1% ao dia (1,01³⁶⁵ ≈ 37,8) mostra e o
que ela esconde, quando o caminho até a mesma chegada tem um semestre de marcação a mercado
contra?

**Fonte dos dados:** cálculo próprio. A linha 1 é a conta do texto (1,01³⁶⁵ = 37,7834,
conferida em `processo/07-verificacao.md`, "Contas" e item 6.6). O "1% melhor por dia" é de
James Clear, *Hábitos Atômicos* ([jamesclear.com/continuous-improvement](https://jamesclear.com/continuous-improvement),
acesso em 2026-10-28, via 07-verificacao). A linha 2 é **cenário ilustrativo, não dado
observado**: a forma é decisão do autor (`processo/04-draft-v2.md`, "Para a etapa 8"), e os
parâmetros foram escolhidos nesta etapa. Não representa a carreira de ninguém.

**Parâmetros do cenário (também escritos na figura e na legenda):**

- valor(t) = 1,01ᵗ × m(t), t em dias corridos de 0 a 365.
- m(t) = 1 antes do dia 183. Do dia 183 ao 365: m(t) = 1 − 0,6 × sen²(π(t − 183)/182).
- O semestre contra é o segundo semestre inteiro, e m fica abaixo de 1 em todos os dias dele.
  No fundo (dia 274), m = 0,4: o valor marcado é 40% do valor da curva (6,1× contra 15,3×).
- No dia 365, m volta a 1 e as duas linhas chegam a 37,78×. É o *pull to par*, a convergência
  da marcação para a curva no vencimento. Queda de preço no caminho, não perda realizada.
- **Por que 0,6:** com a curva rendendo 1% ao dia, uma marcação mais rasa só achata a linha 2
  (com 0,4 ela nunca cai; com 0,5 cai 34 dias, quase nada). Com 0,6 o valor marcado cai de fato
  por 51 dias, e no dia 274 vale menos do que valia no dia 183. É o "em queda" do texto, o
  menor valor redondo que o entrega.
- **Por que o segundo semestre:** o semestre termina no dia 365, então a marcação volta à
  curva no vencimento, como na analogia do texto. Um semestre no meio do ano reverteria antes
  do vencimento.

**Dados:** `posts/2026-10-27-samurais-e-duelos/graficos/dados/graf-01.csv`, 366 linhas (dias
0 a 365). Colunas: `dia`, `curva` (1,01ᵗ), `m` (fator de marcação) e `com_semestre_contra`
(curva × m).

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import math
import os

import pandas as pd
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

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))
# Janela do semestre e fundo lidos do próprio CSV (fonte única: o bloco "Dados").
contra = df[df["m"] < 1]
sem_ini, sem_fim = int(contra["dia"].min()) - 1, int(contra["dia"].max()) + 1
fundo = df.loc[df["m"].idxmin()]
ini = df.loc[df["dia"] == sem_ini].iloc[0]
fim = df.iloc[-1]


def lg(v):
    # anotação em eixo log do Plotly recebe log10 do valor, não o valor
    return math.log10(v)


def num(v, casas=1):
    return f"{v:.{casas}f}".replace(".", ",")


fig = go.Figure()

# Semestre contra: faixa mint atrás das linhas, do dia 183 ao 365.
fig.add_vrect(x0=sem_ini, x1=sem_fim, fillcolor=mint, line_width=0, layer="below")

# Linha 2 por baixo, linha 1 tracejada por cima: até o dia 183 as duas coincidem, e o tracejado
# slate sobre o forest mostra isso sem precisar de legenda.
fig.add_trace(go.Scatter(x=df["dia"], y=df["com_semestre_contra"], mode="lines",
                         line=dict(color=forest, width=4), showlegend=False))
fig.add_trace(go.Scatter(x=df["dia"], y=df["curva"], mode="lines",
                         line=dict(color=slate, width=2, dash="dash"), showlegend=False))
fig.add_trace(go.Scatter(x=[fim["dia"]], y=[fim["curva"]], mode="markers",
                         marker=dict(color=forest, size=11, symbol="square",
                                     line=dict(color=ink, width=1)),
                         showlegend=False))

# Rótulo direto da linha 1 (sem caixa de legenda), no canto vazio acima da reta.
fig.add_annotation(x=110, y=lg(1.01 ** 110), ax=-70, ay=-215, showarrow=True, arrowhead=0,
                   arrowwidth=1, arrowcolor=slate, xanchor="left", align="left",
                   text="Tracejada: 1% todo dia, 1,01<sup>t</sup>.<br>"
                        "Até o dia 183, as duas linhas coincidem.",
                   font=dict(color=slate, size=16, family=font_body))

# Rótulo da linha 2 e achado do semestre na mesma anotação, apontando para o fundo:
# no dia 274 o valor marcado é menor do que no começo do semestre.
fig.add_annotation(
    x=int(fundo["dia"]), y=lg(fundo["com_semestre_contra"]), ax=-30, ay=120,
    showarrow=True, arrowhead=2, arrowwidth=1.5, arrowcolor=forest, xanchor="center",
    align="left",
    text="<b>Cheia: a mesma curva, com o segundo<br>semestre de marcação a mercado contra.</b><br>"
         f"No dia {int(fundo['dia'])}, ela vale {num(fundo['com_semestre_contra'])}×, "
         f"abaixo dos {num(ini['com_semestre_contra'])}×<br>"
         f"do dia {sem_ini}. A curva já está em {num(fundo['curva'])}×.",
    font=dict(color=forest, size=16, family=font_body),
)
# A chegada: as duas linhas no mesmo ponto.
fig.add_annotation(
    x=int(fim["dia"]), y=lg(fim["curva"]), ax=22, ay=0, showarrow=True, arrowhead=0,
    arrowwidth=1, arrowcolor=ink, xanchor="left", align="left",
    text=f"<b>≈ {num(fim['curva'])}×</b><br>nas duas,<br>no dia {int(fim['dia'])}",
    font=dict(color=ink, size=17, family=font_body),
)
# Nome da faixa, no alto.
fig.add_annotation(xref="x", yref="paper", x=(sem_ini + sem_fim) / 2, y=1, yanchor="bottom",
                   showarrow=False, text="Segundo semestre: marcação a mercado contra",
                   font=dict(color=forest, size=15, family=font_body))

# Rodapé alinhado à borda esquerda da figura (paper x negativo = dentro da margem l).
fig.add_annotation(
    xref="paper", yref="paper", x=-0.085, y=0, yshift=-62, xanchor="left", yanchor="top",
    showarrow=False, align="left",
    text="Cenário ilustrativo, não dado observado. Linha cheia: 1,01<sup>t</sup> × m(t), com "
         "m(t) = 1 − 0,6 × sen²(π(t − 183)/182)<br>"
         "do dia 183 ao 365 e m(t) = 1 antes. No dia 274, m = 0,4. No dia 365, m volta a 1, "
         "como a marcação<br>"
         "de um título que converge para a curva no vencimento: queda de preço no caminho, "
         "não perda realizada.<br>"
         "Escala logarítmica: a mesma distância vertical é a mesma variação percentual. "
         "Cálculo próprio.",
    font=dict(color=slate, size=13, family=font_body),
)

fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=900, height=660,
    margin=dict(l=70, r=110, t=90, b=170),
    title=dict(text="A conta do 1% ao dia mostra a chegada, não o caminho",
               font=dict(color=ink, size=22, family=font_display), x=0.02, xanchor="left",
               y=0.97, yanchor="top"),
    font=dict(family=font_body, color=ink),
)
fig.update_xaxes(
    title=dict(text="dias corridos", font=dict(color=slate, size=14, family=font_body)),
    range=[-4, 369], tickvals=[0, 91, sem_ini, 274, sem_fim],
    tickfont=dict(color=slate, size=14, family=font_data),
    showgrid=False, zeroline=False, showline=True, linecolor=mist, ticks="outside",
    tickcolor=mist,
)
# Eixo log começa em 1× (o valor inicial), não em zero: log não tem zero, e 1× é a origem
# real do multiplicador. Ver "Gate de Tufte" abaixo.
fig.update_yaxes(
    type="log", range=[lg(0.9), lg(48)],
    tickvals=[1, 2, 5, 10, 20, 40], ticktext=["1×", "2×", "5×", "10×", "20×", "40×"],
    tickfont=dict(color=slate, size=14, family=font_data),
    title=dict(text="multiplicador acumulado (escala log)",
               font=dict(color=slate, size=14, family=font_body)),
    gridcolor=mist, gridwidth=1, zeroline=False, showline=False,
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
```

**Escolha de tipo:** duas linhas no mesmo eixo, multiplicador × dias corridos, **em escala
logarítmica**. Em log, taxa constante vira reta, e essa é exatamente a premissa que o texto
questiona ("Ela supõe uma taxa constante e positiva, todo santo dia"). O semestre contra
aparece como desvio dessa reta, e a profundidade se lê como porcentagem: 40% da curva ocupa a
mesma altura em qualquer ponto do ano. Descartado: eixo linear. Ele dá a "curva de taco de
hóquei" que o leitor conhece do Clear, mas espreme os primeiros cinco meses abaixo de 5× (cerca
de um oitavo da altura) e faz um mesmo percentual de queda parecer maior no fim do ano do que
no começo. Descartados também: dias negativos esparsos e "mesma média com oscilação", as outras
formas que `02-estrutura.md` deixava abertas. O autor escolheu o semestre que se reverte.

**Anotação:** três `add_annotation` ligadas ao dado, sem caixa de legenda. (1) O rótulo da
linha cheia junto com o achado, com seta para o fundo do semestre, no dia 274: a marcação está
em 6,1×, abaixo dos 6,2× do dia 183, com a curva já em 15,3×. Um trimestre inteiro de "1% ao
dia" apagado no preço. Rótulo e achado ficam juntos porque, separados, colidiam na mesma região.
(2) A chegada no dia 365, "≈ 37,8× nas duas", sobre o marcador quadrado. (3) O rótulo da
tracejada, no canto vazio acima da reta, que avisa que as duas linhas coincidem até o dia 183.
A faixa `mint` com o nome "Segundo semestre: marcação a mercado contra" marca a janela.

**Gate de Tufte:**
- **Eixo sem zero, por exceção justificada.** O eixo é log, que não tem zero, e começa em 0,9,
  logo abaixo de 1×, que é o valor inicial real do multiplicador. Não há trecho truncado: a
  série inteira, de 1× a 37,8×, está na figura. A escala log está declarada no título do eixo
  e no rodapé.
- **Lie Factor:** nenhuma área ou tamanho codifica dado. A faixa `mint` marca uma janela de
  tempo (dias 183 a 365) e tem exatamente essa largura no eixo x. A diferença entre as linhas
  é posição num eixo log declarado, então a altura visual é proporcional a log(m). É
  proporcional ao dado na escala que o rodapé anuncia. O alvo é 1,0 nessa escala, e não há
  ênfase extra.
- Sem 3D, sombra, textura nem moldura. Só grid horizontal, em `mist`.
- Duas séries, abaixo do limiar de três: não há caso para *small multiples* nem para revelação
  progressiva.
- Acessibilidade (DESIGN.md §8, 1.4.1): as linhas se distinguem por cor **e** por traço (cheia
  × tracejada), com rótulo direto em cada uma.

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo),
`color.forest.500` (linha 2, marcador, nome da faixa), `color.neutral.slate` (linha 1, eixos,
rodapé), `color.neutral.mint` (faixa do semestre), `color.neutral.mist` (grid e linha de base),
`color.neutral.ink` (anotações principais, título); `typography.fontFamily.display` (título),
`.body` (texto), `.data` (números dos eixos). Sem `lime`: a chegada não é conquista a celebrar,
e o argumento do texto é o caminho, não o ponto final.

**Alt-text (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linhas, em escala logarítmica, do multiplicador acumulado ao longo de 365 dias
> corridos. A linha tracejada é a conta de 1% ao dia, composto: sobe em reta, de 1× até cerca de
> 37,8× no dia 365. A linha cheia é um cenário ilustrativo: a mesma curva, mas com o segundo
> semestre inteiro de marcação a mercado contra. As duas coincidem até o dia 183. Depois a
> linha cheia descola para baixo. No dia 274, a curva está em 15,3×, e a linha cheia em 6,1×,
> menos do que os 6,2× que valia no dia 183. Ela então sobe mais rápido e encontra a curva no
> dia 365, nos mesmos 37,8×. Mesma chegada, caminho diferente: queda de preço no caminho, não
> perda realizada.

**Legenda:**

> A conta do 1% ao dia mostra a chegada, não o caminho. As duas linhas chegam a 1,01³⁶⁵ ≈ 37,8×
> no dia 365. A cheia passa o segundo semestre com a marcação a mercado contra: o preço,
> atualizado todo dia pelo valor de mercado, cai até 40% do que diz a curva no dia 274 e volta
> a ela no vencimento. Cenário ilustrativo, não dado observado: valor = 1,01ᵗ × m(t), com
> m(t) = 1 − 0,6 × sen²(π(t − 183)/182) do dia 183 ao 365. Escala logarítmica. Cálculo próprio.
