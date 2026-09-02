# Verificação técnica — "Quando os Modelos se Rebelam"

Laudo do agente `verificador-tecnico`, etapa 7, sobre `04-draft-v1.md` (versão pós-loop
5→2/4, a que está em disco nesta rodada). Este laudo **substitui** o conteúdo anterior deste
arquivo: o texto que estava aqui foi produzido contra um estado de rascunho diferente do
atual — cita números que não existem mais no draft (ex.: "R$2,55 bilhões" da Sadia, "44%" de
redução de VaR, "algo em torno de 25:1" para o LTCM) e por isso ficaria enganoso para a etapa
de consolidação se mantido. Onde a verificação anterior fez trabalho genuíno e ainda
relevante (ex.: leitura do PWG 1999 sobre o nocional do LTCM), esse achado foi conferido de
novo nesta rodada e incorporado abaixo com fonte própria.

Metodologia: busca web, `WebFetch` de página/PDF quando possível, extração de texto de PDF
via `pdftotext` quando `WebFetch` falhou no binário, chamada direta à API pública do Banco
Central (`api.bcb.gov.br`), e recálculo em `python3` para todo número percentual/razão citado
no draft ou candidato a entrar nele.

---

## 1. Citação de Kempthorne (abertura + bibliografia)

**No corpo do texto**: o draft já não nomeia Kempthorne — usa "um dos professores" com
`[VERIFICAR]` inline explicando o motivo. Isso está correto e não precisa de mudança.

**Confirmação independente desta rodada**: refiz a checagem da página de recurso oficial do
MIT OCW para a *Lecture 3: Probability Theory* (18.S096, Fall 2013) via `WebFetch` direto —
a página identifica **Dr. Choongbum Lee** como instrutor desta aula específica, não
Kempthorne. Também consultei a página do MIT Math (`math.mit.edu/classes/18.S096/fall13`),
que lista os quatro instrutores do curso (Kempthorne, Choongbum Lee, Vasily Strela, Jake Xia)
mas não atribui aulas individualmente — a atribuição de Lee à Lecture 3 vem especificamente
da página de recurso daquela aula, não de inferência.

**Veredito sobre a bibliografia** (o item que este laudo precisava resolver, já que o corpo
já estava hedgeado): ⚠️ **Impreciso — ajustar**. A entrada atual —

> Peter Kempthorne et al., '18.S096 Topics in Mathematics with Applications in Finance', MIT
> OpenCourseWare, Fall 2013 (...)

lista Kempthorne como autor principal ("et al." implica ele como primeiro/principal) de um
curso cuja aula especificamente citada na abertura do texto (ainda que sem nome, no corpo) não
é dele. Isso não é "errado" no sentido de o curso não existir ou Kempthorne não fazer parte
dele — ele de fato coordena/leciona parte do curso — mas um leitor que siga a citação até a
fonte primária vai encontrar, na aula relevante, outro nome. **Correção proposta**: trocar
"Peter Kempthorne et al." por uma forma que não implique autoria principal de Kempthorne sobre
o curso inteiro, por exemplo:

> MIT OpenCourseWare, '18.S096 Topics in Mathematics with Applications in Finance', Fall 2013
> (instrutores: Peter Kempthorne, Choongbum Lee, Vasily Strela, Jake Xia; versão atualizada:
> 18.642, Fall 2024)

Isso preserva a citação do curso (correta e útil) sem atribuir autoria enganosa a uma pessoa
específica que não ministrou a aula referenciada no gancho de abertura.

Fonte: [MIT OCW — Lecture 3: Probability Theory](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-3-probability-theory/); [MIT Math — 18.S096 Fall 2013](https://math.mit.edu/classes/18.S096/fall13/). Acesso: 01/09/2026.

---

## 2. Ibovespa e dólar em 16–18/05/2017 (`graf-01`)

Fui direto às fontes primárias, não à imprensa.

**PTAX/dólar comercial (venda, fechamento)** — API pública do Banco Central, série SGS 1
("Taxa de câmbio - Livre - Dólar americano (venda) - diário"), consultada via
`api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados`:

| Data | Câmbio (venda, fechamento) |
|---|---|
| 16/05/2017 | R$ 3,0924 |
| 17/05/2017 | R$ 3,1076 |
| 18/05/2017 | R$ 3,3807 |

Variação 17→18/05: `(3,3807-3,1076)/3,1076 = +8,79%` (recalculado em `python3`).

**Ibovespa (fechamento)** — cruzei duas fontes independentes: histórico diário do índice
`^BVSP` (mirror de dados B3) e múltiplas notícias financeiras da época, que convergem no
mesmo valor:

| Data | Fechamento (pontos) |
|---|---|
| 16/05/2017 | 68.684,00 |
| 17/05/2017 | 67.540,00 |
| 18/05/2017 | 61.597,00 |

Variação 17→18/05: `(61.597-67.540)/67.540 = -8,80%` (recalculado em `python3`) — bate
exatamente com o "-8,80%, maior queda diária desde outubro de 2008" repetido pela imprensa
financeira (InfoMoney, Seu Dinheiro, Cointimes) já levantada em `03-pesquisa.md`.

**Veredito**: ✅ Confirmado, com números agora fechados para o `graf-01` — dólar
3,1076→3,3807 (+8,79%), Ibovespa 67.540→61.597 (-8,80%). Ressalva honesta: não consegui abrir
diretamente a página de "Estatísticas Históricas" da B3 (carrega via JavaScript, `WebFetch`
não renderiza) nem a API Olinda de PTAX (erro de conexão) — a série do Ibovespa vem de um
espelho de dados de mercado (não é a página da B3 em si), e a série cambial vem da API SGS do
Bacen (essa sim é fonte primária direta, número de série 1, documentada em
`dadosabertos.bcb.gov.br`). Recomendo que quem monte o `graf-01` re-confirme o Ibovespa
batendo a série espelhada contra a página da B3 quando o visual for de fato gerado, mas os
dois números convergem entre si e com a imprensa da época — risco residual baixo.

Não há percentual solto na prosa visível do draft atual (`04-draft-v1.md`) — os números só
entram na legenda do `graf-01`, que é onde devem ir os valores acima.

Fontes: [Banco Central — SGS série 1](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados?formato=json&dataInicial=15/05/2017&dataFinal=19/05/2017); Yahoo Finance `^BVSP` histórico diário; [InfoMoney](https://www.infomoney.com.br/mercados/joesley-day-a-delacao-que-colocou-em-xeque-a-agenda-de-reformas-e-fez-o-ibovespa-derreter-mais-de-10/). Acesso: 01/09/2026.

---

## 3. Target forward 2008 — Aracruz, Sadia, volume total de mercado

O parágrafo do draft (linhas ~194-206) já é genérico ("estimado na casa de dezenas de
bilhões de dólares") e **não cita nenhum número específico de Aracruz ou Sadia em prosa** —
o `[VERIFICAR]` inline está pendurado num parágrafo que, na versão atual, não afirma o número
que ele adverte contra. Isso é seguro como está. Ainda assim, fechei os números para o caso de
a consolidação querer adicionar precisão.

**Aracruz — ✅ Confirmado, com fonte primária citável**: `US$ 2,13 bilhões (fair value)`. Achei
o texto literal do Fato Relevante de 03/11/2008 citado dentro de um paper acadêmico revisado
(XVIII Congresso Brasileiro de Custos, 2011, Perera/Reis Neto/Cavalcanti Alves):

> "No dia 3 de novembro a Aracruz divulgou o seguinte Fato Relevante: 'De modo a viabilizar a
> mencionada reestruturação, também nesta data foi concluído o desfazimento da parte mais
> substancial das operações com derivativos até então mantidas com os Bancos, eliminando-se
> 97% da exposição da Companhia a derivativos, com a realização de uma perda total de
> aproximadamente US$ 2,13 bilhões (fair value).'"

Isso também é confirmado independentemente por um artigo acadêmico peer-reviewed em inglês
(*International Journal of Auditing Technology*, 2017): "it posted a derivate loss of US$2.1
billion... the 7th largest derivative loss for all time". **Atenção**: existem outros números
de imprensa (R$2,1bi — Exame; R$2,5bi — RACEF) que **misturam moeda** — são leituras
imprecisas do mesmo fato relatado em dólar, não um número diferente. Se a consolidação citar
um valor, o correto é **US$2,13 bilhões**, não "R$2,1/2,5 bilhões". Não confundir com o
prejuízo líquido *anual* da empresa em 2008 (R$4,194 bilhões, Terra Economia) — métrica
diferente (resultado total do ano, não a liquidação específica dos derivativos), nem com
"R$4,7 bilhões" que aparece no mesmo paper acadêmico como estimativa própria dos autores para
o impacto acumulado de derivativos no resultado operacional ao longo de 2006-2008 (mais uma
métrica distinta — cuidado para não somar coisas diferentes).

**Sadia — ⚠️ dois números legítimos, métricas diferentes, nenhum "R$2,55 bi" exato**:
- Fato Relevante da Sadia foi em **25/09/2008** (data diferente da Aracruz), reconhecendo
  operações "em valores superiores à finalidade de proteção" — o texto do Fato Relevante em
  si, segundo o mesmo paper acadêmico, não traz uma cifra fechada.
- **Despesa financeira com derivativos em 2008: R$2,5 bilhões** (Capital Aberto, "O Caso
  Sadia"), dos quais R$705,9 milhões já realizados (efeito caixa) e R$1,8 bilhão reconhecido
  contabilmente.
- **Prejuízo líquido anual de 2008: R$2,48 bilhões** (primeiro prejuízo anual em 64 anos —
  InfoMoney) — métrica diferente (resultado total do ano, não só derivativos).
- O mesmo paper acadêmico usado para a Aracruz estima, com metodologia própria, "prejuízos de
  2,6 bilhões de reais com derivativos" para a Sadia — uma terceira estimativa, próxima mas
  não idêntica às duas acima.

Se a consolidação optar por incluir um número, recomendo **R$2,5 bilhões em despesas
financeiras com derivativos** (Capital Aberto/Exame), citando explicitamente que é a despesa
financeira, não o prejuízo líquido do ano — e não usar "R$2,55 bilhões" (não encontrei essa
cifra exata em nenhuma fonte).

**Volume total de mercado — 📏 Faixa, não ponto único**. Não existe um "~US$35bi" consensual
único; o que existe é uma faixa de estimativas conforme metodologia/fonte:
- ~US$10 bilhões — estimativa inicial e mais conservadora, atribuída então ao diretor de
  política monetária do Banco Central (via literatura secundária).
- ~US$25 bilhões — estimativa do BIS (Bank for International Settlements), *BIS Quarterly
  Review*, jun/2009 (não consegui abrir o PDF diretamente nesta rodada para citar o número
  exato de página, mas a cifra é referenciada de forma consistente por múltiplas fontes
  acadêmicas).
- **~US$37 bilhões — fonte primária direta, Banco Central do Brasil**, Trabalhos para
  Discussão nº 202 (março de 2010), que eu abri e li via `pdftotext`:

  > "Após pesquisa sobre a posição das instituições financeiras com seus clientes e o
  > cruzamento das mesmas na CETIP S.A. (...) estimou-se que o delta dessas exposições estaria
  > próximo de US$37 bilhões ao final de setembro de 2008."

**Veredito**: `[FAIXA: ~US$35 bilhões → US$25-37 bilhões, conforme metodologia (BIS ~US$25bi;
Banco Central/CETIP ~US$37bi ao final de set/2008, Trabalhos para Discussão BCB nº 202/2010)]`
— se a consolidação quiser um número âncora único, o mais defensável é **"quase US$37
bilhões"** citando diretamente o BCB (fonte primária, não estimativa de imprensa), mas o
enquadramento em faixa é mais honesto dado quanto os números variam por metodologia. O draft
atual, ao dizer apenas "dezenas de bilhões de dólares" sem fixar um número, já está seguro —
não precisa de correção obrigatória, só resolve o `[VERIFICAR]` pendente.

Fontes: Perera, Reis Neto & Cavalcanti Alves, "Derivativos e crise financeira: os custos da
especulação no Brasil — o caso da Aracruz e da Sadia" (XVIII Congresso Brasileiro de Custos,
2011); Capital Aberto, "O Caso Sadia, Parte I"; InfoMoney (Sadia, prejuízo 2008); Terra
Economia (Aracruz, prejuízo anual 2008); Banco Central do Brasil, Trabalhos para Discussão nº
202 (mar/2010). Acesso: 01/09/2026.

---

## 4. LTCM — patrimônio, ativos, alavancagem, nocional, perda, resgate

Fonte primária lida diretamente nesta rodada: **President's Working Group on Financial
Markets, *Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management* (1999)**,
via busca e `WebFetch`, cruzada com **Federal Reserve History, "Near Failure of Long-Term
Capital Management"**.

- **Patrimônio ~US$4,7-4,8 bilhões (início de 1998)** — ✅ Confirmado. PWG usa "the January 1,
  1998, equity capital figure of $4.8 billion"; a literatura secundária mais citada
  (Lowenstein, *When Genius Failed*) usa US$4,72bi, que arredonda para o "~US$4,7bi" do draft.
  Ambos defensáveis, não precisa de correção.
- **Ativos >US$125 bilhões — ✅ Confirmado, e a fonte primária usa exatamente essa
  comparação inter-temporal.** O PWG diz: "the LTCM Fund's balance sheet on August 31, 1998,
  included over $125 billion in assets. Even using the January 1, 1998, equity capital figure
  of $4.8 billion, this level of assets still implies a balance-sheet leverage ratio of more
  than 25-to-1." Ou seja: a própria fonte primária compara patrimônio de janeiro com ativos de
  agosto para ilustrar a alavancagem — não é um erro do draft usar a mesma combinação, é
  literalmente o que o relatório oficial faz.
- **Alavancagem "superior a 25 para 1" — ✅ Confirmado, praticamente citação literal.** "More
  than 25-to-1" no original bate com "superior a 25 para 1" no draft. Recalculei:
  `125/4,8 = 26,0`; `125/4,7 = 26,6` — ambos consistentes com "superior a 25", que é uma
  afirmação de piso (não de valor central), então não há subestimativa aqui. O
  `[VERIFICAR: fontes divergem entre 25:1 e 30:1]` que está no draft pode ser **removido**: a
  frase específica "superior a 25 para 1" está diretamente sourceada e correta; a variação
  para "~30:1" que aparece em outras fontes secundárias vem de usar uma data de corte
  diferente (ex.: patrimônio já reduzido por perdas em agosto), não de a fonte primária
  divergir de si mesma.
- **Nocional "mais de um trilhão de dólares" — ✅ Confirmado, e mais preciso que isso.** O PWG
  dá dois números possíveis: "$1.3 trillion at the end of 1997 and $1.5 trillion at the end of
  1998" (só posições de balcão/OTC); separadamente, para agosto de 1998: futuros >US$500bi +
  swaps >US$750bi + opções/outros OTC >US$150bi, que somados dão bruto ≈US$1,4tri (mistura
  bolsa com balcão, métrica diferente da primeira). **O número "US$1,25 trilhão" que o draft
  havia marcado como não confirmado não aparece em lugar nenhum da fonte primária** — não
  usar. A frase atual do draft ("mais de um trilhão de dólares") é segura e bate com qualquer
  uma das leituras acima; o `[VERIFICAR]` correspondente pode ser resolvido/removido. Se a
  consolidação quiser mais precisão: "cerca de US$1,3 trilhão (fim de 1997)" ou "até US$1,5
  trilhão (fim de 1998)", citando o PWG diretamente.
- **Perda ~US$4,6 bilhões em menos de quatro meses** — ✅ Consistente com múltiplas fontes
  secundárias convergentes (já levantado em `03-pesquisa.md`; não encontrei essa soma agregada
  isolada no texto do PWG nesta leitura, mas não há fonte discordante).
- **Resgate: 23/09/1998, 14 instituições, ~US$3,6 bilhões, sob articulação de William
  McDonough (Fed de Nova York)** — ✅ Confirmado quase literalmente contra o PWG e a Federal
  Reserve History: "fourteen firms agreed to participate in the consortium... invested about
  $3.6 billion in new equity" para ~90% de participação.
- **Calote russo em 17/08/1998** — ✅ Confirmado ("Russia's devaluation of the ruble and
  declaration of a debt moratorium on August 17").
- **David Viniar, CFO do Goldman Sachs, "25-sigma", 2007** — ✅ Confirmado (Financial Times,
  13/ago/2007), e o draft já o trata corretamente como episódio posterior e análogo, não como
  parte do LTCM.

Fontes: [President's Working Group on Financial Markets (1999), via home.treasury.gov](https://home.treasury.gov/system/files/236/hedgfund.pdf); [Federal Reserve History — Near Failure of LTCM](https://www.federalreservehistory.org/essays/ltcm-near-failure). Acesso: 01/09/2026.

---

## 5. Financial Modelers' Manifesto (Derman & Wilmott, 2009)

Consegui extrair o texto completo do PDF original (`emanuelderman.com`) via `pdftotext`
(o `WebFetch` direto retornava binário não processado; baixar e converter localmente
resolveu). Texto original do "Modelers' Hippocratic Oath":

> "I will remember that I didn't make the world, and it doesn't satisfy my equations. Though
> I will use models boldly to estimate value, I will not be overly impressed by mathematics.
> I will never sacrifice reality for elegance without explaining why I have done so. Nor will
> I give the people who use my model false comfort about its accuracy. Instead, I will make
> explicit its assumptions and oversights. I understand that my work may have enormous effects
> on society and the economy, many of them beyond my comprehension."

Comparado ponto a ponto com a paráfrase do draft:

| Original (5 compromissos) | Paráfrase do draft |
|---|---|
| "I didn't make the world, and it doesn't satisfy my equations" | "lembrar que você não criou o mundo, e ele não satisfaz suas equações" |
| "use models boldly to estimate value, ... not be overly impressed by mathematics" | "usar modelos com ousadia para estimar valor, sem se deixar impressionar demais pela matemática" |
| "never sacrifice reality for elegance without explaining why" | "nunca sacrificar realidade por elegância sem dizer explicitamente que fez isso" |
| "not give ... false comfort about its accuracy. ... make explicit its assumptions and oversights" | "não dar a quem usa o modelo falso conforto sobre sua precisão, tornando premissas e omissões explícitas" |
| "my work may have enormous effects on society and the economy, ... beyond my comprehension" | "reconhecer que o trabalho tem efeitos sobre a sociedade e a economia que excedem a própria compreensão" |

**Veredito**: ✅ **Confirmado.** Os cinco compromissos batem, na ordem certa, sem adição nem
omissão de conteúdo. O `[VERIFICAR]` correspondente pode ser removido.

Fonte: Emanuel Derman & Paul Wilmott, [*The Financial Modelers' Manifesto*](https://emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf) (7 jan. 2009). Acesso: 01/09/2026.

---

## 6. London Whale (JPMorgan CIO, 2012)

Fonte primária: consegui acessar o texto da declaração de abertura do senador Carl Levin,
presidente do Permanent Subcommittee on Investigations, no registro oficial da audiência
(mirror em demos.org, texto legível via `pdftotext`), que descreve a mecânica exata:

> "The CIO had been constructing a new VaR model that would lower calculated risk in the SCP.
> It had not yet been properly tested and there was no system in place to transmit data on new
> trades automatically. New trades would have to be manually recorded on a spreadsheet and
> then loaded each night... Nonetheless, CIO put the new VaR model in place at the end of
> January. The apparent risk of the SCP dropped by 50% instantaneously, well below limits.
> Nothing had changed, but the flashing red lights were turned off... instead, the traders used
> the new risk headroom to lay on more trades."

Isso confirma, quase textualmente, a frase do draft: "trocar o modelo de VaR por um novo,
implementado com planilhas Excel e transferência manual de dados, que cortou a estimativa de
perda potencial pela metade e liberou espaço para a mesa continuar aumentando a aposta." —
**"pela metade" bate exatamente com "dropped by 50% instantaneously"** da fonte primária.

**Prejuízo total**: múltiplas fontes convergem em **~US$6,2 bilhões** (Bloomberg Quicktake,
Wikipedia, cobertura consistente). O draft diz "mais de US$6 bilhões" — número seguro e
conservador, não precisa de ajuste, embora "US$6,2 bilhões" seja mais preciso se a
consolidação quiser fechar a casa decimal.

**Veredito**: ✅ Confirmado — mecânica e valor batem com a fonte primária (registro oficial do
Senado) e com a cobertura consolidada do caso.

Fontes: Abertura do Sen. Carl Levin, Senate Permanent Subcommittee on Investigations,
audiência "JPMorgan Chase Whale Trades" (2013), [mirror legível via demos.org](https://www.demos.org/sites/default/files/publications/JPMorganHearing_Demos.pdf); [Bloomberg Quicktake — The London Whale](https://www.bloomberg.com/quicktake/the-london-whale). Acesso: 01/09/2026.

---

## 7. Verificações conceituais

### Hipóteses de Black–Scholes

O draft lista (entre outras coisas, frase que já hedgeia não-exaustividade): movimento
browniano geométrico sem saltos; volatilidade constante; taxa livre de risco constante e
conhecida; ausência de custo de transação e imposto; rebalanceamento contínuo possível;
liquidez ilimitada com venda a descoberto livre e ativos infinitamente divisíveis.

Cruzando com o paper original (Black & Scholes, 1973) e exposições padrão do modelo: as
hipóteses citadas no draft **estão corretas e são um subconjunto real das hipóteses
canônicas**. ⚠️ **Impreciso por omissão, não por erro** — o paper original lista também que
a ação **não paga dividendos** durante a vida da opção e que a opção é **europeia** (só pode
ser exercida no vencimento) — duas hipóteses centrais e frequentemente citadas que o draft não
menciona. Como o texto já se protege com "entre outras coisas", isso não é tecnicamente
incorreto, mas se a consolidação quiser fechar a lista com mais rigor, vale considerar
acrescentar ao menos a hipótese de dividendos (a mais citada de todas em qualquer exposição
didática do modelo).

### VaR (Value at Risk)

Definição do draft: "uma estimativa estatística da perda máxima esperada num horizonte de
tempo, com certa probabilidade". Comparando com a definição-padrão de Philippe Jorion
(referência canônica do campo): "VaR is the maximum loss over a target horizon such that
there is a low, prespecified probability that the actual loss will be larger." A definição do
draft está **alinhada em estrutura** com a de Jorion (perda máxima, horizonte, probabilidade).
Único ponto de atenção: a palavra "esperada" pode, para um leitor mais técnico, soar como se
estivesse falando de "perda esperada" (expected loss/shortfall), que é uma métrica diferente
de VaR (VaR é um quantil-limiar, não uma média condicional). Não é um erro factual — é uma
ambiguidade de leitura possível. ✅ Confirmado como definição válida e usual; nota de estilo,
não de conteúdo, se quiserem trocar "perda máxima esperada" por "perda máxima" simples para
eliminar a ambiguidade.

### 'Convergence trade' e on-the-run/off-the-run

Descrição do draft: títulos recém-emitidos ("on-the-run") mais líquidos, negociando com
prêmio sobre títulos antigos de vencimento quase idêntico ("off-the-run"), mesmo risco de
crédito, aposta na convergência do spread. Isso é exatamente a descrição padrão do trade
clássico do LTCM na literatura (Lowenstein, *When Genius Failed*; PWG 1999) — títulos
on-the-run negociam com yield mais baixo / preço mais alto por causa do prêmio de liquidez, o
LTCM vendia o caro (on-the-run) e comprava o barato (off-the-run), apostando que o prêmio de
liquidez se dissiparia. ✅ Confirmado, sem imprecisão.

### Outros fatos pontuais conferidos de passagem

- **Nobel de 1997 para Scholes e Merton; Fischer Black morto em 1995 ("dois anos antes")** —
  ✅ Confirmado: Black morreu em 30/08/1995 (múltiplas fontes, incluindo o próprio press
  release do Prêmio Nobel de 1997, que registra explicitamente que o prêmio não é concedido
  postumamente). 1995→1997 = dois anos, exato.
- **MacKenzie, *An Engine, Not a Camera* (2006)** — título e ano corretos (MIT Press, 2006),
  bem estabelecido na literatura de sociologia econômica.
- **Smile de volatilidade pós-crash de 1987** — ✅ Consistente com Rubinstein (1994), *Implied
  Binomial Trees*, já levantado em `03-pesquisa.md`; não há nada a corrigir no draft, que
  trata isso qualitativamente, sem número a checar.

---

## Resumo executivo

**Itens verificados nesta rodada**: os 7 pedidos pelo despacho, mais 3 fatos pontuais
conferidos de passagem (Nobel/Black, MacKenzie, smile de 1987) — todos com fonte primária ou,
quando isso não foi possível (BIS Quarterly Review, B3 Estatísticas Históricas), nota
explícita de qual fonte não pôde ser aberta diretamente e por quê.

### `[VERIFICAR]` e `[FAIXA]` para o texto final

1. Bibliografia — trocar "Peter Kempthorne et al." por **"MIT OpenCourseWare, '18.S096 Topics
   in Mathematics with Applications in Finance', Fall 2013 (instrutores: Peter Kempthorne,
   Choongbum Lee, Vasily Strela, Jake Xia; versão atualizada: 18.642, Fall 2024)"** — não é um
   `[VERIFICAR]`, é uma correção direta a aplicar na consolidação.
2. O `[VERIFICAR]` da citação de Kempthorne no corpo do texto (linhas 9-15 do draft) **deve
   ser mantido como está** — a pesquisa e esta verificação convergem em não confirmar a
   atribuição, e a frase já está devidamente hedgeada com "um dos professores".
3. `[FAIXA: ~US$35 bilhões → US$25-37 bilhões, conforme metodologia (BIS ~US$25bi; Banco
   Central/CETIP ~US$37bi ao final de set/2008, Trabalhos para Discussão BCB nº 202/2010)]` —
   só relevante se a consolidação decidir sair do "dezenas de bilhões" genérico atual (que já
   é seguro) para um número mais específico.
4. `[VERIFICAR: fonte primária/regulatória para o volume total de operações target forward no
   Brasil em 2008]` do draft atual **pode ser resolvido** com a fonte primária do BCB
   (Trabalhos para Discussão nº 202) encontrada nesta rodada — não precisa mais ficar em
   aberto, só decidir se vira número único (~US$37bi) ou faixa (item 3 acima).
5. `[VERIFICAR]` do nocional do LTCM ("US$1,25 trilhão não confirmado") **pode ser removido**
   — a frase atual do draft ("mais de um trilhão de dólares") já está confirmada contra a
   fonte primária (PWG 1999: US$1,3tri fim-1997 / US$1,5tri fim-1998); "US$1,25tri" nunca
   apareceu na fonte e não deve ser usado se a consolidação quiser mais precisão — usar
   US$1,3tri ou US$1,5tri, com data.
6. `[VERIFICAR]` de "alavancagem superior a 25 para 1 (fontes divergem 25:1-30:1)` **pode ser
   removido** — a frase específica do draft bate quase literalmente com a fonte primária
   (PWG 1999: "more than 25-to-1"); não é uma divergência de fonte, é uma citação correta de
   um piso, não de um valor central.
7. `[VERIFICAR]` da paráfrase do Financial Modelers' Manifesto **pode ser removido** — os
   cinco compromissos foram conferidos ponto a ponto contra o texto original e batem.

### Correções pontuais recomendadas (não `[VERIFICAR]`, ajuste direto de texto)

8. Se a consolidação adicionar números específicos de Aracruz/Sadia: usar **US$2,13 bilhões**
   (Aracruz, Fato Relevante 03/11/2008) e, para a Sadia, **R$2,5 bilhões em despesas
   financeiras com derivativos** (não "R$2,55 bilhões", cifra que não encontrei em nenhuma
   fonte) — rotulando explicitamente a métrica para não confundir com prejuízo líquido anual.
9. Números confirmados para o `graf-01`: Ibovespa 67.540 (17/05) → 61.597 (18/05), -8,80%;
   dólar (PTAX venda, BCB SGS série 1) R$3,1076 (17/05) → R$3,3807 (18/05), +8,79%.
10. Hipóteses de Black–Scholes: considerar acrescentar "sem pagamento de dividendos" à lista,
    já hedgeada por "entre outras coisas" — não obrigatório, mas é a omissão mais notável
    frente ao paper original.

### Sem necessidade de marcador ou correção

Definição de VaR (alinhada com Jorion); caracterização de 'convergence trade' e
on-the-run/off-the-run; Nobel 1997/morte de Fischer Black em 1995; MacKenzie (2006); smile de
volatilidade pós-1987; patrimônio do LTCM (~US$4,7-4,8bi); resgate do LTCM (14 instituições,
~US$3,6bi, 23/09/1998); calote russo (17/08/1998); perda do LTCM (~US$4,6bi); "25-sigma" de
Viniar (2007, tratado corretamente como episódio análogo e posterior); mecânica e valor do
London Whale (redução de 50% no VaR via planilha manual, >US$6bi de prejuízo).
