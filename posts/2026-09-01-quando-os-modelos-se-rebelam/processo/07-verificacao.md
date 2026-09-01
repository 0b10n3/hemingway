# Verificação técnica — "Quando os Modelos se Rebelam"

Laudo do agente `verificador-tecnico`, etapa 7. Veredito por item, contra fonte primária
quando disponível. Parte do trabalho de checagem já estava feito em `03-pesquisa.md`; este
laudo confirma consistência com o draft atual (`04-draft-v1.md`) e fecha as duas pendências
explicitamente deixadas em aberto pela pesquisa.

## Os dois pontos em aberto (prioridade desta etapa)

### 1. Citação de Peter Kempthorne — ❓ Não verificável, mesmo após checagem ativa

Metodologia usada além da busca textual da etapa 3 (que já não tinha conseguido ler
legenda/vídeo): baixei diretamente o PDF de notas de aula
(`MIT18_S096F13_lecnote3.pdf`, 18.S096 Fall 2013, Lecture 3: Probability Theory) e li o
conteúdo inteiro — são 6 páginas de definição formal (função de massa de probabilidade,
distribuição normal/log-normal, função geradora de momentos, lei dos grandes números,
teorema central do limite). **Não há nenhuma menção a moeda, lançamento, "cara" ou viés em
todo o documento.** Isso já era esperado — notas de aula em PDF costumam ser só o
formalismo, sem os exemplos narrados oralmente — mas elimina essa fonte específica como
confirmação textual.

Fui além do que a pesquisa da etapa 3 tinha conseguido: usando `yt-dlp`, baixei a legenda
automática (auto-caption, inglês) dos três vídeos de aula candidatos e fiz busca exaustiva
por "coin", "100 times", "biased", "bias", "heads" em cada um — zero ocorrências nos três:

- **18.S096 Fall 2013, Lecture 3: Probability Theory** (youtube `f9XFM8YLccg`) — confirmado
  por fonte adicional (MIT OCW indexado por infocobuild.com, meta keywords da página da
  aula) que o instrutor desta aula específica é **Dr. Choongbum Lee**, não Kempthorne. O
  curso 2013 tem quatro instrutores (Kempthorne, Lee, Strela, Xia) revezando aulas; a aula
  de probabilidade da versão 2013 não é a de Kempthorne.
- **18.642 Fall 2024, Lecture 4: Linear Algebra (cont.); Probability Theory** (youtube
  `mtXTs2U1uMA`) — confirmado pelo calendário oficial do curso (OCW) que esta aula **é**
  ministrada por Kempthorne, e a transcrição confirma que o conteúdo falado é de fato
  probabilidade. Sem ocorrência das palavras-chave.
- **18.642 Fall 2024, Lecture 5: Probability Theory (cont.); Stochastic Processes I**
  (youtube `wMGEKMHsOKE`) — mesmo instrutor (Kempthorne), mesma checagem, mesmo resultado
  nulo.

Ou seja: nem a aula original citada pelo rascunho (2013, Lecture 3) nem as duas aulas de
probabilidade da versão atualizada (2024, Lectures 4-5, que são as que Kempthorne de fato
ministra) contêm a frase — nem nada parecido com ela — nas legendas/transcrição de áudio.

Achado adicional relevante: buscando a estrutura da frase em inglês, encontrei em Jordan
Ellenberg, *How Not to Be Wrong* — "If you flip a coin 82 times and get 82 heads, you ought
to be thinking, 'Something is biased about this coin.'" — um exemplo do mesmo tipo (moeda
enviesada como ilustração de retorno à média/viés), mas com número diferente (82, não 100) e
autor diferente. Isso sugere que a estrutura do exemplo é um lugar-comum pedagógico usado por
vários autores de probabilidade — o que torna ainda mais importante não afirmar a atribuição
específica a Kempthorne sem confirmação, porque é exatamente o tipo de frase que se generaliza
e se remistura entre fontes na memória de quem escreve.

**Veredito: não confirmado, apesar de busca ativa em fonte primária (PDF de notas + três
transcrições de vídeo via download direto, não só busca textual).** Isso não prova que a
frase seja falsa — Kempthorne pode tê-la dito em algum momento não capturado pela legenda
automática, ou em uma aula/ano diferente dos três checados — mas não há nenhuma evidência a
favor e uma evidência de estrutura genérica (Ellenberg) que pesa contra a atribuição específica
tal como está. Marcador a inserir no texto:

`[VERIFICAR: citação de Kempthorne não confirmada contra fonte primária — checados o PDF de
notas da aula 18.S096 Fall 2013 Lecture 3 e as transcrições de vídeo de 18.S096 Lecture 3
(2013, ministrada por Choongbum Lee, não Kempthorne) e 18.642 Lectures 4-5 (2024, ministradas
por Kempthorne) — nenhuma contém a frase ou algo equivalente]`

Recomendação editorial (não obrigatória, fica a critério da consolidação): dado que a aula de
2013 citada no rascunho nem é de Kempthorne segundo o próprio MIT OCW, vale considerar reescrever
a abertura sem atribuir a frase a uma aula específica, ou trocar a referência para as aulas 4-5
de 18.642 (2024, que são realmente de Kempthorne) sem a citação entre aspas — como paráfrase do
tipo de raciocínio que ele ensina, não como citação literal.

### 2. Nocional de derivativos do LTCM (US$ 1,25 trilhão) — ⚠️ Impreciso, correção exata disponível

Abri o relatório primário diretamente: President's Working Group on Financial Markets,
*Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management* (1999),
`home.treasury.gov/system/files/236/hedgfund.pdf` (baixado e lido via `pdftotext`). O
documento **não contém a cifra "US$ 1,25 trilhão"** em nenhum lugar. Os números que ele dá,
literalmente:

> "The notional amount of LTCM's total OTC derivatives position was **$1.3 trillion** at the
> end of 1997 and **$1.5 trillion** at the end of 1998."

E, num trecho separado, referente a agosto de 1998 especificamente:

> "At the end of August, 1998, the gross notional amounts of the Fund's contracts on futures
> exchanges exceeded **$500 billion**, swaps contracts more than **$750 billion**, and
> options and other OTC derivatives over **$150 billion**."

(Essa segunda soma — bolsa + swaps + opções/outros — dá bruto ≈ US$1,4 tri, mas mistura
posições em bolsa com posições de balcão, uma métrica diferente da primeira citação, que é só
OTC.)

Não existe, em nenhuma das duas leituras possíveis do relatório primário, o número "US$1,25
trilhão". **Correção proposta**: como o texto enquadra o número como "início de 1998", a
opção mais fiel ao relatório primário é trocar por **"US$ 1,3 trilhão"** (fim de 1997/início
de 1998), citando o PWG (1999) diretamente. Alternativa: apresentar como faixa —
`[FAIXA: US$ 1,25 trilhão → US$ 1,3 trilhão (fim de 1997) a US$ 1,5 trilhão (fim de 1998),
conforme PWG 1999]` — já que o fundo cresceu o nocional ao longo do ano da crise e "início de
1998" versus "no auge, antes do colapso" são pontos diferentes no tempo que o próprio
relatório trata separadamente.

## Recálculos pedidos explicitamente — patrimônio, ativos e alavancagem do LTCM

O mesmo relatório primário (PWG 1999) traz o parágrafo-fonte de onde saem "US$125 bilhões" e
"25:1" no rascunho, e ele mistura duas datas diferentes — o que é uma pista importante para
avaliar a frase do rascunho:

> "With regard to leverage, the LTCM Fund's balance sheet on **August 31, 1998**, included
> over **$125 billion** in assets. Even using the **January 1, 1998**, equity capital figure
> of **$4.8 billion**, this level of assets still implies a balance-sheet leverage ratio of
> more than **25-to-1**."

Ou seja: **o próprio "US$125 bilhões" citado no rascunho é, na fonte primária, um número de
31 de agosto de 1998 — não de "início de 1998"** como o rascunho enquadra. O número de ativos
que a mesma fonte dá para o fim de 1997/início de 1998 é diferente: **US$129 bilhões**
("LTCM, with total assets of $129 billion at the end of 1997..."), com alavancagem de
balanço explicitamente citada como **"28-to-1 at the end of 1997"** noutra seção do mesmo
relatório.

Isso não é necessariamente um erro do rascunho — é o mesmo movimento retórico que o próprio
PWG faz (comparar o patrimônio de janeiro com os ativos de agosto para ilustrar como a
alavancagem cresceu ao longo do ano de crise) — mas o rascunho apresenta os dois números como
se fossem do mesmo instante ("no início de 1998... aproximadamente US$125 bilhões"), o que
tecnicamente não bate com a datação da fonte primária. ⚠️ Vale ajustar a frase para deixar
claro que "US$125 bilhões" é o pico dos ativos em agosto de 1998 (imediatamente antes do
colapso), não um número de janeiro.

Recálculo pedido pelo agente que despachou esta tarefa:

```python
125 / 4.7  = 26.6   # com os números exatos do próprio rascunho
125 / 4.8  = 26.0   # com a equidade que a fonte primária usa (Jan/1998)
129 / 4.8  = 26.9   # ativos fim-1997 / equidade Jan-1998
129 / 4.6  = 28.0   # bate com o "28-to-1 at the end of 1997" que a fonte primária cita
```

**Veredito: "algo em torno de 25:1" é uma subestimativa.** Com os próprios números do
rascunho (125bi/4,7bi), a alavancagem é 26,6:1, não "em torno de 25". Mesmo usando a
equidade que a fonte primária usa (US$4,8bi), dá 26,0:1. A fonte primária evita esse problema
falando em **"more than 25-to-1"** (limite inferior, não valor central) — recomendo trocar
"algo em torno de 25:1" por algo equivalente ("pouco mais de 25:1" ou, com mais precisão,
"cerca de 26:1"), porque "em torno de 25" soa como valor central e a conta real fica acima
disso.

Sobre o patrimônio "US$4,7 bilhões": a fonte primária usa US$4,8bi para 1º/jan/1998; a
literatura secundária mais citada sobre o caso (Lowenstein, *When Genius Failed*) usa
US$4,72bi, que arredonda para US$4,7bi — a diferença entre US$4,7bi e US$4,8bi é pequena e
ambas são defensáveis dependendo da fonte/arredondamento; não requer correção.

## Recálculo pedido — variação cambial do Joesley Day (8,06%)

```python
d0, d1 = 3.14, 3.38
(d1 - d0) / d0 * 100  # = 7.643%, não 8,06%
```

⚠️ **Impreciso, mas por um motivo específico e não por erro de fonte.** A conta literal com
os dois valores exatamente como aparecem no texto (R$3,14 → R$3,38, ambos arredondados a duas
casas) dá 7,64%, não 8,06%. O percentual "8,06%" em si está correto e é o número
consistentemente reportado pela imprensa financeira (InfoMoney: "o dólar subiu 8,06%... de
cerca de R$ 3,14 para R$ 3,38") — mas ele só bate matematicamente contra cotações mais
precisas que as duas casas decimais mostradas no texto. Testei contra uma cotação mais precisa
amplamente citada (R$3,1283 → R$3,3805): `(3.3805-3.1283)/3.1283*100 = 8,06%` — bate
exatamente. A cotação PTAX do Banco Central para as mesmas datas (fonte oficial, consultada via
API do Bacen, `olinda.bcb.gov.br`) dá valores um pouco diferentes ainda (R$3,1076 →
R$3,3807, uma variação de 8,79%), porque PTAX é fixada em horário diferente do fechamento
comercial que a imprensa usa como referência para "8,06%" — não é a mesma métrica.

**Recomendação**: como o texto já anuncia "R$3,14" e "R$3,38" com apenas duas casas, a conta
do leitor que multiplicar cabeça vai dar 7,6%, não 8,06% — um leitor atento vai notar a
inconsistência. Duas saídas: (a) trocar as cotações por valores com mais casas decimais
(R$3,13 e R$3,38 continuam arredondando errado; usar R$3,1283 e R$3,3805 resolve
completamente), ou (b) manter as cotações arredondadas e trocar "8,06%" por "cerca de 7,6%".
Não é erro de fonte — é inconsistência de precisão entre duas casas do texto.

## Itens já cobertos pela pesquisa da etapa 3 — reconfirmados consistentes com o draft atual

Não refeitos do zero (a pesquisa já tinha fonte primária ou múltiplas fontes consistentes);
apenas conferido que o texto atual (`04-draft-v1.md`) continua batendo com o que foi
confirmado:

- **Joesley Day, 18/05/2017**: queda intradiária -10,47%, fechamento -8,80% (maior queda
  diária desde 22/10/2008), primeiro *circuit breaker* desde 2008 — ✅ consistente.
- **Aracruz Celulose**: perda de US$2,13 bilhões, comunicada em 03/11/2008 — ✅ consistente.
- **Sadia**: o draft já distingue corretamente "R$2,55 bilhões em despesas financeiras" de
  "prejuízo líquido de R$2,48 bilhões" — ✅ a correção que a pesquisa recomendou já está
  aplicada no draft atual, nada a fazer.
- **MacKenzie, performatividade/contraperformatividade**: o draft já separa explicitamente as
  duas fases (pré-1987 convergência, pós-1987 divergência/*smile*) — ✅ a nuance que a
  pesquisa apontou como faltante já está incorporada no draft atual.
- **LTCM — fundação 1994, John Meriwether; Nobel 1997 para Scholes e Merton**: fatos padrão,
  sem necessidade de nova checagem — ✅.
- **LTCM — devolução de US$2,7bi aos investidores no fim de 1997**: ✅ consistente.
- **LTCM — calote russo em 17/08/1998**: confirmado diretamente no texto do PWG 1999
  ("Russia's devaluation of the ruble and declaration of a debt moratorium on August 17 of
  last year") — ✅.
- **LTCM — resgate de 23/09/1998, 14 instituições, ~US$3,6 bilhões, sob articulação de
  William McDonough**: confirmado diretamente no texto do PWG 1999 ("fourteen firms agreed to
  participate in the consortium... The firms participating in the consortium invested about
  $3.6 billion in new equity"; McDonough citado como presidente do Fed de Nova York) — ✅. O
  draft arredonda para "~US$3,6 bi", que bate exatamente com a fonte primária.
- **LTCM — perda de ~US$4,6 bilhões em menos de quatro meses**: já confirmado por múltiplas
  fontes na pesquisa (o resumo do PWG não traz esse número agregado nesta seção, mas não há
  divergência) — ✅.
- **David Viniar, "25 desvios-padrão", 2007, *Financial Times***: ✅ consistente, usado
  corretamente como analogia posterior, não atribuído ao episódio LTCM.
- **London Whale — perda "pelo menos US$6,2 bilhões"**: o draft já usa a cifra corrigida
  (antes ">US$6 bi") — ✅ correção da pesquisa já aplicada.
- **London Whale — redução de "cerca de 44%" na estimativa de VaR**: o draft já usa 44%
  (antes "pela metade") — ✅ correção da pesquisa já aplicada.
- **SR 11-7 (Fed/OCC, 2011) em vigor antes do London Whale (2012)**: ✅ consistente.
- **Financial Modelers' Manifesto (Derman & Wilmott, 2009)**: texto do "juramento" já
  conferido pela pesquisa contra o PDF original hospedado no site do próprio Derman — ✅.
- **Volume total de operações "target forward" no Brasil em 2008, ~US$35 bilhões**: tentei
  localizar a fonte primária/regulatória sugerida pela pesquisa (BIS Quarterly Review, junho
  de 2009, "Derivatives-related exposures in the corporate sector: the case of Mexico and
  Brazil") — o PDF não carregou de forma legível (retornou HTML malformado/404 em duas
  tentativas) e não consegui confirmar o número contra essa fonte nesta etapa. Permanece como
  estimativa de consenso de imprensa/acadêmico, sem fonte regulatória direta confirmada.
  Mantenho o marcador já sinalizado pela pesquisa:
  `[VERIFICAR: fonte primária/regulatória (Banco Central, CVM ou BIS) para o volume total de
  ~US$35 bilhões em operações "target forward" no Brasil em 2008 — não localizada nesta
  etapa; número é consenso de imprensa e literatura acadêmica]`

## Resumo executivo

**Itens verificados nesta etapa**: 20 (incluindo os dois pontos em aberto, os dois
recálculos pedidos explicitamente, e 16 itens reconfirmados contra o draft atual).

**`[VERIFICAR]` / `[FAIXA]` que devem aparecer no texto final**:

1. `[VERIFICAR: citação de Kempthorne não confirmada contra fonte primária — checados o PDF
   de notas da aula 18.S096 Fall 2013 Lecture 3 e as transcrições de vídeo de 18.S096 Lecture 3
   (2013, ministrada por Choongbum Lee, não Kempthorne) e 18.642 Lectures 4-5 (2024,
   ministradas por Kempthorne) — nenhuma contém a frase ou algo equivalente]`
2. `[FAIXA: US$ 1,25 trilhão → US$ 1,3 trilhão (fim de 1997) a US$ 1,5 trilhão (fim de 1998),
   conforme President's Working Group on Financial Markets, Hedge Funds, Leverage, and the
   Lessons of Long-Term Capital Management (1999)]` — alternativa mais simples: trocar direto
   por "US$1,3 trilhão", que é o número que bate com o enquadramento "início de 1998" do
   texto.
3. `[VERIFICAR: fonte primária/regulatória (Banco Central, CVM ou BIS) para o volume total de
   ~US$35 bilhões em operações "target forward" no Brasil em 2008 — não localizada nesta
   etapa; número é consenso de imprensa e literatura acadêmica]`

**Correções pontuais recomendadas (não obrigatoriamente `[VERIFICAR]`, mas merecem ajuste de
texto na consolidação)**:

4. "algo em torno de 25:1" → "pouco mais de 25:1" ou "cerca de 26:1" (a conta com os próprios
   números do texto, 125bi/4,7bi, dá 26,6:1; mesmo com a equidade da fonte primária, US$4,8bi,
   dá 26,0:1 — "em torno de 25" subestima).
5. "US$125 bilhões em ativos" atribuído a "início de 1998" → esse valor é, na fonte primária,
   especificamente de 31 de agosto de 1998 (pico pré-colapso), não do início do ano. Ajustar a
   frase para deixar isso explícito, ou trocar por US$129 bilhões (valor de fim de 1997) se a
   intenção é mesmo "início do ano".
6. "8,06%" de alta do dólar bate matematicamente contra cotações mais precisas
   (R$3,1283→R$3,3805), mas não contra os valores de duas casas decimais como aparecem no
   texto (R$3,14→R$3,38, que dá 7,64%). Ajustar as cotações para mais precisão ou o percentual
   para "cerca de 7,6%", para eliminar a inconsistência interna.

**Sem necessidade de novo marcador**: os demais 16 itens reconfirmados (lista completa acima)
já estavam corretos no draft atual, incluindo três correções que a pesquisa da etapa 3 já
tinha recomendado e que o draft já aplicou antes desta etapa (Sadia, MacKenzie, London Whale
×2).
