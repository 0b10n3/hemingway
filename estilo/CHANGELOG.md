# Changelog — guia de voz Syntaxis

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
