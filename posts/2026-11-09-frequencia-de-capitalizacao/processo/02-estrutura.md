# Etapa 2 — Estrutura

O rascunho já chega estruturado, e o pipeline não reordena a argumentação. Esta etapa confere a
estrutura contra o backward design, mapeia os movimentos e decide os visuais pelo critério.
Proposta de mudança estrutural, se houver, vira pergunta ao autor.

## Ficha de Saída (`docs/BACKWARDS_DESIGN.md` §2)

Adotada do rascunho. Dois ajustes: o campo 8 sem o FIDC (decisão do autor na etapa 0) e o campo
6 ganha uma referência a ser conferida na etapa 7.

| Campo | Conteúdo |
| --- | --- |
| 1. Competência de saída | *Converter* uma taxa entre nominal com m capitalizações, efetiva anual e contínua; *avaliar* se a diferença de frequência é relevante para a taxa e o prazo em jogo; *traduzir* a taxa do DI para a entrada de um modelo (r = ln(1 + i), T = du/252). |
| 2. Teste de transferência | A poupança: 0,5% ao mês, mais TR, quando a meta da Selic está acima de 8,5% ao ano (Lei nº 12.703/2012). O leitor deve dizer sozinho por que "6% ao ano" é uma taxa nominal, quanto ela vale efetiva (6,17%) e quanto vale contínua (5,99%). |
| 3. Tese de fundo | "O contínuo não compete com o composto. É o limite dele." É da mesma família da tese-mãe da série, "capitalização não é lei da natureza, é cláusula" (texto anterior). |
| 4. Erro-alvo | Achar que a capitalização contínua é um regime à parte, mais agressivo ou mais preciso que o composto, e que capitalizar com mais frequência ("rende todo dia") sempre aumenta o rendimento de forma relevante. |
| 5. Ferramenta prática | A quarta pergunta antes de qualquer taxa (efetiva, nominal ou contínua?); as conversões nominal ↔ efetiva ↔ contínua; as funções EFETIVA, NOMINAL, LN e EXP; r = ln(1 + i) e T = du/252 para Black-Scholes; e a regra de bolso: dobrar a frequência corta pela metade a distância até o teto. |
| 6. Âncora de autoridade | Jacob Bernoulli, 1683 (MacTutor, Universidade de St Andrews); Manual de Apreçamento de Opções da B3, eq. (1.5) [conferir versão vigente, etapa 7]; especificação do DI1 (taxa efetiva anual, base 252); Hull, cap. 4. |
| 7. Os dois lados do balcão | De um lado, quem cota a taxa: o credor que cota nominal, a B3 e as tesourarias em efetiva 252, a mesa de opções em contínua. Do outro, quem paga ou recebe a diferença: o tomador do financiamento, o investidor, quem compra ou vende a opção. O distribuidor aparece só de passagem, no "rende todo dia" (§4.3: nenhuma das três condições se verifica, então não ganha bloco). |
| 8. Ponte de série | Vem de "A Corda e o Arco", cujo fecho prometia frequência, 12,68% e o teto de 15,03%. **Aponta para:** o fim da série du/252, sem anunciar o próximo texto (o FIDC foi cancelado). |

**Verificação: a sequência entrega o campo 1?**

| Competência | Onde o texto a produz |
|---|---|
| nominal → efetiva | "Nominal, frequência, efetiva" (fórmula + 12% → 12,68%) |
| efetiva → contínua (e volta) | "De onde vem o e" → "Mesma curva, outra etiqueta" (r = ln(1 + i), identidade, escada de nominais equivalentes) |
| avaliar se a frequência pesa | "Rende todo dia não é render mais" (R$ 9.342 → 887 → 45; regra de bolso) e o bloco de decisão em "Uma pergunta antes das outras três" |
| DI → modelo | "Por que a mesa de opções fala contínuo" (eq. 1.5 da B3) + "Onde mora o erro" (exemplo numérico) |
| teste de transferência (poupança) | Fechamento. Exige só nominal → efetiva → contínua, que o leitor já viu com os 12%. |

Entrega. A única lacuna possível: o teste pede "quanto vale contínua", e o texto só mostra a
conversão contínua a partir da efetiva (ln(1 + i)). O caminho direto da nominal mensal, 12 ×
ln(1,005), dá o mesmo número e não precisa entrar. O leitor passa pela efetiva. Não muda nada.

## Mapa de movimentos

| Seção do rascunho | Movimento | Ato do arco | O que prova |
|---|---|---|---|
| Abertura (sem H2) | 1 — Abertura (modo B) | Setup | Cobra a conta deixada no texto anterior (12,68%), resolve, empurra ao limite. Pergunta-âncora: o rendimento cresce sem limite? Bernoulli, 1683. |
| Dois motores rivais | 2 — O Mito | Setup | A versão que circula (composto = mundo real, contínuo = outro bicho, mais agressivo ou mais preciso). A tese fica isolada: "O contínuo não compete com o composto. É o limite dele." |
| Nominal, frequência, efetiva | 3 — A Anatomia | Setup → conflito | j, m, j/m e i; a fórmula; a over do texto anterior como nominal. |
| ↳ A escada de Bernoulli | 3 (cont.) | Conflito | Os degraus encolhem; teto ≤ 3 pelo binômio; topo em e. Fecha com a frase-sinal (§5.3): "Até aqui, é o capítulo de taxas equivalentes de qualquer livro… O interessante começa…". |
| De onde vem o e | 4 — O Lado de Lá (versão mat. fin.: de onde vem a fórmula e qual hipótese embute) | Conflito | Escada elevada a j → e^j; dM/dt = jM; a hipótese de que nenhum centavo fica parado. |
| ↳ Mesma curva, outra etiqueta | 4 (cont.) → virada | Clímax conceitual | (1 + i)^t = e^{rt}: identidade, não aproximação. Escada de nominais equivalentes, 14,000 → 13,103. A fama de "mais agressivo" vem de comparar o mesmo número nas duas etiquetas. |
| ↳ Um aviso de vocabulário | 4 (cont.) | — | "Exponencial" na B3 = composto; no manual de opções = contínuo. "As duas são exponenciais." |
| Rende todo dia não é render mais | 5 — O Ponto Cego (o caso em que a intuição quebra), por contraste com o vizinho: a taxa nominal | Resolução, parte 1 | O ganho de frequência some rápido (R$ 9.342 / 887 / 45). Na taxa efetiva (DI), a frequência já foi paga, e o erro de varejo é ler efetiva como nominal. |
| Por que a mesa de opções fala contínuo | 4b — dois lados do balcão (quem cota em contínua e por quê) | Resolução, parte 2 | Manual B3: r = ln(1 + TPre), T = DU/252. Três conveniências: soma, cálculo, volatilidade log. Hull: "conveniência, não precisão". |
| ↳ Onde mora o erro | 5b — o ponto cego que custa dinheiro | Resolução, parte 2 | DI a 14% direto no modelo = 15,03%. Call +3,1%, put −6,0%. Frequência < 0,5 pb × etiqueta 103 pb. Aforismo: "O perigo nunca foi a frequência. É a etiqueta." |
| Uma pergunta antes das outras três | 8 — A Prateleira (a conta na planilha) | Resolução prática | Quarta pergunta, regra de decisão em três casos, bloco de planilha, regra de bolso, truncamento da LTN. |
| Fechamento: o topo da escada | 9 — Síntese + ponte (absorve o 7) | Fecho | Tese repetida isolada; teste de transferência (poupança); fim da série du/252; CTA. |
| Para continuar aprendendo | 10 | — | 4 itens, 3 livros (Maor, Hull, Assaf Neto) + MacTutor. Atende a §5.7. |

**Opcionais:** o 6 (Materialidade) fica de fora, porque o instrumento é conceitual e não há série
que mude o argumento. O 7 é absorvido pelo 9, porque a abertura é modo B e Bernoulli é
retomado como "o topo da escada".

**Observação estrutural para a etapa 5 (não é mudança):** o movimento 4 aparece em duas partes
("De onde vem o e" e "Por que a mesa de opções fala contínuo"), com o 5 no meio. Isso é
coerente com §3 ("os movimentos 4 e 5 se invertem sem prejuízo"): o primeiro 4 é a origem da
fórmula, o segundo é o lado de quem cota em contínua. A etapa 5 avalia se o leitor sente a volta.

## Três pilares

- **Dado:** os números de Bernoulli, a escada de nominais equivalentes, os R$ 9.342 / 887 / 45, o
  Black-Scholes, a poupança. Tudo em cálculo próprio declarado, mais o DI1 e o manual da B3 como
  fonte.
- **Narrativa:** Bernoulli, 1683, até Euler, com a pergunta empurrada ao limite; a correção ou
  aprofundamento da série (tensão).
- **Visual:** graf-01 e graf-02 (abaixo).

## Visuais — critério da etapa 2

**Renumeração pela ordem de aparição.** No rascunho, o graf-02 (Bernoulli) aparece antes do
graf-01 (convergência a 14%). A proposta é renumerar: **graf-01 = linha quebrada de Bernoulli**,
**graf-02 = convergência da efetiva para o teto a 14%**. A etapa 4 aplica. A mudança é só de
rótulo.

### graf-01 — a linha quebrada de Bernoulli (era graf-02)

- **Onde:** "A escada de Bernoulli", logo depois dos números da escada.
- **Por quê:** o texto afirma que cada linha quebrada fica abaixo da seguinte e todas abaixo da
  curva. O gráfico mostra isso e faz a ponte visual com a "corda" do texto anterior.
- **Tipo pelo critério:** (1) há série numérica real: o montante de 1 a 100% ao ano, em t ∈ [0,
  1], para m = 1, 2, 4, 12 e para o contínuo, com valores exatos nos nós (2; 2,25; 2,4414; 2,6130;
  2,7183). → **graf**. O diagrama perde porque há métrica real por trás das formas: o montante, e
  as alturas finais são o argumento. Não cabe infográfico, porque a peça isolada carrega a ideia.
- **Spec mínima para a etapa 8:** eixo x de 0 a 1 ano; eixo y é o montante; quatro linhas
  quebradas (cordas lineares entre os nós k/m) e a curva e^t; rótulo do valor final em cada uma.
  Manchete própria ("Mais cordas, mais perto da curva, nunca acima dela") e fonte "cálculo
  próprio".

### graf-02 — convergência da efetiva para o teto (era graf-01)

- **Onde:** "Rende todo dia não é render mais", depois de "Volte aos 14% nominais e suba com eles
  a escada de Bernoulli."
- **Por quê:** o parágrafo seguinte cita os ganhos em reais de cada degrau. Sem o gráfico, o
  leitor não vê o degrau encolher.
- **Tipo pelo critério:** (1) série numérica real: a efetiva (1 + 0,14/m)^m − 1 para m = 1, 2,
  4, 12, 52, 252, 365, com a assíntota e^0,14 − 1 = 15,03%. → **graf**. O diagrama e o infográfico
  perdem pelo mesmo motivo do graf-01.
- **Spec mínima:** eixo x em m (escala log ou categórica com os rótulos anual / semestral / mensal
  / semanal / diária), eixo y é a taxa efetiva, linha tracejada horizontal no teto 15,03%, pontos
  rotulados. Manchete: "Cada degrau sobe menos que o anterior". Fonte: cálculo próprio. A etapa
  8 reconstrói os dados (o "embedded content" não veio).

**Fica fora:** o exemplo de Black-Scholes, como gráfico. Só dois números por cenário, e a prosa
carrega. Infográfico também fica fora: nenhum gatilho.

## O que fica de fora

- A comparação 252 × 360 × 365, que é régua e já saiu nos dois textos anteriores (decisão do
  montador, mantida).
- "Primeira vez que um número foi definido por um processo de limite" (MacTutor), que não foi
  confirmada.
- A ANBIMA "exponencial de dias", trocada pela metodologia do Tesouro.
- A Susep e a ETTJ contínua, já citadas no texto anterior.
- O FIDC.
