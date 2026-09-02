# Quando os Modelos se Rebelam

### Por que o descolamento entre modelo e realidade é esperado — e por que entender isso separa um bom modelador de um extremista frustrado

Vez ou outra compartilho aqui conteúdo de aulas do MIT OpenCourseWare (o repositório de aulas
e cursos que o MIT disponibiliza gratuitamente). Eles mantêm uma quantidade enorme de
material.

Entre esses materiais está a disciplina 'Topics in Mathematics with Applications in Finance'
(18.S096, na versão de 2013, atualizada como 18.642 em 2024). A disciplina é um passeio, a
passo rápido, por uma série de ferramentas e modelos matemáticos fundamentais em finanças.

Um dos meus momentos favoritos do curso é a aula de probabilidade. Nela, um dos professores
diz, numa explicação sobre a ideia de retorno à média:

> "Se você lança uma moeda 100 vezes, obtendo cara em todos os lançamentos, você deveria
> estar considerando seriamente a possibilidade de que essa moeda tenha algum vício ou
> defeito." [VERIFICAR: a atribuição desta fala a Peter Kempthorne não se sustentou na
> pesquisa desta rodada — a página oficial de recursos do MIT OCW para esta aula específica
> (Lecture 3, Probability Theory, 18.S096) lista Choongbum Lee como instrutor, não Kempthorne.
> Confirmar assistindo ao vídeo da aula antes de publicar; se não for possível confirmar,
> remover o nome e manter só "um dos professores do curso".]

A frase é dita no contexto de que muitas pessoas começam a esperar o retorno à média, mas
acabam se esquecendo de que a própria média pode ter mudado.

Esse tipo de pensamento equivocado — bastante presente quando o problema envolve
probabilidades — é sintoma de uma compreensão parcial, ou mesmo equivocada, do funcionamento
de modelos.

Uma má compreensão do que são modelos, de como funcionam e da importância das hipóteses que os
fundamentam pode ser a diferença entre ser um modelador bem-sucedido ou se tornar um
extremista frustrado diante de modelos.

No texto de hoje vou tratar dessas ideias e mostrar como o desacoplamento entre modelo e
realidade pode levar até vencedores do Prêmio Nobel ao desastre.

## Três palavras que você usa como sinônimo e não são

Emanuel Derman é uma figura útil aqui porque conhece os dois lados da história: doutor em
física teórica de partículas, foi para a Goldman Sachs e virou um dos nomes centrais da
engenharia financeira, coautor do modelo de volatilidade local Derman–Kani.

Em 'Models. Behaving. Badly.' (2011), ele propõe uma separação que vale a pena levar a sério:
'teoria', 'modelo' e 'intuição' são três coisas diferentes.

'Teoria' é a tentativa de descrever o que uma coisa é. Uma teoria bem-sucedida se torna
indistinguível do fenômeno — as equações de Maxwell não se parecem com o eletromagnetismo;
dentro da física clássica, elas são o eletromagnetismo. Teorias pedem confirmação empírica,
mas não pedem justificativa: não faz sentido perguntar por que você escolheu comparar a luz
com uma onda eletromagnética.

'Modelo' é a tentativa de descrever com o que uma coisa se parece. Um modelo se apoia sempre
em terreno emprestado: é uma analogia, uma metáfora que compara o objeto de estudo a outra
coisa cuja dinâmica você já sabe manipular. Black–Scholes trata o preço de uma ação como
fumaça se difundindo numa sala. A semelhança é sempre parcial, e por isso todo modelo exige
justificativa — você precisa defender por que a analogia se sustenta neste caso.

'Intuição' é o terceiro termo, e é o mais fácil de descartar como misticismo — o que seria um
erro. Na acepção de Derman, intuição não é palpite: é o resultado da imersão prolongada num
domínio, o ponto em que você para de operar a ferramenta e passa a pensar através dela. É o
que permite a um gestor de risco olhar para um número que saiu do sistema e dizer 'esse número
está errado' antes de conseguir explicar por quê.

Em finanças, o que existe são modelos. Não teorias. CAPM (modelo de precificação de ativos de
capital), Black–Scholes, Hipótese dos Mercados Eficientes, Vasicek, Gordon: todos imitam o
estilo da física e usam a sintaxe da matemática, mas não têm a mesma ancoragem ontológica —
ou seja, não descrevem o que a coisa é, só com o que ela se parece.

*[graf-01: comparativo Teoria x Modelo — o que faz, fundamento, se exige justificativa,
quando falha, reflexividade. Ver `02-estrutura.md`: mantido como tabela nativa, não vira
peça visual — a comparação de conceitos abstratos não tem objeto concreto por trás.]*

### E onde entram as "hipóteses"?

Aqui mora uma armadilha específica da nossa língua. Em inglês existem duas palavras:
'hypothesis' (conjectura testável, que a metodologia científica manda você tentar falsear) e
'assumption' (premissa, condição de contorno assumida como verdadeira para a construção seguir
de pé).

Em português, as duas viram hipótese.

O resultado é que o aluno aprende "as hipóteses do modelo de Black–Scholes" e as coloca
mentalmente na mesma caixa de hipótese nula — formalidade de demonstração, coisa que aparece
no slide antes da fórmula e depois some. Não é isso. As hipóteses de Black–Scholes não são
conjecturas a testar: são a bula do remédio. Elas definem o domínio de validade do
instrumento. Ignorá-las não é imprecisão acadêmica, é usar o aparelho fora da faixa de
operação.

O leitor mais rigoroso pode se perguntar: essa taxonomia é rigorosa ou é a licença poética de
um físico que virou banqueiro? A resposta honesta é: bate em parte.

Modelos serem representações parciais e deliberadamente distorcidas tem convergência forte com
a filosofia da ciência — Nancy Cartwright argumenta, em 'How the Laws of Physics Lie' (1983),
que até as leis fundamentais só são literalmente verdadeiras sobre modelos idealizados; George
Box resumiu isso na frase que virou clichê: todos os modelos estão errados, alguns são úteis.
Já a ideia de que "modelo falha, logo a analogia deixou de servir" é mais complicada do que
parece: quando uma predição falha, o teste atinge o conjunto inteiro — núcleo, premissas
auxiliares, calibração, dados —, e você nunca consegue isolar logicamente o culpado sozinho
(é o chamado problema de Duhem–Quine). E a ideia de que teoria é categoricamente distinta de
modelo tem discordância real: na visão semântica das teorias (Suppes, van Fraassen, Giere),
teorias também são famílias de modelos — as equações de Maxwell idealizam vácuo perfeito,
cargas pontuais, meios homogêneos, do mesmo jeito que qualquer modelo financeiro idealiza.

Minha leitura: trate a distinção como uma ferramenta de ancoragem, não como uma parede. De um
lado, construções que sobrevivem a testes de falseamento cada vez mais severos e cujo objeto
não reage a elas. Do outro, construções cujo objeto é feito de gente que lê o próprio modelo.
Finanças mora firmemente do lado direito, e Derman está certo no que importa: tratar a segunda
coisa como se fosse a primeira é a origem do problema.

## O radar da rodovia

Um exemplo fora de finanças ajuda, porque nele ninguém tem viés comportamental.

Pense num radar de solo. Ele mede o tempo que o veículo leva para cruzar um intervalo mínimo
entre dois sensores e reporta a velocidade média nesse intervalo. Depois trata esse número
como se fosse a velocidade instantânea.

*[ilu-01: a metáfora do radar na rodovia — carro cruzando dois sensores, a velocidade média
tratada como se fosse instantânea. Ver `08-briefing-visual.md`.]*

Matematicamente, isso é uma troca: velocidade média por velocidade instantânea. A troca só é
válida porque o movimento é contínuo e suave. A inércia garante que o carro não teleporta de
10 km/h para 100 km/h — ele precisa passar por 40, 60 e 80 no caminho. Sob essa premissa, a
aproximação é excelente e o radar funciona muito bem.

Agora quebre a premissa. Imagine que a aceleração pudesse dar um salto instantâneo, sem
percorrer os valores intermediários. O radar continuaria calculando corretamente e continuaria
entregando um número sem sentido. A matemática seguiria perfeita; o cenário é que teria
mudado.

Guarde essa frase, porque ela descreve praticamente todo desastre de modelo que você vai ver
na sua carreira.

Quase nunca a conta está errada.

O que está errado é o contexto em que a conta foi aplicada.

## Black–Scholes: o que está na bula

Black–Scholes é o caso clássico, porque a bula é longa e quase ninguém lê até o fim.

O modelo, publicado por Fischer Black e Myron Scholes em 1973 (com contribuição decisiva de
Robert Merton), resolve um problema que até então não tinha resposta fechada: quanto vale uma
opção — o direito, não a obrigação, de comprar ou vender um ativo por um preço fixado no
futuro. Antes dele, precificar opção era arte de mesa, negociada por sensação. Depois dele,
virou fórmula que cabe numa calculadora, e é por isso que se espalhou tão rápido a ponto de
Scholes e Merton receberem o Nobel de Economia em 1997 por esse mesmo trabalho — Black já
tinha morrido dois anos antes, e o prêmio não é concedido postumamente.

O modelo assume, entre outras coisas, que o preço do ativo segue um movimento browniano
geométrico — trajetórias contínuas, sem saltos —, que a volatilidade é constante ao longo da
vida da opção, que a taxa livre de risco é constante e conhecida, que não há custo de
transação nem imposto, que é possível negociar e rebalancear o hedge (a posição que anula o
risco) em tempo contínuo, e que a liquidez é ilimitada, com venda a descoberto livre e ativos
infinitamente divisíveis.

Repare que as hipóteses de continuidade, rebalanceamento contínuo e liquidez ilimitada são, na
prática, uma coisa só: a possibilidade de o vendedor da opção se ajustar continuamente
enquanto o mundo se move. É daí que sai o argumento de não-arbitragem, e é daí que sai o
preço.

E é exatamente essa a premissa que o mercado brasileiro adora quebrar.

18 de maio de 2017. Na noite anterior vaza a gravação entre Joesley Batista e o então
presidente Michel Temer. Na abertura, o Ibovespa cai o suficiente para acionar um circuit
breaker (mecanismo que suspende o pregão por alguns minutos quando a queda passa de um limite);
a queda intradiária e o fechamento do dia, e a alta do dólar no mesmo pregão, entram como
'[graf-01]' [VERIFICAR: valores exatos de fechamento do Ibovespa (B3) e PTAX (Banco Central)
para 17 e 18/05/2017 — a pesquisa desta rodada achou pequena divergência entre fontes de
imprensa (dólar fechando em R$3,38 ou R$3,3890) e recomenda puxar a série oficial em vez da
imprensa antes de publicar o gráfico].

Pergunte a quem estava vendido em opções naquela manhã quantas vezes conseguiu rebalancear o
delta (a sensibilidade do preço da opção ao preço do ativo) entre o fechamento do dia 17 e a
abertura do dia 18. A resposta é zero. Não porque o operador foi lento, mas porque não existiu
preço no meio do caminho. O modelo pressupõe um filme; o que aconteceu foi um corte do editor.

O mercado, aliás, já tinha admitido isso muito antes. Depois do crash de outubro de 1987, a
superfície de volatilidade implícita deixou de ser plana e passou a exibir o famoso 'smile'
(ou 'skew').

Em português direto: os preços praticados passaram a embutir, permanentemente, uma
probabilidade de salto maior do que a que o modelo comporta. O smile é a cicatriz da hipótese
de continuidade — o mercado usa a fórmula de Black–Scholes como linguagem de cotação e ajusta
a premissa por fora, mexendo no input de volatilidade.

E há um detalhe que o sociólogo Donald MacKenzie explora bem em 'An Engine, Not a Camera'
(2006): Black–Scholes não apenas descreveu o mercado de opções, ele o transformou.

Depois de 1973, com a fórmula difundida em tabelas e calculadoras, os preços observados
passaram a aderir melhor ao modelo do que aderiam antes. O modelo não era uma câmera apontada
para o mercado; era um motor que o empurrava. Isso é reflexividade no sentido de George Soros:
o observador é participante, e a crença coletiva no modelo altera o objeto modelado.

O cometa não muda de órbita porque o astrônomo publicou.
O mercado muda.

No segundo semestre de 2008, dezenas de exportadoras brasileiras carregavam estruturas de
derivativos cambiais chamadas 'target forward', com payoff (o resultado financeiro final)
assimétrico: ganho limitado se o dólar caísse, perda alavancada e sem trava se ele disparasse.
Enquanto o real se valorizava, a estrutura parecia hedge (proteção) barato. Quando o dólar
subiu, virou outra coisa. A Aracruz Celulose e a Sadia figuram entre os casos mais citados
dessas perdas, a Sadia acabou incorporada pela Perdigão — o que deu origem à BRF — e o volume
total dessas operações no país é estimado na casa de dezenas de bilhões de dólares [VERIFICAR:
os valores específicos de prejuízo da Aracruz e da Sadia, e o volume total de mercado
(~US$35bi), variam entre fontes e precisam de confirmação contra fato relevante/fonte
regulatória antes de publicar — ver `03-pesquisa.md`]. A precificação estava errada? Não
necessariamente. O que estava errado era chamar aquilo de hedge — e o cenário em que a
premissa de câmbio comportado valia.

## LTCM: quando dois Nobéis descobrem que o mundo não satisfaz as equações

Se existe um caso que precisa ser contado a todo analista júnior, é esse.

O Long-Term Capital Management foi fundado em 1994 por John Meriwether, ex-chefe da mesa de
arbitragem da Salomon Brothers. Entre os sócios estavam Myron Scholes e Robert Merton, que em
1997, com o fundo em operação, receberiam o Nobel de Economia justamente pelo trabalho de
precificação de derivativos. O conselho reunia provavelmente a maior concentração de capital
intelectual quantitativo já montada num único fundo.

A estratégia central era 'convergence trade' (aposta de que dois preços parecidos convergem).
O exemplo canônico: títulos do Tesouro americano recém-emitidos ('on-the-run') são mais
líquidos e negociam com prêmio sobre títulos antigos de vencimento praticamente idêntico
('off-the-run'). Mesmo risco de crédito, preços diferentes. O modelo dizia que a diferença
tenderia a se fechar. Vende o caro, compra o barato, espera.

O problema é que essas diferenças são medidas em pontos-base. Para transformar centavos em
bilhões, é preciso alavancagem. Muita alavancagem.

*[diag-01: ciclo do colapso do LTCM — calote russo → fuga para qualidade → spreads divergem
em vez de convergir → chamada de margem → venda forçada → preços pioram contra as posições
que restam. Ver `08-briefing-visual.md` e `03-pesquisa.md` para os números de anotação.]*

No fim de 1997, confiante nas próprias métricas, o fundo devolveu bilhões de dólares aos
investidores por não encontrar oportunidades suficientes, mantendo o tamanho da carteira. O
efeito foi mecânico: menos capital, mesmo risco, alavancagem maior. No início de 1998 o LTCM
operava com um patrimônio de cerca de US$4,7 bilhões contra mais de US$125 bilhões em ativos —
alavancagem superior a 25 para 1 [VERIFICAR: fontes divergem entre ~25:1 e ~30:1 conforme a
data de corte do patrimônio usada — ver `03-pesquisa.md`] — e um nocional de derivativos fora
de balanço estimado em mais de um trilhão de dólares [VERIFICAR: o valor específico de
US$1,25 trilhão não foi confirmado contra fonte primária nesta rodada].

O sistema de risco era baseado em VaR (valor em risco: uma estimativa estatística da perda
máxima esperada num horizonte de tempo, com certa probabilidade) e dizia, com serenidade, que
a ruína era estatisticamente irrelevante. O raciocínio: as posições estavam espalhadas por
dezenas de mercados pouco correlacionados; a chance de todas perderem ao mesmo tempo era
desprezível.

Essa é a premissa. E ela é histórica, não estrutural. A matriz de correlação foi estimada em
uma amostra, e amostras descrevem os regimes que estavam nelas.

Em 17 de agosto de 1998, a Rússia deu calote na dívida em rublos e desvalorizou a moeda. O que
veio a seguir não estava no cenário: uma fuga global para qualidade e liquidez. Investidores do
mundo inteiro abandonaram tudo que fosse menos líquido e correram para comprar exatamente os
Treasuries on-the-run — precisamente a ponta que o LTCM estava vendida.

Em vez de convergirem, os spreads divergiram. E divergiram juntos, em mercados que não tinham
nenhuma razão econômica para se mover em bloco. A correlação, que era o alicerce do cálculo de
risco, foi para perto de 1 no pior momento possível. Vale registrar como isso soa de dentro:
em 2007, o então CFO do Goldman Sachs descreveria um episódio semelhante (não o LTCM — um caso
posterior e análogo, com dois fundos quantitativos do próprio banco) como movimentos de 25
desvios-padrão acontecendo vários dias seguidos. Quando você precisa dizer uma frase dessas, o
problema não é o mercado, é a distribuição que você escolheu.

Aí veio a segunda premissa quebrada, e essa é a mais cruel. Para cobrir chamadas de margem, o
fundo precisou vender. Mas o LTCM era grande demais em relação aos mercados em que operava: o
próprio ato de vender empurrava os preços contra as posições que ainda restavam. A hipótese de
liquidez é a premissa mais invisível e mais letal de toda a modelagem financeira. Ela é
invisível porque quase nunca aparece escrita.

O fundo perdeu cerca de US$4,6 bilhões em menos de quatro meses. Em 23 de setembro de 1998,
sob articulação de William McDonough, então presidente do Fed de Nova York, catorze
instituições financeiras aportaram cerca de US$3,6 bilhões para evitar uma liquidação forçada
que teria contaminado os mercados de crédito globais. O Fed não pôs dinheiro próprio: organizou
a sala.

E aqui está o ponto que eu quero que fique. Não houve erro de matemática no LTCM. As equações
estavam corretas. Os testes estatísticos estavam corretos. O que houve foi um modelo calibrado
num regime sendo operado, com alavancagem de mais de 25 para 1, dentro de outro regime. O erro
não estava na conta. Estava na fronteira entre a conta e o mundo, e essa fronteira não está
escrita em lugar nenhum da planilha.

Vale uma ressalva que o próprio caso convida a fazer, e que eu não quero que passe batido:
alavancar 25 vezes não é uma consequência do modelo, é uma escolha de quem opera o modelo.
Nada na premissa de liquidez obrigava os sócios do LTCM a apostar naquele tamanho — a decisão
de alavancagem foi discricionária, humana, sobre uma correlação estimada historicamente.
Chamar o desastre de "a matemática estava certa, a premissa é que quebrou" é verdade, mas é
também uma forma elegante de tirar a responsabilidade de cima de quem decidiu o tamanho da
aposta.

## As duas patologias

Quando o modelo se comporta mal, o jovem analista tende a adoecer de uma entre duas formas. As
duas são compreensíveis. As duas custam caro.

### O fundamentalista

O primeiro tipo defende o modelo. Diante do prejuízo, ele classifica o evento como cisne
negro, outlier, "cinco desvios-padrão", anomalia irracional do mercado. A equação está
imaculada; a realidade é que se comportou mal.

O detalhe perturbador é que, logicamente, ele nunca pode ser provado errado. É o resultado do
problema de Duhem–Quine: como o teste atinge o conjunto todo, sempre existe um ajuste auxiliar
capaz de salvar o núcleo. O filósofo Imre Lakatos descreveu isso como o "cinturão protetor" de
um programa de pesquisa — você recalibra a janela, troca a distribuição, adiciona um
parâmetro, e o núcleo sobrevive. Fazer isso não é irracional; é assim que a ciência normal
funciona.

O que separa um programa saudável de um degenerado é se os ajustes geram previsões novas ou
apenas explicam, depois do fato, por que a última perda não conta.

O caso limite disso tem nome e data: em 2012, o Chief Investment Office (a mesa que gerencia
os ativos e riscos do próprio banco) do JPMorgan em Londres estourou repetidamente os limites
de VaR do banco. A resposta não foi reduzir posição. Foi trocar o modelo de VaR por um novo,
implementado com planilhas Excel e transferência manual de dados, que cortou a estimativa de
perda potencial pela metade e liberou espaço para a mesa continuar aumentando a aposta.

O resultado foi o episódio conhecido como London Whale e mais de US$6 bilhões de prejuízo.

Quando o risco excede o limite do modelo, o cinturão protetor pode ser esticado até virar
fraude regulatória.

### O niilista

O segundo tipo abandona tudo. Viu Black–Scholes errar nas caudas, viu a projeção de PIB furar
feio, viu o backtest (teste retrospectivo de uma estratégia contra dados históricos) lindo
virar pó no primeiro trimestre real, e concluiu que finanças quantitativas é charlatanismo com
LaTeX. Passa a operar por leitura de mercado, feeling e gráfico.

Derman comenta algo parecido sobre 2008: o fracasso de alguns modelos virou munição para um
ceticismo raso, que confundiu "esse modelo falhou nessas condições" com "modelar é inútil".

Rejeitar a abstração porque ela é imperfeita é abandonar a medicina porque nenhum tratamento é
infalível. O niilista troca um instrumento com margem de erro conhecida por um instrumento com
margem de erro desconhecida — e chama isso de prudência. Andar com um modelo cujos limites
você mapeou é estritamente melhor do que andar às cegas.

Repare que as duas patologias têm a mesma raiz: as duas confundem modelo com teoria. O
fundamentalista porque acredita na promessa de verdade absoluta; o niilista porque acreditou
nela primeiro e se sentiu traído depois.

## A ficha técnica: como usar modelo sem virar refém dele

Em 2009, Emanuel Derman e Paul Wilmott publicaram o 'Financial Modelers' Manifesto', cujo
núcleo é um juramento de Hipócrates do modelador. Parafraseando os compromissos: lembrar que
você não criou o mundo, e ele não satisfaz suas equações; usar modelos com ousadia para
estimar valor, sem se deixar impressionar demais pela matemática; nunca sacrificar realidade
por elegância sem dizer explicitamente que fez isso; não dar a quem usa o modelo falso
conforto sobre sua precisão, tornando premissas e omissões explícitas; e reconhecer que o
trabalho tem efeitos sobre a sociedade e a economia que excedem a própria compreensão
[VERIFICAR: paráfrase dos cinco compromissos do manifesto original — não foi possível extrair
o texto exato do PDF fonte nesta rodada de pesquisa, conferir contra o documento antes de
publicar].

Traduzindo para o seu dia a dia como analista: antes de entregar um número que saiu de um
modelo, responda seis perguntas. Se você não souber responder três delas, você não sabe o que
está entregando.

1. Qual é a analogia? Esse modelo compara meu ativo com o quê? — todo modelo é metáfora;
   nomear a metáfora revela onde ela quebra.
2. Quais premissas o cenário atual está violando agora? — não é se viola, é quais e quanto.
3. Em que amostra os parâmetros foram calibrados? Ela contém um regime de estresse? —
   correlação e volatilidade estimadas em bonança descrevem bonança.
4. O que acontece com o resultado se o preço saltar, em vez de andar? — testa a hipótese de
   continuidade, a mais frágil no Brasil.
5. Consigo sair da posição no tamanho em que estou, sem mover o preço? — a premissa de
   liquidez, que matou o LTCM e quase nunca está escrita.
6. Se o resultado vier errado, como eu vou saber que foi o modelo, e não a calibração, o dado
   ou o mundo? — o problema de Duhem–Quine na prática: definir o critério antes de precisar
   dele.

## Fechamento

Nenhum modelo é uma bala de prata.

Isso não significa que finanças não tenham nenhuma teoria — existem, sim, resultados que
funcionam como teoria dentro de seu próprio domínio fechado (a ausência de arbitragem, por
exemplo, é quase axiomática). O que não existe é uma teoria no sentido forte que descreva o
mercado inteiro como as equações de Maxwell descrevem o eletromagnetismo: o que existem, na
imensa maioria dos casos, são analogias projetadas sobre um sistema feito de gente que reage
ao próprio modelo. Esperar que uma equação capture isso integralmente é um erro de categoria,
não de cálculo.

Mas modelos são alavancas extremamente eficientes.

Uma alavanca não decide nada por você e não sabe nada sobre o mundo — ela apenas multiplica a
força que você aplica. Ela multiplica competência tanto quanto multiplica burrice, e com a
mesma indiferença. O LTCM não quebrou por usar modelos; quebrou por aplicar 25 vezes de
alavancagem sobre uma premissa histórica tratada como lei natural.

O que eu proponho ao analista que está começando é uma relação desapegada, não uma relação
cética. Estude estocástico a sério. Aprenda a derivar Black–Scholes, não a decorá-la. E depois
trate o resultado como o que ele é: uma estimativa condicionada a premissas que você consegue
listar, com um domínio de validade que você consegue descrever, e uma fronteira além da qual o
número que aparece na tela não significa mais nada.

Um modelo é uma ferramenta que não sabe que é uma ferramenta. Cabe a você saber.

---

### Fontes e leituras

- Peter Kempthorne et al., '18.S096 Topics in Mathematics with Applications in Finance', MIT
  OpenCourseWare, Fall 2013 (versão atualizada: 18.642, Fall 2024)
- Emanuel Derman, 'Models. Behaving. Badly.' (2011)
- Emanuel Derman & Paul Wilmott, 'The Financial Modelers' Manifesto' (2009)
- Donald MacKenzie, 'An Engine, Not a Camera: How Financial Models Shape Markets' (2006)
- Nancy Cartwright, 'How the Laws of Physics Lie' (1983); Imre Lakatos, 'Falsification and the
  Methodology of Scientific Research Programmes' (1970)
- Roger Lowenstein, 'When Genius Failed' (2000); Federal Reserve History, 'Near Failure of
  Long-Term Capital Management'
- President's Working Group on Financial Markets, 'Hedge Funds, Leverage, and the Lessons of
  Long-Term Capital Management' (1999)
- US Senate PSI, 'JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses'
  (2013)
- Imprensa financeira brasileira sobre o pregão de 18/05/2017; fatos relevantes de 2008 sobre
  Aracruz e Sadia; Revista RACEF, 'A crise financeira internacional (2008) e o efeito dos
  derivativos cambiais'

---

## Notas de processo (não vão para o post final)

- **Marcadores resolvidos nesta etapa** (ver `00-transcricao.md`): o parágrafo-definição de
  Black–Scholes foi escrito na seção correspondente; o parágrafo do fechamento foi reescrito
  para reconhecer, sem contradizer a tese central, que "teoria" também existe em domínios
  restritos de finanças — ecoando a nuance já registrada na seção 1 (visão semântica de
  Suppes/van Fraassen/Giere), em vez de reafirmar a frase categórica original do rascunho.
- **Bold de ênfase do rascunho original convertido para aspas simples ou removido**, por
  `estilo-autoral.md` regra 4. Jargão (circuit breaker, delta, hedge, payoff, VaR, backtest,
  Chief Investment Office, convergence trade, on-the-run/off-the-run) recebeu gloss na
  primeira ocorrência, por regra 1.
- **`[VERIFICAR]` inseridos inline** nos quatro pontos que a pesquisa (etapa 3) marcou como
  arriscados: citação de Kempthorne, números do target forward 2008, alavancagem/nocional do
  LTCM, e paráfrase do Financial Modelers' Manifesto. Os números do Ibovespa/dólar em
  18/05/2017 ficaram referenciados ao placeholder `graf-01` com `[VERIFICAR]` de fonte
  oficial, em vez de arredondados de imprensa — decisão de não afirmar percentual solto no
  corpo do texto até a etapa 7 confirmar.
- **Movimento aspiracional de Michael Lewis (item 3, `estilo-autoral.md` §5)** aplicado na
  ressalva sobre a alavancagem do LTCM ser decisão humana, não decorrência do modelo — ponto
  de pesquisa (etapa 3, ausente do rascunho original) incorporado ao argumento em vez de só
  registrado como observação de pesquisa.
- Ainda sem CTA de compartilhamento explícito — mantém o padrão de fechamento ensaístico com
  aforismo, como o próprio rascunho já indicava.
