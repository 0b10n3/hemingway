# Frente B — Estilometria aplicada para extração de guia de voz autoral

## 1. Eixos estabelecidos de análise estilométrica

A literatura clássica (Stamatatos, "A Survey of Modern Authorship Attribution Methods", 2009) organiza traços de estilo em camadas — léxico, sintático, caractere/n-gramas, estrutural e semântico —, e frameworks de estilística aplicada (ex.: modelo de sete camadas usado por guias de "controle de estilo para IA") acrescentam níveis fonológico/rítmico, gráfico-tipográfico e pragmático-discursivo. Combinando essas fontes, os eixos mais recorrentes são:

- **Léxico**: riqueza vocabular (type-token ratio, hapax legomena, curva de crescimento de vocabulário), preferência por palavras funcionais (function words) — o traço mais estudado em atribuição de autoria —, registro/formalidade, campos semânticos recorrentes.
- **Sintático**: comprimento médio de frase, variância desse comprimento, proporção de orações simples/compostas/complexas, razão coordenação vs. subordinação, uso de voz passiva, POS n-gramas.
- **Pontuação e ritmo**: distribuição de pontuação (vírgulas, travessões, reticências, ponto e vírgula), tratada como camada "gráfica"; cadência frasal (alternância de frases curtas/longas — "burstiness") como marca rítmica pessoal.
- **Discursivo/estrutural**: organização macro do texto (abertura, progressão, fechamento), uso de conectivos e árvores de discurso (Rhetorical Structure Theory), ponto de vista, coesão.
- **Retórico/persona**: figuras de linguagem, analogias/metáforas recorrentes, tom, estratégias de persuasão, "voz" no sentido de presença autoral perceptível.

## 2. Híbrido quantitativo + qualitativo vs. abordagens puras

Não há um único "paper definitivo" comparando as duas abordagens para geração de guias de voz, mas a evidência converge em uma direção clara: **avaliação puramente qualitativa (impressão de leitura, inclusive por LLM) é sistematicamente menos confiável do que quando ancorada em métricas**. Estudos recentes sobre "LLM-as-judge" mostram que juízes de LLM são sensíveis a estilo de superfície e confundem "substância" com "estilo de apresentação", exibindo alta confiança mesmo quando o julgamento está errado (arXiv 2608.01666, "Style Wins, Substance Loses"). A resposta proposta nessa literatura é justamente instrumentar o julgamento qualitativo com métricas quantitativas de apoio (ex.: Style Bias Index) para estabilizar o veredito. Do lado da estilometria clássica, o argumento inverso também aparece: métodos puramente baseados em intuição/regras (ex.: guias de siete camadas para "controlar estilo de IA") produzem descrições operacionais, mas não têm mecanismo de checagem — um observador pode nomear um traço que soa plausível sem que ele realmente discrimine o autor de outros. A prática estabelecida em estilometria computacional (Burrows' Delta, contagem de function words) é precisamente contar para não "alucinar" traço: a frequência e a dispersão do traço no corpus são o critério de realidade, não a impressão de um leitor.

## 3. Limiares de evidência em corpora pequenos

Para atribuição de autoria, Eder ("Does size matter? Authorship attribution, small samples, big problem", 2013; "Short Samples in Authorship Attribution: A New Approach", DH2017) é a referência central: amostras confiáveis giram em torno de **5.000 palavras corridas**; abaixo de ~3.000 palavras a taxa de atribuição incorreta pode superar 60%; 2.000 palavras é citado como piso absoluto em alguns estudos, e 500 palavras aparece como mínimo extremo, pouco confiável. Um segundo critério, complementar à contagem bruta, é a **dispersão**: um traço só deve ser considerado parte do estilo do autor se aparecer de forma relativamente homogênea através de múltiplos textos distintos, não concentrado em um único documento (conceito de dispersão lexical de Gries, 2008/2020). Ou seja, dois limiares combinados: (a) volume mínimo de texto por amostra/autor (ordem de milhares de palavras) e (b) recorrência do traço em vários textos separados, não apenas frequência agregada.

## 4. Separar traço autoral de traço condicionado por gênero

Este é um problema ativo na literatura ("Register variation explains stylometric authorship analysis", Nini et al.; "The Importance of Suppressing Domain Style in Authorship Analysis", arXiv 2005.14714): muitas variáveis estilométricas tradicionais são sensíveis a tema/gênero, e parte do que parece "sinal de autor" é na verdade sinal de registro. Estratégias recomendadas: (1) **unmasking** (Koppel & Schler) — testar a robustez de um traço removendo iterativamente as features mais discriminantes e verificando se o sinal de autor sobrevive entre gêneros; (2) construir corpora deliberadamente heterogêneos por gênero e comparar o mesmo autor através deles, retendo apenas traços estáveis; (3) "penalizar" ou controlar estatisticamente sinais de gênero/cronologia a posteriori; (4) preferir features menos sensíveis a tópico (function words, pontuação, estrutura sintática) a features lexicais de conteúdo, que carregam tema. Para um extrator prático: ao montar o corpus de amostras, marcar cada texto com seu gênero/formato e exigir que um traço apareça em pelo menos dois formatos diferentes antes de promovê-lo a "traço geral da voz"; traços que só aparecem em um formato devem ser rotulados como condicionados a esse formato, não como voz autoral universal.

---

## Fontes

- [A Survey of Modern Authorship Attribution Methods — Stamatatos (PDF)](https://icsdweb.aegean.gr/stamatatos/papers/survey.pdf)
- [Syntactic Stylometry: Using Sentence Structure for Authorship Attribution](https://ai.uga.edu/sites/default/files/inline-files/theses/hollingsworth_charles_d_201208_ms.pdf)
- [Unveiling Authorship via Computational Stylometry (arXiv 2501.09561)](https://arxiv.org/pdf/2501.09561)
- [A Systematic Method for Controlling AI Writing Style — Tricontinental](https://thetricontinental.org/a-systematic-method-for-controlling-ai-writing-style/)
- [Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation (arXiv 2608.01666)](https://arxiv.org/abs/2608.01666)
- [Quantitative LLM Judges (arXiv 2506.02945)](https://arxiv.org/html/2506.02945)
- [Do LLMs write like humans? Variation in grammatical and rhetorical styles — PNAS](https://www.pnas.org/doi/10.1073/pnas.2422455122)
- [Short Samples in Authorship Attribution — OpenMethods (resumo de Eder)](https://openmethods.dariah.eu/2017/09/20/microsoft-word-341-eder-short-samples-in-authorship-attribution-341-docx-341-pdf/)
- [Does size matter? Authorship attribution, small samples, big problem — Eder](https://www.academia.edu/17435663/Does_size_matter_Authorship_attribution_small_samples_big_problem)
- [Short Samples in Authorship Attribution: A New Approach — Eder, DH2017 (PDF)](https://dh2017.adho.org/abstracts/341/341.pdf)
- [Survey of Methods in Computational Literary Studies — Corpus Building for Authorship Attribution](https://methods.clsinfra.io/corpus-author.html)
- [The Importance of Suppressing Domain Style in Authorship Analysis (arXiv 2005.14714)](https://arxiv.org/pdf/2005.14714)
- [Register variation explains stylometric authorship analysis — ResearchGate](https://www.researchgate.net/publication/366812943_Register_variation_explains_stylometric_authorship_analysis)
- [Evaluating Unmasking for Cross-Genre Authorship Verification — Koppel & Schler line of work](https://www.academia.edu/30905510/Evaluating_unmasking_for_cross_genre_authorship_verification)
- [Computational Methods in Authorship Attribution — Koppel, Schler, Argamon (PDF)](https://u.cs.biu.ac.il/~koppel/papers/authorship-JASIST-final.pdf)
- [Measuring and interpreting lexical dispersion in corpus linguistics](https://www.researchgate.net/publication/320731532_Measuring_and_interpreting_lexical_dispersion_in_corpus_linguistics)
- [Chapter 5, Analyzing Dispersion — Stefan Th. Gries (PDF)](https://www.stgries.info/research/2020_STG_Dispersion_PHCL.pdf)
- [Stylometric Detection: Methods & Applications](https://www.emergentmind.com/topics/stylometric-detection)
