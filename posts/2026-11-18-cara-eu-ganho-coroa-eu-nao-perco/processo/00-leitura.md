# Etapa 0 — Leitura do rascunho

Fonte: `_arquivo/drafts/2026-11-18_Notas de um Professor — Cara, eu ganho. Coroa, eu não perco.md` (intocado; **ainda não versionado**: está fora do git, nem em `main` nem nesta
branch, e fica para o autor commitar em `main`, escopo `arquivo`, como nos dois precedentes).

**Front-matter:** ausente. O arquivo abre com o H1 "# Notas de um Professor — Cara, eu ganho.
Coroa, eu não perco. [draft v1]" e "Nov 18, 2026 · @0b10n3" (cabeçalho de exportação).

**Linha editorial:** lida, não inferida. O rascunho traz o campo literal, numa linha da Ficha:
`linha_editorial: Notas de um Professor`, e o H1 repete a linha. O valor é um dos dois válidos,
então o pipeline segue sem parar. Diferente dos precedentes de 09/11 e 13/11, em que o campo não
existia em lugar nenhum. A etapa 2 completa a Ficha de Saída, a etapa 5 roda sem validação
argumentativa e a 5a não roda. Se o autor quiser outra linha, é decisão do gate.

**Título e slug:** título "Cara, eu ganho. Coroa, eu não perco.", subtítulo "Preço não é opinião:
é o custo de montar o mesmo fluxo." O autor já decidiu no rascunho: "Seguir com os títulos
atuais". Slug pelo título: `2026-11-18-cara-eu-ganho-coroa-eu-nao-perco`. As "Notas para o pipeline" pedem salvar o draft como
`_arquivo/drafts/AAAA-MM-DD_nao-arbitragem.md`. Não se aplica: o arquivo já está em `_arquivo/`
com outro nome, e `_arquivo/` não se renomeia.

**Autoria:** o texto foi montado a partir de uma pauta, com pesquisa e contas feitas antes do
pipeline. A seção final "Notas de revisão (não publicar)" fala do texto na terceira pessoa ("O draft
segue a pauta…"), traz "Decisões para você" e as contas conferidas em Python. O autor respondeu
quatro das cinco decisões no próprio rascunho. Vale o precedente de `2026-11-02-a-barriga-da-curva`
e `2026-11-09-frequencia-de-capitalizacao`: o texto é tratado como rascunho, a etapa 4 dá mais
peso à voz e memória pessoal não se inventa. Não há trecho de memória pessoal pedido: a
primeira pessoa só costura a série ("deixei uma fórmula", "Contei essa história em").

**Continuidade de série:** o texto continua "Frequência de Capitalização"
(`posts/2026-11-09-frequencia-de-capitalizacao`, aprovado em 09/11), cujo fim deixa a fórmula de
planilha do PU da LTN e diz que "Com a régua, o motor e agora a etiqueta, o expoente du/252 desta
série está explicado de ponta a ponta." A abertura do rascunho retoma as duas coisas.

**Natureza do rascunho:** chega completo. Ficha de Saída em forma curta (só a competência e uma
linha de metadados, sem a tabela de 8 campos), título e subtítulo, abertura com a moeda e a
LTN × principal de NTN-F 2029, sete seções H2 e quatro H3 de corpo, dois blocos LaTeX mais um
inline em bloco, quatro tabelas, um bloco de planilha, uma menção a Black-Scholes, um CTA do
Skill Check, exercício de transferência (NTN-B), ponte para o *bootstrapping*, quatro referências
e o aviso legal. Fecha com "Notas de revisão (não publicar)". Cerca de 2.900 palavras de corpo.

**Limpeza aplicada na cópia:** `\[`/`\]` → `[`/`]`, `\_` → `_`. Nada mais mudou. O corpo
abaixo é verbatim.

---

# Notas de um Professor — Cara, eu ganho. Coroa, eu não perco. [draft v1]

Nov 18, 2026 · @0b10n3

## Ficha de Saída (não publicar)

Com este texto, o leitor deve conseguir montar a carteira de títulos zero-cupom que replica um título com cupom, precificá-lo pela Lei do Preço Único e dizer se uma operação é arbitragem ou aposta de correlação.

`linha_editorial: Notas de um Professor` · voz: ensaística em registro técnico · tipo (BACKWARDS_DESIGN §4.2): conceito de finanças · abertura: modo B (moldura conceitual + enigma)

## Cara, eu ganho. Coroa, eu não perco.

**Subtítulo:** Preço não é opinião: é o custo de montar o mesmo fluxo.

---

No fim do [último texto](https://syntaxis.substack.com/p/frequencia-de-capitalizacao), deixei uma fórmula de planilha para replicar o preço de uma LTN (Letra do Tesouro Nacional, o título público prefixado sem cupom). Com ela, a série de convenções fechou: a régua, o motor e a etiqueta.

A palavra que importa hoje já estava naquela linha: *replicar*.

Comece por uma aposta. Uma moeda é lançada. Se der cara, você ganha. Se der coroa, você não perde nada. E não paga para entrar.

Ninguém recusaria. É o ganha-ganha mais puro que existe, e tem um detalhe: é ganha-ganha de uma pessoa só.

No mercado, essa aposta tem nome. É a **arbitragem**. E boa parte da teoria de preços foi construída sobre a ideia de que ela não dura.

Agora, um caso concreto. Em 1º de janeiro de 2029, o Tesouro Nacional vai pagar R$ 1.000 a quem tiver uma LTN 2029. No mesmo dia, vai pagar R$ 1.048,81 a quem tiver uma NTN-F 2029 (Nota do Tesouro Nacional, série F: o prefixado que paga cupom a cada seis meses). São o último cupom e o principal.

Na custódia dos títulos públicos, a NTN-F pode ser desmembrada: o principal e cada cupom passam a circular como títulos separados. [VERIFICAR: norma vigente do desmembramento; a referência mais antiga encontrada é o Comunicado Selic nº 7.588, de 2000. A Mais Retorno lista emissões de “NTN-F somente cupons” em 2026.]

Separados, o principal da NTN-F 2029 e a LTN 2029 são a mesma promessa. Mesmo devedor, mesmo valor, mesma data.

Se uma das duas estiver mais barata que a outra, a moeda da aposta acabou de aparecer.

O que obriga duas promessas idênticas a custarem o mesmo? E o que mais se tira daí, além dessa igualdade?

## A taxa não manda no preço

A versão que circula é mais ou menos esta.

Cada título tem a sua taxa. A NTN-F é cotada pela TIR (taxa interna de retorno: a taxa única que, aplicada a todos os fluxos, reproduz o preço), a LTN pela dela, e o preço sai de cada taxa. O valor presente, a soma dos fluxos descontados, seria uma convenção de cálculo: a fórmula que o manual manda usar.

E arbitragem, nessa versão, é qualquer operação esperta entre dois ativos parecidos, que aposta que a diferença de preço entre eles vai fechar.

As duas metades erram pelo mesmo motivo: tratam o preço como opinião. A opinião do mercado sobre os juros, sobre o título, sobre o futuro.

**Preço não é opinião. É o custo da réplica.**

Essa frase basta para tirar a fórmula de valor presente, o preço justo de uma NTN-F e, com mais matemática, a fórmula de Black-Scholes.

## A aposta que não sobrevive

Arbitragem é uma carteira que custa zero (ou menos que zero) hoje, nunca dá prejuízo no futuro e dá lucro em pelo menos um cenário. Ela aparece de duas formas:

1. Você recebe dinheiro hoje e não deve nada depois.
2. Você não paga nada hoje, nunca perde e, em algum cenário, ganha.

Cara, eu ganho. Coroa, eu não perco.

O **princípio da não arbitragem** diz que, num mercado em equilíbrio, nenhuma das duas formas sobrevive. Ele não diz que elas nunca aparecem. Diz que não duram: quem as vê opera, e a operação as apaga.

Princípio, aqui, no sentido do matemático: axioma. Não se prova, se assume. O que se prova são as consequências.

A primeira é a **Lei do Preço Único**: dois ativos, ou duas carteiras, com exatamente os mesmos fluxos, nas mesmas datas e do mesmo devedor, têm o mesmo preço hoje.

```latex
CF_A(t) = CF_B(t)\ \text{para toda data}\ t \quad\Longrightarrow\quad P_A = P_B
```

### A prova cabe numa LTN

A demonstração é por absurdo, e a promessa da abertura serve de exemplo. Para simplificar a conta, troque 2029 por um ano (252 dias úteis) e use 14,30% ao ano, perto da curva prefixada de novembro de 2026. A LTN de um ano vale 1.000 ÷ 1,143, ou R$ 874,89.

Agora suponha que alguém cote o principal desmembrado de uma NTN-F, que paga os mesmos R$ 1.000 na mesma data, a R$ 870,00.

A mesa compra o principal e vende a LTN a descoberto (vende o título que não tem, tomado emprestado, e o devolve no fim):

| Data | Compra do principal (R$) | Venda da LTN (R$) | Líquido (R$) |
| --- | --- | --- | --- |
| Hoje | −870,00 | +874,89 | **+4,89** |
| Em 252 dias úteis | +1.000,00 | −1.000,00 | 0 |

R$ 4,89 no bolso hoje, sem nenhuma obrigação líquida depois. É a primeira forma de arbitragem.

Se o princípio vale, o preço de R$ 870,00 não sobrevive. Invertendo as pontas (comprar a LTN, vender o principal), o caso contrário também cai. Sobra a igualdade.

### Quem paga o ganha-ganha

O ganha-ganha da moeda era de uma pessoa só, e alguém pagou por ele. Quem vendeu o principal a R$ 870,00 entregou R$ 4,89 de valor ao arbitrador. O almoço do arbitrador saiu do prato de quem cotou errado.

Mas a operação tem um efeito colateral. Quem compra o barato empurra o preço dele para cima. Quem vende o caro empurra o preço dele para baixo. Repetida por todo mundo que enxerga a mesma moeda, a operação fecha a diferença, e a aposta desaparece.

Nesse ponto, o ganha-ganha muda de dono.

Depois que as mesas fecham a diferença, quem compra uma NTN-F, quem marca uma carteira a mercado (atualiza o valor dela pelo preço do dia) e o próprio Tesouro, que leiloa LTN e NTN-F toda semana, passam a trabalhar com preços coerentes entre si. Ninguém precisa saber quem foi o arbitrador para se beneficiar dele.

O ganho individual some. Fica um mercado em que ninguém consegue explorar ninguém sem correr risco. Esse é o ganha-ganha coletivo, e o nome técnico dele é equilíbrio.

Até aqui, é a primeira página de qualquer livro de renda fixa. O que sai dela é bem maior que a igualdade entre dois preços.

## Preço sem opinião

Que problema esse princípio resolve, e para quem?

O problema clássico de precificar é que o preço depende do que as pessoas querem: quanto risco toleram, quanto aceitam esperar, o que acham que vai acontecer. Um modelo que parte daí exige saber o que ninguém sabe.

A não arbitragem pula essa etapa. Ela não pergunta o que você acha dos juros. Pergunta quanto custa montar o mesmo fluxo com o que já tem preço no mercado. Se a réplica existe, o preço está decidido, concorde você ou não.

Da Lei do Preço Único sai, primeiro, a soma. Se a carteira C paga exatamente o que A e B pagam juntos, então P(C) = P(A) + P(B). O preço de um pacote é a soma do preço das peças.

Basta, então, conhecer o preço das peças mais simples. Em renda fixa prefixada, a peça mais simples é um título que paga R$ 1 numa única data. O preço hoje desse R$ 1 é o **fator de desconto** daquela data, DF(t). A LTN é exatamente isso, em lotes de R$ 1.000.

Qualquer fluxo prefixado do mesmo devedor é uma pilha dessas peças. Logo:

```latex
P = \sum_{t} CF_t \cdot DF(t), \qquad DF(t) = \frac{1}{(1 + r_t)^{du_t/252}}
```

em que CF_t é o fluxo pago na data t, du_t são os dias úteis até ela e r_t é a taxa zero-cupom (também chamada de taxa *spot*: a taxa de um título que só paga no fim) do vértice t (cada prazo da curva).

Repare de onde a fórmula veio. Ela não começou como matemática de valor presente. Começou com uma aposta que não sobrevive.

### A mesma ideia, com mais matemática

O caso mais famoso de réplica não é de renda fixa.

Em 1973, Fischer Black e Myron Scholes, e no mesmo ano Robert Merton, mostraram que uma opção sobre ação pode ser replicada por uma carteira de ação e título sem risco, ajustada continuamente conforme o preço da ação se mexe. Se a réplica existe, a opção tem de custar o mesmo que ela. Senão, alguém compra uma, vende a outra e embolsa a diferença.

O resultado é a fórmula que o manual de opções da B3 usa, a do texto anterior. E ela tem uma ausência famosa: o retorno esperado da ação não aparece nela. A fórmula não pede a opinião de ninguém sobre se a ação vai subir.

Merton e Scholes receberam o Nobel de Economia de 1997. Black tinha morrido em 1995, e o prêmio não é dado a título póstumo.

Daqui em diante, o texto fica na renda fixa, onde a réplica é estática: monta-se uma vez e espera-se o vencimento.

## Uma NTN-F feita de LTNs

Uma carteira que paga exatamente o mesmo que um título é um **portfólio equivalente** (ou carteira replicante) desse título. Pela Lei do Preço Único, os dois têm de custar o mesmo.

Pegue uma NTN-F hipotética, a um ano e meio do vencimento, com três pagamentos: em 126, 252 e 378 dias úteis. O cupom é de 10% ao ano, pago por semestre sobre R$ 1.000:

```latex
C = 1.000 \times \left[(1{,}10)^{1/2} - 1\right] = 48{,}808848
```

Os fluxos são R$ 48,81, R$ 48,81 e R$ 1.048,81 (o último cupom mais o principal).

Agora suponha três LTNs vencendo exatamente nessas datas, negociadas a 14,00%, 14,30% e 14,55% ao ano. As taxas são ilustrativas, na ordem de grandeza da curva prefixada de novembro de 2026, com a Selic em 13,75% desde a reunião do Copom de 4 de novembro.

Para replicar a NTN-F, compre, em cada data, LTNs na quantidade fluxo ÷ 1.000:

| Vértice (dias úteis) | Taxa *spot* (% a.a.) | PU da LTN (R$) | Quantidade de LTN | Custo na réplica (R$) |
| --- | --- | --- | --- | --- |
| 126 | 14,00 | 936,585812 | 0,04880885 | 45,713675 |
| 252 | 14,30 | 874,890639 | 0,04880885 | 42,702404 |
| 378 | 14,55 | 815,656609 | 1,04880885 | 855,467869 |
| **Total** |  |  |  | **943,883948** |

Pela Lei do Preço Único, o PU (preço unitário) justo da NTN-F é R$ 943,88. É cálculo próprio, sem os truncamentos da metodologia do Tesouro.

A TIR que reproduz esse preço é 14,53% ao ano. Fica abaixo dos 14,55% da LTN do vencimento porque a curva é positivamente inclinada (as taxas longas acima das curtas): dois dos três fluxos são descontados a taxas menores.

A TIR sai do preço, e não o contrário.

### A moeda aparece

Suponha um dealer (a instituição que faz preço de compra e de venda) que cota a NTN-F usando, como TIR, a taxa da LTN do vencimento: 14,55% para os três fluxos. O PU dele sai a R$ 943,68, ou R$ 0,20 abaixo da réplica.

A mesa compra 100.000 NTN-F do dealer e vende a réplica: 4.881 LTNs de 126 dias, 4.881 de 252 e 104.881 de 378.

| Ponta | Hoje (R$) |
| --- | --- |
| Compra de 100.000 NTN-F a R$ 943,680875 | −94.368.087,53 |
| Venda das LTNs da réplica | +94.388.697,41 |
| **Líquido na montagem** | **+20.609,88** |

O arredondamento dos lotes deixa a mesa devendo R$ 115,18 a mais do que recebe em cada data, o que vale R$ 302,60 hoje. Descontada essa sobra, o lucro travado é de R$ 20.307,28: exatamente 100.000 vezes os R$ 0,20 de diferença.

Nas três datas, os cupons e o principal da NTN-F pagam as LTNs vendidas. Cara, a mesa ganha. Coroa, não perde.

Repare na escala. São R$ 20 mil numa operação de R$ 94 milhões, cerca de 2 pontos-base (um ponto-base é um centésimo de ponto percentual). Arbitragem de verdade costuma ser assim: pequena, rápida e disputada.

### A mesma conta, todo dia

O mercado leva essa decomposição tão a sério que ela existe fisicamente: é o desmembramento da abertura, que transforma uma NTN-F em zeros negociáveis.

E a ANBIMA faz a conta ao contrário, todo dia. A estrutura a termo prefixada que ela divulga é estimada a partir dos preços de LTN e NTN-F, pelo modelo de Svensson: os fatores de desconto que melhor explicam todos esses preços ao mesmo tempo. É a Lei do Preço Único aplicada a uma prateleira inteira.

## Nem toda convergência é arbitragem

Volte à segunda metade do mito: arbitragem como qualquer aposta de que a diferença entre dois ativos parecidos vai fechar.

Pense numa operação clássica da bolsa brasileira. Quando a diferença de preço entre a ação preferencial da Petrobras (PETR4) e a ordinária (PETR3) foge da média histórica, compra-se uma e vende-se a outra, esperando a volta.

As duas ações são da mesma empresa e andam juntas quase sempre. Mas não pagam o mesmo fluxo: a ordinária dá direito a voto, a preferencial dá prioridade no dividendo. A diferença entre elas pode abrir e continuar aberta, por um motivo que o histórico não previu.

Isso é **trading de correlação** (também chamado de operação de valor relativo): uma aposta numa relação estatística, que vale em média, até deixar de valer. A arbitragem se apoia numa identidade de fluxos, que vale em todo cenário.

O critério cabe numa pergunta: se a diferença de preço dobrar amanhã, você perde dinheiro no vencimento?

Na NTN-F do exemplo, não. O marca a mercado pode doer no meio do caminho, mas no vencimento as LTNs vendidas são pagas, centavo por centavo, pelos fluxos da NTN-F comprada.

No trading de correlação, pode perder de vez. Não existe data em que as duas pontas sejam obrigadas a se encontrar.

O caso mais caro dessa confusão já passou por aqui. O LTCM (Long-Term Capital Management, o fundo americano que quebrou em 1998) chamava de arbitragem muitas operações de convergência entre títulos parecidos, mas não idênticos. Elas divergiram ao mesmo tempo, e o fundo não teve capital para esperar. Contei essa história em [“Quando os Modelos se Rebelam”](https://syntaxis.substack.com/p/quando-os-modelos-se-rebelam).

Trading de correlação merece um texto próprio, e vai ganhar um. Por ora, basta a fronteira: a arbitragem vive de identidade, a correlação vive de estatística.

### Os limites da arbitragem de verdade

Até a arbitragem de verdade tem custo. Andrei Shleifer e Robert Vishny, num artigo de 1997 no *Journal of Finance*, resumiram o problema: a arbitragem de livro não exige capital nem corre risco; a de verdade quase sempre exige os dois.

Na NTN-F do exemplo, três atritos aparecem:

1. **Vender o que não tem custa.** Para vender a LTN a descoberto, a mesa precisa tomá-la emprestada, em geral por uma operação compromissada (a compra com compromisso de revenda, em que o título muda de mão por um prazo combinado). Se aquele vencimento estiver escasso, tomar o papel fica caro, e o custo come o ganho.
2. **Cada ponta cruza um spread.** O spread de compra e venda é a diferença entre o preço de quem compra e o de quem vende. A réplica tem quatro pontas, e 2 pontos-base somem rápido.
3. **Nem toda data tem LTN.** O Tesouro não emite LTN para todo semestre. Sem o título, a mesa recorre ao DI futuro (o contrato da B3 sobre a taxa DI), que não paga o mesmo fluxo: tem ajuste diário de margem e referência no CDI, não no Tesouro. A réplica vira quase arbitragem, com um resíduo de risco que precisa ser medido.

Por isso os desvios que aparecem nas telas não são, em geral, dinheiro esquecido. Na maior parte das vezes, são o preço desses atritos.

## Antes de chamar de arbitragem

Sabendo de onde vem o preço, a decisão muda em dois lugares.

O primeiro é a hora de dizer se um título está barato. Comparar a TIR da NTN-F com a taxa da LTN do mesmo vencimento é o erro do dealer do exemplo. O certo é comparar preço com preço: o PU de mercado contra o PU da réplica na curva.

Na planilha, com os fluxos em B2:B4, as taxas *spot* em C2:C4 e os dias úteis em D2:D4:

```
PU da réplica:              =SOMARPRODUTO(B2:B4/(1+C2:C4)^(D2:D4/252))
Quantidade de LTN por data: =B2/1000
Desvio por título:          =PU_mercado - PU_réplica
```

O segundo é a hora de classificar uma operação. Antes de chamar qualquer coisa de arbitragem, três perguntas:

1. **Os fluxos são idênticos, nas mesmas datas?** PETR3 e PETR4 falham aqui.
2. **O devedor é o mesmo?** Um CDB e uma LTN com o mesmo vencimento podem pagar o mesmo valor, mas não carregam o mesmo risco de crédito. A Lei do Preço Único não diz nada sobre eles.
3. **Dá para vender a ponta cara, e quanto custa sustentar a posição até o vencimento?** O empréstimo do papel, o spread e a margem entram aqui.

Três respostas sim, e um custo menor que o desvio: é arbitragem. Qualquer não: é outra coisa. Pode até ser uma boa operação, mas tem risco, e precisa ser tratada como tal.

Precificar por fluxo de caixa é parte de duas dimensões do [Syntaxis Skill Check](https://skill.syntaxis.com.br/), a de mercados e produtos e a de matemática financeira. É um diagnóstico gratuito, que compara o seu perfil com o que o mercado espera para o próximo degrau da carreira.

## A moeda que ninguém lança duas vezes

A aposta da abertura existe. Cara, eu ganho; coroa, eu não perco. Mas dura só o tempo de alguém notar.

Quem nota ganha sozinho e, ao ganhar, apaga a aposta. O que fica é um mercado em que duas promessas iguais custam o mesmo, um título com cupom custa o que custam as suas peças, e uma opção custa o que custa a carteira que a imita. O ganha-ganha de um vira o de todos.

Preço não é opinião. É o custo da réplica.

Se o texto funcionou, você consegue montar sozinho a réplica de outro título do Tesouro. A NTN-B (Tesouro IPCA+ com Juros Semestrais) paga cupom de 6% ao ano sobre o VNA (valor nominal atualizado pelo IPCA), em duas parcelas por ano. A NTN-B Principal paga só o VNA, no vencimento. Quantas NTN-B Principal de cada data replicam uma NTN-B? E por que comprar a NTN-B e vender essa réplica é arbitragem, mas comprar a NTN-B e vender LTNs não é?

No próximo texto, a conta vai ao contrário. Em vez de usar a curva para precificar a NTN-F, usamos LTNs e NTN-Fs para construir a curva, vértice por vértice. É o *bootstrapping* (a construção da curva zero-cupom a partir dos títulos com cupom), e é nele que fica claro por que a TIR de uma NTN-F e a taxa *spot* do mesmo prazo são objetos diferentes.

Se este texto ajudou você a separar arbitragem de aposta, encaminhe para quem chama de arbitragem qualquer *long-short*.

## Para continuar aprendendo

- Bruce Tuckman e Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 4ª ed. (Wiley, 2022), cap. 1, “Prices, Discount Factors, and Arbitrage”. A versão de mesa deste texto: fatores de desconto, carteira replicante e Lei do Preço Único, com os títulos e os *STRIPS* (cupons e principal desmembrados) do Tesouro americano.
- John H. Cochrane, *Asset Pricing*, ed. revisada (Princeton University Press, 2005), cap. 4 [VERIFICAR: capítulo e título, “The Discount Factor”]. A versão teórica: por que a Lei do Preço Único garante que existe um fator de desconto, e a não arbitragem, que ele é positivo.
- Andrei Shleifer e Robert Vishny, “The Limits of Arbitrage”, *Journal of Finance*, v. 52, n. 1, p. 35–55 (1997). Por que a arbitragem de verdade exige capital, corre risco e pode falhar justo quando os preços mais se afastam do valor.
- ANBIMA, [*Estrutura a Termo das Taxas de Juros Estimada e Inflação Implícita: Metodologia*](https://www.anbima.com.br/data/files/9A/F4/E3/1F/4805B710B0F024B7882BA2A8/est-termo_metodologia_v2021.pdf) (versão de agosto de 2021). Como a curva prefixada divulgada todo dia é extraída dos preços de LTN e NTN-F pelo modelo de Svensson: a Lei do Preço Único em escala de mercado.

---

*Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira.*

## Notas de revisão (não publicar)

O draft segue a pauta com o ganha-ganha em duas camadas: a arbitragem como ganha-ganha de uma pessoa só (§ A aposta que não sobrevive) e o equilíbrio como ganha-ganha coletivo (§ Quem paga o ganha-ganha). São cerca de 2.900 palavras de corpo, na faixa dos últimos NdP.

### Decisões para você

- [ ] **Ponte de série.** “Frequência de Capitalização” apontava para o FIDC. Este texto troca a direção e promete o *bootstrapping* (e um texto sobre trading de correlação). Ok, ou o FIDC continua sendo o próximo? Seguir com o bootstraping
- [ ] **Título.** Alternativas: “O almoço que não dura”; “Mesmo fluxo, mesmo preço”. O subtítulo carrega a tese em refrão. Seguir com os títulos atuais
- [ ] **Exemplo estilizado ou real.** A NTN-F do exemplo é hipotética (126, 252 e 378 dias úteis, taxas ilustrativas). Dá para trocar por uma NTN-F 2029 real precificada na ETTJ da ANBIMA de uma data fixa, ao custo de mais fluxos e de um número que envelhece. Estilizado
- [ ] **Black-Scholes só como menção.** Sem derivação, para não tirar o foco da renda fixa. Se quiser mais, cabe uma caixa com a carteira delta-hedge em três linhas. Só mencao
- [ ] **Movimentos 6 e 7 omitidos.** Sem materialidade (o tema é conceitual) e sem fechamento de loop (abertura no modo B; o movimento 9 volta à moeda).

### Pendências [VERIFICAR]

- Norma vigente do desmembramento de NTN-F no Selic. Encontrei o Comunicado Selic nº 7.588 (2000) e códigos ISIN de “NTN-F somente cupons” emitidos em 2026 na Mais Retorno; falta a fonte oficial atual.
- Valor exato do cupom pago: R$ 48,81 no texto (1.000 × 0,048808848). Material da ENAP/Tesouro Direto cita R$ 48,80 por truncamento; confirmar antes de escrever R$ 1.048,81 na abertura.
- Cochrane, *Asset Pricing*: confirmar capítulo 4 e o título “The Discount Factor” na edição revisada.

### Contas conferidas (Python, cálculo próprio)

| Item | Valor |
| --- | --- |
| Cupom semestral | 1.000 × (1,10^0,5 − 1) = 48,808848 |
| LTN 1 ano a 14,30% | 874,890639 |
| PU da réplica (14,00 / 14,30 / 14,55%) | 943,883948 |
| TIR da réplica | 14,5328% a.a. |
| PU do dealer a 14,55% flat | 943,680875 (−0,203073) |
| Montagem com 100.000 NTN-F e 4.881 / 4.881 / 104.881 LTNs | +20.609,88 |
| Sobra do arredondamento | −115,18 por data; VP −302,60 |
| Lucro travado | 20.307,28 (2,2 pontos-base sobre R$ 94,4 milhões) |

### Fontes usadas na pesquisa

- Selic em 13,75% na 282ª reunião do Copom, 4/11/2026 (Agência Brasil, Estadão Conteúdo).
- Tesouro Prefixado 2029 a 14,65% em 11/11/2026 (Tesouro Nacional, via brapi): base da ordem de grandeza das taxas ilustrativas.
- Comunicado do Tesouro sobre leilões de 2026: NTN-F ofertadas semanalmente com as LTN.
- ANBIMA, metodologia da ETTJ: curva pré estimada com LTN e NTN-F, modelo de Svensson.
- Shleifer e Vishny (1997), *Journal of Finance* 52(1), p. 35–55.
- Tuckman e Serrat, 4ª ed. (Wiley, 2022): cap. 1 confirmado no sumário da editora.

### Para o pipeline

- Salvar como `_arquivo/drafts/AAAA-MM-DD_nao-arbitragem.md` com `linha_editorial: Notas de um Professor`.
- Visual sugerido (etapa 8): diagrama da réplica, a NTN-F decomposta em três LTNs com quantidade e custo de cada uma, ao lado do diagrama de fluxos da carteira de arbitragem (hoje +20,6 mil; vencimentos zerados).
- Checagem mecânica feita à mão: nenhum travessão nem exclamação no corpo, refrão isolado na § 2 e na § 9, frase-sinal uma vez (fim da anatomia), antítese no máximo uma por seção fora do refrão.


---

## Marcadores extraídos do rascunho

| # | Trecho (verbatim ou resumido) | Classificação | Resolução |
|---|---|---|---|
| 1 | Sem front-matter; linha da Ficha "`linha_editorial: Notas de um Professor` · voz: ensaística em registro técnico · tipo (BACKWARDS_DESIGN §4.2): conceito de finanças · abertura: modo B" | Estrutural | **Resolvido (etapa 0):** campo lido do rascunho, valor válido. Voz, tipo e modo de abertura vão para a etapa 1/2. |
| 2 | "Ficha de Saída (não publicar)": só a competência de saída, sem os 8 campos | Estrutural | Pendente (etapa 2): completar os 8 campos a partir do corpo. |
| 3 | Título "Cara, eu ganho. Coroa, eu não perco." / subtítulo "Preço não é opinião: é o custo de montar o mesmo fluxo." × alternativas "O almoço que não dura", "Mesmo fluxo, mesmo preço" | Estrutural | **Resolvido (autor, no rascunho):** "Seguir com os títulos atuais". |
| 4 | Decisão "Ponte de série": FIDC × *bootstrapping* (e um texto sobre trading de correlação) | Estrutural | **Resolvido (autor, no rascunho):** "Seguir com o bootstraping". O FIDC já estava cancelado (ver `posts/2026-11-09-frequencia-de-capitalizacao/estado.json`). |
| 5 | Decisão "Exemplo estilizado ou real" (NTN-F hipotética × NTN-F 2029 na ETTJ) | Nota de conteúdo | **Resolvido (autor, no rascunho):** "Estilizado". |
| 6 | Decisão "Black-Scholes só como menção" × caixa com a carteira *delta-hedge* | Nota de conteúdo | **Resolvido (autor, no rascunho):** "Só mencao". |
| 7 | Decisão "Movimentos 6 e 7 omitidos" (sem materialidade; abertura modo B, o 9 volta à moeda) | Estrutural | Registro, sem pergunta. Etapa 2 confere contra o §3 do BACKWARDS_DESIGN. |
| 8 | "[VERIFICAR: norma vigente do desmembramento; a referência mais antiga encontrada é o Comunicado Selic nº 7.588, de 2000. A Mais Retorno lista emissões de “NTN-F somente cupons” em 2026.]" (abertura) | Nota de conteúdo | Pendente (etapa 3/7). |
| 9 | Pendência: cupom pago R$ 48,81 (1.000 × 0,048808848) × R$ 48,80 por truncamento (ENAP/Tesouro Direto); "confirmar antes de escrever R$ 1.048,81 na abertura" | Nota de conteúdo | Pendente (etapa 3/7). |
| 10 | "[VERIFICAR: capítulo e título, “The Discount Factor”]" (Cochrane, *Asset Pricing*, ed. revisada) | Nota de conteúdo | Pendente (etapa 7). |
| 11 | "Contas conferidas (Python, cálculo próprio)": cupom 48,808848; LTN 1 ano 874,890639; réplica 943,883948; TIR 14,5328%; PU do *dealer* 943,680875 (−0,203073); montagem +20.609,88; sobra −115,18 por data, VP −302,60; lucro 20.307,28 (2,2 pb sobre R$ 94,4 mi). No corpo, também: 1.000 ÷ 1,143 = 874,89; 870,00 → +4,89; PUs 936,585812 / 815,656609; custos 45,713675 / 42,702404 / 855,467869; venda das LTNs +94.388.697,41; compra −94.368.087,53 | Nota de conteúdo | Pendente (etapa 7): recalcular tudo. |
| 12 | Fatos: Selic 13,75% na 282ª reunião do Copom, 4/11/2026; Tesouro Prefixado 2029 a 14,65% em 11/11/2026; leilões semanais de LTN e NTN-F; ETTJ ANBIMA por Svensson com LTN e NTN-F (metodologia v. ago/2021); Black, Scholes e Merton em 1973; Nobel de 1997 a Merton e Scholes, Black morto em 1995; LTCM em 1998; Shleifer e Vishny (1997), *JF* 52(1), 35–55; Tuckman e Serrat, 4ª ed., cap. 1 “Prices, Discount Factors, and Arbitrage”; NTN-B com cupom de 6% a.a. sobre o VNA; PETR3 × PETR4 (voto × prioridade no dividendo); "a fórmula que o manual de opções da B3 usa, a do texto anterior" | Nota de conteúdo | Pendente (etapa 3/7): conferir em fonte primária. |
| 13 | Links: [último texto](…/p/frequencia-de-capitalizacao); [“Quando os Modelos se Rebelam”](…/p/quando-os-modelos-se-rebelam); [Syntaxis Skill Check](https://skill.syntaxis.com.br/); PDF da metodologia da ETTJ (ANBIMA) | Nota de conteúdo | Pendente (etapa 7): conferir URL contra `marketing/catalogo.json` e o site. |
| 14 | CTA no corpo: "Precificar por fluxo de caixa é parte de duas dimensões do [Syntaxis Skill Check]…" | Nota de conteúdo | Registro: já vem do rascunho, no mesmo lugar do precedente (fim da Prateleira). A etapa 9a avalia; não se duplica. |
| 15 | Promessa no corpo: "Trading de correlação merece um texto próprio, e vai ganhar um." | Nota de conteúdo | Registro: coberto pela decisão 4 (o autor aprovou o item que citava os dois). Alerta para o gate: é promessa de série, como a do FIDC. |
| 16 | "Visual sugerido (etapa 8): diagrama da réplica, a NTN-F decomposta em três LTNs com quantidade e custo de cada uma, ao lado do diagrama de fluxos da carteira de arbitragem (hoje +20,6 mil; vencimentos zerados)." | Sugestão de visual | Pendente (etapa 2/8): conferir o tipo pelo critério. |
| 17 | "Salvar como `_arquivo/drafts/AAAA-MM-DD_nao-arbitragem.md`…" | Instrução de escrita (de processo) | **Resolvido (etapa 0):** não aplicável, `_arquivo/` não se renomeia; o arquivo fica com o nome que o autor deu. |
| 18 | "Checagem mecânica feita à mão: nenhum travessão nem exclamação no corpo, refrão isolado na § 2 e na § 9, frase-sinal uma vez (fim da anatomia), antítese no máximo uma por seção fora do refrão." | Nota de conteúdo | Registro: a etapa 9 roda `scripts/checar_post.py`; a 6 confere a antítese (regra 20). |
| 19 | Aviso legal no fim do corpo | Nota de conteúdo | Etapa 9: substituído pela cópia de `docs/AVISO_LEGAL.md`. |
| 20 | "Notas de revisão (não publicar)" inteira | Nota de conteúdo | Registro: fora do `post.md`. Decisões nos itens 3–7, pendências nos 8–11, fontes no 12, visual no 16. |
