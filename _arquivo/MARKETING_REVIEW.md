# Marketing Review — Syntaxis Educação

> Revisão estratégica produzida em 05/08/2026, com base nos arquivos do projeto e nas respostas do founder coletadas durante esta sessão.

---

## 1. Sumário Executivo

A Syntaxis Educação tem uma tese de posicionamento incomum e forte para o mercado brasileiro de infoprodutos financeiros: em vez de vender "liberdade financeira" ou "day trade", vende **skill técnica aplicada ao mercado de capitais, com mentalidade AI-First, ensinada por quem tem carreira acadêmica E profissional simultaneamente**. A segmentação de público (`AUDIENCES.md`, `FEAR.md`, `GREED.md`) é, de longe, o ativo mais maduro do projeto — nível de profundidade raro em projetos neste estágio, com dados datados, fontes rastreáveis e regras claras de uso por segmento.

O que está em risco não é a tese, é a **execução no tempo disponível**. Hoje é 05/08/2026. O `MARKETING.md` prevê o curso gratuito (FVDT) rodando de agosto a outubro de 2026, com lives semanais aos domingos — ou seja, a primeira live precisaria acontecer em **10 dias ou menos**. Você confirmou que apenas a estrutura/roteiro do MOD01 existe; nada foi gravado, e você está operando sozinho, com orçamento modesto de mídia. Isso é o núcleo do problema estratégico deste review: **o calendário implícito nos documentos não é factível como está escrito.**

Este documento não tenta "salvar" a data de agosto a qualquer custo. Ele propõe um recalibre honesto do cronograma, mantém a arquitetura de oferta e a segmentação (que estão corretas), e sinaliza com precisão onde a marca ainda não tem um Sistema de Design/Voz formalizado — apenas um manual pedagógico, que não é a mesma coisa.

**Atualização de 05/08/2026 (mesma sessão, segunda rodada):** três decisões do founder e uma pesquisa de mercado aprofundada foram incorporadas a este documento. (1) A promessa de resultado da página de vendas foi definida e cristalizada (§4). (2) A lacuna de tripwire apontada na Seção 5 foi resolvida: o funil passa a ter uma **isca paga de R$9,90** como porta de entrada (§5), substituindo a isca 100% gratuita como primeiro ponto de contato monetizável. (3) O curso gratuito de TVM foi especificado — **4 módulos, 8 semanas, 1 encontro ao vivo de até 1h30/semana** — o que permitiu recalcular o calendário com datas exatas (§8). Além disso, a Seção 3 foi expandida com pesquisa de mercado brasileiro 2026 e 8 personas detalhadas (2 por segmento).

---

## 2. Contexto e Fontes Consultadas

Todos os arquivos da pasta raiz e subpastas relevantes foram lidos antes de qualquer conclusão. Nenhum arquivo de identidade visual, tokens de design ou guia de voz de marca foi encontrado no projeto — isso é registrado como lacuna na Seção 12.

| Arquivo                                   | Papel                                                                                                                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `PROJECT_DESCRIPTION.md`                  | Documento fundacional: proposta de valor, metodologia pedagógica (5 pilares), benchmarks de mercado, bibliografia de design instrucional. Não é um documento de marketing, mas define o "produto" que o marketing precisa vender.                                                                 |
| `MARKETING.md`                            | Rascunho principal de estratégia. Define a esteira Free → Paid → Mentorship, o pacote de ofertas, e uma lista nua de 6 épicos (EPIC 0–5) sem datas, owners ou critérios de conclusão.                                                                                                             |
| `AUDIENCES.md`                            | **SSOT de segmentação de copy.** Define 4 segmentos (`#Millennials-FEAR`, `#Millennials-GREED`, `#GENZ-FEAR`, `#GENZ-GREED`) com perfil, medo/desejo central, âncora de dado, objeção-mestra e anti-padrões. Documento de referência obrigatória para qualquer peça de copy.                      |
| `FEAR.md`                                 | Banco de dados de medos por geração, com ~30 datapoints com fonte (Deloitte, KPMG, WEF, Gallup, GPTW, etc.), organizados por segmento e com ângulos de copy derivados.                                                                                                                            |
| `GREED.md`                                | Banco de dados de ambições/oportunidades por geração, mesma estrutura de `FEAR.md`. Contém o dado mais citável do projeto (CFA Institute: 37% da Gen Z aponta mercado financeiro como carreira mais promissora).                                                                                  |
| `METHODOLOGY.md`                          | Diretrizes de design instrucional para agentes de IA — governa como aulas e cases são criados (Andragogia, Backward Design, Alinhamento Construtivo, Carga Cognitiva, AI-First). É uma **fonte de verdade pedagógica**, não uma fonte de verdade de marca/visual — tratado como tal neste review. |
| `FoundationsTVM/PROJECT_DESCRIPTION.md`   | Descrição do curso-isca (FVDT): objetivos de aprendizado (O1–O5), critérios de avaliação (LA01–LA05), estrutura modular.                                                                                                                                                                          |
| `FoundationsTVM/REFS/MOD01/MOD01.md`      | Conteúdo já roteirizado do primeiro módulo do curso gratuito — inclui um case completo (CDB vs. LCI) já em formato praticamente publicável. Este é hoje o material mais avançado de todo o projeto.                                                                                               |
| `FoundationsTVM/REFS/*.md` e `*.pdf`      | Referências bibliográficas de conteúdo técnico (TVM, cálculo financeiro, modelagem). Fontes de conteúdo, não de marketing.                                                                                                                                                                        |
| `IntroMathFinance/PROJECT_DESCRIPTION.md` | Placeholder de 3 linhas para a trilha "Fundamentos Matemáticos para Finanças". Praticamente não desenvolvido.                                                                                                                                                                                     |
| `APPS/`                                   | Pasta vazia.                                                                                                                                                                                                                                                                                      |

**Lacuna confirmada:** não existe nenhum documento de identidade visual (paleta, tipografia, logo, tokens) nem guia de voz/tom de marca separado da segmentação de copy. `AUDIENCES.md` cobre _estrutura de argumento_ por segmento, mas não cobre _voz de marca_ (formal/informal, uso de gírias, emojis, tratamento — "você" vs "tu", etc.). Ver Seção 12.

---

## 3. Público-Alvo e Personas

O projeto já definiu isso com mais rigor do que a média de lançamentos deste porte. Resumindo com minhas palavras a partir de `AUDIENCES.md` + `FEAR.md` + `GREED.md`:

- **`#GENZ-FEAR`** (18–28, estagiário/trainee/analista júnior): teme não conseguir nem entrar no mercado — automação de vagas de entrada, exigência de credencial, ambiguidade de critérios. Fala a língua de _estabilidade_.
- **`#GENZ-GREED`** (mesmo perfil, viés de aceleração): já escolheu o setor (37% CFA Institute) e quer prova rápida e verificável de competência, não promessa. Fala a língua de _prova_.
- **`#Millennials-FEAR`** (30–36, analista pleno/sênior ou middle manager): teme ficar preso na média depois de uma década investida — não é medo de idade, é medo de ser genérico e substituível.
- **`#Millennials-GREED`** (mesmo perfil, viés de colheita): quer recuperar terreno e entrar no topo da distribuição que colheu o retorno da especialização técnica.

**Avaliação:** a matriz 2×2 (geração × eixo emocional) é sofisticada o suficiente para uma operação founder-solo — na verdade, é sofisticada _demais_ em relação à capacidade de execução atual, ponto que retomo na Seção 11 (Riscos). Manter os 4 segmentos é correto para a _estratégia de mensagem_; para a _operação real de copy_ nos primeiros 90 dias, recomendo priorizar 2 dos 4 segmentos (ver Seção 6) para não diluir esforço de um time de uma pessoa só.

**Lacuna identificada na primeira versão:** não havia persona nomeada e narrativa. Resolvida abaixo com pesquisa de mercado e 8 personas (2 por segmento).

### 3.1 Nota de metodologia e transparência

Os 8 links de LinkedIn fornecidos pelo founder foram usados como direção de pesquisa (tentativa de leitura de perfis públicos via `WebFetch`). O LinkedIn bloqueou o acesso automatizado (HTTP 999 — bloqueio padrão de scraping da plataforma, mesmo para perfis públicos, sem login). **Portanto, nenhuma persona abaixo é uma cópia ou paráfrase de uma pessoa real identificável** — não tenho dados verificáveis sobre esses 8 indivíduos e não é apropriado atribuir biografia, medos ou renda a pessoas reais nomeadas sem confirmação. Em vez disso, os 8 links foram tratados como **sinal do tipo de arquétipo de carreira que o founder já tem no radar** (estagiários/trainees/analistas juniores de instituições financeiras brasileiras, e profissionais de carreira mais avançada), e as personas foram construídas como **composições fictícias**, ancoradas em:

- Dados já existentes em `FEAR.md` e `GREED.md` (fontes: Deloitte Global 2026, KPMG US, WEF, CFA Institute, PwC, Anbima/Datafolha, entre outras);
- Pesquisa de mercado adicional realizada nesta sessão (ver §3.2), com fontes brasileiras de 2026 sobre salários, programas de trainee e comportamento de consumo de conteúdo.

Se o founder já tiver informações reais e autorizadas sobre esses 8 perfis (ex: são leads, ex-colegas ou alunos-piloto), a forma mais segura de incorporá-las é o founder colar aqui os dados relevantes (cargo, empresa, formação, dores relatadas) — aí sim posso refinar as personas com informação real e consentida, em vez de inferida de perfil bloqueado.

### 3.2 Pesquisa de mercado — Brasil, 2026

**Remuneração e programas de entrada:**

- Trainees de grandes bancos/instituições (BTG, Itaú, Santander, UBS) pagam entre **R$8.700 e R$11.500/mês**; Santander 2025 abriu em R$9.200 [Seja Trainee](https://sejatrainee.com.br/trainee-financeiro-tendencias-de-programas/), [Trainee UBS Brasil 2026](https://otrainee.com.br/2025/10/22/jornada-trainee-ubs-brasil-2026/).
- A XP Inc. recebe nova turma de estagiários em **agosto de 2026** [Programa de Estágio XP](https://lp.xpi.com.br/programa_de_estagio).
- Perfil buscado pelos programas: formação recente em Administração/Economia/Engenharia, inglês avançado, "perfil analítico, visão estratégica" e — cada vez mais — familiaridade com aplicações práticas de IA em produtos financeiros [Na Prática](https://napratica.org.br/noticias/confira-estas-dicas-para-quem-quer-ser-trainee-em-banco-em-2026), [Itaú Trainee 2026](https://www.itau.com.br/media/dam/m/11ffae96c57ff1e4/original/inscricoes-abertas-para-programa-trainee-itau-unibanco-2026.pdf).
- Fora dos programas de trainee, salário médio de analista **júnior R$3.000–5.000**, **pleno ~R$6.060**, **sênior ~R$7.843** [Glassdoor/Salario.com.br 2026](https://www.glassdoor.com.br/Sal%C3%A1rios/analista-de-mercado-de-capitais-sal%C3%A1rio-SRCH_KO0,31.htm).

**Gen Z brasileira e mercado de trabalho:**

- 59% da Gen Z (18–28) vê o mercado como fechado/desafiador; obstáculos citados: baixos salários (48%), exigência de experiência prévia (39%), alta concorrência (35%), falta de networking (32%) [FIESC](https://fiesc.com.br/pt-br/imprensa/maioria-dos-jovens-ve-mercado-de-trabalho-como-fechado-e-desafiador-aponta-estudo).
- 66% temem não conseguir um trabalho com segurança financeira; 62% consideram estabilidade financeira essencial para a felicidade [Reporter Naressi](https://www.reporternaressi.com.br/noticias/receio-com-futuro-leva-geracao-z-a-buscar-estabilidade-na-carreira.html).
- ~90% relatam algum grau de ansiedade sobre o futuro profissional; 18% se dizem sobrecarregados demais para sequer enviar currículo [Isso é Brasília, ago. 2026](https://www.issoebrasilia.com.br/2026/08/9-em-cada-10-jovens-tem-ansiedade-sobre.html). Este dado reforça — com uma fonte 2026 adicional e nacional — a tese de "ambiguidade como gatilho de ansiedade" já registrada em `FEAR.md` §1.4.

**Millennials brasileiros e estagnação:**

- Quase 1 em cada 4 profissionais no meio de carreira enfrenta estagnação (sem promoção/aumento por 5+ anos) — pesquisa NYU/Burning Glass Institute, citada pela Forbes Brasil em **agosto de 2026** [Forbes Brasil](https://forbes.com.br/carreira/2026/08/por-que-1-em-cada-4-profissionais-enfrenta-a-estagnacao-no-meio-da-carreira/). Esta é uma segunda fonte, independente das já citadas em `FEAR.md` §2.3, e reforça o eixo de estagnação como argumento central para `#Millennials-FEAR`.
- Millennials brasileiros tendem a redefinir sucesso: aprendizado contínuo, propósito e qualidade de vida pesam mais que ascensão hierárquica pura — coerente com o achado de `GREED.md` §3.3 sobre "sustentabilidade de carreira" substituindo "aceleração de carreira".

**IA no trabalho financeiro (contexto de produto, não só de copy):**

- Copilot/ChatGPT já são usados por analistas para reduzir tempo em tarefas repetitivas (leitura de planilhas, geração de relatórios); 74% dos CFOs pretendem ampliar uso de IA em atividades financeiras [Deloitte, via Contabeis.com.br](https://www.contabeis.com.br/noticias/78511/ia-no-setor-financeiro-avancos-e-impactos-reestruturam-o-brasil/). Isso valida que a camada AI-First do produto (`METHODOLOGY.md` §2) não é modismo de copy — é o que o mercado de trabalho já está cobrando na prática.

**Consumo de conteúdo (relevante para §7 Canais):**

- Gen Z busca conselhos de carreira majoritariamente em **YouTube (80%)** e **Instagram (73%)**; LinkedIn aparece em apenas 26% [Fast Company Brasil](https://fastcompanybrasil.com/futuro-do-trabalho/geracao-z-instagram-procurar-emprego/). Vídeo curto já é mais de 50% do tempo de consumo de conteúdo informativo dessa geração.
- **Implicação direta para o funil:** a estratégia de YouTube ao vivo + recortes curtos (Reels/Shorts) definida em `MARKETING.md` está alinhada com o comportamento real do público prioritário (`#GENZ-*`). LinkedIn, apesar de ser a rede "óbvia" para o tema, é canal secundário para captação de Gen Z — mantê-lo como canal de credibilidade/parcerias B2B (co-produção, Seção 7), não como canal primário de tráfego.

### 3.3 Personas detalhadas (2 por segmento)

Cada persona conecta perfil demográfico, dado-âncora (`FEAR.md`/`GREED.md`), objeção-mestra (`AUDIENCES.md`) e implicação prática de copy/produto. Nomes são fictícios (ver nota de metodologia em §3.1).

---

#### `#GENZ-FEAR` — Medo de exclusão, palavra-chave: estabilidade

**Persona 1 — Bianca Ferreira, 21 anos**
Estagiária de Middle Office em uma corretora de médio porte em São Paulo, cursando Administração na Mackenzie, 4º semestre. Trabalha 6h/dia + faculdade à noite. Ainda não tem certeza se vai ser efetivada — o estágio dura mais 8 meses e ela já viu duas colegas de turma não serem renovadas. Estuda para o CPA-20 nas horas vagas, mas sente que "saber a teoria" e "saber fazer o que o analista pede" são coisas diferentes, e ninguém no escritório tem tempo de ensinar com calma. Assiste conteúdo de carreira no YouTube e Instagram, quase nunca no LinkedIn. **Medo central:** não conseguir provar valor suficiente para ser efetivada — ligado ao dado de `FEAR.md` §1.1 (33% dos cargos de entrada esperados como automatizados/ampliados por IA, KPMG 2026). **Objeção-mestra:** "não tenho experiência para aproveitar isso ainda" — ela não sabe se um curso vai ajudar ou se só vai empilhar mais teoria que ela já tem. **Gatilho de compra:** ver um case prático idêntico ao que ela faz no dia a dia (ex: comparação CDB vs. LCI, já roteirizado em `MOD01.md`) resolvido com clareza — prova que o curso ensina o "como fazer", não só o "o que é".

**Persona 2 — Rafael Andrade, 24 anos**
Analista júnior de crédito, efetivado há 6 meses em um banco médio em Belo Horizonte, formado em Ciências Contábeis pela UFMG. Ganha na faixa de R$3.000–4.500 (compatível com `GREED.md` faixa júnior). Assim que foi efetivado, a real ansiedade começou: agora ele é cobrado por prazo e qualidade de análise, e sente que aprendeu "o básico do básico" na faculdade. Ouviu no corredor que o banco está testando uma ferramenta de IA para pré-triagem de propostas de crédito e tem medo real de que sua função de analista júnior — a mais mecânica — seja a primeira a encolher. **Medo central:** ficar defasado tecnicamente antes mesmo de completar um ano de casa — liga direto ao dado do WEF (`FEAR.md` §1.1, 41% das empresas planejam reduzir headcount por IA até 2030). **Objeção-mestra:** mesma do segmento, mas com uma variação: "será que vale gastar tempo estudando fora do trabalho, se o trabalho já toma 10h do meu dia?". **Gatilho de compra:** entender que o curso ensina a **usar** a IA que ameaça seu cargo, não só a temê-la — reposicionamento de ameaça para ferramenta, coerente com a camada AI-First do produto.

---

#### `#GENZ-GREED` — Prova rápida e mensurável, palavra-chave: prova

**Persona 1 — Yasmin Rocha, 22 anos**
Trainee em programa de banco grande em São Paulo (perfil Itaú/Santander), formada em Economia pela FGV, ganhando na faixa de R$9.000–9.500/mês (`GREED.md`/pesquisa de mercado §3.2). Entrou no trainee competindo com mais de 3.000 candidatos e sabe que a real disputa começa agora: em 18 meses ela vai escolher (ou ser escolhida para) uma trilha fixa dentro do banco. Ela não tem medo de não conseguir emprego — já conseguiu o mais difícil. O que ela quer é **provar, com evidência quantificável, que domina competência técnica de verdade** antes da escolha de trilha, para não ser alocada em uma área menos estratégica por falta de repertório demonstrado. Verifica todo dado antes de acreditar; segue 4-5 creators de finanças no Instagram e YouTube, desconfia de "guru de resultado". **Desejo central:** entrar com vantagem mensurável na trilha que escolher — ecoa o dado CFA Institute em `GREED.md` §1 (37% da Gen Z vê o setor financeiro como carreira mais promissora). **Objeção-mestra:** "consigo aprender isso de graça no YouTube" — ela já tenta, mas sente o conteúdo fragmentado demais para uma decisão de carreira desse tamanho. **Gatilho de compra:** um curso que entrega certificado/portfólio de case resolvido que ela possa literalmente mostrar na conversa de alocação de trilha.

**Persona 2 — Pedro Kalil, 26 anos**
Analista de renda fixa em uma corretora digital, trabalho remoto a partir de Porto Alegre, formado em Engenharia de Produção com pós-graduação lato sensu em finanças. Ganha na faixa de R$6.000–7.000 (pleno). Já passou pela fase de "conseguir a vaga" e agora está mirando virar especialista reconhecido em crédito estruturado dentro de 2-3 anos — sem depender de virar gestor de equipe, papel que não o atrai. Já tem side hustle de conteúdo (pequeno canal no YouTube sobre CDBs e debêntures) e usa isso como prova social ativa da própria competência. **Desejo central:** acelerar a curva de reconhecimento técnico com credencial + prática aplicada de IA (ligado a `GREED.md` §2.1: prêmio salarial por skills de IA saltou de 25% para 56% entre 2024-2025, PwC). **Objeção-mestra:** quer saber exatamente o ROI em tempo — "quantas horas isso vai tomar e o que eu ganho concretamente no fim". **Gatilho de compra:** ver a AI Skill entregável do módulo como algo que ele pode incorporar no próprio conteúdo/trabalho imediatamente, não como material passivo de estudo.

---

#### `#Millennials-FEAR` — Medo de estagnação, palavra-chave: genérico

**Persona 1 — Camila Duarte, 33 anos**
Analista sênior de tesouraria em um banco tradicional em São Paulo, 10 anos de carreira, formada em Administração pela PUC-SP, ganhando na faixa de R$7.500–8.500. Nunca foi promovida a coordenadora — dizem que "falta um diferencial técnico mais forte", mas ninguém detalha qual. Vê analistas mais novos, com menos tempo de casa, sendo promovidos por dominarem ferramentas que ela nunca teve tempo de aprender formalmente (Python, modelagem mais sofisticada). Tem duas filhas pequenas, tempo é o recurso mais escasso da vida dela — não tem 6 meses livres para um MBA. **Medo central:** ser vista como "genérica", substituível por qualquer analista sênior com o mesmo tempo de casa — dado-âncora `FEAR.md` §2.1 (top 10% dos Millennials tem 20% mais patrimônio que Boomers na mesma idade; a média, 30% menos). **Objeção-mestra:** "já é tarde para me especializar" — ela genuinamente acredita que passou da idade de "começar do zero" em algo técnico. **Gatilho de compra:** um formato que respeite o tempo dela — curso gravado + case aplicável, não mais um compromisso de agenda fixa longa — e uma prova de que 8-12 semanas mudam uma conversa de promoção, não uma reformulação de carreira inteira.

**Persona 2 — Marcelo Tavares, 36 anos**
Coordenador (middle manager) de crédito corporativo em um banco médio no Rio de Janeiro, MBA concluído há 4 anos, ganhando na faixa de R$11.000–13.000. Tecnicamente "chegou lá" — tem cargo de liderança — mas sente exatamente a armadilha descrita em `FEAR.md` §2.3: mais responsabilidade, quase nenhum poder real de decisão, e a régua de cobrança da diretoria não parou de subir. Lidera 5 analistas mais jovens que, segundo ele, "sabem mais IA aplicada do que eu". Tem vergonha de admitir isso publicamente. **Medo central:** perder autoridade técnica diante do próprio time, sendo o gestor que não acompanha a régua nova de competência — conecta com a pesquisa Forbes Brasil ago/2026 sobre estagnação de meio de carreira (§3.2). **Objeção-mestra:** mesma do segmento ("já é tarde"), mas com camada extra de orgulho — ele não quer aparecer como aluno iniciante ao lado dos próprios subordinados. **Gatilho de compra:** formato discreto (auto-ritmo, sem exposição em turma ao vivo obrigatória) e linguagem que trate como reforço de autoridade, não como remediação — exatamente o anti-padrão que `AUDIENCES.md` §5 já mapeia ("não infantilizar").

---

#### `#Millennials-GREED` — Colher o retorno da especialização, palavra-chave: colheita

**Persona 1 — Juliana Prado, 32 anos**
Analista pleno de modelagem financeira em uma gestora de recursos em São Paulo, formada em Ciências Econômicas pela USP, ganhando na faixa de R$8.000–9.000. Diferente de Camila (persona Millennials-FEAR), Juliana não teme ficar para trás — ela já decidiu ativamente que não quer virar gestora e está apostando em virar **referência técnica** reconhecida em precificação de ativos de crédito. Já domina Excel avançado e Python básico, quer aprofundar aplicação de IA em modelagem para acelerar o reconhecimento dentro e fora da empresa (LinkedIn é canal ativo para ela, diferente da Gen Z). **Desejo central:** autoridade técnica como caminho de renda e reconhecimento sem depender da escada hierárquica — dado-âncora `GREED.md` §3.1 (top 10% dos Millennials tem 20% mais patrimônio que Boomers) e §3.3 ("autoridade sem escada" como ângulo pouco explorado). **Objeção-mestra:** "vale o investimento de tempo neste momento da carreira?" — ela já é competente, precisa se convencer de que o curso adiciona algo que ela não replicaria sozinha em fóruns/documentação. **Gatilho de compra:** ver o mecanismo único do produto (professor híbrido acadêmico+mercado, case brasileiro real com tensão institucional) como algo que ela não encontra em conteúdo gratuito fragmentado.

**Persona 2 — Diego Salomão, 35 anos**
Contador em transição de carreira para a área de investimentos, atualmente analista de controladoria em uma empresa industrial em Curitiba, ganhando na faixa de R$7.000–8.000. Fez a certificação CPA-20 por conta própria há 1 ano e já assessora informalmente amigos e família com investimentos em renda fixa — quer profissionalizar isso e migrar para dentro do setor financeiro formalmente, capturando o "prêmio de especialização" que ele vê outros colegas de universidade (que foram para bancos) já colhendo. **Desejo central:** recuperar terreno perdido por ter escolhido uma trilha de carreira (contabilidade corporativa) que estagnou, migrando lateralmente para onde o retorno de especialização é maior — dado-âncora `GREED.md` §3.1 (a "grande transferência de riqueza" e o prêmio de trajetórias de alto status). **Objeção-mestra:** mistura as duas do segmento — teme que "já é tarde" para migrar de área aos 35, mas também quer confirmação de que **vale o investimento** antes de dar o salto. **Gatilho de compra:** prova de que o conteúdo é aplicável imediatamente em algo tangível (ex: a ferramenta de comparação de financiamento do Objetivo O5 do FVDT) que ele possa usar como portfólio para migração de carreira, não apenas como certificado.

---

#### 3.4 Como usar estas personas na operação

- **Prioridade de produção de conteúdo no lançamento gratuito (0–90 dias):** Bianca e Rafael (`#GENZ-FEAR`) e Yasmin e Pedro (`#GENZ-GREED`) são o público do curso gratuito de TVM — coerente com a recomendação de priorização por segmento já feita em §6.
- **Prioridade na abertura de carrinho das trilhas pagas:** Camila, Marcelo, Juliana e Diego (`#Millennials-*`) respondem melhor a oferta paga estruturada (formato auto-ritmo, prova de aplicação imediata) do que ao formato de live semanal ao vivo — usar essas 4 personas para briefar a copy da página de vendas de Renda Fixa e Fundamentos Matemáticos.
- **Mentoria (backend):** Marcelo (quer reforço de autoridade discreto) e Juliana (quer virar referência técnica) são as personas mais próximas do perfil ideal para as 10 vagas de mentoria — usar isso para desenhar os critérios de aplicação mencionados no EPIC 5 (§9).

---

## 4. Proposta de Valor e Posicionamento

**Proposta de valor central (nas minhas palavras):** _"Desenvolva as skills técnicas que o mercado de capitais brasileiro realmente usa — modelagem, dados, renda fixa — ensinadas por quem soma carreira acadêmica sólida e experiência de mercado real, com mentalidade AI-First desde a primeira aula."_

**Mecanismo único (o que diferencia de concorrentes como Wall Street Mojo, Coursera, Analyst Prep, citados em `PROJECT_DESCRIPTION.md`):**

1. **Professor híbrido** (acadêmico + profissional de mercado) — não é nem curso 100% teórico de universidade, nem "guru de resultado" sem lastro acadêmico.
2. **Case brasileiro real**, não genérico traduzido — `METHODOLOGY.md` exige tensão institucional brasileira (CVM, CMN) em todo case, o que nenhum dos 3 benchmarks citados replica para o público local.
3. **AI-First como competência entregável**, não markerting de IA — cada módulo entrega Skills e arquivos de contexto reutilizáveis no trabalho, o que responde diretamente à objeção-mestra de `#Millennials-GREED` ("vale o investimento de tempo?") e ao gap identificado em `GREED.md` §2.4 (74% da Gen Z relata falta de acesso a mentoria/prática real).

**Avaliação:** a proposta de valor é forte e defensável, mas **não está escrita em lugar nenhum como frase única e testável**. Ela está implícita, espalhada entre `PROJECT_DESCRIPTION.md` e `METHODOLOGY.md`. Recomendo cristalizar uma versão de 1 frase + 3 provas, para ser usada em toda página de vendas/anúncio — sem isso, cada peça de copy vai reinventar o posicionamento.

**Promessa de resultado (definida pelo founder nesta revisão):** o resultado esperado é que analistas e estagiários **aprendam as skills e ferramentas usadas em situações reais de trabalho — incluindo aprender a usar e trabalhar com IA — de forma a alcançarem o próximo nível em suas carreiras.**

Esta é a promessa-guia e deve substituir qualquer formulação genérica ("aprenda finanças", "domine investimentos") em toda página de vendas e roteiro de aula daqui em diante. Traduzida em uma frase de copy testável (sugestão, a validar com o founder):

> _"[Nome do curso] entrega as skills técnicas e o fluxo de trabalho com IA que hoje separam quem estagia de quem é efetivado — e quem é efetivado de quem vira referência."_

Esta frase amarra diretamente com os 4 segmentos e as 8 personas detalhadas em §3.3: para `#GENZ-FEAR` (Bianca, Rafael) o gancho é "efetivação"; para `#GENZ-GREED` (Yasmin, Pedro) é "provar competência rápido"; para `#Millennials-FEAR` (Camila, Marcelo) é "deixar de ser genérico"; para `#Millennials-GREED` (Juliana, Diego) é "virar referência". A promessa é quantificável no sentido de ser **verificável pelo aluno na prática do próprio trabalho** (ele sabe se passou a usar a skill ou não), sem prometer número de salário/promoção que a Syntaxis não controla — o que mantém a promessa ética e alinhada ao anti-padrão de `AUDIENCES.md` §5 contra dados não verificáveis.

---

## 5. Arquitetura da Oferta (funil completo)

Baseado em `MARKETING.md`, reconstruído e com uma correção estrutural:

```
ISCA PAGA — R$9,90 (self-liquidating offer)
└─ Formato exato ainda em aberto (ver §13) — sugestão: extrair um recorte
   já pronto do MOD01.md (ex: o case CDB vs. LCI) em formato de guia/AI
   Skill de baixo ticket.
   Objetivo: filtrar tráfego frio por intenção real de compra, cobrir
   parte do custo de mídia, e entregar uma "primeira vitória" rápida
   antes do compromisso de tempo do curso ao vivo.

CURSO GRATUITO AO VIVO — Fundamentos do Valor do Dinheiro no Tempo (FVDT)
└─ 4 módulos, 8 semanas, 1 encontro ao vivo de até 1h30/semana
   (domingos, YouTube) + Slack para cases
   Objetivo: construir audiência, comunidade e prova social; nutrir
   quem comprou a isca paga e captar quem chegou por outros canais,
   alimentando a lista via Substack.

CORE OFFER
└─ Pacote "Profissional de Renda Fixa":
   ├─ Renda Fixa — Títulos Públicos e Privados (gravado/Hotmart)
   │  Notas de aula, Guia de Case, AI Skills, Flashcards, AI guided cases
   └─ Fundamentos Matemáticos para Finanças (gravado/Hotmart)
      Notas de aula, Guia de Case, AI Skills, Flashcards, AI guided cases
   Faixa sugerida pelo founder: trilha individual R$700–1.200 /
   pacote completo R$1.500–2.500

UPSELL / BACKEND
└─ Pacote Mentorship = pacote completo + mentoria individual
   6 encontros de 1h, cap de 10 alunos, R$5.000–8.000
```

**Avaliação da arquitetura:**

- A lógica **isca → core → upsell** está correta e é bem escolhida — usar o gratuito para provar qualidade antes de vender é coerente com o público cético definido em `AUDIENCES.md` (`#GENZ-GREED` "não quer promessa, quer evidência").
- **Tripwire resolvido nesta revisão.** O founder decidiu adotar uma **isca paga de R$9,90** como porta de entrada do funil (diagrama acima), substituindo a isca 100% gratuita como primeiro ponto de contato monetizável — e resolvendo a lacuna identificada na primeira versão deste review. R$9,90 é mais agressivo que a faixa R$27–47 originalmente sugerida aqui, o que é coerente com a lógica de _self-liquidating offer_: o objetivo não é lucro na venda em si, é qualificar lead pagante (filtra quem só quer conteúdo grátis) e gerar caixa marginal para reinvestir em mídia. **Ponto de atenção:** a R$9,90, a comissão padrão da Hotmart (9,9% + R$1,00 por venda) consome quase 20% do valor — não modelar isso como fonte de receita, e sim como filtro + geração de caixa mínima. **Falta definir o formato exato do que é entregue nessa isca** e a relação entre ela e o curso gratuito (a isca dá acesso prioritário ao curso ao vivo, ou são ofertas paralelas independentes?) — ver pergunta em §13.
- **Cap de 10 alunos na mentoria é bem calibrado** para operação solo — não expandir sem contratar suporte.
- A oferta de **co-produção com influencers** (Eu Me Banco, T2 Educação, Top Invest) mencionada en passant em `MARKETING.md` linha 53 é citada mas não desenvolvida em nenhum épico. Dado que você é founder solo com orçamento modesto de ads, **esta é provavelmente a alavanca de aquisição de maior ROI disponível** e está subdimensionada em prioridade — ver Seção 9.

---

## 6. Estratégia de Lançamento (modelo escolhido e justificativa)

O modelo implícito em `MARKETING.md` é um **híbrido semente + evergreen embrionário**: lançamento "semente" via lives gratuitas ao vivo (construção de audiência e prova social simultânea à criação de conteúdo) alimentando uma lista, seguido de lançamento interno clássico (carrinho aberto) para as trilhas pagas.

**Isso é a escolha certa para founder solo em 2026**, pelos seguintes motivos:

- Lançamento "semente" não exige conteúdo 100% pronto antecipadamente — você grava enquanto ensina ao vivo, o que é compatível com o estado atual (só roteiro pronto).
- Constrói prova social organicamente (comentários, participação no Slack) antes de pedir dinheiro — importante para os 4 segmentos, que são unanimemente céticos a promessas não verificadas.
- Reduz custo de aquisição pago justamente quando o orçamento é modesto.

**Ajuste recomendado ao modelo:** não tente rodar os 4 segmentos de `AUDIENCES.md` com a mesma intensidade nas lives gratuitas. Para o pré-lançamento e lançamento do FVDT (curso de fundamentos, mais raso, público mais júnior), **priorize `#GENZ-FEAR` e `#GENZ-GREED`** como eixo principal de copy — é o público mais alcançável organicamente (YouTube, TikTok-adjacent, Slack de comunidade) e mais alinhado ao nível de entrada do curso gratuito. Reserve `#Millennials-*` para quando as trilhas pagas (Renda Fixa, Mat. Financeira) e a mentoria abrirem — é onde a promessa de "recuperar terreno"/"topo da distribuição" faz mais sentido de oferta.

---

## 7. Canais e Táticas de Aquisição

Com orçamento modesto (confirmado pelo founder) e operação solo, a ordem de prioridade recomendada é:

1. **YouTube ao vivo (domingos) + Slack da comunidade** — já definido em `MARKETING.md`, é o canal primário e correto: custo marginal zero, gera conteúdo reaproveitável (recortes, cases) e constrói prova social ao vivo. **Confirmado pela pesquisa desta sessão (§3.2):** Gen Z busca conselhos de carreira majoritariamente em YouTube (80%) e Instagram (73%); LinkedIn é canal secundário (26%) para esse público. Isso valida a priorização de YouTube/Instagram como canais primários de aquisição para `#GENZ-*` e reforça manter LinkedIn como canal de credibilidade/parcerias (item 3 abaixo), não de tráfego de topo de funil.
2. **Substack** — já mencionado como canal de lista. Usar para nutrição via e-mail entre lives (recência importa: lives semanais + newsletter intercalada evita perda de momentum de 7 dias).
3. **Co-produção/parcerias** (Eu Me Banco, T2 Educação, Top Invest) — subutilizado hoje. Para founder solo, uma parceria de audiência bem negociada vale mais que R$ de ads modestos. Recomendo transformar isso em um épico formal com prazo (ver Seção 9), não deixar como nota de rodapé.
4. **Orçamento modesto de ads** — direcionar **exclusivamente** para: (a) retargeting de quem assistiu lives/visitou a lista mas não se inscreveu, e (b) tráfego frio para o carrinho de abertura das trilhas pagas, nunca para topo de funil frio genérico. Com verba limitada, ads de topo de funil sem produto pago pronto queimam orçamento sem retorno mensurável.
5. **WhatsApp** — não mencionado em nenhum documento. Dado o público brasileiro e a preferência por avisos de abertura/fechamento de carrinho em tempo real, recomendo lista de transmissão de WhatsApp para os momentos críticos de escassez (abertura/fechamento) — e-mail sozinho tem taxa de abertura mais baixa que WhatsApp para esse tipo de gatilho.

**Uso responsável de IA no funil:** o projeto já tem isso bem resolvido no produto (AI Skills entregáveis), mas não há menção a uso de IA na _produção_ do funil (copy assistida, atendimento). Dado que você é founder solo, IA generativa para rascunho de copy (sempre validado contra `AUDIENCES.md`) e para triagem de dúvidas no Slack/WhatsApp é recomendável — mas deve ser **divulgado com transparência** quando usada em atendimento direto ao aluno, coerente com o próprio posicionamento AI-First da marca (usar IA às escondidas contradiz a proposta de valor).

---

## 8. Calendário e Marcos (pré-lançamento, lançamento, pós-lançamento)

**Alerta central deste review:** o calendário implícito em `MARKETING.md` (curso gratuito rodando ago–out/2026, lives aos domingos) não era factível a partir de 05/08/2026 com apenas o MOD01 roteirizado e nenhuma gravação feita, operando sozinho. Um lançamento semente com pré-lançamento adequado (aquecimento de audiência, criativos, testes técnicos de transmissão) precisa de **2–4 semanas mínimas** antes da primeira live para não nascer sem plateia.

**Atualização:** com a estrutura do curso gratuito agora definida (4 módulos, 8 semanas, 1 encontro de até 1h30/domingo) e a isca paga de R$9,90 confirmada, foi possível recalcular o calendário com datas exatas — e a boa notícia é que, mesmo com a estreia adiada para início de setembro (em vez de agosto), o curso gratuito ainda termina em outubro, dentro da janela originalmente prevista em `MARKETING.md`.

Calendário revisado, com datas exatas (2026):

| Marco                                                                                                        | Data/Janela                                                 | Racional                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fechamento do roteiro completo do FVDT (4 módulos)                                                           | 05/08 – 19/08/2026                                          | Sem isso, as lives ficam sem preparação de conteúdo dos módulos 2–4 enquanto o módulo 1 já está no ar — risco real de atropelo.                              |
| Estruturação da isca paga (R$9,90): página de vendas, checkout Hotmart, criativo, definição de formato (§13) | 12/08 – 23/08/2026                                          | Roda em paralelo ao fechamento do roteiro — é um produto pequeno, não deve competir por tempo com a produção do curso.                                       |
| Campanha de tráfego para a isca paga (orçamento modesto) + abertura de lista Substack/Slack                  | 24/08 – 05/09/2026                                          | Gera caixa marginal, testa criativos/mensagem antes da estreia ao vivo, e começa a aquecer audiência para a primeira live.                                   |
| **Primeira live (abertura oficial do curso gratuito — Módulo 1)**                                            | **06/09/2026 (domingo)**                                    | Prioriza qualidade de estreia sobre velocidade — uma estreia mal preparada é mais cara de recuperar do que 4 semanas de atraso frente ao plano original.     |
| Lives semanais FVDT (8 encontros, 4 módulos, ~2 encontros/módulo)                                            | 06/09, 13/09, 20/09, 27/09, 04/10, 11/10, 18/10, 25/10/2026 | Cadência semanal fixa aos domingos, encerrando em outubro — compatível com a janela "ago–out" original do `MARKETING.md`, apenas deslocada ~1 mês no início. |
| Pré-lançamento trilhas pagas (Renda Fixa + Mat. Financeira)                                                  | 11/10 – 25/10/2026 (últimas 2 semanas do curso gratuito)    | Clássico do lançamento interno: abrir carrinho para quem já está "aquecido" pelo gratuito, não depois que o engajamento esfriar.                             |
| Abertura de carrinho (trilhas pagas)                                                                         | 26/10 – 02/11/2026 (janela de 7 dias)                       | Escassez de prazo real (não artificial) — coerente com o público cético mapeado em `AUDIENCES.md` §5.                                                        |
| Pós-lançamento: entrega, onboarding, coleta de prova social (depoimentos)                                    | nov/2026                                                    | Prova social coletada aqui alimenta o próximo ciclo de lançamento (mentoria, turma 2).                                                                       |
| Pré-lançamento + lançamento Mentoria (10 vagas)                                                              | dez/2026 – jan/2027                                         | Mentoria como backend requer prova social do lançamento anterior — não faz sentido lançar simultaneamente ao core offer.                                     |

---

## 9. Épicos e Roadmap

Os 6 épicos listados em `MARKETING.md` (EPIC 0–5) estão **sequenciados corretamente em lógica de funil**, mas sem prazos, critérios de conclusão, ou dependências explícitas — e faltam épicos estruturais. Avaliação épico a épico:

| Épico original                     | Avaliação                                                                                                                                                                | Ação recomendada                                                                                                                                                                                                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| EPIC 0 — Pré-lançamento YouTube    | Subdimensionado em prioridade. Hoje é o épico mais crítico e urgente, mas está descrito em uma linha sem tarefas.                                                        | Quebrar em: (1) roteiro completo FVDT (4 módulos), (2) estruturação e campanha da isca paga R$9,90, (3) setup técnico de transmissão, (4) criativos de aquecimento, (5) criação Slack. Prazo: 05/08–05/09/2026 (ver tabela completa em §8).                     |
| EPIC 1 — Youtube Lives Free Launch | Sequenciamento correto (depende do EPIC 0). Data-alvo implícita (10/08) não é factível — ver §8.                                                                         | Recalibrar início para 06/09/2026, com os 8 encontros semanais (4 módulos) indo até 25/10/2026.                                                                                                                                                                 |
| EPIC 2 — Pré-lançamento Renda Fixa | Corretamente depois do EPIC 1, mas **arriscado**: `MARKETING.md` não deixa claro se a produção do curso gravado de Renda Fixa começa em paralelo ao EPIC 1 ou só depois. | **Reordenar:** iniciar produção de conteúdo de Renda Fixa em paralelo às lives gratuitas (a partir de meados de setembro), não depois que elas terminarem — senão o carrinho abre sem produto gravado pronto, repetindo o mesmo erro de calendário do EPIC 0/1. |
| EPIC 3 — Launch Renda Fixa         | Correto na posição, mas sem escassez definida (prazo de carrinho, bônus de ordem de chegada) — nenhum mecanismo de urgência descrito em nenhum documento.                | Definir mecanismo de escassez legítima antes deste épico (ver §10 Checklist).                                                                                                                                                                                   |
| EPIC 4 — Pré-lançamento Mentoria   | Está mal posicionado: mentoria é _backend_ de alto ticket, deveria vir depois de coletar prova social do EPIC 3, não em paralelo/logo em seguida.                        | Manter depois do EPIC 3 com espaçamento de 1–2 meses para coleta de depoimentos.                                                                                                                                                                                |
| EPIC 5 — Launch Mentoria           | Ok na posição, mas cap de 10 alunos não está ligado a nenhum épico de qualificação de lead (como saber quem entrevistar para as 10 vagas?).                              | Adicionar sub-tarefa de processo de aplicação/entrevista antes da abertura.                                                                                                                                                                                     |

**Épicos ausentes que precisam ser criados:**

- **EPIC -1 (novo, mais urgente que tudo): Fundamentos de Marca e Oferta.** Parcialmente resolvido nesta revisão — a promessa de resultado (§4) e o tripwire/isca paga (§5) já foram definidos pelo founder. **Ainda em aberto:** nome comercial do pacote (hoje só existe "Free, Paid and Mentorship" como rótulo interno), formato exato da isca de R$9,90, e validação final da faixa de preço informada (§13).
- **Épico de Parcerias/Co-produção.** Hoje é uma frase solta em `MARKETING.md` linha 53. Dado que é provavelmente a alavanca de aquisição mais barata disponível para founder solo, merece épico próprio com prazo — recomendo rodar em paralelo ao EPIC 0/1 (contato com Eu Me Banco, T2 Educação, Top Invest pode começar imediatamente, é apenas outreach).

**Épicos de baixo impacto consumindo desproporção:** nenhum foi identificado como superdimensionado — ao contrário, o problema atual é subdimensionamento generalizado (épicos descritos em títulos de uma linha). Não há risco de esforço desperdiçado em baixo impacto; há risco de nenhum épico ter escopo suficiente para ser executável.

---

## 10. Métricas de Sucesso e Pontos de Decisão

Nenhuma meta numérica está definida em nenhum documento. Proposta de métricas mínimas por fase, para servir de ponto de decisão go/no-go:

| Fase                    | Métrica                                                                                              | Ponto de decisão                                                                                                                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Isca paga (R$9,90)      | Custo por venda vs. R$9,90 recebido (líquido de ~20% de taxa Hotmart); taxa de conversão do criativo | Se CAC > receita líquida da isca, ela está funcionando só como filtro de qualificação, não como geração de caixa — ok, mas ajusta expectativa de orçamento. |
| Pré-lançamento          | Tamanho da lista (Substack + Slack) antes da 1ª live                                                 | Se lista < 100 inscritos na véspera da estreia, considerar adiar 1–2 semanas em vez de estrear com plateia pequena.                                         |
| Lançamento gratuito     | Taxa de presença ao vivo / audiência da lista; retenção entre lives (mesmos alunos voltando)         | Retenção < 30% entre a 1ª e a 3ª live é sinal de desalinhamento de conteúdo/promessa — pausar e ajustar antes de seguir para EPIC 2.                        |
| Pré-venda trilhas pagas | Taxa de conversão lista → interesse manifestado (lista de espera/pesquisa de intenção)               | Validar interesse _antes_ de abrir carrinho — barato de medir, evita produzir/vender no escuro.                                                             |
| Carrinho aberto         | Conversão lista aquecida → venda; ticket médio real vs. faixa projetada (R$700–2.500)                | Definir CAC máximo aceitável dado orçamento modesto — sem isso, não dá para saber se ads estão funcionando.                                                 |
| Mentoria                | Taxa de aplicação → aceite nas 10 vagas                                                              | Se demanda > 10, sinaliza espaço para 2ª turma ou aumento de preço na próxima cohort.                                                                       |

---

## 11. Riscos e Planos de Mitigação

| Risco                                                                                                                                     | Severidade                                        | Mitigação                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Calendário de agosto não é factível** (conteúdo só roteirizado, founder solo, hoje é 05/08)                                             | 🔴 Alto                                           | Recalibrar datas conforme §8. Comunicar qualquer atraso publicamente com transparência antes que vire ausência silenciosa — pior para a marca que um adiamento anunciado.                                                                                                                                                                                                  |
| **Sobrecarga de founder solo em 4 segmentos de copy simultâneos**                                                                         | 🟡 Médio                                          | Priorizar `#GENZ-*` no lançamento gratuito, reservar `#Millennials-*` para as trilhas pagas (§6).                                                                                                                                                                                                                                                                          |
| **Formato da isca paga (R$9,90) ainda não definido** — tripwire em si já foi resolvido pela decisão do founder, mas falta o "o quê" exato | 🟡 Médio                                          | Definir o formato (guia, AI Skill, e-book) a partir de conteúdo já roteirizado no MOD01 antes do EPIC 0 — ver §13.                                                                                                                                                                                                                                                         |
| **Nenhum mecanismo de escassez legítima definido**                                                                                        | 🟡 Médio                                          | Definir prazo real de carrinho + bônus por ordem de inscrição antes do EPIC 3. Evitar contagem regressiva falsa — o público (`AUDIENCES.md` §5) reconhece e pune esse padrão.                                                                                                                                                                                              |
| **Falta de identidade visual/voz de marca formalizada**                                                                                   | 🟡 Médio                                          | Ver checklist de marca em §12 — risco de inconsistência visual conforme mais peças de copy são produzidas por diferentes ferramentas de IA.                                                                                                                                                                                                                                |
| **Co-produção/parcerias subexploradas apesar de baixo custo e alto potencial**                                                            | 🟡 Médio                                          | Elevar a épico formal com prazo, iniciar outreach imediatamente (§9).                                                                                                                                                                                                                                                                                                      |
| **Nenhuma meta numérica de go/no-go definida**                                                                                            | 🟢 Baixo-Médio                                    | Adotar métricas mínimas propostas em §10 antes da 1ª live.                                                                                                                                                                                                                                                                                                                 |
| **Dependência de uma única pessoa para produção + ensino + atendimento + marketing**                                                      | 🔴 Alto (estrutural, não corrigível neste review) | Fora do escopo deste documento decidir contratação, mas sinalizo: o roadmap de 6+ épicos em paralelo a lives semanais ao vivo é um volume de trabalho que historicamente leva founders solo a burnout ou atraso em cascata. Vale reservar orçamento modesto também para terceirizar 1 tarefa mecânica (edição de vídeo, por exemplo) antes de terceirizar copy/estratégia. |

---

## 12. Checklist de Alinhamento de Marca

Avaliado contra boas práticas de lançamento 2026 e contra os documentos de marca disponíveis (`AUDIENCES.md`, `METHODOLOGY.md` — não há guia visual/tom separado).

**Boas práticas de lançamento 2026:**

- [x] Clareza de promessa — presente na proposta pedagógica (`PROJECT_DESCRIPTION.md`), mas **não cristalizada em frase única de copy** (§4). Ação: escrever a frase de posicionamento antes do EPIC 0.
- [x] Prova social planejada — implícita no modelo lives + Slack, mas **nenhum mecanismo formal de coleta de depoimento está desenhado**. Ação: adicionar etapa de coleta de depoimento ao final de cada módulo/case (ex: pedir print de "aha moment" no Slack).
- [ ] Mecanismo de escassez legítimo — **ausente**. Ação: definir antes do EPIC 3 (§9, §11).
- [ ] Jornada de e-mail/WhatsApp — Substack cobre e-mail; **WhatsApp não está no plano** apesar de ser canal de maior abertura no Brasil para avisos de carrinho. Ação: avaliar lista de transmissão de WhatsApp (§7).
- [x] Uso responsável de IA no funil — bem resolvido _no produto_ (AI Skills, AI-First); **não formalizado no atendimento/copy** (§7). Ação: política simples de transparência de uso de IA em atendimento direto.
- [ ] Mobile-first — nenhum documento menciona formato de consumo (mobile vs. desktop) para e-book, flashcards, ou site próprio mencionado em `MARKETING.md` linha 51. Dado que flashcards e AI guided cases são produtos de uso recorrente, **mobile-first é especialmente crítico** e não está garantido. Ação: confirmar com qualquer ferramenta/plataforma escolhida para hospedar flashcards que o consumo mobile é nativo, não responsivo genérico.

**Consistência de tom e vocabulário (contra `AUDIENCES.md`):**

- `METHODOLOGY.md` define tom pedagógico (andragógico, sem infantilização) que está **alinhado** com o anti-padrão de `AUDIENCES.md` §5 para `#Millennials-FEAR` ("não infantilizar nem tratar como iniciante"). Nenhum desalinhamento encontrado aqui.
- **Desalinhamento específico identificado:** `MARKETING.md` usa nomenclatura em inglês para os pacotes ("Free, Paid and Mentorship", "EPIC 0", "LAUNCH") mas todo o resto do projeto — incluindo `AUDIENCES.md`, que é o SSOT de copy — é em português com termos técnicos em português (ex: "estagiários", "mercado de capitais brasileiro"). Isso não é necessariamente um erro (nomenclatura interna de projeto pode ser em inglês), mas **precisa de uma decisão explícita**: os nomes comerciais das trilhas serão em português (coerente com o público e com `AUDIENCES.md`) ou haverá mistura de idiomas na página de vendas? Recomendo nomes comerciais 100% em português — o público-alvo (`#GENZ-FEAR` particularmente) reage mal a inglês desnecessário como sinal de distância/elitismo, o que contradiz o próprio anti-padrão de "não infantilizar" mas também não afastar.
- **Nenhum guia de voz de marca existe** (formal vs. informal, uso de "você" vs. "tu", uso de emoji, gírias de mercado financeiro vs. explicação simplificada). `AUDIENCES.md` define _estrutura de argumento_ por segmento mas não _tom_. Ação recomendada: criar um `VOICE.md` curto (não precisa ser extenso) definindo 3–5 regras de tom, para evitar que peças de copy geradas por IA em sessões diferentes soem como marcas diferentes.

---

## 13. Perguntas em Aberto para o Founder

**Resolvidas nesta rodada:** data de estreia (§8, recalculada), promessa de resultado (§4), tripwire/isca paga (§5). Seguem as perguntas ainda em aberto:

1. **Formato exato da isca paga (R$9,90):** será um guia em PDF, uma AI Skill entregável, um mini-case interativo, ou outra coisa? Sugestão desta revisão: extrair o case CDB vs. LCI já roteirizado em `MOD01.md`, mas a decisão final e o formato de entrega (arquivo, plataforma, automação de acesso) dependem do founder.
2. **Relação entre a isca paga e o curso gratuito:** quem compra a isca de R$9,90 ganha acesso prioritário/bônus ao curso gratuito ao vivo, ou são duas ofertas paralelas e independentes no funil? Isso muda a copy da página de vendas da isca e a lógica de nutrição pós-compra.
3. **Nome comercial dos pacotes:** os nomes de trilha/pacote serão definidos em português (recomendado, §12) ou há preferência por nomenclatura em inglês/mista?
4. **Plataforma de flashcards e conteúdo mobile:** `MARKETING.md` menciona "site próprio" para flashcards — já há uma ferramenta/stack escolhida, ou isso ainda está em aberto? Isso afeta diretamente o prazo do EPIC 2/3.
5. **Parcerias:** já existe algum contato prévio com Eu Me Banco, T2 Educação ou Top Invest, ou o outreach começaria do zero?
6. **Precificação final:** a faixa informada (trilha R$700–1.200 / pacote R$1.500–2.500 / mentoria R$5.000–8.000) é uma hipótese a validar com a lista antes da abertura de carrinho, ou já é a decisão final?
7. **Dados reais de persona:** os 8 perfis de LinkedIn enviados têm alguma relação direta com o projeto (leads, ex-colegas, alunos-piloto)? Se sim, e se o founder tiver autorização/contexto para compartilhar detalhes reais (cargo, empresa, dores relatadas em conversa), as 8 personas fictícias em §3.3 podem ser refinadas com dado real em vez de composição de mercado — ver nota de metodologia em §3.1.
