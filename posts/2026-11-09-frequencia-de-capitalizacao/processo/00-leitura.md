# Etapa 0 — Leitura do rascunho

Fonte: `_arquivo/drafts/2026-11-09Frequência de Capitalização.md` (intocado; já commitado em
`main`, `6a20a9b`).

**Front-matter:** ausente. O arquivo abre com o H1 "# Notas de um Professor — Frequência de
Capitalização \[draft v1\]" e "Nov 9, 2026 · @0b10n3" (cabeçalho de exportação).

**Linha editorial:** não há campo `linha_editorial`, então o pipeline parou e perguntou. **O autor
confirmou Notas de um Professor em 2026-11-09.** Daí: a etapa 2 usa a Ficha de Saída que o
próprio rascunho já traz (§"Ficha de Saída (não publicar)"), a etapa 5 roda sem validação
argumentativa e a 5a não roda.

**Título e slug:** o rascunho traz três candidatos: "Frequência de Capitalização" (H1), "Capitalização Contínua vs. Composta" com subtítulo "O Limite Matemático Que Explica as Duas"
(bloco da Ficha) e "Quantas Cordas Cabem num Ano?" (Pergunta ao autor nº 1). O slug é neutro:
`2026-11-09-frequencia-de-capitalizacao`. O título fica para a etapa 1.

**Autoria:** o texto foi montado a partir da pesquisa de pauta. As notas de processo dizem que "o
anexo trouxe só a pesquisa de pauta", e a Pergunta nº 4 diz: "Não escrevi nada no seu lugar".
Vale o precedente de `2026-11-02-a-barriga-da-curva`: o texto é tratado como rascunho, a
etapa 4 dá mais peso à voz e trecho de memória pessoal vira `[PREENCHER: …]`.

**Continuidade de série:** o texto continua "A Corda e o Arco" (`posts/2026-11-02-a-barriga-da-curva`, aprovado em
05/11), cuja última frase deixa o gancho: frequência, 12,68%, teto de 15,03%, motor contínuo.
**FIDC — tensão resolvida nesta etapa.** O texto sobre FIDC foi cancelado
(`evals/marketing/01-a-barriga-da-curva.md`, desdobramentos de 2026-11-09), e a promessa já saiu
dos três posts que a faziam. Este rascunho ainda anuncia o FIDC no fechamento e no campo 8 da
Ficha. **Decisão do autor (2026-11-09):** cortar a promessa e fechar sem anunciar o próximo
texto. A etapa 4 aplica.

**Natureza do rascunho:** chega completo e já com parte da verificação feita. Tem Ficha de Saída
com 8 campos, abertura que retoma o gancho do texto anterior, seis seções, seis blocos LaTeX,
dois blocos de planilha, um exemplo de Black-Scholes, dois visuais (`graf-01` como "embedded
content", que não veio no arquivo; `graf-02` descrito) e uma bibliografia de quatro itens. Fecha
com "Notas de processo (não publicar)": ajustes à pauta, pendências, visuais, quatro perguntas
ao autor e fontes consultadas.

**Limpeza aplicada na cópia:** `&#91;` → `[`, `\[`/`\]` → `[`/`]`, `\_` → `_`. Nada mais mudou.
O corpo abaixo é verbatim.

---

# Notas de um Professor — Frequência de Capitalização [draft v1]

Nov 9, 2026 · @0b10n3

## Ficha de Saída (não publicar)

Com este texto, o leitor deve conseguir converter uma taxa de uma frequência de capitalização para outra e saber quando essa diferença pesa no resultado. Também deve conseguir passar a taxa do DI para a taxa contínua que um modelo de opções usa.

Título : Capitalização Contínua vs. Composta
Subtítulo: O Limite Matemático Que Explica as Duas.


| Campo | Conteúdo |
| --- | --- |
| 1. Competência de saída | Converter uma taxa entre nominal com m capitalizações, efetiva anual e contínua; avaliar se a diferença de frequência é relevante para a taxa e o prazo em jogo; traduzir a taxa do DI para a entrada de um modelo (r = ln(1 + i), T = du/252). |
| 2. Teste de transferência | A poupança: 0,5% ao mês, mais TR, quando a meta da Selic está acima de 8,5% ao ano (Lei nº 12.703/2012). O leitor deve dizer sozinho por que "6% ao ano" é uma taxa nominal, quanto ela vale efetiva (6,17%) e quanto vale contínua (5,99%). |
| 3. Tese de fundo | "O contínuo não compete com o composto. É o limite dele." Mesma família da tese-mãe da série: a frequência é uma cláusula de cotação, não uma lei da natureza. |
| 4. Erro-alvo | Que a capitalização contínua é um regime à parte, mais agressivo ou mais preciso que o composto, e que capitalizar com mais frequência ("rende todo dia") sempre aumenta o rendimento de forma relevante. |
| 5. Ferramenta prática | Quarta pergunta antes de qualquer taxa (efetiva, nominal ou contínua?); conversões nominal ↔ efetiva ↔ contínua; funções EFETIVA, NOMINAL, LN e EXP; r = ln(1 + i) e T = du/252 para Black-Scholes; regra de bolso: dobrar a frequência corta pela metade a distância até o teto. |
| 6. Âncora de autoridade | Jacob Bernoulli, 1683 (MacTutor, Universidade de St Andrews); Manual de Apreçamento de Opções da B3, eq. (1.5); especificação do DI1 (taxa efetiva anual, base 252); Hull, cap. 4. |
| 7. Os dois lados do balcão | Quem cota a taxa (credor que cota nominal, B3 e tesourarias em efetiva 252, mesa de opções em contínua) × quem paga ou recebe a diferença (tomador do financiamento, investidor, quem compra ou vende a opção). Distribuidor: só de passagem, no "rende todo dia". |
| 8. Ponte de série | Vem de "A Corda e o Arco" (o gancho prometia frequência, 12,68% e o teto de 15,03%) → aponta para o FIDC, adiado lá em uma frase. |



No fim do último texto, deixei uma conta para você. Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números você de fato paga?

A resposta cabe em poucas linhas. 'Capitalizados mensalmente' quer dizer que o contrato divide os 12% por doze, dá 1% ao mês, e compõe esse 1% doze vezes. Cada real vira 1,01 elevado a 12, ou 1,1268.

Você paga os 12,68%. Os 12% são só a forma de cotar.

Agora empurre a pergunta. E se o contrato capitalizasse todo dia? E a cada segundo?

Cada corte a mais põe o juro para render mais cedo, então o rendimento sobe. Mas sobe até onde? Se dá para cortar o ano em pedaços cada vez menores, o rendimento cresce sem limite?

Em 1683, o matemático suíço Jacob Bernoulli fez essa mesma pergunta, com a taxa mais simples que existe: 100% ao ano.

A resposta dele explica duas coisas que parecem não ter relação. Por que o composto que você usa todo dia, o du/252 (dias úteis sobre 252) desta série, é só um caso particular. E por que o manual de opções da B3 faz as contas em outra taxa, que nenhum CDB jamais cotou.

## Dois motores rivais

A versão que circula é mais ou menos esta. O juro composto é o regime do mundo real: CDB (Certificado de Depósito Bancário), Tesouro, financiamento. A capitalização contínua é outro bicho, coisa de modelo e de quem precifica opções.

E, como capitaliza a cada instante, o contínuo seria o mais agressivo dos dois. Ou o mais preciso, conforme quem conta.

No texto anterior, eu mesmo apresentei três motores lado a lado. Devo uma correção: dois deles são o mesmo.

O contínuo não compete com o composto. É o limite dele.

## Nominal, frequência, efetiva

Três nomes resolvem a conta da abertura.

A taxa nominal, j, é o número escrito no contrato. A frequência de capitalização, m, diz quantas vezes por ano o juro é incorporado ao saldo. A taxa de cada subperíodo é a proporcional, j/m, que se compõe m vezes no ano. A taxa efetiva, i, é o que de fato rendeu no fim do ano:

```latex
1 + i = \left(1 + \frac{j}{m}\right)^{m}
```

Com j = 12% e m = 12, sai a conta da abertura: 1,01 elevado a 12, 12,68%.

É a mesma embalagem da *over* ao mês do texto anterior, a taxa do dia multiplicada por 30. Linear por fora, composta por dentro: uma taxa nominal com capitalização diária.

Volte à imagem do último texto. Dentro de cada subperíodo, o juro corre em linha reta: é uma corda. Na passagem para o subperíodo seguinte, o juro vira saldo e passa a render. As cordas se emendam numa linha quebrada, e quanto maior o m, mais curtas elas ficam.

### A escada de Bernoulli

Bernoulli tomou um capital de 1 a 100% ao ano. Com uma capitalização no ano, o capital vira 2. Com duas, de 50% cada, vira 1,5 × 1,5 = 2,25. Com quatro, 2,44. Com doze, 2,61. Com 52, uma por semana, 2,69. Com 365, uma por dia, 2,7146.

Cada degrau sobe menos que o anterior. Do anual para o semestral, o capital ganha 0,25. Do diário para o capitalizado a cada hora, ganha menos de quatro milésimos.

> [graf-02] Ilustração: a linha quebrada de Bernoulli. Capital de 1 a 100% ao ano, de zero a um ano. Linhas quebradas com 1, 2, 4 e 12 cordas terminam em 2, 2,25, 2,44 e 2,61. Por cima delas, a curva contínua termina em 2,718. Cada linha quebrada fica abaixo da seguinte, e todas abaixo da curva.

Bernoulli mostrou, com o binômio de Newton, que a escada nunca passa de 3. A conta cabe em uma linha. Expandido, o fator do ano fica assim:

```latex
\left(1 + \frac{1}{n}\right)^{n} = 1 + 1 + \frac{1}{2!}\left(1 - \frac{1}{n}\right) + \frac{1}{3!}\left(1 - \frac{1}{n}\right)\left(1 - \frac{2}{n}\right) + \cdots
```

Os parênteses são todos menores que 1, e cada fatorial cresce mais rápido que as potências de 2. A partir do terceiro termo, a soma fica abaixo de 1/2 + 1/4 + 1/8 + …, que dá 1. O total, portanto, nunca passa de 1 + 1 + 1 = 3.

E, quanto maior o n, mais perto de 1 chega cada parêntese: a escada sobe sempre, sem passar de 3. Uma escada assim tem um topo. O topo é 2,71828…, o número que Leonhard Euler, quase cinquenta anos depois, chamaria de e.

Até aqui, é o capítulo de taxas equivalentes de qualquer livro, com uma nota histórica. O interessante começa quando se troca os 100% de Bernoulli por uma taxa qualquer.

## De onde vem o e

Troque os 100% por uma taxa nominal qualquer, j, e chame de n o quociente m/j. Então j/m = 1/n e m = n × j. O fator do ano vira a escada de Bernoulli elevada a j:

```latex
\left(1 + \frac{j}{m}\right)^{m} = \left[\left(1 + \frac{1}{n}\right)^{n}\right]^{j} \;\longrightarrow\; e^{j} \qquad (m \to \infty)
```

Para 14% nominais, o teto é e elevado a 0,14, ou 1,1503: 15,03% ao ano, o número que apareceu duas vezes no texto anterior. Para um prazo t qualquer, o montante no limite é C vezes e elevado a (j × t). É o motor contínuo.

Há outro caminho até a mesma fórmula, e ele mostra a hipótese escondida. Se o juro é incorporado a cada instante, o saldo cresce, em cada instante, a uma velocidade proporcional a ele mesmo: a taxa vezes o saldo.

```latex
\frac{dM}{dt} = j\,M \quad\Longrightarrow\quad M(t) = C\,e^{\,j\,t}
```

O e é a base em que a curva sobe, em cada ponto, na mesma velocidade do próprio valor. Por isso ele aparece sempre que alguma coisa cresce em proporção a si mesma. A hipótese embutida é que nenhum centavo fica parado, nem por um instante, e que tudo é reinvestido à mesma taxa.

### Mesma curva, outra etiqueta

Agora a correção que eu devia ao texto anterior. Pegue a convenção brasileira, 14% ao ano efetivos, e reescreva o fator de um prazo qualquer:

```latex
(1 + i)^{t} = e^{\,t\,\ln(1 + i)} = e^{\,r\,t}, \qquad r = \ln(1{,}14) = 13{,}10\%
```

Não é uma aproximação. É uma identidade. A curva de um CDB prefixado a 14% ao ano, com o prazo medido em du/252, é, ponto a ponto, uma curva do motor contínuo, com taxa de 13,10%.

O mesmo vale para as frequências do meio do caminho. As cinco taxas abaixo entregam o mesmo rendimento, 14% em um ano:

- capitalização anual: 14,000%;
- semestral: 13,542% nominais;
- mensal: 13,175% nominais;
- diária, 252 vezes no ano: 13,106% nominais;
- contínua: 13,103%.

Quanto mais vezes se capitaliza, menor precisa ser o número cotado para entregar o mesmo rendimento. Os números descem e encostam nos 13,10% da taxa contínua.

Não existe uma fronteira entre o composto e o contínuo. Existe uma escada de etiquetas para o mesmo rendimento, e o contínuo é o topo dela.

A fama de 'mais agressivo' vem de comparar o mesmo número nas duas etiquetas: 14% compostos uma vez por ano contra 14% contínuos. É a conta dos 15,03% do texto anterior. O que muda é o número cotado, não o motor.

### Um aviso de vocabulário

No mercado brasileiro, 'exponencial' quase sempre quer dizer composto. A B3 chama a convenção de 252 dias úteis de 'conversão exponencial 252', e foi nesse sentido que o texto anterior falou em regime exponencial. O manual de opções da mesma B3 chama a taxa contínua de 'taxa de juro exponencial, em regime contínuo'.

As duas são exponenciais. É justamente o ponto deste texto.

## Rende todo dia não é render mais

Volte aos 14% nominais e suba com eles a escada de Bernoulli.

[embedded content: cálculo próprio · taxa nominal de 14% ao ano; efetiva = (1 + 0,14/m)^m − 1; teto = e^0,14 − 1 · no post, entra como graf-01 (imagem exportada)]

Em R$ 1 milhão por um ano, passar da capitalização anual para a mensal vale R$ 9.342,03. Da mensal para a diária, mais R$ 887,05. Da diária para a contínua, R$ 44,72.

Cada vez que se dobra a frequência, a distância até o teto cai quase exatamente pela metade. O ganho existe, mas some rápido.

Isso desmonta uma frase comum de propaganda: o dinheiro que 'rende todo dia'. Rende mesmo. O CDI (no mercado, o nome da taxa DI, a dos empréstimos de um dia entre bancos) é apurado e incorporado a cada dia útil. Mas a taxa DI é divulgada como taxa efetiva ao ano, base 252, e a própria B3 registra que a capitalização acontece só em dias úteis. A capitalização diária já está dentro dos 14%.

A 14% ao ano, o fator de cada dia útil é 1,14 elevado a 1/252: 0,05201% ao dia. Composto 252 vezes, dá exatamente 14%. Não sobra nada para a frequência acrescentar.

Ela só acrescenta quando o número cotado é nominal. Quem lê os 14% como nominal e divide por 252 chega a 0,05556% ao dia, e a 15,02% no ano. É o erro da etiqueta, em versão de varejo.

Numa taxa efetiva, a frequência já foi paga.

## Por que a mesa de opções fala contínuo

Se composto e contínuo são a mesma curva, por que alguém se daria ao trabalho de trocar a etiqueta?

O Manual de Apreçamento de Contratos de Opções da B3, o documento que define o prêmio de referência das opções listadas, responde na prática. Para opções sobre ações, ETFs (fundos negociados em bolsa) e índices, o manual usa a fórmula de Black-Scholes-Merton, a de preço de opções. A taxa que entra nela não é a do DI futuro como cotada. É a tradução dela:

```latex
r_n = \ln\left(1 + \text{TPre}_{n}\right), \qquad T_n = \frac{DU_n}{252}
```

TPreₙ é a taxa prefixada para o vencimento n, tirada da curva do DI1, o contrato futuro da B3 sobre a taxa DI, cotado em taxa efetiva anual, base 252. DUₙ são os dias úteis até o vencimento.

A régua continua brasileira: o prazo é du/252. A curva também continua a mesma: e elevado a (rₙ × Tₙ) dá exatamente o fator do DI. A B3 não trocou de motor. Trocou de etiqueta.

Troca porque o modelo é escrito em tempo contínuo, e nele a etiqueta contínua facilita três coisas:

1. O retorno vira soma. Em taxa contínua, a taxa de dois anos é a soma das taxas de cada ano: 13,10% + 13,10% = 26,21%, e e elevado a 0,2621 dá 1,2996, que é 1,14 ao quadrado. Na taxa efetiva, dois anos de 14% dão 29,96%, e não 28%. Para tirar de uma curva a taxa a termo (a taxa combinada hoje para um período que começa no futuro), basta subtrair.
2. O cálculo diferencial trabalha. O modelo descreve o preço do ativo mudando instante a instante, e o preço da opção sai de uma equação diferencial. O desconto que encaixa nela é e elevado a (−r × T): a equação dM/dt = r × M, lida de trás para a frente.
3. A volatilidade (a medida de quanto o preço oscila) já é medida assim. O manual a calcula a partir de retornos logarítmicos, o logaritmo da razão entre dois preços, que é o retorno em taxa contínua.

John Hull, no capítulo de taxas de juros do seu manual de derivativos, um dos mais usados no mercado, registra que as taxas contínuas são usadas extensivamente na análise de derivativos. É conveniência, não precisão.

### Onde mora o erro

De um lado do balcão, a tesouraria cota o DI em taxa efetiva, base 252. Do outro, a mesa de opções precisa de uma taxa contínua. O risco mora na passagem de um lado para o outro.

Quem pega o DI futuro a 14% e coloca direto no modelo, como se fosse r, está usando 15,03% ao ano sem perceber.

Um exemplo simples, em cálculo próprio. Ação a R$ 100,00, sem dividendos. Opção com preço de exercício (o preço fixado no contrato) de R$ 100,00, volatilidade de 25% ao ano e um ano, 252 dias úteis, até o vencimento.

O preço a termo da ação, o preço justo hoje para entregá-la daqui a um ano, é R$ 114,00 com a taxa traduzida e R$ 115,03 sem a tradução. A opção de compra (o direito de comprar a ação pelo preço de exercício) sai a R$ 16,72 com r = 13,10% e a R$ 17,24 com r = 14%: 3,1% mais cara. A opção de venda (o direito de vender a ação pelo preço de exercício) sai 6,0% mais barata, R$ 4,18 contra R$ 4,44.

Na seção anterior, capitalizar a cada instante em vez de todo dia valia menos de meio ponto-base (o centésimo de ponto percentual). Errar a etiqueta vale 103.

O perigo nunca foi a frequência. É a etiqueta.

## Uma pergunta antes das outras três

As três perguntas do texto anterior (motor, base, dias que contam) ganham uma que vem antes delas:

Qual é a etiqueta da taxa? Efetiva, nominal ou contínua? E, se é nominal, capitaliza quantas vezes por ano?

Com a resposta, a decisão fica simples.

Se uma das taxas é nominal e a outra efetiva, converta antes de comparar. Os 12% nominais com capitalização mensal custam 68 pontos-base a mais do que parecem.

Se as duas têm frequências altas, diária contra contínua, a diferença cabe no arredondamento. Pode ignorar.

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

No mercado, até a precisão é cláusula. Na metodologia do Tesouro Nacional para a LTN (Letra do Tesouro Nacional, o título público prefixado), o expoente du/252 é truncado na 14ª casa decimal e o preço unitário, na 6ª. Para replicar o preço na planilha:

```
PU da LTN:   =TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6)
```

## Fechamento: o topo da escada

Capitalizar com mais frequência rende mais, mas cada corte rende menos que o anterior, e a escada tem topo. Bernoulli provou em 1683 que ela tem topo, e Euler deu a esse topo um nome. Uma taxa efetiva de 14% e uma contínua de 13,10% descrevem o mesmo dinheiro. A frequência não muda o motor. Muda a etiqueta.

O contínuo não compete com o composto. É o limite dele.

Se o texto funcionou, você consegue ler sozinho uma taxa que todo brasileiro já ouviu. Quando a meta da Selic (a taxa básica de juros) está acima de 8,5% ao ano, a poupança paga 0,5% ao mês, mais a TR (Taxa Referencial). Deixe a TR de lado. Por que "a poupança rende 6% ao ano" é uma taxa nominal? Quanto ela vale efetiva? E quanto vale na etiqueta que um modelo usaria?

Com a régua, o motor e agora a etiqueta, o expoente du/252 desta série está explicado de ponta a ponta. No próximo texto, o FIDC (Fundo de Investimento em Direitos Creditórios), que prometi duas vezes: uma carteira de recebíveis dividida em cotas, e a pergunta de quem recebe primeiro.

Se este texto ajudou você a ler uma taxa pela etiqueta, encaminhe para quem ainda acha que o contínuo é o juro mais agressivo.

## Para continuar aprendendo

- Eli Maor, *e: A História de um Número* (Record) [VERIFICAR: ano da edição] — a biografia do número, dos juros compostos de Bernoulli à notação de Euler; o apêndice sobre a existência do limite de (1 + 1/n)ⁿ é a versão completa da conta deste texto.
- John C. Hull, *Options, Futures, and Other Derivatives*, 11ª ed. (Pearson, 2021), cap. 4, "Interest Rates" — frequência de capitalização, taxa contínua e conversões, e por que os derivativos preferem a etiqueta contínua.
- Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações*, 15ª ed. (GEN Atlas, 2022) — taxas nominais, efetivas e equivalentes, com a nomenclatura e os exemplos do mercado brasileiro.
- J. J. O'Connor e E. F. Robertson, ["The number e"](https://mathshistory.st-andrews.ac.uk/HistTopics/e/) (MacTutor History of Mathematics, Universidade de St Andrews) — o registro histórico curto: Bernoulli em 1683, o binômio, a carta de Euler de 1731.

## Notas de processo (não publicar)

O anexo trouxe só a pesquisa de pauta. O draft segue o gancho que você aprovou no fim de "A Corda e o Arco" (frequência, 12,68%, teto de 15,03%, motor contínuo, FIDC depois) e o vocabulário da série (motor, régua, corda, arco). Todos os números foram recalculados em Python (cálculo próprio).

### Ajustes à pauta

| Ponto da pauta | O que mudou no draft | Por quê |
| --- | --- | --- |
| "Capitalização exponencial (contínua)" e o título "do Composto ao Exponencial" | O texto diz "motor contínuo" e trata o duplo sentido de 'exponencial' numa subseção | Na série e na B3, "exponencial 252" é o composto. A nota do Substack ("Juro composto é o exponencial andando devagar") tem o mesmo problema. Sugestão: "O contínuo é o composto que nunca para de cortar o ano." |
| Nó 2: 252 × 360/365 como exemplo de frequência | Usado só para mostrar que, numa taxa efetiva base 252, capitalizar todo dia não acrescenta nada | 252, 360 e 365 são régua (contagem de dias), não frequência. A comparação de réguas já saiu nos dois textos anteriores |
| "Primeira vez que um número foi definido por um processo de limite" (MacTutor) | Fora do texto | A página original do MacTutor não abriu daqui. A cópia consultada confirma 1683, o binômio, o intervalo entre 2 e 3 e a carta de Euler de 1731, mas não essa frase |
| ANBIMA, fator "Exponencial de Dias" | Trocado pela metodologia do Tesouro Nacional: expoente truncado na 14ª casa, PU na 6ª | Não achei a expressão na ANBIMA; a regra de truncamento está no documento do Tesouro |
| Hull, 9ª ed. (2018) | 11ª ed. (2021), como no post anterior | Coerência da série. O uso "extensivo" de taxas contínuas em derivativos está na apresentação do cap. 4 (O'Reilly, 10ª ed.); parafraseado, sem citação literal |
| Nova âncora | Manual de Apreçamento de Opções da B3, eq. (1.5): r = ln(1 + TPre), T = DU/252 | Mostra a própria B3 fazendo a tradução; é mais forte que citar só o Hull |

### Pendências [VERIFICAR]

- Ano da edição da Record do livro do Maor.
- Manual de opções da B3: consultei a v26 (página de rosto com 26/05/2026). Conferir o número da equação na versão vigente na data da publicação.
- Hull, 11ª ed.: número da seção "Continuous compounding" (4.2 nas edições anteriores).
- "Rende todo dia": ficou genérico, sem nomear instituição.

### Visuais

- graf-01 (convergência para o teto): desenhado acima; exportar para o post.
- graf-02 (linha quebrada de Bernoulli: 1, 2, 4 e 12 cordas e a curva contínua): só descrito no texto, falta produzir.

### Perguntas ao autor

1. Título: "Quantas Cordas Cabem num Ano?" continua a imagem da corda e do arco. Prefere um dos títulos da pauta?
2. O mito admite que o texto anterior apresentou três motores e diz "devo uma correção". Fica assim, ou prefere enquadrar como aprofundamento?
3. Profundidade: a demonstração do teto de 3 (binômio) e o exemplo de Black-Scholes são os trechos mais técnicos. Ficam no corpo, encurtam ou vão para nota? É a decisão 3 em aberto no BACKWARDS_DESIGN.
4. Uma linha sua: como o e apareceu para você na graduação em Matemática? Encaixaria depois da escada de Bernoulli. Não escrevi nada no seu lugar.

### Fontes consultadas

- [MacTutor, "The number e" (cópia em umanitoba.ca)](https://home.cc.umanitoba.ca/~mcleod/Number/e.html) — Bernoulli em 1683, binômio, limite entre 2 e 3; notação e de Euler, carta a Goldbach de 1731.
- [B3, Programa de Treinamento DI, "Taxas de Juros"](https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/programa-de-treinamento-di/02-taxas-de-juros.htm) — base 360 internacional; "conversão exponencial 252" para Selic e DI; capitalização só em dias úteis.
- [B3, Futuro de DI1](https://b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/futuro-de-taxa-media-de-depositos-interfinanceiros-de-um-dia.htm) — cotação em taxa de juro efetiva anual, base 252 dias úteis.
- [B3, Manual de Apreçamento — Contratos de Opções (v26)](https://b3.com.br/data/files/1A/46/F7/E4/6C66E91064BF82E9AC094EA8/Manual%20de%20Aprecamento%20-%20Opcoes%20v26.pdf) — Black-Scholes-Merton; rₙ = ln(1 + TPreₙ), "taxa de juro exponencial, em regime contínuo"; Tₙ = DUₙ/252.
- [Tesouro Nacional, Metodologia de Cálculo dos Títulos Públicos Federais](https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/26310_1658601/Metodologia%20de%20Calculo%20-%20290424.pdf) — LTN: PU = 1.000/(1 + taxa)^(du/252), expoente truncado na 14ª casa, PU na 6ª.
- [Hull, cap. 4, apresentação (O'Reilly, 10ª ed.)](https://www.oreilly.com/library/view/options-futures-and/9780136805199/xhtml/fileP7001013702000000000000000000D28.xhtml) — taxas contínuas "usadas extensivamente na análise de derivativos".
- [Lei nº 12.703/2012](https://modeloinicial.com.br/lei/L-12703-2012/lei-12703) — poupança a 0,5% ao mês enquanto a meta da Selic for superior a 8,5% ao ano.
- [Maor, e: The Story of a Number (sumário, De Gruyter)](https://www.degruyterbrill.com/document/doi/10.1515/9781400832347/html) e [edição da Record](https://www.record.com.br/en/products/e-a-historia-de-um-numero) — apêndice 2 sobre a existência do limite.

---

## Marcadores extraídos do rascunho

| # | Trecho (verbatim ou resumido) | Classificação | Resolução |
|---|---|---|---|
| 1 | Sem front-matter; H1 "Notas de um Professor — Frequência de Capitalização [draft v1]" | Estrutural | **Resolvido (etapa 0):** o autor confirmou Notas de um Professor (2026-11-09). |
| 2 | "Ficha de Saída (não publicar)": tabela com 8 campos | Estrutural | **Resolvido (etapa 2):** adotada em `02-estrutura.md`, campo 8 sem FIDC. |
| 3 | Título: "Capitalização Contínua vs. Composta" / "O Limite Matemático Que Explica as Duas" × "Quantas Cordas Cabem num Ano?" (Pergunta 1) | Estrutural | **Resolvido (etapa 1):** "Frequência de Capitalização"; subtítulo provisório no draft, troca decidida no gate (autor, 2026-11-09). |
| 4 | "No próximo texto, o FIDC (…), que prometi duas vezes" (fechamento) + campo 8 "aponta para o FIDC" | Nota de conteúdo | **Resolvido (etapa 0):** o FIDC foi cancelado. O autor decidiu cortar e fechar sem anunciar (2026-11-09). A etapa 4 aplica. |
| 5 | Pergunta 2: "devo uma correção" (texto anterior com três motores) — manter ou enquadrar como aprofundamento? | Nota de conteúdo | **Resolvido (etapa 1):** aprofundamento (autor, 2026-11-09). A etapa 4 aplicou (notas 2–4). |
| 6 | Pergunta 3: profundidade — demonstração do teto de 3 e exemplo de Black-Scholes no corpo, encurtados ou em nota? (decisão 3 do BACKWARDS_DESIGN) | Estrutural | **Resolvido (etapa 1):** ficam no corpo (autor, 2026-11-09). |
| 7 | Pergunta 4: "Uma linha sua: como o e apareceu para você na graduação em Matemática? Encaixaria depois da escada de Bernoulli." | Instrução de escrita | **Resolvido (etapa 1):** fica de fora (autor, 2026-11-09). |
| 8 | "[embedded content: cálculo próprio · taxa nominal de 14% ao ano; efetiva = (1 + 0,14/m)^m − 1; teto = e^0,14 − 1 · no post, entra como graf-01 (imagem exportada)]" | Sugestão de visual | Pendente (etapa 2/8): o conteúdo embutido não veio no arquivo e a etapa 8 reconstrói a partir da fórmula. |
| 9 | "> [graf-02] Ilustração: a linha quebrada de Bernoulli…" (1, 2, 4, 12 cordas + curva contínua) | Sugestão de visual | Pendente (etapa 2/8): conferir o tipo pelo critério (série real × diagrama). |
| 10 | "[VERIFICAR: ano da edição]" (Maor, Record) | Nota de conteúdo | Pendente (etapa 7). |
| 11 | Pendência: número da equação (1.5) no Manual de Opções da B3 na versão vigente (consultada v26, 26/05/2026) | Nota de conteúdo | Pendente (etapa 3/7). |
| 12 | Pendência: número da seção "Continuous compounding" no Hull, 11ª ed. | Nota de conteúdo | Pendente (etapa 7). O texto cita só "cap. 4". Conferir também contra o "capítulo 6" citado no du252. |
| 13 | Pendência: "Rende todo dia" ficou genérico, sem nomear instituição | Nota de conteúdo | Registro: manter genérico (nenhuma ação). |
| 14 | Ajustes à pauta: o vocabulário "exponencial" ambíguo; 252/360/365 como régua; a frase do MacTutor "primeira vez que um número foi definido por limite" fora; troca da ANBIMA pelo Tesouro; Hull 11ª ed.; nova âncora no manual da B3 | Nota de conteúdo | Registro: decisões do montador, todas incorporadas ao corpo. A etapa 7 confere as fontes. A sugestão de frase "O contínuo é o composto que nunca para de cortar o ano" (para a nota do Substack) vai ao gate. |
| 15 | Números: 1,01¹² = 1,1268; Bernoulli 2 / 2,25 / 2,44 / 2,61 / 2,69 / 2,7146; Δ diário→horário < 0,004; e^0,14 = 1,1503; ln 1,14 = 13,10%; nominais equivalentes 13,542 / 13,175 / 13,106 / 13,103; R$ 9.342,03 / 887,05 / 44,72; 1,14^(1/252) = 0,05201%; 0,14/252 = 0,05556% → 15,02%; BS: termo 114,00 × 115,03, call 16,72 × 17,24 (+3,1%), put 4,18 × 4,44 (−6,0%); 103 pb; poupança 6,17% / 5,99%; 26,21% e 1,2996; 68 pb | Nota de conteúdo | Pendente (etapa 7): recalcular tudo. |
| 16 | Fatos: Bernoulli 1683; Euler, "quase cinquenta anos depois", carta de 1731; B3 "conversão exponencial 252", capitalização só em dias úteis; DI1 cotado em efetiva base 252; manual de opções com rₙ = ln(1 + TPreₙ), Tₙ = DUₙ/252 e volatilidade por retorno log; Tesouro LTN com truncamento na 14ª e na 6ª casa; Lei 12.703/2012; Hull "extensively" | Nota de conteúdo | Pendente (etapa 3/7): conferir em fonte primária. |
| 17 | "Notas de processo (não publicar)" inteira | Nota de conteúdo | Registro: a seção não entra em `post.md`. As pendências estão nos itens 10–13, os visuais no 8–9 e as perguntas no 3 e no 5–7. As fontes alimentam a etapa 3. |
