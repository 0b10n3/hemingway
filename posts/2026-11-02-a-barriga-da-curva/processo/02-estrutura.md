# Etapa 2 — Estrutura

A estrutura é a do rascunho. Ele já percorre os movimentos de `docs/BACKWARDS_DESIGN.md` §3 na
variante "matemática financeira" do §4.2. Esta etapa mapeia, preenche a Ficha de Saída, confere
se a sequência entrega a competência e decide os visuais. **Não reordena nem corta seção.** O
reenquadramento da abertura (decisão do autor, etapa 0) é texto, não ordem: entra na etapa 4.

## Ficha de Saída

| Campo | Preenchimento |
| --- | --- |
| **1. Competência de saída** | *Converter* qualquer taxa cotada para a régua brasileira (exponencial, base 252, dias úteis) declarando as três peças que a acompanham (regime, base, dias que contam) e *prever*, antes da conta, de que lado fica a diferença: em prazo menor que o período da taxa, o linear paga mais; em prazo maior, o composto. |
| **2. Teste de transferência** | **Taxa nominal × efetiva num financiamento.** O texto não calcula capitalização mensal de taxa anual; o Fechamento entrega o caso ("Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números é o que você de fato paga?"). Se o leitor faz as três perguntas e chega sozinho a (1 + 0,12/12)^12 − 1, o texto funcionou como aula. Já está no rascunho, no lugar certo (movimento 9). |
| **3. Tese de fundo** | "Capitalização não é lei da natureza. É cláusula." Família: a do du252 ("uma taxa sem régua é um número pela metade"). Os dois formam o par ferramenta da linha, fora da tese-mãe da série de crédito ("o risco muda de endereço"). |
| **4. Erro-alvo** | Que o juro composto rende mais que o simples sempre, e desde o primeiro dia; e, na mesa, que duas taxas com o mesmo número cotado em regimes diferentes são comparáveis. Gente competente acredita: é a versão de livro-texto ("A versão que se aprende cedo") e o "O número na tela é o mesmo" do CDB × operação linear 360. |
| **5. Ferramenta prática** | (a) A regra da corda: prazo < período → linear > composto, com o mesmo número; (b) a equação de equivalência (1 + i₂₅₂)^(du/252) = 1 + i₃₆₀·dc/360; (c) as quatro fórmulas de planilha; (d) as três perguntas (regime, base, dias). |
| **6. Âncora de autoridade** | Origem da régua: **Circular BCB nº 2.761/1997**, com Márcio Garcia (PUC-Rio) como registro de época; **Comunicado BCB nº 7.684/2000** `[VERIFICAR]`. Sobrevida do linear: **Resolução CMN nº 5.171/2024**, art. 6º (citada no corpo, não na bibliografia — §5.7), e a especificação do **FRC de cupom cambial da B3**. Contínuo: metodologias de ETTJ da **ANBIMA** e da **Susep**. Matemática: desigualdade de Bernoulli (resultado clássico, sem citação). |
| **7. Os dois lados do balcão** | Quem aplica × quem toma: "a régua linear paga mais a quem aplica e cobra mais de quem toma sempre que o prazo é menor que o período da taxa" — e o inverso depois do primeiro período. O terceiro ator é **quem cota** (a mesa que monta a curva inteira, o regulador que fixa a régua): é ele que explica a escolha de 1998 (consistência entre prazos). Distribuidor: não se aplica (nenhuma das três condições do §4.3). |
| **8. Ponte de série** | **Vem de:** o du252 (a régua: como contar o tempo), e antes dele LCA e debêntures, que usaram du/252 sem explicá-lo. **Aponta para:** o FIDC, prometido no fim das debêntures e de novo no du252. Este é o segundo parêntese de ferramenta antes dele (reenquadramento, etapa 0). |

**Regra de corte (§2):** campo 2 preenchido. É aula.

## Verificação: a estrutura entrega a competência?

| Seção do rascunho | Movimento(s) | Observação |
| --- | --- | --- |
| Título + subtítulo provisório | 0 | O deck carrega assunto, não tese. Alternativa proposta no briefing, decisão no gate. |
| Abertura sem intertítulo (série; R$ 1 mi a 14% por 126 du; R$ 70.000 × R$ 67.707,83) | 1 (modo B) | Termina na pergunta-âncora ("Por quê? E o que isso muda…"). Reenquadramento na etapa 4. ✓ |
| "A versão que se aprende cedo" | 2 (O Mito) | Mito em voz alta (composto rende mais, sempre, desde o primeiro dia), oposição em frase curta e isolada ("As duas afirmações são falsas."), aforisma ("Capitalização não é lei da natureza. É cláusula."). ✓ |
| "Três réguas para o mesmo tempo" + "O prazo quebrado" | 3 (A Anatomia) | Três regimes com fórmula, t = du/252, convenção linear × exponencial. Frase-sinal (§5.3): "Até aqui, é o segundo capítulo de qualquer livro … O interessante começa quando se pergunta por que cada mercado escolheu a sua régua." É passagem do raso ao profundo. ✓ |
| "Quem escolhe a régua, e por quê" + "A virada de 1998" + "Onde o linear sobrevive" + "E o contínuo" | 4 (O Lado de Lá, versão "de onde vem a fórmula e qual hipótese embute") | Hipótese de cada régua (juro parado × reinvestido), consistência entre prazos (1,07² × 1,14^0,5·1,14^0,5), decisão do regulador, e onde cada régua sobrevive. É a seção mais longa (quatro blocos). Tensão "virada de 1998 repete o du252" (briefing). |
| "A barriga da curva" | 5 (O Ponto Cego), contraste com vizinho nomeado (CDB pré × operação linear 360 a 14%) | Fecha o loop do gancho (R$ 1.070,00 × R$ 1.067,71 no gráfico = os R$ 2.292,17 da abertura em escala R$ 1.000). Camada da base (365/360). Tese isolada: "Ela é a metade de uma cláusula." ✓ |
| "A bola de neve demora a rolar" | 6 (Materialidade, versão conceitual: escala no tempo, não no mercado) | Não é série de mercado; é cálculo próprio que muda o argumento (o juro sobre juro é marginal em prazos curtos). O §3 aceita: o número muda a leitura. Aforisma: "O motor do juro composto não é a taxa. É o tempo." ✓ |
| "Três perguntas antes de qualquer taxa" | 8 (A Prateleira, versão "a conta que o leitor refaz na planilha") | Ferramentas (b), (c), (d). Exemplo 91 dc/63 du → 14,92%. ✓ |
| "Fechamento: o expoente que faltava" | 9 (Síntese + ponte) + teste de transferência | Retoma a tese sem jargão, propõe o teste (nominal × efetiva), ponte para o FIDC, CTA. ✓ |
| "Para continuar aprendendo" | 10 | 4 itens anotados, 3 livros + Garcia. Cumpre §5.7 (3–4 itens, ≥ 2 livros, nenhuma lei). ✓ |
| "Notas de processo (não publicar)" | — | Fora do `post.md`. |

**Conclusão:** a sequência produz a competência do campo 1. A regra da corda (ferramenta a) é
provada no movimento 5, a equivalência e as fórmulas (b, c) no 8, as três perguntas (d) também
no 8, e o teste de transferência vem no 9. A tese aparece isolada no Mito, no Ponto Cego ("metade
de uma cláusula") e no Fechamento. ✓

Movimento 7 (fechamento do loop) não se aplica (modo B); o 5 já fecha o gancho numericamente.

## Observações para a etapa 5 (forma, não decisão)

1. **Peso do movimento 4.** Quatro blocos (por que, 1998, linear, contínuo) entre a Anatomia e o
   Ponto Cego. O centro do texto (a barriga) só chega depois de ~1.200 palavras. Ver se o leitor
   chega lá.
2. **Contínuo como terceiro regime.** Entra na Anatomia, volta no 4 ("E o contínuo") e no graf-01
   (linha tracejada), mas não participa da tese nem da ferramenta. Ver se soma ou dispersa.
3. **"Barriga da curva"** como jargão de mesa (vértices intermediários da curva de juros). Ver
   alerta no briefing.
4. **Vocabulário régua/motor** (tensão do briefing).
5. **CTA "divide a taxa anual por doze"** × "Nenhuma das três réguas é a certa" (alerta no briefing).

## O que fica de fora

- **Juro simples em operações de crédito ao consumidor (Tabela Price × SAC, anatocismo no
  Judiciário).** O texto menciona anatocismo só como nome; a discussão jurídica é outro post.
- **Taxa over antes de 1998 em profundidade**: uma frase com `[VERIFICAR]`, sem cálculo.
- **Convexidade/duration**: "convexa" aparece no sentido de cálculo (curva do montante), não no de
  renda fixa. A etapa 6 evita qualquer frase que sugira o segundo sentido.
- **Black-Scholes e gregas**: uma frase, como exemplo de onde o contínuo vive.
- **Contagem de dias úteis em detalhe**: está no du252; aqui só a fórmula de planilha e o alerta
  do calendário.

## Onde entra graf-NN / diag-NN / info-NN

Restrição de formato (precedentes do CRA e do du252): a Substack não tem tabela nativa; os blocos
LaTeX ficam como bloco de equação da Substack (o autor cola no editor); o bloco de planilha fica
como bloco de código nativo.

| Peça | Onde | Tipo | Por quê (e por que os outros perderam) |
| --- | --- | --- | --- |
| **graf-01** | "A barriga da curva", depois de "quem não fez, pode confiar no desenho" | Gráfico de linhas: montante de R$ 1.000 a 14% a.a., t de 0 a 2 anos, três regimes (simples, composto, contínuo com a taxa cotada como instantânea, tracejado); marcação do ponto de maior distância perto de 6 meses (R$ 1.070,00 × R$ 1.067,71) e do encontro em t = 1 (R$ 1.140,00) | Série numérica (montante em R$ por prazo) → graf (critério 1). A tentação de diagrama existe ("reta × curva" é forma geométrica), mas o desenho carrega métrica real: os valores marcados são os números do texto, e a distância em R$ é o argumento. diag perde porque tiraria os números. info perde porque é uma ideia só. **Atenção de escala:** a distância entre reta e curva é ~0,2% do montante; a etapa 8 decide entre eixo y recortado (com aviso) ou painel inferior com a diferença simples − composto em R$. |
| **graf-02** | "A bola de neve demora a rolar", no lugar do "[embedded content]" | Gráfico de linhas: parcela do juro sobre juro no juro total (%), prazos de 1 a 30 anos, três taxas (6%, 10%, 14%), linha de referência em 50% (a virada: juro sobre juro = juro linear), viradas anotadas | Série numérica por prazo → graf (critério 1). A virada é o argumento ("depois de uma década a 14%", "mais de duas a 6%") e cai no cruzamento com 50%. Alternativa considerada: barras empilhadas capital + juro linear + juro sobre juro a 14%; perde porque mostra uma taxa só e esconde a comparação 6% × 14%. diag e info perdem pelos mesmos motivos do graf-01. O conteúdo original do "embedded content" não veio no arquivo; a etapa 8 reconstrói pela fórmula do rascunho. |
| — info-NN | — | Não se aplica | Nenhuma síntese exige mais de uma peça. Padrão: não tem. |

**Considerado e deixado em prosa:**
- **"Onde cada régua vive"** (Brasil 252 exponencial; cupom cambial linear 360; Treasuries accrued
  linear; taxa legal simples; Susep e modelos em contínuo; ANBIMA discreta). Relação entre
  entidades sem métrica → seria diag (critério 2). Fica em prosa: o rascunho não propõe, a seção
  já é uma enumeração curta com subtítulos, e o pipeline não acrescenta peça que o texto não
  pede. Se a etapa 5 apontar que o movimento 4 está pesado, o diagrama vira opção para o autor.
- **Fatiamento 1,07 × 1,07 = 1,1449**: conta de uma linha, fica em prosa.
- **Prazo quebrado (219.800,00 × 217.186,92)**: dois números, fica em prosa.

Formato: Plotly com tokens de `../../brand/` (`marca-syntaxis`), exportado em PNG/SVG, como nos
posts anteriores.

## Confirmação dos três pilares

- **Dado**: R$ 70.000 × R$ 67.707,83; ln(1,14); prazo quebrado; 1,1449; fevereiro × julho de 1998;
  R$ 299,60 = 280,00 + 19,60; viradas por taxa; 14,19%; 14,92%; 12,68%.
- **Narrativa**: o "você acertou / você errou" da abertura → a versão escolar → as três réguas →
  por que cada mercado escolheu a sua → a barriga (o desenho explica a abertura) → a bola de neve
  demora → as três perguntas → a cláusula.
- **Visual**: graf-01, graf-02.

---

## Revisão pós-etapa 5 (2026-11-04)

A etapa 5 devolveu uma alta (A1) e o pipeline voltou aqui, com escopo restrito. Decisões do
autor (2026-11-04):

1. **Espinha = nominal × efetiva (A1).** Pergunta-âncora: "O motor que a renda fixa brasileira usa
   por padrão é justamente o que paga menos em seis meses. Por que, então, cotar assim…?" Resposta:
   consistência entre prazos (fatiamento), como **propriedade**. A seção 1998 prova outra coisa e
   diz: o motor composto já estava lá (over "efetiva-dia"); a norma trocou a embalagem, uma **taxa
   nominal** (over ao mês, diária × 30), por uma **efetiva**. O fechamento liga essa troca ao teste
   de transferência (12% capitalizados mensalmente → 12,68%). O exemplo de Garcia ganha a distinção
   mês civil × prazo em du.
2. **Movimentos 4 e 5 invertidos (M1, M7).** Nova ordem: Abertura → Mito → Anatomia (+ prazo
   quebrado) → **Barriga (5)** → **Bola de neve (6)** → **Quem escolhe o motor / 1998 / Onde o
   linear sobrevive (4)** → Três perguntas (8) → Fechamento (9) → Bibliografia (10). A taxa legal
   (CMN 5.171) passa a ser o **vizinho nomeado** da barriga, no lugar da operação anônima; o aviso
   "mais adiante" sai. Frase-sinal da Anatomia: "O interessante começa quando se desenha essa
   diferença."
3. **Contínuo encolhido (M2).** A subseção "E o contínuo" vira uma frase em "Onde o linear
   sobrevive". A armadilha dos 15,03% fica na Anatomia. **graf-01 perde a linha tracejada** (ela
   desenhava o erro como se fosse o motor): passa a ter dois motores. Isso não resolve a escala
   (~0,2%); a etapa 8 segue decidindo entre eixo recortado e painel com a diferença.
4. **Título mantido, duplo sentido nomeado (M3).** Um parágrafo na barriga diz que esta não é a
   barriga da curva de juros da mesa (vencimentos intermediários), e sim a do prazo curto.

**Verificação da competência (refeita):** prever o lado (barriga + taxa legal + bola de neve) →
por que o padrão é o composto (fatiamento) → nominal × efetiva (1998) → converter (três perguntas,
equação, planilha, separação motor × régua) → teste de transferência (nominal × efetiva no
financiamento), agora preparado pela seção 1998. ✓

**graf-02:** marcador único no lugar do "embedded content" (B5).
