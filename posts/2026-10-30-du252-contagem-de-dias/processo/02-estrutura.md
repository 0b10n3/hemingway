# Etapa 2 — Estrutura

A estrutura é a do rascunho do autor. Ela já percorre quase todos os movimentos de
`docs/BACKWARDS_DESIGN.md` §3, na variante "matemática financeira" do §4.2. Esta etapa mapeia,
preenche a Ficha de Saída, confere se a sequência entrega a competência e decide os visuais.
**Não reordena nada nem corta seção.** Os pontos em que a forma do rascunho se afasta do
modelo ficam como observação para a etapa 5.

## Ficha de Saída

| Campo | Preenchimento |
| --- | --- |
| **1. Competência de saída** | *Converter* uma taxa anual em dinheiro (fator, PU, valor de resgate) declarando as quatro peças que a acompanham: contagem de dias, regime de capitalização, calendário e tratamento das pontas. Como consequência, *diagnosticar*, numa conta ou num código que não bate com a tela, qual das quatro peças foi lida errado. |
| **2. Teste de transferência** | **O CDB pós-fixado a 100% do CDI.** O texto explica a taxa DI como diária de um dia útil e a régua DU/252, mas só calcula prefixados (LTN, CDB pré). Se o leitor termina e consegue dizer, sozinho, como um CDB a 100% do CDI acumula (fator diário (1 + DI)^(1/252) por dia útil do calendário ANBIMA, com a aplicação dentro e o resgate fora, e a diária da sexta cobrindo o fim de semana), o texto funcionou como aula. Alternativa registrada, mais exigente: o CET (Custo Efetivo Total) de um empréstimo pessoal, cotado ao mês em dias corridos, comparado com o CDB. Ela obriga a trocar de régua, mas a convenção do CET precisaria de verificação própria. |
| **3. Tese de fundo** | "Uma taxa sem régua é um número pela metade: o mesmo 12% vale dinheiro diferente conforme a contagem, o regime e o calendário." Versão do autor: "antes de perguntar quanto rende, pergunte em que régua." **Não é da família da tese-mãe da série de crédito** ("o risco muda de endereço, não desaparece"). É o primeiro texto da linha do tipo matemática financeira puro. O parentesco mais próximo é o "Ninguém ficou com a diferença": o dinheiro não mudou de mão, foi a leitura que mudou. Ver a tensão de série (`01-briefing.md`). |
| **4. Erro-alvo** | Que "12% ao ano" rende 12% em um ano de calendário, e que taxas de produtos e mercados diferentes se comparam pelo número, sem a convenção. Na versão de código: que *business day* de `numpy`/`pandas` é dia útil brasileiro, e que os calendários ANBIMA e B3 são intercambiáveis. Gente competente acredita: "Quatro armadilhas que já vi em código de gente boa", e a frase da sala de aula, "No Brasil é 252 composto, lá fora é 360 linear". |
| **5. Ferramenta prática** | Quatro: (a) as quatro perguntas do fecho (contagem, regime, calendário, pontas); (b) as fórmulas do Fator e do PU em DU/252; (c) a inversão para taxa equivalente entre réguas (os 12,00 / 11,36 / 11,20 / 10,71); (d) os dois caminhos de código, `bizdays` com `following` e `pandas` com `CustomBusinessDay` e `inclusive="left"`. |
| **6. Âncora de autoridade** | Fórmula: **Metodologias ANBIMA de Precificação** (PU em base 252, título público). Calendário: **Resolução CMN nº 4.880/2020**, citada com número na Anatomia/Ponto Cego (não na bibliografia, §5.7). Origem do 252: **Circular BCB nº 2.761/1997**, com o comentário de época de Márcio Garcia (PUC-Rio). Bolsa × banco: **B3, OC 055/2024-PRE** (DI1). Não há paper acadêmico, e o tema não pede um: é convenção regulatória, e a fonte primária é o regulador. |
| **7. Os dois lados do balcão** | Quem lê a taxa (investidor que aplica no CDB, júnior da mesa, quem escreve o código da marcação) × quem a define e paga (o emissor: Tesouro na LTN, banco no CDB; é o contrato do emissor que fixa a régua, "o contratado" da tabela). O rascunho dá o protagonismo a quem calcula no meio (mesa, *back office*, desenvolvedor), e isso combina com o público. O movimento 4 em post de matemática financeira vira "de onde vem a fórmula e qual hipótese ela embute" (§4.2), e o rascunho tem isso: o DI de um dia útil e a Circular de 1997. Distribuidor: não se aplica (nenhuma das três condições do §4.3). |
| **8. Ponte de série** | **Vem de:** a série de crédito (CDB → LCI → LCA → CRI/CRA → debêntures), que usou "% ao ano" e DU/252 sem parar para explicar a convenção. O post das debêntures (2026-10-15) já tinha a taxa diária (1 + c)^(1/252) e um PU em du/252. **Aponta para:** em aberto. O post das debêntures prometeu o FIDC, e este rascunho promete só uma nota sobre cupom cambial ("Isso merece uma nota só para ele"). É a **tensão de série** registrada na etapa 1, que vai ao autor depois da etapa 3. |

**Regra de corte (§2):** o campo 2 está preenchido. É aula, não descrição de produto.

## Verificação: a estrutura entrega a competência de saída?

| Seção do rascunho | Movimento(s) | Observação |
| --- | --- | --- |
| Título + subtítulo | 0 | O título (e-mail, escolhido pelo autor) instala o erro-alvo em segunda pessoa. O subtítulo carrega a tese em três partes (sábado, 12% que não rende 12%, código). ✓ |
| Abertura sem intertítulo (LTN 12% → 11,85%; "Faltaram três"; os dois leitores; memória do autor) | 1 (modo B) | Termina na pergunta-âncora, que é o primeiro H2. Modo B dispensa o movimento 7, mas o rascunho fecha o loop mesmo assim, no meio ("É daí que vem a LTN do começo do texto"). ✓ |
| "'12% ao ano' de quê?" | 2 (O Mito) | Mito enunciado ("No Brasil é 252 composto, lá fora é 360 linear soa como uma coisa só") e oposto em frase curta e isolada ("São duas."). A tese isolada pelo §5.4 é "Uma taxa de juros, sozinha, não é informação completa." ✓ |
| "A régua e o motor" | 3 (A Anatomia) | Régua (três convenções), motor (dois regimes), a combinação brasileira, Fator e PU, "inclusive/exclusive". **Não fecha com frase-sinal (§5.3).** "Guarde o 'inclusive/exclusive'" é promessa, não passagem do raso ao profundo. Observação para a etapa 5; o pipeline não acrescenta. |
| "Por que o relógio para no sábado" | 4 (O Lado de Lá, versão matemática financeira) + fecho do loop da abertura | De onde vem a régua (DI de um dia útil) e quem a fixou (Circular 2.761/1997). A hipótese embutida, "252 é uma convenção, não uma contagem", mais a tabela 2024–2028 e o retorno da LTN. ✓ |
| "Quanto custa a régua errada" | 5 (O Ponto Cego, contraste com três vizinhos nomeados: DC/365, DC/360, linear) + 6 (Materialidade, em escala de carteira) | Ferramentas 5b e 5c. A tese volta isolada no meio do texto ("Errado é ler um número com a régua do outro."). A materialidade é ordem de grandeza por cálculo próprio (R$ 100 mi), não série de mercado. O §3 aceita porque o número muda o argumento. A etapa 7 confere como cálculo declarado. |
| "ANBIMA ou B3? Duas perguntas diferentes" | 5 (segundo ponto cego, contraste com o calendário vizinho nomeado) | Âncoras CMN 4.880 e OC 055/2024. Dezembro de 2026 como prova (22 × 20). Regra prática em dois itens. ✓ |
| "Na prática: Python sem cair em armadilhas" | 8 (A Prateleira, versão "a conta que o leitor refaz", aqui no código) | Ferramenta 5d. As quatro armadilhas espelham as quatro perguntas do fecho na ordem calendário → calendário → pontas → validade. Os dois caminhos fecham o exemplo do CDB com o mesmo `40 101815.15`. ✓ |
| "Outros relógios" | 9 (generalização lateral) + ponte | Três mercados ou regras vizinhos (EUA, cupom cambial, rolagem de opções). A promessa da nota sobre cupom cambial está aqui. |
| "Antes de perguntar quanto rende" | 9 (Síntese) | Tese isolada de novo ("antes de perguntar quanto rende, pergunte em que régua"). As quatro perguntas são a competência de saída em forma de checklist. CTA do autor. Falta a ponte para o próximo texto (tensão de série). |
| "Para ir além" | 10 | 7 itens anotados, 0 livros. Tensão de bibliografia (§5.7). |

**Conclusão:** a sequência produz a competência do campo 1. As quatro peças aparecem na ordem
em que o leitor precisa delas: régua e motor (Anatomia), calendário (ANBIMA × B3), pontas
(Armadilha 3). E as quatro perguntas do fecho são a competência escrita como checklist. A
tese aparece isolada no início (movimento 2), no meio (taxas equivalentes) e no fim
(movimento 9). ✓

A "pergunta 4" do fecho (as pontas) é a única peça que o texto introduz na Anatomia ("Guarde o
'inclusive/exclusive'") e só desenvolve no código. Um leitor que pule o Python perde a
explicação. Fica como observação para a etapa 5, não como lacuna de estrutura.

## Observações para a etapa 5 (forma, não decisão)

1. **Frase-sinal ausente** no fim da Anatomia (§5.3). O modelo pede uma, uma vez por texto.
2. **Três imagens: régua, motor, relógio.** "Por que o relógio para no sábado" e "Outros
   relógios" trazem uma terceira imagem, e "O terceiro relógio: a rolagem" a usa para uma
   peça que nas quatro perguntas é "pontas/calendário". Ver se soma ou dispersa.
3. **"Pontas" só se explicam no código** (ver acima).
4. **Loop da abertura** fechado no meio do texto, não no fim. Avaliar se o fecho retoma a LTN.
5. **Ponte e CTA** dependem da tensão de série.

## O que fica de fora

- **Pós-fixado (CDI, Selic, IPCA+)**: é o teste de transferência. O texto não o calcula, de
  propósito.
- **NTN-F e cupons**: o PU de títulos com cupom fica com a metodologia ANBIMA, citada.
- **Truncamento ANBIMA**: o autor já declarou a omissão na "Nota de rigor".
- **ISDA, Actual/Actual ICMA × ISDA e variantes de 30/360**: "Outros relógios" fica no nível de
  menção, e a etapa 3 só confere que a menção é correta.
- **Cupom cambial em profundidade**: promessa de texto futuro.

## Onde entra graf-NN / diag-NN / info-NN

Restrição de formato (precedentes do CRA e do Musashi): a Substack não tem tabela nativa.
Tabela que carrega número vira peça-imagem. As duas fórmulas `$$…$$` ficam como bloco LaTeX
em `post.md`, como no post do CRA. A Substack tem bloco de equação no editor, e o autor cola
a fórmula nele. Os cinco blocos de código ficam como bloco de código nativo da Substack.

| Peça | Onde | Tipo | Por quê (e por que os outros perderam) |
| --- | --- | --- | --- |
| **graf-01** | "Por que o relógio para no sábado", no lugar da tabela "Dias úteis no calendário ANBIMA" (2024–2028) | Gráfico de barras: dias úteis por ano, com linha de referência em 252 e o rendimento efetivo de 12% a.a. base 252 anotado em cada barra | Série numérica real (dias úteis por ano, calendário ANBIMA) → graf (critério 1). Mostra de uma vez o "252 é uma convenção, não uma contagem" e o "o ano é que muda de tamanho". O rendimento por ano (1,12^(du/252) − 1) é cálculo próprio derivado e o rodapé declara. diag perde porque há métrica. info perde porque é uma ideia só. Janela: os 5 anos do autor. Se a etapa 7, ao conferir o "quase nunca" do subtítulo, montar uma série mais longa, a ampliação vai ao gate como opção e não entra em silêncio. |
| **graf-02** | "Quanto custa a régua errada", no lugar da tabela do CDB (4 cálculos) | Tabela-imagem (`go.Table`) com a linha "o contratado" em destaque | Série numérica (4 leituras do mesmo 12%: fator, resgate, diferença) → graf (critério 1). Fica em formato de tabela para preservar as cinco colunas do autor (precedente: graf-01 e graf-02 do CRA). Virar barras perderia fórmula e fator, e isso seria mudança de conteúdo, não de formato. A lista das quatro taxas equivalentes fica em prosa (lista nativa da Substack), fora da peça. |
| **diag-01** | "ANBIMA ou B3?", junto de "Em números: dezembro de 2026 tem 22 dias úteis … e 20 dias de pregão" | Calendário de dezembro de 2026 em grade, com três estados por dia: dia útil e pregão; dia útil sem pregão (24/12 e 31/12); nem um nem outro (fins de semana e 25/12) | Relação estrutural (quais dias pertencem a qual calendário), sem métrica central → diag (critério 2). Torna visível que a diferença está em dois dias específicos e não espalhada no ano. graf perde porque não há série a comparar, a contagem 22 × 20 cabe na frase. info perde porque é uma peça só. |
| — info-NN | — | Não se aplica | Nenhuma síntese exige mais de uma peça. Padrão: não tem. |

**Considerado e deixado em prosa:** um fluxo "duas datas → régua → τ → motor → fator", ou as
quatro perguntas como etapas de um fluxo. É a metáfora central do autor (critério 4), e o
texto já a resolve com duas listas curtas e duas fórmulas. Um diagrama repetiria o texto sem
acrescentar informação (regra 9 do guia). Fica em prosa.

Formato: Plotly com tokens de `../../brand/` (`marca-syntaxis`), exportado em PNG/SVG, como
nos posts anteriores. As peças ficam na etapa 8.

## Confirmação dos três pilares

- **Dado**: LTN 12% → 11,85%; dias úteis 2024–2028; CDB em quatro réguas; taxas
  equivalentes; dezembro 22 × 20; a saída de cada bloco de código.
- **Narrativa**: o número que não bate (abertura) → a pergunta "de quê?" → régua e motor → por
  que o dia útil (DI, 1997) → quanto custa errar → qual calendário → como não errar no código
  → outros relógios → as quatro perguntas.
- **Visual**: graf-01, graf-02, diag-01.
