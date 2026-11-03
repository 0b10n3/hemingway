# Etapa 1 — Briefing

## Linha editorial

**Notas de um Professor.** O rascunho não tem front-matter; o H1 traz o prefixo da linha e o
autor confirmou na etapa 0. O conteúdo bate: mecanismo técnico (regimes de capitalização,
convenções de prazo), sem relato de carreira. Pelo `docs/BACKWARDS_DESIGN.md` §4.2, é post de
**matemática financeira**: o movimento 4 vira "de onde vem a fórmula e qual hipótese ela
embute" (seção "Quem escolhe a régua"), o 5 vira "o caso em que a intuição quebra" (a barriga
entre 0 e 1 período), o 8 vira "a conta que o leitor refaz na planilha" (as três perguntas e
as quatro fórmulas). Ficha de Saída na etapa 2; etapa 5 sem validação argumentativa; 5a não roda.

## Voz

**Ensaística em registro técnico** (§4.1 do guia, com o rigor do §4.3), a mesma escolha do
du252. Sinais no rascunho: primeira pessoa singular ("Nunca expliquei", "Esqueci"), ironia
contra a versão escolar ("coisa de livro escolar e de agiota de bairro", a frase atribuída a
Einstein), aforismo isolado em parágrafo próprio ("Capitalização não é lei da natureza. É
cláusula."), CTA de encaminhamento. Ênfase já vem em aspas simples ('bola de neve', 'juro
sobre juro', 'gregas'); nenhum negrito; itálico só em título de obra. Conforme a regra 4.

**Peso extra de voz na etapa 4** (decisão do autor na etapa 0): o texto não foi escrito pelo
autor. A etapa 4 confere contra `estilo/estilo-autoral.md` §3, §4.1 e §7.2 (tiques de IA), sem
reordenar o argumento. Onde o texto simula memória ou opinião pessoal, ou o autor confirma, ou
vira `[PREENCHER: …]`. Hoje há uma: "uma frase que repito para mim mesmo" (sai com o
reenquadramento, ver abaixo).

## Tese em uma frase

Capitalização é cláusula, não lei da natureza: com o mesmo número cotado, o juro simples paga
mais que o composto em qualquer fração de período, o composto só passa à frente depois do
primeiro período (e o juro sobre juro leva uma década para pesar), e o Brasil adotou o composto
em 1998 não porque paga mais, mas porque é a régua que não se contradiz de um prazo para o outro.

Aforisma do texto: "Capitalização não é lei da natureza. É cláusula." Aparece duas vezes (fim do
Mito e Fechamento), de propósito.

## Gancho

R$ 1 milhão a 14% ao ano por 126 dias úteis: "R$ 70 mil, você acertou… E você errou": R$ 67.707,83
num CDB prefixado. Diferença de R$ 2.292,17, "a distância entre duas réguas". **Modo B**
(proposição contraintuitiva com número; §4.1 do `BACKWARDS_DESIGN.md`), sem evento datado, então
o movimento 7 é opcional e o 9 absorve o fechamento. A pergunta-âncora vem explícita: "A régua
que o mercado brasileiro adotou por norma … é justamente a que paga menos em seis meses. Por quê?"
O loop fecha na seção "A barriga da curva" (o desenho explica o R$ 2.292,17) e de novo no
Fechamento ("não foi a régua que paga mais").

## Reenquadramento de série (decisão do autor, etapa 0)

O du252 explicou a **régua** (como contar o tempo: du, 252, calendário) e só nomeou o **motor**
(linear ou composto) — com a promessa explícita "O próximo volta à série de crédito com o FIDC".
Este texto explica o motor: por que o du/252 entra no expoente. Ângulo para a etapa 4:

- Abertura: sai "Nunca expliquei de onde ele vem" e a frase "o problema do professor é que ele
  esquece que foi aluno. Esqueci." (já usada no du252). Entra o gancho de continuidade: o último
  texto contou os dias; ficou faltando dizer por que o resultado vai no expoente. A lista de
  textos anteriores (LCA, debênture) fica, e ganha o du252.
- Ponte: "Então, antes do FIDC" vira o reconhecimento de que este é o segundo parêntese de
  ferramenta antes do FIDC. "Agora, sim, o FIDC" fica no Fechamento, mas precisa soar como
  promessa cumprida, não repetida.
- "Como nos textos anteriores, quase todo erro de leitura nasce de misturar três perguntas":
  conferir na etapa 4 que as três perguntas são as mesmas (ou declaradamente uma extensão) das
  do fecho do du252 ("Qual o regime? Composto ou linear?" está lá).

## Analogias e movimentos a preservar

Vieram do rascunho, não deste pipeline (lembrando: o rascunho não é do autor, então
"preservar" aqui quer dizer "não trocar sem pergunta", não "é assinatura dele"):

- **"Duas réguas" / "Três réguas para o mesmo tempo"** — os regimes como réguas. **Colide com
  o du252** (ver tensão abaixo).
- **A barriga da curva**: a reta do simples é a corda da curva convexa do composto, e por isso
  passa por cima entre 0 e 1. É o centro do texto e o título.
- **"A bola de neve demora a rolar"**: decomposição em capital + juro linear + juro sobre juro.
- **"O motor do juro composto não é a taxa. É o tempo."** (usa "motor" no sentido comum, não no
  do du252; ver tensão.)
- **"Ela é a metade de uma cláusula."** / **"Capitalização não é lei da natureza. É cláusula."**
- **Fatiar o prazo vira estratégia** (1,07² = 1,1449): o argumento de consistência que explica a
  escolha de 1998. É o movimento 4.
- **"Nenhuma das três réguas é a certa. Cada uma é a que resolve o problema de quem está cotando."**
- Fontes já trazidas: Circular BCB 2.761/1997, Garcia (PUC-Rio, 1997), Comunicado BCB 7.684/2000,
  Resolução CMN 5.171/2024 (art. 6º; art. 406 CC), B3 (FRC de cupom cambial), ANBIMA (ETTJ),
  Susep (ETTJ), Assaf Neto, Samanez, Hull. A etapa 3 confere; a etapa 7 verifica.

## Encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §3.4, §5)

O tema é o do curso gratuito ao vivo, **Fundamentos do Valor do Dinheiro no Tempo** (juros
simples/compostos, taxas equivalentes), e da trilha **"Fundamentos Matemáticos para Finanças"**
do core offer. Leitor principal: `#GENZ-FEAR`/`#GENZ-GREED` (estagiário e analista júnior que
"sabe a fórmula" mas não sabe por que o mercado usa uma e não a outra). Leitor que encaminha:
`#Millennials-*`. O CTA do rascunho ("encaminhe para quem ainda divide a taxa anual por doze") é
de crescimento de lista e combina. Não forçar menção a curso ou preço.

## Resolução dos marcadores da etapa 0

| # | Marcador | Resolução nesta etapa |
|---|---|---|
| 1 | Linha editorial | Resolvido na etapa 0. |
| 2 | Subtítulo provisório "Juro simples, composto e contínuo além dos livros" | **Proposta:** o movimento 0 pede que o deck carregue a tese, não o assunto; o provisório carrega o assunto. Alternativa para o autor escolher no gate: "Por que o juro simples rende mais que o composto em seis meses, e por que o Brasil escolheu o composto mesmo assim". A etapa 4 usa o provisório; a troca é decisão do gate (não estrutural). |
| 3 | Autoria | Resolvido na etapa 0. |
| 4 | Abertura × du252 | Resolvido na etapa 0; ângulo fixado acima. |
| 5 | Frase atribuída a Einstein | **Tensão nomeada** (abaixo). |
| 6–9 | `[VERIFICAR]` (taxa over mensal; Comunicado 7.684; contagem de datas; edições) | Etapa 3 levanta, etapa 7 confere. O #8 reaproveita o laudo do du252. |
| 10–11 | graf-01, graf-02 | Etapa 2 confirma pelo critério; etapa 8 produz. |
| 12–14 | Correções à pesquisa, números, fatos normativos | Etapa 3/7. |
| 15 | Notas de processo | Fora do `post.md`. |

## Tensões registradas (perguntas nomeadas)

Vão ao autor depois da etapa 3 (como no du252), para a etapa 4 já escrever a resposta.

**Tensão — vocabulário régua/motor.** No du252, "régua" é a contagem de dias e "motor" é a
capitalização ("Na renda fixa brasileira em reais, a combinação padrão é régua DU/252 com motor
composto"). Este rascunho chama os regimes de capitalização de "réguas" ("Três réguas para o
mesmo tempo", "a distância entre duas réguas", "a régua contínua") e usa "motor" em sentido
solto. Lidos em sequência, o leitor encontra a mesma palavra com dois sentidos. **(A) Alinhar ao
du252: regime vira "motor", "régua" fica só para contagem/base; (B) manter "régua" para regime
neste texto, sem ponte; (C) manter e dizer explicitamente que, aqui, "régua" é o conjunto
regime + base + contagem.**

**Tensão — "A virada de 1998" repete o du252.** O du252 já conta a Circular 2.761, a mensalização
herdada da hiperinflação e Garcia. O que este rascunho acrescenta é o porquê (consistência entre
prazos, já na seção anterior), o exemplo fevereiro × julho de Garcia e o Comunicado 7.684. **(A)
Encurtar a subseção ao que é novo, remetendo ao du252; (B) manter integral (o leitor pode não ter
lido o du252).** Mudança de extensão de seção, não de ordem.

**Tensão — Einstein.** "a força que uma frase atribuída a Einstein, sem fonte que a sustente,
chamaria de oitava maravilha do mundo". O próprio rascunho deixa a decisão ao autor ("mantive
como ironia sinalizada; corte se preferir"). **(A) Manter; (B) cortar.**

## Alertas para as etapas seguintes (não são decisões)

- **"Barriga da curva" é jargão de mercado.** Na mesa de juros, "barriga da curva" é o trecho
  intermediário da curva de juros (os vértices médios do DI futuro), não a convexidade entre
  0 e 1 período. Para o leitor profissional, o título promete outro assunto. A etapa 5 avalia se
  o duplo sentido é trunfo (dá para nomeá-lo em uma frase) ou ruído.
- **CTA "quem ainda divide a taxa anual por doze"**: dividir por doze é o regime linear, que o
  próprio texto diz não ser errado ("Nenhuma das três réguas é a certa"). A etapa 5 avalia a
  coerência; a etapa 4 pode ajustar para "quem ainda acha que o composto sempre rende mais".
- **Glosas na primeira ocorrência** (regra 1; §5.1 do `BACKWARDS_DESIGN.md`), para a etapa 6:
  CDB, B3, Selic, Taxa DI, LTN, NTN-B, LFT, DI futuro, overnight, pontos-base, spread, cupom
  cambial (glosado), DDI, FRC, ETTJ, Svensson, Black-Scholes-Merton (glosado em parte),
  anatocismo (glosado). LCA e PU já vêm glosados.
- **Seis blocos LaTeX + um bloco de planilha.** A Substack renderiza LaTeX em bloco; a etapa 2
  confirma que nenhum vira imagem. A etapa 7 confere a função `DIATRABALHOTOTAL` (nome pt-BR,
  separador `;`, e se o "-1" bate com a convenção `(início, fim]` verificada no du252).
- **graf-02 não veio no arquivo** ("embedded content"). A etapa 8 reconstrói a partir da
  fórmula do juro sobre juro, 6%/10%/14%, 1 a 30 anos.
- **Dois lados do balcão** (campo 7 da Ficha): o rascunho tem "paga mais a quem aplica e cobra
  mais de quem toma". A etapa 2 confere se basta.
- **Tamanho:** ~2.300 palavras de prosa publicável. Não há pedido de corte.
