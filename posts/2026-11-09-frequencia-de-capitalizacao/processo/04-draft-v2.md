# Etapa 4 — Draft v2

Reentrada na etapa 4 depois da crítica (etapa 5), com as decisões do autor sobre os achados. Base:
`04-draft-v1.md`. Mudanças só de ligação, sem reordenar seções. Números novos em cálculo próprio
(Python), a conferir na etapa 7.

## Notas laterais: o que mudou e por quê

| # | Achado | Onde | Mudança | Origem |
|---|---|---|---|---|
| 1 | M1 | Abertura | A pergunta-âncora passa a apontar para o porquê do teto. "O texto anterior adiantou que, a 14%, ele nunca passa de 15,03%. Mas por que existe um teto (…)? E de onde vem esse número?" | Autor: aplicar M1, M2, M4, M7 |
| 2 | M5 | De onde vem o e | A hipótese ganha consequência: é a hipótese do composto do texto anterior, com outro intervalo. "Mesma hipótese, mesmo motor." | Autor: ligar à tese |
| 3 | M4 | De onde vem o e; Mesma curva | "É o motor contínuo." → "É a capitalização contínua."; "uma curva do motor contínuo" → "uma curva de capitalização contínua". Entra a frase-mapa: dois motores (linear e composto) e três etiquetas do composto (efetiva, nominal, contínua). "Motor contínuo" não aparece mais | Autor |
| 4 | M2 | Mesma curva | Parágrafo que fecha a promessa da abertura: "É isso que faz do du/252 desta série um caso particular (…)" | Autor |
| 5 | B1 | Mesma curva | "É uma identidade, e por isso nenhuma das duas etiquetas é mais precisa que a outra." Liga a refutação ao "mais preciso" do mito | Orquestrador (baixo, redação) |
| 6 | M6 | Rende todo dia | Três frases com o rotativo do cartão: 451,7% a.a. (set/2026, BC), cerca de 15,3% a.m.; diário 522,6%; contínuo 526,7%; "até o último degrau da escada vale mais de quatro pontos percentuais". Também "Se a taxa é de cartão, não pode." no bloco de decisão | Autor: sim; `03-pesquisa.md` contraponto 2 |
| 7 | B4 | Mesa de opções | "As duas primeiras, o texto anterior já adiantou:" (remissão) | Orquestrador (baixo) |
| 8 | M7 | Onde mora o erro | "Lados do balcão" → passagem interna ("Dentro da mesma instituição…"), e "Quem paga fica do outro lado do balcão". Depois dos números: quem compra a call paga R$ 0,52 a mais por ação, quem vende a put recebe R$ 0,26 a menos. "Ninguém errou a taxa. Errou a etiqueta." Não afirma que o erro é comum | Autor |
| 9 | B1 | Onde mora o erro | "Na seção anterior" → "Na escada dos 14%" | Orquestrador (baixo) |
| 10 | M8 | Prateleira | A LTN fica e ganha a ligação: "Para comparar dois CDBs, meio ponto-base some. Para replicar um preço, não: a 14%, meio ponto-base muda o preço de uma LTN de um ano em quase R$ 0,04 (…)" | Autor: manter a LTN e ligar |

**Não aplicado:** M3 (o deck com a tese) vai ao gate com o subtítulo. B6 (Súmula 541) foi
descartado pelo autor, que manteve a LTN. B2, B3, B5, B7–B10 ficam como observação.

**Números novos (cálculo próprio, etapa 7 confere):** (1 + 4,517)^(1/12) − 1 = 15,29% a.m.;
nominal 183,53%; diária (1 + 1,8353/252)^252 − 1 = 522,57%; contínua e^1,8353 − 1 = 526,73%;
diferença 4,15 pp. Call 17,24 − 16,72 = 0,52; put 4,44 − 4,18 = 0,26. LTN de 252 du: 1.000/1,14 −
1.000/1,14005 = R$ 0,0385. Teste do Tesouro (14,36%, 532 du) com a fórmula do texto:
753,315323, igual ao documento.

---

# Frequência de Capitalização

*O limite matemático que explica o composto e o contínuo*

No fim do último texto, deixei uma conta para você. Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números você de fato paga?

A resposta cabe em poucas linhas. 'Capitalizados mensalmente' quer dizer que o contrato divide os 12% por doze, dá 1% ao mês, e compõe esse 1% doze vezes. Cada real vira 1,01 elevado a 12, ou 1,1268.

Você paga os 12,68%. Os 12% são só a forma de cotar.

Agora empurre a pergunta. E se o contrato capitalizasse todo dia? E a cada segundo?

Cada corte a mais põe o juro para render mais cedo, então o rendimento sobe. O texto anterior adiantou que, a 14%, ele nunca passa de 15,03%. Mas por que existe um teto, se dá para cortar o ano em pedaços cada vez menores? E de onde vem esse número?

Em 1683, o matemático suíço Jacob Bernoulli fez essa mesma pergunta, com a taxa mais simples que existe: 100% ao ano.

A resposta dele explica duas coisas que parecem não ter relação. Por que o composto que você usa todo dia, o du/252 (dias úteis sobre 252) desta série, é só um caso particular. E por que o manual de opções da B3 faz as contas em outra taxa, que nenhum CDB jamais cotou.

## Dois motores rivais

A versão que circula é mais ou menos esta. O juro composto é o regime do mundo real: CDB (Certificado de Depósito Bancário), Tesouro, financiamento. A capitalização contínua é outro bicho, coisa de modelo e de quem precifica opções.

E, como capitaliza a cada instante, o contínuo seria o mais agressivo dos dois. Ou o mais preciso, conforme quem conta.

No texto anterior, apresentei três motores lado a lado, e uma linha avisava que o contínuo, com a taxa certa, dá o mesmo montante que o composto. Aquela linha merece um texto inteiro, porque diz mais do que parece: dois dos três motores são o mesmo.

O contínuo não compete com o composto. É o limite dele.

## Nominal, frequência, efetiva

Três nomes resolvem a conta da abertura.

A taxa nominal, j, é o número escrito no contrato. A frequência de capitalização, m, diz quantas vezes por ano o juro é incorporado ao saldo. A taxa de cada subperíodo é a proporcional, j/m, que se compõe m vezes no ano. A taxa efetiva, i, é o que de fato rendeu no fim do ano:

$$
1 + i = \left(1 + \frac{j}{m}\right)^{m}
$$

Com j = 12% e m = 12, sai a conta da abertura: 1,01 elevado a 12, 12,68%.

É a mesma embalagem da *over* ao mês do texto anterior, a taxa do dia multiplicada por 30. Linear por fora, composta por dentro: uma taxa nominal com capitalização diária.

Volte à imagem do último texto. Dentro de cada subperíodo, o juro corre em linha reta: é uma corda. Na passagem para o subperíodo seguinte, o juro vira saldo e passa a render. As cordas se emendam numa linha quebrada, e quanto maior o m, mais curtas elas ficam.

### A escada de Bernoulli

Bernoulli tomou um capital de 1 a 100% ao ano. Com uma capitalização no ano, o capital vira 2. Com duas, de 50% cada, vira 1,5 × 1,5 = 2,25. Com quatro, 2,44. Com doze, 2,61. Com 52, uma por semana, 2,69. Com 365, uma por dia, 2,7146.

Cada degrau sobe menos que o anterior. Do anual para o semestral, o capital ganha 0,25. Do diário para o capitalizado a cada hora, ganha menos de quatro milésimos.

![Gráfico: a linha quebrada de Bernoulli. Capital de 1 a 100% ao ano, de zero a um ano. Linhas quebradas com 1, 2, 4 e 12 cordas terminam em 2, 2,25, 2,44 e 2,61. Por cima delas, a curva contínua termina em 2,718. Cada linha quebrada fica abaixo da seguinte, e todas abaixo da curva.](graf-01)

Bernoulli mostrou, com o binômio de Newton, que a escada nunca passa de 3. A conta cabe em uma linha. Expandido, o fator do ano fica assim:

$$
\left(1 + \frac{1}{n}\right)^{n} = 1 + 1 + \frac{1}{2!}\left(1 - \frac{1}{n}\right) + \frac{1}{3!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) + \cdots
$$

Os parênteses são todos menores que 1, e cada fatorial cresce mais rápido que as potências de 2. A partir do terceiro termo, a soma fica abaixo de 1/2 + 1/4 + 1/8 + …, que dá 1. O total, portanto, nunca passa de 1 + 1 + 1 = 3.

E, quanto maior o n, mais perto de 1 chega cada parêntese: a escada sobe sempre, sem passar de 3. Uma escada assim tem um topo. O topo é 2,71828…, o número que Leonhard Euler, numa carta de 1731, chamaria de e.

Até aqui, é o capítulo de taxas equivalentes de qualquer livro, com uma nota histórica. O interessante começa quando se troca os 100% de Bernoulli por uma taxa qualquer.

## De onde vem o e

Troque os 100% por uma taxa nominal qualquer, j, e chame de n o quociente m/j. Então j/m = 1/n e m = n × j. O fator do ano vira a escada de Bernoulli elevada a j:

$$
\left(1 + \frac{j}{m}\right)^{m} = \left[\left(1 + \frac{1}{n}\right)^{n}\right]^{j} \;\longrightarrow\; e^{j} \qquad (m \to \infty)
$$

Para 14% nominais, o teto é e elevado a 0,14, ou 1,1503: 15,03% ao ano, o número que apareceu duas vezes no texto anterior. Para um prazo t qualquer, o montante no limite é C vezes e elevado a (j × t). É a capitalização contínua.

Há outro caminho até a mesma fórmula, e ele mostra a hipótese escondida. Se o juro é incorporado a cada instante, o saldo cresce, em cada instante, a uma velocidade proporcional a ele mesmo: a taxa vezes o saldo.

$$
\frac{dM}{dt} = j\,M \quad\Longrightarrow\quad M(t) = C\,e^{\,j\,t}
$$

O e é a base em que a curva sobe, em cada ponto, na mesma velocidade do próprio valor. Por isso ele aparece sempre que alguma coisa cresce em proporção a si mesma. A hipótese embutida é que nenhum centavo fica parado, nem por um instante, e que tudo é reinvestido à mesma taxa.

É a hipótese do composto do texto anterior, que já supunha o juro reinvestido à mesma taxa. Muda só o tamanho do intervalo em que ele volta a render. Mesma hipótese, mesmo motor.

### Mesma curva, outra etiqueta

Agora, aquela linha do texto anterior por extenso. Pegue a convenção brasileira, 14% ao ano efetivos, e reescreva o fator de um prazo qualquer:

$$
(1 + i)^{t} = e^{\,t\,\ln(1 + i)} = e^{\,r\,t}, \qquad r = \ln(1{,}14) = 13{,}10\%
$$

Não é uma aproximação. É uma identidade, e por isso nenhuma das duas etiquetas é mais precisa que a outra. A curva de um CDB prefixado a 14% ao ano, com o prazo medido em du/252, é, ponto a ponto, uma curva de capitalização contínua, com taxa de 13,10%.

É isso que faz do du/252 desta série um caso particular. O composto brasileiro é o limite de Bernoulli com outra etiqueta: taxa efetiva no lugar de r = ln(1 + i), prazo medido em dias úteis sobre 252.

O mesmo vale para as frequências do meio do caminho. As cinco taxas abaixo entregam o mesmo rendimento, 14% em um ano:

- capitalização anual: 14,000%;
- semestral: 13,542% nominais;
- mensal: 13,175% nominais;
- diária, 252 vezes no ano: 13,106% nominais;
- contínua: 13,103%.

Quanto mais vezes se capitaliza, menor precisa ser o número cotado para entregar o mesmo rendimento. Os números descem e encostam nos 13,10% da taxa contínua.

Não existe uma fronteira entre o composto e o contínuo. Existe uma escada de etiquetas para o mesmo rendimento, e o contínuo é o topo dela.

Para a série, isso muda o mapa. Ficam dois motores, o linear e o composto. O composto tem três etiquetas: a efetiva, a nominal com a sua frequência e a contínua.

A fama de 'mais agressivo' vem de comparar o mesmo número nas duas etiquetas: 14% compostos uma vez por ano contra 14% contínuos. É a conta dos 15,03% do texto anterior. O que muda é o número cotado, não o motor.

### Um aviso de vocabulário

No mercado brasileiro, 'exponencial' quase sempre quer dizer composto. A B3 chama a convenção de 252 dias úteis de 'conversão exponencial 252', e foi nesse sentido que o texto anterior falou em regime exponencial. O manual de opções da mesma B3 chama a taxa contínua de 'taxa de juro exponencial, em regime contínuo e base anual'.

As duas são exponenciais. É justamente o ponto deste texto.

## Rende todo dia não é render mais

Volte aos 14% nominais e suba com eles a escada de Bernoulli.

![Gráfico: taxa efetiva de 14% nominais ao ano conforme a frequência de capitalização. Anual, 14,00%; semestral, 14,49%; mensal, 14,93%; diária, 15,02%. Todas ficam abaixo do teto contínuo de 15,03%, marcado por uma linha tracejada. Cada degrau sobe menos que o anterior. Cálculo próprio.](graf-02)

Em R$ 1 milhão por um ano, passar da capitalização anual para a mensal vale R$ 9.342,03. Da mensal para a diária, mais R$ 887,05. Da diária para a contínua, R$ 44,72.

Cada vez que se dobra a frequência, a distância até o teto cai quase exatamente pela metade. O ganho existe, mas some rápido.

A 14%. A distância até o teto cresce com o quadrado da taxa, e há taxas no Brasil em que ela não some. O rotativo do cartão de crédito custou 451,7% ao ano em setembro de 2026, segundo o Banco Central, cerca de 15,3% ao mês. Se esses 15,3% fossem capitalizados todo dia em vez de todo mês, o ano sairia por 522,6%. No contínuo, por 526,7%. A taxas assim, até o último degrau da escada vale mais de quatro pontos percentuais.

Isso desmonta uma frase comum de propaganda: o dinheiro que 'rende todo dia'. Rende mesmo. O CDI (no mercado, o nome da taxa DI, a dos empréstimos de um dia entre bancos) é apurado e incorporado a cada dia útil. Mas a taxa DI é divulgada como taxa efetiva ao ano, base 252, e a própria B3 registra que a capitalização acontece só em dias úteis. A capitalização diária já está dentro dos 14%.

A 14% ao ano, o fator de cada dia útil é 1,14 elevado a 1/252: 0,05201% ao dia. Composto 252 vezes, dá exatamente 14%. Não sobra nada para a frequência acrescentar.

Ela só acrescenta quando o número cotado é nominal. Quem lê os 14% como nominal e divide por 252 chega a 0,05556% ao dia, e a 15,02% no ano. É o erro da etiqueta, em versão de varejo.

Numa taxa efetiva, a frequência já foi paga.

## Por que a mesa de opções fala contínuo

Se composto e contínuo são a mesma curva, por que alguém se daria ao trabalho de trocar a etiqueta?

O Manual de Apreçamento de Contratos de Opções da B3, o documento com a metodologia dos prêmios de referência das opções listadas, responde na prática. Para opções sobre ações, ETFs (fundos negociados em bolsa) e índices, o manual usa a fórmula de Black-Scholes-Merton, a de preço de opções. A taxa que entra nela não é a do DI futuro como cotada. É a tradução dela:

$$
r_n = \ln\left(1 + \text{TPre}_{n}\right), \qquad T_n = \frac{DU_n}{252}
$$

TPreₙ é a taxa prefixada para o vencimento n, tirada da curva do DI1, o contrato futuro da B3 sobre a taxa DI, cotado em taxa efetiva anual, base 252. DUₙ são os dias úteis até o vencimento.

A régua continua brasileira: o prazo é du/252. A curva também continua a mesma: e elevado a (rₙ × Tₙ) dá exatamente o fator do DI. A B3 não trocou de motor. Trocou de etiqueta.

Troca porque o modelo é escrito em tempo contínuo, e nele a etiqueta contínua facilita três coisas. As duas primeiras, o texto anterior já adiantou:

1. O retorno vira soma. Em taxa contínua, a taxa de dois anos é a soma das taxas de cada ano: 13,10% + 13,10% = 26,21%, e e elevado a 0,2621 dá 1,2996, que é 1,14 ao quadrado. Na taxa efetiva, dois anos de 14% dão 29,96%, e não 28%. Para tirar de uma curva a taxa a termo (a taxa combinada hoje para um período que começa no futuro), basta subtrair.
2. O cálculo diferencial trabalha. O modelo descreve o preço do ativo mudando instante a instante, e o preço da opção sai de uma equação diferencial. O desconto que encaixa nela é e elevado a (−r × T): a equação dM/dt = r × M, lida de trás para a frente.
3. A volatilidade (a medida de quanto o preço oscila) já fala essa língua. No modelo, ela é o desvio-padrão dos retornos logarítmicos, o logaritmo da razão entre dois preços, que é o retorno em taxa contínua. Quando o manual estima a volatilidade de ativos pouco negociados a partir do histórico, é com esses retornos que trabalha.

John Hull, no capítulo de taxas de juros do seu manual de derivativos, um dos mais usados no mercado, registra que as taxas contínuas são usadas extensivamente na análise de derivativos [VERIFICAR: formulação do Hull, 11ª ed., cap. 4; a pesquisa não achou a frase em fonte verificável]. A escolha é de conveniência, não de precisão.

### Onde mora o erro

Dentro da mesma instituição, a tesouraria cota o DI em taxa efetiva, base 252, e a mesa de opções precisa de uma taxa contínua. O risco mora na passagem de uma para a outra. Quem paga fica do outro lado do balcão.

É o erro dos 15,03% que o texto anterior apontou, agora com endereço: o DI futuro a 14% colocado direto no modelo, como se fosse r.

Um exemplo simples, em cálculo próprio. Ação a R$ 100,00, sem dividendos. Opção com preço de exercício (o preço fixado no contrato) de R$ 100,00, volatilidade de 25% ao ano e um ano, 252 dias úteis, até o vencimento.

O preço a termo da ação, o preço justo hoje para entregá-la daqui a um ano, é R$ 114,00 com a taxa traduzida e R$ 115,03 sem a tradução. A opção de compra (o direito de comprar a ação pelo preço de exercício) sai a R$ 16,72 com r = 13,10% e a R$ 17,24 com r = 14%: 3,1% mais cara. A opção de venda (o direito de vender a ação pelo preço de exercício) sai 6,0% mais barata, R$ 4,18 contra R$ 4,44.

Do outro lado do balcão, quem compra a opção de compra cotada assim paga R$ 0,52 a mais por ação, e quem vende a opção de venda recebe R$ 0,26 a menos. Ninguém errou a taxa. Errou a etiqueta.

Na escada dos 14%, capitalizar a cada instante em vez de todo dia valia menos de meio ponto-base (o centésimo de ponto percentual). Errar a etiqueta vale 103.

O perigo nunca foi a frequência. É a etiqueta.

## Uma pergunta antes das outras três

As três perguntas do texto anterior (motor, base, dias que contam) ganham uma que vem antes delas:

Qual é a etiqueta da taxa? Efetiva, nominal ou contínua? E, se é nominal, capitaliza quantas vezes por ano?

Com a resposta, a decisão fica simples.

Se uma das taxas é nominal e a outra efetiva, converta antes de comparar. Os 12% nominais com capitalização mensal custam 68 pontos-base a mais do que parecem.

Se as duas têm frequências altas, diária contra contínua, e a taxa é da ordem do DI, a diferença cabe no arredondamento. Pode ignorar. Se a taxa é de cartão, não pode.

Se a taxa vai entrar num modelo, traduza sempre. O erro da etiqueta é da ordem de um ponto percentual.

Na planilha, as contas são estas:

```
Nominal (m vezes ao ano) → efetiva:   =EFETIVA(j;m)     ou  =(1+j/m)^m-1
Efetiva → nominal (m vezes ao ano):   =NOMINAL(i;m)     ou  =m*((1+i)^(1/m)-1)
Efetiva → contínua:                   =LN(1+i)
Contínua → efetiva:                   =EXP(r)-1
DI futuro → Black-Scholes:            r: =LN(1+taxa)    T: =du/252
```

E uma regra de bolso: dobrar a frequência corta quase exatamente pela metade a distância até o teto contínuo. Para saber se a frequência importa no seu caso, compare essa distância com a precisão de que você precisa.

Para comparar dois CDBs, meio ponto-base some. Para replicar um preço, não: a 14%, meio ponto-base muda o preço de uma LTN de um ano em quase R$ 0,04, e o Tesouro manda manter seis casas decimais. No mercado, até a precisão é cláusula. Na metodologia do Tesouro Nacional para a LTN (Letra do Tesouro Nacional, o título público prefixado), o expoente du/252 é truncado na 14ª casa decimal e o preço unitário, na 6ª. Para replicar o preço na planilha:

```
PU da LTN:   =TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6)
```

## Fechamento: o topo da escada

Capitalizar com mais frequência rende mais, mas cada corte rende menos que o anterior, e a escada tem topo. Bernoulli provou em 1683 que ela tem topo, e Euler deu a esse topo um nome. Uma taxa efetiva de 14% e uma contínua de 13,10% descrevem o mesmo dinheiro. A frequência não muda o motor. Muda a etiqueta.

O contínuo não compete com o composto. É o limite dele.

Se o texto funcionou, você consegue ler sozinho uma taxa que todo brasileiro já ouviu. Quando a meta da Selic (a taxa básica de juros) está acima de 8,5% ao ano, a poupança paga 0,5% ao mês, mais a TR (Taxa Referencial). Deixe a TR de lado. Por que "a poupança rende 6% ao ano" é uma taxa nominal? Quanto ela vale efetiva? E quanto vale na etiqueta que um modelo usaria?

Com a régua, o motor e agora a etiqueta, o expoente du/252 desta série está explicado de ponta a ponta.

Se este texto ajudou você a ler uma taxa pela etiqueta, encaminhe para quem ainda acha que o contínuo é o juro mais agressivo.

## Para continuar aprendendo

- Eli Maor, *e: A História de um Número* (Record) [VERIFICAR: ano da edição] — a biografia do número, dos juros compostos de Bernoulli à notação de Euler; o apêndice sobre a existência do limite de (1 + 1/n)ⁿ é a versão completa da conta deste texto.
- John C. Hull, *Options, Futures, and Other Derivatives*, 11ª ed. (Pearson, 2021), cap. 4, "Interest Rates" — frequência de capitalização, taxa contínua e as fórmulas de conversão entre uma e outra (seção 4.4).
- Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações*, 15ª ed. (GEN Atlas, 2022) — taxas nominais, efetivas e equivalentes, com a nomenclatura e os exemplos do mercado brasileiro.
- J. J. O'Connor e E. F. Robertson, ["The number e"](https://mathshistory.st-andrews.ac.uk/HistTopics/e/) (MacTutor History of Mathematics, Universidade de St Andrews) — o registro histórico curto: Bernoulli em 1683, o binômio, a carta de Euler de 1731.
