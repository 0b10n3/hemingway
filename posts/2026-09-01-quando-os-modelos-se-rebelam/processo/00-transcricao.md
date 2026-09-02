# Quando os Modelos se Rebelam

### Por que o descolamento entre modelo e realidade é esperado — e por que entender isso separa um bom modelador de um extremista frustrado

---

Vez ou outra compartilho aqui conteúdo de aulas do MIT OpenCourseWare. Eles mantêm uma quantidade enorme de aulas e cursos disponibilizados gratuitamente.

Entre esses materiais está a disciplina _Topics in Mathematics with Applications in Finance_ (18.S096, na versão de 2013, atualizada como 18.642 em 2024). A disciplina é um passeio, a passo rápido, por uma série de ferramentas e modelos matemáticos que são fundamentais em finanças.

Um dos meus momentos favoritos do curso é a aula de probabilidade (_Probability Theory_) do professor Peter Kempthorne. Em uma explicação sobre a ideia de retorno à média, Kempthorne diz:

> "Se você lança uma moeda 100 vezes, obtendo cara em todos os lançamentos, você deveria estar considerando seriamente a possibilidade de que essa moeda tenha algum vício ou defeito."

A frase é dita no contexto de que muitas pessoas começam a esperar o "retorno à média", mas acabam se esquecendo de que a média pode ter sido alterada na realidade.

Esse tipo de pensamento equivocado — bastante presente quando o problema envolve probabilidades — se apresenta como sintoma de uma compreensão parcial, ou mesmo equivocada, do funcionamento de modelos.

Uma má compreensão do que são modelos, de como funcionam e da importância das hipóteses que os fundamentam pode ser a diferença entre ser um "modeleiro" bem-sucedido ou se tornar um frustrado extremista ante modelos.

No texto de hoje vamos tratar dessas ideias e mostrar como o desacoplamento entre modelo e realidade pode levar até mesmo vencedores do Prêmio Nobel ao desastre.

---

## 1. Três palavras que você usa como sinônimo e não são

Emanuel Derman é uma figura útil aqui porque ele conhece os dois lados da história: doutor em física teórica de partículas, foi para a Goldman Sachs e virou um dos nomes centrais da engenharia financeira, coautor do modelo de volatilidade local Derman–Kani.

Em _Models. Behaving. Badly._ (2011), ele propõe uma separação que vale a pena levar a sério: **teoria**, **modelo** e **intuição** são três coisas diferentes.

**Teoria** é a tentativa de descrever o que uma coisa _é_. Uma teoria bem-sucedida se torna indistinguível do fenômeno. As equações de Maxwell não se parecem com o eletromagnetismo; dentro da física clássica, elas _são_ o eletromagnetismo. Teorias pedem confirmação empírica, mas não pedem justificativa: não faz sentido perguntar "por que você escolheu comparar a luz com uma onda eletromagnética?".

**Modelo** é a tentativa de descrever com o que uma coisa _se parece_. Um modelo se apoia sempre em terreno emprestado: é uma analogia, uma metáfora que compara o objeto de estudo a outra coisa cuja dinâmica você já sabe manipular. Black–Scholes trata o preço de uma ação como fumaça se difundindo numa sala. A semelhança é sempre parcial, e por isso todo modelo exige justificativa: você precisa defender por que a analogia se sustenta _neste_ caso.

**Intuição** é o terceiro termo, e é o mais fácil de descartar como misticismo — o que seria um erro. Na acepção de Derman, intuição não é palpite: é o resultado da imersão prolongada em um domínio, o ponto em que você para de operar a ferramenta e passa a pensar através dela. É o que permite a um gestor de risco olhar para um número que saiu do sistema e dizer "esse número está errado" antes de conseguir explicar por quê.

Em finanças, o que existe são modelos. Não teorias. CAPM, Black–Scholes, Hipótese dos Mercados Eficientes, Vasicek, Gordon: todos imitam o _estilo_ da física e usam a _sintaxe_ da matemática, mas não têm a mesma ancoragem ontológica.

||**Teoria** (ex.: eletromagnetismo)|**Modelo** (ex.: Black–Scholes)|
|---|---|---|
|O que faz|Descreve o que a coisa é|Descreve com o que a coisa se parece|
|Fundamento|Próprio|Emprestado, por analogia|
|Exige justificativa?|Não. Exige confirmação|Sim, sempre. E a defesa é contextual|
|Quando falha|Revela um limite físico novo (clássico → quântico)|Revela que a analogia deixou de servir naquele cenário|
|Reflexividade|Nenhuma. O elétron não lê o paper|Alta. O mercado adota o modelo e muda de comportamento|

### E onde entram as "hipóteses"?

Aqui mora uma armadilha específica da nossa língua. Em inglês existem duas palavras: _hypothesis_ (conjectura testável, que a metodologia científica manda você tentar falsear) e _assumption_ (premissa, condição de contorno assumida como verdadeira para a construção seguir de pé).

Em português, as duas viram **hipótese**.

O resultado é que o aluno aprende "as hipóteses do modelo de Black–Scholes" e as coloca mentalmente na mesma caixa de "hipótese nula" — como formalidade de demonstração, coisa que aparece no slide antes da fórmula e depois some. Não é isso. As hipóteses de Black–Scholes não são conjecturas a testar: são **a bula do remédio**. Elas definem o domínio de validade do instrumento. Ignorá-las não é imprecisão acadêmica, é usar o aparelho fora da faixa de operação.

O leitor mais rigoroso pode se perguntar: essa taxonomia é rigorosa ou se é a licença poética de um físico que virou banqueiro? A resposta honesta é: **bate em parte**.

| Ponto de Derman | O que diz a filosofia da ciência | Veredito |
|---|---|---|
| Modelos são representações parciais e deliberadamente distorcidas | Convergência forte. Nancy Cartwright (_How the Laws of Physics Lie_, 1983) argumenta que até as leis fundamentais só são literalmente verdadeiras sobre modelos idealizados. George Box: todos os modelos estão errados, alguns são úteis | Alinhado |
| Modelo falha ⇒ a analogia deixou de servir | Duhem–Quine complica: quando uma predição falha, o teste atinge o _conjunto_ (núcleo + premissas auxiliares + calibração + dados). Você nunca consegue isolar logicamente o culpado | Alinhado, mas incompleto — e a incompletude importa |
| Teoria é categoricamente distinta de modelo | Aqui há discordância real. Na **visão semântica** das teorias (Suppes, van Fraassen, Giere), teorias _são_ famílias de modelos. As equações de Maxwell também idealizam: vácuo perfeito, cargas pontuais, meios homogêneos | Fronteira mais borrada do que Derman pinta |

Minha leitura: trate a distinção como uma **ferramenta de ancoragem**, não como uma parede. De um lado, construções que sobrevivem a testes de falseamento cada vez mais severos e cujo objeto não reage a elas. Do outro, construções cujo objeto é feito de gente que lê o próprio modelo. Finanças mora firmemente do lado direito e Derman está certo no que importa: tratar a segunda coisa como se fosse a primeira é a origem do problema.

---

## 2. O radar da rodovia

Um exemplo fora de finanças ajuda, porque nele ninguém tem viés comportamental.

Pense num radar de solo. Ele mede o tempo que o veículo leva para cruzar um intervalo minúsculo entre dois sensores e reporta a velocidade média nesse intervalo. Depois trata esse número como se fosse a velocidade instantânea.

Matematicamente, isso é uma troca: velocidade média por velocidade instantânea. A troca só é válida porque o movimento é contínuo e suave. A inércia garante que o carro não teleporta de 10 km/h para 100 km/h — ele precisa passar por 40, 60 e 80 no caminho. Sob essa premissa, a aproximação é excelente e o radar funciona muito bem.

Agora quebre a premissa. Imagine que a aceleração pudesse dar um salto instantâneo, sem percorrer os valores intermediários. O radar continuaria calculando corretamente e continuaria entregando um número sem sentido. **A matemática seguiria perfeita; o cenário é que teria mudado.**

Guarde essa frase, porque ela descreve praticamente todo desastre de modelo que você vai ver na sua carreira.

Quase nunca a conta está errada.

O que está errado é o contexto em que a conta foi aplicada.

---

## 3. Black–Scholes: o que está na bula

Black–Scholes é o caso clássico, porque a bula é longa e quase ninguém lê até o fim.

O modelo assume, entre outras coisas:

1. O preço do ativo segue um Movimento Browniano Geométrico — trajetórias **contínuas**, sem saltos;
2. **Volatilidade constante** ao longo da vida da opção;
3. Taxa livre de risco constante e conhecida;
4. Ausência de custos de transação e impostos;
5. Possibilidade de negociar e **rebalancear o hedge em tempo contínuo**;
6. Liquidez ilimitada, venda a descoberto livre, divisibilidade dos ativos.

Repare que as hipóteses 1, 5 e 6 são, na prática, uma coisa só: a possibilidade de o vendedor da opção se ajustar continuamente enquanto o mundo se move. É daí que sai o argumento de não-arbitragem, e é daí que sai o preço.

E é exatamente essa a premissa que o mercado brasileiro adora quebrar.

**18 de maio de 2017.** Na noite anterior vaza a gravação entre Joesley Batista e o então presidente Michel Temer. Na abertura, o Ibovespa cai o suficiente para acionar o primeiro _circuit breaker_ desde 2008; a queda chega a 10,47% no intradiário e o índice fecha a −8,80%, a maior baixa diária desde outubro de 2008. O dólar sobe 8,06% no mesmo pregão, de R$ 3,14 para R$ 3,38.

Pergunte a quem estava vendido em opções naquela manhã quantas vezes conseguiu rebalancear o delta entre o fechamento do dia 17 e a abertura do dia 18. A resposta é zero. Não porque o operador foi lento, mas porque **não existiu preço no meio do caminho**. O modelo pressupõe um filme; o que aconteceu foi um corte do editor.

O mercado, aliás, já tinha admitido isso muito antes. Depois do crash de outubro de 1987, a superfície de volatilidade implícita deixou de ser plana e passou a exibir o famoso _smile_ (ou _skew_).

Em português direto: os preços praticados passaram a embutir, permanentemente, uma probabilidade de salto maior do que a que o modelo comporta. O _smile_ é a cicatriz da hipótese 1 — o mercado usa a fórmula de Black–Scholes como uma linguagem de cotação e ajusta a premissa por fora, mexendo no _input_ de volatilidade.

E há um detalhe que o sociólogo Donald MacKenzie explora bem em _An Engine, Not a Camera_ (2006): Black–Scholes não apenas descreveu o mercado de opções, ele **o transformou**.

Depois de 1973, com a fórmula difundida em tabelas e calculadoras, os preços observados passaram a aderir melhor ao modelo do que aderiam antes. O modelo não era uma câmera apontada para o mercado; era um motor que o empurrava. Isso é reflexividade no sentido de George Soros: o observador é participante, e a crença coletiva no modelo altera o objeto modelado.

O cometa não muda de órbita porque o astrônomo publicou.
O mercado muda.

> **Nota brasileira: o target forward de 2008.** No segundo semestre de 2008, dezenas de exportadoras brasileiras carregavam estruturas de derivativos cambiais com payoff assimétrico — ganho limitado se o dólar caísse, perda alavancada e sem trava se ele disparasse. Enquanto o real se valorizava, a estrutura parecia hedge barato. Quando o dólar subiu, virou outra coisa. A Aracruz Celulose comunicou perda de US$ 2,13 bilhões ao desmontar as posições em novembro; a Sadia perdeu R$ 2,55 bilhões e acabou incorporada pela Perdigão, o que deu origem à BRF. Estima-se que o volume total dessas operações no país tenha chegado a US$ 35 bilhões. A precificação estava errada? Não necessariamente. O que estava errado era chamar aquilo de hedge — e o cenário em que a premissa de câmbio comportado valia.

---

## 4. LTCM: quando dois Nobéis descobrem que o mundo não satisfaz as equações

Se existe um caso que precisa ser contado a todo analista júnior, é esse.

O Long-Term Capital Management foi fundado em 1994 por John Meriwether, ex-chefe da mesa de arbitragem da Salomon Brothers. Entre os sócios estavam **Myron Scholes e Robert Merton**, que em 1997, com o fundo em operação, receberiam o Nobel de Economia justamente pelo trabalho de precificação de derivativos.

O conselho reunia provavelmente a maior concentração de capital intelectual quantitativo já montada num único fundo.

A estratégia central era _convergence trade_. O exemplo canônico: títulos do Tesouro americano recém-emitidos (_on-the-run_) são mais líquidos e negociam com prêmio sobre títulos antigos de vencimento praticamente idêntico (_off-the-run_).

Mesmo risco de crédito, preços diferentes. O modelo dizia que a diferença tenderia a se fechar. Vende o caro, compra o barato, espera.

O problema é que essas diferenças são medidas em pontos-base. Para transformar centavos em bilhões, é preciso alavancagem.

Muita alavancagem.

No fim de 1997, confiante nas próprias métricas, o fundo **devolveu US$ 2,7 bilhões aos investidores** por não encontrar oportunidades suficientes, mantendo o tamanho da carteira. O efeito foi mecânico: menos capital, mesmo risco, alavancagem maior.

No início de 1998 o LTCM operava com cerca de US$ 4,7 bilhões de patrimônio, aproximadamente US$ 125 bilhões em ativos (algo em torno de 25:1) e um nocional de derivativos fora de balanço estimado em US$ 1,25 trilhão.

O sistema de risco era baseado em VaR e dizia, com serenidade, que a ruína era estatisticamente irrelevante. O raciocínio: as posições estavam espalhadas por dezenas de mercados pouco correlacionados; a chance de todas perderem ao mesmo tempo era desprezível.

Essa é a premissa. E ela é histórica, não estrutural. A matriz de correlação foi estimada em uma amostra e amostras descrevem os regimes que estavam nelas.

Em **17 de agosto de 1998**, a Rússia deu calote na dívida em rublos e desvalorizou a moeda. O que veio a seguir não estava no cenário: uma fuga global para qualidade e liquidez. Investidores do mundo inteiro abandonaram tudo que fosse menos líquido e correram para comprar exatamente os Treasuries _on-the-run_ — precisamente a ponta que o LTCM estava vendida.

Em vez de convergirem, os spreads divergiram. E divergiram **juntos**, em mercados que não tinham nenhuma razão econômica para se mover em bloco. A correlação, que era o alicerce do cálculo de risco, foi para perto de 1 no pior momento possível. Vale registrar como isso soa de dentro: em 2007, o então CFO do Goldman Sachs descreveria episódio semelhante como movimentos de 25 desvios-padrão acontecendo vários dias seguidos. Quando você precisa dizer uma frase dessas, o problema não é o mercado — é a distribuição que você escolheu.

Aí veio a segunda premissa quebrada, e essa é a mais cruel. Para cobrir chamadas de margem, o fundo precisou vender. Mas o LTCM era grande demais em relação aos mercados em que operava: **o próprio ato de vender empurrava os preços contra as posições que ainda restavam**. A hipótese de liquidez é a premissa mais invisível e mais letal de toda a modelagem financeira. Ela é invisível porque quase nunca aparece escrita.

O fundo perdeu cerca de US$ 4,6 bilhões em menos de quatro meses. Em 23 de setembro de 1998, sob articulação de William McDonough, então presidente do Fed de Nova York, **14 instituições financeiras aportaram cerca de US$ 3,6 bilhões** para evitar uma liquidação forçada que teria contaminado os mercados de crédito globais. O Fed não pôs dinheiro próprio: organizou a sala.

E aqui está o ponto que eu quero que fique. **Não houve erro de matemática no LTCM.** As equações estavam corretas. Os testes estatísticos estavam corretos. O que houve foi um modelo calibrado em um regime sendo operado, com alavancagem de 25 para 1, dentro de outro regime. O erro não estava na conta. Estava na fronteira entre a conta e o mundo, e essa fronteira não está escrita em lugar nenhum da planilha.

---

## 5. As duas patologias

Quando o modelo se comporta mal, o jovem analista tende a adoecer de uma entre duas formas. As duas são compreensíveis. As duas custam caro.

### O fundamentalista

O primeiro tipo defende o modelo. Diante do prejuízo, ele classifica o evento como cisne negro, outlier, "cinco desvios-padrão", anomalia irracional do mercado. A equação está imaculada; a realidade é que se comportou mal.

O detalhe perturbador é que, logicamente, **ele nunca pode ser provado errado**.
É o resultado de Duhem–Quine: como o teste atinge o conjunto todo, sempre existe um ajuste auxiliar capaz de salvar o núcleo. Imre Lakatos descreveu isso como o "cinturão protetor" de um programa de pesquisa: você recalibra a janela, troca a distribuição, adiciona um parâmetro, e o núcleo sobrevive. Fazer isso não é irracional, é assim que a ciência normal funciona.

O que separa um programa saudável de um degenerado é se os ajustes **geram previsões novas** ou apenas explicam, depois do fato, por que a última perda não conta.

O caso limite disso tem nome e data: em 2012, o Chief Investment Office do JPMorgan em Londres estourou repetidamente os limites de VaR do banco. A resposta não foi reduzir posição. Foi **trocar o modelo de VaR** por um novo, implementado com planilhas Excel e transferência manual de dados, que cortou a estimativa de perda potencial pela metade e liberou espaço para a mesa continuar aumentando a aposta.

O resultado foi o episódio conhecido como London Whale e mais de US$ 6 bilhões de prejuízo.

Quando o risco excede o limite do modelo, o cinturão protetor pode ser esticado até virar fraude regulatória.

### O niilista

O segundo tipo abandona tudo. Viu Black–Scholes errar nas caudas, viu a projeção de PIB furar feio, viu o backtest lindo virar pó no primeiro trimestre real, e concluiu que finanças quantitativas é charlatanismo com LaTeX. Passa a operar por "leitura de mercado", feeling e gráfico.

Derman comenta algo parecido sobre 2008: o fracasso de alguns modelos virou munição para um ceticismo raso, que confundiu "esse modelo falhou nessas condições" com "modelar é inútil".

Rejeitar a abstração porque ela é imperfeita é abandonar a medicina porque nenhum tratamento é infalível. O niilista troca um instrumento com margem de erro conhecida por um instrumento com margem de erro desconhecida — e chama isso de prudência. Andar com um modelo cujos limites você mapeou é estritamente melhor do que andar às cegas.

Repare que as duas patologias têm a **mesma raiz**: as duas confundem modelo com teoria. O fundamentalista porque acredita na promessa de verdade absoluta; o niilista porque acreditou nela primeiro e se sentiu traído depois.

---

## 6. A ficha técnica: como usar modelo sem virar refém dele

Em 2009, Emanuel Derman e Paul Wilmott publicaram o _Financial Modelers' Manifesto_, cujo núcleo é um "juramento de Hipócrates do modelador". Parafraseando os cinco compromissos:

1. Lembrar que **"eu não criei o mundo, e ele não satisfaz minhas equações"**;
2. Usar modelos com ousadia para estimar valor, sem se deixar impressionar demais pela matemática;
3. Nunca sacrificar realidade por elegância sem dizer explicitamente que fez isso;
4. Não dar a quem usa o modelo falso conforto sobre sua precisão — tornar premissas e omissões explícitas;
5. Reconhecer que o trabalho tem efeitos sobre a sociedade e a economia que excedem a própria compreensão.

Traduzindo para o seu dia a dia como analista: antes de entregar um número que saiu de um modelo, responda seis perguntas. Se você não souber responder três delas, você não sabe o que está entregando.

|#|Pergunta|Por que importa|
|---|---|---|
|1|Qual é a analogia? Esse modelo compara meu ativo com o quê?|Todo modelo é metáfora. Nomear a metáfora revela onde ela quebra|
|2|Quais premissas o cenário atual está violando **agora**?|Não é se viola — é quais e quanto|
|3|Em que amostra os parâmetros foram calibrados? Ela contém um regime de estresse?|Correlação e volatilidade estimadas em bonança descrevem bonança|
|4|O que acontece com o resultado se o preço saltar, em vez de andar?|Testa a hipótese de continuidade, a mais frágil no Brasil|
|5|Consigo sair da posição no tamanho em que estou, sem mover o preço?|A premissa de liquidez, que matou o LTCM e quase nunca está escrita|
|6|Se o resultado vier errado, como eu vou saber que foi o modelo — e não a calibração, o dado ou o mundo?|Duhem–Quine na prática: definir o critério **antes** de precisar dele|

---

## Fechamento

Nenhum modelo é uma bala de prata.

Não porque a matemática seja fraca, mas porque em finanças não existem teorias no sentido forte: existem analogias projetadas sobre um sistema feito de gente que reage ao próprio modelo. Esperar que uma equação capture isso integralmente é um erro de categoria, não de cálculo.

Mas modelos são alavancas extremamente eficientes.

Uma alavanca não decide nada por você e não sabe nada sobre o mundo — ela apenas multiplica a força que você aplica. Ela multiplica competência tanto quanto multiplica burrice, e com a mesma indiferença. O LTCM não quebrou por usar modelos; quebrou por aplicar 25 vezes de alavancagem sobre uma premissa histórica tratada como lei natural.

O que eu proponho ao analista que está começando é uma relação desapegada, não uma relação cética. Estude estocástico a sério. Aprenda a derivar Black–Scholes, não a decorá-la. E depois trate o resultado como o que ele é: uma estimativa condicionada a premissas que você consegue listar, com um domínio de validade que você consegue descrever, e uma fronteira além da qual o número que aparece na tela não significa mais nada.

Um modelo é uma ferramenta que não sabe que é uma ferramenta. Cabe a você saber.

---

### Fontes e leituras

- Peter Kempthorne et al., _18.S096 Topics in Mathematics with Applications in Finance_, MIT OpenCourseWare, Fall 2013 — [ocw.mit.edu](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/) (versão atualizada: 18.642, Fall 2024)
- Emanuel Derman, _Models. Behaving. Badly._ (2011)
- Emanuel Derman & Paul Wilmott, _The Financial Modelers' Manifesto_ (2009)
- Donald MacKenzie, _An Engine, Not a Camera: How Financial Models Shape Markets_ (2006)
- Nancy Cartwright, _How the Laws of Physics Lie_ (1983); Imre Lakatos, _Falsification and the Methodology of Scientific Research Programmes_ (1970)
- Roger Lowenstein, _When Genius Failed_ (2000); Federal Reserve History, _Near Failure of Long-Term Capital Management_ — [federalreservehistory.org](https://www.federalreservehistory.org/essays/ltcm-near-failure)
- President's Working Group on Financial Markets, _Hedge Funds, Leverage, and the Lessons of Long-Term Capital Management_ (1999)
- US Senate PSI, _JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses_ (2013)
- Joesley Day: InfoMoney e Seu Dinheiro, pregão de 18/05/2017
- Aracruz e Sadia: fatos relevantes de 2008; Revista RACEF, _A crise financeira internacional (2008) e o efeito dos derivativos cambiais_

---

_Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira. Decisões de investimento são de responsabilidade exclusiva do leitor._

---

## Marcadores extraídos do rascunho

| Marcador (verbatim) | Local no rascunho | Classificação | Resolução |
|---|---|---|---|
| `[LINHA EDITORIAL: Spoiler]` | Topo do arquivo, antes do título de apoio | Estrutural | *(preenchida na etapa 1)* |
| `[CAPA: Como ideia para criativo de capa, podemos utilizar algo como uma rebelia de máquinas humanoides como nos filmes de Terminator]` | Topo do arquivo, logo após a linha editorial | Sugestão de visual | *(preenchida na etapa 8)* |
| `[escrever um breve prágrafo sobre o que é o modelo e pq ele é tao famoso.]` | Seção 3, antes da lista de premissas de Black–Scholes | Instrução de escrita | *(preenchida na etapa 4)* |
| `[tentar reescrever o parágrafo acima. Existem teorias em financas.]` | Seção "Fechamento", logo após o primeiro parágrafo | Instrução de escrita | *(preenchida na etapa 4)* |
