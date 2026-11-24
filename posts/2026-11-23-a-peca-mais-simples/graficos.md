# Gráficos — "A Peça Mais Simples"

Duas peças decididas em `processo/02-estrutura.md` ("Visuais — decisão pelo critério"),
renumeradas pela ordem de aparição no texto na etapa 4: **`graf-01` = Copom × taxa prefixada, a
história longa** (o `graf-02` de `02-estrutura.md`) e **`graf-02` = o Prefixado 2029 em outubro** (o
`graf-01` de lá). **Esta versão traz só o `graf-01`**, feito antes da etapa 8 a pedido do autor
(2026-11-23), junto com o prompt do infográfico alternativo (`infograficos.md`, tensão T2). O
`graf-02` entra na etapa 8, que também revisa este bloco contra o checklist; não refaz.

Os tokens de marca são lidos em runtime de `../../brand/tokens/syntaxis.tokens.json`. Todo bloco
roda a partir da raiz do repositório (`pipelines/hemingway/`) e foi testado com `python3` (plotly +
kaleido). A fonte de título (Montserrat) não está instalada nesta máquina; o PNG sai com a fonte
reserva da pilha. Reexportar com Montserrat, Source Sans 3 e IBM Plex Mono instaladas, se quiser.

## Dados

O bloco baixa as séries das fontes primárias e grava `graficos/dados/graf-01.csv` (diária) e as duas
versões enxutas usadas no prompt do infográfico (`graf-01-semanal.csv`, `graf-01-meta-selic.csv`).
Os `assert` conferem a série contra `processo/03-pesquisa.md` (itens 5 e 8). Só biblioteca padrão.
O CSV do Tesouro tem 14,7 MB; para não baixar de novo, aponte `TD_CSV` para uma cópia local.

**Escolha da série (de `03-pesquisa.md`, item 4):** nenhuma série pública cobre 2002 a 2026 sozinha.
De jan/2002 a set/2019, a taxa referencial de *swap* DI × pré de 360 dias da B3 (SGS 7806,
descontinuada em 30/09/2019). De out/2019 em diante, a taxa de compra das LTN no Tesouro Direto,
interpolada linearmente para 365 dias corridos entre as duas LTN que cercam 1 ano. As duas medem a
mesma coisa (a taxa prefixada de 1 ano) e, no período em que se sobrepõem (2005–2019), a versão do
Tesouro Direto fica em média 0,06 p.p. acima do *swap* (desvio de 0,13 p.p.; cálculo do
pesquisador). No 1º semestre de 2023 não havia LTN de menos de 1 ano no Tesouro Direto (a mais curta
tinha cerca de 546 dias): a série fica sem dado, e o gráfico mostra a lacuna em vez de extrapolar.
A meta Selic é a SGS 432, que vale a partir do dia seguinte à reunião.

```python
import csv
import io
import json
import os
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta

POST_DIR = "posts/2026-11-23-a-peca-mais-simples"
OUT = os.path.join(POST_DIR, "graficos/dados")
INI, FIM = date(2002, 1, 1), date(2026, 11, 19)   # FIM = última data-base do CSV do Tesouro
CORTE_SWAP = date(2019, 9, 30)                     # a SGS 7806 termina aqui
TD_URL = ("https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/"
          "resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv")
TD_CSV = os.environ.get("TD_CSV")                  # opcional: o CSV já baixado (14,7 MB)


def baixar(url, tentativas=4):
    # a API do BCB devolve 502 de vez em quando; tenta de novo antes de desistir
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for n in range(tentativas):
        try:
            return urllib.request.urlopen(req, timeout=180).read()
        except urllib.error.HTTPError as e:
            if e.code < 500 or n == tentativas - 1:
                raise
            time.sleep(5 * (n + 1))


def sgs(codigo, ini, fim):
    # série diária: a API devolve no máximo 10 anos por consulta
    serie, a = {}, ini
    while a <= fim:
        b = min(date(a.year + 9, 12, 31), fim)
        url = (f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json"
               f"&dataInicial={a:%d/%m/%Y}&dataFinal={b:%d/%m/%Y}")
        for r in json.loads(baixar(url)):
            if r["valor"] not in ("", None):
                serie[datetime.strptime(r["data"], "%d/%m/%Y").date()] = float(r["valor"])
        a = b + timedelta(days=1)
    return serie


def dia(s):
    return datetime.strptime(s, "%d/%m/%Y").date()


def interp_1a(pontos, alvo=365):
    # linear na taxa, entre as duas LTN que cercam 1 ano (dias corridos); sem par, sem dado
    abaixo = [p for p in pontos if p[0] <= alvo]
    acima = [p for p in pontos if p[0] >= alvo]
    if not abaixo or not acima:
        return None
    (d0, t0), (d1, t1) = max(abaixo), min(acima)
    return t0 if d1 == d0 else t0 + (t1 - t0) * (alvo - d0) / (d1 - d0)


meta = sgs(432, INI, FIM)
swap = {d: v for d, v in sgs(7806, INI, CORTE_SWAP).items() if v > 0}

raw = open(TD_CSV, "rb").read() if TD_CSV else baixar(TD_URL)
ltn = defaultdict(list)
for r in csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter=";"):
    if r["Tipo Titulo"] != "Tesouro Prefixado":
        continue
    base = dia(r["Data Base"])
    if CORTE_SWAP < base <= FIM:
        taxa = float(r["Taxa Compra Manha"].replace(",", "."))
        if taxa > 0:
            ltn[base].append(((dia(r["Data Vencimento"]) - base).days, taxa))
td = {d: interp_1a(p) for d, p in ltn.items()}

linhas = []
for d in sorted(set(swap) | set(td)):
    if d not in meta:
        continue
    if d <= CORTE_SWAP:
        pre, fonte = swap[d], "swap_di_pre_360_b3"
    else:
        pre, fonte = td[d], "ltn_td_interp_1a"
    linhas.append({"data": d.isoformat(), "meta_selic": f"{meta[d]:.2f}",
                   "pre_1a": "" if pre is None else f"{pre:.4f}", "fonte_pre": fonte})

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "graf-01.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0]))
    w.writeheader()
    w.writerows(linhas)

v = {r["data"]: r for r in linhas}
pre = lambda d: float(v[d]["pre_1a"])
# confere com 03-pesquisa.md, item 5 (episódios) e item 8 (meta Selic)
assert f"{pre('2002-10-15'):.2f}" == "32.69" and v["2002-10-15"]["meta_selic"] == "21.00"
assert f"{pre('2008-10-24'):.2f}" == "16.38"
assert f"{pre('2016-10-19'):.2f}" == "12.18"
assert v["2026-11-19"]["meta_selic"] == "13.75"
lacuna = [r["data"] for r in linhas if r["pre_1a"] == ""]
print("linhas", len(linhas), "lacuna", len(lacuna), lacuna[:1], lacuna[-1:])
for d in ("2020-08-07", "2021-03-17", "2024-11-26", "2024-12-19", "2026-10-02",
          "2026-10-09", "2026-10-23", "2026-10-26", "2026-11-19"):
    print(d, v[d]["pre_1a"], v[d]["meta_selic"])

# Versões enxutas para o prompt do infográfico (graficos/info-01-prompt-claude-web.md):
# semanal = última observação de cada semana ISO, com o dia de cada episódio no lugar da sua semana;
# meta Selic = só as datas em que a meta muda (primeiro dia da série com a nova meta).
EPISODIOS = ["2002-10-15", "2008-10-24", "2015-09-23", "2016-10-19", "2021-03-17", "2024-12-19",
             "2026-10-26"]
semana = {}
for r in linhas:
    k = date.fromisoformat(r["data"]).isocalendar()[:2]
    if semana.get(k, {}).get("data") not in EPISODIOS:
        semana[k] = r
with open(os.path.join(OUT, "graf-01-semanal.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["data", "pre_1a"])
    for k in sorted(semana):
        r = semana[k]
        w.writerow([r["data"], f"{float(r['pre_1a']):.2f}" if r["pre_1a"] else ""])
mudancas, anterior = [], None
for r in linhas:
    if r["meta_selic"] != anterior:
        mudancas.append([r["data"], r["meta_selic"]])
        anterior = r["meta_selic"]
with open(os.path.join(OUT, "graf-01-meta-selic.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["vigente_desde", "meta_selic"])
    w.writerows(mudancas)
assert all(semana[date.fromisoformat(d).isocalendar()[:2]]["data"] == d for d in EPISODIOS)
print("semanal", len(semana), "mudancas da meta", len(mudancas))
```

## graf-01

**Onde entra:** no Mito ("Prefixado para quem acha que o juro vai cair"), onde o autor deixou a NOTA
PARA CLAUDE: depois de "…sobe quando ele corta, cai quando ele aperta." e antes de "Tem um pedaço
de verdade aí." A etapa 4 escreve a frase de anúncio, com dois-pontos.

**Por que é graf (`02-estrutura.md`):** série numérica real contra uma referência, critério 1. A
alternativa em infográfico (T2) está em `infograficos.md`; o autor escolhe no gate.

**Pergunta que o gráfico responde:** a taxa prefixada acompanha o Copom, ou anda antes dele e salta
sem ele?

**Fonte dos dados:** Banco Central, SGS 432 (meta Selic) e SGS 7806 (*swap* DI × pré de 360 dias, B3,
até set/2019), https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados; Tesouro Nacional,
Tesouro Transparente, "Preço e taxa dos títulos do Tesouro Direto",
https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv
(data-base até 19/11/2026). Acesso em 2026-11-23. Interpolação de 1 ano: cálculo próprio.

**Dados:** `posts/2026-11-23-a-peca-mais-simples/graficos/dados/graf-01.csv`, 6.184 dias úteis de
02/01/2002 a 19/11/2026. Colunas: `data`, `meta_selic`, `pre_1a` (vazio nos 124 dias do 1º semestre
de 2023), `fonte_pre` (`swap_di_pre_360_b3` ou `ltn_td_interp_1a`).

**Código Plotly executável** (gera `figuras/graf-01.svg` e `figuras/graf-01.png`):

```python
import json
import os

import pandas as pd
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
grove = c["grove"]["500"]["$value"]       # a série que é o ponto (DESIGN.md §10)
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")


def num(v, casas=1):
    return f"{v:.{casas}f}".replace(".", ",")


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-01.csv"), parse_dates=["data"])
ix = df.set_index("data")

fig = go.Figure()
# Meta Selic: contexto, em slate, em degrau (vale até a próxima decisão do Copom).
fig.add_trace(go.Scatter(x=df["data"], y=df["meta_selic"], mode="lines", line_shape="hv",
                         line=dict(color=slate, width=2), showlegend=False, hoverinfo="skip"))
# Taxa prefixada de 1 ano: o ponto do gráfico, em grove.500. A lacuna de 2023 fica visível.
fig.add_trace(go.Scatter(x=df["data"], y=df["pre_1a"], mode="lines", connectgaps=False,
                         line=dict(color=grove, width=1.6), showlegend=False, hoverinfo="skip"))

# Episódios (03-pesquisa.md, item 5). O número vem do CSV; o texto diz o que a Selic fazia.
EPISODIOS = [
    ("2002-10-15", "<b>out/2002, eleição</b><br>{pre}%, com a Selic em {selic}%", 60, 10, "left"),
    ("2008-10-24", "<b>out/2008, Lehman</b><br>{pre}%, Selic parada em {selic}%", 0, -80, "center"),
    ("2016-10-19", "<b>out/2016, 1º corte do Copom</b><br>a taxa já estava em {pre}%, Selic em {selic}%",
     -50, 95, "right"),
    ("2021-03-17", "<b>mar/2021, 1ª alta do Copom</b><br>a taxa já estava em {pre}%, Selic em {selic}%",
     -40, -150, "right"),
    ("2024-12-19", "<b>dez/2024, pacote fiscal</b><br>{pre}%, Selic em {selic}%", -20, -75, "right"),
    ("2026-10-26", "<b>out/2026, eleição</b><br>{pre}%, Selic parada em {selic}%", -10, -150, "right"),
]
for d, txt, ax, ay, anchor in EPISODIOS:
    r = ix.loc[d]
    selic = r["meta_selic"]
    fig.add_trace(go.Scatter(x=[d], y=[r["pre_1a"]], mode="markers", showlegend=False,
                             hoverinfo="skip", marker=dict(color=grove, size=8,
                                                           line=dict(color=bg, width=1.5))))
    fig.add_annotation(x=d, y=r["pre_1a"], ax=ax, ay=ay, showarrow=True, arrowhead=0, arrowwidth=1,
                       arrowcolor=ink, xanchor=anchor, align=anchor if anchor != "center" else "center",
                       text=txt.format(pre=num(r["pre_1a"]), selic=num(selic, 2).rstrip("0").rstrip(",")),
                       font=dict(color=ink, size=13, family=font_body), bgcolor=bg)

fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-46, xanchor="left", yanchor="top",
                   showarrow=False, align="left",
                   text="Fonte: Banco Central, SGS 432 (meta Selic) e SGS 7806 (swap DI × pré de 360 dias, "
                        "B3, até set/2019); Tesouro Nacional, Tesouro Transparente<br>(taxa de compra das LTN "
                        "no Tesouro Direto, interpolada para 1 ano, de out/2019 em diante; cálculo próprio). "
                        "1º semestre de 2023 sem dado:<br>não havia LTN de menos de 1 ano no Tesouro Direto.",
                   font=dict(color=slate, size=12, family=font_body))

fig.update_xaxes(range=["2001-07-01", "2027-03-01"], dtick="M24", tickformat="%Y",
                 tickfont=dict(color=slate, size=13, family=font_data),
                 showgrid=False, zeroline=False, showline=False, ticks="")
fig.update_yaxes(range=[0, 36], tickvals=[0, 5, 10, 15, 20, 25, 30, 35],
                 ticktext=[f"{v}%" for v in (0, 5, 10, 15, 20, 25, 30, 35)],
                 tickfont=dict(color=slate, size=13, family=font_data),
                 gridcolor=mist, gridwidth=1, zeroline=False, showline=False)
fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=1000, height=640,
    margin=dict(l=60, r=40, t=96, b=118),
    title=dict(text="A taxa prefixada anda antes do Copom e salta sem ele<br>"
                    f"<span style='font-size:15px;color:{slate};font-family:{font_body}'>"
                    f"<b style='color:{slate}'>meta Selic</b> (o degrau das decisões do Copom) e "
                    f"<b style='color:{grove}'>taxa prefixada de 1 ano</b>, em % ao ano, 2002 a 2026</span>",
               font=dict(color=ink, size=22, family=font_display), x=0.01, xanchor="left",
               y=0.965, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-01.svg"))
fig.write_image(os.path.join(out_dir, "graf-01.png"), scale=2)
print("ok")
```

**Escolha de tipo:** duas linhas no mesmo eixo, a meta em degrau (vale até a próxima decisão) e a taxa
prefixada diária, com seis episódios anotados. A comparação é de distância e de quem vira primeiro, no
mesmo eixo e na mesma unidade. Descartados: (1) a diferença entre as duas (taxa − Selic) num gráfico
só, que esconde o nível e o degrau do Copom, que são o assunto; (2) média mensal, que apaga os saltos
(o pico de 32,7% em 15/10/2002 vira cerca de 30%); (3) *small multiples* por ciclo, que quebram a
leitura de 25 anos numa linha só; (4) o episódio de 2015 e o de nov/2022 anotados, que lotariam a
metade direita (ficam nos cartões do infográfico e em `03-pesquisa.md`).

**Anotação:** seis episódios com o valor do dia e a meta Selic do dia, tirados do CSV: out/2002
(eleição: 32,7%, Selic em 21%), out/2008 (Lehman: 16,4%, Selic parada em 13,75%), out/2016 (1º corte:
a taxa já em 12,2%, Selic em 14,25%), mar/2021 (1ª alta: a taxa já em 4,6%, Selic em 2%), dez/2024
(pacote fiscal: 15,6%, Selic em 12,25%), out/2026 (eleição: 14,6%, Selic parada em 13,75%). As séries
são identificadas no subtítulo, com cada nome na cor da sua linha (os rótulos dentro do painel batiam
nas linhas em qualquer posição testada).

**Gate de Tufte:**
- Eixo y em zero (taxas; o zero é a referência natural). Escala linear nos dois eixos.
- Duas séries, abaixo do limiar de três. Só uma tem cor; a outra se distingue também pela forma
  (degrau) e pela espessura.
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`.
- A lacuna de 2023 aparece como quebra da linha, declarada no rodapé.
- Emenda de fontes declarada no rodapé (*swap* até set/2019, LTN interpolada depois).

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo,
contorno dos marcadores, fundo das anotações), `color.grove.500` (taxa prefixada, marcadores, nome da
série no subtítulo), `color.neutral.slate` (meta Selic, eixos, subtítulo, rodapé), `color.neutral.ink`
(título, anotações), `color.neutral.mist` (grid); `typography.fontFamily.display` (título), `.body`
(subtítulo, anotações, rodapé), `.data` (eixos). Sem `lime`.

**Título no gráfico:** "A taxa prefixada anda antes do Copom e salta sem ele"

**Alt-text (para o placeholder `graf-01` em `post.md`, 115 caracteres):**

> Meta Selic e taxa prefixada de 1 ano, 2002 a 2026: a taxa vira antes do Copom e salta em crises com a Selic parada.

**Legenda:**

> Meta Selic (degrau) e taxa prefixada de 1 ano, de 2002 a 2026. Nos ciclos longos, as duas andam
> juntas; nas viradas, a taxa vira antes do Copom; nos sustos (2002, 2008, 2024, 2026), salta com a
> Selic parada ou na contramão. Fonte: Banco Central (SGS 432 e 7806) e Tesouro Transparente; cálculo
> próprio.
