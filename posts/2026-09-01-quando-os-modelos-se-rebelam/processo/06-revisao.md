# Revisão de linha e norma — "Quando os Modelos se Rebelam"

Fonte: `04-draft-v1.md`, confrontado contra `estilo/estilo-autoral.md` §3-4,
`pesquisa/frente-c-editoracao.md` §3, `.claude/skills/voz-syntaxis/references/antipadroes.md`.
Marcadores `[VERIFICAR: ...]` e placeholders visuais (`ilu-01`, `graf-01`, `diag-01`) não
foram tocados. Seção "Notas de processo" e "Loop etapa 5 → 2/4" ignoradas — não fazem parte
do texto do post.

## Parágrafo de abertura

**Original:** "Numa aula de probabilidade **que assisti** no MIT OpenCourseWare..."
**Sugestão:** "Numa aula de probabilidade **a que assisti** no MIT OpenCourseWare..."
**Motivo (norma):** regência de "assistir" no sentido de "presenciar" é transitiva indireta
("assistir a algo"); a relativa correspondente exige "a que". Primeira frase do post — prioridade
alta.

## Títulos de obra em aspas simples em vez de itálico

**Original:** títulos inteiros entre aspas simples — `'Topics in Mathematics with
Applications in Finance'`, `'Models. Behaving. Badly.'`, `'An Engine, Not a Camera'`,
`'Financial Modelers' Manifesto'` e as 8 entradas de "Fontes e leituras".
**Sugestão:** itálico (`*Models. Behaving. Badly.*` etc.), preservando aspas simples só para
jargão/conceito (uso já correto em 'convergence trade', 'on-the-run', 'smile').
**Motivo (norma, com ressalva):** a nota da regra 4 do guia é explícita — itálico é para título
de obra ou estrangeirismo isolado, nunca aspas. A escolha por aspas em todas as ~13 ocorrências
parece deliberada; mudança de grande superfície, confirmar antes de aplicar em massa.

## Aspas duplas dispersas quebrando o padrão de aspas simples

**Locais:** `### E onde entram as "hipóteses"?`; `"as hipóteses do modelo de
Black–Scholes"`; `cisne negro, outlier, "cinco desvios-padrão", anomalia irracional do
mercado`; `o "cinturão protetor"`; `"esse modelo falhou nessas condições" com "modelar é
inútil"`.
**Sugestão:** trocar todas por aspas simples, por consistência com o resto do texto (regra 4).
**Achado adicional:** na lista "cisne negro, outlier, 'cinco desvios-padrão', anomalia
irracional", só o terceiro item tem aspas — uniformizar (nenhum ou todos).

## "precificar opção era arte de mesa"

**Sugestão:** "precificar **opções** era arte de mesa" — plural genérico é a construção
natural para afirmação categórica (paralelo a "vender ações é arriscado").
**Motivo:** linha.

## Gloss duplicado de "hedge"

Primeira ocorrência: "o hedge (a posição que anula o risco)"; segunda (target forward):
"parecia hedge (proteção) barato" — duas definições parentéticas diferentes para o mesmo
termo podem soar como explicações concorrentes. Considerar remover o segundo parêntese ou
tornar eco explícito. Não é erro de regra (regra 1 exige gloss só na primeira ocorrência).

## Jargão sem marcação de aspas simples/itálico

**Termos:** `circuit breaker`, `hedge`, `payoff`, `spreads`, `backtest` — sem aspas simples,
ao contrário de 'convergence trade', 'on-the-run'/'off-the-run', 'target forward',
'smile'/'skew', já marcados no mesmo texto.
**Sugestão:** aplicar aspas simples na primeira ocorrência de cada um.
**Motivo (norma):** `pesquisa/frente-c-editoracao.md` §3 cita termos do mesmo campo semântico
como candidatos a marcação por não estarem incorporados ao português; inconsistência entre
"termo glossado com aspas" e "sem aspas" é ruído de auditoria (`estilo-autoral.md` §9, item 3).
`delta` e `VaR` ficam como estão (notação matemática e sigla, tratados como CAPM/COE).

## Vírgula picada entre orações independentes (Aracruz/Sadia)

**Original:** "...figuram entre os casos mais citados dessas perdas, a Sadia acabou
incorporada pela Perdigão..."
**Sugestão:** "...figuram entre os casos mais citados dessas perdas; a Sadia, aliás, acabou
incorporada pela Perdigão..."
**Motivo (norma):** vírgula ligando duas orações independentes sem conjunção — pede ponto e
vírgula, ponto ou conjunção.

## Sigla LTCM sem amarração no corpo

O H2 já usa "LTCM", mas o corpo nunca grafa "Long-Term Capital Management (LTCM)" lado a lado.
**Sugestão:** no primeiro parágrafo — "O Long-Term Capital Management (LTCM) foi fundado em
1994 por John Meriwether...".
**Motivo (norma):** sigla usada antes de ser apresentada por extenso — regra 1.

## "CFO" sem gloss

**Sugestão:** "o então CFO (diretor financeiro) do Goldman Sachs..."
**Motivo (norma):** sigla/jargão corporativo sem explicação na primeira ocorrência, mesmo
padrão de "Chief Investment Office", glosado duas linhas depois no próprio texto.

## "a ponta que o LTCM estava vendida"

**Sugestão:** "precisamente a ponta **em que** o LTCM estava **vendido**."
**Motivo (norma):** preposição elidida ("estar vendido numa ponta", não "estar vendido [uma]
ponta") + concordância de gênero (o sujeito é "o LTCM", masculino em todas as outras 6
ocorrências no texto; o particípio correto é "vendido", não "vendida").

## "um modelo calibrado num regime sendo operado"

**Sugestão:** "um modelo calibrado num regime, sendo operado, com alavancagem de mais de 25
para 1, dentro de outro regime."
**Motivo (linha/pontuação):** sem a vírgula, "num regime sendo operado" lê como se fosse o
regime que está sendo operado, quando é o modelo — a oração reduzida de gerúndio precisa de
vírgulas de isolamento.

## "finanças quantitativas é charlatanismo"

**Sugestão:** "finanças quantitativas **são** charlatanismo com LaTeX."
**Motivo (norma, confiança média):** "finanças" é substantivo de forma plural; concordância
prescritiva pede "são" — caso disputado (paralelo a "Estados Unidos é/são"), decisão editorial
válida manter "é" se soar mais natural em registro falado.

## "não dar a quem usa o modelo falso conforto"

**Sugestão:** "não dar, a quem usa o modelo, falso conforto sobre sua precisão..."
**Motivo (linha):** sem vírgulas de isolamento, "o modelo falso conforto" pode ser mal-parseado
em voz alta como substantivo composto.

## "aplicar 25 vezes de alavancagem"

**Sugestão:** "aplicar uma alavancagem de 25 vezes sobre uma premissa histórica..."
**Motivo (linha):** "aplicar X vezes de Y" não é colocação natural em português.

## "Estude estocástico a sério" (baixa prioridade)

**Sugestão opcional:** "Estude cálculo estocástico a sério."
**Motivo (linha):** "estocástico" é adjetivo; "cálculo estocástico"/"processos estocásticos"
são as formas substantivas — mas pode ser elipse deliberada no registro telegráfico da
sequência de imperativos; sinalizado, não obrigatório.

## Achado fora do escopo desta etapa — sinalização para a etapa 7

"Fontes e leituras" cita "Peter Kempthorne et al." como autor/instrutor do curso sem nenhuma
ressalva, mas o `[VERIFICAR: ...]` no corpo do texto (abertura) registra que essa atribuição
"não se sustentou na pesquisa desta rodada" (a página oficial do MIT OCW lista Choongbum Lee,
não Kempthorne, para essa aula específica). A lista de fontes afirma com confiança exatamente
o dado que o corpo trata como não verificado — inconsistência factual entre duas partes do
mesmo documento. Não é problema de linha/norma; a etapa 7 (verificação técnica) deve resolver
as duas pontas juntas: se "Kempthorne" for removido/hedgeado no corpo, a entrada da
bibliografia precisa do mesmo tratamento.

## Resumo de prioridade

**Norma (aplicar sem debate):** regência de "assistir a" na abertura; "a ponta em que o LTCM
estava vendido"; vírgula picada Aracruz/Sadia; sigla LTCM sem amarração; CFO sem gloss;
consistência aspas simples vs. duplas; marcação de jargão sem aspas (circuit breaker/hedge/
payoff/spreads/backtest).

**Norma com ressalva (aplicar com bom senso):** títulos de obra em aspas vs. itálico (grande
superfície — confirmar); concordância "finanças é/são".

**Linha (mais subjetivo):** "precificar opção(ões)"; gloss duplicado de hedge; vírgula em "num
regime, sendo operado"; vírgulas em "não dar, a quem usa o modelo, falso conforto"; "aplicar 25
vezes de alavancagem"; "Estude estocástico" (baixa prioridade).
