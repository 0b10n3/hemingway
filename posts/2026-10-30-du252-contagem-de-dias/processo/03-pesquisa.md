# Etapa 3 — Pesquisa

Laudo do agente `pesquisador-editorial`, gravado pelo pipeline principal. Todas as fontes
acessadas em **30/10/2026**. "Cálculo próprio" = conta do pesquisador, sem fonte de mercado,
a refazer na etapa 7. O pesquisador não executou código: a semântica do `bizdays` vem de
testes, changelog e código-fonte.

**Nota do pipeline principal (execução local, `bizdays` 1.0.19 instalado em diretório isolado
do scratchpad, numpy 2.5.2, pandas 3.0.5):** `cal.bizdays("2026-01-02","2027-01-01")` = 248;
com `following` = 249 (`following("2027-01-01")` = 2027-01-04); exemplo do CDB = 40;
`B3.enddate` = 2026-12-31; `ANBIMA.enddate` = 2099-12-25. Isso confirma a semântica (from, to]
descrita no item 7. A etapa 7 refaz tudo.

---

## 0. Título e subtítulo: "'12% ao ano' quase nunca rende 12% em um ano"

**Série de dias úteis (DU) por ano no calendário ANBIMA** (cálculo próprio a partir das regras
de feriado; corroborações abaixo):

| Ano | DU | Ano | DU | Ano | DU |
|---|---|---|---|---|---|
| 1998 | 249* | 2009 | 250 | 2020 | 251 |
| 1999 | 250* | 2010 | 251 | 2021 | 251 |
| 2000 | 250 | 2011 | 251 | 2022 | 251 |
| 2001 | 250 | 2012 | 251 | 2023 | 249 |
| 2002 | 253 | 2013 | 253 | 2024 | 253 |
| 2003 | 253 | 2014 | 253 | 2025 | 252 |
| 2004 | 252 | 2015 | 250 | 2026 | 249 |
| 2005 | 251 | 2016 | 251 | 2027 | 251 |
| 2006 | 249 | 2017 | 249 | 2028 | 248 |
| 2007 | 250 | 2018 | 250 | 2029 | 249 |
| 2008 | 254 | 2019 | 253 | 2030 | 252 |

\* Em 1998 e 1999 a quinta-feira santa ainda não era dia útil (ver §4).

**Como a série foi obtida e conferida:**
- **2014–2024 corroborados pela suíte de testes do `bizdays`.** As diferenças entre asserts
  consecutivos de `cal.bizdays("2013-08-13", <1º DU de cada ano>)` dão o número de DU de cada
  ano (ex.: 2607 − 2358 = 249 em 2023; 2860 − 2607 = 253 em 2024).
  https://raw.githubusercontent.com/wilsonfreitas/python-bizdays/master/test_bizdays.py
- **2026–2028 conferidos feriado a feriado** contra o `ANBIMA.cal` do pacote
  (https://raw.githubusercontent.com/wilsonfreitas/python-bizdays/master/bizdays/ANBIMA.cal).
  2026 também contra a página oficial da ANBIMA: 13 feriados, 15/11 num domingo
  (https://www.anbima.com.br/feriados/fer_nacionais/2026.asp).
- **Demais anos pela regra:** dias de semana do ano, menos os 4 feriados móveis (sempre em dia
  de semana), menos os fixos em dia de semana; 20/11 a partir de 2024. Em 2000, Sexta-feira
  Santa coincidiu com 21/04.
- **1998 = 249 bate com Garcia**, e só porque a quinta-feira santa (09/04/1998) não era dia
  útil. Pela regra de hoje, 1998 teria 250.

**Números para o "quase nunca":**
- **2001–2030:** só 3 de 30 anos têm exatamente 252 (2004, 2025, 2030). 20 abaixo (rendem
  menos de 12%), 7 acima. Faixa 248–254. Média **251,0**.
- **Regime anterior (8 feriados fixos, até 2023):** 252 só em bissexto que começa numa
  quinta-feira (2004).
- **Regime atual (com 20/11):** 252 em ano comum que começa na terça ou na quarta, ou bissexto
  que começa na quinta: **cerca de 1 ano em 4** (estimativa). O "quase nunca" vale para a
  janela histórica, mas está exagerado olhando para frente.
- **12% a.a. base 252 por número de DU** (cálculo próprio aproximado): 248 → 11,80%;
  249 → 11,85%; 250 → 11,90%; 251 → 11,95%; 252 → 12,00%; 253 → 12,05%; 254 → 12,10%.

---

## 1. Abertura: LTN a 12% de 02/01/2026 a 01/01/2027 entrega 11,85%

- **A conta fecha:** 1,12^(249/252) − 1 ≈ 11,85%; 1,12^(253/252) − 1 ≈ 12,05% (cálculo
  próprio).
- **A LTN jan/2027 existe** como "Tesouro Prefixado 2027", vencimento 01/01/2027 (fontes
  secundárias: https://maisretorno.com/tesouro-direto/tesouro-prefixado-01-01-2027,
  https://investidor10.com.br/tesouro-direto/tesouro-prefixado-2027/). Ficha oficial no
  tesourodireto.com.br não aberta.
- **Pagamento no dia útil seguinte (04/01/2027): confirmação parcial.**
  - B3, *Tesouro Direto – Treinamento de Operações* (ago/2022), trecho da busca: "Resgate – A
    sensibilização do arquivo ocorre no dia do vencimento do título, em casos de fins de
    semana ou feriado, no próximo dia útil". Slide não localizado
    (https://www.b3.com.br/data/files/36/81/7E/8C/533928103A654428AC094EA8/TD%20-%20Operacional%20_treinamento%20para%20distribuidores_.pdf).
  - Código Civil, art. 132, §1º: "Se o dia do vencimento cair em feriado, considerar-se-á
    prorrogado o prazo até o seguinte dia útil" (reprodução secundária:
    https://jurisway.org.br/explica/3/3474; conferir no Planalto).
  - Decreto 11.301/2022 (características dos títulos) não tem regra de dia não útil
    (https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/Decreto/D11301.htm); revogado
    pelo Decreto 12.814/2026, não lido.

---

## 2. "'12% ao ano' de quê?"

- **A B3 confirma a oposição 252 × 360** (Programa de Treinamento DI, módulo "02 - Taxas de
  Juros"): "No Brasil, taxas de juros são baseadas em um ano de 252 dias úteis composto por 12
  meses de 21 dias úteis" e "As taxas de juros no mercado financeiro internacional são
  baseadas em um ano de 360 dias corridos".
  https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/s_di_train_prog/02-taxas-de-juros.htm
- **Contraponto: mesmo em reais, 252 composto é padrão, não regra única.** O Caderno de
  Fórmulas B3 de CDB/DI/LF (atualizado em 28/06/2021) aceita como critério de juros: "252 –
  número de dias úteis"; "252 – Número de meses × 21"; "360 ou 365 – dias corridos"; "360 ou
  365 – meses × 30". Todos **compostos** (pp. 36–44). Apropriação dos pré-fixados "diária, por
  dias úteis ou corridos" (p. 6).
  https://www.b3.com.br:443/data/files/7D/A3/B2/BB/2054A710D25F12A7AC094EA8/CDBs-DIs-DPGE-LAM-LC-LF-LFS-LFSC-LFSN-IECI-RDB.pdf
  Reforça "régua e motor são peças independentes": existe CDB DC/365 composto registrado na B3.

---

## 3. "A régua e o motor"

**Fórmulas oficiais do Fator e do PU**
- **ANBIMA, *Metodologias ANBIMA de Precificação* (05/05/2021), p. 35, LTN:** PU = VN /
  [(Taxa/100 + 1)^(du/252)], VN = R$ 1.000. "du = Dias úteis entre a data de liquidação
  (inclusive) e a data de vencimento". O quadro da LTN **não escreve "(exclusive)"**; os de
  NTN-F (p. 36) e LFT (p. 37) escrevem.
  https://www.anbima.com.br/data/files/5D/92/EC/E7/E82F971013C70F976B2BA2A8/Metodologias-ANBIMA-de-precificacao.pdf
- **Tesouro Nacional, *Methodology for Calculating Federal Government Bonds Offered in Primary
  Auctions* (sem data), p. 3, LTN:** "bd = number of business days between settlement date
  (inclusive) and maturity date (exclusive)". Fonte mais explícita para o
  "inclusive/exclusive".
  https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/27710_1639917/Metodologia_Preços_ingles[1].pdf
- **B3, OC 055/2024-PRE, Anexo I (DI1), p. III:** PO = 100.000 / (1 + i/100)^(n/252); "n =
  número de Dias Úteis compreendidos no período entre a data da operação, inclusive, e a data
  de vencimento do contrato, exclusive". Confirma os 100.000 pontos.

**Truncamento (para a "Nota de rigor")**
- ANBIMA p. 32, LTN: taxa T-4/I-4; "Exponencial de Dias" T-14; PU T-6/I-6; Valor Financeiro T-2
  (T = truncado, I = informado). O exemplo do Tesouro (p. 3) usa os mesmos níveis.
- **Consenso:** ANBIMA, Tesouro e B3 usam DU/252 composto, liquidação inclusive, vencimento
  exclusive. Sem divergência.

---

## 4. "Por que o relógio para no sábado"

**O DI é de um dia útil**
- B3, *Metodologia de Apuração da Taxa DI*: operações de DI pré-fixados "pactuadas por um dia
  útil e registradas e liquidadas pelo sistema B3", só "entre instituições de conglomerados
  diferentes".
  https://b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/di/metodologia-de-apuracao-da-taxa/
- Mesma página, procedimento de **"datas especiais"**: em torno de feriados, "o mercado negocia
  a taxa DI para 1 e/ou 2 overs"; no exemplo de 24/12 a B3 agrega operações de 1 DU e de 2 DU
  convertidas para um over. Sustenta "uma diária cobrindo sexta, sábado e domingo".
- DI1 (OC 055/2024-PRE, pp. III–IV): FC = (1 + DI)^(1/252) com 1 dia útil entre sessões;
  produtório das Taxas DI quando há mais de um. Fim de semana não gera DI.

**Circular BCB nº 2.761 (texto oficial lido)**
- Data **18/06/1997**. Art. 1º: Selic "expressa sob a forma anual, com 2 (duas) casas
  decimais", expoente 252. Art. 2º: TBC e TBAN "na forma de taxa efetiva anualizada [...]
  considerando-se 252 (duzentos e cinqüenta e dois) dias úteis para o ano". Art. 4º:
  "surtindo efeito a partir de 01.01.98". Assinada por Francisco Lafaiete de Pádua Lopes.
  https://www.bcb.gov.br/pre/normativos/circ/1997/pdf/circ_2761_v1_o.pdf
- **Nuance de vigência:** Circular nº 2.780, de 12/11/1997, art. 4º: "produzindo efeito a
  partir de 02.01.98, inclusive, data em que produzirá efeito, também, a Circular nº 2.761"
  (02/01 era o primeiro dia útil de 1998).
  https://www.bcb.gov.br/pre/normativos/circ/1997/pdf/circ_2780_v1_o.pdf

**O 252 sobreviveu à norma que o criou**
- Art. 1º da 2.761 revogado pela Circular 3.671/2013 (base secundária:
  https://okai.com.br/documento/2013-10-18/circular-nº-3-671).
- Hoje: **Resolução BCB nº 46, de 24/11/2020**, art. 2º: "A Taxa Selic, expressa sob a forma
  anual, em termos percentuais, considerando a **convenção** de 252 (duzentos e cinquenta e
  dois) dias úteis" (via https://www.legisweb.com.br/legislacao/?id=404871; conferir no BCB).
- **O próprio BC chama o 252 de "convenção".** Sustenta "252 é uma convenção, não uma
  contagem".

**"Até 1997, a Selic era expressa ao mês"**
- Garcia: "as taxas tornaram-se mensalizadas no Brasil devido à megainflação; nada mais
  natural, portanto, que voltem a ser cotadas em termos anuais". A 2.761 "altera a forma de
  expressão". Texto normativo anterior (forma mensal) não localizado.

**Márcio G. P. Garcia, "Efeitos da anualização da taxa Selic"** (30/06/1997, Depto. de
Economia da PUC-Rio; lido na íntegra:
https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf)
- p. 5, item b, **literal**: "1998 tem 249 dias úteis, enquanto a fórmula do BC usa 252 dias
  úteis. Isto, obviamente, tem que ser levado em conta nos fluxos de caixa dos ativos."
  **Confirmado.**
- Crítica de época: p. 2, com taxa fixa por dia útil, "Fevereiro, com apenas 18 dias úteis,
  teria uma taxa de 1,42%; enquanto julho, com 23 dias úteis, teria uma taxa de 1,82%"; p. 4,
  a medida "afeta fluxos de caixa" e "o número de dias corridos é o que determina o custo de
  oportunidade do dinheiro nos mercados estrangeiros" (antecipa a tensão do cupom cambial);
  p. 4, "A medida do BC não alterou os princípios da matemática financeira."

**Por que 1998 tinha 249**
- Resolução CMN nº 2.516, de 29/06/1998, art. 1º: não são dias úteis sábados, domingos,
  feriados nacionais, segunda e terça de Carnaval, Corpus Christi e 02/11. Parágrafo único:
  "A Quinta-Feira da Semana Santa será considerada dia útil somente a partir do ano 2000."
  https://www.bcb.gov.br/pre/normativos/res/1998/pdf/res_2516_v2_P.pdf

**"12 meses de 21 dias úteis"**: na página do treinamento DI (§2). "Meses × 21" também é
critério contratual de CDB no Caderno B3 (pp. 37–40): (1 + i)^(NºMeses×21/252).

---

## 5. "Quanto custa a régua errada" (graf-02)

**Conferência do exemplo do CDB** (cálculo próprio, calendário ANBIMA 2026)
- 01/10 a 01/12/2026: 61 dias corridos; 43 dias de semana em [01/10, 01/12); menos 12/10
  (segunda), 02/11 (segunda) e 20/11 (sexta) = 40 DU.
- Fatores batem: 1,12^(40/252) ≈ 1,0181515; 1,12^(61/365) ≈ 1,019120; 1,12^(61/360) ≈
  1,019389; linear 1,0203333. Taxas equivalentes 11,36%, 11,20%, 10,71% batem. Com 43 DU, o
  resgate sai cerca de R$ 137 acima.
- **As linhas DC/365 e DC/360 compostas não são hipotéticas:** são critérios que a B3 aceita
  para registrar CDB (Caderno, pp. 40–41). Um sistema que ignora o critério cadastrado erra
  exatamente assim.
- Tese "Errado é ler um número com a régua do outro": o treinamento B3 traz a tabela de bases
  (360, 365, 252). As quatro taxas equivalentes são cálculo do autor, declarado como tal.

---

## 6. "ANBIMA ou B3? Duas perguntas diferentes" (diag-01)

**Resolução CMN nº 4.880, de 23/12/2020** (DOU 24/12/2020; vigência 01/03/2021; texto via
https://www.normaslegais.com.br/legislacao/resolucao-cmn-4880-2020.htm)
- **Art. 6º:** não são dias úteis "para operações do mercado financeiro e para prestação de
  informações ao Banco Central" sábados, domingos e feriados nacionais, mais: I – segunda e
  terça de Carnaval; II – Corpus Christi. **Lista do rascunho correta.**
- **Art. 3º:** "Não haverá atendimento presencial no último dia útil do ano", admitidas só
  operações entre as instituições do art. 1º. Fala em "atendimento presencial", não "agências
  fechadas", e chama o dia de "último **dia útil** do ano".
- Feriados estaduais e municipais não são dia não útil; "festividades locais" só como hipótese
  de horário especial (art. 2º, §1º, II).
- **Art. 9º revoga** Res. 2.932/2002, Res. 3.180/2004 e o art. 17 da Res. 4.072/2012.
- Linhagem: Res. 1.774/1990 → 2.516/1998 → 2.932/2002 → 4.880/2020 (elo 2.516 → 2.932 via Res.
  2.875/2001, só em fonte secundária).
- **Link do rascunho** (bcb.gov.br/estabilidadefinanceira/exibenormativo?...) renderiza em
  JavaScript; a ferramenta só recebeu o título. A etapa 7 abre no navegador.

**ANBIMA, página de feriados** (https://www.anbima.com.br/feriados/feriados.asp): feriados
nacionais **de 2001 a 2099**, planilha Feriados.xls; exclui municipais, eleições e o último
dia do ano. **Critério declarado:** "feriados em que não há sensibilização das Reservas
Bancárias" (a definição operacional de "o juro correu hoje?").

**Lei nº 14.759, de 21/12/2023** (DOU 22/12/2023, Seção 1, p. 1): art. 1º, 20 de novembro
feriado nacional (Dia Nacional de Zumbi e da Consciência Negra); art. 2º, vigência na
publicação. Primeiro 20/11 nacional: 2024.
https://www2.camara.leg.br/legin/fed/lei/2023/lei-14759-21-dezembro-2023-795091-publicacaooriginal-170522-pl.html

**B3 nos feriados paulistas a partir de 2022**
- CE 109/2021-VNC (28/10/2021): "Conforme divulgado no Ofício Circular 150/2020-PRE, de
  17/11/2020 [...] em 2022, no feriado municipal em São Paulo, haverá (i) negociação [...]".
  https://b3.com.br/data/files/D5/F2/DA/8F/32535810F534EB48AC094EA8/CE%20109-2021-VNC%20Calendario%20de%20feriados%202022_F_REVISADO_F%20_004__RR.pdf
- OC 041/2026-VNC repete: "desde o calendário de 2022, em relação aos feriados em São Paulo"
  (Quadro B: 09/07/2026 com funcionamento normal). OC 150/2020-PRE não aberto.
- "Até 2021 a B3 fechava em 25/01, 09/07 e 20/11": notícias
  (https://monitormercantil.com.br/b3-funciona-normalmente/) e a própria mudança. Em 2022,
  09/07 e 20/11 caíram em fim de semana.

**Calendário B3 de 2026** — **OC 041/2026-VNC (errata), 30/06/2026**, revoga o OC
003/2026-VNC (08/01/2026); a errata só tira 03/07 do quadro do CSD2.
https://www.b3.com.br/data/files/20/57/01/AA/06A1F910ADC36BE9AC094EA8/OC%20041-2026-VNC%20ERRATA%20-%20CALENDARIO%20DE%20FERIADOS%20EM%202026_PT.pdf
- 24/12 (quinta): "Véspera de Natal (expediente interno nas instituições bancárias sem sessão
  de negociação, mas com processo de alocação de registros de Balcão [...])".
- 31/12 (quinta): "Expediente interno nas instituições bancárias (sem sessão de negociação
  [...])". Balcão até 13h nos dois dias.
- **14 dias de semana sem pregão** em 2026 (12 feriados nacionais em dia útil + 24/12 + 31/12),
  como no `B3.cal` do pacote.

**DI apurado em 24/12 e 31/12:** séries SGS 12 (CDI, % a.d.) e SGS 11 (Selic) do BCB têm valor
em 24/12/2024 e 31/12/2024 (0,045513 nas duas). **Confirma "a taxa DI é apurada e o juro
corre".**
https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial=20/12/2024&dataFinal=06/01/2025

**Dezembro de 2026** (cálculo próprio, dados do diag-01): 23 dias de semana; menos 25/12 =
**22 DU ANBIMA**; menos 24/12 e 31/12 = **20 pregões**.
- Dia útil e pregão: 1–4, 7–11, 14–18, 21–23, 28–30.
- Dia útil sem pregão: 24 e 31.
- Nem um nem outro: 5, 6, 12, 13, 19, 20, 25, 26, 27.
- "Cerca de R$ 90": 100.000 × (1,12^(2/252) − 1) ≈ R$ 89,98.

**OC 055/2024-PRE** (16/04/2024; assunto "Adequação dos Contratos de Derivativos Listados ao
Tratamento de Feriado Extraordinário – Contratos de Juros"; DI1 no Anexo I)
https://www.b3.com.br/data/files/FF/C5/51/86/158EE810C54843E8DC0D8AA8/OC%20055-2024%20PRE%20Contratos%20FE%20-%20Juros%20(PT).pdf
- p. II, literal: "'Dia Útil' o dia para fins de operações praticadas no mercado financeiro
  nacional, de acordo com o significado atribuído na Resolução 4.880 [...]; e (ii) 'Dia de
  Sessão de Negociação', quaisquer dos dias em que houver sessão de negociação na B3".
- p. III, item ii: "Quando houver mais de um Dia Útil entre a última sessão de negociação e o
  dia do ajuste [...] o fator de correção representará a acumulação de todas as Taxas DI
  divulgadas". **Confirmado.**
- **A mais:** o vencimento do DI1 é o "Primeiro Dia de Sessão de Negociação" do mês (p. I). A B3
  usa o próprio calendário para a data e o bancário para os juros.

---

## 7. "Na prática: Python sem cair em armadilhas"

### `numpy.busday_count`
- NumPy v2.5: "Counts the number of valid days between begindates and enddates, not including
  the day of enddates". Defaults: weekmask '1111100', holidays []. Início incluído, fim
  excluído. https://numpy.org/doc/stable/reference/generated/numpy.busday_count.html
- O **43** bate com a contagem de dias de semana.

### `pandas`
- `date_range(..., inclusive=...)`: "both", "neither", "left", "right"; default "both" (pandas
  3.1.0: https://pandas.pydata.org/docs/reference/api/pandas.date_range.html). `inclusive`
  substituiu `closed` no 1.4.0 (PR #43504: https://github.com/pandas-dev/pandas/pull/43504).
- `CustomBusinessDay(weekmask='Mon Tue Wed Thu Fri', holidays=None, calendar=None)`; feriados
  vão para `numpy.busdaycalendar`.
  https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html
- `bdate_range`: freq default 'B'; holidays e weekmask "only used when custom frequency strings
  are passed" (https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html). Com 'B',
  feriados não valem (pode dar erro; a etapa 7 testa).
- A lista `feriados_2026` do Caminho B **é idêntica** aos 13 feriados ANBIMA de 2026, inclusive
  15/11 (domingo, sem efeito).

### `bizdays` (Wilson Freitas)
- **Versão:** PyPI mostra **1.0.19, de 04/01/2026, ainda a mais recente** (1.0.18 em
  03/01/2026; 1.0.16 em 05/01/2025). https://pypi.org/project/bizdays/
- **CHANGELOG:** 1.0.18 "Updated B3.cal with 2026's holidays"; 1.0.19 reestrutura o pacote e
  instala os .cal junto; 1.0.13 corrige a issue #47; 1.0.11 (29/12/2023) "ANBIMA calendar
  updated with new holiday nov-20th".
  https://raw.githubusercontent.com/wilsonfreitas/python-bizdays/master/CHANGELOG.md
- **Início e fim dos calendários:** `B3.cal` 2000-01-01 a **2026-12-31** (14 feriados de 2026
  batem com o OC 041/2026-VNC; nenhuma data de 2027). `ANBIMA.cal` 2000-01-01 a
  **2099-12-25** (20/11 de 2024 em diante). Sem datas explícitas, `startdate`/`enddate` =
  mínimo e máximo dos feriados do arquivo. Fora do intervalo: `DateOutOfRange` ("Given date
  out of calendar range").
  - **Divergência de documentação:** https://wilsonfreitas.github.io/python-bizdays/calendars.html
    diz ANBIMA até **2078-12-25**; parece desatualizada (o .cal e a ANBIMA vão até 2099).
- **Semântica de `Calendar.bizdays(from, to)` (ponto crítico):**
  - A documentação (quick.html) não diz quais pontas conta.
  - **Os testes mostram que exclui a data inicial e inclui a final:**
    `cal.bizdays("2013-01-02", "2013-01-05") == 2`, com 05/01/2013 num sábado ([início, fim)
    daria 3; (início, fim] dá 2). O código confirma.
  - Pela regra da issue #47, quando `from` não é dia útil o resultado cai em 1. Testes:
    `bizdays("2013-01-01","2013-01-31") == 21` (janeiro de 2013 tinha 22 DU depois do dia 1º) e
    `bizdays("2013-01-01","2014-01-01") == 252` (2013 teve 253 DU). Issue #47:
    https://github.com/wilsonfreitas/python-bizdays/issues/47 (aberta e fechada em 12/02/2024).
  - **Consequências para o rascunho:** `bizdays("2026-01-02","2027-01-01")` = DU em
    (02/01/2026, 01/01/2027] = 05/01 a 31/12/2026 = **248**; com `following` (04/01/2027),
    248 + 1 = **249**. Os números são coerentes com essa semântica, mas **a explicação não é**:
    31/12/2026 entra nas duas contagens; o dia que falta no 248 é **02/01/2026**, que a função
    exclui e nada compensa, porque a ponta final é feriado. Pela convenção de mercado
    ([liquidação, vencimento)), contar direto até 01/01/2027 já dá 249: a armadilha é da
    biblioteca, não da convenção. O comentário do Caminho A ("inclui a aplicação, exclui o
    vencimento") descreve o contrário do que a função faz; a contagem só sai igual porque
    01/10 e 01/12/2026 são dias úteis.
- **Código Civil, art. 132, caput** ("computam-se os prazos, excluído o dia do começo, e
  incluído o do vencimento"; fonte secundária, conferir no Planalto): a mesma regra de pontas
  do `bizdays`, oposta à convenção financeira.
- **Remédio para a Armadilha 4 (não verificado):** o `bizdays` carrega calendários do
  `pandas_market_calendars` com prefixo `PMC/`, inclusive B3; não conferido até quando vai.

---

## 8. "Outros relógios"

**EUA**
- Slides de curso baseados em Hull, cap. 6, "Interest Rate Futures" (FIU): "Treasury Bonds:
  Actual/Actual; T-bills and Money Market Instruments: Actual/360; Corporate and Municipal
  Bonds: 30/360". https://faculty.fiu.edu/~dupoyetb/Financial_Risk_Mgt/lectures/Ch06.pdf
- Exemplos mostram acúmulo **linear dentro do período** (Treasury "$4 × (31/184)"; T-bill
  "$100 × 0,08 × (48/360)"). **"Todos com acúmulo linear dentro de cada período" está correto
  para juros acumulados.** Ressalvas: o yield de bonds compõe semestralmente entre períodos;
  T-bills são cotadas em base de desconto. Paralelo do slide: com Actual/360, "the interest
  earned in an entire year is 365/360 times the quoted rate".
- Livro não lido; a seção 6.1 é "Day Count and Quotation Conventions" pelo sumário da 11ª ed.

**Tabela do treinamento DI da B3:** além de 360 (30/360 aproximado, dc/360 correto) e 252
(du/252), **também tem a base 365 (30/365, dc/365)**. O rascunho cita só 360 e 252.

**Cupom cambial**
- DDI: "Taxa de juro, expressa em percentual ao ano, **linear, base 360 dias corridos**, com até
  três casas decimais"; vencimento no 1º dia útil do mês; DI acumulado da operação (inclusive)
  ao vencimento (exclusive).
  https://b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/futuro-de-cupom-cambial-de-depositos-interfinanceiros-de-um-dia.htm
- FRC: "linear, base 360 dias corridos, com até duas casas decimais"; combinação de duas pontas
  de DDI.
  https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/operacoes-estruturadas-de-forward-rate-agreement-de-cupom-cambial.htm
- **"Dois relógios no mesmo prédio" sustentado**, reforçado pelo CE 006/2024-VPC (§10): o 20/11
  tirou um dia de accrual das curvas em dias úteis e não mexeu no "cupom de uma taxa de
  câmbio".

**Opções sobre ações, novembro de 2026**
- Calendário de vencimentos da B3: **19/11/2026** para opções sobre ações e 18/11/2026 para
  Ibovespa.
  https://www.b3.com.br/pt_br/solucoes/plataformas/puma-trading-system/para-participantes-e-traders/calendario-de-negociacao/vencimentos/calendario-de-vencimentos-de-opcoes-sobre-acoes-e-indices/
  Ressalva: a ferramenta parece ter trocado rótulos em jan–mar; novembro está consistente. A
  etapa 7 confere visualmente.
- **Regra de antecipação em texto contratual:** OC 006/2026-VPC (05/02/2026), opções
  *semanais* sobre ação: "Caso esse dia não seja Dia de Sessão de Negociação, o vencimento
  ocorrerá na data imediatamente anterior em que houver sessão de negociação". Mesmo ofício
  define Dia Útil pela CMN 4.880.
  https://www.b3.com.br/data/files/D7/A3/54/6B/45E2C91076A8EEB9AC094EA8/OC%20006-2026-VPC%20ALTERACOES%20CONTRATOS%20OPCAO%20DE%20COMPRA%20E%20VENDA%20VENCIMENTOS%20SEMANAIS%20ACAO%20UNIT%20ETF%20BDR_PT.pdf
- Contrato das opções mensais não aberto. Vencimento na terceira sexta desde maio de 2021
  (antes, terceira segunda), segundo notícias (ex.: https://www.suno.com.br/noticias/?p=139723).
- **Contraste:** em **Feriado Extraordinário** (fora do calendário), o DI1 tem o vencimento
  **postergado** para a sessão seguinte (OC 055/2024-PRE, p. V). Na B3, a rolagem não tem
  direção única: depende do contrato e do tipo de feriado.

---

## 9. "Antes de perguntar quanto rende" (as quatro perguntas)

- Âncora primária por pergunta: contagem → treinamento B3; regime → Caderno B3 e Hull;
  calendário → CMN 4.880 e OC 041/2026-VNC; pontas → Tesouro (liquidação inclusive, vencimento
  exclusive), OC 055/2024-PRE, numpy, testes do `bizdays`.
- **Achado para a pergunta 4:** convivem duas regras de pontas com respaldo próprio. Código
  Civil: exclui o começo, inclui o vencimento. Convenção financeira: inclui a liquidação,
  exclui o vencimento. Dão o mesmo número com as duas pontas em dia útil e se separam quando
  uma cai em feriado.

---

## 10. Contrapontos e o que ninguém está dizendo

**Contrapontos**
1. **"DU/252 composto" é padrão, não lei, nem para CDB.** A B3 registra CDB em DC/360, DC/365,
   meses×30 e meses×21 (Caderno, pp. 36–44). O "o contratado" do rascunho já contorna isso.
2. **"Quase nunca rende 12%":** 3 de 30 anos em 2001–2030, mas cerca de 1 em 4 no regime atual.
3. **Crítica de época ao 252 fixo (Garcia, 1997):** "volatilidade" mensal artificial e
   conhecida de antemão (fevereiro × julho), efeito em fluxos de caixa, assimetria com o custo
   de oportunidade estrangeiro em dias corridos. **Nenhum debate recente** propondo trocar o 252
   pelos DU efetivos foi encontrado (silêncio, não evidência de consenso).
4. **Caso público de erro de calendário com ressarcimento:** nenhum encontrado. Os casos
   documentados são ajustes regulatórios planejados (itens 3 e 4 abaixo).

**O que ninguém está dizendo**
1. **O 252 está acima da média.** Média 2001–2030: 251,0 DU/ano. No regime com 20/11, média de
   longo prazo em torno de **250,5**: "12% a.a. base 252" rende em média cerca de **11,92%** por
   ano civil (cálculo próprio). Nos EUA, Actual/360 rende 365/360 da taxa num ano (slides de
   Hull). Nos dois mercados "ao ano" não quer dizer "por ano civil", com vieses de sinal
   oposto.
2. **O 20/11 deixou o 252 mais frequente e a média mais baixa.** Antes de 2024, só 2004 teve
   252; depois, 2025, 2030 e cerca de 1 em 4 anos.
3. **Feriado novo transfere dinheiro.**
   - CE 006/2024-VPC (08/02/2024): instrumentos "em base de 252 dias [...] serão impactados pelo
     feriado"; em base 360/365, "não sofrerão impactos"; contratos em dias úteis "terão 01 dia
     a menos de *accrual*".
     https://www.b3.com.br/data/files/34/E1/2E/AD/D0A8D8103152D4C8AC094EA8/CE%20006-2024-VPC%20Feriado%2020_nov_vfinal.pdf
   - CE 013/2024-VPC (04/04/2024): a B3 recalculou a taxa dos CDB/DI do "Registro Simplificado
     Prefixado Final", preservando o valor de resgate.
     https://www.b3.com.br/data/files/AC/52/46/F9/E6AAE8100E866AE8AC094EA8/CE%20013-2024-VPC%20Feriado%2020Nov_Calculo%20das%20taxas_v02.pdf
   - OC 207/2023-PRE (07/12/2023): o ajuste dos futuros liquidado em D+2 "terá o impacto
     financeiro da mudança na contagem de dias úteis até vencimento causado pela diferença de
     calendários entre D+0 e D+1".
     https://www.b3.com.br/data/files/75/C1/52/35/F854C810719CE3C8DC0D8AA8/OC%20207-2023-PRE%20Procedimentos%20para%20Tratamento%20de%20Novo%20Feriado%20Nacional%20no%20Dia%2020%20de%20Novembro%20(PT).pdf
4. **As regras do calendário também mudam:** quinta-feira santa deixa de ser feriado em 2000
   (Res. 2.516/1998); 20/11 entra em 2024. "O calendário tem data de validade" vale para as
   regras, não só para o arquivo.
5. **O calendário B3 vive um ano à frente porque a B3 só o publica um ano à frente.** OC
   054/2025-VNC (calendário de 2026) é de 04/12/2025. O `B3.cal` é atualizado todo janeiro
   (1.0.10, 1.0.16, 1.0.18). A ANBIMA publica até 2099.
6. **Há contrato em que "12% ao ano" rende exatamente 12% em 12 meses:** CDB no critério "meses
   × 21", expoente 12×21/252 = 1 (Caderno B3, p. 37). É a frase da B3 "12 meses de 21 dias
   úteis" virando cláusula.

---

## 11. Teste de transferência (Ficha, campo 2): CDB a 100% do CDI

- **Caderno B3, §6.1 (pp. 47–48):** Fator DI = Π (1 + TDIk × p/100), TDIk = (DIk/100 + 1)^(1/252)
  − 1; período "da data de emissão [...] inclusive, até a data de [...] vencimento, exclusive";
  fator diário com 16 casas (truncado a cada passo); Fator DI arredondado em 8 casas. Serve
  para validar a resposta esperada do leitor.
- **CET (alternativa da Ficha):** não pesquisado.

---

## 12. Bibliografia (§5.7: 3–4 itens, mínimo de 2 livros)

**Em nenhum livro brasileiro há sumário que confirme, capítulo a capítulo, a cobertura de
DU/252.** Nenhum capítulo ou página indicado sem conferência.

| Livro | Dados conferidos | O que cobre (evidência) | Em catálogo? |
|---|---|---|---|
| José Roberto Securato (org.), *Cálculo Financeiro das Tesourarias: Bancos e Empresas* | 5ª ed., Saint Paul, 2015, ISBN 9788580041149, 544 p. | Sinopse: formação de preços de títulos públicos, carregamento, duration. DU/252 não confirmado por sumário. | Contraditório ("esgotado" × "sob encomenda"). https://www.martinsfontespaulista.com.br/calculo-financeiro-das-tesourarias-768937/p |
| Alexandre Assaf Neto, *Mercado Financeiro* | 16ª ed., GEN Atlas, 2025, ISBN 9786559776719, 408 p. | Sinopse: instituições, operações, marcação a mercado. DU/252 não confirmado. | Sob encomenda. https://www.martinsfontespaulista.com.br/mercado-financeiro-1127643/p |
| Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações* | 15ª ed., GEN Atlas, 2022, ISBN 9786559773237, 312 p. | Sinopse genérica. Taxa over e DU não confirmados. | Sob encomenda. https://www.martinsfontespaulista.com.br/matematica-financeira-e-suas-aplicacoes-1004941/p |
| Armando José Tosi, *Matemática Financeira com Ênfase em Produtos Bancários* | 4ª ed., GEN Atlas, 2015, ISBN 9788522498925, 368 p. | Sinopse cita CDI, Selic, Cetip e "taxa over". | Sob encomenda. https://www.martinsfontespaulista.com.br/matematica-financeira-com-enfase-em-produtos-bancarios-762375/p |
| Eduardo Fortuna, *Mercado Financeiro: Produtos e Serviços* | Última edição confirmada: 21ª, Qualitymark, 2018, 904 p. ISBN e edições posteriores não confirmados. | Panorama de produtos. DU/252 não confirmado. | ? https://www.jornaldocomercio.com/_conteudo/2018/05/cadernos/empresas_e_negocios/628679-mercado.html |
| John C. Hull, *Options, Futures, and Other Derivatives* | 11th ed., Pearson, 2021, ISBN 9780136939979 (Global 9781292410654). Em português: *Opções, Futuros e Outros Derivativos*, 9ª ed., Bookman, 2016, ISBN 9788582603925 (só via Buscapé). | Cap. 6, §6.1 "Day Count and Quotation Conventions" (sumário; conteúdo via slides derivados). | Sim (Pearson). https://www.pearson.com/store/p/options-futures-and-other-derivatives/P200000005938/9780136939979 ; https://www.buscape.com.br/livros/opcoes-futuros-e-outros-derivativos-9-ed-2016-hull-john-c-9788582603925 |
| Frank J. Fabozzi e Francesco A. Fabozzi, *Bond Markets, Analysis, and Strategies* | 10ª ed., 2021; catálogo de biblioteca dá **MIT Press**, não Pearson. | Capítulo de day count não confirmado. | ? https://library.cbr.ru/catalog/lib/books/588403/ |
| CVM/B3, *Livro TOP: Mercado de Derivativos no Brasil – Conceitos, Produtos e Operações* | 2ª ed., dez/2025 (1ª em 2015), gratuito. | Seis capítulos, derivativos de juros e câmbio. DI1/DDI não confirmados pelo nome. | Gratuito; página gov.br deu 404. https://legismap.com.br/conteudos/artigos-e-noticias/cvm-lanca-2-edicao-do-livro-top-mercado-de-derivativos-no-brasil-conceitos-produtos-e-operacoes |
| Octavio Bessada, C. Barbedo, G. Araújo, *Mercado de Derivativos no Brasil* | Record; edição e ano não confirmados. | DI futuro e DDI, pela ementa da PUC-Rio. | ? |

**Leitura do pesquisador:** evidência mais direta de cobertura: Hull (day count, internacional)
e Tosi (taxa over, produtos bancários brasileiros). Securato é o mais "tesouraria", sem sumário.

**Conferência dos 7 links do "Para ir além":** ANBIMA OK (05/05/2021, fórmulas e truncamento;
versão mais nova não verificada); treinamento B3 OK; OC 055/2024-PRE OK; Garcia OK; PyPI OK;
pandas OK; CMN 4.880 (BCB) não carregou na ferramenta, abrir no navegador.

---

## Divergências com o rascunho

1. **`bizdays` e as pontas.** "Inclui a aplicação, exclui o vencimento" (Caminho A) contraria o
   comportamento real: a função exclui `from` e inclui `to` (teste
   `bizdays("2013-01-02","2013-01-05") == 2`; código-fonte; execução local do pipeline). 248,
   249 e 40 batem. Na Armadilha 3, "porque 31 de dezembro conta" está errado: 31/12 entra nas
   duas contagens; o que falta no 248 é 02/01/2026. Pela convenção de mercado, até 01/01/2027
   já dá 249. Segunda armadilha não mencionada: com `from` em feriado, o resultado cai em 1
   (`bizdays("2013-01-01","2014-01-01") == 252`, embora 2013 tenha tido 253 DU).
2. **ANBIMA no `bizdays` até 2099-12-25.** Bate com o `.cal` e a ANBIMA; a documentação do
   pacote diz 2078-12-25.
3. **Vigência da Circular 2.761.** "A partir de 1º de janeiro de 1998" é o art. 4º; a Circular
   2.780/1997 fixou efeito "a partir de 02.01.98, inclusive". Nuance, não erro.
4. **Garcia e os 249 de 1998.** Confirmado palavra por palavra (p. 5), pela regra da época
   (quinta-feira santa feriado, Res. 2.516/1998). Pela regra de hoje, 1998 teria 250.
5. **"Quase nunca rende 12%".** 3 de 30 anos em 2001–2030 sustentam; no calendário atual, cerca
   de 1 em 4 anos.
6. **"Na renda fixa brasileira [...] CDB, debêntures [...] a combinação é DU/252 composto".**
   Padrão, não regra: a B3 aceita CDB em DC/360, DC/365 e meses×30/×21.
7. **LTN paga em 04/01/2027.** Sustentada só por trecho de treinamento da B3 (slide não
   localizado) e pelo Código Civil, art. 132, §1º. Sem texto do Tesouro.
8. **Tabela do treinamento DI da B3** também tem base 365; o rascunho cita só 360 e 252.
9. **"No último dia útil, as agências não abrem ao público".** A CMN 4.880 diz "não haverá
   atendimento presencial". Nuance de redação.
10. **"Inclusive/exclusive" na ANBIMA.** O quadro da LTN não escreve "(exclusive)"; NTN-F e LFT
    escrevem. Fonte explícita para a LTN: metodologia do Tesouro; para o DI1: OC 055/2024-PRE.
11. **Vencimento de opções em 19/11/2026.** Data confirmada; regra de antecipação conferida no
    contrato de opções *semanais* (OC 006/2026-VPC); mensais não abertas.
12. **Link da CMN 4.880 no BCB** não carregou na ferramenta; texto conferido em cópia
    (normaslegais). A etapa 7 abre no navegador.

PDFs baixados nesta etapa (Circulares 2.761 e 2.780, Res. 2.516, OCs B3, Caderno de Fórmulas,
metodologia ANBIMA) ficaram no diretório `tool-results/` da sessão, fora do repositório.
