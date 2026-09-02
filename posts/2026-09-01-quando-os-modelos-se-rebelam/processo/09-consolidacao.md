# Consolidação — Quando os Modelos se Rebelam (rodada 4)

Aplica `05-critica.md` (já incorporada em `04-draft-v1.md` na própria etapa 4, ver nota de
revisão pós-crítica naquele arquivo), `06-revisao.md` e `07-verificacao.md` sobre
`04-draft-v1.md`, produzindo `post.md` na raiz. Entregáveis já publicados na etapa 8:
`capa.md`, `ilustracoes.md`, `graficos.md`, `diagramas.md`.

## O que foi aplicado de `06-revisao.md`

- Removidas ~25 ocorrências de negrito/itálico de ênfase (regra 4 do guia de voz) — termo de
  definição vira aspas simples ('teoria', 'modelo', 'intuição', 'hipótese', 'a bula do
  remédio', 'bate em parte', 'visão semântica', 'ferramenta de ancoragem', 'agora', 'empírica');
  sentença inteira/aforismo perde o negrito por completo (todas as ocorrências listadas no
  laudo).
- Jargão técnico-financeiro sem marcação → itálico: `_hedge_`, `_payoff_`, `_spreads_`,
  `_outlier_`, `_backtest_`, `_feeling_`.
- Correção de concordância: "que o LTCM estava vendida" → "vendido".
- Sigla VaR glossada na primeira ocorrência.
- Sigla CFO glossada ("diretor financeiro").
- Reordenação para resolver ambiguidade sintática: "Não dar a quem usa o modelo falso conforto
  sobre sua precisão" → "Não dar falso conforto a quem usa o modelo sobre sua precisão".
- Consistência de vírgula após advérbio de data no início de parágrafo (seção 4).
- Reancoragem em 1ª pessoa do parágrafo do Fechamento que amarra com a seção 1 ("Isto não
  contradiz..." → "Não é contradição com a ressalva que eu já fiz..."), para casar com a
  moldura pessoal que a seção 1 usa no mesmo argumento ("Minha leitura:...").
- Consistência de formulação de alavancagem ("25 vezes de alavancagem" → "alavancagem de mais
  de 25 para 1", casando com a correção numérica da etapa 7 e com a formulação já usada em
  outros pontos do texto).
- Título do livro sem espaços: "Models.Behaving.Badly." (duas ocorrências).
- Ordem "extremista frustrado" alinhada ao título; regência "entre A e B" corrigida; "ante
  modelos" → "diante de modelos"; "desacoplamento" → "descolamento" (consistência com o
  título).
- Parágrafo de abertura sobre Derman reescrito para resolver quebra de paralelismo (apostos
  nominais + orações verbais sem sujeito de retomada).

**Não aplicado** (fora do escopo desta consolidação, registrado para decisão futura, não
bloqueia): a observação sobre a fórmula "Não é X, é Y" aparecer cinco vezes — item de
vigilância, não correção, per `06-revisao.md`.

## O que foi aplicado de `07-verificacao.md`

- **Kempthorne removido do corpo e da bibliografia** — a atribuição não se sustenta (tabela
  oficial de instrutores do MIT OCW). Texto final: "um dos professores diz", citação mantida
  entre aspas diretas. Bibliografia reformulada para listar os quatro instrutores do curso sem
  implicar autoria principal de Kempthorne.
- **Target forward de 2008 resolvido** — `[VERIFICAR]` substituído pela frase final com fonte
  primária do Banco Central (Trabalhos para Discussão nº 202, Mesquita & Torós, 2010):
  exposição delta de ~US$ 37 bilhões via CETIP, fim de setembro de 2008.
- **Cotações de dólar corrigidas** para precisão de 4 casas (R$3,1283 → R$3,3805), fechando
  exatamente com o "8,06%" já usado no texto e no `graf-01`.
- **LTCM**: patrimônio (início de 1998) e ativos (agosto de 1998) separados por data em vez de
  apresentados como uma única fotografia; "em torno de 25:1" → "mais de 26 para 1"; nocional
  "US$ 1,25 trilhão" (não encontrado na fonte primária) → "US$ 1,3 trilhão" (fim de 1997, PWG
  1999).
- **Bibliografia de Aracruz/Sadia** reformulada para não implicar que a RACEF confirma o número
  de US$ 2,13 bilhões usado no corpo (ela cita R$ 2,5 bilhões sem proveniência rastreável) —
  citação da RACEF removida da linha que sustenta o número, mantida como nota de contexto
  institucional à parte.

Todos os demais números (Ibovespa, London Whale, perda/resgate/devolução do LTCM, os cinco
compromissos do Manifesto, as seis hipóteses de Black–Scholes) foram confirmados sem alteração.

## `[VERIFICAR]` remanescentes em `post.md`

**Nenhum.** Os dois pontos que chegaram com `[VERIFICAR]` explícito nesta rodada (citação de
abertura, volume do target forward) foram resolvidos com fonte primária e decisão final na
etapa 7 — nenhum marcador sobrevive à consolidação.

## Pendência não resolvida nesta etapa — vai para o gate humano (etapa 10)

**Tensão de linha editorial**, registrada em `01-briefing.md` e corroborada estruturalmente em
`05-critica.md` item 5: o rascunho declara `Spoiler`, mas o conteúdo (conceitual, estudo de
caso de terceiros, sem arco de jornada pessoal do autor) pesa, pelo critério de
`PROJECT_DESCRIPTION.md`, para `Notas de um Professor`. `post.md` mantém `linha_editorial:
Spoiler` como valor de trabalho (a declaração original do autor), pendente de confirmação —
não é decisão desta etapa.
