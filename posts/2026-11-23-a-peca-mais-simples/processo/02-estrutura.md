# Etapa 2 — Estrutura

O rascunho já chega estruturado, e o pipeline não reordena a argumentação. Esta etapa preenche a
Ficha de Saída, confere a estrutura contra o backward design, mapeia os movimentos e decide os
visuais pelo critério. Proposta de mudança estrutural, se houver, vira pergunta ao autor.

## Ficha de Saída (`docs/BACKWARDS_DESIGN.md` §2)

O rascunho não traz a Ficha. Os oito campos saem do próprio corpo, sem conteúdo novo.

| Campo | Conteúdo |
| --- | --- |
| 1. Competência de saída | *Precificar* uma LTN a partir da taxa, e a taxa a partir do preço, com du/252 e os truncamentos do Tesouro; *medir* o risco de preço (*duration* modificada, DV01) e *decompor* uma variação de preço em carregamento e choque de taxa; *dizer* contra o que a taxa da LTN aposta, comparando-a com a Selic esperada (expectativa + prêmio de prazo); e *escolher* o uso que cabe (casar compromisso, travar taxa, tomar posição). |
| 2. Teste de transferência | O CDB prefixado de banco médio a 16% ao ano, vencimento em 1º/1/2029, no mesmo 17/11 em que a LTN pagava 14,98%. O leitor deve: precificar R$ 1.000 de face na mesma régua (cerca de R$ 732,56, ver M9); separar o ponto percentual a mais entre curva (nenhum: mesma data, mesma fila de taxas) e o que paga outra coisa (crédito do banco, FGC no lugar do Tesouro, falta de recompra diária); e dizer o que muda se precisar sair antes. O texto não explica CDB prefixado. |
| 3. Tese de fundo | "Quem compra LTN não aposta na queda dos juros. Aposta contra a curva." Mesma família de "Preço não é opinião. É o custo da réplica." (texto anterior) e "Capitalização não é lei da natureza. É cláusula." (a-corda-e-o-arco): o número que parece previsão é preço de uma regra. |
| 4. Erro-alvo | "Prefixado é para quem acha que os juros vão cair, e o preço da LTN segue o Copom." Gente competente repete (é a frase de material de corretora e de assessor), e ela tem um pedaço de verdade, que o Mito concede. |
| 5. Ferramenta prática | A linha do PU com o truncamento do Tesouro e as três fórmulas de planilha (du, PU a partir da taxa, taxa a partir do PU); *duration* modificada e DV01; a decomposição carregamento × choque; a regra de empate LTN × LFT (Selic acumulada contra (1 + i)^(du/252)) com os três cenários; os dois cuidados do uso (data e valor nominal). |
| 6. Âncora de autoridade | Decreto nº 12.814/2026, art. 2º (características da LTN); Lei nº 10.179/2001; Tesouro Nacional, metodologia de cálculo dos títulos (fórmula e truncamentos); PAF 2026 revisado (metas de composição da dívida); Boletim Focus; Tuckman e Serrat (fatores de desconto, DV01). |
| 7. Os dois lados do balcão | **Quem emite:** o Tesouro (custo × risco, PAF, leilão, *dealers*, recompra em outubro). **Quem empresta com ela:** o Banco Central (compromissadas; LRF art. 34). **Quem carrega:** bancos (posição na curva, LCR, garantia), fundos, previdência, não residentes. **Quem compra na ponta:** a pessoa física do Tesouro Direto (a Prateleira). Distribuidor: não tratado; nenhuma das três condições do §4.3 se verifica (custódia da B3 e taxa da instituição aparecem como custo, sem efeito na prateleira). |
| 8. Ponte de série | **Vem de** "Cara, eu ganho. Coroa, eu não perco." (a NTN-F montada com três LTNs; a promessa do *bootstrapping*, aqui rolada). **Aponta para** a NTN-F no próximo texto; o *bootstrapping* depois dela; e um texto próprio para o título de inflação (ver alerta de promessas no briefing). |

**Verificação: a sequência entrega o campo 1?**

| Competência | Onde o texto a produz |
|---|---|
| precificar (taxa → preço → taxa) | "Uma linha, quatro textos" (a fórmula, cada pedaço ligado a um texto da série) → "O preço do Tesouro" (14,98% → R$ 746,004202; truncamentos; as três fórmulas de planilha; 12,40% de volta a partir de R$ 773,741961) |
| medir risco e decompor | "Quanto o preço anda" (*duration* = prazo; modificada 1,83; DV01; ±1 p.p.; convexidade) e a decomposição dos −3,58% em +1,12% de carregamento e −4,65% de choque |
| dizer contra o que aposta | Mito (a versão que circula; a queda já estava no preço em 8/10) → "A aposta escondida na taxa" (regra de empate LTN × LFT; cenários; prêmio de prazo; outubro explicado pelo prêmio) |
| escolher o uso | "Três trabalhos na carteira" (compromisso com data, trava, posição; o erro de pôr a reserva em LTN) |
| teste de transferência (CDB) | Fecho. Exige a fórmula (mesma régua), a ideia de curva como fila por prazo (Mito, Ponto Cego) e as três gavetas de risco da anatomia (crédito, liquidez, preço), com o FGC já glosado. O leitor viu tudo. |

Entrega. A lacuna possível: a anatomia diz que o risco de crédito da LTN é "o menor do país" e que
não há FGC "porque não há banco no meio", mas não diz que crédito e liquidez entram na taxa como
prêmio. O teste pede exatamente essa separação. É raciocínio a transferir, não conteúdo que falte;
a etapa 5 confere se o exercício não fica difícil demais com o que o texto deu.

## Mapa de movimentos

| Seção do rascunho | Movimento | Ato do arco | O que prova |
|---|---|---|---|
| Abertura (sem H2), tempo 1 | 1 — Abertura (costura) | Gancho | A promessa do *bootstrapping*, o barão, a promessa rolada; a LTN foi cobaia de quatro textos e nunca apresentada; a série muda de rumo, um título por vez. |
| Abertura, tempo 2 | 1 — Abertura (modo A) | Contexto | Outubro de 2026: leilão recorde, Prefixado 2029 de R$ 773,74 a R$ 746,00, eleição, leilão cancelado e recompra, Selic parada. Pergunta-âncora dupla. |
| Prefixado para quem acha que o juro vai cair | 2 — O Mito | Setup | A versão que circula (prefixado para quem acha que cai; LTN segue o Copom); o pedaço de verdade; os fatos de outubro contra ela; a queda já estava no preço em 8/10. Tese isolada: "**Quem compra LTN não aposta na queda dos juros. Aposta contra a curva.**" Define a curva como fila de taxas por prazo. |
| Cinco títulos, um devedor | 3 — A Anatomia | Setup | Base legal (Lei nº 10.179/2001, Decreto nº 12.814/2026), Selic (sistema), as quatro perguntas, a tabela dos cinco títulos, o devedor único, a LTN pelo art. 2º, datas e prazos, tributação, liquidez, risco. Fecha com a frase-sinal (§5.3): "Até aqui, é o que a página do Tesouro Direto conta. A partir daqui, a conta." |
| Uma linha, quatro textos | 3 → bloco de matemática financeira | Ação crescente | A fórmula do PU; régua, motor, etiqueta, réplica; a LTN como fator de desconto vendido em lotes, "o átomo da curva prefixada". |
| ↳ O preço do Tesouro | (cont.) | Ação crescente | A conta com número real (R$ 746,004202 contra R$ 746,00 na tela); truncamentos; as três fórmulas de planilha; o caminho de volta (12,40%). |
| ↳ Quanto o preço anda | (cont.) | Ação crescente | *Duration*, *duration* modificada, DV01, convexidade; a decomposição dos −3,58% (carregamento × choque); o Tesouro Selic rendeu 1,2% no período. |
| Quem vende, quem compra, quem empresta | 4 — O Lado de Lá (produto: engenharia de quem emite) | Conflito | O problema do Tesouro não é o seu. |
| ↳ O Tesouro trava o custo | 4 (cont.) + 6 parcial | Conflito | Custo × risco (LFT × LTN); PAF e a fatia de prefixados; leilão, *dealers*, segunda rodada; outubro dos dois lados (NTN-F 2031 vendida a 12,61%, recomprada a 15,79%). |
| ↳ O Banco Central empresta com ela | 4 (cont.) + 6 parcial | Conflito | LRF art. 34; compromissadas (R$ 885,7 bilhões por dia). |
| ↳ Os bancos carregam, garantem e protegem | 4 (cont.) + 6 parcial | Conflito | Três gavetas da tesouraria (posição na curva, LCR, garantia); detentores da dívida. |
| A aposta escondida na taxa | 5 — O Ponto Cego, por contraste com o vizinho (LFT) | Clímax | A regra de empate; Focus; três cenários; o prêmio de prazo; outubro explicado sem o Copom; o ponto cego da versão que circula. |
| Três trabalhos na carteira | 8 — A Prateleira (alocação, risco relativo) | Resolução prática | Pagar conta com data (R$ 100 mil; IR; taxa líquida; dois cuidados); travar taxa; tomar posição (*duration*); o erro mais caro (reserva em LTN). Volta à pergunta da tabela. |
| De volta a outubro | 7 — Fechamento do loop | Resolução | O Tesouro fez o serviço dele; quem comprou a 12,40% fez uma aposta com pouco prêmio; os −3,6% são o preço de sair, não o resultado da aposta. |
| A peça mais simples | 9 — Síntese + ponte | Fechamento | Retoma a tese sem jargão; refrão isolado; exercício do CDB; Skill Check; ponte para a NTN-F e para o barão; CTA de encaminhamento. |
| Para continuar aprendendo | 10 | — | 4 itens, 2 livros (Tuckman e Serrat; Securato), 2 documentos do Tesouro (metodologia; PAF). Atende a §5.7. |

**Opcionais:** o 7 existe porque a abertura é modo A (obrigatório). O 6 (Materialidade) não tem
seção própria: os números de escala (leilão recorde, giro de R$ 42,9 bilhões no secundário, fatia
de 21,14% na dívida, R$ 885,7 bilhões em compromissadas, detentores) estão dentro da anatomia e do
Lado de Lá, a serviço de cada argumento. Correto: a tese não depende de escala.

**Ordem:** 3 → matemática → 4 → 5 → 8 → 7 → 9. O 7 depois do 8 funciona: o leitor relê outubro
já sabendo o que cada uso da LTN aposta. Nada a propor.

**Arco (versão completa, `references/tecnicas-narrativas.md`):** gancho (promessa rolada) →
contexto (outubro) → ação crescente (anatomia e conta) → conflito (os lados do balcão) → clímax
(a aposta escondida na taxa) → resolução (prateleira, outubro relido) → fechamento técnico (tese,
exercício, ponte). O fechamento é o da voz técnica.

## Três pilares

- **Dado:** leilão de 8/10, cotações do Prefixado 2029, PAF, detentores, Focus, contas próprias
  declaradas.
- **Narrativa:** o caso de outubro, aberto na abertura e fechado em "De volta a outubro".
- **Visual:** `graf-01` e `graf-02` (abaixo), mais as duas tabelas.

## Visuais — decisão pelo critério

### `graf-01` — o Prefixado 2029 em outubro (marcador M3)

- **Onde:** no Mito, onde o rascunho já tem o placeholder ("embedded content"), logo depois de "o
  Prefixado 2029 perdeu 3,6%" e antes de "E tem o outro lado."
- **Pergunta:** a taxa do Prefixado 2029 subiu de 12,40% para 14,98% entre 13/10 e 17/11 com a
  Selic parada em 13,75%?
- **Critério:** há série numérica real (11 cotações de taxa de compra do Tesouro Direto, 9/10 a
  17/11/2026) contra uma referência (meta Selic) → **gráfico**. Diagrama perde: há métrica central.
  Infográfico perde: uma peça só carrega o ponto. Taxa (não preço) no eixo, porque a comparação é
  com a Selic, na mesma unidade.
- **Forma:** linha da taxa em `grove.500`; meta Selic como degrau em `slate`; anotações em 13/10
  (12,40%), 25/10 (eleição), 26/10 (leilão cancelado e recompra), 4/11 (Copom mantém 13,75%) e
  17/11 (14,98%).
- **Dados:** a etapa 3 levanta as 11 cotações (Tesouro Direto; a fonte do rascunho cita InvestNews
  e EuQueroInvestir como compilações). Se não fechar, `graficos.md` sai com `[VERIFICAR]` e o
  autor fornece a série que usou.

### `graf-02` — Copom × taxa prefixada, a história longa (marcador M2)

- **Onde:** no Mito, onde o autor deixou a nota, logo depois da versão que circula ("…sobe quando
  ele corta, cai quando ele aperta.") e antes de "Tem um pedaço de verdade aí." A etapa 4 escreve
  uma frase de anúncio com dois-pontos, no padrão do autor ("Lado a lado com…").
- **Pergunta:** a taxa prefixada acompanha o Copom, ou anda antes dele e salta sem ele?
- **Critério:** há série numérica real (meta Selic das reuniões do Copom e uma taxa prefixada de
  prazo fixo, por exemplo o *swap* DI × pré de 360 dias ou a taxa do Tesouro Prefixado, em duas
  décadas) → **gráfico**. Diagrama perde: há métrica central. **Infográfico perde**: o ponto
  (acompanha nos ciclos longos, antecipa nas viradas, salta nos sustos) cabe numa peça só, com
  anotação dos episódios; não há duas peças que só façam sentido lidas juntas
  (`.claude/agents/prompts-visuais.md`, critério de gatilho). O autor escreveu "infográfico" na
  nota; ver T2.
- **Forma:** meta Selic em degrau (`slate`) e taxa prefixada em `grove.500`; anotações de
  episódios que a pesquisa confirmar (candidatos: eleição de 2002; crise de 2008; 2015; queda
  antecipada de 2016–2017; pandemia e alta antecipada de 2020–2021; estresse fiscal de dezembro de
  2024; outubro de 2026).
- **Pesquisa (etapa 3):** o pedido do autor é "pesquisa aprofundada sobre esse ponto do Copom e
  altas e baixas na taxa da LTN". O pesquisador levanta a série, a fonte primária (BCB/SGS, ANBIMA,
  B3, Tesouro Transparente) e os episódios com data e número. O que entra no texto é o gráfico e,
  no máximo, a frase de anúncio; o resto é contexto para o autor.
- **Alerta para a etapa 5:** dois gráficos no mesmo H2, a três parágrafos um do outro. Respondem
  perguntas diferentes (a história longa × o caso de outubro), mas a etapa 5 avalia o peso da
  seção.

### Tabelas

As duas tabelas do rascunho (os cinco títulos; os cenários LTN × LFT) ficam como tabela markdown,
pelo precedente do post de 18/11. O Substack não tem tabela nativa; o autor converte na
publicação. Diagrama perderia: são atributos e valores, não relação estrutural.

### O que não vira visual

- A decomposição do prejuízo (+1,12% × −4,65%): cabe em uma frase com a conta; um gráfico de
  cascata seria o terceiro gráfico da primeira metade. Fica em prosa.
- "LTN = fator de desconto; NTN-F = pacote de LTNs": já foi o `diag-01` do texto anterior.
- O barão, o átomo e a molécula: metáforas do autor; este pipeline não produz ilustração.

## O que fica de fora

- História dos títulos públicos (ORTN, OTN, a dívida dos anos 1980) e do Tesouro Direto.
- NTN-F, NTN-B e LFT em detalhe: cada uma tem texto próprio na série.
- O *bootstrapping* e a ETTJ: rolados para depois.
- Marcação a mercado de fundos e a "volatilidade" do Tesouro Direto como tema.
- "Tesouro Prefixado: o guia completo" (2024): não citar nem linkar (M7).

## Tensões registradas nesta etapa

- **T2 — Gráfico ou infográfico (M2).** A nota pede "incluir um infográfico". Pelo critério da
  etapa 2, a peça é um gráfico anotado (há série real e uma peça carrega o ponto). Pergunta ao
  autor: segue como gráfico anotado, ou ele quer de fato um infográfico (por exemplo, linha do
  tempo dos ciclos do Copom com cartões de episódio ao lado da série)? A etapa 8 produz o gráfico
  pelo critério; se o autor escolher o infográfico, reentra na 8 sem consumir loop.
