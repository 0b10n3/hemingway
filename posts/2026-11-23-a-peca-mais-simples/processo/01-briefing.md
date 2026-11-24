# Etapa 1 — Briefing

## Linha editorial

**Notas de um Professor**, confirmada pelo autor na etapa 0 (o rascunho não trazia o campo). O
tipo, pela tabela de `docs/BACKWARDS_DESIGN.md` §4.2, é **produto / instrumento** (a LTN), com
um bloco de **matemática financeira** dentro (a linha do PU, a *duration*, a decomposição do
prejuízo). O que muda nos movimentos:

- o 4 vira a engenharia de quem emite e de quem carrega: "Quem vende, quem compra, quem
  empresta" (Tesouro, PAF e leilão; Banco Central e compromissadas; bancos, ALM, LCR e garantia);
- o 5 vira a distinção estrutural contra o vizinho nomeado: "A aposta escondida na taxa", LTN ×
  LFT, com o prêmio de prazo como o que a intuição comum não vê;
- o 8 vira alocação e risco relativo: "Três trabalhos na carteira" (casar compromisso, travar
  taxa, tomar posição).

A etapa 5 roda sem validação argumentativa, e a 5a não roda.

## Voz

**Ensaística em registro técnico** (§4.2 do guia), a voz padrão da linha. Sinais no rascunho:

- **tese em refrão de duas frases**, plantada no Mito e repetida no fecho, literal: "Quem compra
  LTN não aposta na queda dos juros. Aposta contra a curva." Hoje ela também é o subtítulo, palavra
  por palavra (ver T1 abaixo);
- **vocabulário de série** retomado como objeto: régua, motor, etiqueta, réplica, cada um amarrado
  a um pedaço da fórmula do PU ("Uma linha, quatro textos"); termo novo: **átomo** (a LTN como
  átomo da curva prefixada; "tudo o mais é molécula");
- fórmula display anunciada por dois-pontos e glosada depois ("O preço de uma LTN cabe numa
  linha:" … "em que PU é…"); conta resolvida até o número final (R$ 746,004202; R$ 961,90;
  R$ 13.405);
- caso real datado como gancho (outubro de 2026) e fecho em anel ("De volta a outubro");
- primeira pessoa só para costurar a série ("prometi", "Esta, eu vou rolar"); "você" didático;
  imperativo que conduz ("Repare", "Pense", "compare");
- humor seco, uma vez por bloco: a promessa rolada como o Tesouro rola a dívida, o barão que
  "pode esperar no pântano mais umas semanas", "Ninguém deixa esse dinheiro na mesa por
  distração";
- fecho técnico: «Se o texto funcionou, você consegue analisar sozinho…» + exercício + "Para
  continuar aprendendo".

**A etapa 4 dá mais peso à voz**, pelo precedente da etapa 0 (texto montado a partir de
pesquisa). Confere o texto contra `estilo/estilo-autoral.md` §3, §4.2 e §7.2 e contra
`estilo/preferencias-de-edicao.md`, sem reordenar o argumento.

## Tese em uma frase

A LTN é o fator de desconto de um prazo vendido em lotes de R$ 1.000; quem a compra não aposta
que a Selic vai cair, aposta que a Selic de verdade, até o vencimento, fique abaixo do que a
curva cobrava no dia da compra, e por isso o preço dela anda com a curva (o que se espera da
Selic mais o prêmio pela dúvida), não com a Selic de hoje.

Aforismo do texto: "Quem compra LTN não aposta na queda dos juros. Aposta contra a curva."
Aparece no Mito e no fecho, de propósito (§5.4).

## Gancho

**Abertura em dois tempos**, aprovada pelo autor no rascunho (decisão 1):

1. **A promessa rolada.** O texto anterior prometeu o *bootstrapping*; este explica o nome
   (Münchhausen) e "rola" a promessa como o Tesouro rola a dívida. Justifica a mudança de rumo da
   série: a LTN foi cobaia de quatro textos e nunca foi apresentada.
2. **Modo A, evento datado.** Outubro de 2026: leilão recorde de LTN em 8/10 a cerca de 12,5%
   com a Selic em 13,75%; Prefixado 2029 a R$ 773,74 (12,40%) em 13/10; reeleição em 25/10;
   juros futuros disparam, o Tesouro cancela o leilão e recompra; R$ 746,00 (14,98%) em 17/11;
   a Selic não se mexeu.

Pergunta-âncora, explícita no fim da abertura: "O que, exatamente, se compra quando se compra
uma LTN? E, se a Selic ficou parada, o que derrubou o preço?"

O modo A obriga o movimento 7, que existe: "De volta a outubro".

## Continuidade de série

O texto continua "Cara, eu ganho. Coroa, eu não perco."
(`posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco/post.md`, aprovado em 18/11). O que já foi
dito lá e o que isso pede aqui:

- **O gancho bate.** Lá: "No próximo texto, a conta vai ao contrário. … É o *bootstrapping* (a
  construção da curva zero-cupom a partir dos títulos com cupom)". Aqui: "No fim do último texto,
  prometi construir a curva de juros vértice por vértice, com uma técnica de nome curioso:
  *bootstrapping*." Coerente.
- **"Uma NTN-F foi montada com três LTNs"**: bate. Lá, três LTNs de 126, 252 e 378 dias úteis, a
  taxas ilustrativas (14,00%, 14,30%, 14,55%). Aqui o número é real (Prefixado 2029 a 14,98% em
  17/11), na mesma ordem de grandeza.
- **Selic de 13,75%**, mantida em 4/11 (lá) e "não se mexeu" entre 13/10 e 17/11 (aqui).
  Coerente.
- **Glosa da LTN**: lá, "(Letra do Tesouro Nacional, o título público prefixado sem cupom)";
  aqui, a mesma. Coerente.
- **Os quatro apelidos**: régua (contagem du/252 de "Você está contando os dias errado", nomeada
  em "A Corda e o Arco": «Chamamos essa contagem de régua.»), motor ("A Corda e o Arco"),
  etiqueta ("Frequência de Capitalização"), réplica ("Cara, eu ganho…"). A atribuição do
  rascunho bate com o texto publicado. A LTN aparece de fato como exemplo nos quatro (em
  "Você está contando os dias errado", a LTN de 12% com liquidação em 2/1/2026).
- **Formato de fórmula:** o post publicado usa `$$ … $$`; o rascunho usa blocos ```` ```latex ````.
  A etapa 4 converte.
- **Tabelas:** o rascunho tem duas (os cinco títulos; os três cenários). O Substack não tem
  tabela nativa (`.claude/agents/prompts-visuais.md`); o post de 18/11 manteve tabela markdown
  no `post.md` e o autor converteu na publicação. Segue o precedente; a etapa 2 registra.
- **Skill Check:** o texto anterior pôs o CTA no mesmo lugar (antes da ponte, perto do fecho),
  com as mesmas duas dimensões. Este repete o padrão.
- **Ponte para a frente:** NTN-F no próximo texto; *bootstrapping* "quando as peças estiverem na
  mesa", com o barão saindo do pântano "com ela [a NTN-F] na mesa"; e, na Prateleira, um texto
  próprio para o título de inflação ("o título que casa com ele é outro, e ele tem texto próprio
  nesta série"). Ver alerta de promessas abaixo.

## Briefing de funil (`../../strategy/FUNIL.md` §1 e §5)

- **Segmento:** `#GENZ-GREED` e `#GENZ-FEAR`: o estagiário ou analista júnior de renda fixa,
  tesouraria ou *research* que já precificou LTN na planilha e nunca separou expectativa de prêmio.
  O gancho da promessa para esse segmento é "provar competência rápido" (ler o PU, o DV01 e o que
  a taxa aposta é o que se cobra de um júnior de mesa). A Prateleira fala também com o investidor
  pessoa física do Tesouro Direto, que é quem encaminha "para quem ainda compra prefixado porque a
  Selic vai cair".
- **Estágio:** topo gratuito (§5).
- **Objetivo do post:** educar e fazer a lista crescer por encaminhamento. O CTA do Skill Check
  (gratuito, topo) já está no corpo. Curso ou preço não entram no corpo; oferta, se houver, é
  decisão da etapa 9a.

## Analogias e movimentos a preservar

Vieram do rascunho, não deste pipeline:

- **A promessa rolada**: "faço com ela o que o Tesouro faz com os títulos que vencem, pago a
  antiga emitindo uma nova, com prazo mais longo." Amarra a abertura ao assunto (dívida pública).
- **O barão de Münchhausen no pântano**: nome do *bootstrapping*, pausa e retorno na ponte final.
- **Átomo e molécula**: a LTN como fator de desconto vendido em lotes; "tudo o mais é molécula".
- **Régua, motor, etiqueta, réplica** mapeados nos pedaços da fórmula.
- **A curva como "a fila de taxas prefixadas, uma por prazo"**.
- **O prêmio como "o preço do seguro contra ela estar errada"**.
- **As gavetas** (anatomia; tesouraria dos bancos) e **os dois lados do balcão**.
- **"A recompra diária do Tesouro garante que existe comprador. Não garante o preço."**

## Resolução dos marcadores da etapa 0

| # | Marcador | Resolução nesta etapa |
|---|---|---|
| M1 | Linha editorial | Resolvido na etapa 0 (autor). |
| M2 | NOTA PARA CLAUDE: pesquisa sobre Copom × altas e baixas da taxa da LTN + infográfico | Etapa 3 faz a pesquisa; etapa 2 decide o tipo pelo critério; etapa 8 produz. |
| M3 | "embedded content" (11 cotações do Prefixado 2029 × Selic) | Etapa 2 decide o tipo; etapa 3 levanta a série; etapa 8 produz. |
| M4 | Abertura em dois tempos, APROVADO | Resolvido pelo autor. A etapa 5 avalia ritmo, sem desfazer a decisão. |
| M5 | Título "A Peça Mais Simples"; pensar em outros subtítulos | Título resolvido. Subtítulo: etapa 4 propõe; o gate decide (T1). |
| M6 | Família dos títulos públicos na anatomia, APROVADO | Resolvido pelo autor. |
| M7 | Não referenciar "Tesouro Prefixado: o guia completo" (2024) | Resolvido: o texto não cita nem linka. **Vale para a 9a**: o item `legado:tesouro-prefixado-o-guia-completo` está no catálogo, e o estrategista recebe a restrição no prompt. |
| M8 | Candidatos a corte, "se precisar" (sem resposta) | Resolvido pela condição: não há pedido de corte e o tamanho está na faixa (cerca de 3.000 palavras de prosa). Se a etapa 5 apontar dado que não serve ao argumento nesses dois trechos, vira pergunta ao autor. |
| M9 | Teste de transferência (CDB a 16%); resposta como Note de D+2 | Etapa 2 (campo 2 da Ficha); etapa 7 confere a conta (cerca de R$ 732). A Note fica como sugestão para `/distribuir`, registrada em `estado.json`. |
| M10–M15 | `[VERIFICAR]` (Securato; link do PAF; suspensão do Tesouro Direto; "maior volume desde dez/2020"; portaria dos *dealers*; Focus do início de outubro) | Etapa 3 levanta; etapa 7 fecha. |
| M16 | Premissas dos cenários e dos −3,6% | Etapa 7 recalcula e diz se o texto declara o bastante; o gate decide se muda. |
| M17 | "A pesquisa de pauta não veio anexada" | Resolvido: não há pauta em `../_insumos/ideias/` nem em `posts/`. O texto segue como está. |
| M18 | Contas conferidas em Python | Etapa 7 recalcula tudo. |
| M19 | Parágrafos em negrito do autor na abertura | Etapa 4 preserva o sentido; etapa 6 olha a forma ("O motivo é de justo" parece digitação de "O motivo é justo"). |
| M20 | Aviso legal e referências | Etapa 9: aviso de `docs/AVISO_LEGAL.md` no fim, depois de `* * *`; referências antes dele, como no post de 18/11. |

## Tensões registradas (perguntas nomeadas)

- **T1 — Subtítulo.** O autor pediu "pensar em outras propostas de subtítulos". Hoje o subtítulo
  repete o refrão palavra por palavra, que já aparece isolado no Mito e no fecho. A etapa 4 propõe
  três ou quatro alternativas; o gate pergunta: manter o atual ou trocar por uma delas?

## Alertas para as etapas seguintes (não são decisões)

- **Abertura longa.** São cerca de 22 parágrafos curtos antes do primeiro H2, contra 3–6 do §3
  do BACKWARDS_DESIGN. A abertura em dois tempos foi aprovada; a etapa 5 avalia se o leitor chega
  à pergunta-âncora sem cansar, sem propor desfazer os dois tempos.
- **Promessas de série.** O texto faz três: NTN-F no próximo; *bootstrapping* "quando as peças
  estiverem na mesa" (a abertura sugere a família inteira, "um título público por vez, do mais
  simples ao que tem mais engrenagens"; a ponte final sugere logo depois da NTN-F: "Com ela na
  mesa, o barão finalmente sai do pântano"); e um texto próprio para o título de inflação. A etapa
  5 confere se as duas frases sobre o *bootstrapping* dizem a mesma coisa. Fica registrado porque
  a promessa do FIDC foi feita duas vezes e cancelada depois.
- **Antítese em série** (regra 20, teto de uma por seção, nunca duas seguidas). Contagem
  preliminar: "A aposta escondida na taxa" tem três ("A taxa da LTN não é a previsão da Selic. É…";
  "A eleição não mudou a Selic. Mudou o prêmio."; "O preço da LTN não responde à Selic de hoje.
  Responde à curva…"); "De volta a outubro" e "Três trabalhos" têm uma cada; a abertura e o Mito,
  mais o refrão. A etapa 6 confere.
- **Metadiscurso** (§7.2): "No restante do texto, procuramos dar mais sentido a este último
  pensamento." (anúncio, e no plural de modéstia, que a voz técnica não usa); "O último item é o
  que dá o título a este texto."; "É esse o ponto cego da versão que circula" (nome de movimento
  da estrutura no corpo, ainda que como expressão comum). A etapa 6 olha.
- **Frase-sinal** (§5.3): "Até aqui, é o que a página do Tesouro Direto conta. A partir daqui, a
  conta." Uma vez, no fim da anatomia. Correto.
- **"Selic" com dois sentidos**: a taxa (glosada na abertura) e o sistema (glosado na anatomia,
  "Sistema Especial de Liquidação e de Custódia"). A etapa 6 confere se o leitor não tropeça.
- **Glosas na primeira ocorrência** (regra 14; §5.1), para a etapa 6. Glosados: LTN, Selic,
  Copom, LFT/NTN-F/NTN-B (pela tabela), FGC, deságio, *duration*, *duration* modificada,
  ponto-base, DV01, convexidade, PAF, *dealers*, compromissadas, DI futuro, LCR, Boletim Focus,
  prêmio de prazo. Sem glosa: ANBIMA, B3, CDI, CDB, IPCA, IOF, IR, TIR (glosa funcional só na
  ponte), juros futuros, pregão, mercado secundário de balcão, carregamento (definido pelo uso),
  Demab. A etapa 6 decide quais o leitor da linha já domina.
- **Estrangeirismo em itálico** (regra 4): *bootstrapping*, *duration*, *dealers* estão; "DV01"
  é sigla. Etapa 6.
- **Negrito** (regra 4): frase-tese (refrão, duas vezes), rótulos das gavetas, os quatro itens
  da fórmula, frases do caso de outubro ("o maior volume em prefixados desde dezembro de 2020",
  "o Tesouro cancelou o leilão…") e os dois parágrafos do autor. A etapa 6 confere a função de
  cada um, lembrando que negrito do autor é decisão dele.
- **Números**: o rascunho declara as contas conferidas em Python; a etapa 7 recalcula todas. Uma
  conferência rápida desta etapa bateu PU (R$ 746,004202), carregamento (+1,12%), choque
  (−4,65%), DV01 (R$ 0,14; R$ 182,57), ±1 p.p. (−1,80%/+1,85%), taxa líquida (12,87%), CDB
  (R$ 732,56) e o rendimento do Tesouro Selic (1,2%). Pontos a olhar: os detentores somam
  86,25%, o resto é 13,75%, não 13,76%; "Média de 16% ao ano" no cenário só bate com CDI de
  15,90% (meta de 16% − 0,10), o que a tabela não diz.
- **Fatos de outubro e novembro de 2026**: todos posteriores ao que este pipeline sabe de
  memória. A etapa 3 confere em fonte primária (Tesouro, BCB, ANBIMA, B3) e a 7 fecha.
- **Tamanho:** cerca de 3.000 palavras de prosa, na faixa do texto anterior. Sem pedido de corte
  (M8).
