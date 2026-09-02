# Pesquisa — Quando os Modelos se Rebelam

Executada pelo agente `pesquisador-editorial` a partir de `00-transcricao.md`,
`01-briefing.md` e `02-estrutura.md`.

## Abertura — a citação de Kempthorne (achado mais importante desta pesquisa)

**A atribuição a Peter Kempthorne é duvidosa e deveria ser tratada como `[VERIFICAR]` de alto
risco antes de publicar.**

Evidência levantada (múltiplas buscas independentes convergindo no mesmo resultado):

- A página de recurso da própria MIT OCW para a *Lecture 3: Probability Theory* (18.S096,
  Fall 2013) — [ocw.mit.edu/.../lecture-3-probability-theory](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-3-probability-theory/)
  e o recurso do PDF de notas [.../mit18_s096f13_lecnote3](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/mit18_s096f13_lecnote3)
  — foram consultadas em três fetches separados; em todos, o instrutor identificado para esta
  aula específica é **Dr. Choongbum Lee**, não Kempthorne.
- O curso 2013 lista quatro instrutores (Kempthorne, Choongbum Lee, Vasily Strela, Jake Xia)
  — [math.mit.edu/classes/18.S096/fall13](https://math.mit.edu/classes/18.S096/fall13/) — mas
  nenhuma página lista explicitamente "quem leciona qual aula" de forma centralizada; a
  evidência de que é Lee vem especificamente da página de recurso da Lecture 3.
- Padrão de conteúdo é consistente com essa divisão: nos PDFs da versão atualizada 2024
  (18.642), vários slides trazem o crédito impresso "Dr. Kempthorne" — mas nas aulas de
  conteúdo **aplicado** (Regression Analysis, Stochastic Processes I, Stochastic Differential
  Equations, Stochastic Calculus —
  [exemplo](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/mit18_642_f24_lec05.pdf)),
  nunca na aula de probabilidade básica.
- Choongbum Lee é matemático puro (grafos aleatórios, teoria de Ramsey —
  [Google Scholar](https://scholar.google.com/citations?user=044QzjcAAAAJ&hl=en)), do MIT
  Math, sem perfil de mercado financeiro — compatível com a Lecture 3 ser descrita como
  "revisão da teoria de probabilidade necessária para o curso" (conteúdo pré-requisito, não
  aplicado). Kempthorne, ao contrário, tem CV de mercado (consultoria financeira desde 1992,
  gestor de portfólio num hedge fund sistemático de US$2,1bi entre 2010-2012 —
  [CV MIT](https://math.mit.edu/documents/uploads/cv/2015_07_20_CV_kempthorne.pdf)), o que
  combina melhor com as aulas aplicadas.
- **Descompasso temático**: a frase do rascunho é dita "no contexto de reversão à média" —
  mas reversão à média é tópico de séries temporais/processos estocásticos, não da aula
  descrita como cobrindo "random variables, probability distributions, and the Central Limit
  Theorem". Evidência circunstancial adicional de que a citação pode vir de outra aula (ou
  outro professor) e ter sido remontada de memória.
- Na versão 2024 (18.642), Choongbum Lee não é mais listado como instrutor (só Kempthorne,
  Strela, Xia), e o vídeo da Lecture 3 aparece como indisponível/restrito na cópia do
  Internet Archive ([archive.org/details/mit18_642f24](https://archive.org/details/mit18_642f24))
  — consistente com Lee ter deixado o MIT e essa aula ter sido retirada da atualização.
- **Não foi encontrado o texto exato da citação** ("se você lança uma moeda 100 vezes...") em
  nenhuma nota de aula, transcrição ou material indexado — é plausivelmente uma fala oral no
  vídeo, não escrita, o que busca textual não confirma nem refuta.

**Recomendação explícita**: isto não pode ser resolvido por busca textual — alguém precisa
assistir ao vídeo da Lecture 3 (2013) e checar quem fala e o que exatamente é dito. Até lá, a
atribuição nominal a Kempthorne é a peça mais frágil do texto inteiro, porque é o gancho de
abertura e nomeia uma pessoa real.

## 1. "Três palavras..." (Derman: teoria/modelo/intuição)

- Confirmação independente da tese central de Derman via podcast Econlib/EconTalk,
  "[Derman on Theories, Models, and Science](https://www.econtalk.org/derman-on-theories-models-and-science/)"
  — reforça a distinção teoria/modelo/metáfora tal como o rascunho já apresenta.
- **Contraponto real e citável**: no mesmo episódio, comentários posteriores atribuídos a
  Eugene Fama corrigem Derman em pontos específicos — caudas gordas em retornos já eram
  conhecidas há décadas antes da crise de 2008; hipótese de mercados eficientes não implica
  CAPM necessariamente; EMH não pressupõe distribuições normais. Economista relevante
  discordando de partes específicas do enquadramento "física vs. finanças" de Derman.
- **Contraponto adicional, não usado no rascunho**: Uskali Mäki,
  "[Performativity: Saving Austin from MacKenzie](https://personal.lse.ac.uk/ROBERT49/teaching/ph232/pdf/Maki-SavingAustinFromMacKenzie.pdf)"
  — filósofo da economia questionando a precisão conceitual do próprio conceito de
  "performatividade" que sustenta a leitura de MacKenzie (usada na seção 3). O rascunho já
  faz esse exercício de auto-crítica para Derman (tabela "ponto de Derman vs. filosofia da
  ciência") mas não para MacKenzie — mesma régua não aplicada aos dois autores.
- George Box, "all models are wrong, but some are useful": a formulação completa não é de
  1976 puro — "all models are wrong" aparece em 1976 (JASA, "Science and Statistics"); a
  formulação completa com "but some are useful" se consolida num paper de 1978 e no livro de
  1987 com Draper (*Empirical Model-Building and Response Surfaces*, p. 424) —
  [fonte](https://blogs.sas.com/content/iml/2025/04/02/all-models-are-wrong.html). Se o post
  datar essa frase, o ano correto depende de qual versão está sendo citada.

## 2. "O radar da rodovia"

Não requer fonte externa — é analogia do próprio autor, sem número a verificar. Nenhuma
pendência de pesquisa aqui.

## 3. Black–Scholes / Joesley Day (`graf-01`)

**Números do pregão 18/05/2017** — confirmados de forma consistente por múltiplas fontes de
imprensa financeira brasileira (não fonte primária/regulador, mas convergentes):
- Intradiário -10,47%, fechamento -8,80% (maior queda diária desde outubro de 2008), dólar
  subindo de ~R$3,14 para ~R$3,38 —
  [InfoMoney](https://www.infomoney.com.br/mercados/joesley-day-a-delacao-que-colocou-em-xeque-a-agenda-de-reformas-e-fez-o-ibovespa-derreter-mais-de-10/),
  [Cointimes](https://cointimes.com.br/bolsa-enfrenta-primeiro-circuit-breaker-desde-joesley-day/),
  [Seu Dinheiro](https://www.seudinheiro.com/2019/empresas/dois-anos-de-joesley-day-relembre-o-terremoto-que-abalou-os-mercados/).
- Divergência a marcar: uma busca indicou máxima intradiária do dólar em R$3,44 e fechamento
  em R$3,3890 (não R$3,38 redondo) — a variação percentual de R$3,14→R$3,38 dá ~7,6%, não
  "8,06%". Etapa 7 deveria puxar a série oficial em vez de reconciliar por aproximação.
- **Fontes primárias candidatas para etapa 7**: B3 —
  "[Índice Ibovespa – Estatísticas Históricas](https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-amplos/indice-ibovespa-ibovespa-estatisticas-historicas.htm)"
  (fechamento em pontos por pregão) e Banco Central —
  [dataset PTAX diário](https://dadosabertos.bcb.gov.br/dataset/dolar-americano-usd-todos-os-boletins-diarios)
  (câmbio oficial por data). Nenhuma das duas foi consultada diretamente nesta pesquisa (só
  via resumos de busca); ambas são as fontes certas para fechar o número com precisão.
- Não encontrada fonte primária da B3 confirmando "primeiro circuit breaker desde 2008" — só
  imprensa secundária repetindo a mesma frase.

**Sorriso de volatilidade (potencial reabertura de visual)**: Rubinstein (1994), *Implied
Binomial Trees*, Journal of Finance — paper acadêmico revisado por pares, estabelece que a
vol implícita pré-crash de 1987 era praticamente plana e que, pós-crash, emergiu um *smirk*
negativo persistente em opções de S&P 500. Working paper do Chicago Fed,
"[Explaining Asset Pricing Puzzles Associated with the 1987 Market Crash](https://www.chicagofed.org/-/media/publications/working-papers/2010/wp2010-10-pdf.pdf)"
tem dados quantificados. Isso contradiz a premissa de `02-estrutura.md` de que "não há dado
quantificado para plotar" — há, sim, se alguém quiser reabrir essa peça (a própria estrutura
já previu essa possibilidade).

**Target forward 2008**:
- Volume total ~US$35 bilhões: aparece em resumos ligados à literatura RACEF/BCB, mas não
  foi possível confirmar a citação primária exata (nem BCB nem CVM) — recomenda-se etapa 7
  buscar diretamente
  "[O mercado de câmbio brasileiro e o desenvolvimento do mercado de derivativos cambiais](https://www.bcb.gov.br/conteudo/relatorioinflacao/EstudosEspeciais/EE41_O_mercado_de_cambio_brasileiro_e_o_desenvolvimento_do_mercado_de_derivativos_cambiais.pdf)"
  (BCB).
- **Aracruz — inconsistência real de unidade monetária entre fontes**: um resumo (via RACEF)
  fala em "R$ 2,5 bilhões"; outro (via Exame) fala em "R$ 2,1 bilhões"; um terceiro fala em
  "US$ 2,13 bilhões (fair value)" e, no mesmo resultado, também usa "R$ 2,13 bilhões" para o
  mesmo número — confusão de moeda até nos resumos automáticos. O prejuízo líquido *total* da
  Aracruz em 2008 foi R$4,194 bilhões
  ([Terra Economia](https://www.terra.com.br/economia/aracruz-fecha-2008-com-prejuizo-de-r-4194-bilhoes,9c8f17a7adc4b310VgnCLD200000bbcceb0aRCRD.html))
  — número bem maior e diferente do prejuízo específico com derivativos, com risco real de
  confundir "prejuízo do ano" com "prejuízo do desmonte das posições". A fonte que resolve a
  ambiguidade é o Fato Relevante da própria Aracruz de 03/11/2008 (não localizado
  diretamente nesta pesquisa).
- **Sadia**: prejuízo líquido anual de R$2,48 bilhões em 2008 (primeiro prejuízo anual em 64
  anos —
  [InfoMoney](https://www.infomoney.com.br/mercados/perdas-cambiais-pesam-e-sadia-reporta-prejuizo-de-r-248-bilhoes-em-2008/))
  e, separadamente, despesa financeira com derivativos de R$2,5 bilhões — nenhum dos dois
  bate exatamente com os "R$2,55 bilhões" do rascunho; próximo, mas não idêntico, com dois
  números candidatos (prejuízo do ano vs. despesa financeira específica) que podem estar
  sendo confundidos.

## 4. LTCM (`diag-01`)

- Fonte mais forte encontrada: Federal Reserve History,
  "[Near Failure of Long-Term Capital Management](https://www.federalreservehistory.org/essays/ltcm-near-failure)"
  (já citada no rascunho) — confirma: patrimônio caiu de US$4,72bi (início de 1998) para
  ~US$600 milhões em setembro; usando o patrimônio de 1º/jan/1998 (US$4,8bi) contra
  >US$125bi em ativos, alavancagem >25:1; 14 instituições aportaram US$3,6bi (outra fonte usa
  US$3,65bi) por ~90% do fundo, sob mediação do Fed de NY; fundo perdeu 44% do valor só em
  agosto de 1998.
- **Variação de alavancagem entre fontes**: outra fonte (resumo de Wikipedia) cita patrimônio
  ~US$5bi e >US$125bi emprestados, alavancagem "aproximadamente 30:1" — não 25:1. A diferença
  entre 25:1 e 30:1 depende do ponto no tempo usado para o patrimônio-base. O "~25:1" do
  rascunho está no limite inferior do que é citado — não é errado, mas merece nota de que a
  razão exata varia por fonte/data de corte.
- **Nocional ~US$1,25 trilhão**: não confirmado diretamente nesta pesquisa — número
  amplamente repetido na cultura geral sobre o LTCM, mas recomenda-se etapa 7 confirmar
  contra o relatório do President's Working Group (1999) — espelho em
  [cftc.gov](https://www.cftc.gov/sites/default/files/tm/tmhedgefundreport.htm) — ou contra
  *When Genius Failed* de Lowenstein diretamente.
- Perda ~US$4,6bi em <4 meses: confirmada de forma consistente em múltiplas fontes.
- David Viniar (CFO do Goldman Sachs), "25-sigma": confirmado — Financial Times, 13/ago/2007,
  no contexto da perda de >25% de valor em uma semana por dois fundos quantitativos do
  próprio Goldman (não é sobre o LTCM — episódio análogo e posterior, de 2007, que o rascunho
  já cita corretamente sem confundir com o LTCM).
  [Reuters Breakingviews](https://www.breakingviews.com/considered-view/goldmans-mr-25-standard-deviation-hard-to-follow/),
  [paper acadêmico "How Unlucky Is 25-Sigma?"](https://arxiv.org/pdf/1103.5672).

**Contraponto genuíno sobre o enquadramento do LTCM** (ausente do rascunho): o rascunho
enquadra o colapso quase inteiramente como "premissa quebrada" (liquidez), não como erro de
julgamento de risco. Há literatura de peso discordando dessa ênfase:
- Cato Institute,
  "[Too Big to Fail? Long-Term Capital Management and the Federal Reserve](https://www.cato.org/sites/cato.org/files/pubs/pdf/bp52.pdf)"
  — argumenta que o resgate criou precedente de risco moral ("too big to fail"), e que o
  próprio Greenspan usou o termo "moral hazard" para descrever o legado do resgate.
- Chicago Fed working paper,
  "[The Costs and Benefits of Moral Suasion: Evidence from the Rescue of Long-Term Capital Management](https://www.chicagofed.org/-/media/publications/working-papers/2002/wp2002-11-pdf.pdf)"
  — análise acadêmica de se o resgate (mediado, não financiado, pelo Fed) foi eficiente.
- O argumento do crítico, resumido: alavancagem 25:1-30:1 é uma **escolha** de gestão de
  risco, não um fato passivo do modelo — dizer "a matemática estava certa, a premissa é que
  quebrou" é uma forma elegante de tirar a responsabilidade da decisão humana de alavancar
  tanto sobre uma correlação estimada historicamente. Esse crítico tem razão num ponto real:
  nada na "premissa de liquidez" obrigava os sócios a operar com 25x; a alavancagem foi
  decisão discricionária, não decorrência do modelo. O rascunho já flerta com isso no
  fechamento ("o LTCM não quebrou por usar modelos; quebrou por aplicar 25 vezes de
  alavancagem"), mas a seção 4 em si narra o evento como se a alavancagem fosse quase
  incidental — vale o texto reconhecer essa tensão, mesmo sem adotá-la.

## 5. As duas patologias — London Whale (JPMorgan, 2012)

- Fonte primária: US Senate Permanent Subcommittee on Investigations,
  "[JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses](https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/031314%20-%20PSI%20JPMorgan%20Whale%20Trades%20Hearing%20and%20Report.pdf)"
  (2013, ~300 páginas) — confirma que o CIO escondeu mais de US$660 milhões em perdas por
  meses via "mismarking" do book, manipulou modelos de risco, ignorou limites, e desinformou
  investidores/reguladores. Recomenda-se etapa 7 puxar o PDF primário para citar a mecânica
  exata do novo modelo de VaR.
- A troca do modelo de VaR via planilha Excel com erro (dividir pela soma em vez da média das
  taxas antiga/nova, que "diluiu" a volatilidade por um fator de 2 e cortou a estimativa de
  risco pela metade) é amplamente reportada, mas por fontes secundárias (blogs técnicos:
  AccountingWeb, Revolution Analytics/Revolutions, ProsperSpark) — consistente com o que o
  rascunho descreve, mas sem confirmação direta do texto do relatório do Senado nesta
  pesquisa.
- Perda total: consistentemente citada como US$6,2 bilhões (ex.:
  [Bloomberg Quicktake](https://www.bloomberg.com/quicktake/the-london-whale)) — o ">US$6bi"
  do rascunho é seguro/conservador.

## 6. Financial Modelers' Manifesto

- Fonte primária localizada —
  [emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf](https://emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf),
  site do próprio Derman — mas a ferramenta de busca retornou o conteúdo como binário não
  processado; não foi possível extrair o texto exato dos cinco compromissos do "juramento"
  nesta sessão. Outras cópias candidatas: SSRN (abstract 1324878), Wilmott.com, e um espelho
  acadêmico da Universidade de Oslo usado como material de ensino. Wikipedia confirma
  metadados (versão resumida na BusinessWeek em dez/2008, versão completa em jan/2009,
  estrutura que ecoa propositalmente o Manifesto Comunista) mas não reproduz o texto dos
  cinco pontos.
- **Recomendação**: etapa 7 precisa baixar o PDF (funcionou como download binário, ~1,5MB) e
  extrair o texto diretamente para checar a paráfrase dos cinco compromissos que o rascunho
  já usa.

## Contrapontos e ângulos ausentes do rascunho (síntese)

1. **Governança de risco de modelo já é lei, não só disciplina pessoal**: Fed/OCC,
   "[SR 11-7 — Supervisory Guidance on Model Risk Management](https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107.pdf)"
   (abril de 2011) formalizou exatamente o espírito da "ficha técnica" do rascunho
   (documentar premissas, validação independente, monitoramento contínuo) como exigência
   regulatória para bancos — não é mais só ethos individual do analista. Ângulo interessante e
   ausente: o London Whale aconteceu **em 2012, um ano depois** dessa exigência já estar em
   vigor — o que complica qualquer leitura de "bastava ter processo" e reforça o ponto do
   próprio rascunho sobre o "cinturão protetor" de Lakatos, mas aplicado a nível
   institucional, não só individual.
2. **A tese de MacKenzie (performatividade) é ela mesma contestada academicamente** — Uskali
   Mäki e trabalho posterior do próprio MacKenzie sobre "contraperformatividade" (2018)
   recuaram da versão mais forte da tese original. O rascunho aplica rigor filosófico à
   distinção de Derman (tabela dedicada) mas usa MacKenzie sem o mesmo tratamento.
3. **LTCM como precedente de "too big to fail"** é discutido pesadamente na literatura de
   regulação financeira, mas nunca aparece no rascunho, que trata o caso puramente como
   "falha de modelo". Ângulo que aprofundaria o fechamento sem contradizer a tese central.
4. **A própria originalidade da citação de Kempthorne é frágil** — mesmo além da questão de
   autoria, a frase ("cara 100 vezes, suspeite da moeda") é um exemplo pedagógico genérico de
   estatística introdutória (atualização bayesiana vs. falácia do apostador); não foi
   encontrado texto único e citável na internet que a torne "de" alguém específico.

## Material aproveitável para os visuais (`ilu-01`, `graf-01`, `diag-01`)

- **`graf-01` (Joesley Day)**: usar como eixos candidatos as séries oficiais de fechamento do
  Ibovespa (B3 — estatísticas históricas) e PTAX (BCB — dataset aberto) para 16, 17 e
  18/05/2017, em vez dos números arredondados de imprensa — evita herdar a pequena
  inconsistência percentual encontrada nesta pesquisa.
- **`diag-01` (ciclo do LTCM)**: a sequência causal já descrita no rascunho (calote russo →
  fuga para qualidade → spreads divergem → chamada de margem → venda forçada → preços
  pioram) está bem sustentada pela Federal Reserve History; os números de anotação mais
  seguros para entrar no diagrama são: patrimônio ~US$4,7-4,8bi, ativos >US$125bi, alavancagem
  >25:1 (citar como "mais de 25 para 1", não fixar em exatos 25:1 dado o range 25-30:1 entre
  fontes), perda ~US$4,6bi, resgate US$3,6bi/14 instituições — evitar usar o nocional de
  US$1,25tri até confirmação (fonte não encontrada nesta pesquisa).
- **`ilu-01` (radar da rodovia)**: nenhum dado externo necessário — é metáfora pura do autor.

## Risco de publicar sem mais checagem (ordem decrescente)

1. **Citação de Kempthorne** — de longe o mais arriscado. Evidência real e repetida aponta
   que a aula específica (*Probability Theory*, 18.S096) foi lecionada por Choongbum Lee, não
   Kempthorne, e o texto da citação não foi localizado em lugar nenhum indexável. É o gancho
   de abertura do post e nomeia uma pessoa real — não deveria ir ao ar sem alguém assistir ao
   vídeo da aula para confirmar quem fala.
2. **Números do target forward 2008 (Aracruz e Sadia)** — segundo mais arriscado. Há confusão
   real de unidade monetária entre fontes para a Aracruz (R$ vs. US$ 2,1-2,5bi) e dois números
   candidatos distintos para a Sadia (prejuízo do ano vs. despesa com derivativos) que não
   batem exatamente com R$2,55bi. O total de mercado de US$35bi também não tem fonte primária
   confirmada nesta pesquisa.
3. **Alavancagem/nocional do LTCM** — risco moderado. O formato geral está bem sustentado
   (Federal Reserve History), mas "25:1" é o extremo inferior de um range citado como 25:1-30:1
   conforme a data de corte do patrimônio, e o nocional de US$1,25 trilhão não foi confirmado
   nesta pesquisa.
4. **Números do Ibovespa/dólar em 18/05/2017** — risco menor mas não nulo: os números centrais
   (-10,47%/-8,80%/R$3,14→R$3,38) são consistentes entre múltiplas fontes de imprensa
   financeira, mas nenhuma delas é fonte primária (B3/BCB), e há um pequeno descompasso
   aritmético (7,6% vs. um possível "8,06%") que vale fechar com a série oficial.

O London Whale (>US$6bi) é o número mais seguro dos citados no rascunho — confirmado de forma
consistente e com margem de segurança na formulação original.
