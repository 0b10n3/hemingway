# Etapa 2 — Estrutura

O rascunho já chega estruturado, e o pipeline não reordena a argumentação. Esta etapa completa a
Ficha de Saída, confere a estrutura contra o backward design, mapeia os movimentos e decide os
visuais pelo critério. Proposta de mudança estrutural, se houver, vira pergunta ao autor.

## Ficha de Saída (`docs/BACKWARDS_DESIGN.md` §2)

O rascunho traz o campo 1 e uma linha de metadados. Os outros sete campos saem do próprio corpo,
sem conteúdo novo.

| Campo | Conteúdo |
| --- | --- |
| 1. Competência de saída | *Montar* a carteira de títulos zero-cupom que replica um título com cupom (quantidade = fluxo ÷ valor de face, data a data); *precificar* o título pela Lei do Preço Único (PU = Σ CF_t · DF(t)); *classificar* uma operação como arbitragem ou aposta de correlação. |
| 2. Teste de transferência | A NTN-B (cupom de 6% a.a. sobre o VNA, em duas parcelas) contra a NTN-B Principal (só o VNA, no vencimento). O leitor deve dizer sozinho quantas NTN-B Principal de cada data replicam uma NTN-B, e por que comprar a NTN-B e vender essa réplica é arbitragem, mas comprar a NTN-B e vender LTNs não é (o fluxo em IPCA não é o fluxo prefixado: falha a pergunta 1). |
| 3. Tese de fundo | "Preço não é opinião. É o custo da réplica." Abre o arco que vem depois da série de convenções (régua, motor, etiqueta): da precificação por réplica ao *bootstrapping*. Mesma família de "Capitalização não é lei da natureza. É cláusula." (a-corda-e-o-arco): o número que parece dado é consequência de uma regra. |
| 4. Erro-alvo | Em duas metades, que gente competente de fato repete: (a) cada título tem a sua taxa e o preço sai dela, e o valor presente é uma convenção de cálculo; (b) arbitragem é qualquer operação de convergência entre dois ativos parecidos (o *long-short* de PETR3 × PETR4). |
| 5. Ferramenta prática | O PU da réplica na planilha (`SOMARPRODUTO`), a quantidade de LTN por data (fluxo ÷ 1.000) e o desvio (PU de mercado − PU da réplica); comparar preço com preço, nunca TIR com taxa *spot*; as três perguntas antes de chamar algo de arbitragem; e o critério "se a diferença dobrar amanhã, você perde dinheiro no vencimento?". |
| 6. Âncora de autoridade | Tuckman e Serrat, cap. 1 (fatores de desconto, carteira replicante, Lei do Preço Único); Cochrane, *Asset Pricing*, cap. 4 [conferir, etapa 7]; Shleifer e Vishny (1997), *Journal of Finance*; ANBIMA, metodologia da ETTJ (Svensson sobre LTN e NTN-F); Black, Scholes e Merton (1973), Nobel de 1997. |
| 7. Os dois lados do balcão | De um lado, quem cota: o *dealer* que precifica a NTN-F pela taxa da LTN do vencimento, quem vende o principal barato. Do outro, quem arbitra: a mesa que compra o barato, vende a réplica e, ao fazer isso, fecha a diferença. Depois, quem se beneficia sem operar: quem compra NTN-F, quem marca carteira a mercado e o Tesouro, que leiloa LTN e NTN-F toda semana (emissor; o lado de lá do conceito). Distribuidor: não tratado; nenhuma das três condições do §4.3 se verifica. |
| 8. Ponte de série | Vem de "Frequência de Capitalização" (a fórmula de planilha que replica o PU da LTN; fim da série de convenções). **Aponta para:** o *bootstrapping* (a curva zero-cupom construída a partir de LTN e NTN-F), por decisão do autor, e um texto futuro sobre trading de correlação. |

**Verificação: a sequência entrega o campo 1?**

| Competência | Onde o texto a produz |
|---|---|
| montar a réplica | "Uma NTN-F feita de LTNs" (definição de portfólio equivalente; tabela com quantidade = fluxo ÷ 1.000 por vértice) |
| precificar pela Lei do Preço Único | "A aposta que não sobrevive" (princípio → Lei do Preço Único → prova por absurdo) → "Preço sem opinião" (soma → fator de desconto → P = Σ CF · DF) → tabela da réplica (R$ 943,88) e "A TIR sai do preço" |
| classificar arbitragem × correlação | "Nem toda convergência é arbitragem" (identidade × estatística; a pergunta-critério) → "Os limites da arbitragem de verdade" (três atritos) → "Antes de chamar de arbitragem" (três perguntas + custo menor que o desvio) |
| teste de transferência (NTN-B) | Fecho. Exige a réplica (quantidade = fluxo ÷ face, aqui em VNA) e a pergunta 1 das três (fluxos idênticos). O leitor já viu as duas. |

Entrega. Uma lacuna pequena: o texto ensina "quantidade = fluxo ÷ 1.000" para o prefixado, e o
teste pede a mesma conta sobre o VNA, que muda com o IPCA. A quantidade de NTN-B Principal por
data é a fração do cupom (fluxo ÷ VNA), e o VNA se cancela. É exatamente o raciocínio a
transferir, então não é lacuna de estrutura. A etapa 7 confere se o enunciado não supõe NTN-B
Principal em toda data de cupom como fato de mercado (alerta do briefing).

## Mapa de movimentos

| Seção do rascunho | Movimento | Ato do arco | O que prova |
|---|---|---|---|
| Abertura (sem H2) | 1 — Abertura (modo B) | Setup | Cobra a palavra do texto anterior ("replicar"), lança a moeda, nomeia a arbitragem, materializa em LTN 2029 × principal desmembrado da NTN-F 2029. Pergunta-âncora: o que obriga duas promessas idênticas a custarem o mesmo, e o que mais se tira daí? |
| A taxa não manda no preço | 2 — O Mito | Setup | A versão que circula, em duas metades (preço sai da taxa; arbitragem é qualquer convergência). Tese isolada: "**Preço não é opinião. É o custo da réplica.**" Promete o VP, a NTN-F e Black-Scholes. |
| A aposta que não sobrevive | 3 — A Anatomia | Setup → conflito | Definição de arbitragem (duas formas), o princípio como axioma, a Lei do Preço Único como primeira consequência, em fórmula. |
| ↳ A prova cabe numa LTN | 3 (cont.) | Conflito | Prova por absurdo com números: LTN a R$ 874,89 × principal a R$ 870,00 → R$ 4,89 hoje, zero depois. |
| ↳ Quem paga o ganha-ganha | 3 (cont.) | Conflito | Quem perde (quem cotou errado), por que a diferença fecha, e o ganha-ganha coletivo: equilíbrio. Fecha com a frase-sinal (§5.3): "Até aqui, é a primeira página de qualquer livro de renda fixa. O que sai dela é bem maior que a igualdade entre dois preços." |
| Preço sem opinião | 4 — O Lado de Lá (conceito: que problema resolve, e para quem) | Conflito → virada | Precificar sem saber preferências; a soma; o fator de desconto; a LTN como a peça; P = Σ CF · DF. "Ela não começou como matemática de valor presente. Começou com uma aposta que não sobrevive." |
| ↳ A mesma ideia, com mais matemática | 4 (cont.) | — | Black, Scholes e Merton (1973): a opção replicada; o retorno esperado ausente; o Nobel de 1997. Só menção (decisão do autor). Fecha devolvendo o texto à renda fixa. |
| Uma NTN-F feita de LTNs | 4 → clímax conceitual | Clímax | Portfólio equivalente; a NTN-F de 126/252/378 du; a tabela da réplica; PU justo R$ 943,88; TIR 14,53% abaixo dos 14,55%. "A TIR sai do preço, e não o contrário." Fecha a primeira metade do Mito. |
| ↳ A moeda aparece | 4 (cont.) | Clímax | O *dealer* que cota pela taxa do vencimento; a montagem com 100.000 NTN-F; +R$ 20.609,88, arredondamento, R$ 20.307,28 travados. Escala: cerca de 2 pontos-base. |
| ↳ A mesma conta, todo dia | 4 (cont.) | — | O mercado leva a decomposição a sério: o desmembramento (fecha o fio da abertura) e a ETTJ da ANBIMA (a Lei do Preço Único na prateleira inteira). |
| Nem toda convergência é arbitragem | 5 — O Ponto Cego, por contraste com o vizinho (trading de correlação) | Resolução, parte 1 | PETR3 × PETR4: mesma empresa, fluxos diferentes. Identidade × estatística. A pergunta-critério. LTCM, com link para o post da série. Fecha a segunda metade do Mito. |
| ↳ Os limites da arbitragem de verdade | 5 (cont.) | Resolução, parte 1 | Shleifer e Vishny (1997). Três atritos na NTN-F do exemplo: aluguel do papel, *spread*, data sem LTN (DI futuro). Os desvios de tela são, em geral, o preço desses atritos. |
| Antes de chamar de arbitragem | 8 — A Prateleira (que decisão real muda) | Resolução prática | Comparar preço com preço; bloco de planilha; as três perguntas; regra de decisão. CTA do Skill Check. |
| A moeda que ninguém lança duas vezes | 9 — Síntese + ponte (absorve o 7) | Fecho | Volta à moeda; o ganha-ganha de um vira o de todos; tese isolada; exercício da NTN-B; ponte para o *bootstrapping*; CTA de encaminhamento. |
| Para continuar aprendendo | 10 | — | 4 itens, 2 livros (Tuckman e Serrat; Cochrane), 1 artigo (Shleifer e Vishny), 1 metodologia (ANBIMA). Atende a §5.7. |

**Opcionais:** o 6 (Materialidade) fica de fora: o conceito não depende de escala, e uma série
(estoque de NTN-F, volume de desmembramento) não muda o argumento. O 7 é absorvido pelo 9: a
abertura é modo B, e o caso da LTN 2029 não é evento de mercado. O fecho volta à moeda. Confere
com a decisão 5 do rascunho.

**Observações estruturais para a etapa 5 (não são mudanças):**

- **O Mito tem duas metades, e elas são respondidas em lugares distantes.** A primeira (o preço
  sai da taxa) se fecha em "Uma NTN-F feita de LTNs" ("A TIR sai do preço"); a segunda
  (arbitragem é qualquer convergência) só em "Nem toda convergência é arbitragem", que a retoma
  por sinal explícito ("Volte à segunda metade do mito"). A etapa 5 avalia se o leitor guarda a
  segunda metade por quatro seções.
- **O movimento 4 tem três partes** (soma e fator de desconto; Black-Scholes; a réplica da NTN-F)
  e carrega o clímax. O desvio por Black-Scholes fica no meio, entre a fórmula e a réplica. É
  coerente com a decisão "só menção", e a seção termina devolvendo o texto à renda fixa. A etapa 5
  avalia se a quebra de ritmo compensa.
- **Abertura longa para o §3** (3–6 parágrafos): são cerca de 14 parágrafos curtos, com a moeda e
  a LTN 2029 em sequência. Ver alerta do briefing.
- **Onde o exemplo é hipotético.** A abertura usa títulos reais (LTN 2029, NTN-F 2029); a prova e
  a réplica usam títulos estilizados (um ano; 126/252/378 du), com aviso explícito ("Para
  simplificar a conta", "hipotética", "ilustrativas"). A etapa 5 confere se a passagem do real ao
  estilizado fica clara para o leitor.

## Três pilares

- **Dado:** a LTN de um ano a 14,30%; a réplica (três vértices, PU, TIR); a montagem de 100.000
  NTN-F; a Selic e a ordem de grandeza da curva de novembro de 2026; os 2 pontos-base. Tudo em
  cálculo próprio declarado, com a Selic e a curva como fonte.
- **Narrativa:** a moeda e o ganha-ganha em duas camadas; Black, Scholes, Merton e o Nobel; o
  LTCM (com o post da série).
- **Visual:** diag-01 e diag-02 (abaixo).

## Visuais — critério da etapa 2

O rascunho sugere: "diagrama da réplica, a NTN-F decomposta em três LTNs com quantidade e custo
de cada uma, ao lado do diagrama de fluxos da carteira de arbitragem (hoje +20,6 mil; vencimentos
zerados)". Pelo critério, são dois diagramas, um em cada subseção.

### diag-01 — a NTN-F decomposta em três LTNs

- **Onde:** "Uma NTN-F feita de LTNs", logo depois da tabela da réplica e antes de "Pela Lei do
  Preço Único, o PU (preço unitário) justo da NTN-F é R$ 943,88."
- **Por quê:** a tabela dá os números, mas não mostra a forma: cada fluxo da NTN-F é um lote de
  LTN da mesma data, e o preço da NTN-F é a soma dos três custos. É a imagem que o leitor precisa
  levar para o teste de transferência (NTN-B → NTN-B Principal).
- **Tipo pelo critério:** (1) não há série numérica real: são três fluxos de um exemplo
  estilizado, sem trajetória. (2) Há relação estrutural entre entidades (um título = soma de
  três), numa linha do tempo de fluxos → **diag**. O gráfico perde porque a métrica não é série
  real e o ponto é a decomposição, não a comparação de grandezas. O infográfico perde porque a
  peça isolada carrega a ideia.
- **Spec mínima para a etapa 8:** linha do tempo com hoje, 126, 252 e 378 du. À esquerda (ou em
  cima), a NTN-F com os três fluxos (R$ 48,81; R$ 48,81; R$ 1.048,81). À direita (ou embaixo), as
  três LTNs da mesma data com a quantidade (0,0488; 0,0488; 1,0488) e o custo de cada lote hoje
  (R$ 45,71; R$ 42,70; R$ 855,47), somando R$ 943,88. Manchete própria ("Três LTNs, a mesma
  NTN-F"). Fonte: cálculo próprio, taxas ilustrativas.

### diag-02 — os fluxos da carteira de arbitragem

- **Onde:** "A moeda aparece", depois do parágrafo do arredondamento e antes de "Nas três datas,
  os cupons e o principal da NTN-F pagam as LTNs vendidas."
- **Por quê:** é a moeda da abertura desenhada: dinheiro entra hoje, e nas três datas o que a
  NTN-F paga cobre o que as LTNs vendidas cobram. O leitor vê o "coroa, não perde".
- **Tipo pelo critério:** (1) não há série real: são quatro datas de um exemplo. (2) Fluxo entre
  duas pontas numa linha do tempo → **diag**. Gráfico e infográfico perdem pelo mesmo motivo do
  diag-01.
- **Spec mínima:** linha do tempo com hoje e as três datas. Hoje: −R$ 94,37 milhões (compra de
  100.000 NTN-F) e +R$ 94,39 milhões (venda das LTNs), líquido +R$ 20.609,88. Em cada data: a
  NTN-F paga, as LTNs cobram, líquido −R$ 115,18 (arredondamento dos lotes). Rodapé: lucro
  travado de R$ 20.307,28. Manchete própria ("Dinheiro hoje, nada a pagar depois" ou equivalente).
  Fonte: cálculo próprio.

**Por que dois, não um lado a lado.** Cada diagrama ilustra a tabela de uma subseção diferente,
e o painel duplo encolhe na largura do celular, onde a Substack mais é lida. Se o autor preferir
uma figura única com os dois painéis, é ajuste de gate na etapa 8.

**Ficam fora:** um gráfico da ETTJ real com os três vértices do exemplo. Há série real (ANBIMA),
mas o exemplo é estilizado por decisão do autor, e a curva de uma data fixa envelhece. O
*payoff* da moeda, também: a prosa carrega. Infográfico: nenhum gatilho.

## O que fica de fora

- A NTN-F 2029 real precificada na ETTJ (decisão do autor: estilizado).
- A derivação de Black-Scholes e a caixa da carteira *delta-hedge* (decisão do autor: só menção).
- O FIDC (cancelado).
- Materialidade (série de estoque ou de desmembramento).
- O "Para o pipeline", a checagem à mão e as notas de revisão do rascunho.
