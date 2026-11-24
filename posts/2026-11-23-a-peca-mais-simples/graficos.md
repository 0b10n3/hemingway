# Gráficos — "A Peça Mais Simples"

Duas peças decididas em `processo/02-estrutura.md` ("Visuais — decisão pelo critério"),
renumeradas pela ordem de aparição no texto na etapa 4: **`graf-01` = Copom × taxa prefixada, a
história longa** (o `graf-02` de `02-estrutura.md`) e **`graf-02` = o Prefixado 2029 em outubro** (o
`graf-01` de lá). **As duas peças existem.** O `graf-01` foi feito antes da etapa 8 a pedido do
autor (2026-11-23), junto com o prompt do infográfico alternativo (`infograficos.md`, tensão T2); a
etapa 8 o revisou contra o checklist sem refazê-lo (nota no fim do bloco dele) e produziu o
`graf-02`, cujo bloco de dados fica dentro da seção dele. A seção "Dados" logo abaixo é a do
`graf-01`.

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
grove_txt = c["grove"]["700"]["$value"]   # texto em verde: 4,95:1 sobre Chalk (grove.500 dá 3,16:1)
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
     -60, -180, "right"),
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
                    f"<b style='color:{grove_txt}'>taxa prefixada de 1 ano</b>, em % ao ano, 2002 a 2026</span>",
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

> Nos ciclos longos, a taxa prefixada acompanha a Selic; nas viradas, vira antes do Copom; nos sustos, salta com a Selic parada.

**Revisão da etapa 8 (2026-11-23), contra `checklist-graficos.md` e a marca.** Conferido e dentro do
padrão: pergunta em uma frase, fonte com link e data de acesso, dados versionados, tokens lidos em
runtime, forma de ênfase (`grove.500` × `slate`), eixo y em zero, sem 3D, sombra ou moldura, sem
`lime`, alt-text de 115 caracteres. Fora do padrão (dados e figura não foram mexidos: esta etapa não
regrava `figuras/graf-01.*`). **Itens 1 a 3 aplicados pela conversa principal em 2026-11-24, figura reexportada:**

1. **A anotação de mar/2021 cobre o pico de 2015 (erro de leitura).** O fundo Chalk da caixa corta a
   linha em cerca de 15,6%; a série chega a 16,23% em 23/09/2015 (`graf-01.csv`), e o episódio do
   rebaixamento some. Correção testada: na tupla de `2021-03-17`, trocar `-40, -150` por `-60, -180`
   (a caixa sobe acima do pico e não encosta na de dez/2024). Reexportar a figura depois.
2. **Contraste do nome da série no subtítulo.** "taxa prefixada de 1 ano" em `grove.500` sobre Chalk
   dá 3,16:1; texto de 15 px pede 4,5:1 (`DESIGN.md` §8, SC 1.4.3). A linha fica em `grove.500` (traço
   pede 3:1); o texto vai para `grove.700` (4,95:1), como no rótulo do `graf-02`.
3. **Legenda de quatro linhas.** A instrução pede uma linha, com o ponto que a figura prova; a fonte
   já está no rodapé da figura. Proposta: "Nos ciclos longos, a taxa prefixada acompanha a Selic; nas
   viradas, vira antes do Copom; nos sustos, salta com a Selic parada."
4. **Para o gate, não é erro:** em 26/10, o `graf-01` mostra 14,6% (taxa de 1 ano, interpolada) e o
   `graf-02`, 15,40% (o Prefixado 2029, prazo mais longo). As séries estão rotuladas, mas o leitor
   atento pode estranhar os dois números para o mesmo dia.

## graf-02

**Onde entra:** no Mito, depois de "Dia a dia, a taxa do Prefixado 2029 e a Selic:" (frase de anúncio
da etapa 4, com dois-pontos) e antes de "E tem o outro lado." O placeholder já está em
`processo/04-draft-v2.md`.

**Por que é graf (`02-estrutura.md`, onde se chama `graf-01`):** série numérica real (a taxa de
compra diária do Tesouro Direto) contra uma referência (a meta Selic), critério 1. Taxa, não preço,
no eixo: a comparação é com a Selic, na mesma unidade. Começa em 1/10, e não em 9/10, por decisão do
autor (`04-draft-v2.md`, item 4 da crítica): mostra o 1º turno, que o texto usa duas vezes (o rali de
5/10 no Mito e "o dia mais otimista do ano" em "De volta a outubro").

**Pergunta que o gráfico responde:** com a Selic parada em 13,75%, quanto e quando andou a taxa do
Prefixado 2029 entre o 1º turno e 17/11/2026?

**Fonte dos dados:** Tesouro Nacional, Tesouro Transparente, "Preço e taxa dos títulos do Tesouro
Direto",
https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv
(taxa e PU de compra da manhã; arquivo atualizado em 20/11/2026, data-base até 19/11/2026); Banco
Central, SGS 432 (meta Selic),
https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/10/2026&dataFinal=17/11/2026.
Acesso em 2026-11-23. A série bate, linha a linha, com a tabela de `processo/03-pesquisa.md`, item 8.

**Dados:** `posts/2026-11-23-a-peca-mais-simples/graficos/dados/graf-02.csv`, 32 pregões de
01/10 a 17/11/2026 (sem pregão em 12/10 e 2/11, feriados). Colunas: `data`, `taxa_compra` (% ao
ano), `pu_compra` (R$, liquidação em D+1), `meta_selic` (% ao ano, 13,75 em todas as linhas). O
período para em 17/11, a última data do texto: o CSV do Tesouro vai até 19/11, mas os dois pregões a
mais seriam uma cauda sem anotação, e o rótulo do fim da linha passaria a mostrar uma taxa (15,04%) que
o texto não cita. O bloco abaixo gera o CSV das fontes primárias, só com biblioteca padrão; os
`assert` conferem os números que o texto e as anotações usam. Para não baixar de novo os 14,7 MB do
Tesouro, aponte `TD_CSV` para uma cópia local.

```python
import csv
import io
import json
import os
import time
import urllib.error
import urllib.request
from datetime import date, datetime

POST_DIR = "posts/2026-11-23-a-peca-mais-simples"
OUT = os.path.join(POST_DIR, "graficos/dados")
INI, FIM = date(2026, 10, 1), date(2026, 11, 17)   # 1/10 mostra o 1º turno; 17/11 é a última data do texto
VENC = "01/01/2029"                                 # Tesouro Prefixado 2029
TD_URL = ("https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/"
          "resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv")
TD_CSV = os.environ.get("TD_CSV")                   # opcional: o CSV já baixado (14,7 MB)


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


def dia(s):
    return datetime.strptime(s, "%d/%m/%Y").date()


url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json"
       f"&dataInicial={INI:%d/%m/%Y}&dataFinal={FIM:%d/%m/%Y}")
meta = {dia(r["data"]): float(r["valor"]) for r in json.loads(baixar(url))}

raw = open(TD_CSV, "rb").read() if TD_CSV else baixar(TD_URL)
linhas = []
for r in csv.DictReader(io.StringIO(raw.decode("utf-8-sig")), delimiter=";"):
    if r["Tipo Titulo"] != "Tesouro Prefixado" or r["Data Vencimento"] != VENC:
        continue
    base = dia(r["Data Base"])
    if INI <= base <= FIM:
        linhas.append({"data": base.isoformat(),
                       "taxa_compra": r["Taxa Compra Manha"].replace(",", "."),
                       "pu_compra": r["PU Compra Manha"].replace(",", "."),
                       "meta_selic": f"{meta[base]:.2f}"})
linhas.sort(key=lambda r: r["data"])

os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "graf-02.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0]))
    w.writeheader()
    w.writerows(linhas)

v = {r["data"]: r for r in linhas}
# confere com o texto (04-draft-v2.md) e com 03-pesquisa.md, itens 2 e 8
assert (v["2026-10-13"]["taxa_compra"], v["2026-10-13"]["pu_compra"]) == ("12.40", "773.74")
assert (v["2026-11-17"]["taxa_compra"], v["2026-11-17"]["pu_compra"]) == ("14.98", "746.00")
assert v["2026-10-02"]["taxa_compra"] == "13.83" and v["2026-10-05"]["taxa_compra"] == "12.74"
assert v["2026-10-26"]["taxa_compra"] == "15.40"     # pregão seguinte ao 2º turno (anotação)
assert v["2026-11-04"]["taxa_compra"] == "15.13"     # dia do Copom (anotação)
assert {r["meta_selic"] for r in linhas} == {"13.75"}
assert len(linhas) == 32 and linhas[0]["data"] == "2026-10-01" and linhas[-1]["data"] == "2026-11-17"
print("linhas", len(linhas), linhas[0]["data"], linhas[-1]["data"])
```

**Código Plotly executável** (gera `figuras/graf-02.svg` e `figuras/graf-02.png`):

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
grove_txt = c["grove"]["700"]["$value"]   # nome da série em texto: 4,95:1 sobre Chalk (grove.500 dá 3,16:1)
fam = tokens["typography"]["fontFamily"]


def stack(key):
    # pilha inteira de fallback, com aspas: "Source Sans 3" sem aspas invalida a declaração CSS
    return ", ".join(f'"{n}"' if " " in n else n for n in fam[key]["$value"])


font_display, font_body, font_data = stack("display"), stack("body"), stack("data")


def num(v):
    return f"{v:.2f}".replace(".", ",")


df = pd.read_csv(os.path.join(POST_DIR, "graficos/dados/graf-02.csv"), parse_dates=["data"])
ix = df.set_index("data")
taxa = lambda d: ix.loc[d, "taxa_compra"]
pu = lambda d: num(ix.loc[d, "pu_compra"])
selic = df["meta_selic"].iloc[-1]

fig = go.Figure()
# Meta Selic: contexto, em slate. Parada em 13,75% o período inteiro.
fig.add_trace(go.Scatter(x=df["data"], y=df["meta_selic"], mode="lines", line_shape="hv",
                         line=dict(color=slate, width=2), showlegend=False, hoverinfo="skip"))
# Taxa de compra do Prefixado 2029, um ponto por pregão: o ponto do gráfico, em grove.500.
fig.add_trace(go.Scatter(x=df["data"], y=df["taxa_compra"], mode="lines",
                         line=dict(color=grove, width=2.5), showlegend=False, hoverinfo="skip"))
# Marcadores nos pregões anotados (taxa) e no dia do Copom (meta Selic).
marcados = ["2026-10-02", "2026-10-05", "2026-10-13", "2026-10-26", "2026-11-17"]
fig.add_trace(go.Scatter(x=marcados, y=[taxa(d) for d in marcados], mode="markers", showlegend=False,
                         hoverinfo="skip", marker=dict(color=grove, size=8, line=dict(color=bg, width=1.5))))
fig.add_trace(go.Scatter(x=["2026-11-04"], y=[ix.loc["2026-11-04", "meta_selic"]], mode="markers",
                         showlegend=False, hoverinfo="skip",
                         marker=dict(color=slate, size=8, line=dict(color=bg, width=1.5))))

nota = dict(showarrow=True, arrowhead=0, arrowwidth=1, arrowcolor=ink, axref="x", ayref="y",
            font=dict(color=ink, size=13, family=font_body), bgcolor=bg)
# (ponto, posição do texto em dados, âncoras, texto). Números do CSV; posições testadas para não
# cobrir linha nem outra anotação.
ANOTACOES = [
    ("2026-10-05", taxa("2026-10-05"), "2026-10-06", 14.05, "left", "bottom",
     f"<b>5/10, pregão após o 1º turno</b><br>de {num(taxa('2026-10-02'))}% para "
     f"{num(taxa('2026-10-05'))}% num dia"),
    ("2026-10-13", taxa("2026-10-13"), "2026-10-13", 11.95, "center", "top",
     f"<b>13/10: {num(taxa('2026-10-13'))}%</b><br>R$ {pu('2026-10-13')} por título"),
    ("2026-10-26", taxa("2026-10-26"), "2026-10-25", 15.9, "right", "middle",
     f"<b>26/10, pregão após o 2º turno: {num(taxa('2026-10-26'))}%</b><br>"
     "leilões da semana cancelados,<br>Tesouro Direto suspenso"),
    ("2026-11-04", selic, "2026-11-04", 13.3, "center", "top",
     f"<b>4/11, Copom</b><br>mantém a Selic em {num(selic)}%"),
]
for x, y, ax, ay, xa, ya, txt in ANOTACOES:
    fig.add_annotation(x=x, y=y, ax=ax, ay=ay, xanchor=xa, yanchor=ya, align=xa if xa != "center"
                       else "center", text=txt, **nota)

# Rótulo direto no fim de cada linha (17/11), no lugar de legenda.
fig.add_annotation(x="2026-11-17", y=taxa("2026-11-17"), xanchor="left", xshift=10, showarrow=False,
                   align="left", font=dict(color=ink, size=13, family=font_body),
                   text=f"<b style='color:{grove_txt}'>Prefixado 2029</b><br>"
                        f"<b>17/11: {num(taxa('2026-11-17'))}%</b><br>R$ {pu('2026-11-17')} por título")
fig.add_annotation(x="2026-11-17", y=selic, xanchor="left", xshift=10, showarrow=False, align="left",
                   font=dict(color=slate, size=13, family=font_body),
                   text=f"<b>meta Selic</b><br>{num(selic)}%")

fig.add_annotation(xref="paper", yref="paper", x=0, y=0, yshift=-44, xanchor="left", yanchor="top",
                   showarrow=False, align="left",
                   text="Fonte: Tesouro Nacional, Tesouro Transparente (taxa de compra da manhã do Tesouro "
                        "Prefixado 2029, vencimento em 1º/1/2029);<br>Banco Central, SGS 432 (meta Selic). "
                        "Um ponto por pregão; sem pregão em 12/10 e 2/11. O eixo começa em 11%.",
                   font=dict(color=slate, size=12, family=font_body))

SEG = ["2026-10-05", "2026-10-12", "2026-10-19", "2026-10-26", "2026-11-02", "2026-11-09", "2026-11-16"]
fig.update_xaxes(range=["2026-09-29", "2026-11-18"], tickvals=SEG,
                 ticktext=["5 out", "12 out", "19 out", "26 out", "2 nov", "9 nov", "16 nov"],
                 tickfont=dict(color=slate, size=13, family=font_data),
                 showgrid=False, zeroline=False, showline=False, ticks="")
fig.update_yaxes(range=[11, 16.4], tickvals=[11, 12, 13, 14, 15, 16],
                 ticktext=[f"{v}%" for v in (11, 12, 13, 14, 15, 16)],
                 tickfont=dict(color=slate, size=13, family=font_data),
                 gridcolor=mist, gridwidth=1, zeroline=False, showline=False)
fig.update_layout(
    paper_bgcolor=bg, plot_bgcolor=bg, width=1000, height=620,
    margin=dict(l=60, r=150, t=100, b=100),
    title=dict(text="Com a Selic parada, a taxa do Prefixado 2029 caiu no 1º turno e saltou no 2º<br>"
                    f"<span style='font-size:15px;color:{slate};font-family:{font_body}'>"
                    "taxa de compra no Tesouro Direto e meta Selic, em % ao ano, de 1º/10 a 17/11/2026"
                    "</span>",
               font=dict(color=ink, size=22, family=font_display), x=0.01, xanchor="left",
               y=0.965, yanchor="top"),
    font=dict(family=font_body, color=ink),
)

out_dir = os.path.join(POST_DIR, "figuras")
os.makedirs(out_dir, exist_ok=True)
fig.write_image(os.path.join(out_dir, "graf-02.svg"))
fig.write_image(os.path.join(out_dir, "graf-02.png"), scale=2)
print("ok")
```

**Escolha de tipo:** a taxa diária em linha contra a meta Selic, no mesmo eixo e na mesma unidade: o
ponto é ver a taxa andar mais de um ponto, duas vezes e em sentidos opostos, com a referência parada.
Descartados: (1) o preço (PU) no eixo, que não se compara com a Selic e inverte o sentido (a taxa
sobe, o preço cai); o PU fica nas anotações de 13/10 e 17/11, que o texto cita; (2) barras de
variação diária, que perdem o nível e a distância até a Selic; (3) taxa e preço em dois eixos y, que
criam uma relação visual entre escalas arbitrárias; (4) a anotação do leilão de 8/10 (12,53%), que a
linha já mostra no patamar de 5 a 9/10 e que lotaria o canto esquerdo; (5) ir até 19/11 (ver Dados).

**Anotação:** cinco pontos, com os números lidos do CSV:
- **5/10, pregão após o 1º turno:** de 13,83% (2/10) para 12,74%, com marcador nos dois pregões;
- **13/10:** 12,40%, R$ 773,74 por título;
- **26/10, pregão após o 2º turno:** 15,40%, o pico da série; leilões da semana cancelados e Tesouro
  Direto suspenso (`03-pesquisa.md`, itens 3 e 20). É a taxa da manhã: o CSV não traz o intradia;
- **4/11, Copom mantém a Selic em 13,75%:** a seta aponta para a linha da Selic, porque o evento é
  dela;
- **17/11:** 14,98%, R$ 746,00 por título, no rótulo direto do fim da linha.

As duas séries são identificadas por rótulo direto no fim de cada linha, sem legenda. Posições
conferidas no PNG: nenhum texto cobre linha ou outra anotação; a seta do 1º turno cruza a linha da
Selic, sem cobri-la.

**Gate de Tufte:**
- **Eixo y começa em 11%, não em zero (exceção justificada).** O gráfico compara movimentos em pontos
  percentuais contra uma referência parada, a meta Selic, que está no gráfico e faz o papel de base:
  as distâncias até ela (−1,01 ponto em 5/10, +1,65 em 26/10, +1,23 em 17/11) e os saltos de um pregão
  (−1,09 em 5/10, +2,63 em 26/10) são o assunto. Em renda fixa, um ponto não é pouco: no Prefixado
  2029, vale cerca de 1,8% do preço (*duration* modificada de 1,83, no texto). Com o eixo em zero, a
  faixa de 12,3% a 15,4% ocuparia um quinto da altura, o salto do 1º turno teria cerca de 28 px na
  figura de 1000 × 620 e as anotações se espremeriam numa tira. O nível contra o zero já está no
  `graf-01`, três parágrafos antes, com eixo em zero. Aqui, o tick de 11% fica visível na base e o
  rodapé declara "O eixo começa em 11%".
- **Lie Factor:** sobre a diferença em pontos percentuais, que é o que o gráfico compara, 1,0 (escala
  linear: um ponto tem a mesma altura em todo o eixo). Lido como nível a partir da base do eixo, não
  seria: a alta de 12,40% para 14,98% é +21% na taxa e +184% na altura acima de 11% (fator 8,9). É o
  custo declarado do recorte, e o motivo do aviso no rodapé.
- Duas séries, só uma com cor. A Selic se distingue também por ser reta e por ter rótulo próprio.
- Sem 3D, sombra, textura nem moldura. Grid horizontal em `mist`.
- Eixo x em tempo de calendário: fins de semana e feriados ocupam espaço, e a linha liga um pregão ao
  seguinte (o salto de 23/10 para 26/10 atravessa o fim de semana do 2º turno). O rodapé diz "Um ponto
  por pregão".

**Tokens usados** (de `../../brand/tokens/syntaxis.tokens.json`): `color.neutral.chalk` (fundo,
contorno dos marcadores, fundo das anotações), `color.grove.500` (taxa do Prefixado 2029 e seus
marcadores), `color.grove.700` (o nome "Prefixado 2029" no rótulo direto: 4,95:1 sobre Chalk, contra
3,16:1 do `grove.500`, abaixo dos 4,5:1 que texto de 13 px pede), `color.neutral.slate` (meta Selic e
seu marcador, rótulo da Selic, eixos, subtítulo, rodapé), `color.neutral.ink` (título, anotações,
setas), `color.neutral.mist` (grid); `typography.fontFamily.display` (título), `.body` (subtítulo,
anotações, rótulos, rodapé), `.data` (eixos). Sem `lime`.

**Título no gráfico:** "Com a Selic parada, a taxa do Prefixado 2029 caiu no 1º turno e saltou no 2º"

**Alt-text (o do placeholder `graf-02` em `processo/04-draft-v2.md` serve: bate com a figura; 115
caracteres):**

> Taxa do Prefixado 2029 e meta Selic em out e nov/2026: a taxa cai no 1º turno e salta no 2º, com a Selic em 13,75%.

**Legenda** (a fonte está no rodapé da figura):

> Com a Selic parada em 13,75%, a taxa do Prefixado 2029 caiu mais de um ponto no pregão após o 1º turno e subiu mais de dois no pregão após o 2º.
