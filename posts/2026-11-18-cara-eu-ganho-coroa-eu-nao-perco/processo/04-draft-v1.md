# Etapa 4 — Draft v1

Base: o corpo do rascunho (`00-leitura.md`), revisado e não reescrito, sem reordenar seções. Voz
ensaística em registro técnico (`01-briefing.md`). Saíram a Ficha de Saída (que mora em
`02-estrutura.md`) e as "Notas de revisão". Glosas, norma e itálico ficam para a etapa 6.
Recalcular os números fica para a etapa 7. O aviso legal padrão entra na etapa 9 (o do rascunho
fica por ora). Nenhuma instrução de escrita do inventário da etapa 0 pedia trecho novo (o único
item do tipo, nº 17, foi resolvido na etapa 0).

## Notas laterais: o que mudou e por quê

| # | Onde | Mudança | Origem |
|---|---|---|---|
| 1 | Topo | H1 "Cara, eu ganho. Coroa, eu não perco." e subtítulo em itálico; saem o H1 com "[draft v1]", a linha de data e o "**Subtítulo:**" | Autor, títulos atuais |
| 2 | Uma NTN-F feita de LTNs | "com a Selic em 13,75% desde a reunião do Copom de 4 de novembro" → "com a Selic em 13,75%, mantida pelo Copom na reunião de 4 de novembro". A 282ª reunião (4/11) manteve a taxa; o corte para 13,75% foi na 281ª (16/09) | `03-pesquisa.md`, pendência a (BCB, SGS 432 e comunicados do Copom) |
| 3 | Abertura | "R$ 1.048,81" → "R$ 1.048,80". O Tesouro fixa o PU de juros em R$ 48,808850 e trunca o valor financeiro na 2ª casa: quem tem um título recebe R$ 1.048,80 no vencimento. Os R$ 48,81 / R$ 1.048,81 do exemplo hipotético ficam: lá a conta é declarada "sem os truncamentos da metodologia do Tesouro". A etapa 7 decide se o exemplo adota a convenção do Tesouro (o que muda a sobra do arredondamento e o lucro travado em centavos) | `03-pesquisa.md`, pendência d e item 2 |
| 4 | Abertura | O parágrafo do desmembramento passa a afirmar só o que a fonte oficial sustenta: o Selic permite desmembrar cupons "quando prevista tal faculdade na emissão" (Res. BCB 55/2020, art. 45), com glosa do Selic, em dois parágrafos (regra 1). Que a NTN-F tem essa faculdade continua `[VERIFICAR]`, agora com o que se achou (só o Mais Retorno). Vai ao gate como pergunta nomeada se a etapa 7 não fechar | `03-pesquisa.md`, pendência c e item 4 |
| 5 | A aposta que não sobrevive | "Ele não diz que elas nunca aparecem. Diz que não duram: …" → "Elas até aparecem, mas não duram: …". Era a primeira de duas antíteses em parágrafos seguidos (a segunda, "Não se prova, se assume", é do registro matemático do autor e fica) | Guia, regra 20 (nunca duas seguidas) |
| 6 | Preço sem opinião | "Ela não pergunta o que você acha dos juros. Pergunta quanto custa…" → "Em vez de perguntar o que você acha dos juros, ela pergunta quanto custa…". A seção tinha duas antíteses; fica a da virada ("Ela não começou como matemática de valor presente. Começou com uma aposta que não sobrevive."), que amarra a fórmula à abertura | Guia, regra 20 (cerca de uma por seção) |
| 7 | Nem toda convergência é arbitragem | LTCM "o fundo americano que quebrou em 1998" → "que precisou ser socorrido em 1998". Em 23/09/1998, 14 instituições puseram US$ 3,6 bilhões no fundo; o post da série conta o socorro | `03-pesquisa.md`, item 19 (Federal Reserve History) |
| 8 | Os limites da arbitragem de verdade | DI futuro: "tem ajuste diário de margem e referência no CDI" → "tem ajuste diário (ganhos e perdas liquidados todo dia) e referência na taxa DI". Na B3, ajuste diário e margem de garantia são coisas distintas, e o ativo é a "Taxa DI, divulgada pela B3" | `03-pesquisa.md`, item 23 (especificação do DI1) |
| 9 | Fecho, exercício | "Quantas NTN-B Principal de cada data replicam uma NTN-B?" → "Se houvesse uma NTN-B Principal em cada data de cupom, quantas de cada data replicariam uma NTN-B?", e "é arbitragem" → "seria arbitragem". Só há NTN-B Principal em 6 vencimentos; o exercício não pode supor que a réplica existe no mercado | `03-pesquisa.md`, item 26; briefing, alerta |
| 10 | Para continuar aprendendo | Cochrane: `[VERIFICAR]` resolvido, "cap. 4, “The Discount Factor”" (seções 4.1 Lei do Preço Único e existência do fator; 4.2 não arbitragem e fator positivo) | `03-pesquisa.md`, item 28 |
| 11 | Uma NTN-F feita de LTNs; A moeda aparece | Placeholders `diag-01` (depois da tabela da réplica) e `diag-02` (depois do parágrafo do arredondamento), com alt-text curto | `02-estrutura.md`, visuais |
| 12 | Fórmulas | Três blocos ```` ```latex ```` → `$$ … $$`, o formato do post publicado da série | Briefing, continuidade |

**Conferido e sem mudança:** a ordem de grandeza das taxas (ETTJ de 11/11 e 17/11; pendência b);
os leilões semanais de LTN e NTN-F (pendência e; o cancelamento de 29/10 é exceção pontual);
Svensson sobre LTN e NTN-F (pendência f); Tuckman e Serrat, cap. 1 (pendência g); Shleifer e
Vishny (item 20); PETR3 × PETR4 no estatuto (item 18); Nobel de 1997 e o estatuto da Fundação
(item 11); "Nem toda data tem LTN" (item 22).

**Fica para decisão posterior (não aplicado; acrescentar seria parágrafo novo):**
- **O caso real da semana** (item 34): com os preços indicativos da ANBIMA de 11/11/2026, a NTN-F
  2029 sai cerca de R$ 0,81 acima da sua réplica em LTN, no sentido oposto ao do *dealer* do
  exemplo. O autor escolheu o exemplo estilizado; isto pode virar uma frase em "A mesma conta,
  todo dia" ou ficar fora. Vai ao gate como sugestão, depois de a etapa 7 recalcular.
- **Falta de capital como atrito** (item 31): o *puzzle* TIPS × Treasury (Fleckenstein, Longstaff
  e Lustig, 2014) mostra réplica exata com desvio de mais de US$ 20 por US$ 100 durante meses. O
  rascunho já cita Shleifer e Vishny, que cobrem o argumento; o exemplo seria acréscimo.
- **Principal desmembrado e zero "igual" nem sempre têm o mesmo preço** (item 32, Daves e
  Ehrhardt, 1993): o principal reconstitui o título, o zero não. Toca a frase "são a mesma
  promessa" da abertura. A etapa 5 avalia se pede ressalva.
- **Vencimento em feriado** (item 3): 1º/1/2029 é feriado e a liquidação cai em 2/1/2029. A etapa 7
  decide se "Em 1º de janeiro de 2029, o Tesouro Nacional vai pagar" precisa de ajuste.

---

# Cara, eu ganho. Coroa, eu não perco.

*Preço não é opinião: é o custo de montar o mesmo fluxo.*

No fim do [último texto](https://syntaxis.substack.com/p/frequencia-de-capitalizacao), deixei uma fórmula de planilha para replicar o preço de uma LTN (Letra do Tesouro Nacional, o título público prefixado sem cupom). Com ela, a série de convenções fechou: a régua, o motor e a etiqueta.

A palavra que importa hoje já estava naquela linha: *replicar*.

Comece por uma aposta. Uma moeda é lançada. Se der cara, você ganha. Se der coroa, você não perde nada. E não paga para entrar.

Ninguém recusaria. É o ganha-ganha mais puro que existe, e tem um detalhe: é ganha-ganha de uma pessoa só.

No mercado, essa aposta tem nome. É a **arbitragem**. E boa parte da teoria de preços foi construída sobre a ideia de que ela não dura.

Agora, um caso concreto. Em 1º de janeiro de 2029, o Tesouro Nacional vai pagar R$ 1.000 a quem tiver uma LTN 2029. No mesmo dia, vai pagar R$ 1.048,80 a quem tiver uma NTN-F 2029 (Nota do Tesouro Nacional, série F: o prefixado que paga cupom a cada seis meses). São o último cupom e o principal.

No Selic (o sistema do Banco Central onde os títulos públicos ficam custodiados), um título pode ter os cupons desmembrados do principal, quando a emissão prevê essa faculdade (Resolução BCB nº 55/2020, art. 45).

Desmembrados, o principal e cada cupom passam a circular como títulos separados. [VERIFICAR: que a emissão da NTN-F prevê o desmembramento; não há fonte oficial, só o agregador Mais Retorno, que lista o principal desmembrado da NTN-F 2029 (código Selic 950198)]

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

O **princípio da não arbitragem** diz que, num mercado em equilíbrio, nenhuma das duas formas sobrevive. Elas até aparecem, mas não duram: quem as vê opera, e a operação as apaga.

Princípio, aqui, no sentido do matemático: axioma. Não se prova, se assume. O que se prova são as consequências.

A primeira é a **Lei do Preço Único**: dois ativos, ou duas carteiras, com exatamente os mesmos fluxos, nas mesmas datas e do mesmo devedor, têm o mesmo preço hoje.

$$
CF_A(t) = CF_B(t)\ \text{para toda data}\ t \quad\Longrightarrow\quad P_A = P_B
$$

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

A não arbitragem pula essa etapa. Em vez de perguntar o que você acha dos juros, ela pergunta quanto custa montar o mesmo fluxo com o que já tem preço no mercado. Se a réplica existe, o preço está decidido, concorde você ou não.

Da Lei do Preço Único sai, primeiro, a soma. Se a carteira C paga exatamente o que A e B pagam juntos, então P(C) = P(A) + P(B). O preço de um pacote é a soma do preço das peças.

Basta, então, conhecer o preço das peças mais simples. Em renda fixa prefixada, a peça mais simples é um título que paga R$ 1 numa única data. O preço hoje desse R$ 1 é o **fator de desconto** daquela data, DF(t). A LTN é exatamente isso, em lotes de R$ 1.000.

Qualquer fluxo prefixado do mesmo devedor é uma pilha dessas peças. Logo:

$$
P = \sum_{t} CF_t \cdot DF(t), \qquad DF(t) = \frac{1}{(1 + r_t)^{du_t/252}}
$$

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

$$
C = 1.000 \times \left[(1{,}10)^{1/2} - 1\right] = 48{,}808848
$$

Os fluxos são R$ 48,81, R$ 48,81 e R$ 1.048,81 (o último cupom mais o principal).

Agora suponha três LTNs vencendo exatamente nessas datas, negociadas a 14,00%, 14,30% e 14,55% ao ano. As taxas são ilustrativas, na ordem de grandeza da curva prefixada de novembro de 2026, com a Selic em 13,75%, mantida pelo Copom na reunião de 4 de novembro.

Para replicar a NTN-F, compre, em cada data, LTNs na quantidade fluxo ÷ 1.000:

| Vértice (dias úteis) | Taxa *spot* (% a.a.) | PU da LTN (R$) | Quantidade de LTN | Custo na réplica (R$) |
| --- | --- | --- | --- | --- |
| 126 | 14,00 | 936,585812 | 0,04880885 | 45,713675 |
| 252 | 14,30 | 874,890639 | 0,04880885 | 42,702404 |
| 378 | 14,55 | 815,656609 | 1,04880885 | 855,467869 |
| **Total** |  |  |  | **943,883948** |

![Diagrama: os três fluxos da NTN-F hipotética e as três LTNs das mesmas datas que os replicam, com quantidade e custo de cada lote.](diag-01)

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

![Diagrama: os fluxos da carteira de arbitragem. A mesa recebe dinheiro hoje e, nas três datas, a NTN-F comprada paga as LTNs vendidas.](diag-02)

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

O caso mais caro dessa confusão já passou por aqui. O LTCM (Long-Term Capital Management, o fundo americano que precisou ser socorrido em 1998) chamava de arbitragem muitas operações de convergência entre títulos parecidos, mas não idênticos. Elas divergiram ao mesmo tempo, e o fundo não teve capital para esperar. Contei essa história em [“Quando os Modelos se Rebelam”](https://syntaxis.substack.com/p/quando-os-modelos-se-rebelam).

Trading de correlação merece um texto próprio, e vai ganhar um. Por ora, basta a fronteira: a arbitragem vive de identidade, a correlação vive de estatística.

### Os limites da arbitragem de verdade

Até a arbitragem de verdade tem custo. Andrei Shleifer e Robert Vishny, num artigo de 1997 no *Journal of Finance*, resumiram o problema: a arbitragem de livro não exige capital nem corre risco; a de verdade quase sempre exige os dois.

Na NTN-F do exemplo, três atritos aparecem:

1. **Vender o que não tem custa.** Para vender a LTN a descoberto, a mesa precisa tomá-la emprestada, em geral por uma operação compromissada (a compra com compromisso de revenda, em que o título muda de mão por um prazo combinado). Se aquele vencimento estiver escasso, tomar o papel fica caro, e o custo come o ganho.
2. **Cada ponta cruza um spread.** O spread de compra e venda é a diferença entre o preço de quem compra e o de quem vende. A réplica tem quatro pontas, e 2 pontos-base somem rápido.
3. **Nem toda data tem LTN.** O Tesouro não emite LTN para todo semestre. Sem o título, a mesa recorre ao DI futuro (o contrato da B3 sobre a taxa DI), que não paga o mesmo fluxo: tem ajuste diário (ganhos e perdas liquidados todo dia) e referência na taxa DI, não no Tesouro. A réplica vira quase arbitragem, com um resíduo de risco que precisa ser medido.

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

Se o texto funcionou, você consegue montar sozinho a réplica de outro título do Tesouro. A NTN-B (Tesouro IPCA+ com Juros Semestrais) paga cupom de 6% ao ano sobre o VNA (valor nominal atualizado pelo IPCA), em duas parcelas por ano. A NTN-B Principal paga só o VNA, no vencimento. Se houvesse uma NTN-B Principal em cada data de cupom, quantas de cada data replicariam uma NTN-B? E por que comprar a NTN-B e vender essa réplica seria arbitragem, mas comprar a NTN-B e vender LTNs não é?

No próximo texto, a conta vai ao contrário. Em vez de usar a curva para precificar a NTN-F, usamos LTNs e NTN-Fs para construir a curva, vértice por vértice. É o *bootstrapping* (a construção da curva zero-cupom a partir dos títulos com cupom), e é nele que fica claro por que a TIR de uma NTN-F e a taxa *spot* do mesmo prazo são objetos diferentes.

Se este texto ajudou você a separar arbitragem de aposta, encaminhe para quem chama de arbitragem qualquer *long-short*.

## Para continuar aprendendo

- Bruce Tuckman e Angel Serrat, *Fixed Income Securities: Tools for Today's Markets*, 4ª ed. (Wiley, 2022), cap. 1, “Prices, Discount Factors, and Arbitrage”. A versão de mesa deste texto: fatores de desconto, carteira replicante e Lei do Preço Único, com os títulos e os *STRIPS* (cupons e principal desmembrados) do Tesouro americano.
- John H. Cochrane, *Asset Pricing*, ed. revisada (Princeton University Press, 2005), cap. 4, “The Discount Factor”. A versão teórica: por que a Lei do Preço Único garante que existe um fator de desconto, e a não arbitragem, que ele é positivo.
- Andrei Shleifer e Robert Vishny, “The Limits of Arbitrage”, *Journal of Finance*, v. 52, n. 1, p. 35–55 (1997). Por que a arbitragem de verdade exige capital, corre risco e pode falhar justo quando os preços mais se afastam do valor.
- ANBIMA, [*Estrutura a Termo das Taxas de Juros Estimada e Inflação Implícita: Metodologia*](https://www.anbima.com.br/data/files/9A/F4/E3/1F/4805B710B0F024B7882BA2A8/est-termo_metodologia_v2021.pdf) (versão de agosto de 2021). Como a curva prefixada divulgada todo dia é extraída dos preços de LTN e NTN-F pelo modelo de Svensson: a Lei do Preço Único em escala de mercado.

---

*Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira.*
