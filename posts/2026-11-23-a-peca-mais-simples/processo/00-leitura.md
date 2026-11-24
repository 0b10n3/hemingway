# Etapa 0 — Leitura do rascunho

Fonte: `_arquivo/drafts/2026-11-23_A Peça Mais Simples_draft.md` (intocado; **ainda não
versionado**: está fora do git, nem em `main` nem nesta branch, e fica para o autor commitar em
`main`, escopo `arquivo`, como nos precedentes).

**Front-matter:** ausente. O arquivo abre com "1. A Peça Mais Simples — draft v1", "Nov 23, 2026 ·
@0b10n3" e um `## ` vazio (cabeçalho de exportação).

**Linha editorial:** o campo `linha_editorial` não existe em lugar nenhum do rascunho, então o
pipeline parou e perguntou. **O autor confirmou Notas de um Professor em 2026-11-23.** Daí: a
etapa 2 preenche a Ficha de Saída, a etapa 5 roda sem validação argumentativa e a 5a não roda.

**Título e slug:** título "A Peça Mais Simples", decidido pelo autor no rascunho (decisão 3:
"Seguir A Peça Mais Simples"). Subtítulo do rascunho: "Quem compra LTN não aposta na queda dos
juros. Aposta contra a curva." O autor pediu "pensar em outras propostas de subtítulos" (marcador
M5). Slug: `2026-11-23-a-peca-mais-simples`.

**Autoria:** como em `2026-11-18-cara-eu-ganho-coroa-eu-nao-perco`, o texto chega montado a
partir de pesquisa, com contas conferidas em Python antes do pipeline. A seção final "Notas de
revisão (não publicável)" fala com o autor ("Decisões editoriais para você validar") e o autor
respondeu três das seis decisões no próprio arquivo (1, 2 e 4; a 3 em parte). Há também
intervenções visíveis do autor no corpo: dois parágrafos em negrito que não seguem o padrão do
resto ("**O motivo é de justo. Conversa com o espírito professoral desta série.**" e "**O
*bootstrapping* volta quando as peças estiverem na mesa.**") e uma "NOTA PARA CLAUDE". Vale o
precedente: o texto é tratado como rascunho, a etapa 4 dá mais peso à voz e memória pessoal não se
inventa. Não há trecho de memória pessoal pedido.

**Continuidade de série:** o texto continua "Cara, eu ganho. Coroa, eu não perco."
(`posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco`, aprovado em 18/11), cujo fim prometeu o
*bootstrapping*. A abertura "rola" essa promessa e muda o rumo da série: um título público por
vez. Cita pelos apelidos os quatro textos anteriores (régua, motor, etiqueta, réplica) e promete,
para o próximo, a NTN-F.

**Natureza do rascunho:** chega completo. Título e subtítulo, abertura em dois tempos (promessa
rolada + caso de outubro de 2026), oito seções H2 e oito H3 de corpo, dois blocos LaTeX, um bloco
de planilha, duas tabelas, um placeholder de gráfico ("embedded content"), uma nota de
infográfico, exercício de transferência (CDB prefixado a 16%), CTA do Skill Check, ponte para a
NTN-F, aviso legal, quatro referências (duas com `[VERIFICAR]`) e "Notas de revisão (não
publicável)". Cerca de 3.000 palavras de prosa, pela estimativa do próprio rascunho (3.800
contando tabelas, fórmulas e referências).

**Limpeza aplicada na cópia:** `&#32;` removido (espaço no fim do parágrafo), `&#91;` → `[`,
`\[`/`\]` → `[`/`]`, `\*` → `*`. Nada mais mudou. O corpo abaixo é verbatim.

---

1. A Peça Mais Simples — draft v1

Nov 23, 2026 · @0b10n3

## 

---

**Título:** A Peça Mais Simples

**Subtítulo:** Quem compra LTN não aposta na queda dos juros. Aposta contra a curva.

---

No fim do último texto, prometi construir a curva de juros vértice por vértice, com uma técnica de nome curioso: *bootstrapping*.

O nome vem de uma façanha impossível, a de se erguer do chão puxando as alças da própria bota. Na versão alemã da história, é o Barão de Münchhausen saindo de um pântano puxado pelo próprio cabelo.

Promessa é dívida. Esta, eu vou rolar: faço com ela o que o Tesouro faz com os títulos que vencem, pago a antiga emitindo uma nova, com prazo mais longo. (O barão pode esperar no pântano mais umas semanas.)

**O motivo é de justo. Conversa com o espírito professoral desta série.**

O *bootstrapping* constrói a curva a partir dos títulos. Só que a LTN (Letra do Tesouro Nacional, o título público prefixado sem cupom) apareceu em quatro textos seguidos desta série, como cobaia da régua, do motor, da etiqueta e da réplica, e nunca foi apresentada.

Nem ela, nem as irmãs.

Então a série muda de rumo. A partir de hoje, um título público por vez, do mais simples ao que tem mais engrenagens.

**O *bootstrapping* volta quando as peças estiverem na mesa.**

E começa com uma boa notícia: para precificar a LTN, você já tem a caixa de ferramentas inteira. Falta compreender melhor o que se está comprando.

O mercado acabou de dar uma aula sobre isso.

Em 8 de outubro de 2026, o Tesouro Nacional vendeu R$ 27,86 bilhões em LTN num único leilão, **o maior volume em prefixados desde dezembro de 2020**. As taxas ficaram perto de 12,5% ao ano, abaixo da Selic (a taxa básica de juros), que estava em 13,75%.

Em 13 de outubro, o Tesouro Prefixado 2029, a LTN que vence em 1º de janeiro de 2029 e que a pessoa física compra no Tesouro Direto, custava R$ 773,74, a 12,40% ao ano.

Em 25 de outubro, Lula foi reeleito.

No pregão seguinte, os juros futuros dispararam, o Tesouro Direto suspendeu as negociações mais de uma vez, e **o Tesouro cancelou o leilão de prefixados da semana para, no lugar dele, recomprar títulos**.

Em 17 de novembro, o mesmo Prefixado 2029 custava R$ 746,00, a 14,98% ao ano. Quem comprou em 13 de outubro via 3,6% a menos na tela.

A Selic, nesse meio-tempo, não se mexeu.

O que, exatamente, se compra quando se compra uma LTN?

E, se a Selic ficou parada, o que derrubou o preço?

## Prefixado para quem acha que o juro vai cair

Uma conversa que corre o mercado, sobre as LTN e títulos preíxados, é mais ou menos esta.

O prefixado é para quem acha que os juros vão cair.  O Tesouro Selic, para quem acha que vão subir. E o preço da LTN segue o Copom (o Comitê de Política Monetária, que define a meta da Selic): sobe quando ele corta, cai quando ele aperta.

* NOTA PARA CLAUDE - Aqui podemos fazer um pesquis aprofundada sobre esse ponto do copom e altas e baixas na taxa da LTN, e a partir desse conteudo incluir um infográfico.

Tem um pedaço de verdade aí.

Quando a taxa da LTN cai, o preço sobe. E, se a Selic cair muito, quem travou uma taxa prefixada ganha de quem ficou no pós-fixado.

Mas os fatos de outubro não se alinham muito bem com essa verão. Entre 13 de outubro e 17 de novembro, o Copom se reuniu uma vez, não mudou nada, e o Prefixado 2029 perdeu 3,6%.

[embedded content: Tesouro Nacional, taxas de compra do Tesouro Direto, compiladas por InvestNews e EuQueroInvestir; Selic: Copom. 11 cotações entre 9/10 e 17/11/2026.]

E tem o outro lado.

Em 8 de outubro, quem comprou LTN a 12,5% com a Selic em 13,75% não estava apostando que os juros iam cair. Estava pagando por isso: a queda já estava no preço.

**Quem compra LTN não aposta na queda dos juros. Aposta contra a curva.**

A curva é a fila de taxas prefixadas, uma por prazo, que o mercado negocia todo dia. A LTN ganha quando a Selic de verdade, dia após dia até o vencimento, fica abaixo do que a curva cobrava no dia da compra. Perde quando fica acima.

No restante do texto, procuramos dar mais sentido a este  último pensamento.

## Cinco títulos, um devedor

Título público federal é a dívida que o Tesouro Nacional vende para financiar o governo. A emissão é autorizada pela Lei nº 10.179/2001, e as características de cada papel estão no Decreto nº 12.814, de janeiro de 2026. Todos ficam registrados no Selic (Sistema Especial de Liquidação e de Custódia, operado pelo Banco Central), onde a propriedade e os pagamentos são controlados.

Cada título responde a quatro perguntas: o que corrige o valor (o indexador), quando o dinheiro volta (só no fim ou em cupons pelo caminho), quanto vale na face e quando vence. Nos leilões de hoje, as respostas formam cinco papeis:

| Título | Nome no Tesouro Direto | O que remunera | Cupom |
| --- | --- | --- | --- |
| LFT | Tesouro Selic | Selic acumulada | não tem |
| LTN | Tesouro Prefixado | taxa fixa, pelo deságio | não tem |
| NTN-F | Tesouro Prefixado com Juros Semestrais | taxa fixa | 10% ao ano, em duas parcelas |
| NTN-B Principal | Tesouro IPCA+ | IPCA + taxa fixa | não tem |
| NTN-B | Tesouro IPCA+ com Juros Semestrais | IPCA + taxa fixa | 6% ao ano, em duas parcelas |

O devedor é o mesmo nos cinco: o Tesouro, que deve em reais, a moeda que o próprio Estado emite. Não há FGC (o Fundo Garantidor de Créditos, o seguro dos depósitos bancários) porque não há banco no meio.

O que muda de um papel para outro não é o risco de crédito. É o risco de juros que você leva para casa.

A LTN é o mais seco dos cinco. Pelo art. 2º do decreto, o valor nominal é múltiplo de R$ 1.000, o rendimento é definido pelo deságio (o desconto sobre o valor de face) e o resgate é pelo valor nominal, no vencimento. Nenhum pagamento no caminho. Você paga menos de R$ 1.000 hoje e recebe R$ 1.000 numa data marcada.

As datas são sempre o primeiro dia de janeiro, abril, julho ou outubro. Os prazos em oferta vão de alguns meses a pouco mais de cinco anos: o leilão de 8 de outubro vendeu vencimentos de 2028, 2029 e 2032.

O resto da anatomia cabe em três gavetas:

- **Tributação:** Imposto de Renda pela tabela regressiva da Lei nº 11.033/2004, de 22,5% (até 180 dias) a 15% (acima de 720 dias), e IOF sobre o rendimento nos primeiros 30 dias. Investidor não residente é isento de IR desde a Lei nº 11.312/2006.
- **Liquidez:** no mercado secundário de balcão, os prefixados giram dezenas de bilhões de reais por dia (R$ 42,9 bilhões em 5 de outubro, segundo o Banco Central). No Tesouro Direto, o próprio Tesouro recompra o título todo dia útil, a preço de mercado.
- **Risco:** o de crédito é o menor do país. O de preço é todo seu.

Até aqui, é o que a página do Tesouro Direto conta.

A partir daqui, a conta.

## Uma linha, quatro textos

O preço de uma LTN cabe numa linha:

```latex
PU = \frac{1000}{(1 + i)^{du/252}}
```

em que PU é o preço unitário, i é a taxa anual e du é o número de dias úteis até o vencimento.

Nenhum pedaço dessa linha é novo para quem acompanhou a série:

- **du/252 é a régua** (“Você está contando os dias errado”). Dias úteis entre a liquidação, inclusive, e o vencimento, exclusive, sobre 252.
- **A potência é o motor** (“A Corda e o Arco”). Juro composto: o juro de cada dia vira saldo e passa a render.
- **i é a etiqueta** (“Frequência de Capitalização”). Taxa efetiva ao ano, base 252. Quem divide os 14,98% por 252 erra o preço.
- **A fração inteira é a réplica** (“Cara, eu ganho. Coroa, eu não perco.”). O termo 1/(1 + i)^(du/252) é o fator de desconto daquele prazo, o preço hoje de R$ 1 entregue no vencimento.

O último item é o que dá o título a este texto. A LTN é o fator de desconto vendido em lotes de R$ 1.000. No texto anterior, uma NTN-F foi montada com três LTNs. Qualquer fluxo prefixado se monta assim. A LTN é o átomo da curva prefixada: tudo o mais é molécula.

### O preço do Tesouro

Repare na conta com um número real. Em 17 de novembro, o Tesouro Direto vendia o Prefixado 2029 a 14,98% ao ano. A compra liquida no dia útil seguinte, 18 de novembro, e dali até 1º de janeiro de 2029 são 529 dias úteis no calendário da ANBIMA.

A metodologia do Tesouro trunca o expoente na 14ª casa decimal e o preço na 6ª. O expoente é 529/252 = 2,09920634920634. O fator de 1,1498 elevado a ele é 1,340475. E o preço:

```latex
PU = \frac{1000}{1{,}1498^{\,2{,}09920634920634}} = 746{,}004202
```

A tela do Tesouro Direto mostrava R$ 746,00. Na planilha, com as datas e a lista de feriados da ANBIMA:

```
du:                    =DIATRABALHOTOTAL(liquidação; vencimento-1; feriados)
PU a partir da taxa:   =TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6)
Taxa a partir do PU:   =(1000/PU)^(252/du)-1
```

A terceira linha faz o caminho de volta. Com o preço de 13 de outubro, R$ 773,741961, e 553 dias úteis, ela devolve os 12,40% da abertura.

### Quanto o preço anda

Numa LTN, a *duration* (o prazo médio dos fluxos, ponderado pelo valor presente de cada um) é o próprio prazo, porque só há um fluxo: 529/252, ou 2,10 anos. Dividida por 1 + i, vira a *duration* modificada, 1,83, a variação percentual do preço para cada ponto percentual de taxa.

Na prática, a 14,98%:

- cada ponto-base (um centésimo de ponto percentual) vale R$ 0,14 por título, ou R$ 182,57 para cada R$ 1 milhão aplicado (o DV01, na sigla da mesa);
- um ponto percentual a mais na taxa tira 1,80% do preço; um a menos põe 1,85%. A diferença é a convexidade, a mesma curvatura do arco.

Com isso, dá para abrir o prejuízo da abertura em duas partes, em cálculo próprio. De 13 de outubro a 17 de novembro passaram 24 dias úteis. Se a taxa tivesse ficado em 12,40%, o título teria andado 1,12% em direção aos R$ 1.000: é o carregamento. A alta de 2,58 pontos na taxa tirou 4,65%. Compostas (1,0112 × 0,9535), as duas dão os −3,58% da tela.

No mesmo período, o Tesouro Selic rendeu cerca de 1,2%.

## Quem vende, quem compra, quem empresta

Toda LTN tem alguém do outro lado do balcão. Na emissão, é o Tesouro. E o problema que ele resolve com ela não é o seu.

### O Tesouro trava o custo

Para o Tesouro, emitir é escolher entre custo e risco. A LFT costuma sair mais barata, mas repassa cada decisão do Copom para a conta de juros da dívida: se a Selic sobe, a dívida inteira atrelada a ela fica mais cara no dia seguinte. A LTN cobra prêmio por isso. Em troca, o Tesouro sabe hoje quanto vai pagar em 2029.

Por isso a fatia de prefixados é lida como um indicador de qualidade da dívida. O Plano Anual de Financiamento (PAF, o documento em que o Tesouro fixa as metas da dívida para o ano), revisado em 26 de agosto de 2026, mira de 20% a 24% de prefixados na Dívida Pública Federal, e de 49% a 53% de títulos atrelados à Selic. Em setembro, os prefixados eram 21,14%.

O caminho até o mercado é o leilão. LTN e NTN-F saem às quintas-feiras; LFT e NTN-B, às terças. Quem dá lance são instituições com acesso ao Selic, com papel central dos *dealers*: até 12 bancos e corretoras credenciados pelo Tesouro, pela Portaria STN/MF nº 182/2024, que se comprometem a comprar no leilão e a dar liquidez no secundário. Em troca, só eles entram na segunda rodada, logo depois do leilão, ao mesmo preço.

O Tesouro também atua quando o mercado trava. Foi o que fez em outubro, e os números mostram os dois lados do balcão com uma nitidez rara:

- em 8 de outubro, vendeu NTN-F de 2031 a 12,61% ao ano, no mesmo leilão das LTNs a 12,5%;
- em 26 de outubro, cancelou o leilão da semana e recomprou 5 milhões de NTN-F de 2031 a 15,79%, num total de cerca de R$ 7,1 bilhões em prefixados.

O mesmo papel, vendido caro e recomprado barato em 18 dias. Para o Tesouro, as duas pontas foram boas. Para quem comprou em 8 de outubro e vendeu no dia 26, não.

### O Banco Central empresta com ela

O Banco Central não emite títulos próprios desde 2002, por força do art. 34 da Lei de Responsabilidade Fiscal. Para tirar ou pôr dinheiro no sistema, usa os títulos do Tesouro que tem em carteira como lastro de operações compromissadas (vendas com recompra marcada, que funcionam como empréstimo garantido).

Na semana de 5 a 9 de outubro, essas operações de um dia somaram, em média, R$ 885,7 bilhões por dia. Nas de prazo mais longo, o lastro oferecido foi LFT, LTN, NTN-B e NTN-F.

### Os bancos carregam, garantem e protegem

Nos bancos, a LTN aparece em três gavetas da tesouraria:

1. **Posição na curva.** Um banco que empresta prefixado (consignado, veículo, cartão parcelado) e capta em CDB atrelado ao CDI já carrega, no balanço, a mesma aposta de quem compra LTN. A mesa decide quanto dessa aposta manter e quanto neutralizar, com LTN ou com DI futuro (o contrato da B3 que troca uma taxa prefixada pelo CDI do período).
2. **Colchão de liquidez.** Título público federal é ativo de primeira linha no LCR (o índice de Basileia III que exige ativos líquidos para atravessar 30 dias de estresse).
3. **Garantia.** É o lastro mais aceito no interbancário, em compromissadas e em chamadas de margem.

O resultado aparece em quem detém a dívida interna. Em setembro de 2026, as instituições financeiras tinham 31,33% do estoque; os fundos de investimento, 22,93%; os fundos de pensão, 22,41%; os não residentes, 9,58%. A pessoa física do Tesouro Direto está no grupo dos 13,76% restantes.

## A aposta escondida na taxa

Para ver contra o que a LTN aposta, compare com a vizinha de prateleira: a LFT, o Tesouro Selic.

Quem fica na LFT recebe a Selic de cada dia até o vencimento, seja ela qual for. Quem compra a LTN e carrega até o fim recebe a taxa travada na compra. Deixando de lado o pequeno deságio da LFT, a regra é uma só:

> A LTN ganha da LFT se a Selic acumulada até o vencimento ficar abaixo de (1 + i) elevado a du/252. Perde se ficar acima.

Com o Prefixado 2029 a 14,98%, o empate pede uma Selic média perto de 15% ao ano até 2029. Hoje ela está em 13,75%. E a mediana do Boletim Focus (a pesquisa semanal do Banco Central com as projeções do mercado) de 16 de novembro aponta 13,75% no fim de 2026, 12,75% no fim de 2027 e 11% no fim de 2028.

Para medir a distância, três cenários para R$ 10 mil aplicados em 17 de novembro, até 1º de janeiro de 2029, em valores brutos e cálculo próprio:

| Cenário para a Selic | No Tesouro Selic | No Prefixado 2029 |
| --- | --- | --- |
| Segue o Focus (trajetória interpolada entre os fins de ano) | R$ 12.818 | R$ 13.405 |
| Fica parada em 13,75% | R$ 13.081 | R$ 13.405 |
| Média de 16% ao ano | R$ 13.631 | R$ 13.405 |

A última coluna não muda. É isso que *prefixado* quer dizer: o número foi escrito no dia da compra.

Agora repare na primeira linha. Se o Focus estiver certo, a LTN paga cerca de 2,5 pontos percentuais por ano acima da Selic média esperada. Ninguém deixa esse dinheiro na mesa por distração.

A diferença tem nome: prêmio de prazo, o que o mercado cobra para travar dinheiro por dois anos numa taxa fixa, num país em que as contas públicas preocupam e a mediana pode errar para cima. A taxa da LTN não é a previsão da Selic. É a previsão mais o preço do seguro contra ela estar errada.

Com isso, outubro se explica sem o Copom. Em 8 de outubro, a curva cobrava pouco prêmio: LTNs de 2028 e 2029 a 12,5%, menos de um ponto acima do que o Focus da época esperava para a Selic (12% no fim de 2027, 10,5% no fim de 2028). A eleição não mudou a Selic. Mudou o prêmio. E a LTN, que é só um fator de desconto, refez o preço na hora.

É esse o ponto cego da versão que circula. O preço da LTN não responde à Selic de hoje. Responde à curva, que junta o que se espera da Selic de amanhã e quanto se cobra pela dúvida.

## Três trabalhos na carteira

Na carteira de quem investe, a LTN serve para três coisas diferentes. Cada uma usa uma parte do que vimos.

### Pagar uma conta com data

O uso mais limpo é casar o título com um compromisso de valor e data conhecidos. Pense em R$ 100 mil para a entrada de um imóvel em janeiro de 2029.

Em 17 de novembro, 100 títulos do Prefixado 2029 custavam R$ 74.600,42. Carregados até o fim, viram R$ 100 mil brutos, qualquer que seja o caminho da curva até lá. Quem comprou em 13 de outubro e segurar até 2029 recebe os 12,40% contratados. Os −3,6% de novembro só viram prejuízo para quem vende.

O valor líquido é menor. Como o prazo passa de 720 dias, o IR é de 15% sobre o ganho: cada título entrega R$ 961,90, uma taxa líquida de 12,87% ao ano (cálculo próprio). Saem ainda a custódia da B3, de 0,20% ao ano, e a taxa da instituição, se houver.

Dois cuidados. A data: a LTN só vence em quatro dias por ano, e um compromisso em março obriga a escolher entre vender antes (com risco de preço) e reinvestir por dois meses. E o valor: os R$ 100 mil são nominais. Se o preço do que você vai comprar anda com a inflação, o título que casa com ele é outro, e ele tem texto próprio nesta série.

### Travar uma taxa

O segundo uso é trocar incerteza por um número. No Tesouro Selic, o dinheiro rende o que a Selic render: se ela cair, o rendimento cai junto, e o reinvestimento sai mais pobre. Na LTN, o rendimento até o vencimento está escrito.

Não é um almoço grátis. Você troca o risco de reinvestir mal pelo risco de ter travado abaixo do que a Selic vai pagar, a terceira linha da tabela acima.

### Tomar posição na curva

O terceiro uso é comprar para vender antes do vencimento, apostando que a taxa vai cair. Aí a LTN deixa de ser compromisso e vira posição, e a ferramenta é a *duration*. Uma posição de R$ 100 mil no Prefixado 2029 ganha ou perde cerca de R$ 1.800 a cada ponto percentual de taxa.

O erro mais caro mistura os dois primeiros usos com o terceiro: guardar em LTN o dinheiro que pode ser preciso a qualquer momento, como a reserva de emergência. A recompra diária do Tesouro garante que existe comprador. Não garante o preço.

Voltando à pergunta da tabela: no dia em que você compra, a decisão não é se os juros vão cair. É se você aceita o preço que a curva cobra por trocar a Selic de cada dia por um número fixo, até uma data que cabe nos seus planos.

## De volta a outubro

Com o que vimos, dá para reler o caso da abertura.

O Tesouro vendeu R$ 27,86 bilhões em LTN a 12,5% porque era o que a curva pagava. Travou dívida barata por dois anos, e no fim do mês ainda recomprou NTN-F com desconto. Fez o serviço dele.

Quem comprou o Prefixado 2029 a 12,40% em 13 de outubro apostou que a Selic média até 2029 ficaria abaixo de 12,40%. Com a curva daquele dia, era uma aposta com pouco prêmio. A eleição mudou o prêmio, a aposta piorou, e o preço mostrou isso no dia seguinte. Esse é o trabalho do preço.

Os −3,6% não são o resultado da aposta. São o preço de sair dela hoje. O resultado só sai em 2029, quando der para comparar os 12,40% com a Selic que de fato aconteceu.

## A peça mais simples

A LTN é uma promessa de R$ 1.000 numa data, vendida com desconto. O desconto é o fator de desconto daquele prazo, e por isso ela é o átomo de toda a curva prefixada. O preço dela não segue a Selic de hoje: segue a curva, que soma o que se espera da Selic e quanto se cobra pela dúvida.

**Quem compra LTN não aposta na queda dos juros. Aposta contra a curva.**

Se o texto funcionou, você consegue analisar sozinho um produto vizinho. Um banco médio oferece um CDB prefixado com vencimento em 1º de janeiro de 2029, a 16% ao ano, no mesmo 17 de novembro em que a LTN pagava 14,98%. Quanto custa, na mesma régua, R$ 1.000 de face desse CDB? Que parte do ponto percentual a mais é aposta na curva, e que parte paga outra coisa? E o que muda se você precisar sair antes?

Precificar títulos de renda fixa e medir o risco de juros fazem parte de duas dimensões do [Syntaxis Skill Check](https://skill.syntaxis.com.br/), a de mercados e produtos e a de matemática financeira. É um diagnóstico gratuito, que compara o seu perfil com o que o mercado espera para o próximo degrau da carreira.

No próximo texto, a irmã de cupom: a NTN-F, o prefixado que paga 10% ao ano em duas parcelas. Já sabemos que ela é um pacote de LTNs. Falta ver o que a taxa que o mercado cota para ela, a TIR, esconde sobre cada peça, e por que isso pesa justamente em semanas como as de outubro. Com ela na mesa, o barão finalmente sai do pântano.

Se este texto ajudou você a ler uma LTN pelo que ela aposta, encaminhe para quem ainda compra prefixado “porque a Selic vai cair”.

---

*Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira.*

## Para continuar aprendendo

- Bruce Tuckman e Angel Serrat, *Fixed Income Securities: Tools for Today’s Markets*, 4ª ed. (Wiley, 2022). Os capítulos sobre fatores de desconto e sobre DV01 e *duration* são a versão de mesa deste texto, com os títulos do Tesouro americano no lugar da LTN.
- José Roberto Securato (coord.), *Cálculo Financeiro das Tesourarias: Bancos e Empresas* (Saint Paul) [VERIFICAR: edição e ano]. O manual brasileiro de mesa: LTN, LFT e NTN com as convenções locais, du/252 e taxa over incluídas.
- Tesouro Nacional, [*Metodologia de Cálculo dos Títulos Públicos Federais Ofertados nos Leilões Primários*](https://www.tesourotransparente.gov.br/publicacoes/methodology-for-calculating-federal-government-bonds-offered-in-primary-auctions). A fonte das fórmulas e dos truncamentos usados aqui, título por título.
- Tesouro Nacional, *Plano Anual de Financiamento 2026* (revisão de agosto) [VERIFICAR: link]. Onde o emissor explica, com metas, por que quer mais ou menos prefixados na dívida: o lado de lá do balcão, por escrito.

## Notas de revisão (não publicável)

**Insumos.** A pesquisa de pauta não veio anexada à mensagem. O texto saiu de pesquisa própria (Tesouro, Demab/BCB, Copom, Focus, cotações do Tesouro Direto) e da estrutura dos oito movimentos. Se a pauta existe, ela pode mudar ângulo e exemplos.

**Conta conferida em Python, com o calendário ANBIMA (pacote bizdays).** A fórmula com truncamento reproduz ao centavo seis preços publicados do Prefixado 2029 (13/10, 29/10, 4/11, 9/11, 12/11 e 17/11), sempre com liquidação em D+1, como diz a documentação do Tesouro Transparente. Cálculos próprios no texto: decomposição carregamento × choque, *duration* e DV01, cenários LTN × LFT, taxa líquida de IR, rendimento do Tesouro Selic no período (Selic over de 13,65%).

**Premissas a declarar ou mudar:**

- Cenário “Focus”: Selic interpolada em linha reta entre os fins de ano (13,75% → 12,75% → 11%), CDI = meta − 0,10. Selic média resultante: 12,53% ao ano.
- Preços do Tesouro Direto são de compra. Quem vende recebe pela taxa de venda, um pouco maior, então os −3,6% são aproximados.
- Os cenários ignoram o deságio da LFT (Selic + 0,11% em novembro).

**[VERIFICAR] antes de publicar:**

- Edição e ano do Securato; link do PAF 2026 revisado.
- “O Tesouro Direto suspendeu as negociações mais de uma vez” em 26/10: duas fontes falam em suspensões temporárias, sem horário oficial.
- “Maior volume desde dezembro de 2020” se refere aos R$ 33,3 bilhões em prefixados (LTN + NTN-F) de 8/10; os R$ 27,86 bilhões são só LTN. A frase da abertura está escrita assim de propósito.
- Portaria dos *dealers*: usei a STN/MF nº 182/2024 (até 12 instituições). Confirmar se segue vigente.
- O Focus do início de outubro (12% em 2027, 10,5% em 2028) veio de matéria de 13/10; conferir no boletim de 5/10.

**Decisões editoriais para você validar:**

1. Abertura em dois tempos: a promessa rolada (piada da rolagem da dívida + barão) e o caso de outubro, que pede o fechamento do loop no fim. APROVADO
2. Um bullet do pedido chegou vazio (“Apresentar”). Tratei como a família dos títulos públicos, na tabela da anatomia. Se era outra coisa, me diga. APROVADO
3. Título “O Átomo da Curva”. Alternativas: “A Peça Mais Simples”, “R$ 1.000 numa data”, “A Selic ficou parada”. Seguir A Peça Mais Simples . Pensar em outras propostas de subtítulos.
4. Em 2024 você publicou “Tesouro Prefixado: o guia completo”. Não citei; dá para linkar como a versão para quem está começando. Não referenciar aquele texto.
5. O texto tem cerca de 3.000 palavras, na faixa dos últimos. Candidatos a corte, se precisar: a gaveta “Garantia” dos bancos e a frase sobre detentores da dívida.
6. Teste de transferência: CDB prefixado a 16% (o leitor precisa chegar a cerca de R$ 732 por R$ 1.000 de face e separar curva de crédito/liquidez). A resposta pode virar Note de D+2.

---

## Marcadores extraídos do rascunho

| # | Marcador (verbatim ou resumo fiel) | Padrão | Etapa | Resolução |
|---|---|---|---|---|
| M1 | Ausência de `linha_editorial` | Estrutural | 0 | **Resolvido:** autor confirmou Notas de um Professor (2026-11-23). |
| M2 | "* NOTA PARA CLAUDE - Aqui podemos fazer um pesquis aprofundada sobre esse ponto do copom e altas e baixas na taxa da LTN, e a partir desse conteudo incluir um infográfico." (seção "Prefixado para quem acha que o juro vai cair") | Sugestão de visual (infográfico), com pedido de pesquisa | 3 (pesquisa) → 2/8 (tipo e peça) | |
| M3 | "[embedded content: Tesouro Nacional, taxas de compra do Tesouro Direto, compiladas por InvestNews e EuQueroInvestir; Selic: Copom. 11 cotações entre 9/10 e 17/11/2026.]" | Sugestão de visual (gráfico com série real) | 2 (tipo) → 3 (dados) → 8 | |
| M4 | "Decisões editoriais 1: Abertura em dois tempos … APROVADO" | Estrutural | 1 | |
| M5 | "Decisões editoriais 3: … Seguir A Peça Mais Simples . Pensar em outras propostas de subtítulos." | Instrução de escrita (título resolvido; subtítulo pede propostas) | 1 (título) → 4 (propostas de subtítulo) | |
| M6 | "Decisões editoriais 2: Um bullet do pedido chegou vazio (“Apresentar”). Tratei como a família dos títulos públicos … APROVADO" | Estrutural | 1 | |
| M7 | "Decisões editoriais 4: … “Tesouro Prefixado: o guia completo”. … Não referenciar aquele texto." | Nota de conteúdo (restrição: não citar nem linkar) | 1; vale também para a 9a | |
| M8 | "Decisões editoriais 5: … cerca de 3.000 palavras … Candidatos a corte, se precisar: a gaveta “Garantia” dos bancos e a frase sobre detentores da dívida." (sem resposta do autor) | Nota de conteúdo (corte opcional) | 1 → 5 | |
| M9 | "Decisões editoriais 6: Teste de transferência: CDB prefixado a 16% (… cerca de R$ 732 …). A resposta pode virar Note de D+2." (sem resposta do autor) | Nota de conteúdo | 2 (Ficha) → 7 (conta); a Note é da distribuição | |
| M10 | Securato, *Cálculo Financeiro das Tesourarias* "[VERIFICAR: edição e ano]" | Nota de conteúdo | 3 → 7 | |
| M11 | PAF 2026 revisado "[VERIFICAR: link]" | Nota de conteúdo | 3 → 7 | |
| M12 | "[VERIFICAR] … “O Tesouro Direto suspendeu as negociações mais de uma vez” em 26/10: duas fontes falam em suspensões temporárias, sem horário oficial." | Nota de conteúdo | 3 → 7 | |
| M13 | "[VERIFICAR] … “Maior volume desde dezembro de 2020” se refere aos R$ 33,3 bilhões em prefixados (LTN + NTN-F) de 8/10; os R$ 27,86 bilhões são só LTN. A frase da abertura está escrita assim de propósito." | Nota de conteúdo | 3 → 7 | |
| M14 | "[VERIFICAR] … Portaria dos *dealers*: usei a STN/MF nº 182/2024 (até 12 instituições). Confirmar se segue vigente." | Nota de conteúdo | 3 → 7 | |
| M15 | "[VERIFICAR] … O Focus do início de outubro (12% em 2027, 10,5% em 2028) veio de matéria de 13/10; conferir no boletim de 5/10." | Nota de conteúdo | 3 → 7 | |
| M16 | "Premissas a declarar ou mudar": cenário Focus interpolado (Selic média 12,53%, CDI = meta − 0,10); preços de compra (os −3,6% são aproximados); cenários ignoram o deságio da LFT (Selic + 0,11%) | Nota de conteúdo | 7 (recalcular) → gate | |
| M17 | "Insumos. A pesquisa de pauta não veio anexada à mensagem. … Se a pauta existe, ela pode mudar ângulo e exemplos." | Nota de conteúdo | 1 | |
| M18 | "Conta conferida em Python, com o calendário ANBIMA (pacote bizdays)" + lista de cálculos próprios | Nota de conteúdo | 7 (recalcular tudo) | |
| M19 | Os dois parágrafos em negrito do autor na abertura ("**O motivo é de justo. …**", "**O *bootstrapping* volta …**") | Nota de conteúdo (intervenção do autor; preservar o sentido) | 4 e 6 | |
| M20 | Aviso legal no corpo do rascunho; "Para continuar aprendendo" depois dele | Nota de conteúdo | 9 (aviso de `docs/AVISO_LEGAL.md`, no fim) | |
