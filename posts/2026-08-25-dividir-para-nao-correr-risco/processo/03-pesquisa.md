# Laudo de pesquisa — "Dividir para não correr risco"

Pesquisa feita pelo agente `pesquisador-editorial`. Estrutura abaixo espelha `02-estrutura.md`.

---

## 1. "O que uma LCI realmente faz" (gancho + contexto) — Banco Master

Não encontrei motivo para questionar os fatos-base já usados (liquidação extrajudicial em nov/2025, desembolso do FGC perto de R$ 44 bi). Múltiplas fontes de imprensa e institucionais (Agência Brasil, Poder360, Contec Brasil, MercGroup) tratam o caso Master como consenso factual, sem controvérsia sobre a ordem de grandeza. Não fiz reconstrução forense adicional do caso — a estrutura já pede explicitamente que isso fique fora do escopo (§ "O que fica de fora"), então não insisti nesse ponto.

## 2. "O que é a LCI, rapidamente" (contexto)

- **Quem pode emitir**: confirmado por múltiplas fontes — bancos comerciais, múltiplos com carteira imobiliária, Caixa, sociedades de crédito imobiliário, associações de poupança e empréstimo, companhias hipotecárias e demais autorizadas pelo BC (Lei nº 10.931/2004, art. 12). A entrada das SCFIs ("financeiras") é confirmada com data específica: **1º de julho de 2025**, via **Resolução BCB nº 471/2025** — o rascunho diz só "desde 2025", o que está certo mas poderia ganhar precisão de data/norma na etapa 7. ([Okai](https://okai.com.br/blog/financeiras-agora-podem-emitir-lci-aumento-da-concorrencia-e-estimulo-ao-credito-imobiliario), acesso 25/08/2026)
- **Isenção de IR / MP 1.303/2025**: confirmado que a MP propunha tributar (5% a 7,5%) novas emissões de LCI/LCA/CRI/CRA/debêntures incentivadas, e que caducou sem virar lei. Há **divergência de data entre fontes** sobre quando exatamente caducou — uma fonte diz "caducou em agosto de 2025" (prazo constitucional de 120 dias vencido), outra diz "perdeu a validade em 08/10/2025" após votação de retirada de pauta (251 x 193). O rascunho não cita data específica de caducidade, então isso não é um problema para o texto como está — mas sinalizo a divergência para a etapa 7 caso alguém queira adicionar uma data. ([InfoMoney](https://www.infomoney.com.br/minhas-financas/mp-1-303-cai-no-congresso-veja-como-fica-a-tributacao-dos-investimentos-agora/), [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2025/10/07/com-placar-apertado-comissao-mista-aprova-mp-para-compensar-iof), acesso 25/08/2026)
- **Carência mínima**: confirmado o histórico completo dos prazos: Resolução CMN nº 5.119/2024 **aumentou** a carência mínima da LCI de 3 para 12 meses (fev/2024); Resolução CMN nº 5.215/2025 (22/05/2025) **reduziu** de volta para 6 meses para LCI pós-fixada/prefixada, mantendo 36 meses para títulos atualizados por índice de preços. Isso bate exatamente com o que o rascunho descreve na seção 4 (recuo do estoque após 5.118/5.119, depois "redução da carência mínima trazida pela Resolução CMN nº 5.215/2025"). ([LegisWeb](https://www.legisweb.com.br/legislacao/?id=478582), [ABBC](https://abbc.org.br/resolucao-cmn-no-5-215-2025-ajuste-nos-prazos-minimos-de-vencimento-da-lci-e-da-lca/), [SABZ Advogados](https://www.sabz.com.br/publicacoes-banco/consultivo-prazo-de-lci-e-lca-cai-de-9-para-6-meses), acesso 25/08/2026)
- **"O que qualquer material de corretora conta"**: confirmado. Amostras de Genial, Grafeno, XP e outras corretoras (busca por título/resumo, não fetch completo — dois fetches deram 403) tratam a LCI nesse nível básico (tipos de rentabilidade, isenção, FGC), sem entrar na distinção estrutural CRI/LIG/LCI que o texto explora depois.

## 3. "Por que o banco emite LCI" (ação crescente + clímax) — o argumento central

### O "mito" que o texto ataca é real, não espantalho

Encontrei confirmação de que a narrativa "o banco compartilha a rentabilidade do crédito imobiliário com você" — ou variações próximas — de fato circula em material de mercado, embora raramente com essas palavras exatas. O exemplo mais próximo e citável:

> "A isenção de imposto é um benefício fiscal criado pelo governo para estimular o financiamento dos setores imobiliário e agrícola [...] Ao oferecer isenção de IR, o governo atrai mais investidores, os bancos captam mais recursos e conseguem financiar esses setores com taxas melhores. [...] Ao captar um grande volume de dinheiro por meio de LCIs e LCAs, os bancos são obrigados por lei a direcionar esses recursos especificamente para financiar projetos do setor imobiliário."

Essa é a versão "governo incentiva, banco repassa o benefício" — irmã da "versão hollywoodiana" que o texto nomeia, embora enquadrada mais em política pública do que em "favor do banco". (fonte agregada via busca, sem link único e assinado — não é uma fonte forte o suficiente para citar no post, mas confirma que o enquadramento existe e é comum; acesso 25/08/2026)

Ao mesmo tempo, encontrei material de mercado que **já** faz a distinção correta que o texto defende — ou seja, o "mito" não é universal, há literatura de qualidade média/alta que já acerta:

> "O risco primário ao investir em LCI é o risco de inadimplência por parte da Instituição Financeira emissora da LCI [...] embora a LCI seja lastreada em créditos imobiliários, o risco real que o investidor assume é o da instituição financeira emissora, não dos tomadores de crédito imobiliário."

Isso é um dado relevante para o draft: o texto pode (se quiser) reconhecer que nem toda explicação de mercado é "hollywoodiana" — algumas corretoras já acertam o risco de crédito do banco emissor, mas praticamente nenhuma delas conecta isso à taxonomia CRI/LIG/LCI (segregação patrimonial, patrimônio de afetação) que dá o "porquê" estrutural. Esse é provavelmente o ângulo genuinamente original do texto, mais do que a correção do risco em si.

### Taxonomia CRI / LIG / LCI

Confirmada em todos os pontos que pesquisei:

- **CRI** (Lei nº 9.514/1997): emissão exclusiva de companhias securitizadoras (sociedades por ações, não financeiras), que adquirem os créditos por cessão e podem instituir regime fiduciário sobre eles para lastrear o CRI — segregação patrimonial via regime fiduciário, confirmado. ([normaslegais.com.br](https://www.normaslegais.com.br/legislacao/tributario/l9514.htm), [ABSIA](https://absia.org.br/lei-no-9-514-97/), acesso 25/08/2026)
- **LIG** (Lei nº 13.097/2015): confirmado "duplo recurso" — o investidor pode acionar tanto a carteira de ativos segregada (patrimônio de afetação, regime fiduciário registrado em depositário central) quanto o patrimônio do banco emissor em caso de insuficiência da carteira. Composição da carteira: créditos imobiliários garantidos por hipoteca/alienação fiduciária/incorporação sob regime de afetação (Lei 4.591/64), títulos públicos, derivativos e outros ativos autorizados pelo CMN. ([Colégio Notarial do Brasil](https://www.notariado.org.br/lei-13-09715-cria-a-letra-imobiliaria-garantida-lig/), [ConJur](https://www.conjur.com.br/2015-mar-03/julianna-albino-lei-1309715-cria-letra-imobiliaria-garantida), acesso 25/08/2026)
- **LCI** (Lei nº 10.931/2004, art. 12 e seguintes): confirmado que a lista de emissores e o requisito de lastro batem com o texto.

### Ho & Saunders (1981)

Citação confirmada corretamente: Ho, Thomas S. Y.; Saunders, Anthony. "The Determinants of Bank Interest Margins: Theory and Empirical Evidence." *Journal of Financial and Quantitative Analysis*, v. 16, n. 4, 1981, p. 581-600. Modelo do banco como "dealer avesso a risco" (risk-averse dealer) confirmado como descrição correta do paper original — é a leitura padrão da literatura, amplamente citado como trabalho seminal sobre margem bancária. ([JSTOR](https://www.jstor.org/stable/2330377), [IDEAS/RePEc](https://ideas.repec.org/a/cup/jfinqa/v16y1981i04p581-600_00.html), acesso 25/08/2026). Nenhum anacronismo detectado.

### "Trampolim" — ponto de atenção para a etapa 7

O rascunho afirma: *"o próprio Banco Central reconheceu, por escrito, que bancos vinham usando a garantia do FGC como 'trampolim' de captação"*. Não encontrei essa palavra em nenhuma nota oficial, resolução ou comunicado do BC/CMN citado diretamente — em todas as fontes que localizei, "trampolim" aparece como **caracterização jornalística**, não citação textual do regulador:

> "As novas regras [...] são um recado claro do Banco Central para que instituições financeiras não repitam o modus operandi de usar o FGC como trampolim para captar recursos com taxas altas, como o Banco Master fez." (Seu Dinheiro, comentário editorial do jornalista, não citação direta)

Isso é diferente de "o Banco Central reconheceu, por escrito". O conteúdo regulatório em si — a lógica de conter o *moral hazard* de captação ancorada na garantia do FGC — está confirmado (ver seção 5 abaixo), mas a atribuição da palavra "trampolim" ao próprio BC, em documento oficial, **não encontrei fonte primária que sustente**. Recomendo à etapa 7 verificar se existe, em nota técnica ou exposição de motivos da Resolução 5.295/5.296, uso literal dessa palavra ou similar (ex.: "moral hazard", "uso indevido da garantia") — ou então o draft deveria atribuir a formulação a "a leitura do mercado sobre a resolução" em vez de ao Banco Central diretamente.

## 4. "Quanto a LCI movimenta no mercado" (resolução — escala) — dados B3

Encontrei fonte direta (B3/Bora Investir, o canal educacional oficial da B3) para praticamente toda a série que o rascunho usa, com pequenas variações de arredondamento a checar na etapa 7:

| Período | Estoque LCI | Fonte |
|---|---|---|
| dez/2020 | R$ 141 bi | busca agregada (sem link único assinado — **fonte fraca**, recomendo a etapa 7 tentar achar o release B3 original de 2020/2021) |
| jan/2024 | R$ 373 bi (citado no rascunho) | não verificado por fonte própria nesta pesquisa |
| abr/2024 | R$ 362 bi (citado no rascunho, recuo pós-Resolução 5.118/5.119) | não verificado por fonte própria nesta pesquisa |
| 2023 (fim) | R$ 360 bi | busca agregada |
| 2024 (fim) | R$ 350 bi (alta de 15% sobre 2023) | [Bora Investir/B3](https://borainvestir.b3.com.br/tipos-de-investimentos/renda-fixa/cdb/cdb-lci-lca-e-lf-estoque-de-produtos-de-captacao-bancaria-na-b3-cresceu-17-em-2025/) |
| 2025 (fim) | **R$ 508,8 bi**, alta de **29%** no ano (maior crescimento entre os produtos) | mesma fonte B3, confirmado literalmente |
| jun/2025 | R$ 454 bi | Suno/Forbes (citando B3), acesso 25/08/2026 |
| jun/2026 | **R$ 544 bi**, alta de 20% sobre jun/2025 | [Suno](https://www.suno.com.br/noticias/b3-b3sa3-renda-fixa-captacao-bancaria-cdb-lci-lca-mt/) (citando release B3 do 1º semestre de 2026), acesso 25/08/2026 |

Note a pequena inconsistência interna: R$ 350 bi (fim de 2024, fonte B3) vs. R$ 373 bi (jan/2024) e R$ 362 bi (abr/2024) citados no rascunho — se jan/2024 é R$ 373 bi e o fim de 2024 é R$ 350 bi, o estoque teria **caído** ao longo de 2024, o que contradiz a narrativa "recuo em fev/2024, depois retomada". Vale a etapa 7 reconciliar essas três cifras contra a série completa da B3 (idealmente pegar o release trimestral/mensal direto do site da B3, não via imprensa).

Estoque total de produtos de captação bancária (CDB+LCI+LCA+LF) confirmado: **R$ 4,2 tri (2024) → R$ 4,9 tri (2025), alta de 17%**; **R$ 6,3 tri em jun/2026 (alta de 13% no semestre vs. R$ 5,6 tri em jun/2025)**. ([Bora Investir/B3](https://borainvestir.b3.com.br/tipos-de-investimentos/renda-fixa/cdb/cdb-lci-lca-e-lf-estoque-de-produtos-de-captacao-bancaria-na-b3-cresceu-17-em-2025/), [Suno](https://www.suno.com.br/noticias/b3-b3sa3-renda-fixa-captacao-bancaria-cdb-lci-lca-mt/), acesso 25/08/2026)

Composição ao final de 2025 confirmada em detalhe, e bate com o rascunho, mas com um produto a mais que o rascunho não menciona:
- CDB: R$ 2,8 tri (alta de 13%)
- LCA: R$ 599,9 bi (alta de 16%)
- LCI: R$ 508,8 bi (alta de 29%, maior crescimento)
- **Letra Financeira (LF): R$ 976,8 bi (alta de 24%)** — o rascunho, na frase "o estoque de produtos de captação bancária registrados na B3 (CDB, LCA, LCI e Letra Financeira) somava R$ 4,9 trilhões", já lista corretamente os quatro produtos, então está certo — só não recalcula o % de LF. A conta "LCI perto de 10% do total" do rascunho confere: 508,8/4.900 ≈ 10,4%.

Em jun/2026, CDB especificamente estava em **R$ 2,7 tri** (alta de 8% sobre R$ 2,5 tri em jun/2025) — nota que este número é menor que o R$ 2,8 tri de fim de 2025, o que é plausível (flutuação trimestral) mas vale conferência na etapa 7 se o post citar o número de jun/2026 para CDB.

## 5. "Onde a LCI entra no seu portfólio" — os dois marcadores `[VALIDAR]`

### Faixa de equivalência (LCI 90% CDI ↔ CDB X% CDI)

**Confirmado com segunda fonte independente, e com a mecânica exata**: a tabela regressiva de IR (vigente desde 2005, aplicável a CDB, Tesouro Direto, LC, LF e debêntures comuns) tem 4 faixas:
- até 180 dias: 22,5%
- 181–360 dias: 20%
- 361–720 dias: 17,5%
- acima de 720 dias: 15%

Aplicando a fórmula de gross-up do próprio rascunho (taxa bruta = rendimento líquido ÷ (1 − alíquota)) a uma LCI de 90% do CDI:
- alíquota 15% (prazo > 2 anos): 90 ÷ 0,85 = **105,9% do CDI**
- alíquota 22,5% (prazo ≤ 180 dias): 90 ÷ 0,775 = **116,1% do CDI**

Isso confirma a faixa **105% a 118%** do rascunho como aproximadamente correta, mas o cálculo exato dá **105,9% a 116,1%**, não 118%. A diferença é pequena (menos de 2 pontos percentuais no teto), mas a etapa 7 deveria decidir se ajusta o número para "105% a 116%" (mais preciso) ou mantém "105% a 118%" como arredondamento intencional (o rascunho já tem `[VALIDAR: os exemplos variam com o CDI vigente; não citar como faixa fixa]`, o que sugere que o autor já sabia que era aproximado). Fontes: tabela regressiva confirmada por múltiplas corretoras (Santander, XP, Rico, Safra) de forma consistente entre si; cálculo de gross-up confirmado por calculadoras de mercado (investidortop.com.br, brapi.dev, meelion.com) que chegam ao mesmo resultado. ([Bora Investir/B3 — glossário tabela regressiva](https://borainvestir.b3.com.br/glossario/tabela-regressiva-do-imposto-de-renda/), [XP](https://conteudos.xpi.com.br/aprenda-a-investir/relatorios/tabela-regressiva/), acesso 25/08/2026)

### "Em prazos muito longos, a comparação pode virar a favor do CDB"

Aqui é preciso uma correção conceitual importante para o draft, não só uma segunda fonte. A alíquota de IR do CDB **não continua caindo** em prazos muito longos — ela **atinge o piso de 15% aos 720 dias (2 anos) e para aí**. Não existe uma quinta faixa abaixo de 15% para prazos de 5, 10, 20 anos. Então a frase do rascunho, se lida como "a alíquota continua caindo com o prazo", está tecnicamente errada sobre o mecanismo.

O que **de fato acontece**, e que encontrei confirmado (embora por fontes de blog de corretora, qualidade média — não achei fonte regulatória ou acadêmica de segunda camada) é outro mecanismo, diferente do que "alíquota cai mais": em prazos longos, bancos costumam oferecer **percentuais de CDI mais altos em CDB do que em LCI** (o gap de taxa entre os dois produtos se abre, não porque a alíquota do CDB caia mais, mas porque o banco precifica de forma diferente e a LCI para prazos longos costuma pagar percentuais de CDI relativamente mais baixos). Um exemplo concreto (fonte de blog, citar com cautela): "as LCIs atreladas ao CDI com prazo de 12 meses caíram de 94,41% do CDI em 2025 para 88% em 2026" — se verdadeiro, mostra o CDI% da LCI comprimindo, o que jogaria a comparação a favor do CDB não pela alíquota, mas pela taxa ofertada. Encontrei também a heurística de mercado: "para prazos acima de 720 dias (IR 15%), o ponto de equilíbrio cai para ~85% do CDI — qualquer LCI acima disso supera o CDB [a 100% do CDI] em termos líquidos" — isto é, mesmo no piso de alíquota, uma LCI de 90% do CDI ainda bate um CDB de 100% do CDI; só perde se o CDB oferecido tiver taxa nominal comparativamente mais alta que o normal (110%+ do CDI). **Nenhuma dessas fontes é regulatória ou acadêmica — são blogs/calculadoras de corretora, a mesma categoria de "única fonte de mercado" que o rascunho já sinaliza como insuficiente.** Não encontrei uma fonte de qualidade superior (BCB, Anbima, artigo técnico assinado) que trate especificamente desse ponto de virada.

**Recomendação explícita para a etapa 4/7**: o mecanismo correto a expressar, se o texto mantiver essa frase, não é "a alíquota cai o suficiente" (que sugere queda contínua e é tecnicamente falso além de 2 anos), e sim algo como "a partir de 2 anos a alíquota do CDB já bateu no piso de 15% e não cai mais — e a essa altura, dependendo das taxas de CDI% que o banco está oferecendo em cada produto naquele prazo específico, a vantagem pode passar para o CDB". Isso é uma correção de mecanismo, não só de fonte — vale reportar como achado central desta pesquisa.

## 6. Contrapontos genuínos

**O contraponto mais forte que encontrei** (e que o briefing já antecipa como possível): a ideia de que a exigência regulatória de lastro em crédito imobiliário **de fato direciona capital** para o setor de um jeito que não aconteceria sem o instrumento — tornando "é favor" (ou "incentivo de política pública", mais precisamente) menos errado do que o texto admite. Isso aparece explicitamente em material de mercado mainstream, não é uma posição marginal:

> "Ao captar um grande volume de dinheiro por meio de LCIs e LCAs, os bancos são obrigados por lei a direcionar esses recursos especificamente para financiar projetos do setor imobiliário [...] Como ambos os setores [...] são considerados estratégicos para a economia brasileira, o governo oferece um incentivo para quem investe nesses papéis." (fonte agregada de busca, qualidade média, acesso 25/08/2026)

Essa é uma crítica genuína e coerente: o argumento do texto ("não é favor, é spread") é correto sobre **de quem é o risco** (o argumento central e mais forte da estrutura), mas é potencialmente incompleto sobre **por que o produto existe do ponto de vista regulatório** — a isenção de IR e a exigência de lastro são, sim, desenho de política pública para baratear crédito imobiliário, mesmo que a mecânica de risco dentro do produto seja "spread comum de intermediação financeira" como o texto descreve. Ou seja: "é spread" explica o risco; não explica sozinho por que o Estado subsidiou esse spread especificamente com isenção fiscal. Um crítico diria que o texto conflou duas perguntas diferentes — "de quem é o risco" (resposta: do banco) e "por que esse produto existe e é incentivado" (resposta: política de crédito direcionado) — e resolveu só a primeira, tratando isso como se resolvesse a segunda também.

Não encontrei uma fonte acadêmica formal (paper, working paper do BC) que faça esse argumento explicitamente sobre a LCI — o achado é de material de mercado/educacional, o que enfraquece um pouco a força do contraponto como "literatura", mas não como posição de mercado real.

Um segundo contraponto menor, mais técnico: alguém poderia argumentar que a proteção do FGC até o teto **é**, na prática, uma forma de "favor" socializado (o custo do FGC é rateado entre todas as instituições associadas, via contribuição compulsória) — ou seja, mesmo aceitando "é spread" para o banco individual, o sistema como um todo subsidia o risco de crédito bancário via um fundo mutualizado, o que é outra camada de "favor" que o texto não menciona. Não encontrei essa formulação exata em nenhuma fonte específica — é uma inferência a partir de como o FGC é financiado (contribuição mensal das associadas), não uma citação de terceiro. Sinalizando como possível ângulo, não como achado com fonte.

## 7. O que ninguém está dizendo — Resolução CMN 5.295/5.296 e efeito pós-junho/2026

Confirmado o conteúdo técnico da resolução: entrou em vigor em **1º de junho de 2026** (aprovada em 23/04/2026, regulamentada pelo BC em 29/05/2026). Cria o **Ativo de Referência (AR)** — indicador de qualidade/liquidez/diversificação dos ativos da instituição — e obriga alocação em títulos públicos federais quando o Valor de Referência (captações garantidas pelo FGC) ultrapassa o AR, ou seis vezes o Patrimônio Líquido Ajustado e 80% das Captações de Referência, ou dez vezes o PLA. Dobra o multiplicador da Contribuição Adicional ao FGC para 0,02%. ([MercGroup](https://www.mercgroup.com.br/insights/fgc-cmn-5295-bcb-novo-regime-bancos-medios-2026), [Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-04/cmn-endurece-regras-para-bancos-captarem-recursos-com-garantia-do-fgc), acesso 25/08/2026)

**Mas o efeito prático ainda é mínimo neste momento (ago/2026)**: os fatores de alocação compulsória são escalonados e começam em **0,05 (5%) em julho de 2026**, subindo gradualmente até **1,00 (100%) só em julho de 2028**. Não encontrei nenhum dado de mercado (estoque de LCI, spread, taxas ofertadas) **posterior à implementação** que já mostre efeito mensurável da norma — é cedo demais, o fator inicial é pequeno, e o release da B3 de jun/2026 (R$ 544 bi, ainda em alta de 20% no ano) é de antes da resolução entrar em vigor.

Isso é exatamente a lacuna que o briefing já perguntava sobre: **não há, até a data desta pesquisa, dado verificável de que a resposta regulatória já esteja "sendo sentida" no mercado** — o que existe é a norma em vigor e um cronograma de escalonamento de quatro anos. Se o draft quiser fechar o arco com "a resposta veio poucos meses depois" (o que é factualmente correto — abr/2026 é ~5 meses depois de nov/2025), ele **não deveria** insinuar que o efeito de mercado já apareceu nos números, porque isso não foi confirmado e a mecânica da própria norma (fator de 0,05 em jul/2026) sugere que ainda não apareceria de forma visível nos R$ 544 bi de jun/2026 (que são, aliás, anteriores à vigência da norma). Recomendo ao draft ficar em "a norma existe e nomeia oficialmente o mecanismo" sem alegar efeito já observado no estoque.

Um ângulo que também não vi ninguém conectar explicitamente: a resolução usa linguagem técnica de **liquidez e diversificação de ativos**, não de "vedar o modelo de negócio Master" — ou seja, ela ataca o sintoma (concentração de captação garantida por FGC sem lastro de qualidade) sem impedir que um banco continue captando via LCI/CDB a taxas acima de mercado, contanto que aloque o excedente em títulos públicos. Isso é coerente com "o risco muda de endereço, não desaparece" (o mote do texto) — mas também mostra que a resposta regulatória, tecnicamente, não elimina o mecanismo descrito no texto, apenas o encapsula. Pode valer uma frase de nuance no fechamento, se o autor achar que cabe.

## Citações legais/acadêmicas — checagem rápida (não forense)

| Citação | Status |
|---|---|
| Lei nº 10.931/2004 (cria LCI) | Confirmada — art. 12 e seguintes tratam de emissores e lastro |
| Lei nº 11.033/2004, art. 3º (isenção IR) | Não verificado o texto exato do artigo nesta pesquisa, mas múltiplas fontes de mercado confirmam essa lei/artigo como base da isenção — consistente |
| Lei nº 13.097/2015 (LIG) | Confirmada — patrimônio de afetação e duplo recurso batem com o texto |
| Lei nº 9.514/1997 (CRI) | Confirmada — companhias securitizadoras, cessão, regime fiduciário |
| Resoluções CMN nº 5.118/5.119 (2024) | Confirmadas — fev/2024, restrições de lastro para CRI/CRA/LCI/LCA/LIG, aumento de carência LCI de 3→12 meses |
| Resolução CMN nº 5.215/2025 | Confirmada — 22/05/2025, reduz carência de 9→6 meses (nota: o rascunho não menciona o intermediário "9 meses", só "6 meses"; tecnicamente o histórico completo é 3→12→6, o rascunho simplifica indo direto para "6 meses", o que não está errado mas omite o passo de 9 meses — irrelevante para a tese, mas a etapa 7 pode decidir se vale precisar) |
| Resoluções CMN nº 5.295/5.296 (2026) | Confirmadas no conteúdo técnico (Ativo de Referência, alocação em títulos públicos); **não confirmada** a atribuição da palavra "trampolim" como citação textual do BC (ver seção 3 acima — é caracterização de imprensa) |
| Ho & Saunders (1981), JFQA | Confirmada, sem anacronismo, leitura do "dealer avesso a risco" é a leitura padrão da literatura |
| Vedrossi (2002), dissertação USP | Localizada e confirmada — título, ano, instituição e orientação batem exatamente com a citação do rascunho |
| BCB, "Covered Bond: uma opção para o Brasil?" (Cadernos FGV) | Localizado artigo com esse título em periódico FGV (periodicos.fgv.br/cc) — não confirmada autoria específica do Banco Central nem o volume/ano exatos, recomendo a etapa 7 abrir o PDF diretamente para confirmar autoria institucional |

---

## Notas finais para quem for escrever o draft (etapa 4)

1. O achado mais importante desta pesquisa é a **correção de mecanismo** na seção 5 (o piso de 15% de IR é atingido aos 2 anos e não cai mais — "alíquota cai o suficiente em prazos muito longos" precisa ser reformulado).
2. O segundo achado mais importante é o **contraponto de política de crédito direcionado** (seção 6) — é real, aparece em material de mercado mainstream, e o texto pode ganhar uma frase reconhecendo essa camada sem enfraquecer a tese central sobre risco.
3. A citação "trampolim" atribuída ao Banco Central "por escrito" não tem fonte primária confirmada nesta pesquisa — recomendo à etapa 7 tratar como bandeira vermelha até achar a nota técnica/exposição de motivos original, ou reformular a atribuição no draft.
4. Os números de estoque de LCI têm uma pequena inconsistência interna (jan/2024 R$ 373 bi + abr/2024 R$ 362 bi vs. fim de 2024 R$ 350 bi) que vale reconciliar contra a fonte B3 original antes da publicação.
