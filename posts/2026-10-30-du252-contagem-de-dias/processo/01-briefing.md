# Etapa 1 — Briefing

## Linha editorial

**Notas de um Professor.** O front-matter do rascunho declara `linha: Notas de um Professor`
(chave fora do contrato, `linha_editorial`), e o autor confirmou na etapa 0. O conteúdo bate
com a linha: conceito e mecanismo técnico (convenção de contagem de dias e capitalização),
sem relato de carreira. Pelo `docs/BACKWARDS_DESIGN.md` §4.2, o post é do tipo **matemática
financeira**, com uma perna de modelagem (o código). Consequências: Ficha de Saída na etapa 2,
etapa 5 sem validação argumentativa, etapa 5a não roda.

## Voz

**Ensaística, em registro técnico** (§4.1 do guia, com o rigor do §4.3). Os dois posts
anteriores da linha (CRI/CRA, debêntures) foram em voz explicativa. Este rascunho escolhe
outra coisa, e a escolha é do autor, não do pipeline:

- Primeira pessoa singular de opinião e de memória: "A explicação que mais me ajudou não está
  em nenhuma fórmula", "Agora a parte que eu acho mais bonita", "Quatro armadilhas que já vi
  em código de gente boa", e o espaço reservado para a memória pessoal (marcador #5).
- Tem tese contestável e erro-alvo: "Errado é ler um número com a régua do outro."
- Ironia leve, sempre na abertura ou em transição, nunca em cima de número (§5.5 do
  `BACKWARDS_DESIGN.md`): "O problema do professor é que ele esquece que foi aluno.", "o
  calendário continua não colaborando", "Se o seu código usa o calendário da B3, ele tem dois
  meses de vida."
- Fecha com CTA de compartilhamento e comentários (marcador #6), como pede o §4.1.

Não é tensão, é registro para a etapa 6 não "explicativizar" o texto por reflexo de série.
Se o autor quiser alinhar à voz dos dois posts anteriores, isso é pedido dele no gate.

**Atenção para a etapa 6:** o rascunho tem muito negrito. Há três usos diferentes, e a etapa
6 trata cada um pela regra 4 do guia, como conversão regrada e não como tensão (precedente:
`2026-09-28-o-certificado-nao-muda-o-devedor`):
1. Negrito de ênfase no meio da frase: "**régua**", "**motor**", "**anual, base 252 dias
   úteis**", "**11,85%**", "**40 dias úteis**", "**22 dias úteis**", "**quinta-feira,
   19/11**", "**régua DU/252 com motor composto**", "**um dia útil**", e outros. Sai.
2. Rótulo no início de item de lista ou parágrafo: "**Armadilha 1: …**", "**Calendário
   ANBIMA**", "**1. Feriados de São Paulo (até 2021).**", "**Lá fora, o juro não descansa.**",
   "**Valor aplicado:**" e os rótulos das quatro perguntas finais. A etapa 6 decide se o
   rótulo vira H3, texto simples com dois-pontos (regra 3) ou fica.
3. Linha em destaque da tabela do CDB (o contratado). Vai para a etapa 8, que decide o
   destaque visual na peça.

Itálico: *day count* e *du* são estrangeirismo e variável (permitidos). "*o juro correu
hoje?*" e "*a bolsa abriu hoje?*" são ênfase (regra 4). A "Nota de rigor" inteira em itálico
dentro de citação é formatação de bloco, e a etapa 6 decide.

## Tese em uma frase

"12% ao ano" não é informação completa: uma taxa só vira dinheiro com uma régua (contagem de
dias), um motor (capitalização) e um calendário; no Brasil a combinação é DU/252 composto
sobre o calendário bancário da ANBIMA, e ler o mesmo número com a régua ou o calendário de
outra pergunta gera erro de dinheiro, não de arredondamento.

Em forma de aforisma, a do próprio autor: "antes de perguntar quanto rende, pergunte em que
régua."

## Gancho

A LTN (Letra do Tesouro Nacional, o título público prefixado; o rascunho não glosa a sigla,
ver alertas) comprada a 12% ao ano no primeiro dia útil de 2026 que entrega 11,85% até
01/01/2027. É um dado, não uma cena, seguido de duas frases curtas que desarmam a suspeita de
erro ("Ninguém errou a conta. Ninguém ficou com a diferença.") e da explicação em uma linha
("Faltaram três."). Pelo §4.1 do `BACKWARDS_DESIGN.md`, é **modo B** (proposição
contraintuitiva com número), não modo A, porque não há evento datado. O rascunho fecha o
loop do gancho no meio do texto ("É daí que vem a LTN do começo do texto"), e não no fim.
Combina com o movimento aspiracional §5.8 (Gladwell: validar a intuição, "12% ao ano rende
12% em um ano", antes de desmontá-la).

A pergunta-âncora é o primeiro intertítulo: "'12% ao ano' de quê?"

## Analogias e movimentos do autor a preservar (vieram do rascunho, não do pipeline)

- **A régua e o motor.** Eixo central: contagem de dias (régua, devolve τ) e capitalização
  (motor, devolve o fator) são peças independentes, e o mercado monta combinações. Volta na
  tabela do CDB ("lido com réguas e motores diferentes") e no fecho ("pergunte em que
  régua").
- **"Uma taxa de juros, sozinha, … É um número esperando uma régua."**
- **O dia financeiro é o intervalo entre duas liquidações.** "O fim de semana não é de graça.
  Ele está embutido no período da sexta." É a explicação causal do DU/252, e o autor a
  apresenta como a que mais o ajudou.
- **"252 é uma convenção, não uma contagem."** E "A taxa é a mesma. O ano é que muda de
  tamanho."
- **Taxas equivalentes invertidas:** "Mesmo dinheiro, quatro números. Nenhum está errado.
  Errado é ler um número com a régua do outro." É a tese isolada no meio do texto.
- **ANBIMA × B3 como duas perguntas:** "o juro correu hoje?" × "a bolsa abriu hoje?".
- **"O calendário tem data de validade."** (Armadilha 4.)
- **"Outros relógios"**, com o terceiro relógio, a rolagem. A metáfora muda de régua/motor
  para relógio na seção final. Fica como alerta para a etapa 5 (abaixo), sem decisão aqui.
- **"O problema do professor é que ele esquece que foi aluno."** Ponte para o espaço da
  memória pessoal e assinatura da linha editorial.
- Fontes já trazidas pelo autor: Circular BCB nº 2.761/1997, Márcio Garcia (PUC-Rio, 1997),
  Resolução CMN nº 4.880/2020, Lei nº 14.759/2023, ANBIMA (metodologias), B3 (treinamento DI,
  OC 055/2024-PRE), `bizdays` (Wilson Freitas), pandas. O pipeline não troca nenhuma nesta
  etapa. A etapa 3 confere e a etapa 7 verifica.

## Encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §3.3, §3.4, §5)

Substack é nutrição de lista. O texto fala com dois públicos de propósito ("Se essa frase
soou estranha, este texto é para você. Se soou óbvia, talvez ele seja para o júnior que senta
do seu lado."):

- **`#GENZ-FEAR` e `#GENZ-GREED`**, o público do curso gratuito ao vivo (§3.4). Bianca
  (estagiária de *middle office*, "saber a teoria" × "saber fazer o que o analista pede") e
  Pedro (analista de renda fixa) são o leitor de "este texto é para você". O tema é
  literalmente o do curso gratuito, Fundamentos do Valor do Dinheiro no Tempo.
- **`#Millennials-*`** como leitor que encaminha. Camila (tesouraria, Python) é a leitora das
  armadilhas de código.

A ponte de produto é o core offer "Profissional de Renda Fixa" (§5): as duas trilhas, "Renda
Fixa — Títulos Públicos e Privados" (LTN, PU, calendário) e "Fundamentos Matemáticos para
Finanças" (régua, motor, taxas equivalentes). O CTA sugerido pelo autor (encaminhar para quem
está começando na mesa e comentar) é de crescimento de lista e combina com esse duplo
público. Não forçar menção a curso ou preço.

## Resolução dos marcadores da etapa 0

| # | Marcador | Resolução nesta etapa |
|---|---|---|
| 1 | Linha editorial | Resolvido na etapa 0 (autor: Notas de um Professor). |
| 2 | Título | Resolvido na etapa 0 (autor: variante de e-mail). `busca_organica` e `nota_substack` vão para o frontmatter na etapa 9. Como o título é o de e-mail, `assunto_email` é igual ao título e não precisa de campo próprio. |
| 3 | Subtítulo | **Resolvido:** fica o do autor como `subtitulo`. O deck cumpre o movimento 0 (carrega a tese, não só o assunto). O "quase nunca rende 12% em um ano" vai para a etapa 7 (frequência de anos com exatamente 252 DU numa janela longa; na tabela do autor, 1 em 5). |
| 4 | `status`/`slug`/`data` | Registro: `status: rascunho`, slug `2026-10-30-du252-contagem-de-dias`, `data: 2026-10-30`. |
| 5 | Espaço da memória pessoal | Resolvido na etapa 0 (autor escreve até o gate). A etapa 4 converte em `[PREENCHER: …]` sem escrever nada no lugar. |
| 6 | CTA sugerido | **Resolvido:** o texto do CTA é do autor e encaixa no funil (ver acima). A etapa 4 tira o colchete e o rótulo "CTA — sugestão", mantém a frase e registra em nota lateral. Ver a tensão de série abaixo: se o autor quiser ponte para o próximo texto, ela entra junto do CTA. |
| 7 | "Isso merece uma nota só para ele" (cupom cambial) | Etapa 2 (campo 8 da Ficha). Ligado à tensão de série. |
| 8 | Visuais implícitos | Etapa 2 decide o tipo pelo critério, etapa 8 produz. |
| 9–14 | Números, normas, código, outros mercados | Etapa 3 levanta fonte primária, etapa 7 recalcula, executa e confere. |
| 15 | Nota de rigor (truncamento) | Fica. Etapa 7 confere se os centavos batem sem truncamento. |
| 16 | "Para ir além" (7 links) | Etapa 7 abre os links. Ver a tensão de bibliografia abaixo. |

## Tensões registradas (perguntas nomeadas)

**Tensão — ponte de série.** O último texto da linha, `2026-10-15-renda-fixa-condicoes-variaveis`
(debêntures, aprovado em 26/10), termina com "O próximo texto é sobre o FIDC (Fundo de
Investimento em Direitos Creditórios)". Este texto é sobre DU/252, e o rascunho não menciona a
série. Ele aponta para frente só uma vez, para uma nota futura sobre cupom cambial. A
pergunta: **(A) texto avulso na linha, sem ponte, e o FIDC continua sendo o próximo; (B) uma
frase reconhece que este é um parêntese de ferramenta antes do FIDC; ou (C) a promessa
explícita passa a ser o cupom cambial?** Vai ao autor depois da etapa 3, junto com a
bibliografia, para que a etapa 4 já escreva a resposta. Se não houver resposta até lá, a
etapa 4 segue com (A), que é o rascunho como está.

**Tensão — bibliografia.** O `BACKWARDS_DESIGN.md` §5.7 pede de 3 a 4 referências, mínimo de 2
livros, e evitar lei na bibliografia. O "Para ir além" do rascunho tem 7 itens, nenhum livro e
uma norma (CMN 4.880). Os 7 itens são fontes primárias e documentação de código, todos
anotados, e o último post da linha resolveu a mesma tensão enxugando para 4 (gate de
2026-10-26). A pergunta: **(A) enxugar para 3–4 com 2 livros, (B) manter os 7 do autor como
"Para ir além" técnico, ou (C) manter os 7 e acrescentar os livros?** Vai ao autor depois da
etapa 3, com as opções reais de livro que a pesquisa encontrar.

## Alertas para as etapas seguintes (não são decisões)

- **Siglas e jargão sem glosa na primeira ocorrência** (regra 1 e §5.1 do
  `BACKWARDS_DESIGN.md`), para a etapa 6: LTN (primeira frase do texto), Selic, DI, CDB,
  DI1, VF, "marcação", "pregão", Treasuries, DDI/FRC, "cupom cambial", PyPI, Actual/Actual.
  PU já vem glosado ("o preço unitário"). O leitor é um colega júnior competente (§5.6), mas a
  glosa é da assinatura da linha.
- **Semântica de `bizdays` nas pontas** (para a etapa 7, que executa o código): a Armadilha 3
  diz que `cal.bizdays("2026-01-02", "2027-01-01")` dá 248 e, com `following`, 249. Se for
  isso, a função exclui a data inicial e inclui a final, o que contradiz o comentário do
  Caminho A ("inclui a aplicação, exclui o vencimento"). Com as duas pontas em dia útil, a
  contagem não muda, mas o comentário e a explicação "porque 31 de dezembro conta" precisam
  bater com o comportamento real. Executar com a versão citada (1.0.19) e conferir a
  documentação.
- **Metáfora régua/motor × relógio.** As seções "Por que o relógio para no sábado" e "Outros
  relógios" introduzem uma terceira imagem (relógio). A etapa 5 avalia se a troca soma ou
  dispersa. O pipeline não unifica por conta própria.
- **Fechamento do loop do gancho no meio do texto.** A LTN volta na seção do 252, não no fim.
  A etapa 5 avalia se o fecho ("Antes de perguntar quanto rende") precisa retomá-la.
- **Movimento 4 (O Lado de Lá) e dois lados do balcão** são campos obrigatórios da linha. Em
  post de matemática financeira, o movimento 4 vira "de onde vem a fórmula e qual hipótese ela
  embute" (§4.2): o rascunho tem isso no DI de um dia e na Circular de 1997. A etapa 2
  confere.
- **Datas sensíveis ao dia da publicação:** "dois meses de vida" (calendário B3 do `bizdays`
  termina em 31/12/2026), "Exemplo fresco: em novembro de 2026", "a mais recente no PyPI
  enquanto escrevo". Com publicação em 30/10/2026, todos valem. A etapa 7 confere a versão do
  pacote nesta data.
- **Tamanho:** ~2.230 palavras de prosa mais cinco blocos de código. Não há pedido de corte.
