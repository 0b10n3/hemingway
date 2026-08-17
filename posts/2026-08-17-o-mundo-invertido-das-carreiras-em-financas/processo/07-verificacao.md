# 07 — Verificação técnica

Verificação sobre `processo/04-draft-v1.md`, cruzada com `processo/03-pesquisa.md` (fontes já
levantadas) e as duas pendências `[VERIFICAR]` deixadas por `processo/06-revisao.md`. Buscas
feitas via `WebSearch`/`WebFetch` em 2026-08-17 (data de acesso de todas as fontes abaixo).

## 1. Sigla GFMI

**Trecho do draft:** "o pré-requisito listado pela GFMI, provedora de treinamento profissional
de risco, para o curso dela sobre VaR."

**Veredito: ✅ Confirmado.** GFMI = **Global Financial Markets Institute** (razão social
completa: Global Financial Markets Institute, Inc.), firma de treinamento e consultoria
financeira certificada pela NASBA, fundada em 1998, gerida por profissionais de Wall Street.
Nome completo aparece no rodapé/copyright do site e na página institucional.

Fontes:
- [Home — Global Financial Markets Institute](https://www.gfmi.com/) (copyright "Global
  Financial Markets Institute"; acesso 2026-08-17)
- [About Us — Global Financial Markets Institute](https://www.gfmi.com/about-us/) (acesso
  2026-08-17)

**Correção a aplicar (resolve o `[VERIFICAR]` de `06-revisao.md`):** "GFMI (Global Financial
Markets Institute), provedora de treinamento profissional de risco, para o curso dela sobre
VaR."

### Fidelidade da citação da GFMI

Texto completo do pré-requisito na página do curso, confirmado via fetch direto em
2026-08-17: *"Participants should understand simple financial concepts such as present value
and the calculation of returns and have some familiarity with financial markets and
instruments. They should also be comfortable with the use of basic statistical concepts such
as probability distribution, mean and variance to describe possible gains or losses on
portfolios. No advanced knowledge of mathematics or statistics is required."*

O draft traduz/cita como: *"entender conceitos financeiros simples, como valor presente"* +
"não pede matemática avançada". Isso corresponde fielmente à primeira cláusula do original
("understand simple financial concepts such as present value") e à última frase ("No advanced
knowledge of mathematics or statistics is required"). O draft omite "and the calculation of
returns" e a parte sobre conforto com estatística básica (probabilidade, média, variância) —
mas nenhuma omissão distorce o sentido: a citação usada é um subconjunto fiel, não uma
paráfrase que inverte ou exagera o original.

**Veredito: ✅ Confirmado**, com nota: a citação é parcial (recorte fiel do primeiro trecho da
frase), não a íntegra do parágrafo de pré-requisitos. Não é erro, mas fica registrado.

Fonte: [Value at Risk Course — GFMI](https://www.gfmi.com/training_courses/value-at-risk-course/)
(conteúdo confirmado via fetch em 2026-08-17)

## 2. Expansão de CFA

**Trecho do draft:** "O currículo do CFA (a certificação mais reconhecida do mercado de
investimentos)."

**Veredito: ✅ Confirmado.** CFA = Chartered Financial Analyst. A caracterização "certificação
mais reconhecida do mercado de investimentos" é defensável — múltiplas fontes independentes
descrevem o CFA como "the most respected and recognized investment credential" / "gold
standard" da indústria de gestão de investimentos, reconhecido em mais de 165 países, com taxa
de aprovação inferior a 20% dos candidatos que começam o Nível I até obter o título completo.

Fontes:
- [CFA® Program — CFA Institute](https://www.cfainstitute.org/programs/cfa-program) (acesso
  2026-08-17)
- [What is a Chartered Financial Analyst (CFA)? — Wealthtender](https://wealthtender.com/professional-designations/what-is-a-chartered-financial-analyst-cfa/)
  (acesso 2026-08-17)
- [The CFA® Charter — Forté Foundation](https://www.fortefoundation.org/the-cfa-charter-chartered-financial-analyst-designation/)
  (acesso 2026-08-17)

**Correção a aplicar (resolve o `[VERIFICAR]` de `06-revisao.md`):** "CFA (Chartered Financial
Analyst, a certificação mais reconhecida do mercado de investimentos)."

## 3. Estrutura de capítulos de Hull, *Options, Futures, and Other Derivatives*

**Trecho do draft:** "Taxa de juros e formação de preço a termo vêm nos capítulos 4 a 6; a
mecânica de opções só chega lá pelo 11."

### Parte estável: capítulos 4-6

**Veredito: ✅ Confirmado**, e estável entre edições (verificado nas edições 8ª, 9ª, 10ª e 11ª):
- Capítulo 4 — "Interest Rates" em todas as edições checadas.
- Capítulo 5 — "Determination of Forward and Futures Prices" em todas as edições checadas.
- Capítulo 6 — "Interest Rate Futures" em todas as edições checadas.

A afirmação "taxa de juros e formação de preço a termo vêm nos capítulos 4 a 6" está correta e
não varia por edição nas edições verificadas.

### Parte imprecisa: "capítulo 11" para mecânica de opções

**Veredito: ⚠️ Impreciso.** Em nenhuma das edições checadas o capítulo 11 é o primeiro a tratar
de mecânica de opções — e a numeração muda por edição:

| Edição | "Mechanics of Options Markets" | "Properties of Stock Options" |
|---|---|---|
| 7ª | capítulo 8 | capítulo 9 |
| 8ª | capítulo 9 | capítulo 10 |
| 9ª–11ª | capítulo 10 | capítulo 11 |

Ou seja: nas edições mais recentes (9ª a 11ª, as mais prováveis de estarem em circulação hoje),
o capítulo que introduz a mecânica de opções ("Mechanics of Options Markets") é o **10**, não o
11 — o 11 é "Properties of Stock Options", um capítulo já avançado sobre propriedades/limites de
preço de opções, não a introdução à mecânica. Em edições mais antigas (7ª e 8ª), o deslocamento é
ainda maior.

Fontes:
- [Options, Futures, and Other Derivatives, 11th edition — Pearson](https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005938/9780136939917)
  (acesso 2026-08-17)
- Busca cruzada de sumários de edições 7ª-11ª via múltiplos catálogos acadêmicos e de resolução
  de exercícios (Stuvia, TestBankDeal, Amazon, catdir.loc.gov) (acesso 2026-08-17)
- PDF da 11ª edição citado em `03-pesquisa.md` (lib.ysu.am) não pôde ser reaberto nesta etapa —
  certificado expirado no momento do acesso; sumário confirmado por fontes alternativas listadas
  acima.

`[FAIXA: a mecânica de opções só chega lá pelo 11 → a mecânica de opções só chega bem mais
adiante — capítulo 10 nas edições mais recentes (9ª-11ª), variando entre os capítulos 8 e 10
conforme a edição]`

**Correção proposta para o draft:** trocar "a mecânica de opções só chega lá pelo 11" por algo
como "a mecânica de opções só chega bem mais adiante — lá pelo capítulo 10, dependendo da
edição" (mantém o efeito retórico de distância sem cravar um número que não se sustenta em
nenhuma edição checada).

## 4. Ordem do currículo CFA — Time Value of Money antes de Fixed Income

**Trecho do draft:** "valor do dinheiro no tempo entra logo no primeiro módulo, antes de renda
fixa, porque cada ferramenta dali vai ser reaproveitada depois."

**Veredito: ✅ Confirmado.** Time Value of Money é um reading do módulo "Quantitative Methods"
do currículo CFA Nível I (confirmado diretamente na página do CFA Institute: "2026 Curriculum
CFA® Program Level I Quantitative Methods"). Na lista oficial de áreas de tópico do Nível I,
Quantitative Methods é a 2ª área (logo após Ética), e Fixed Income é a 7ª — ou seja, TVM
antecede Fixed Income na estrutura oficial do currículo, não só na ordem de estudo recomendada.
Guias de preparação (300 Hours) recomendam explicitamente dominar TVM/Discounted Cash Flow antes
de entrar em Fixed Income, porque as técnicas são reaproveitadas na precificação de títulos.

Fontes:
- [Time Value of Money in Finance — CFA Institute, Refresher Reading 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/time-value-money)
  (fonte primária; acesso 2026-08-17)
- [2026 & 2027 Level 1 CFA® Exam Topic Weights — Soleadea](https://soleadea.org/cfa-level-1/topic-weights)
  (ordem oficial das 10 áreas de tópico; acesso 2026-08-17)
- [CFA Level 1 Fixed Income Cheat Sheet — 300 Hours](https://300hours.com/cfa-level-1-fixed-income-cheat-sheet/)
  (acesso 2026-08-17)

## 5. Definição de "valor do dinheiro no tempo"

**Trecho do draft:** "sobre um dos assuntos mais básicos de finanças... o valor do dinheiro no
tempo. É simples de calcular... Compreender de fato o que ela significa é outra história."

**Veredito: ✅ Confirmado — sem erro conceitual.** O post não desenvolve a definição técnica em
prosa (é só mencionada, como o próprio prompt desta etapa observa), então não há afirmação
formal a checar contra a literatura. A caracterização informal ("simples de calcular, mas
compreender o que significa é outra história") é compatível com a definição padrão — o valor do
dinheiro no tempo é o princípio de que uma quantia hoje vale mais que a mesma quantia nominal no
futuro por seu custo de oportunidade; a mecânica de cálculo (VP = VF / (1+i)^n) é de fato
trivial, enquanto a intuição econômica por trás (por que o dinheiro "perde valor" no tempo, como
isso se conecta a juros, risco e inflação) é onde a confusão de fato ocorre na prática — o que é
justamente a tese do post. Nenhuma contradição com a fonte primária consultada na pesquisa
(CFA Institute, Refresher Reading "Time Value of Money").

Fonte: [Time Value of Money in Finance — CFA Institute](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/time-value-money)
(já citada em `03-pesquisa.md`; revalidada nesta etapa em 2026-08-17)

## 6. Varredura do restante do texto

Reli o draft inteiro em busca de outros números, fórmulas, nomes ou citações sem fonte
verificável, além dos itens já listados no prompt desta etapa:

- **VaR — glossário** ("a métrica que estima quanto uma carteira pode perder num cenário
  ruim"): definição informal, mas compatível com a definição padrão de mercado (medida
  estatística do potencial de perda máxima de uma carteira, dado um horizonte de tempo e nível
  de confiança). Não é citação, é gloss — não requer fonte formal. Sem erro.
- **Processos estocásticos — glossário** ("a matemática que descreve fenômenos que evoluem no
  tempo com uma boa dose de aleatoriedade"): gloss informal correto, não é citação técnica
  formal, sem erro conceitual.
- **Não há nenhum número, percentual, valor monetário ou exemplo numérico hipotético** no draft
  (nenhuma conta de "invista R$X a Y% ao ano" ou equivalente) — não há cálculo a refazer nesta
  etapa.
- **Nenhuma norma/resolução/lei é citada** no draft — não há esse tipo de verificação a fazer.
- O restante das afirmações do texto (a experiência pessoal do autor na seção 1, a generalização
  sobre estagiários na seção 4, a observação sobre pesquisa acadêmica na seção 2) já foi tratado
  em `03-pesquisa.md` como material autobiográfico/observação pessoal generalizável, não dado
  externo — consistente com a moldura do briefing, nada a reclassificar aqui.

Nenhum outro item pendente encontrado.

## Resumo

5 itens verificados nesta etapa: **4 confirmados** (✅ GFMI = Global Financial Markets
Institute; ✅ citação da GFMI fiel ao original; ✅ CFA = Chartered Financial Analyst, com
caracterização defensável; ✅ ordem do currículo CFA — TVM antes de Fixed Income; ✅ capítulos
4-6 de Hull sobre juros/preço a termo, estáveis entre edições; ✅ definição de "valor do dinheiro
no tempo" sem erro conceitual) e **1 impreciso** (⚠️ "capítulo 11" para mecânica de opções em
Hull — o número varia por edição e, em nenhuma edição checada, corresponde exatamente ao
capítulo que introduz a mecânica de opções; correção proposta acima, marcada como `[FAIXA:...]`).
Nenhum item ficou como `[VERIFICAR]` aberto — as duas pendências deixadas por `06-revisao.md`
(GFMI e CFA) foram resolvidas com fonte primária. Nada bloqueia a etapa 8 (visuais); a única ação
pendente para a consolidação é aplicar as três correções textuais listadas acima (expansão de
GFMI, expansão de CFA, ajuste do número do capítulo de Hull).

## Lista consolidada para a etapa de consolidação

- `[FAIXA: a mecânica de opções só chega lá pelo 11 → a mecânica de opções só chega bem mais
  adiante — capítulo 10 nas edições mais recentes (9ª-11ª), variando entre os capítulos 8 e 10
  conforme a edição]`

Nenhum `[VERIFICAR: ...]` resta em aberto — GFMI e CFA foram ambos confirmados com fonte
primária e suas expansões devem ser aplicadas diretamente no texto (ver correções nas seções 1
e 2 acima), sem necessidade de placeholder.
