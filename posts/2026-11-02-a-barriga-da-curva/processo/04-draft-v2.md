# Etapa 4 — Draft v2 (respostas do autor à crítica)

Base: `04-draft-v1.md`. Mudanças por decisão do autor sobre `05-critica.md` (A1, M1/M7, M2, M3;
ver `02-estrutura.md`, "Revisão pós-etapa 5") e, para os demais itens, **aplicação por padrão**
das recomendações da crítica, marcada abaixo como "padrão". O autor pode reverter qualquer
uma no gate. Esta reentrada vem da regra da etapa 5 (severidade alta), não de um pedido do gate:
não consome loop. Divergências factuais da pesquisa continuam com a etapa 7.

## Notas laterais

| # | Onde | Mudança | Origem |
|---|---|---|---|
| 1 | Ordem | Barriga e bola de neve sobem para logo depois da Anatomia; "Quem escolhe o motor" (com 1998 e "Onde o linear sobrevive") vem depois delas | Autor (M1) |
| 2 | Abertura, pergunta-âncora | "A forma de cotar que o mercado brasileiro adotou por norma… Por quê? E o que isso muda…?" → "O motor que a renda fixa brasileira usa por padrão é justamente o que paga menos em seis meses. Por que, então, cotar assim, e o que isso muda…?" (uma pergunta só) | Autor (A1) + padrão (B1) |
| 3 | Abertura, 2º–4º § | "Em todas, o du/252 estava no expoente" junta-se ao 2º §; sai "Falta dizer por que está lá" (terceira pergunta). O gancho numérico chega um parágrafo antes | Padrão (B1) |
| 4 | Prazo quebrado | + "É a mesma diferença de meio período da abertura, carregada por mais um ano." (R$ 2.613,08 ≈ 1,14 × R$ 2.292,17). Frase-sinal: "O interessante começa quando se desenha essa diferença." | Padrão (B2); consequência de M1 |
| 5 | Barriga | "Para qualquer fração de período" ganha "Com o mesmo número cotado" | Padrão (M6) |
| 6 | Barriga, graf-01 | Legenda com dois motores; sai a tracejada contínua | Autor (M2) |
| 7 | Barriga | + parágrafo que nomeia o duplo sentido: "Quem é de mesa conhece outra: a barriga da curva de juros, os vencimentos intermediários. Esta fica na outra ponta, no prazo curto…" | Autor (M3) |
| 8 | Barriga | Sai o vizinho anônimo ("uma operação cotada a 14% ao ano, linear, base 360"). Entra a taxa legal (CMN 5.171) como vizinho nomeado, com os dois lados da barriga e "cerca de metade" (15 dias ÷ dias corridos do mês) | Autor (M7) |
| 9 | Barriga → Três perguntas | O parágrafo do 365/360 (14,19%) sai da barriga e vai para a Prateleira | Padrão (B3) |
| 10 | Bola de neve | Marcador único `> [graf-02]` com legenda, no lugar do "[embedded content]"; sai o marcador duplicado | Padrão (B5) |
| 11 | Quem escolhe o motor | Abre com a pergunta que liga à barriga: "Se o composto paga menos no prazo curto e só ganha de verdade no longo, por que é ele o padrão?" | Autor (A1, M1) |
| 12 | A virada de 1998 | Reescrita para a espinha nova: motor composto já existia (over "efetiva-dia"); embalagem "linear por fora, composta por dentro" = **taxa nominal**; Circular 2.761 "Saiu uma taxa nominal, entrou uma efetiva"; Garcia (inflação; fevereiro × julho) + "A taxa efetiva não se contradiz entre prazos medidos em dias úteis. O mês civil… é que passou a oscilar." Sai "Hoje, Taxa DI, LTN, NTN-B… falam essa língua" (repete o du252) | Autor (A1) + padrão (M5) |
| 13 | Onde o linear sobrevive | Taxa legal reduzida a remissão ("que já apareceu na barriga"); "E o contínuo" vira uma frase (modelos, Black-Scholes-Merton, Susep); sai a frase da ANBIMA/Svensson | Autor (M2, M7) |
| 14 | Três perguntas | Abre pelo propósito, sem parágrafo de metodologia. + previsão de direção ("com prazo menor que um ano, a taxa linear vira uma taxa composta maior"). Exemplo 14,92% separa motor (0,75 pp; 14,75% com régua 63/252) e régua (0,17 pp). A quarta conta "traz de volta as duas perguntas que ficaram no texto anterior, calendário e pontas" (resolve a contradição) | Padrão (M5, B4); números: cálculo do pipeline, a refazer na etapa 7 |
| 15 | Fechamento | "Com o mesmo número cotado, o juro simples ganha…"; "O mercado brasileiro cota no composto porque é o motor que não se contradiz de um prazo para o outro. Em 1998, trocou uma taxa nominal por uma efetiva." Teste: "você consegue fazer a mesma troca sozinho" | Autor (A1) + padrão (M6) |
| 16 | CTA | "quem ainda divide a taxa anual por doze" → "quem ainda acha que o composto sempre rende mais" (mira o erro-alvo) | Padrão (M4) |

**Não aplicado (fica visível para o gate):** B6 (bibliografia repete Garcia e Hull do du252;
§5.7 cumprido); B7 (registro explicativo em "Onde o linear sobrevive", agora bem mais curto).

---

# A Barriga da Curva

*Juro simples, composto e contínuo além dos livros*

---

No último texto, contei os dias: os 252 de um ano convencional, os 249 de 2026, o calendário que decide se o juro correu no sábado. O motor, a regra que transforma o tempo contado em dinheiro, ganhou duas linhas: composto, (1 + i) elevado a τ; linear, 1 + i vezes τ.

Duas linhas é pouco para uma conta que aparece em quase todo texto desta série. Na LCA (Letra de Crédito do Agronegócio), para achar a taxa em que um CDB empata com ela depois do imposto. Na debênture, para converter percentual do CDI em CDI mais spread e para estimar quanto o PU (preço unitário, o valor de mercado de cada título) cai quando o spread do devedor abre. Em todas, o du/252 estava no expoente.

Antes do FIDC, então, mais um parêntese de ferramenta. Ele começa com uma pergunta que parece de primeiro período da faculdade.

Você aplica R$ 1 milhão a 14% ao ano por seis meses, ou 126 dias úteis. Quanto rende?

Se a sua resposta foi R$ 70 mil, você acertou. É o que paga o juro simples, e há contratos que pagam assim.

E você errou. Num CDB prefixado à mesma taxa, o rendimento é de R$ 67.707,83.

A diferença, R$ 2.292,17, não é arredondamento. É a distância entre dois motores.

O motor que a renda fixa brasileira usa por padrão é justamente o que paga menos em seis meses. Por que, então, cotar assim, e o que isso muda na hora de ler qualquer taxa que alguém coloca na sua frente?

## A versão que se aprende cedo

A história costuma ser contada assim. Juro simples é coisa de livro escolar e de agiota de bairro. Juro composto é o regime dos profissionais, a 'bola de neve', a força que uma frase atribuída a Einstein, sem fonte que a sustente, chamaria de oitava maravilha do mundo.

Então o composto rende mais. Sempre. E começa a trabalhar desde o primeiro dia.

As duas afirmações são falsas. A primeira, entre zero e um período. A segunda, por mais tempo do que quase todo mundo imagina.

Capitalização não é lei da natureza. É cláusula.

## Três motores para o mesmo tempo

Um regime de capitalização, o motor do texto anterior, é a regra que diz o que acontece com o juro de cada período: se ele fica parado ao lado do capital ou se passa a render junto. Nas três fórmulas abaixo, C é o capital, M o montante (capital mais juros), i a taxa por período e t o prazo medido em períodos da própria taxa.

Na capitalização simples, ou regime linear, o juro incide só sobre o capital inicial. O montante cresce em progressão aritmética, uma reta:

```latex
M = C\,(1 + i\,t)
```

Na capitalização composta, ou regime exponencial, o juro de cada período se incorpora ao saldo e passa a render no período seguinte. É o 'juro sobre juro', que o Direito chama de anatocismo. O montante cresce em progressão geométrica:

```latex
M = C\,(1 + i)^{t}
```

Na capitalização contínua, o juro é reinvestido a cada instante, como se o número de capitalizações por período tendesse ao infinito. Entra a constante de Euler, e ≈ 2,71828, e uma taxa instantânea r:

```latex
M = C\,e^{r\,t}, \qquad r = \ln(1 + i)
```

A segunda igualdade importa. Com r = ln(1,14) = 13,10%, o motor contínuo dá exatamente o mesmo montante que 14% compostos. Quem aplica e elevado a 0,14 vezes t, usando o número cotado como se fosse taxa instantânea, está calculando 15,03% ao ano sem perceber.

Resta medir t, e aqui volta a régua. No Brasil, para quase toda a renda fixa em reais, t = du/252: dias úteis do período sobre um ano convencional de 252 dias úteis. É o expoente dos textos anteriores. Lá fora, o mais comum é contar dias corridos sobre 360 ou 365.

### O prazo quebrado

Quando o prazo tem uma parte inteira n e uma fração f de período, há duas formas de fechar a conta dentro do regime composto. A convenção linear, ou mista, compõe a parte inteira e aplica juro simples na fração. A convenção exponencial compõe tudo:

```latex
M_{\text{linear}} = C\,(1 + i)^{n}\,(1 + i\,f) \qquad M_{\text{exponencial}} = C\,(1 + i)^{n + f}
```

R$ 1 milhão a 14% ao ano por um ano e meio: R$ 219.800,00 de juros pela convenção linear, R$ 217.186,92 pela exponencial. A fração vale R$ 2.613,08 para um dos lados do contrato. É a mesma diferença de meio período da abertura, carregada por mais um ano.

Até aqui, é o segundo capítulo de qualquer livro de matemática financeira. O interessante começa quando se desenha essa diferença.

## A barriga da curva

Eis a peça que separa quem decorou as fórmulas de quem as entende.

Os dois motores passam pelos mesmos dois pontos. Em t = 0, os dois valem C. Em t = 1, os dois valem C vezes (1 + i): no fim do primeiro período ainda não há juro anterior para render juro.

Entre esses dois pontos, a reta do juro simples é a corda de uma curva convexa. E a corda de uma curva convexa passa por cima dela. Com o mesmo número cotado, para qualquer fração de período, o juro composto rende menos que o simples. Quem fez cálculo reconhece a desigualdade de Bernoulli; quem não fez, pode confiar no desenho.

> [graf-01] Gráfico: montante de R$ 1.000 a 14% ao ano entre zero e dois anos, nos dois motores: a reta do juro simples e a curva do juro composto. Entre zero e um ano, a reta fica acima da curva, com a maior distância perto de seis meses (R$ 1.070,00 contra R$ 1.067,71). As duas se encontram em um ano, em R$ 1.140,00, e a curva passa por cima da reta dali em diante.

O espaço entre a corda e a curva, abaixo de um período, é a barriga deste texto. Quem é de mesa conhece outra: a barriga da curva de juros, os vencimentos intermediários. Esta fica na outra ponta, no prazo curto, e mora dentro de qualquer taxa, não só na curva.

Na prática, isso quer dizer que, com o mesmo número cotado, o motor linear paga mais a quem aplica e cobra mais de quem toma sempre que o prazo é menor que o período da taxa. Seis meses de uma taxa anual. Quinze dias de uma taxa mensal. A fração de mês de uma dívida em atraso.

Esse último caso tem endereço. Em 2024, a Resolução CMN nº 5.171 definiu o cálculo da taxa legal, a que corrige uma dívida civil quando o contrato não fixa juros (art. 406 do Código Civil). O art. 6º manda acumulá-la em juros simples, tanto de um mês para o outro quanto na fração do mês, apropriada por dias corridos. O devedor com quinze dias de atraso paga a taxa do mês proporcional aos dias, cerca de metade, e não o equivalente composto: fica do lado de cima da corda. Numa dívida de muitos meses, as taxas mensais se somam em vez de se multiplicar, e ele passa para o lado de baixo. A mesma norma, dos dois lados da barriga.

Por isso a frase "14% ao ano", sozinha, não diz quanto você vai receber. Ela é a metade de uma cláusula.

## A bola de neve demora a rolar

Depois do primeiro período, o composto passa à frente. A pergunta seguinte é quanto do rendimento é, de fato, juro sobre juro.

O montante composto se decompõe em três camadas: o capital; o juro simples sobre o capital, que cresce em linha reta; e o juro sobre juro, a parte que só existe porque o juro anterior foi reinvestido.

```latex
J_{\text{juro sobre juro}} = C\,\left[(1 + i)^{t} - 1 - i\,t\right]
```

Em dois anos a 14% ao ano, R$ 1.000 rendem R$ 299,60. Desses, R$ 280,00 são juro linear. O juro sobre juro responde por R$ 19,60.

> [graf-02] Gráfico: parcela do juro sobre juro no juro total de R$ 1.000 em juros compostos a 6%, 10% e 14% ao ano, prazos de 1 a 30 anos (cálculo próprio).

A virada, o prazo em que o juro sobre juro passa a valer mais que o juro linear, chega depois de uma década a 14% ao ano. A 6%, uma taxa na ordem de grandeza de um juro real, leva mais de duas.

Quem aplica por dois anos está comprando, essencialmente, juro simples com uma correção pequena. Quem aplica por trinta está comprando outra coisa.

Quem faz a bola de neve crescer é o tempo.

## Quem escolhe o motor, e por quê

Se o composto paga menos no prazo curto e só ganha de verdade no longo, por que é ele o padrão?

Cada motor embute uma hipótese. O linear supõe que o juro fica parado até o fim do período. O composto supõe que ele é reinvestido à mesma taxa. Para quem cota juros para muitos prazos ao mesmo tempo, essa diferença vira dinheiro.

Volte ao exemplo da abertura. A 14% ao ano no motor linear, quem aplica por seis meses e renova por mais seis termina o ano com um fator de 1,07 × 1,07 = 1,1449. Rendeu 14,49%, contra 14% de quem aplicou direto por um ano, à mesma taxa cotada.

Uma taxa linear única não consegue valer para todos os prazos ao mesmo tempo. Fatiar o prazo vira estratégia.

No motor composto, o fatiamento não muda nada: 1,14 elevado a 0,5, vezes 1,14 elevado a 0,5, dá 1,14. Aplicar por 63 dias úteis e reaplicar por mais 63 gera o mesmo fator que aplicar por 126. É essa propriedade que permite montar uma curva de juros inteira, do overnight ao título de dez anos, sem que um prazo contradiga o outro.

### A virada de 1998

No Brasil, o motor composto já estava lá antes de a norma falar dele. A over, a taxa do mercado de um dia, nascera como taxa 'efetiva-dia', acumulada de forma composta. O que se mudou foi a embalagem. Cotava-se a over ao mês, multiplicando a taxa do dia por 30 [VERIFICAR: convenção da taxa over mensal como taxa por dia útil × 30, com fonte de livro-texto]: linear por fora, composta por dentro. Uma taxa assim tem nome, taxa nominal, e o número cotado não é o que se recebe.

Como contei no texto anterior, a Circular BCB nº 2.761, de junho de 1997, trocou essa embalagem pela Selic expressa ao ano, como taxa efetiva com base em 252 dias úteis, a partir de 1998. Saiu uma taxa nominal, entrou uma efetiva.

Num texto da época, o economista Márcio Garcia, da PUC-Rio, leu a mudança pela inflação: com ela em um dígito ao ano, era natural voltar a cotar juros ao ano. E apontou um efeito colateral que ficou de fora do texto anterior. Com a mesma taxa por dia útil, fevereiro de 1998, com 18 dias úteis, renderia 1,42% no mês; julho, com 23, renderia 1,82%. Quarenta pontos-base de diferença que pareciam volatilidade e eram só calendário. A taxa efetiva não se contradiz entre prazos medidos em dias úteis. O mês civil, que tem um número variável deles, é que passou a oscilar.

Em julho de 2000, o Comunicado BCB nº 7.684 levou o mesmo padrão às operações do Banco Central com títulos públicos: taxa efetiva anual, base 252 [VERIFICAR: texto integral do Comunicado 7.684].

### Onde o linear sobrevive

O motor linear não morreu. Ele ficou onde resolve melhor o problema de quem cota.

No cupom cambial, a taxa de juro em dólar negociada no Brasil, os contratos futuros da B3 (DDI) e o FRC, sua operação a termo, são cotados em taxa linear ao ano, base 360 dias corridos. É a língua do mercado monetário internacional em dólar, onde depósitos de curto prazo sempre foram rateados de forma proporcional ao tempo.

Nos títulos do Tesouro americano, o juro acumulado entre dois pagamentos de cupom, o que o comprador paga ao vendedor pelos dias já corridos, também é apropriado de forma linear. E há a taxa legal brasileira, que já apareceu na barriga.

O contínuo ficou com os modelos: torna os retornos aditivos no tempo e deixa o cálculo diferencial trabalhar, e por isso aparece no modelo de Black-Scholes-Merton e na curva de juros que a Susep (Superintendência de Seguros Privados) estima antes de converter para taxa discreta.

Nenhum dos três motores é o certo. Cada um é o que resolve o problema de quem está cotando.

## Três perguntas antes de qualquer taxa

Para comparar duas taxas cotadas em motores diferentes, três perguntas resolvem quase tudo. São as duas primeiras do texto anterior, a contagem e o regime, com a contagem aberta em duas:

qual é o motor, linear ou exponencial;

qual é a base, 252, 360 ou 365;

que dias contam, os úteis ou os corridos.

Com as três respondidas, basta igualar os fatores do mesmo período:

```latex
(1 + i_{252})^{du/252} = 1 + i_{360}\,\frac{dc}{360}
```

E dá para prever o lado antes da conta: com prazo menor que um ano, a taxa linear vira uma taxa composta maior.

Uma operação de 91 dias corridos, que no calendário contém 63 dias úteis, cotada a 14% ao ano linear base 360, tem fator de 1 + 0,14 × 91/360 = 1,035389. Na convenção brasileira, isso equivale a 1,035389 elevado a 252/63, menos 1: 14,92% ao ano. O mesmo "14%" virou quase 15%. Do quase um ponto a mais, 0,75 vêm do motor: com a mesma régua, 63/252, a linear daria 14,75% compostos. Os 0,17 restantes vêm da régua, porque 91 dias corridos sobre 360 são um pouco mais que 63 úteis sobre 252.

A régua pesa mesmo num ano inteiro. Num ano civil de 365 dias corridos, 14% ao ano na base 360 rendem 14% × 365/360 = 14,19%.

Na planilha, as quatro contas que resolvem quase tudo:

```
Fator exponencial 252:     =(1+i)^(du/252)
Fator linear 360:          =1+i*dc/360
Linear 360 → exponencial:  =(1+i_lin*dc/360)^(252/du)-1
Dias úteis entre datas:    =DIATRABALHOTOTAL(início;fim;feriados)-1
```

A quarta conta traz de volta as duas perguntas que ficaram no texto anterior, calendário e pontas. O "menos 1" existe porque a função conta as duas pontas, e o mercado conta a data inicial e exclui a final [VERIFICAR: confirmar a convenção de inclusão de datas da ANBIMA e o calendário de feriados a usar]. Um calendário de feriados desatualizado muda o du, e o du está no expoente.

## Fechamento: o expoente que faltava

Com o mesmo número cotado, o juro simples ganha do composto em qualquer fração de período. O composto só começa a ganhar depois do primeiro período, e a bola de neve leva anos para valer mais que o juro linear. O mercado brasileiro cota no composto porque é o motor que não se contradiz de um prazo para o outro. Em 1998, trocou uma taxa nominal por uma efetiva.

Capitalização não é lei da natureza. É cláusula.

Se o texto funcionou, você consegue fazer a mesma troca sozinho. Pegue um contrato de financiamento que mostre, lado a lado, uma 'taxa nominal' e uma 'taxa efetiva'. Faça as três perguntas. Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números é o que você de fato paga?

Agora, sim, o FIDC (Fundo de Investimento em Direitos Creditórios), sem mais parênteses. Com a régua e o motor no lugar, dá para olhar uma carteira de devedores dividida em cotas e perguntar quem recebe primeiro, e quanto isso vale hoje.

Se este texto te ajudou a destravar uma conta que você fazia no automático, encaminhe para quem ainda acha que o composto sempre rende mais.

## Para continuar aprendendo

Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações* (Atlas) [VERIFICAR: edição e ano] — a referência brasileira para regimes, convenção linear e exponencial em prazos quebrados, taxa over e a decomposição do montante composto usada no gráfico.

José Carlos Samanez, *Matemática Financeira* (Pearson) [VERIFICAR: edição e ano] — tratamento paralelo, com mais exercícios de taxas equivalentes e nominais; bom para o teste de transferência.

John C. Hull, *Options, Futures, and Other Derivatives* (Pearson), cap. 4, "Interest Rates" [VERIFICAR: edição e número do capítulo] — frequência de capitalização, taxa contínua e conversões, na língua do mercado internacional.

Márcio G. P. Garcia, nota sobre a anualização da taxa Selic (PUC-Rio, junho de 1997) — o registro de época da mudança de 1998 e de seus efeitos nas taxas mensais. [link](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf)
