# Pesquisa — O Papel do CDB na Transformação de Prazos

*Laudo do agente `pesquisador-editorial`, etapa 3 do pipeline. Fontes citadas por afirmação;
o que não pôde ser confirmado com fonte primária vira `[VERIFICAR: ...]`.*

## Seção 1 [Gancho] — O dinheiro que você não pode usar, e o banco também não

**O que a estrutura promete provar:** que existe diferença real, com consequência prática,
entre depósito à vista e CDB, e que a diferença é sobre *controle do uso do dinheiro*, não
sobre rendimento.

Não existe uma norma isolada que diga literalmente "o banco não pode usar livremente o saldo
da sua conta corrente" — essa é uma glosa pedagógica razoável do áudio de origem, mas a base
regulatória real é indireta e composta por duas peças:

1. **Compulsório mais alto sobre depósitos à vista do que sobre depósitos a prazo.** Fonte
   primária lida integralmente: Banco Central do Brasil, Deban/Diban, "Recolhimento
   Compulsório – Quadro Resumo", atualizado em 24.7.2026 (PDF institucional, obtido via
   `site:bcb.gov.br`, arquivo `Resumo_aliquotas_compulsorios.pdf`):
   - **Recursos à Vista: alíquota de 21%** (base normativa: Resoluções BCB 189/2022,
     227/2022, 426/2024, 486/2025, 551/2026).
   - **Recursos a Prazo — inclui a rubrica contábil "4.1.5.10.00.00-3 DEPÓSITOS A PRAZO"
     (onde entra o CDB): alíquota de 20%** (base normativa: Resolução BCB 145/2021,
     426/2024, 551/2026).
   - Confirma quantitativamente que o regulador trata os dois tipos de captação de forma
     diferente — mas o compulsório sobre "à vista" é *maior*, não zero; não é uma proibição
     de uso, é uma retenção percentual.
2. **Classificação de estabilidade de funding no NSFR** (ver seção 5) — depósitos à
   vista/sem prazo definido recebem fator de financiamento estável mais baixo que depósitos
   a prazo de varejo.

**Recomendação para o draft:** manter a distinção como está no áudio (sustentável em
espírito), mas evitar a frase categórica "o banco não pode usar" sem qualificação — o correto
tecnicamente é "o banco pode usar uma fração menor, e sob regras diferentes, do dinheiro em
conta corrente do que do dinheiro em CDB".

`[VERIFICAR: existe alguma norma do Bacen que restrinja literalmente o uso de saldo em conta
corrente, ou essa é uma simplificação pedagógica sustentada apenas indiretamente pelo
compulsório diferenciado (21% vs 20%) e pela classificação de estabilidade no NSFR?]`

## Seção 2 — O que é, de fato, um CDB

**Definição confirmada, fonte quase-primária** (CVM via Portal do Investidor,
`gov.br/investidor`):

> "Os Certificados de Depósito Bancário (CDB) são títulos de renda fixa, representativos de
> depósitos a prazo, emitidos pelos bancos comerciais (e outras instituições financeiras)
> como mecanismos de captação de recursos [...] título de crédito nominativo, transferível e
> de livre negociação, representativo de promessa de pagamento, em data futura, do valor
> depositado junto ao emissor, acrescido da remuneração convencionada."

Fonte: https://www.gov.br/investidor/pt-br/investir/tipos-de-investimentos/titulos-bancarios/certificado-de-deposito-bancario-cdb
(acesso 2026-08-14).

- Base legal: **Lei nº 4.728/1965**, regulamentada por normas do CMN e do Bacen.
- Tipos de remuneração confirmados: prefixada, pós-fixada (indexada ao CDI/DI, a mais comum
  na prática de mercado, mas ver ressalva na seção 3) e híbrida (ex.: IPCA+spread).

**FGC — valores de cobertura:**

- **R$ 250.000,00 por CPF/CNPJ, por instituição associada ou por conglomerado financeiro** —
  confirmado por leitura direta de `fgc.org.br/en/faq` (acesso 2026-08-14): "The maximum
  guarantee is R$ 250,000 per person against the same member institution or all institutions
  within the same financial conglomerate."
- **Teto global de R$ 1 milhão a cada período de 4 anos** — a página oficial dedicada retornou
  404 nas tentativas de acesso direto, mas o valor está corroborado de forma consistente e
  recente por múltiplas fontes jornalísticas de 2026 que cobrem uma mudança regulatória sobre
  o tema — inclusive uma reportagem que resume a decisão do CMN de abril de 2026 e reafirma
  explicitamente que **a cobertura em si (R$ 250 mil / R$ 1 milhão a cada 4 anos) permanece
  inalterada**: Seu Dinheiro, "Conselho Monetário Nacional aperta regras do FGC e impõe novas
  travas a grandes emissões de CDB, LCI e LCA" (abr. 2026),
  https://www.seudinheiro.com/2026/renda-fixa/conselho-monetario-nacional-aperta-regras-do-fgc-e-impoe-novas-travas-a-grandes-emissoes-de-cdb-lci-e-lca-mlim/
  (acesso 2026-08-14).

`[VERIFICAR: número exato da Resolução CMN que instituiu o teto de R$ 1 milhão/4 anos —
buscas apontaram consistentemente para as Resoluções CMN 4.222/2013 e 4.469/2016, mas isso
não foi confirmado por leitura do texto normativo primário, só por snippets de busca;
checar antes de citar o número da resolução no texto, se o draft quiser citá-la]`

**Achado relevante além do pedido — evento regulatório recente e de peso** (uso editorial —
ver Seção "Contrapontos" abaixo): em **novembro de 2025** o Banco Central decretou a
liquidação extrajudicial do **Banco Master** (e ligadas: Master de Investimentos, Letsbank),
após uma estratégia de captação agressiva via CDB — taxas de até **150% do CDI**, usando a
garantia do FGC como argumento de venda. Gerou o **maior acionamento da história do FGC**.
Há divergência de números entre fontes secundárias (algumas falam em R$ 40,6 bi pagos / ~800
mil credores; outras em R$ 51,8 bi de impacto total / ~1,6 milhão de investidores aguardando
ressarcimento; uma cita R$ 60 bi em depósitos cobertos pelo FGC no banco).

`[VERIFICAR: valor oficial do acionamento do FGC no caso Banco Master, número de credores, se
citado no post]`

Fontes secundárias usadas apenas para mapear o fato (não para números finais):
- Seu Dinheiro, "Como o Banco Master entra em 2026..." (2026),
  https://www.seudinheiro.com/2026/empresas/como-o-banco-master-entra-em-2026-da-corrida-por-cdbs-turbinados-a-liquidacao-investigacoes-e-pressao-sobre-o-bc-miql/
- Agência Brasil, "CMN endurece regras para bancos captarem recursos com garantia do FGC"
  (abr. 2026), https://agenciabrasil.ebc.com.br/economia/noticia/2026-04/cmn-endurece-regras-para-bancos-captarem-recursos-com-garantia-do-fgc

Em resposta direta à crise, o **CMN aprovou em 23 de abril de 2026** um pacote de medidas
contra uso do FGC como "trampolim" para captação agressiva, em vigor desde **1º de junho de
2026**: dobra da Contribuição Adicional (CA) de 0,01% para 0,02% quando depósitos cobertos
pelo FGC atingem 60% ou mais da captação por dívida do banco (antes o gatilho era 75%);
criação de um indicador "Ativo de Referência (AR)"; exigência de alocação em títulos públicos
(MATPF) acima de certos múltiplos de patrimônio, com implementação gradual até 2028. Fonte:
Seu Dinheiro (idem acima).

## Seção 3 — O outro lado do balcão: CDB como passivo do banco (ALM)

A definição de ALM (Asset and Liability Management) como "coração financeiro" do banco,
responsável por gerenciar o funding gap (descasamento de prazos), risco de taxa de juros,
risco de liquidez, e o conceito de FTP (funds transfer pricing) para precificação interna de
captação vs. crédito, é amplamente consensual na literatura de gestão bancária — mas as
fontes encontradas são majoritariamente **secundárias/de mercado** (consultorias, blogs
especializados), não um paper acadêmico ou relatório de banco central específico sobre o
tema. Um relatório da PwC sobre ALM em bancos brasileiros (2018) bloqueou acesso (HTTP 403).

**Achado mais forte, fonte primária:** o próprio Banco Central do Brasil usa a expressão
**"processo de transformação de maturidade realizado pelas instituições"** ao explicar a
lógica do NSFR — praticamente a mesma linguagem da tese do post. Fonte primária lida
diretamente: Bacen, *Relatório de Estabilidade Financeira*, abril de 2018, seção 2.6
"Regulamentação do Net Stable Funding Ratio no Brasil", p. 62-63,
https://www.bcb.gov.br/content/publicacoes/ref/201804/RELESTAB201804-secao2_6.pdf
(acesso 2026-08-14):

> "A adoção do NSFR, de forma complementar aos limites de capital e de alavancagem,
> contribuirá para **mitigar excessos no processo de transformação de maturidade realizado
> pelas instituições**, contribuindo para a solidez do sistema financeiro."

Material de alto valor para as seções 3/5: a "transformação de prazos" não é uma metáfora do
post, é linguagem regulatória oficial do Bacen para descrever exatamente o que o post quer
explicar — vale citar essa fonte diretamente no draft.

`[VERIFICAR: exemplo numérico real de descasamento de prazos ("funding gap") de um banco
brasileiro específico — acesso a relatório Pilar 3 bloqueado (HTTP 403); se o draft quiser um
exemplo concreto com números de um banco nomeado, buscar diretamente no site de RI de um
banco público (Itaú, Bradesco, BB, Santander Brasil), seção "Gerenciamento de Riscos / Pilar
3", que costuma ter tabela de descasamento de prazos entre ativos e passivos por faixa de
vencimento]`

## Seção 4 — CDB não é CDI

**Definições confirmadas, fonte primária B3:**
- CDI = Certificado de Depósito Interfinanceiro — títulos emitidos e negociados
  exclusivamente entre instituições financeiras, com prazo de um dia útil (overnight), para
  equilibrar o caixa diário entre bancos.
- **Taxa DI** é calculada e divulgada pela B3 (não é a mesma coisa que "o CDI" — é a taxa
  média das operações de CDI). Metodologia confirmada em: B3, "Metodologia de Apuração da
  Taxa DI",
  https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/di/metodologia-de-apuracao-da-taxa/
  (acesso 2026-08-14):
  - Taxa DI = média ponderada das taxas de operações de DI prefixadas, de um dia útil,
    **extragrupo** (entre conglomerados diferentes), registradas e liquidadas na B3.
  - Desde 1º/10/2018: só é calculada assim se houver ≥100 operações elegíveis **e** volume
    agregado ≥ R$ 30 bilhões no dia; caso contrário, a Taxa DI = Taxa Selic Over do dia.

**Sobre a proporção de CDBs pós-fixados atrelados ao CDI** (ponto que o áudio admite
incerteza): não há estatística oficial (ANBIMA/Bacen/B3) que meça especificamente "que fração
dos CDBs emitidos no Brasil é pós-fixada em CDI". O que foi encontrado:
- Boletim de Credit Research da ANBIMA (via PDF republicado pela Safra, 27/07/2026) menciona
  que, nas **emissões de renda fixa em geral** (não CDB especificamente — inclui debêntures e
  outros instrumentos), **59% foram indexadas a CDI+, 24% a IPCA, 17% a outros indexadores**.
  Direcionalmente consistente com "a maior parte segue o CDI", mas **não é estatística de CDB
  isolado**.
- ANBIMA (via BTG Pactual, dado de junho/2026): estoque agregado de CDBs + LCIs + LCAs + LIGs
  + Letras Financeiras chegou a R$ 5,2 trilhões (crescimento de 6,8% no ano); CDBs
  especificamente cresceram 9,5% no acumulado de 2026 — sem quebra por indexador.
- InfoMoney (dados da Quantum Finance, maio/2026): taxas médias de CDBs por categoria
  (pós-fixado ~99-101% do CDI conforme prazo; IPCA+ ~7,9-8,1%; prefixado ~13,9-14,1% a.a.),
  sem participação percentual do mercado total.

`[VERIFICAR: proporção de CDBs pós-fixados atrelados ao CDI — não há fonte primária
(ANBIMA/Bacen/B3) com esse recorte específico de "CDB" isolado de outros instrumentos de
renda fixa; a afirmação do áudio ("acredito que seja a maior parte") é plausível e
direcionalmente sustentada por dados adjacentes, mas não é estatística confirmável.
Recomendação: (a) retirar a alegação de proporção do texto final, mantendo só a explicação
qualitativa "é comum, mas não universal, que o CDB pós-fixado seja atrelado ao CDI", ou
(b) manter como VERIFICAR explícito]`

## Seção 5 [Clímax] — Por que o banco precisa emitir CDB: a regra que o Bacen impõe

**Compulsório — dado quantitativo primário e atual**, lido diretamente do Bacen (Deban/Diban,
"Recolhimento Compulsório – Quadro Resumo", atualizado em **24.7.2026**):
- **Recursos a Prazo (inclui CDB): alíquota de 20%.** Base normativa: Resolução BCB nº 145,
  de 24.9.2021 (com alterações pelas Resoluções BCB 426/2024 e 551/2026) e Instruções
  Normativas BCB 557/2024 e 715/2026.
  - Cálculo: deduz R$ 30 milhões da base e, em seguida, há faixas de dedução adicional
    conforme o Nível I do Patrimônio de Referência (PR) do banco — dedução de R$ 3,6 bi se
    PR < R$3 bi; R$ 2,4 bi se PR entre R$3-10 bi; R$ 1,2 bi se PR entre R$10-15 bi; zero se
    PR > R$15 bi. Bancos pequenos têm efetivamente uma faixa de isenção maior — informação
    factual não presente no material de origem; avaliar se cabe no post ou é complexidade
    demais.
- **Recursos à Vista: alíquota de 21%** (mais alta que a de prazo). Base normativa:
  Resolução BCB nº 189/2022 e atualizações (227/2022, 426/2024, 486/2025, 551/2026).
- Para contraste: **Depósitos de Poupança: 20%**, com **Direcionamento de Poupança: 65%
  mínimo** obrigatoriamente para crédito imobiliário.

Achado mais forte e mais verificável de todo o laudo — documento oficial vivo, atualizado no
mesmo mês da pesquisa (24/7/2026), com números exatos e norma exata por tipo de captação.

**LCR — fonte primária confirmada:** Resolução CMN nº 4.401, de 27 de fevereiro de 2015, e
Circular BC nº 3.749, de 5 de março de 2015. LCR em vigor desde 2015. Fonte: Bacen, Relatório
de Estabilidade Financeira, abril de 2018, p. 62 (nota de rodapé 96), lido diretamente.

**NSFR — fonte primária confirmada, mesmo documento:**
- **Resolução CMN nº 4.616, de 30 de novembro de 2017** — define o limite mínimo do NSFR e
  condições de cumprimento.
- **Circular BC nº 3.869, de 19 de dezembro de 2017** — dispõe sobre a metodologia de
  apuração do NSFR.
- NSFR = razão entre **ASF (Recursos Estáveis Disponíveis)** e **RSF (Recursos Estáveis
  Requeridos)**; deve ser mantido permanentemente acima de 100% (ASF > RSF).
- Exigível para instituições do **Segmento 1 (S1)** — bancos de maior porte/relevância
  sistêmica internacional — a partir de **1º de outubro de 2018**.
- Padrão internacional do Comitê de Basileia (BCBS), parte do pacote pós-crise de Basileia
  III — confirma o recorte pedido sobre "Basileia III no Brasil".

**Classificação do funding de varejo como "estável":** encontrada apenas em fontes
secundárias especializadas (Dattos, LegisWeb), que citam a Circular BC 3.869/2017 atribuindo
**fator ASF de 90%** para depósitos de varejo sem prazo definido ou com prazo menor que 1
ano, e **95%** para depósitos de varejo com prazo superior a 1 ano. Tentativas de ler o texto
integral da Circular 3.869/2017 diretamente (LegisWeb e anexo de instruções do Bacen)
falharam (timeout / não extraível).

`[VERIFICAR: percentuais exatos de ASF para depósitos de varejo (90%/95%) — corroborados por
duas fontes secundárias técnicas mas não confirmados por leitura direta do texto normativo da
Circular BC 3.869/2017; checar antes de publicar os percentuais exatos, ainda que a ideia
qualitativa — "funding de varejo pulverizado recebe tratamento de maior estabilidade que
funding de atacado" — esteja bem sustentada pela lógica geral do NSFR confirmada na fonte
primária acima]`

## Seção 6 [Resolução] — Onde o CDB entra na carteira

Nenhuma afirmação numérica nova pedida aqui além do que já está no material de origem (ex.:
"CDB prefixado a 11% ao ano" no item 5 da transcrição) — é exemplo ilustrativo do áudio, não
uma taxa de mercado a verificar; se o draft mantiver um número de taxa específico (11% a.a.),
tratá-lo como exemplo hipotético explicitamente rotulado como tal, não como dado de mercado
atual — taxas de CDB variam diariamente com a Selic/CDI.

## Contrapontos e o que falta na cobertura padrão

**Como o mercado/educação financeira trata o CDB hoje:** revisão de conteúdo de XP, Toro,
Genial, InfoMoney, Serasa, Itaú Corretora. Esse material converge em cobrir bem: definição,
indexadores, proteção do FGC, risco de crédito do emissor (a maioria já deixa claro que "quem
garante não é a corretora, é o banco emissor"), liquidez.

**O que praticamente nenhum desses textos explica** (confirma o diferencial genuíno da tese
do post): **por que, do ponto de vista do banco, é estruturalmente necessário emitir CDB** —
a conexão entre compulsório, LCR/NSFR e a necessidade de captação, mesmo quando o banco
"parece" ter caixa disponível. A cobertura de mercado trata o CDB quase exclusivamente pela
ótica do investidor (retorno, risco, liquidez) e raramente pela ótica regulatória do emissor.
O ângulo "transformação de prazos como explicação estrutural, não comercial" é, de fato, pouco
explorado no conteúdo padrão — o post tem diferencial real, não apenas percebido.

**Contraponto genuíno para a crítica estrutural e verificação técnica:** o material de origem
(`00-transcricao.md`, seção 1) descreve o FGC como conferindo ao CDB um "baixíssimo risco de
crédito estrutural". Tecnicamente correto *quanto ao valor final ressarcido até R$ 250 mil*,
mas a experiência recente e amplamente noticiada do caso Banco Master (liquidação em novembro
de 2025, o maior acionamento da história do FGC) mostra que a proteção do FGC **não elimina
fricção prática real**: atraso (mais de um mês, segundo reportagens, só para fechar a lista de
credores), suspensão de rendimento durante o processo de liquidação, e, para valores acima do
teto, perda efetiva de capital. Isso não invalida a tese do post, mas é contraponto genuíno a
qualquer frase que soe como "CDB com FGC é livre de risco" sem qualificação — publicação em
agosto de 2026, poucos meses depois do evento mais visível de quebra bancária com CDB da
história recente do país. Recomenda-se que a crítica estrutural (etapa 5) e a verificação
técnica (etapa 7) decidam deliberadamente se e como qualificar essa frase — mesmo que o post
não cite o caso Banco Master pelo nome (decisão editorial válida, dado que é caso ainda sob
investigação/litígio).

## Resumo de todos os itens `[VERIFICAR]`

1. Frase-gancho "o banco não pode usar livremente o saldo da conta corrente" — sustentada
   apenas indiretamente (compulsório 21% vs 20%, classificação NSFR); não há vedação legal
   explícita nesses termos.
2. Número da(s) Resolução(ões) CMN que instituíram o teto de R$ 1 milhão/4 anos do FGC
   (buscas sugerem 4.222/2013 e 4.469/2016, não confirmado em leitura primária).
3. Valor oficial (FGC) do acionamento no caso Banco Master e número de credores — fontes
   secundárias divergem (R$ 40,6 bi/800 mil vs. R$ 51,8 bi/1,6 milhão vs. R$ 60 bi em
   depósitos cobertos).
4. Proporção de CDBs pós-fixados atrelados ao CDI — sem fonte primária com esse recorte
   específico (só há dado agregado de renda fixa em geral: 59% CDI/24% IPCA/17% outros,
   ANBIMA jul/2026).
5. Exemplo numérico real de descasamento de prazos (funding gap) de um banco brasileiro
   nomeado — não obtido (bloqueio de acesso ao relatório Pilar 3 consultado).
6. Percentuais exatos de ASF (90%/95%) para depósitos de varejo na Circular BC 3.869/2017 —
   corroborado só por fontes secundárias técnicas, não por leitura direta do normativo.

## Fontes primárias mais fortes obtidas (para reuso nas etapas 7 e 8)

- Bacen, Deban/Diban, *Recolhimento Compulsório – Quadro Resumo*, atualizado 24.7.2026 (lido
  integralmente, PDF) — compulsório 20% recursos a prazo / 21% à vista / 20% poupança / 65%
  direcionamento poupança.
- Bacen, *Relatório de Estabilidade Financeira*, abril de 2018, seção 2.6,
  https://www.bcb.gov.br/content/publicacoes/ref/201804/RELESTAB201804-secao2_6.pdf —
  definições de LCR/NSFR, normas exatas, e a frase "transformação de maturidade realizado
  pelas instituições".
- CVM/Portal do Investidor, definição de CDB:
  https://www.gov.br/investidor/pt-br/investir/tipos-de-investimentos/titulos-bancarios/certificado-de-deposito-bancario-cdb
- B3, Metodologia de Apuração da Taxa DI:
  https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/di/metodologia-de-apuracao-da-taxa/
- FGC, FAQ (valores de cobertura): https://fgc.org.br/en/faq
- Seu Dinheiro, cobertura da reforma do CMN de abril/2026 e do caso Banco Master (contexto
  regulatório mais recente e relevante para a seção de regulação).
