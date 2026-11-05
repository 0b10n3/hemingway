---
titulo: A Corda e o Arco
subtitulo: Juro simples, composto e contínuo além dos livros
slug: 2026-11-02-a-barriga-da-curva
data: 2026-11-02
linha_editorial: Notas de um Professor
tags: [Notas de um Professor, Renda Fixa, Matemática Financeira]
status: aprovado
---

No último texto conversamos sobre como um ano pode ter mais, ou menos, dias úteis do que os 252 de um ano convencional. 2026 tem 249 dias úteis.

Chamamos essa contagem de régua.

O motor, a regra que transforma o tempo contado em dinheiro, ganhou duas linhas:

composto, (1 + i) elevado a τ;

linear, 1 + i vezes τ.

Duas linhas é pouco para uma conta que aparece em quase todo texto desta série.

Na LCA (Letra de Crédito do Agronegócio), para achar a taxa em que um CDB (Certificado de Depósito Bancário) empata com ela depois do imposto. Na debênture, para converter percentual do CDI (no mercado, o nome da taxa DI, a dos empréstimos de um dia entre bancos) em CDI mais *spread* (o prêmio acima do CDI que paga o risco do devedor) e para estimar quanto o PU (preço unitário, o valor de mercado de cada título) cai quando o *spread* do devedor abre. Em todas, o du/252 (dias úteis sobre 252) estava no expoente.

Aqui podemos começar com uma pergunta típica do início de um curso de matemática financeira.

Você aplica R$ 1 milhão a 14% ao ano por seis meses, ou 126 dias úteis. Quanto rende?

Se a sua resposta foi R$ 70 mil, você acertou.

É o que o juro simples paga, e há contratos que pagam assim.

E você também errou.

Num CDB prefixado à mesma taxa, o rendimento é de R$ 67.707,83.

A diferença, R$ 2.292,17, é a distância entre dois motores.

## A versão que se aprende cedo

A história costuma ser contada assim. Juro simples é coisa de livro escolar e de agiota de bairro. Juro composto é o regime dos profissionais, a 'bola de neve', a força que uma frase atribuída a Einstein, sem fonte que a sustente, chamaria de oitava maravilha do mundo.

Então o composto rende mais. Sempre. E começa a trabalhar desde o primeiro dia.

As duas afirmações são falsas. A primeira, entre zero e um período. A segunda, por mais tempo do que quase todo mundo imagina.

Capitalização não é lei da natureza. É cláusula.

## Três motores para o mesmo tempo

Um regime de capitalização, o motor do texto anterior, é a regra que diz o que acontece com o juro de cada período: se ele fica parado ao lado do capital ou se passa a render junto. Nas três fórmulas abaixo, C é o capital, M o montante (capital mais juros), i a taxa por período e t o prazo medido em períodos da própria taxa.

Na capitalização simples, ou regime linear, o juro incide só sobre o capital inicial. O montante cresce em progressão aritmética, uma reta:

$$
M = C\,(1 + i\,t)
$$

Na capitalização composta, ou regime exponencial, o juro de cada período se incorpora ao saldo e passa a render no período seguinte. É o 'juro sobre juro', que o Direito chama de anatocismo. O montante cresce em progressão geométrica:

$$
M = C\,(1 + i)^{t}
$$

Na capitalização contínua, o juro é reinvestido a cada instante, como se o número de capitalizações por período tendesse ao infinito. Entram o número de Euler (e ≈ 2,71828) e uma taxa instantânea r:

$$
M = C\,e^{r\,t}, \qquad r = \ln(1 + i)
$$

A segunda igualdade importa. Com r = ln(1,14) = 13,10%, o motor contínuo dá exatamente o mesmo montante que 14% compostos. Usar e elevado a (0,14 × t), com o número cotado no lugar da taxa instantânea, é calcular 15,03% ao ano sem perceber.

Resta medir t, e aqui volta a régua. No Brasil, para quase toda a renda fixa em reais, t = du/252: dias úteis do período sobre um ano convencional de 252 dias úteis. É o expoente dos textos anteriores. Lá fora, o mais comum é contar dias corridos sobre 360 ou 365.

### O prazo quebrado

Quando o prazo tem uma parte inteira n e uma fração f de período, há duas formas de fechar a conta dentro do regime composto. A convenção linear, ou mista, compõe a parte inteira e aplica juro simples na fração. A convenção exponencial compõe tudo:

$$
M_{\text{linear}} = C\,(1 + i)^{n}\,(1 + i\,f) \qquad M_{\text{exponencial}} = C\,(1 + i)^{n + f}
$$

R$ 1 milhão a 14% ao ano por um ano e meio: R$ 219.800,00 de juros pela convenção linear, R$ 217.186,92 pela exponencial. A fração vale R$ 2.613,08 para um dos lados do contrato. É a mesma diferença de meio período da abertura, carregada por mais um ano.

Até aqui, é o segundo capítulo de qualquer livro de matemática financeira. O interessante começa quando se desenha essa diferença.

## A corda e o arco

Aqui está a ideia que separa quem decorou as fórmulas de quem as entende.

A reta do simples e a curva do composto passam pelos mesmos dois pontos. Em t = 0, os dois valem C. Em t = 1, os dois valem C vezes (1 + i): no fim do primeiro período ainda não há juro anterior para render juro.

Entre esses dois pontos, a reta do juro simples é a corda e a curva do composto é o arco. A curva é convexa (no sentido do cálculo: arqueada para cima, como o fundo de uma tigela).

E a corda de uma curva convexa passa por cima do arco. Com o mesmo número cotado, para qualquer fração de período, o juro composto rende menos que o simples. Quem fez um curso de cálculo reconhece a desigualdade de Bernoulli, na versão para expoentes entre zero e um; quem não fez pode confiar no desenho.

![Gráfico: R$ 1.000 a 14% ao ano, de zero a dois anos, nos dois motores. Entre zero e um ano, a reta do juro simples fica acima da curva do composto, com a maior distância perto de seis meses (R$ 1.070,00 contra R$ 1.067,71, uma diferença de R$ 2,29). As duas se encontram em um ano, em R$ 1.140,00, e a curva passa por cima da reta dali em diante: em dois anos, o composto paga R$ 19,60 a mais.](graf-01)

Na prática, isso quer dizer que, com o mesmo número cotado, o motor linear paga mais a quem aplica e cobra mais de quem toma sempre que o prazo é menor que o período da taxa. Seis meses de uma taxa anual. Quinze dias de uma taxa mensal. A fração de mês de uma dívida em atraso.

Esse último caso tem endereço. Em 2024, a Resolução nº 5.171 do Conselho Monetário Nacional (CMN) definiu o cálculo da taxa legal, a taxa de juros que incide sobre uma dívida civil quando o contrato não fixa a taxa. A norma manda acumulá-la em juros simples, tanto de um mês para o outro quanto na fração do mês, apropriada por dias corridos. O devedor com quinze dias de atraso paga a taxa do mês em proporção aos dias, cerca de metade dela, e não o equivalente composto: paga pela reta, que nesse trecho passa acima da curva. Numa dívida de muitos meses, as taxas mensais se somam em vez de se multiplicar, e a reta passa para baixo da curva. A mesma norma, ora acima da curva, ora abaixo dela.

Por isso a frase "14% ao ano", sozinha, não diz quanto você vai receber.

Ela é a metade de uma cláusula.

## A bola de neve demora a rolar

Depois do primeiro período, o composto passa à frente. A pergunta seguinte é quanto do rendimento é, de fato, juro sobre juro.

O montante composto se decompõe em três camadas: o capital; o juro linear, isto é, o juro simples sobre o capital, que cresce em linha reta; e o juro sobre juro, a parte que só existe porque o juro anterior foi reinvestido.

$$
J_{\text{juro sobre juro}} = C\,\left[(1 + i)^{t} - 1 - i\,t\right]
$$

Em dois anos a 14% ao ano, R$ 1.000 rendem R$ 299,60. Desses, R$ 280,00 são juro linear. O juro sobre juro responde por R$ 19,60.

![Gráfico: parcela do juro sobre juro no juro total de R$ 1.000 aplicados a juros compostos de 6%, 10% e 14% ao ano, em prazos de 1 a 30 anos. Em dois anos a 14%, é 6,5% do juro (R$ 19,60 de R$ 299,60). O juro sobre juro só passa a valer mais que o juro linear depois de 10,42 anos a 14%, 14,02 anos a 10% e 22,39 anos a 6%.](graf-02)

A virada, o prazo em que o juro sobre juro passa a valer mais que o juro linear, chega depois de uma década a 14% ao ano. A 6%, uma taxa da ordem de grandeza de um juro real (o que sobra acima da inflação), leva mais de duas.

Quem aplica por dois anos está comprando, essencialmente, juro simples com uma correção pequena. Quem aplica por trinta está comprando outra coisa.

Quem faz a bola de neve crescer é o tempo.

## Quem escolhe o motor, e por quê

Se o composto paga menos no prazo curto e só ganha de verdade no longo, por que é ele o padrão?

Cada motor embute uma hipótese. O linear supõe que o juro fica parado até o fim do período. O composto supõe que ele é reinvestido à mesma taxa. Para quem cota juros para muitos prazos ao mesmo tempo, essa diferença vira dinheiro.

Volte ao exemplo da abertura. A 14% ao ano no motor linear, quem aplica por seis meses e renova por mais seis termina o ano com um fator de 1,07 × 1,07 = 1,1449. Rendeu 14,49%, contra 14% de quem aplicou direto por um ano, à mesma taxa cotada.

Uma taxa linear única não consegue valer para todos os prazos ao mesmo tempo. Fatiar o prazo vira estratégia.

No motor composto, o fatiamento não muda nada: 1,14 elevado a 0,5, vezes 1,14 elevado a 0,5, dá 1,14. Aplicar por 63 dias úteis e reaplicar por mais 63 gera o mesmo fator que aplicar por 126. É essa propriedade que permite montar uma curva de juros inteira, do *overnight* (o empréstimo de um dia útil para o outro) ao título de dez anos, sem que um prazo contradiga o outro.

### A virada de 1998

No Brasil, o motor composto já estava lá antes de a norma falar dele. A *over*, a taxa das operações de um dia, era uma taxa 'efetiva-dia', acumulada de forma composta. O que mudou foi a embalagem. Com a megainflação, as taxas tinham passado a ser cotadas ao mês, e a convenção de mercado para a *over* ao mês multiplica a taxa do dia por 30: linear por fora, composta por dentro. Uma taxa assim tem nome, taxa nominal, e o número cotado não é o que se recebe.

Como contei no texto anterior, a Circular nº 2.761 do Banco Central do Brasil (BCB), de junho de 1997, trocou a embalagem: a partir de 1998, a Selic (a taxa básica de juros, que é a *over* das operações com títulos públicos) passou a ser expressa ao ano, como taxa efetiva com base em 252 dias úteis. Saiu a cotação ao mês, entrou uma taxa efetiva ao ano.

Num texto da época, o economista Márcio Garcia, da PUC-Rio, leu a mudança pela inflação: com ela em um dígito ao ano, era natural voltar a cotar juros ao ano. E apontou um efeito colateral que ficou de fora do texto anterior. Com a mesma taxa por dia útil, fevereiro de 1998, com 18 dias úteis, renderia 1,42% no mês; julho, com 23, renderia 1,82%. Quarenta pontos-base (0,40 ponto percentual) de diferença que pareciam volatilidade e eram só calendário. A taxa efetiva não se contradiz entre prazos medidos em dias úteis. O mês civil, que tem um número variável deles, é que passou a oscilar.

Em julho de 2000, o Comunicado BCB nº 7.684 levou o mesmo padrão às operações do Banco Central com títulos públicos: taxa efetiva anual, base 252.

### Onde o linear sobrevive

O motor linear não morreu.

O cupom cambial é a taxa de juro em dólar negociada no Brasil. Nele, os contratos futuros da B3 (DDI) e o FRC, a operação a termo de cupom, são cotados em taxa linear ao ano, base 360 dias corridos. É a língua do mercado monetário internacional em dólar, onde depósitos de curto prazo são, por convenção, rateados de forma proporcional ao tempo.

Nos títulos do Tesouro americano, o juro acumulado entre dois pagamentos de cupom (os juros periódicos do título), o que o comprador paga ao vendedor pelos dias já corridos, também é apropriado de forma linear. E há a taxa legal brasileira, que já apareceu neste texto.

O contínuo ficou com os modelos. Ele torna os retornos aditivos no tempo (o retorno de dois períodos é a soma dos dois) e deixa o cálculo diferencial trabalhar. Por isso aparece na fórmula de Black-Scholes-Merton, a de preço de opções, e nas curvas de juros que a Susep (Superintendência de Seguros Privados) estima em taxa contínua para as seguradoras.

Nenhum dos três motores é o certo. Cada um é o que resolve o problema de quem está cotando.

## Três perguntas antes de qualquer taxa

Para comparar duas taxas cotadas em motores diferentes, três perguntas resolvem quase tudo. São as duas primeiras do texto anterior, a contagem e o regime, com a contagem aberta em duas:

1. Qual é o motor? Linear ou composto?
2. Qual é a base? 252, 360 ou 365?
3. Que dias contam? Os úteis ou os corridos?

Com as três respondidas, basta igualar os fatores do mesmo período:

$$
(1 + i_{252})^{du/252} = 1 + i_{360}\,\frac{dc}{360}
$$

em que i₂₅₂ é a taxa composta base 252, i₃₆₀ a linear base 360, du os dias úteis e dc os dias corridos do período.

E dá para prever o lado antes da conta: com a mesma régua e prazo menor que um ano, a taxa linear vira uma taxa composta maior.

Uma operação de 91 dias corridos, que no calendário contém 63 dias úteis, cotada a 14% ao ano linear base 360, tem fator de 1 + 0,14 × 91/360 = 1,035389. Na convenção brasileira, isso equivale a 1,035389 elevado a 252/63, menos 1: 14,92% ao ano. O mesmo "14%" virou quase 15%. Dos quase 100 pontos-base a mais, 75 vêm do motor: com a mesma régua, 63/252, a linear daria 14,75% compostos. Os 17 restantes vêm da régua, porque 91 dias corridos sobre 360 são um pouco mais que 63 úteis sobre 252.

A régua pesa mesmo num ano inteiro. Num ano civil de 365 dias corridos, 14% ao ano linear, base 360, rendem 14% × 365/360 = 14,19%.

Na planilha, as quatro contas que resolvem quase tudo:

```
Fator exponencial 252:     =(1+i)^(du/252)
Fator linear 360:          =1+i*dc/360
Linear 360 → exponencial:  =(1+i_lin*dc/360)^(252/du)-1
Dias úteis entre datas:    =DIATRABALHOTOTAL(início;fim-1;feriados)
```

A quarta conta traz de volta as duas perguntas que ficaram no texto anterior, calendário e pontas. O "menos 1" vai na data final porque a função conta as duas pontas, quando são dias úteis, e o mercado conta a data inicial e exclui a final. Tirar o dia do fim, e não do resultado, mantém a conta certa quando o vencimento cai num feriado, como o 1º de janeiro das LTN (Letras do Tesouro Nacional, os títulos públicos prefixados). Um calendário de feriados desatualizado muda o du, e o du está no expoente.

## Fechamento: o expoente que faltava

Com o mesmo número cotado, o juro simples ganha do composto em qualquer fração de período. O composto só começa a ganhar depois do primeiro período, e a bola de neve leva anos para valer mais que o juro linear. O mercado brasileiro cota no composto porque é o motor que não se contradiz de um prazo para o outro. Em 1998, trocou a cotação ao mês por uma taxa efetiva ao ano.

Capitalização não é lei da natureza. É cláusula.

Se o texto funcionou, você consegue separar sozinho uma taxa nominal de uma efetiva. Pegue um contrato de financiamento que mostre, lado a lado, uma 'taxa nominal' e uma 'taxa efetiva'. Faça as três perguntas. Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números é o que você de fato paga?

Os 12,68% são o fio do próximo texto: a frequência de capitalização. Com uma corda por ano, 14% rendem 14%. Com duas, 14,49%, a conta que já fizemos. Com doze, 14,93%. Quanto mais curtas as cordas, mais a linha quebrada se aproxima do motor contínuo, e o rendimento nunca passa dos 15,03% que já apareceram aqui. Vamos ver o que essa frequência muda na taxa e como essa aproximação é usada. O FIDC que prometi vem depois desse texto.

Se este texto ajudou você a destravar uma conta que você fazia no automático, encaminhe para quem ainda acha que o composto sempre rende mais.

## Para continuar aprendendo

- Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações*, 15ª ed. (GEN Atlas, 2022) — a referência brasileira para regimes, convenção linear e exponencial em prazos quebrados e taxa over.
- Carlos Patricio Samanez, *Matemática Financeira*, 5ª ed. (Pearson Prentice Hall, 2010) — outro manual brasileiro de referência, bom para treinar o teste de transferência.
- John C. Hull, *Options, Futures, and Other Derivatives*, 11ª ed. (Pearson, 2021), cap. 4, "Interest Rates" — frequência de capitalização, taxa contínua e conversões, na língua do mercado internacional.
- Márcio G. P. Garcia, [*Efeitos da anualização da taxa Selic*](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf) (Departamento de Economia da PUC-Rio, 30/06/1997) — o registro de época da mudança de 1998 e de seus efeitos nas taxas mensais.

---

*Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira.*
