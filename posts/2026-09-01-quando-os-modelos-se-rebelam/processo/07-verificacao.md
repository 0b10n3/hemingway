# Verificação técnica — rodada 4

Laudo do subagente de verificação técnica, etapa 7, sobre `04-draft-v1.md` (draft desta
rodada). Metodologia: `WebSearch`/`WebFetch` para achar a fonte primária, `curl` + `pdftotext`
para ler PDFs de fonte primária diretamente (não aceitar resumo de busca como fato fechado),
`python3` para todo recálculo. Onde `03-pesquisa.md` já tinha achado sólido com fonte
primária lida na íntegra, refiz a checagem eu mesmo em vez de aceitar o achado — nos dois
casos abaixo (Kempthorne, target forward) a checagem foi refeita do zero. Onde rodadas
anteriores desta mesma etapa (commits `d452528`, `eb25b13`, `7ef1cf3`) já tinham lido a fonte
primária na íntegra contra um estado de draft diferente, cruzei o achado antigo com o texto
atual e, nos pontos numéricos centrais (LTCM, Kempthorne), refiz a leitura da fonte primária
eu mesmo — não herdei nenhum veredito sem conferir.

---

## 1. A citação de abertura — atribuída a "Peter Kempthorne" no corpo do draft

**Veredito: ❌ Atribuição não se sustenta — confirmado de novo, de forma definitiva, nesta
rodada. Recomendo remover o nome próprio do corpo do texto.**

Refiz a checagem inteira, independente das três rodadas anteriores:

- `WebFetch` direto na página oficial do MIT OCW da aula referenciada (18.S096, Fall 2013,
  *Lecture 3: Probability Theory*) — a página declara explicitamente "Instructor: Dr.
  Choongbum Lee", não Kempthorne.
  [ocw.mit.edu/.../lecture-3-probability-theory](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-3-probability-theory/),
  acesso 02/09/2026.
- Fui além das rodadas anteriores e li a **página de calendário oficial do curso inteiro**
  ([ocw.mit.edu/.../pages/calendar](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/calendar/)),
  que lista instrutor por aula das 26 aulas do curso. Kempthorne aparece como instrutor único
  das aulas 6 (Regression Analysis), 8 (Time Series I), 9 (Volatility Modeling), 11-12 (Time
  Series II-III), 14 (Portfolio Theory) e 15 (Factor Modeling) — nunca da aula 3 (Probability
  Theory), que é de Choongbum Lee. Isto é uma fonte ainda mais forte do que a verificação
  aula-a-aula das rodadas anteriores: é a tabela oficial do MIT que resolve a questão de
  autoria de forma definitiva, não inferência lecture a lecture.
- Rodadas anteriores (ver `eb25b13`, `7ef1cf3` no histórico deste arquivo) já tinham baixado
  a legenda/transcrição real de até cinco aulas candidatas (2013 Lecture 3; 2024 Lectures 4-5,
  6, 8, 9, 12) e não encontraram a frase da moeda em nenhuma. Não refiz esse download nesta
  rodada porque a pergunta de autoria já está fechada pela tabela oficial — mesmo se a frase
  aparecesse em alguma aula de Kempthorne, ela não seria a aula de probabilidade citada no
  draft (que é, comprovadamente, de Lee).
- Achado relevante já registrado antes e que continua de pé: Jordan Ellenberg, *How Not to Be
  Wrong*, usa quase a mesma estrutura pedagógica ("If you flip a coin 82 times and get 82
  heads...") com número diferente e autor diferente — reforça que este é um exemplo-padrão de
  ensino de probabilidade que circula sem dono fixo, o que torna a atribuição pontual a uma
  pessoa ainda mais arriscada.

**Recomendação final (decisão desta etapa, não mais `[VERIFICAR]` em aberto):** remover o
nome próprio do corpo do texto, mantendo a citação entre aspas diretas (a frase em si não é
comprovadamente falsa — só não é rastreável a Kempthorne especificamente, e o curso de fato
tem uma aula de probabilidade, só que ministrada por outro instrutor). Texto exato recomendado
para substituir as linhas 29-39 do draft:

> Um dos meus momentos favoritos do curso é a aula de probabilidade (_Probability Theory_). Em
> uma explicação sobre a ideia de retorno à média, um dos professores diz:
>
> "Se você lança uma moeda 100 vezes, obtendo cara em todos os lançamentos, você deveria estar
> considerando seriamente a possibilidade de que essa moeda tenha algum vício ou defeito."

E na bibliografia (linha 308), trocar a entrada que nomeia Kempthorne como autor principal
("Peter Kempthorne et al., ...") — que implica autoria dele sobre um curso inteiro cuja aula
citada não é sua — por:

> MIT OpenCourseWare, _18.S096 Topics in Mathematics with Applications in Finance_, Fall 2013
> (instrutores: Peter Kempthorne, Choongbum Lee, Vasily Strela, Jake Xia; versão atualizada:
> 18.642, Fall 2024) —
> [ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/)

Confirmei também que 18.642 (Fall 2024) é de fato a versão atualizada do curso, com Kempthorne
entre os instrutores — [ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/),
acesso 02/09/2026 — então a frase "atualizada como 18.642 em 2024" no corpo do texto (linha
27) está correta e não precisa mudar.

Fontes: MIT OCW, página de recurso da Lecture 3 e página de calendário do curso 18.S096 Fall
2013 (acesso direto, 02/09/2026); MIT OCW, página do curso 18.642 Fall 2024 (acesso direto,
02/09/2026); achados de transcrição de rodadas anteriores (`eb25b13`, `7ef1cf3`), não
refeitos por já estarem fechados por uma fonte mais forte (tabela oficial de instrutores).

---

## 2. A nota brasileira do target forward de 2008 — resolução do `[VERIFICAR]`

**Veredito: ✅ Resolvido — cito a fonte primária do Banco Central (não a estimativa do
rascunho original de "US$ 35 bilhões", que não se sustenta em nenhuma fonte rastreável).**

Baixei e li diretamente, via `curl` + `pdftotext`, o PDF do Banco Central do Brasil (não
aceitei o resumo de busca da rodada de pesquisa como fato fechado):

Mário Mesquita e Mario Torós, *Considerações sobre a Atuação do Banco Central na Crise de
2008*, Trabalhos para Discussão nº 202, Banco Central do Brasil, março de 2010, p. 7 —
[bcb.gov.br/pec/wps/port/wps202.pdf](https://www.bcb.gov.br/pec/wps/port/wps202.pdf), acesso
02/09/2026. Trecho exato, extraído do PDF:

> "Após pesquisa sobre a posição das instituições financeiras com seus clientes e o
> cruzamento das mesmas na CETIP S.A. — Balcão Organizado de Ativos e Derivativos (CETIP)
> estimou-se que o delta dessas exposições estaria próximo de US$37 bilhões ao final de
> setembro de 2008. Esta estimativa seria levada em conta na definição de aspectos da
> estratégia de gestão de crise adotada pelo BC."

Esta é a mesma pesquisa que gerou o BIS Papers No 54 (Mesquita & Torós, dez/2010, já citado
nas "Fontes e leituras" do draft) — os mesmos dois autores, o mesmo achado, publicado primeiro
em português pelo próprio Banco Central (Trabalhos para Discussão nº 202, mar/2010) e depois
em inglês pelo BIS. É fonte primária direta (o próprio regulador brasileiro), não uma
estimativa de imprensa ou blog — e é exatamente a métrica que a nota do rascunho está tentando
capturar ("o volume total dessas operações no país").

O "US$ 35 bilhões" do rascunho original não bate com nenhuma fonte rastreável: a origem mais
provável é um blog (Fernando Nogueira da Costa, 21/12/2012, já mapeado em `03-pesquisa.md`
item 2), que por sua vez não cita de onde tirou o número — não é fonte primária e não deve
ser usada.

**Frase final recomendada para substituir o `[VERIFICAR]` no draft** (linhas 170-175):

> O Banco Central estimou a exposição líquida (delta) dessas operações, apuradas via CETIP, em
> cerca de US$ 37 bilhões ao final de setembro de 2008 — o auge da crise no país.

Nota de precisão: isto é exposição/delta registrada na câmara de compensação, não "perda"
nem "volume nocional total negociado" — a frase acima já reflete essa métrica corretamente
("exposição líquida", não "perda" nem "volume de operações"). Se a consolidação preferir
citar a estimativa de perda em vez de exposição, a alternativa sólida e também de fonte
primária é o BIS Quarterly Review de junho de 2009 (Jara, Moreno & Tovar, Box 1, p. 55 — já
lido na íntegra em `03-pesquisa.md`): "losses are expected to be as high as $25 billion" — mas
troca o sentido da frase (perda estimada, não exposição), então recomendo a opção do BCB
acima, que é mais fiel ao que a frase do draft já promete medir ("o volume total dessas
operações").

Fonte: Banco Central do Brasil, Trabalhos para Discussão nº 202 (Mesquita & Torós, mar/2010) —
PDF lido diretamente. Acesso: 02/09/2026.

---

## 3. Demais números do draft, recalculados

### 3.1 Ibovespa e dólar, 18/05/2017 (`graf-01`)

**✅ Confirmado**, com uma ressalva de precisão sobre o percentual do dólar já sinalizada em
rodada anterior e ainda não corrigida no draft atual.

```python
# Ibovespa fechamento 17/05 -> 18/05
(61597.00 - 67540.00) / 67540.00 * 100  # = -8.80  ✅ bate com o draft
# queda intradiária, acionamento do circuit breaker às 10h51, índice em 60.470 pontos
# confirmado via InfoMoney: -10,47% intradiário — ✅ bate com o draft

# dólar, literal com os dois valores do texto (2 casas)
(3.38 - 3.14) / 3.14 * 100  # = 7.64, NÃO 8.06

# dólar, cotação comercial de fechamento mais precisa (mesma fonte que a imprensa usa para "8,06%")
(3.3805 - 3.1283) / 3.1283 * 100  # = 8.06  — bate exatamente
```

O percentual "8,06%" em si é o número correto e é o consistentemente reportado pela imprensa
financeira da época — mas ele só fecha a conta contra cotações com mais casas decimais
(R$3,1283 → R$3,3805) do que as duas casas que o texto mostra (R$3,14 → R$3,38). Um leitor que
multiplique de cabeça com os números que aparecem no texto acha 7,6%, não 8,06% — mesma
inconsistência já apontada na rodada 2 (`eb25b13`) e ainda presente no draft atual.

**⚠️ Impreciso — recomendação:** trocar "de R$ 3,14 para R$ 3,38" por "de R$ 3,13 para
R$ 3,38" não resolve (ainda dá 7,99%, não exatamente 8,06%); a correção limpa é uma das duas:
(a) usar as cotações com mais casas — "de R$ 3,1283 para R$ 3,3805" —, ou (b) manter os
valores arredondados como estão e trocar "8,06%" por "cerca de 7,6%". Recomendo (a), porque
"8,06%" é o número que circula na imprensa e o leitor pode conferir de fora; trocar as
cotações preserva esse número sem quebrar a conta interna do texto.

Fontes: Banco Central, SGS série 1 (PTAX, consulta direta à API,
[api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados)); InfoMoney, "Joesley Day: a delação que colocou em xeque a agenda de reformas..." — [infomoney.com.br](https://www.infomoney.com.br/mercados/joesley-day-a-delacao-que-colocou-em-xeque-a-agenda-de-reformas-e-fez-o-ibovespa-derreter-mais-de-10/), reconfirmado via `WebSearch` em 02/09/2026 (queda intradiária -10,47%, circuit breaker às 10h51 com o índice em 60.470 pontos, fechamento -8,80%, maior queda diária desde 22/10/2008, primeiro circuit breaker desde 2008).

### 3.2 LTCM — patrimônio, ativos, alavancagem, nocional

Li diretamente o PDF da fonte primária: President's Working Group on Financial Markets,
*Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management* (abril de 1999) —
[home.treasury.gov/system/files/236/hedgfund.pdf](https://home.treasury.gov/system/files/236/hedgfund.pdf),
lido via `pdftotext`, acesso 02/09/2026. Trechos exatos extraídos do PDF:

> "With regard to leverage, the LTCM Fund's balance sheet on **August 31, 1998**, included
> over **$125 billion** in assets. Even using the **January 1, 1998**, equity capital figure
> of **$4.8 billion**, this level of assets still implies a balance-sheet leverage ratio of
> more than **25-to-1**."
>
> "LTCM, with total assets of **$129 billion** at the end of 1997... The notional amount of
> LTCM's total OTC derivatives position was **$1.3 trillion** at the end of 1997 and **$1.5
> trillion** at the end of 1998. LTCM's balance sheet leverage was **28-to-1** at the end of
> 1997."
>
> "At the end of 1997, LTCM returned approximately **$2.7 billion** in capital to its
> investors..."
>
> "The firms participating in the consortium invested about **$3.6 billion** in new equity..."

```python
125 / 4.7   # = 26.60 — com os números do próprio draft (US$4,7bi / US$125bi)
125 / 4.8   # = 26.04 — com a equidade que a fonte primária usa (Jan/1998)
129 / 4.8   # = 26.88 — ativos fim de 1997 / equidade início de 1998
```

**⚠️ Impreciso, três pontos específicos, valores centrais corretos:**

1. **Mistura de datas.** "No início de 1998 o LTCM operava com cerca de US$4,7 bilhões de
   patrimônio [e] aproximadamente US$125 bilhões em ativos" apresenta os dois números como
   uma única fotografia de "início de 1998". Não são: o patrimônio de ~US$4,7-4,8bi é de 1º de
   janeiro de 1998; os "mais de US$125 bilhões" em ativos são do balanço de **31 de agosto de
   1998** — a véspera da crise russa, oito meses depois. (A própria fonte primária faz essa
   comparação de propósito, mas dizendo explicitamente as duas datas — o draft omite as datas
   e por isso lê como instantâneo único.)
2. **"Algo em torno de 25:1" subestima.** Com os números do próprio draft, 125/4,7 = 26,6:1,
   não "em torno de 25". A fonte primária usa "more than 25-to-1" (piso, não valor central).
   Recomendo trocar por "mais de 25:1" ou "cerca de 26:1".
3. **"US$1,25 trilhão" de nocional não existe na fonte primária.** O PWG (1999) só registra
   US$1,3 trilhão (fim de 1997) e US$1,5 trilhão (fim de 1998) para o nocional de derivativos
   de balcão — não há "$1,25 trilhão" em nenhuma leitura do documento.

**Correção proposta**, mantendo o tom do parágrafo mas separando as datas e ajustando os dois
números imprecisos:

> No início de 1998 o LTCM tinha cerca de US$ 4,7 bilhões de patrimônio; em agosto do mesmo
> ano, às vésperas da crise, os ativos já passavam de US$ 125 bilhões — mais de 26 para 1 de
> alavancagem — com um nocional de derivativos fora de balanço que somava US$ 1,3 trilhão no
> fim de 1997.

Os demais números do parágrafo do LTCM — devolução de US$2,7bi aos investidores (fim de
1997), perda de US$4,6bi em menos de quatro meses, resgate de US$3,6bi por 14 instituições
sob articulação de William McDonough — **✅ confirmados**, bate exatamente com o PWG (1999)
lido diretamente e, para a perda de US$4,6bi (que o PWG não fecha num número único explícito
no trecho que li), com Federal Reserve History, "Near Failure of Long-Term Capital
Management" —
[federalreservehistory.org/essays/ltcm-near-failure](https://www.federalreservehistory.org/essays/ltcm-near-failure),
reconfirmado via `WebSearch` em 02/09/2026.

### 3.3 JPMorgan London Whale — "mais de US$ 6 bilhões"

**✅ Confirmado.** David Viniar (então CFO do Goldman Sachs, citado sem nome no draft — o que
está correto, ver item abaixo) não é a fonte aqui; a perda do London Whale em si é
consistentemente reportada em "pelo menos US$ 6,2 bilhões" — US Senate Permanent Subcommittee
on Investigations, *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and
Abuses* (abril de 2013) —
[hsgac.senate.gov/.../JPMorgan-Chase-Whale-Trades.pdf](https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(4-12-13).pdf),
reconfirmado via `WebSearch` em 02/09/2026. "Mais de US$ 6 bilhões" no draft é consistente e
conservador frente aos US$6,2bi da fonte primária.

### 3.4 A citação dos "25 desvios-padrão" (2007) — sem nome no draft

**✅ Confirmado, e a ausência do nome próprio no draft está correta.** A frase é de David
Viniar, então CFO do Goldman Sachs, em agosto de 2007 (Financial Times): "We were seeing
things that were 25-standard deviation moves, several days in a row." O draft diz apenas "o
então CFO do Goldman Sachs" sem nomear — isso é preciso (Viniar foi CFO do Goldman de 1999 a
2013, cobre 2007) e evita o mesmo risco de atribuição nominal equivocada do item 1.
Reconfirmado via `WebSearch`, 02/09/2026.

### 3.5 Aracruz — US$ 2,13 bilhões

**✅ Confirmado como número do corpo do texto — mas ⚠️ inconsistência real entre duas fontes
citadas juntas na bibliografia do próprio draft.**

O número no corpo do texto (US$2,13 bilhões, perda comunicada ao desmontar as posições em
novembro de 2008) é o correto e o mais bem sustentado: Bloomberg, "Aracruz Fails to Settle
$2.13 Billion Derivative Loss" (12/12/2008), e o Fato Relevante da própria Aracruz de
03/11/2008 (citado em paper acadêmico revisado, já mapeado em rodada anterior de verificação):
"realização de uma perda total de aproximadamente US$ 2,13 bilhões (fair value)".

Fui atrás, eu mesmo, do artigo da RACEF que o draft já cita nas "Fontes e leituras" — Breno
Augusto de Oliveira Silva e Henrique Penatti Pinese, "A Crise Financeira Internacional (2008) e
o Efeito dos Derivativos Cambiais: a operação de target forward da Aracruz Celulose", *Revista
de Administração, Contabilidade e Economia da Fundace* (RACEF) —
[racef.fundace.org.br/index.php/racef/article/view/23](https://racef.fundace.org.br/index.php/racef/article/view/23/0),
PDF lido integralmente via `pdftotext`, acesso 02/09/2026. O artigo afirma, no resumo e no
corpo: "prejuízos na ordem de R$ 2,5 bilhões em função dos derivativos de câmbio". **Não é
conversão direta de US$2,13 bilhões** — convertendo pela cotação de novembro de 2008 (~R$2,10-
2,40/US$), US$2,13bi dariam entre R$4,5 e R$5,1 bilhões, não R$2,5bi. O artigo da RACEF também
**não cita fonte nem data específica** para o número de R$2,5 bilhões (não aparece Fato
Relevante, não aparece data de corte) — ele aparece como afirmação solta no resumo e é
repetido, também sem nova atribuição, no corpo do texto. O mesmo artigo, à parte, cita
corretamente o prejuízo líquido *anual* da Aracruz em 2008 como R$4,2 bilhões — número
diferente, que é o resultado total do ano, não a liquidação dos derivativos.

**Veredito: não é a mesma cifra em cortes diferentes — é uma inconsistência real entre a
fonte acadêmica (RACEF, R$2,5bi, sem proveniência clara) e a fonte jornalística/regulatória
(Bloomberg + Fato Relevante, US$2,13bi, com data e fonte primária exatas).** O corpo do texto
do draft usa corretamente o número mais bem sustentado (US$2,13bi). O problema é só de
citação: agrupar RACEF sob a mesma linha bibliográfica de "Aracruz e Sadia" ao lado da
Bloomberg, sem qualificar que o número de destaque do próprio artigo da RACEF (R$2,5bi) não
bate com o número usado no corpo do post, pode confundir um leitor que siga a citação até a
fonte. **Recomendação:** manter Bloomberg como referência para o número usado no corpo
(US$2,13bi) e citar a RACEF apenas para o contexto institucional/metodológico do caso (o
artigo é uma boa fonte para entender a mecânica do target forward), não como confirmação do
valor — ou remover a RACEF da linha "Aracruz e Sadia" das Fontes e leituras se o objetivo era
sustentar o número.

### 3.6 Sadia — R$ 2,55 bilhões

**✅ Confirmado, com convergência entre duas fontes secundárias independentes** (não achei
fonte primária direta — Fato Relevante da Sadia, 25/09/2008 — com cifra fechada; ele
reconhece operações "em valores superiores à finalidade de proteção" sem número, segundo o
mesmo paper acadêmico usado para a Aracruz). As duas fontes secundárias convergem no mesmo
detalhamento: despesa financeira com derivativos em 2008 de R$2,5-2,55 bilhões, dos quais
~R$705,9 milhões com efeito caixa — Capital Aberto, "O Caso Sadia" (revista especializada), e
Fernando Nogueira da Costa (blog, já mapeado em `03-pesquisa.md`), que cita a mesma quebra
(R$2,55bi de perdas com os contratos, R$705 milhões de impacto de caixa) dentro de uma despesa
financeira total de R$3,892bi no ano. A convergência exata do detalhamento (mesmo número de
"R$705 milhões" de efeito caixa nas duas fontes) sugere que ambas bebem da mesma demonstração
financeira padronizada (DFP) de 2008 da Sadia, não são estimativas independentes divergentes —
por isso trato como confirmado, mesmo sem ter aberto a DFP original nesta rodada.

---

## 4. Financial Modelers' Manifesto (2009) — os cinco compromissos, seção 6

**✅ Confirmado, fidelidade total — conferido por mim, não só herdado de `03-pesquisa.md`.**

Baixei e li o PDF original diretamente: Emanuel Derman & Paul Wilmott, *The Financial
Modelers' Manifesto*, 7 de janeiro de 2009 —
[emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf](https://emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf),
acesso 02/09/2026. Texto exato dos cinco itens de "The Modelers' Hippocratic Oath":

1. "I will remember that I didn't make the world, and it doesn't satisfy my equations."
2. "Though I will use models boldly to estimate value, I will not be overly impressed by
   mathematics."
3. "I will never sacrifice reality for elegance without explaining why I have done so."
4. "Nor will I give the people who use my model false comfort about its accuracy. Instead, I
   will make explicit its assumptions and oversights."
5. "I understand that my work may have enormous effects on society and the economy, many of
   them beyond my comprehension."

A paráfrase do draft (linhas 254-258) bate em sentido, conteúdo e ordem com os cinco, sem
distorção, adição ou omissão. Único ponto (menor, cosmético): os cinco compromissos vêm
tecnicamente do "Modelers' Hippocratic Oath", subseção final do manifesto — o draft já diz
isso corretamente ("cujo núcleo é um 'juramento de Hipócrates do modelador'"), então não há
nada a corrigir.

---

## 5. As seis hipóteses de Black–Scholes listadas (seção 3)

**✅ Confirmado — lista consistente com a formulação padrão, sem indução a erro.**

Comparado contra o artigo original (Black & Scholes, "The Pricing of Options and Corporate
Liabilities", *Journal of Political Economy*, 1973) e contra a apresentação padrão em
livros-texto de finanças quantitativas (ex. Hull, *Options, Futures, and Other Derivatives*):
a lista canônica inclui (a) GBM sem saltos para o preço do ativo, (b) volatilidade constante,
(c) taxa livre de risco constante e conhecida, (d) ausência de custos de transação e impostos,
(e) negociação/hedge em tempo contínuo, (f) venda a descoberto livre e divisibilidade dos
ativos, e geralmente (g) ausência de dividendos durante a vida da opção, e (h) o instrumento é
uma opção europeia (sem exercício antecipado).

O draft cobre (a)-(f) explicitamente e qualifica a lista com "entre outras coisas" — não
afirma exaustividade. A opção europeia já está definida no parágrafo anterior da mesma seção
("quanto vale uma opção europeia... antes do vencimento"), então não precisa reaparecer na
lista de premissas. A ausência explícita de "sem dividendos" é uma omissão coberta pela
ressalva "entre outras coisas" — simplificação editorial aceitável para um texto de
divulgação, não erro que induza a conclusão equivocada. Nenhuma das seis premissas listadas
está incorreta ou mal descrita.

---

## Resumo para a consolidação

| # | Item | Veredito | Ação |
|---|---|---|---|
| 1 | Citação de Kempthorne (corpo + bibliografia) | ❌ Atribuição não se sustenta (confirmado de forma definitiva via tabela oficial de instrutores do MIT OCW) | Remover "do professor Peter Kempthorne" e "Kempthorne diz" → "um dos professores diz", mantendo aspas diretas; ajustar bibliografia para não implicar autoria principal de Kempthorne sobre o curso inteiro |
| 2 | Target forward 2008 — volume/exposição | ✅ Resolvido com fonte primária do BCB | Substituir `[VERIFICAR]` pela frase final proposta (item 2 acima), citando Mesquita & Torós, BCB Trabalhos para Discussão nº 202 (2010) |
| 3.1 | Dólar 18/05/2017, "8,06%" vs "R$3,14→R$3,38" | ⚠️ Impreciso (inconsistência de casas decimais) | Trocar cotações por R$3,1283→R$3,3805 (mantém 8,06% exato) |
| 3.1 | Ibovespa 18/05/2017 | ✅ Confirmado | Nenhuma mudança |
| 3.2 | LTCM — datas de patrimônio/ativos misturadas | ⚠️ Impreciso | Separar "início de 1998" (patrimônio) de "agosto de 1998" (ativos), ver frase proposta acima |
| 3.2 | LTCM — "em torno de 25:1" | ⚠️ Impreciso (subestima) | Trocar por "mais de 25:1" ou "cerca de 26:1" |
| 3.2 | LTCM — nocional "US$1,25 trilhão" | ⚠️ Impreciso (não existe na fonte) | Trocar por "US$1,3 trilhão" (fim de 1997) |
| 3.2 | LTCM — perda US$4,6bi, resgate US$3,6bi/14 instituições, devolução US$2,7bi | ✅ Confirmado | Nenhuma mudança |
| 3.3 | London Whale, "mais de US$6bi" | ✅ Confirmado | Nenhuma mudança |
| 3.4 | "25 desvios-padrão", CFO sem nome | ✅ Confirmado (e correto não nomear) | Nenhuma mudança |
| 3.5 | Aracruz US$2,13bi (corpo) vs RACEF R$2,5bi (bibliografia) | ⚠️ Impreciso — inconsistência real entre fontes citadas juntas | Manter US$2,13bi no corpo (bem sustentado); qualificar ou remover RACEF como fonte do número na bibliografia |
| 3.6 | Sadia R$2,55bi | ✅ Confirmado (convergência de duas fontes secundárias) | Nenhuma mudança |
| 4 | Financial Modelers' Manifesto, 5 compromissos | ✅ Confirmado, fidelidade total | Nenhuma mudança |
| 5 | 6 hipóteses de Black–Scholes | ✅ Confirmado | Nenhuma mudança |
| — | Título "Models. Behaving. Badly." | ⚠️ Impreciso (já flagueado na rodada 3, ainda não corrigido) | Remover espaços → "Models.Behaving.Badly." nas duas ocorrências (linha 55 e bibliografia) |

### `[VERIFICAR]` / `[FAIXA]` consolidados para o texto final

Nenhum `[VERIFICAR]` precisa sobreviver à consolidação desta rodada — os dois pontos que
chegaram com `[VERIFICAR]` explícito (Kempthorne, target forward) foram resolvidos nesta etapa
com decisão e frase final, não ficam pendentes. Não há `[FAIXA: ...]` novo: o número do target
forward tem uma fonte primária única e direta (BCB, ~US$37bi de exposição delta) que não
precisa ser apresentada como intervalo — a faixa BIS (~US$25bi de perda) mede uma métrica
diferente (perda, não exposição), não é a mesma grandeza em versões distintas.

Se a consolidação preferir, por prudência editorial, manter algum marcador — por exemplo, se
não houver tempo de reescrever a frase de abertura sobre Kempthorne — a formulação mínima
seria:

`[VERIFICAR: a atribuição da citação de abertura a um professor específico do curso do MIT
OCW não é rastreável — a aula de probabilidade citada (Lecture 3, 18.S096 Fall 2013) é
oficialmente atribuída a Choongbum Lee, não a Peter Kempthorne, conforme a tabela de
instrutores do calendário oficial do curso.]`

— mas a recomendação desta etapa é resolver diretamente com a reescrita proposta no item 1,
não deixar isso para uma quinta rodada.
