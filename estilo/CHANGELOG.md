# Changelog — guia de voz Syntaxis

## v2.0.0 — 2026-11-16

Atualização pelo modo `atualizar` da forja, com o corpus publicado (épico de revisão editorial,
`pesquisa/epico-revisao-editorial/`). **Major**: revoga regras da v1.

**Corpus:** de 7 textos (6 posts convertidos + dissertação) para 32: os 31 posts publicados,
capturados do site, mais a dissertação. 55.400 palavras publicadas. As edições do autor entre o
`post.md` e o site (923 operações em 16 posts) entram como evidência.

**Por que major:** as 6 amostras da v1 tinham perdido o negrito e trocado aspas duplas curvas por
simples retas na conversão. A regra 4 ("nunca negrito; aspas simples") descrevia o artefato, não o
autor, e o pipeline a aplicou como norma obrigatória desde agosto.

| v1 | v2 | Evidência |
|---|---|---|
| Regra 4: nunca negrito/itálico; aspas simples | **Revogada.** Nova regra 4: ênfase com função (negrito em frase-tese, termo-chave, nome/obra; itálico em estrangeirismo; aspas curvas com função) | negrito em 27/31 posts; autor acrescenta 128 negritos |
| Regra 7: aposto "frequentemente com travessão duplo" | Regra 3: parêntese é o padrão; travessão raro (≤~3/mil), nunca em título | zero em 8/16; autor corta 46% |
| Regra 9: visual com referência verbal | **Revogada no guia.** Legenda e alt-text são regra do pipeline; anúncio da figura por dois-pontos vai para §8 | referência verbal ~0 em todos os estratos |
| §7.1: nunca tabela ou gráfico nativo | Sai do guia (restrição da plataforma) | Substack não tem tabela |
| §4: duas vozes | Três vozes: ensaística, **ensaística em registro técnico** (nova; desde jan/2026), explicativa (em desuso desde set/2026) | 8 / 6 / 2 posts da era pipeline |
| §4.1: humor constante; metáfora raramente retomada | Humor seco ocasional nas três vozes; fecho em anel (regra 10) | 14/16; 15/16 |
| §5 movimentos 1 e 8 (aspiracionais) | Viram regras descritivas 7 e 9 | 14/16; 16/16 |
| §5 movimento 2 (aside com travessão) | Sai | contraria a regra 3 |
| §8 reticências | Sai (em queda: 0,34 → 0,07 por mil) | — |
| §8 analogia matemática | Promovida (§4.1) | 4 posts pipeline + 4 anteriores |
| — | Novas regras 1, 5 (parte), 6, 10, 11, 12, 15, 16, 17, 18, 19, 20 | ver §3 |

**Linha de base:** 14 dos 15 posts anteriores têm tiques de IA marcados; entram com recorte (§10).

**Teste cego (§7.7 do protocolo), analítico, em dois posts:**
- *should-i-stay-or-should-i-go* (ensaística): o guia prevê a abertura na cena do Clash (regra 7), o
  parágrafo curto (1), o zero travessão (3), o negrito em nome e frase-tese (4), a volta a Mick Jones
  no fecho (10), a 1ª pessoa de mentor e o pedido de resposta pessoal (§4.1). Reconhecível.
- *frequencia-de-capitalizacao* (registro técnico): prevê a cena de Bernoulli, o refrão "O contínuo
  não compete com o composto. É o limite dele." na abertura e no fecho, as fórmulas anunciadas por
  dois-pontos e o fecho "Se o texto funcionou…" (§4.2). Reconhecível.
- Três pontos mais frágeis: (1) negrito varia de zero a ~8 por mil, então a regra não pode ser cota
  (corrigido: "sem cota"); (2) o teto da antítese (regra 20) é estimativa, não medida; (3) a fronteira
  entre registro técnico e explicativa: os extratores divergiram em a-corda-e-o-arco e
  voce-esta-contando-os-dias-errado. O critério de §4 (tese em refrão + fecho em anel = técnico) é o
  desempate.

**Aprovado por:** autor, 2026-11-16, no GATE da onda 1 do épico, regra por regra: as quatro
revogações e reformulações, todas as regras novas, a regra 20 como voz com teto, e a linha de base
com recorte (§10) com confiança alta para forma e média para léxico e postura.

## v1.0.0 — 2026-08-10

Primeira versão do guia, gerada em bootstrap (Fase 2 do meta-prompt).

**Corpus:** 6 posts de Substack (6.742 palavras) + 1 dissertação de mestrado em Matemática
(18.943 palavras lidas / 10.735 na extração via pdftotext) como amostras próprias; 3 textos
de Michael Lewis, 3 contos de Ernest Hemingway e 2 textos de Malcolm Gladwell como camada
aspiracional. Ver `estilo/corpus-manifest.json`.

**Achado central:** os posts de Substack não formam uma voz única — dividem-se em subgênero
*ensaístico* (pessoal, irônico, com CTA) e *explicativo* (impessoal, categórico, sem CTA).
Ver §4 do guia.

**Limitações declaradas:**
- Corpus abaixo do piso de ~8 textos / ~10.000 palavras próprias recomendado pela pesquisa
  de estilometria (`pesquisa/frente-b-estilometria.md`) para confiança alta — por isso
  `confianca_global: media`.
- Nenhuma amostra de LinkedIn disponível; `_arquivo/amostras/proprias/linkedin/` está vazio.
- Regras marcadas `[cross-gênero]` (confirmadas em Substack E dissertação) têm confiança
  mais alta que as demais, por sobreviverem à maior distância de gênero do corpus.

**Aprovado por:** aguardando aprovação do autor (§7.7 do meta-prompt) antes da tag `voz-v1.0.0`.
