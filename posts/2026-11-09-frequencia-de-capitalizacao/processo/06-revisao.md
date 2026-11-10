# Etapa 6 — Revisão de linha e norma

Executor: subagente `revisor-gramatical`. Texto: corpo de `processo/04-draft-v2.md`. Conferido
contra `estilo/estilo-autoral.md` (§3, §4.1, §7), os antipadrões e o vocabulário de "A Corda e o
Arco". Não toca estrutura nem números.

Classes: `norma` = erro objetivo de norma culta ou da regra 1 (inegociável); `linha` = clareza,
ritmo ou leitura em voz alta (sugestão).

**Sem achado:** crase; negrito/itálico de ênfase (itálico só em *over* e em títulos); vocabulário
da série ("motor" nunca no sentido de "etiqueta"); glosas de du/252, CDI/DI, ETF, BSM, taxa a
termo, volatilidade, ponto-base, preço de exercício, call/put, Selic, TR; fragmentos de voz ("A
14%.", "Pode ignorar.").

## Diff comentado

| # | Classe | Atual | Proposta | Motivo |
|---|---|---|---|---|
| 1 | linha | "Cada corte a mais põe o juro para render mais cedo (…) que, a 14%, ele nunca passa de 15,03%." | "Cada corte a mais no ano faz o juro render mais cedo (…) que, a 14%, o rendimento nunca passa de 15,03%." | "corte" sem objeto; regência frouxa; "ele" ambíguo |
| 2 | norma | "que nenhum CDB jamais cotou" | "que nenhum CDB (Certificado de Depósito Bancário) jamais cotou" | Primeira ocorrência de CDB |
| 3 | norma | "o manual de opções da B3 faz" | "o manual de opções da B3, a bolsa brasileira, faz" | Primeira ocorrência de B3 |
| 4 | norma | "CDB (Certificado de Depósito Bancário), Tesouro, financiamento." | "CDB, Tesouro, financiamento." | A glosa subiu (item 2) |
| 5 | linha | "é a proporcional, j/m," | "é a taxa proporcional, j/m," | Nome técnico |
| 6 | linha | "1,01 elevado a 12, 12,68%." | "1,01 elevado a 12, ou 12,68%." | Leitura em voz alta |
| 7 | norma | "da *over* ao mês do texto anterior, a taxa do dia multiplicada por 30." | "da *over* ao mês do texto anterior, em que a taxa das operações de um dia é multiplicada por 30." | *over* sem glosa neste texto |
| 8 | linha | "numa linha quebrada, e quanto maior o m, mais curtas" | "numa linha quebrada e, quanto maior o m, mais curtas" | Padroniza com "E, quanto maior o n," |
| 9 | linha | "um capital de 1 a 100% ao ano" | "um capital de 1, aplicado a 100% ao ano" | "de 1 a 100%" lido como intervalo |
| 10 | linha | "Com doze, 2,61." | "Com 12, 2,61." | Consistência com 52 e 365 (opcional) |
| 11 | norma/linha | alt graf-01: "Capital de 1 a 100% ao ano, de zero a um ano. (…) terminam em 2, 2,25, 2,44 e 2,61." | "Capital de 1 aplicado a 100% ao ano, ao longo de um ano. (…) terminam em 2; 2,25; 2,44 e 2,61." | Série com decimais; ambiguidade |
| 12 | norma | "quando se troca os 100%" | "quando se trocam os 100%" | Concordância na passiva sintética |
| 13 | norma | "o capítulo de taxas equivalentes de qualquer livro" | "o capítulo de taxas equivalentes (taxas diferentes que entregam o mesmo rendimento) de qualquer livro" | Regra 1 |
| 14 | linha | "Para um prazo t qualquer, o montante" | "Para um capital C e um prazo t quaisquer, o montante" | C indefinido neste texto |
| 15 | linha | "o saldo cresce, em cada instante, a uma velocidade" | "o saldo, M, cresce a uma velocidade" | Eco "a cada/em cada instante"; M sem nome |
| 16 | linha | "na mesma velocidade do próprio valor" | "a uma velocidade igual ao próprio valor" | Precisão |
| 17 | linha | "É a hipótese do composto do texto anterior, que já supunha o juro reinvestido à mesma taxa." | "É a hipótese que o texto anterior já atribuía ao composto: o juro reinvestido à mesma taxa." | "que" ambíguo |
| 18 | norma | "nenhuma das duas etiquetas é mais precisa" | "nenhuma das duas etiquetas, os dois jeitos de cotar a mesma taxa, é mais precisa" | "Etiqueta" usada antes de definida (ver S2) |
| 19 | linha | "Não existe uma fronteira entre o composto e o contínuo. Existe uma escada…" | "Entre o composto e o contínuo, o que existe é uma escada…" | Tique "não X. Y." |
| 20 | linha | "O que muda é o número cotado, não o motor." | "Para o mesmo rendimento, o que muda é o número cotado, não o motor." | Contradição aparente com "o mesmo número" |
| 21 | linha | aspas simples nas citações literais da B3 | aspas duplas nas citações literais; simples só em 'exponencial' | Separar ênfase de citação |
| 22 | linha | "As duas são exponenciais." | "As duas taxas são exponenciais." | Referente |
| 23 | linha | "Em R$ 1 milhão por um ano, (…) Da diária para a contínua, R$ 44,72." | "Em R$ 1 milhão aplicado por um ano, (…) Da diária para a contínua, mais R$ 44,72." | Clareza; paralelismo |
| 24 | linha | "O rotativo (…) custou 451,7% (…), segundo o Banco Central, cerca de 15,3% ao mês." | "Segundo o Banco Central, o rotativo (…) custou 451,7% ao ano em setembro de 2026, o equivalente a cerca de 15,3% ao mês." | Atribuição |
| 25 | linha | "Se esses 15,3% fossem capitalizados todo dia" | "Se a mesma taxa nominal, 12 × 15,3%, ou 183,5% ao ano, fosse capitalizada todo dia" | Evitar leitura de 15,3% ao dia (etapa 7 confirma 183,53%) |
| 26 | linha | "Isso desmonta uma frase comum de propaganda" | "Agora, uma frase comum de propaganda" | A anáfora quebrou com a inserção do cartão (S1) |
| 27 | linha | "o fator de cada dia útil é 1,14 elevado a 1/252: 0,05201% ao dia" | "a taxa de cada dia útil é 1,14 elevado a 1/252, menos 1: 0,05201% ao dia" | Fator ≠ taxa |
| 28 | norma | "a metodologia dos prêmios de referência das opções listadas" | "a metodologia dos prêmios de referência (os preços que a B3 calcula para cada opção) das opções negociadas em bolsa" | "prêmio" e "listadas" sem glosa |
| 29 | norma/linha | "não é a do DI futuro como cotada. É a tradução dela:" | "é a do DI futuro, o contrato futuro da B3 sobre a taxa DI, traduzida:" | Glosa na primeira ocorrência; tique |
| 30 | norma/linha | "do DI1, o contrato futuro da B3 sobre a taxa DI, cotado (…). DUₙ são os dias úteis" | "do DI1 (o código do DI futuro na B3), cotado (…). DUₙ é o número de dias úteis" | Consequência do item 29; precisão |
| 31 | linha | "= 26,21%, e e elevado a" | "= 26,21%; e elevado a" | "e e" trava (ver etapa 7, B1) |
| 32 | linha | "O desconto que encaixa nela" | "O desconto que se encaixa nela" | Regência |
| 33 | linha | "dos retornos logarítmicos, o logaritmo da razão entre dois preços, que é" | "dos retornos logarítmicos (cada um, o logaritmo da razão entre dois preços seguidos, que é o retorno em taxa contínua)" | Aposto singular em plural |
| 34 | norma/linha | "John Hull, no capítulo (…) do seu manual de derivativos, um dos mais usados (…) usadas extensivamente na análise de derivativos" | "John Hull escreveu um dos manuais de derivativos (contratos cujo valor depende de outro ativo, como as opções) mais usados no mercado. No capítulo de taxas de juros, ele registra que as taxas contínuas são amplamente usadas na análise desses contratos [VERIFICAR: …]." | Glosa; anglicismo; repetição; "seu" ambíguo |
| 35 | linha | "volatilidade de 25% ao ano e um ano, 252 dias úteis, até o vencimento" | "volatilidade de 25% ao ano e vencimento em um ano (252 dias úteis)" | Prazos embaralhados |
| 36 | linha | "o preço justo hoje para entregá-la" | "o preço justo, combinado hoje, para entregá-la" | "justo hoje" = "logo hoje" |
| 37 | linha | "sai 6,0% mais barata, R$ 4,18 contra R$ 4,44" | "sai a R$ 4,44 com r = 13,10% e a R$ 4,18 com r = 14%: 6,0% mais barata" | Simetria com a call (opcional) |
| 38 | linha | "Ninguém errou a taxa. Errou a etiqueta." | "A taxa estava certa. A etiqueta, errada." | O sujeito oculto de "Errou" é "ninguém"; antecipa o aforismo. A frase atual foi decisão do autor (M7), por isso é sugestão |
| 39 | linha | "valia menos de meio ponto-base (o centésimo de ponto percentual)" | "vale menos de meio ponto-base (um centésimo de ponto percentual)" | Paralelismo de tempo; definição |
| 40 | linha | "nominal e a outra efetiva" | "nominal e a outra, efetiva" | Vírgula de elipse |
| 41 | linha | "O erro da etiqueta é da ordem de um ponto percentual." | "A taxas da ordem do DI, o erro da etiqueta é da ordem de um ponto percentual." | Alcance |
| 42 | linha | "a precisão de que você precisa" | "a precisão que o seu caso exige" | Eco |
| 43 | norma/linha | "o preço de uma LTN de um ano em quase R$ 0,04, e o Tesouro manda manter seis casas decimais. (…) para a LTN (Letra do Tesouro Nacional, o título público prefixado), (…) e o preço unitário, na 6ª." | "muda em quase R$ 0,04 o preço de uma LTN (Letra do Tesouro Nacional, o título público prefixado) de um ano, que paga R$ 1.000 no vencimento. (…) para a LTN, (…) e o PU (preço unitário), na 6ª." | Glosa na 1ª ocorrência; PU; redundância |
| 44 | linha | "e a escada tem topo. Bernoulli provou em 1683 que ela tem topo" | "cada corte rende menos que o anterior. Bernoulli provou em 1683 que a escada tem topo" | Repetição (ver etapa 7, I6) |
| 45 | linha | "A frequência não muda o motor. Muda a etiqueta." | "A frequência só muda a etiqueta." | Duas negações seguidas antes do aforismo |
| 46 | norma | "uma taxa que todo brasileiro já ouviu" | "uma taxa de que todo brasileiro já ouviu falar" | Regência |
| 47 | linha | "Por que "a poupança rende 6% ao ano" é uma taxa nominal? Quanto ela vale efetiva?" | "Por que os 6% ao ano que se costuma atribuir à poupança são uma taxa nominal? Quanto ela vale como taxa efetiva?" | A frase citada não é uma taxa |

Bibliografia: nada de norma.

## Tique "não X. Y."

São cerca de 11 ocorrências. Ficam as que são tese ou matemática: o aforismo principal (2×), "Não
é uma aproximação. É uma identidade.", o aforismo secundário, "A B3 não trocou de motor.", "A
escolha é de conveniência, não de precisão." e "O que muda é o número cotado, não o motor." Os
itens 19, 29, 38 e 45 tiram quatro.

## Sinais estruturais (para o orquestrador ou o gate)

- **S1.** O cartão (M6) ficou entre "some rápido" e a propaganda do "rende todo dia". A sequência
  agora é: pesa pouco → pesa muito no cartão → propaganda. Pode valer conferir a ordem.
- **S2.** "Etiqueta" aparece no H3 e no parágrafo seguinte antes da frase-mapa que a define. O
  item 18 resolve com glosa. Mover a frase-mapa seria decisão estrutural.
- **S3.** O deck está no corpo, em itálico. No post publicado, ele vai em `subtitulo:` no
  front-matter (consolidação).
- **S4.** "Texto anterior"/"último texto" aparece cerca de 13 vezes. Sugestão: nomear e linkar "A
  Corda e o Arco" na primeira menção.
