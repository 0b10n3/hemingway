# 03 — Pesquisa

Fonte: `00-transcricao.md`, `01-briefing.md`, `02-estrutura.md`. Pesquisa feita via busca web
em 2026-08-16 (data de acesso de todas as fontes abaixo, salvo indicação contrária). Executada
pelo agente `pesquisador-editorial`.

## Seção 1 — Abertura ("A conta batia. O produto, não.")

Não requer pesquisa externa — é cena autobiográfica do autor, já registrada no briefing como
material não substituível. Nada a acrescentar aqui.

## Seção 2 — "Bem-vindo à linha Spoiler — e ao mundo invertido, de novo"

**Afirmação da estrutura a sustentar:** a academia (sobretudo em matemática/pesquisa recente)
empurra para a ponta complexa dos produtos (opções, contratos avançados), tornando o começo
invertido comum, não uma falha pessoal.

- Suporte parcial encontrado: artigo do QuantStart ("Why a Masters in Finance Won't Make You a
  Quant Trader") descreve que o núcleo de praticamente todos os programas de Mestrado em
  Engenharia Financeira (MFE) é cálculo estocástico aplicado a precificação de opções e ao
  modelo Black-Scholes — i.e., a produção acadêmica recente em finanças quantitativas de fato
  converge para produtos complexos como núcleo curricular.
  Fonte: [Why a Masters in Finance Won't Make You a Quant Trader — QuantStart](https://www.quantstart.com/articles/Why-a-Masters-in-Finance-Wont-Make-You-a-Quant-Trader/)
- Não encontrei um estudo formal (survey, paper de educação financeira) que meça ou documente
  esse viés curricular de forma sistemática — é inferência razoável a partir da estrutura de
  currículos de MFE, não um dado citável isolado. Se o post quiser afirmar isso como "fato do
  mercado", recomendo tratar como observação do autor (o que já é a moldura do briefing), não
  como dado externo.

## Seção 3 — "A segunda lacuna: dinheiro no tempo" (pilar Dado + `graf-01`)

Esta é a seção que mais precisava de sustentação externa (o dado é "estrutural, não
estatístico" segundo a própria estrutura). Encontrei evidência real e citável de que valor do
dinheiro no tempo/juros são pré-requisito reconhecido — em três fontes independentes:
currículo profissional (CFA), livro-texto de referência (Hull) e provedor de treinamento de
mercado (GFMI/VaR).

**1. CFA Institute — ordem do currículo.**
O programa CFA ensina Time Value of Money dentro de "Quantitative Methods" no Nível I, e a
recomendação de estudo é dominar esse módulo antes de Fixed Income, porque as técnicas de TVM
são usadas na precificação de títulos. TVM é retomado depois em Fixed Income, Equity Valuation
e Derivatives.
Fontes: [CFA Level 1 Fixed Income Cheat Sheet — 300 Hours](https://300hours.com/cfa-level-1-fixed-income-cheat-sheet/);
[Time Value of Money in Finance — CFA Institute](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/time-value-money)

**2. Hull, "Options, Futures, and Other Derivatives" — estrutura do livro-texto padrão do
mercado.**
O livro mais usado como referência para precificação de derivativos trata taxas de juros
(capítulo 4) e determinação de preços a termo/futuros (capítulos 5-6) antes de chegar à
mecânica de opções (capítulo 11) e ao modelo Black-Scholes-Merton (capítulo 16). Ou seja: mesmo
a referência canônica de precificação de opções pressupõe entendimento de juros e estrutura a
termo como pré-requisito de organização didática.
Fonte: [Options, Futures, and Other Derivatives — Pearson (ficha do livro)](https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005938/9780136939917);
estrutura de capítulos confirmada via [PDF da edição em circulação acadêmica](http://lib.ysu.am/disciplines_bk/2b66030e0dd4c77b2bda437f6c1e5e66.pdf)

**3. FRM (GARP) — currículo de risco de mercado.**
O FRM Parte I é estruturado em quatro blocos: Foundations of Risk Management, Quantitative
Analysis, Financial Markets & Products, e só por último Valuation and Risk Models (onde entra
VaR). A ordem de estudo recomendada por quem já passou segue exatamente essa sequência — dos
fundamentos para o modelo de risco avançado.
Fonte: [FRM Part I and II Curriculum Overview — AnalystPrep](https://analystprep.com/study-notes/frm/frm-level-1-syllabus/);
[FRM Exam Guide 2026 — 300 Hours](https://300hours.com/frm/)

**4. A peça mais forte: pré-requisito explícito de um provedor de treinamento de VaR.**
A página do curso de Value at Risk da GFMI (provedor de treinamento profissional para risco de
mercado) lista como pré-requisito textual: *"Participants should understand simple financial
concepts such as present value and the calculation of returns"* — e, crucialmente, também
afirma: *"No advanced knowledge of mathematics or statistics is required."* Isso é evidência
direta e citável de que, na prática de mercado (não só na academia), o valor presente (núcleo
do "valor do dinheiro no tempo") é tratado como pré-requisito de VaR, e que o gargalo de fato
**não é** a matemática avançada — o que reforça diretamente a tese do post (o autor dominava a
matemática; faltava o "básico" operacional).
Fonte: [Value at Risk Course — GFMI](https://www.gfmi.com/training_courses/value-at-risk-course/)
(conteúdo confirmado via fetch em 2026-08-16)

**5. Corporate Finance Institute — estrutura do curso "Market Risk Fundamentals".**
O curso da CFI constrói a sequência: o que é risco de mercado → volatilidade → VaR paramétrico
(posição única, depois portfólio) → cenários mais complexos — posicionando VaR como tópico de
capstone, no fim da progressão, não no início.
Fonte: [Market Risk Fundamentals — Corporate Finance Institute](https://corporatefinanceinstitute.com/course/market-risk-fundamentals/)
(conteúdo confirmado via fetch em 2026-08-16)

**Conclusão para a seção 3:** há material real e citável (não estatístico, mas estrutural —
exatamente como a estrutura pede) em três frentes independentes (currículo de certificação
profissional, livro-texto padrão de mercado, e provedor de treinamento prático de risco) que
convergem na mesma ordem: juros/valor do dinheiro no tempo antes de derivativos/VaR. A peça da
GFMI é a mais forte porque nomeia explicitamente "present value" como pré-requisito e diz que
matemática avançada não é o gargalo — pode ser útil para a etapa 7 (verificação técnica) se o
draft quiser ancorar a afirmação estrutural em algo verificável além da experiência pessoal do
autor.

## Seção 4 — "Não é só quem veio da academia" (estagiário em mesa de risco/VaR)

**O que a estrutura pede:** evidência de que estagiários caem direto em mesas de risco/VaR
complexas e ficam "presos na rotina sem entender a rotina".

- **Não encontrei estudo formal, survey de mercado de trabalho ou pesquisa publicada** que
  documente esse padrão especificamente para estagiários de mesas de risco/VaR. Reporto isso
  como "não encontrado" — não force estatística aqui.
- Encontrei suporte qualitativo/anedótico (não é fonte acadêmica, tratar com essa ressalva se
  usado): artigo do QuantStart sobre a transição de PhD para quant trader afirma que as lacunas
  mais comuns em recém-contratados com forte base matemática são "programação, conhecimento de
  domínio financeiro e intuição de mercado" e que "entender a mecânica básica do mercado em que
  você escolheu trabalhar... não é algo que um programa de MFE ou PhD vai realmente ensinar".
  Isso é consistente com o argumento do post, mas fala de PhDs contratados como quants, não
  especificamente de estagiários em mesas de VaR — é adjacente, não uma correspondência exata.
  Fonte: [How To Get A Quant Job Once You Have A PhD — QuantStart](https://www.quantstart.com/articles/How-To-Get-A-Quant-Job-Once-You-Have-A-PhD/)
- Fóruns como Wall Street Oasis têm threads anedóticos sobre matemática em mesas de trading,
  mas não achei um relato citável e específico sobre "estagiário preso na rotina sem entender a
  rotina" — não recomendo usar fórum anônimo como fonte no post; é ruído, não evidência.
- Referência literária adjacente (não é evidência empírica, é depoimento profissional
  publicado, pode servir como pano de fundo cultural se o autor quiser mencionar): Emanuel
  Derman, *My Life as a Quant: Reflections on Physics and Finance* (Wiley, 2004) — reflete
  sobre o conflito entre o rigor dos modelos físicos/matemáticos e a "hurly-burly" dos mercados
  reais, e sobre os limites de aplicar métodos precisos de física a finanças. É sobre risco de
  modelo e a natureza do conhecimento em física vs. finanças — não é exatamente "não entender o
  produto apesar de saber a matemática", mas é o relato mais próximo e citável de um quant
  reconhecido nomeando essa tensão.
  Fonte: [My Life as a Quant — Wiley](https://www.wiley.com/en-us/My+Life+as+a+Quant:+Reflections+on+Physics+and+Finance-p-9780470192733)

**Conclusão para a seção 4:** a generalização para "estagiário em mesa de VaR" permanece
sustentada apenas pela observação pessoal do autor (que é exatamente o que o briefing já
previa — "a tese se sustenta como observação pessoal generalizável, não como dado
estatístico"). Nenhuma fonte externa contradiz isso, mas também nenhuma o confirma com dado
duro. Recomendo manter como está: generalização, não estatística.

## Seção 5 — "Sem orgulho, sem falsa humildade"

Não requer pesquisa externa — é postura pessoal do autor, registrada no briefing.

## Seção 6 — Fechamento (curso e convite)

Não requer pesquisa externa — detalhes do curso já vêm de `_arquivo/MARKETING_REVIEW.md`, fora
do escopo desta pesquisa.

## Contraponto genuíno (para o autor saber que existe, não necessariamente para incorporar)

Existe debate pedagógico real sobre começar pelo "todo complexo" em vez de pelos fundamentos
isolados. Resumo honesto, incluindo onde o crítico tem razão:

1. **Cognitive Load Theory (Sweller, 1988)** — na verdade **reforça** a tese do post, não a
   contesta: a teoria mostra que resolver problemas complexos sem os esquemas de pré-requisito
   sobrecarrega a memória de trabalho, o que impede reter a regra geral por trás da solução —
   coerente com o relato do autor de saber derivar o modelo sem "aprender de fato o produto".
   Útil como pano de fundo teórico se o verificador técnico quiser, mas é apoio, não
   contraponto.
   Fonte: [Cognitive Load During Problem Solving — Sweller (1988), Cognitive Science 12(2)](https://mrbartonmaths.com/resourcesnew/8.%20Research/Explicit%20Instruction/Cognitive%20Load%20during%20problem%20solving.pdf)

2. **David Perkins, *Making Learning Whole* (Jossey-Bass, 2009)** — argumento sério a favor de
   começar pelo "jogo inteiro" em vez de fragmentos isolados: crianças aprendem beisebol
   jogando uma "versão júnior" do jogo completo desde o início, não praticando fundamentos
   isolados (rebater, correr as bases) sem contexto. **Onde o crítico tem razão:** há evidência
   pedagógica de que aprender fragmentos sem ver o "jogo inteiro" também prejudica a retenção e
   a motivação. **Onde a analogia falha para o caso do post:** a "versão júnior" de Perkins
   ainda é simplificada — o autor não teve uma versão júnior do produto financeiro, teve a
   versão adulta completa (o modelo de precificação real) sem o contexto do jogo inteiro (a
   dinâmica do mercado). Ou seja, o contraponto de Perkins pode ser usado *contra* a leitura
   "sempre comece pelo simples isolado", mas não sustenta "comece pela ponta mais complexa sem
   contexto" — que é o que aconteceu com o autor. É uma nuance a favor de "comece pelo todo
   simplificado", não "comece pelo avançado".
   Fonte: [Making Learning Whole — resenha/resumo, The 74](https://www.the74million.org/article/74-interview-author-and-harvard-scholar-david-perkins-on-what-traditional-classroom-teachers-can-learn-from-science-fairs-backyard-sports-whole-game-learning/);
   livro original: Perkins, D. (2009). *Making Learning Whole: How Seven Principles of Teaching
   Can Transform Education*. Jossey-Bass.

3. **Jean Lave & Etienne Wenger, *Situated Learning: Legitimate Peripheral Participation*
   (Cambridge University Press, 1991)** — teoria de aprendizagem por aprendizado
   situado/comunidades de prática: aprendizes de ofício (parteiras, alfaiates, contramestres da
   Marinha) são inseridos desde cedo na complexidade real da prática, não isolados dela.
   **Onde o crítico tem razão:** há apoio empírico de que ver a complexidade do "todo" desde
   cedo ajuda o aprendiz a formar um mapa mental do que a prática significa. **Onde a analogia
   se complica a favor do post, não contra:** a mesma pesquisa mostra que, apesar de estarem
   cercados da complexidade, os aprendizes começam com tarefas *periféricas, de baixo risco* —
   não com a tarefa mais difícil do ofício. É exatamente o inverso do que aconteceu ao autor
   (que começou pela tarefa/conceito mais avançado, não por uma tarefa periférica simples dentro
   de um contexto complexo). Esse é, na prática, um contraponto que se autodesarma quando
   examinado de perto — vale mencionar ao autor porque é sofisticado, mas não sustenta "comece
   pela precificação de opções sem entender juros".
   Fonte: [Situated Learning: Legitimate Peripheral Participation — Cambridge University Press](https://www.cambridge.org/highereducation/books/situated-learning/6915ABD21C8E4619F750A4D4ACA616CD)

4. **Jerome Bruner, currículo em espiral (*The Process of Education*, 1960)** — hipótese de que
   qualquer assunto pode ser ensinado em forma intelectualmente honesta a qualquer estágio,
   desde que se comece por uma versão intuitiva e simplificada da ideia complexa, revisitada com
   rigor crescente ao longo do tempo. Isso é o contraponto mais próximo de "pode fazer sentido
   começar por uma versão simplificada do avançado" — mas de novo, "versão simplificada" é a
   chave: não é a mesma coisa que aprender a derivação completa de Black-Scholes sem entender o
   que é uma taxa de juros.
   Fonte: [Bruner's Spiral Curriculum — Structural Learning](https://www.structural-learning.com/post/the-spiral-curriculum-a-teachers-guide)

5. **B. C. Regan, "An Ahistorical Approach to Elementary Physics" (arXiv, 2020)** — argumento de
   um físico de que ensinar física seguindo a ordem histórica de descoberta (mecânica clássica →
   eletromagnetismo → moderna) é pedagogicamente menos econômico do que partir de um arcabouço
   unificado mais moderno (ondas no espaço-tempo da relatividade especial) para depois derivar
   os conceitos clássicos. É um contraponto real e citável ao "sempre siga a ordem
   histórica/incremental" — mas note que é sobre reordenar o *arcabouço conceitual* (usar uma
   abstração mais unificada em vez de conceitos fragmentados historicamente acumulados), não
   sobre pular pré-requisitos de fato. Vale como contraponto genuíno de que "básico" não é
   sempre sinônimo de "histórico/incremental" — mas não ataca a tese central do post, que é
   sobre pular a base operacional, não sobre a ordem histórica de descoberta.
   Fonte: [An Ahistorical Approach to Elementary Physics — arXiv:2010.10271](https://arxiv.org/abs/2010.10271)

**Síntese do contraponto:** existe, sim, uma literatura pedagógica séria que valoriza ver o
"todo complexo" cedo. Mas, examinada de perto, essa literatura defende uma *versão
simplificada e contextualizada* do complexo (jogo júnior, arcabouço unificado, tarefa
periférica dentro de um ambiente complexo) — não a exposição direta e sem apoio à forma mais
avançada do conhecimento, que é o que a estrutura descreve ter acontecido com o autor e com o
estagiário de mesa de VaR. Isso significa que o contraponto mais forte contra a tese do post,
se alguém quisesse fazê-lo, provavelmente teria que argumentar "a experiência do autor não foi
'complexidade sem contexto', foi uma versão júnior legítima (dissertação de mestrado
orientada) que ele está reinterpretando romanticamente depois do fato" — um contraponto
possível, mas que exigiria contestar o relato autobiográfico do autor, não a estrutura
pedagógica em si.

## Definição de "valor do dinheiro no tempo" (para uso da etapa 7, verificação técnica)

**Definição padrão:** o valor do dinheiro no tempo é o princípio de que uma quantia disponível
hoje vale mais do que a mesma quantia nominal recebida no futuro, devido à sua capacidade de
gerar retorno (custo de oportunidade do capital) — é o fundamento sobre o qual se constroem
valor presente, valor futuro e taxas de desconto.

Fontes citáveis prontas para verificação técnica:
- [Time Value of Money in Finance — CFA Institute, Refresher Reading 2026](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/time-value-money) —
  fonte primária, autoridade do setor, definição alinhada ao currículo profissional padrão.
- Livro-texto de referência (não consultado em texto integral nesta pesquisa, mas amplamente
  citado como fonte padrão): Brealey, R.A., Myers, S.C. & Allen, F., *Principles of Corporate
  Finance*, McGraw-Hill (edição mais recente disponível na época da verificação técnica) —
  capítulo introdutório sobre valor presente/VPL.
- Alternativa: Ross, S.A., Westerfield, R.W. & Jaffe, J., *Corporate Finance*, McGraw-Hill —
  mesmo tratamento padrão.

Não desenvolvi a definição em prosa aqui porque, conforme o briefing, isso é conteúdo de
referência fora do escopo do post — só deixo a fonte pronta para a etapa 7 conferir se o gloss
mínimo usado no texto está correto.

## Resumo

Encontrei sustentação real e citável para o "dado estrutural" da seção 3: currículo CFA,
livro-texto de Hull e, principalmente, um provedor de treinamento de VaR (GFMI) que lista
"present value" como pré-requisito explícito e diz que matemática avançada não é o gargalo —
peça forte para ancorar a tese. Não encontrei estudo/estatística sobre estagiários de mesas de
VaR (seção 4) nem sobre viés curricular acadêmico documentado formalmente (seção 2) —
reportado como "não encontrado", conforme instruído. Localizei contrapontos pedagógicos
genuínos (Perkins, Lave & Wenger, Bruner, um paper de física sobre ensino "ahistórico") — todos
defendem versões simplificadas/contextualizadas do complexo, não a exposição direta ao
avançado sem base, então nenhum ataca a tese central de frente. Fonte pronta para a definição
de "valor do dinheiro no tempo" também está registrada, para uso da etapa 7.
