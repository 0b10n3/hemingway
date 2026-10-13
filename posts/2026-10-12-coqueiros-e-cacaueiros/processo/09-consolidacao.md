# Etapa 9 — Consolidação (agente `revisao-editorial`)

Post: `2026-10-12-coqueiros-e-cacaueiros` · `linha_editorial: Spoiler` · voz ensaística.
Arquivos alterados: `posts/2026-10-12-coqueiros-e-cacaueiros/post.md` e `posts/2026-10-12-coqueiros-e-cacaueiros/diagramas.md`.
Base: o `post.md` montado a partir do corpo de `processo/04-draft-v3.md`. Os números de linha abaixo se referem ao `post.md` final. A tabela de 06/07 usa os números do v3: até a l. 75, a linha do post é a do v3 menos 5; depois disso, menos 6, porque o comentário HTML do `diag-01` saiu.

## 1. O que foi aplicado

### Da etapa 7 (verificação técnica): as 2 correções ⚠️, com a redação exata proposta
- l. 32: `"metendo um coco debaixo da terra"` → `"metido um coco debaixo da terra"`. Fonte: *Tratado*, cap. XXXIV.
- l. 54: `No fim dos anos 1980, um fungo, a vassoura-de-bruxa, cortou a produção nacional em mais da metade.` → `No fim dos anos 1980, chegou um fungo, a vassoura-de-bruxa. Ao longo da década seguinte, a produção nacional caiu mais da metade.`

### Da etapa 6, itens `norma` (todos)
- l. 14:
  - ponto final depois de "ideias de texto" e fim do espaço duplo;
  - "praias", "beira-mar", "mel de cacau...", "oferecidos" (concordância com o sujeito composto);
  - ponto final no fim do parágrafo.
- l. 16: "uma série", "_O livro dos cinco anéis_", "Miyamoto Musashi".
- l. 18: "passagens".
- l. 26: "Embrapa (Empresa Brasileira de Pesquisa Agropecuária)" e "seria a Índia ou o Sri Lanka".
- l. 46: "de origem." (sem o espaço antes do ponto).
- l. 84: "polemizar sobre as fronteiras".
- l. 106: "O que é fácil para você parece óbvio." (sem a vírgula entre sujeito e verbo).
- l. 108: "Você se lembra… Não se lembra…".
- l. 122: '…me pediria?" Faça' (sem a pontuação dupla).
- l. 126: "Isso? Qualquer um faz." (maiúsculas depois de "?"; os dois-pontos vieram junto, ver itens `linha`).
- l. 138: "_Duration_ (o prazo médio ponderado dos pagamentos de um título)" e "CRA (Certificado de Recebíveis do Agronegócio)".
- l. 156: "CRI (Certificado de Recebíveis Imobiliários)" e "Essa é a camada em que a IA ajuda, mas que ela não substitui."
- l. 176: "responda a este e-mail".
- T-1, itálico de estrangeirismo, 15 ocorrências. É a lista de linhas da 06; o resumo da 06 diz 16, mas a própria lista dela soma 15.
  - _skill(s)_ nas l. 40, 60, 64, 66, 68, 136, 142, 152 (×3), 160;
  - _Duration_/_duration_ nas l. 138 e 156;
  - _big data_ na l. 152;
  - _pipelines_ na l. 158.
  - Exceções mantidas: "skill" em redondo no alt-text do `diag-01` e no frontmatter (subtítulo, `nota_substack`, `busca_organica`). Ficam em redondo também feedback, e-mail, newsletter, Spoiler/spoiler e os nomes de ferramenta.
- T-2: espaço no fim da linha removido nas 13 linhas apontadas (l. 16, 18, 34, 36, 50, 60, 62, 72, 82, 86, 106, 110, 112). A varredura final não acha mais nenhum.

### Da etapa 6, itens `linha` nos trechos redigidos pelo pipeline
- l. 140: "Depois que pegou, o coqueiro parou de pedir."
- l. 162: "Os três são cacaueiros." Saiu "Nenhum dos três dá fruto sem cultivo.", que repetia a l. 138. "pagou o custo de entrada" virou "teve um custo de entrada".
- l. 164: "…a versão do modelo de linguagem também. A ferramenta continua pedindo poda."
- l. 168: "alguém teve de plantá-lo antes…" ("trazê-lo" saiu, porque o "trazer" já está na l. 140).
- l. 116, ANBIMA: não aplicado por decisão do pipeline principal (ver §2).

### Da etapa 6, itens `linha` no texto do autor (só os de clareza)
- l. 14: vírgula depois de "Pelo litoral sul da Bahia" e "à beira-mar".
- l. 16: "na semana passada" e ", de Miyamoto Musashi".
- l. 18: o ponto virou vírgula ("…terra de Jorge Amado, a primeira ideia parecia pronta.") e "por Itacaré e por Ilhéus".
- l. 26: aspas simples em 'coco-da-baía'.
- l. 50: "a planta enriquece uma região inteira".
- l. 120: "Repare no que as pessoas vêm te pedir fora do processo formal."
- l. 126: dois-pontos antes do discurso direto (`responde: "Isso? Qualquer um faz."`).
- l. 136: "_So Good They Can't Ignore You_ (2012)" e 'capital de carreira' entre aspas simples.
- l. 152: "mas ainda tropeça quando é preciso julgamento com nuance".
- l. 174: "o meu coqueiro — ensinar — para ajudar".

### Placeholder do `diag-01` (l. 70)
O alt-text foi trocado pelo refinado de `diagramas.md`, numa linha só. O formato `![Diagrama: ...](diag-01)` foi mantido, com "skill" em redondo.

### `diagramas.md`
Acrescentei um parágrafo "Gate de Tufte (etapa 9)" depois de "Escolha de layout". Ele registra três coisas:
- por que não há `rangemode="tozero"`: os eixos são conceituais e invisíveis, e o `range` só enquadra o plano 0–10;
- por que o Lie Factor não se aplica: nenhum tamanho, área ou posição codifica dado;
- que as bordas `width=1` são hairlines dos quadrantes, não moldura.

O código não mudou.

## 2. O que NÃO foi aplicado, e por quê

**Itens `linha` de voz no texto do autor, que vão ao gate:**
- l. 66: "sai bem feito" → "bem-feito". As duas leituras se defendem.
- l. 142: "Com _skill_ acontece algo parecido." → "Com as _skills_, acontece…". O singular genérico é oral, e é escolha de voz.
- l. 126: "Esse desconforto é justamente o sinal." → "Esse desconforto com o elogio…". O demonstrativo fica sem antecedente explícito.
- l. 156: glossas de "curva de juros" e "marcação a mercado". A recomendação da 06 é manter sem gloss (a lista funciona como ementa). As glossas prontas estão em `06-revisao.md`, l. 198.
- l. 14: "Voltei de viagem com duas ideias de texto." como parágrafo próprio. Opcional.

**Divergência de grafia, que vai ao gate:**
- A 06 propôs "Anbima" (l. 116) por coerência com "Embrapa" e com o precedente da casa (`o-certificado-nao-muda-o-devedor` usou "Anbima").
- Mantive ANBIMA e Embrapa como estão, porque é a grafia que cada instituição usa para si: a ANBIMA se grafa em caixa alta, a Embrapa só com inicial maiúscula. Não é mistura de critério dentro do post. É seguir a grafia de cada instituição.
- O conflito com o precedente da casa ("Anbima") fica registrado para o autor decidir a convenção daqui em diante.

**Decisões estruturais do autor, intocadas:** subtítulo, "duas ideias", simetria em dois recortes, Databricks no CTA × "a ferramenta muda", fecho sem gancho e os itens de atenção da 5a (ver §5).

**Sugestões opcionais da 07, não aplicadas:**
- 2.2: precisão "na Amazônia portuguesa (Pará e Maranhão)";
- ano de Stone & Heen no corpo;
- título brasileiro do Newport;
- tabela de fontes no fim do post. A 07 propôs uma, mas o precedente Spoiler (`borboletas…`) não tem seção de fontes. Decisão do autor.

**Frontmatter:** `status: em-revisao` mantido. O subtítulo ficou sem itálico.

## 3. Checklist da etapa 9, item a item

1. **Coerência entre etapas: ok.**
   - A correção da vassoura-de-bruxa (07) não quebra nenhuma frase da 06. A frase anterior ("Quando o cuidado falha, o tombo é do mesmo tamanho.") continua ligada ao novo par de frases.
   - "metido" encaixa na construção de particípio absoluto da frase do autor.
   - O ajuste da re-checagem pós-v2 (remover "trinta e quatro anos depois, se você confiar no cronista…") já estava no v3 e foi confirmado no texto final.
   - A 06 (l. 162/164/168) e a 05 (b)4 apontam no mesmo sentido, e os cortes aplicados reduzem a repetição sem conflito.
   - Nenhum corte ou reordenação pedido pela 05 ficou sem aplicar por omissão. O que não foi aplicado é decisão do autor (§5).
2. **Aderência à voz (§9 do guia):**
   1. Gloss na primeira ocorrência: ok. Duration, CRA, CRI, Embrapa e ANBIMA estão glosados. "cabruca" tem o aposto como gloss. Ficam sem gloss, com justificativa da 06, Spark, Python, SQL, Databricks e IA. Há uma omissão deliberada pendente do autor: curva de juros e marcação a mercado.
   2. Exemplo depois do conceito: ok. Isso vale para a definição de coqueiro e cacaueiro → diagrama, para "cacaueiro pode virar coqueiro" → programação e para a tese da nota (l. 78) → caso da graduação. A cena da abertura antes da tese é o movimento da voz ensaística, não uma violação.
   3. Zero negrito e zero itálico de ênfase: ok. Os itálicos são só de título de obra ou publicação e de estrangeirismo.
   4. H2 por seção: ok. São seis H2, e a abertura fica sem H2, como é convenção.
   5. Autoridade nomeada: ok. Newport (2012), *Future of Jobs Report 2025* do WEF, Gabriel Soares (1587), Embrapa, Stone & Heen. Stone & Heen estão sem ano. A 07 só confirmou a edição brasileira (2016), e o ano da original não foi verificado, por isso não entrou.
   6. Uma voz só (ensaística): ok.
   7. Voz ensaística: **falha parcial.** Há pergunta retórica genuína (l. 170). **Não há CTA de compartilhamento nem gancho para o próximo texto** (crítica item 13). A promessa do Musashi (l. 16) é o candidato natural ao gancho. Vai ao gate.
   8. Voz explicativa: não se aplica.
   9. Tiques de IA: ok. Nada da lista sobreviveu à revisão. Densidade de "Não é X. É Y." aceita pela 06 (T-3), toda do autor.
   10. Instituições com nome correto: ok. O nome por extenso da ANBIMA foi confirmado pela 07, e o da Embrapa está correto. Nenhuma norma citada no corpo.
3. **`[VERIFICAR]`/`[FAIXA]`: ok.** Os dois `[VERIFICAR]` estão visíveis no texto. Nenhum `[FAIXA]`.
4. **Placeholders: ok.** O `diag-01` do `post.md` tem bloco em `diagramas.md`, e o inverso também vale. Não existem `graficos.md` nem `infograficos.md`, e nenhum `graf-NN`/`info-NN` é citado.
5. **Antipadrões: ok.** Passei `antipadroes.md` da `voz-syntaxis` e varri os marcadores mais comuns da frente D (crucial, fundamental, jornada, ressaltar, "em suma", "cada vez mais", "não apenas" etc.). A única ocorrência é "mergulho", em sentido literal. Os trechos do pipeline estão limpos depois dos ajustes da 06.
6. **Frontmatter: ok**, mas com duas observações para o gate:
   - `busca_organica` ("Skills naturais e aprendidas…") também anuncia o eixo de origem, o mesmo problema do subtítulo (crítica item 8).
   - `nota_substack` afirma "chegou à Bahia em 1553" sem a atribuição "segundo a Embrapa". A 07 registrou que não há documento de época para 1553 e só não abriu `[VERIFICAR]` porque o corpo atribui a data. Na nota, a atribuição some.
   - Título, data, linha, tags e status estão coerentes com o briefing (item 13).
7. **Manchete: não forçada.** "Coqueiros e cacaueiros" é temático e foi aprovado pelo autor na etapa 0. A quebra de intuição já está no assunto do e-mail ("Sua melhor nota pode estar mentindo para você").
8. **Achado enterrado: sem alarme.** A tese (custo, não origem) fecha a abertura (l. 40–42), e o spoiler da nota se anuncia explicitamente (l. 78), além de estar no assunto do e-mail. Persiste o problema de ritmo da crítica item 5: são cerca de 60 linhas até a nota. Não é insight enterrado.
9. **Inventário visual: ok.** Não existe `infograficos.md`, então não há o que justificar. Os arquivos `figuras/diag-01.svg` e `figuras/diag-01.png` existem.
10. **Fluxo Spoiler: ok.** O único bloqueante da 5a tem resposta do autor registrada (separar fundamento de ferramenta), e o gate da 5a está liberado. A etapa fecha.
11. **Gate de Tufte (`diag-01`): ok.** A exceção ao `rangemode` agora está justificada por escrito no spec. Não há 3D, sombra, textura nem moldura. O Lie Factor não se aplica, porque nada codifica dado.

## 4. Lista final de `[VERIFICAR]`

1. l. 116: `[VERIFICAR: nome oficial do programa]`, o programa de mentoria/carreira da ANBIMA em 2025. Só o autor resolve.
2. l. 174: `[VERIFICAR: link da Notas de um Professor]`, a URL. Só o autor resolve.

`[FAIXA]`: nenhum.

## 5. Pendências para o gate (etapa 10)

**Estruturais (crítica, 05):**
- **Item 8, subtítulo:** "Skills nativas, skills importadas…" anuncia o eixo de origem que o post descarta. Vale o mesmo para `busca_organica`.
- **Item 6, "duas ideias de texto":** a segunda ideia nunca é nomeada. Com o ponto final restaurado, a promessa ficou mais visível.
- **(b)3, simetria em dois recortes:** "O símbolo de importado é brasileiro" só vale em escala de país, logo depois de "na Bahia, ele também chegou de fora".
- **Item 13, fecho:** sem CTA de compartilhamento e sem gancho para o próximo texto. É o item 7 do §9 que falha.
- **(b)4, repetição "custo de entrada / se planta sozinho":** reduzida pelos cortes da 06, mas ainda aparece nas l. 38, 140, 162 e 168.
- **Item 4 / (b)1, Gabriel Soares:** o texto usa só a metade favorável. O mesmo parágrafo da fonte fala do "bicho no olho". É decisão do autor já registrada.
- **Itens 2, 5, 9, 10, 11 e 12 (média/baixa):** não reabertos. O item 11 ("cuidado falha → tombo") sobrevive à correção da 07, que tirou a causalidade única do verbo ("caiu") mas manteve "Quando o cuidado falha" na frase anterior.

**Sinalização nova da 06:** Databricks no CTA (l. 174) × "O Databricks de hoje vai mudar… A ferramenta continua pedindo poda." (l. 164). Depois do ajuste da l. 164, o contraste ficou mais explícito. O autor decide se troca o exemplo do CTA ou se acrescenta "e os fundamentos por trás delas".

**5a, 11 itens de atenção e 7 nitpicks sem resposta (não bloqueiam):**
- dados em escala × exposição à IA;
- planilha → _pipelines_;
- WEF como expectativa global;
- "calcular";
- taxa de câmbio × valor;
- Newport × Macnamara;
- "nenhuma é melhor";
- comparação de notas entre disciplinas;
- firma, custo privado e Benson et al.;
- auditoria de energia;
- vassoura-de-bruxa: a cronologia já foi corrigida pela 07; o ângulo de preço e de ciclo segue aberto;
- nitpicks: prospecto (a 07 confirmou a dispensa pela Res. CVM 160, art. 9º, I), "quase tudo que vale dinheiro", três pessoas, fila, memória do esforço, profissional em T, "segundo maior" e "mesmo tamanho".

**Linha e voz não aplicados (§2):** "bem-feito", "Com as _skills_,", "Esse desconforto com o elogio", glossas de curva de juros e marcação a mercado, parágrafo próprio da l. 14.

**Grafia:** ANBIMA/Embrapa mantidas na forma institucional, contra o precedente "Anbima" da casa. O autor fixa a convenção.

**Opcionais da 07:**
- "Pará e Maranhão" (2.2);
- ano de Stone & Heen;
- título brasileiro do Newport. Se entrar, `[VERIFICAR: ano/tradutor da edição Alta Books]`;
- tabela de fontes no fim do post. A proposta está pronta em `07-verificacao.md`.

**Visual:**
- O `post.md` não traz legenda em itálico sob o `diag-01`. A legenda existe em `diagramas.md`, e há precedentes nos dois sentidos.
- Do `estado.json`: as fontes da marca não estão instaladas, e o PNG foi renderizado com fontes de fallback. Além disso, `brand/DESIGN.md` §10 conflita com §4.2. As duas questões ficam fora deste pipeline.

**Confirmações biográficas do autor (07, §3.2):** notas de álgebra × análise "em vários semestres"; IC em sistemas dinâmicos; avaliações nas equipes; roteiro da viagem; frase do T; método de plantio observado (l. 36).

**Git:** nada foi commitado nesta etapa. O `post.md` continua untracked e o `diagramas.md` está modificado; o pipeline principal grava `09-consolidacao.md`, atualiza `estado.json` e commita.
