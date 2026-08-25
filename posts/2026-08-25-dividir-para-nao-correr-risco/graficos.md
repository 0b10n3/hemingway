# Gráficos — Dividir para não correr risco

Uma peça, decidida em `processo/02-estrutura.md` (seção 4) e posicionada em
`processo/04-draft-v1.md`, no início de "Quanto a LCI movimenta no mercado". Checklist de
craft (`references/checklist-graficos.md`) aplicado abaixo: anotação direta nos pontos de
interesse, avaliação de revelação progressiva, contraste avaliado quanto a ser genuíno. Tokens
de marca lidos em runtime de `marca/tokens.json` (skill `marca-syntaxis`) — nenhuma cor
hardcoded fora do arquivo de origem.

## graf-01

**Pergunta que o gráfico responde:** quanto o estoque de LCI cresceu desde 2020, e onde nessa
trajetória aparece o efeito de duas mudanças de regra do CMN (aperto em 2024, afrouxamento em
2025)?

**Fonte dos dados:** confirmada em `processo/07-verificacao.md` item 1 e item 8 — B3/Bora
Investir ("CDB, LCI, LCA e LF: estoque de produtos de captação bancária na B3 cresceu 17% em
2025") e cobertura da Suno sobre o release B3 do 1º semestre de 2026, acesso 25/08/2026. O
ponto de dez/2020 (R$ 141 bi) segue como aproximação própria do autor, não dado publicado
diretamente pela B3 nesta pesquisa — sinalizado no próprio gráfico (ver nota abaixo).

**Dados:** `posts/2026-08-25-dividir-para-nao-correr-risco/graficos/dados/graf-01.csv` — seis
pontos confirmados (não é série mensal contínua): dez/2020, jan/2024, abr/2024, dez/2024,
dez/2025, jun/2026. Entre dez/2020 e jan/2024 não existe dado intermediário verificado — o
gráfico marca esse trecho com linha tracejada e cor apagada, em vez de sugerir uma trajetória
mensal que não foi confirmada (ver "Contraste genuíno" abaixo).

**Código Plotly executável** (testado com `python3` nesta etapa — gera `figuras/graf-01.svg`
e `figuras/graf-01.png`):

```python
import json
import os
import pandas as pd
import plotly.graph_objects as go

POST_DIR = "posts/2026-08-25-dividir-para-nao-correr-risco"
TOKENS_PATH = "marca/tokens.json"

with open(TOKENS_PATH, encoding="utf-8") as f:
    tokens = json.load(f)

# Cores lidas de marca/tokens.json em runtime — fonte única, nenhum hex duplicado aqui.
bg = tokens["neutrals"]["obsidian"]["hex"]
grid = tokens["dataviz"]["grid_line"]
axis_text = tokens["dataviz"]["axis_text"]
text_high = tokens["text"]["high"]["hex"]
text_medium = tokens["text"]["medium"]["hex"]
text_low = tokens["text"]["low"]["hex"]
carbon = tokens["neutrals"]["carbon"]["hex"]
volt_hero = tokens["volt"]["500"]["hex"]
warning = tokens["functional"]["warning"]["hex"]

df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"))
# Datas mantidas como string ISO (não pandas.Timestamp): kaleido/orjson não serializa
# Timestamp em add_annotation. Plotly já detecta eixo de data a partir da string "YYYY-MM-DD".

fig = go.Figure()

# Trecho dez/2020-jan/2024 não tem dado intermediário (só as duas pontas): linha
# tracejada e cor apagada para não sugerir trajetória mensal conhecida que não existe.
fig.add_trace(go.Scatter(
    x=df["data"].iloc[0:2], y=df["estoque_lci_bi"].iloc[0:2],
    mode="lines+markers",
    name="Sem dado intermediário",
    line=dict(color=text_low, width=2, dash="dot"),
    marker=dict(size=8, color=text_low, line=dict(color=bg, width=1)),
    hovertemplate="%{x|%b/%Y}: R$ %{y:,.1f} bi<extra></extra>",
    showlegend=False,
))
fig.add_annotation(
    x=df["data"].iloc[1], y=(df["estoque_lci_bi"].iloc[0] + df["estoque_lci_bi"].iloc[1]) / 2 - 30,
    text="sem dado intermediário<br>entre 2020 e 2024",
    showarrow=False, font=dict(color=text_low, size=11, family="Inter, sans-serif"),
    xanchor="right",
)

fig.add_trace(go.Scatter(
    x=df["data"].iloc[1:], y=df["estoque_lci_bi"].iloc[1:],
    mode="lines+markers",
    name="Estoque de LCI",
    line=dict(color=volt_hero, width=3, dash="solid"),
    marker=dict(size=8, color=volt_hero, line=dict(color=bg, width=1)),
    hovertemplate="%{x|%b/%Y}: R$ %{y:,.1f} bi<extra></extra>",
))

# Marca o ponto de recuo pós-aperto regulatório (abr/2024) com cor de alerta.
fig.add_trace(go.Scatter(
    x=[df["data"].iloc[2]], y=[df["estoque_lci_bi"].iloc[2]],
    mode="markers",
    marker=dict(size=11, color=warning, line=dict(color=bg, width=2)),
    showlegend=False,
    hoverinfo="skip",
))

fig.add_annotation(
    x=df["data"].iloc[2], y=df["estoque_lci_bi"].iloc[2],
    text="Recuo pós-Resoluções CMN<br>5.118/5.119 (lastro mais rígido)",
    showarrow=True, arrowhead=2, arrowcolor=warning, arrowwidth=1.5,
    ax=-40, ay=50,
    font=dict(color=warning, size=12, family="Inter, sans-serif"),
    align="left",
)

fig.add_annotation(
    x=df["data"].iloc[4], y=df["estoque_lci_bi"].iloc[4],
    text="<b>+29% em 2025</b><br>maior alta entre os produtos<br>de captação bancária na B3",
    showarrow=True, arrowhead=2, arrowcolor=volt_hero, arrowwidth=1.5,
    ax=-30, ay=-55,
    font=dict(color=text_high, size=12, family="Inter, sans-serif"),
    align="left",
    bgcolor=carbon, bordercolor=grid, borderwidth=1, borderpad=6,
)

fig.add_annotation(
    x=df["data"].iloc[-1], y=df["estoque_lci_bi"].iloc[-1],
    text="<b>R$ 544 bi</b><br>jun/2026",
    showarrow=False, xanchor="left", xshift=14,
    font=dict(color=volt_hero, size=13, family="Inter, sans-serif"),
    align="left",
)

fig.update_layout(
    title=dict(
        text="O estoque de LCI quase quadruplicou desde 2020 — com um recuo no meio do caminho",
        font=dict(color=text_high, size=16, family="Space Grotesk, sans-serif"),
        x=0.02, xanchor="left",
    ),
    paper_bgcolor=bg,
    plot_bgcolor=bg,
    font=dict(color=text_medium, family="Inter, sans-serif"),
    xaxis=dict(
        title="",
        gridcolor=grid, zerolinecolor=grid, color=axis_text,
        tickformat="%Y",
    ),
    yaxis=dict(
        title="Estoque de LCI (R$ bilhões)",
        gridcolor=grid, zerolinecolor=grid, color=axis_text,
        tickprefix="R$ ", ticksuffix=" bi", rangemode="tozero",
    ),
    showlegend=False,
    margin=dict(l=70, r=130, t=70, b=50),
    width=900, height=560,
)

os.makedirs(os.path.join(POST_DIR, "figuras"), exist_ok=True)
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.svg"))
fig.write_image(os.path.join(POST_DIR, "figuras/graf-01.png"), scale=2)
```

**Escolha de tipo de gráfico justificada:** linha (série temporal) — a pergunta é sobre
trajetória ao longo do tempo e onde nela aparecem dois eventos regulatórios específicos, não
uma comparação pontual entre categorias, então um gráfico de barras foi descartado (esconderia
justamente o "recuo no meio do caminho" que é o achado central do gráfico).

*Nota sobre revelação progressiva (checklist):* uma série única, sem categorias competindo —
não há motivo para dividir em gráficos sequenciais.

*Nota sobre contraste genuíno (checklist):* o "antes/depois" real aqui não é um par
conceitual forçado — é o próprio par que os dados sustentam (estoque antes e depois do aperto
de fev/2024), então a anotação de contraste (ponto de alerta em abr/2024) é genuína, não
decorativa. Já o trecho dez/2020–jan/2024 recebeu tratamento oposto — linha tracejada e cor
apagada — precisamente para **não** fingir um contraste ou uma trajetória contínua que os
dados não sustentam: é a aplicação do mesmo princípio (não forçar leitura que o dado não dá)
em sentido inverso.

**Alt-text final (para o placeholder `graf-01` em `post.md`):**

> Gráfico de linha mostrando a evolução do estoque de LCI no Brasil, em R$ bilhões, de
> dezembro de 2020 a junho de 2026. Sai de R$ 141 bilhões (dez/2020, sem dado intermediário
> confirmado até 2024) para R$ 373 bilhões em janeiro de 2024, recua para R$ 362 bilhões em
> abril de 2024 após o aperto de lastro das Resoluções CMN 5.118 e 5.119, fecha 2024 em R$
> 392,8 bilhões, acelera para R$ 508,8 bilhões ao final de 2025 (alta de 29% no ano, a maior
> entre os produtos de captação bancária na B3) e chega a R$ 544 bilhões em junho de 2026.

**Legenda (para exibição junto à figura em `post.md`):**

> Estoque de LCI no Brasil, R$ bilhões (B3/Bora Investir; dez/2020 é aproximação própria a
> partir de fonte agregada). O ponto laranja marca o recuo após o aperto regulatório de
> fev/2024 (Resoluções CMN 5.118/5.119); o trecho tracejado não tem dado mensal confirmado.
