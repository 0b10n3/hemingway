# Etapa 1 — Briefing

## Linha editorial

**Notas de um Professor.** O autor confirmou na etapa 0. O texto é de **matemática financeira**
(`docs/BACKWARDS_DESIGN.md` §4.2), e o que muda nos movimentos é isto: o 4 vira "de onde vem a
fórmula e qual hipótese ela embute" (seção "De onde vem o e", com dM/dt = jM e a hipótese de
reinvestimento instantâneo). O 5 vira "o caso em que a intuição quebra": a seção "Rende todo dia
não é render mais", e depois o erro de etiqueta no Black-Scholes. O 8 vira "a conta que o leitor
refaz na planilha" (a quarta pergunta e o bloco EFETIVA/NOMINAL/LN/EXP). A etapa 5 roda sem
validação argumentativa, e a 5a não roda.

## Voz

**Ensaística em registro técnico** (§4.1 do guia, com o rigor do §4.3), como no du252 e em "A
Corda e o Arco". Sinais no rascunho:
- primeira pessoa singular: "deixei uma conta para você", "eu mesmo apresentei", "Devo uma
  correção";
- pergunta retórica que carrega o argumento: "Mas sobe até onde?", "por que alguém se daria ao
  trabalho de trocar a etiqueta?";
- aforismo em parágrafo próprio: "O contínuo não compete com o composto. É o limite dele.",
  "Numa taxa efetiva, a frequência já foi paga.", "O perigo nunca foi a frequência. É a
  etiqueta.";
- CTA de encaminhamento no fim;
- ênfase em aspas simples ('Capitalizados mensalmente', 'mais agressivo', 'exponencial', 'rende
  todo dia'), sem negrito, com itálico só em *over* e em títulos de obra (regra 4).

**A etapa 4 dá mais peso à voz**, pelo precedente da etapa 0: o texto foi montado a partir da
pesquisa de pauta. Ela confere o texto contra `estilo/estilo-autoral.md` §3, §4.1 e §7.2, sem
reordenar o argumento. Memória pessoal não se inventa: a Pergunta 4 do rascunho (o e na
graduação) é do autor ou não entra.

## Tese em uma frase

A capitalização contínua não é um regime rival do composto, é o limite dele. Toda taxa composta
pode ser reescrita, sem aproximação, como uma taxa contínua menor (r = ln(1 + i)). A frequência
muda a etiqueta, não o motor, e a diferença que pesa no bolso vem de ler a etiqueta errada, não
de capitalizar mais vezes.

Aforismo do texto: "O contínuo não compete com o composto. É o limite dele." Aparece no Mito e no
Fechamento, de propósito (§5.4). O aforismo secundário, "O perigo nunca foi a frequência. É a
etiqueta.", fecha o movimento 5.

## Gancho

Modo B (moldura conceitual, §4.1), apoiado na continuidade de série. A abertura cobra a conta
que "A Corda e o Arco" deixou para o leitor ("Por que 12% ao ano capitalizados mensalmente viram
12,68% efetivos? E qual dos dois números você de fato paga?"), resolve a conta em três linhas e
a empurra até o limite ("E a cada segundo?"). Entra então Bernoulli, 1683, com 100% ao ano.

Bernoulli é um evento datado, mas não é caso de mercado. Por isso o movimento 7 não é
obrigatório, e o Fechamento retoma a escada ("o topo da escada"), absorvendo a função.

Pergunta-âncora, explícita no fim da abertura: o rendimento cresce sem limite se o ano é
cortado em pedaços cada vez menores? A resposta promete explicar duas coisas: por que o du/252 é
caso particular e por que o manual de opções da B3 usa outra taxa.

## Continuidade de série

O texto continua "A Corda e o Arco" (`posts/2026-11-02-a-barriga-da-curva/post.md`, publicado).
O que já foi dito lá e o que isso pede aqui:

- **Vocabulário:** régua = contagem de dias e base; motor = regime (linear/composto/contínuo). O
  rascunho respeita isso e acrescenta **etiqueta** (efetiva, nominal ou contínua) como terceiro
  termo. A etapa 4 confere que "motor" nunca aparece no sentido de "etiqueta".
- **O texto anterior já mostrou a identidade.** Ele já trazia "M = C e^{rt}, r = ln(1 + i)" e
  "Com r = ln(1,14) = 13,10%, o motor contínuo dá exatamente o mesmo montante que 14% compostos.
  Usar e elevado a (0,14 × t) … é calcular 15,03% ao ano sem perceber." Também fechava com
  "Nenhum dos três motores é o certo". O "Devo uma correção: dois deles são o mesmo" do rascunho
  exagera a distância entre os dois textos, e "Quem pega o DI futuro a 14% e coloca direto no
  modelo … está usando 15,03% ao ano sem perceber" quase repete a frase de lá. Isso vira a
  **Tensão — correção ou aprofundamento** (abaixo).
- **As três perguntas** do texto anterior são motor, base e dias que contam. O rascunho diz o
  mesmo ("motor, base, dias que contam"), então está coerente.
- **Formato de fórmula:** o post publicado usa `$$ … $$`, e o rascunho usa blocos ```` ```latex ````.
  A etapa 4 converte para o formato publicado.
- **Bibliografia:** Hull 11ª ed. e Assaf Neto 15ª ed. já estavam na lista anterior. Repetir é
  aceitável, já que são as referências do tema, mas a anotação precisa dizer o que cada um
  acrescenta aqui (frequência e contínua).
- **FIDC:** a promessa sai (decisão do autor na etapa 0). O fechamento termina sem anunciar
  o próximo texto. O que faz a ponte de série é o fim da série du/252 ("o expoente du/252 desta
  série está explicado de ponta a ponta").

## Briefing de funil (`../../strategy/FUNIL.md` §1 e §5)

- **Segmento:** `#GENZ-FEAR` e `#GENZ-GREED`, o estagiário ou analista júnior que sabe a
  fórmula mas nunca converteu uma taxa do DI para o modelo. O gancho da promessa para esse
  segmento é "provar competência rápido". Quem encaminha é o leitor `#Millennials-*`.
- **Estágio:** topo gratuito (§5).
- **Objetivo do post:** educar e fazer a lista crescer por encaminhamento. O CTA do rascunho
  ("encaminhe para quem ainda acha que o contínuo é o juro mais agressivo") já cumpre isso. O
  corpo não força menção a curso ou preço, e a oferta, se houver, é decisão da etapa 9a.

## Analogias e movimentos a preservar

Vieram do rascunho ou da série, não deste pipeline:

- **Corda / linha quebrada** (do texto anterior): as cordas encurtam com m e a linha quebrada
  tende à curva. É o elo com a série e o centro do graf-02.
- **A escada de Bernoulli**: degraus que sobem cada vez menos, com topo em 2,718. O Fechamento a
  retoma ("o topo da escada").
- **Etiqueta**: a taxa efetiva, a nominal e a contínua são etiquetas diferentes para o mesmo
  rendimento. É o termo novo da série.
- **A quarta pergunta** ("Qual é a etiqueta da taxa?"), que entra antes das três do texto
  anterior.
- **Regra de bolso**: dobrar a frequência corta pela metade a distância até o teto.

## Resolução dos marcadores da etapa 0

| # | Marcador | Resolução nesta etapa |
|---|---|---|
| 1 | Linha editorial | Resolvido na etapa 0. |
| 2 | Ficha de Saída | Etapa 2. |
| 3 | Título | **Tensão nomeada** (abaixo). |
| 4 | FIDC | Resolvido na etapa 0; a etapa 4 aplica. |
| 5 | "Devo uma correção" | **Tensão nomeada** (abaixo), agora com a evidência do texto anterior. |
| 6 | Profundidade (binômio, Black-Scholes) | **Tensão nomeada** (abaixo). |
| 7 | Linha pessoal sobre o e | **Tensão nomeada** (abaixo). |
| 8–9 | graf-01, graf-02 | Etapa 2 confirma pelo critério, etapa 8 produz. |
| 10–12 | `[VERIFICAR]` (Maor, eq. 1.5 da B3, seção do Hull) | Etapa 3 levanta, etapa 7 confere. |
| 13 | "Rende todo dia" genérico | Mantido genérico. |
| 14 | Ajustes à pauta | Incorporados. A frase sugerida para a nota do Substack vai ao gate. |
| 15–16 | Números e fatos | Etapa 7 (recalcular tudo; fonte primária). |
| 17 | Notas de processo | Fora do `post.md`. |

## Tensões registradas (perguntas nomeadas)

Vão ao autor enquanto a etapa 3 roda, como no precedente de "A Corda e o Arco", para a etapa 4
já escrever com as respostas.

**Tensão — título.** O movimento 0 pede que o deck carregue a tese. **(A)** "Quantas Cordas
Cabem num Ano?" (continua a imagem da corda), com deck "O contínuo não compete com o composto. É
o limite dele."; **(B)** "Capitalização Contínua vs. Composta" / "O Limite Matemático Que
Explica as Duas" (o título da Ficha; o "vs." contradiz a tese, que diz que não há rivalidade);
**(C)** outro.

**Tensão — correção ou aprofundamento.** "A Corda e o Arco" já mostrava r = ln(1,14) = 13,10% e
o erro dos 15,03%. **(A)** manter "Devo uma correção: dois deles são o mesmo" (honestidade
editorial, mas exagera: o texto anterior não errou, apresentou três motores e mostrou a
igualdade); **(B)** enquadrar como aprofundamento ("No texto anterior, uma linha dizia que
dois dos três motores davam o mesmo montante. Ela merece um texto."), corrigindo também a
abertura de "Mesma curva, outra etiqueta" e a frase repetida dos 15,03%.

**Tensão — profundidade (decisão 3 do `BACKWARDS_DESIGN.md`).** A demonstração do teto de 3
(binômio) e o exemplo numérico de Black-Scholes são os trechos mais técnicos. **(A)** ficam no
corpo como estão; **(B)** encurtam (o binômio vira uma frase com remissão ao apêndice do Maor e
o Black-Scholes fica só com a call); **(C)** vão para uma nota no fim.

**Tensão — a linha pessoal sobre o e.** O rascunho pede: "como o e apareceu para você na
graduação em Matemática? Encaixaria depois da escada de Bernoulli." O guia (§8) registra a
analogia autobiográfica ligada à formação em matemática como candidata a regra. **(A)** o autor
escreve a linha agora; **(B)** fica de fora; **(C)** `[PREENCHER]` no draft, para o autor
escrever no gate.

## Alertas para as etapas seguintes (não são decisões)

- **"Quase cinquenta anos depois"**: Bernoulli escreveu em 1683 e a carta de Euler é de 1731,
  48 anos depois. A etapa 7 confere a data e se a notação e é de fato da carta a Goldbach ou de
  outra fonte (há quem cite 1727/1728, *Meditatio*).
- **"Cada fatorial cresce mais rápido que as potências de 2"**: a cota precisa de 1/k! ≤
  1/2^(k−1) para k ≥ 1, e o texto diz "a partir do terceiro termo, a soma fica abaixo de 1/2 +
  1/4 + …". A etapa 7 confere a indexação, porque o terceiro termo é 1/2! = 1/2.
- **"Cada vez que se dobra a frequência, a distância até o teto cai quase exatamente pela
  metade"**: a etapa 7 testa com m = 1, 2, 4, …, 365 a 14%. A distância é ≈ j²/(2m)·e^j, então a
  regra vale para m grande.
- **Black-Scholes**: recalcular a call e a put com S = K = 100, σ = 25%, T = 1, r = 13,10% × 14%
  e o "103 pontos-base" (15,03 − 14,00).
- **Poupança**: 0,5% ao mês dá 6,17% efetivo e ln(1,0617) = 5,99%. O "6% ao ano" da poupança é
  nominal com m = 12.
- **Glosas na primeira ocorrência** (regra 1; §5.1), para a etapa 6: CDB (glosado), DI/CDI
  (glosado), DI1, B3, ETF (glosado), Black-Scholes-Merton (glosado), taxa a termo (glosada),
  volatilidade (glosada), ponto-base (glosado), LTN (glosada), PU, TR (glosada), Selic
  (glosada), MacTutor.
- **Seis blocos LaTeX e dois blocos de planilha.** A Substack renderiza LaTeX em bloco. O
  separador `;` e os nomes pt-BR (EFETIVA, NOMINAL, TRUNCAR) são do Excel em português; a etapa 7
  confere.
- **graf-01 não veio no arquivo** ("embedded content"). A etapa 8 reconstrói a partir da fórmula.
- **Tamanho:** cerca de 2.600 palavras de prosa publicável. Não há pedido de corte, mas a tensão
  de profundidade pode encurtar.

## Respostas do autor às tensões (2026-11-09, durante a etapa 3)

- **Título:** "Frequência de Capitalização" (o H1 do rascunho). O movimento 0 pede deck com a
  tese, então a etapa 4 usa como subtítulo provisório "O limite matemático que explica o
  composto e o contínuo" (o da Ficha, sem o "vs."). A troca é decisão do gate.
- **Correção ou aprofundamento:** aprofundamento. O "Devo uma correção" sai, e a abertura de
  "Mesma curva, outra etiqueta" e a frase repetida dos 15,03% são ajustadas para remeter ao texto
  anterior em vez de repeti-lo.
- **Profundidade:** o binômio e o Black-Scholes ficam no corpo, como estão.
- **Linha pessoal sobre o e:** fica de fora. O marcador nº 7 está resolvido, sem `[PREENCHER]`.
