# Manifesto de origem — `_arquivo/`

Este arquivo documenta origem, data e licença de cada item em `_arquivo/`. `_arquivo/` é
imutável: nada aqui é editado, renomeado ou apagado por nenhuma etapa do sistema. Ver
`CLAUDE.md` §"Regras invioláveis".

## Amostras próprias — voz atual

| Arquivo | Gênero | Origem | Data | Licença |
|---|---|---|---|---|
| `amostras/proprias/substack/syntaxis_a_ciência_da_separação.md` | Substack | Post publicado, Syntaxis | não informada | Autoral (Silvano A. A. P. Junior) |
| `amostras/proprias/substack/syntaxis_eu_preciso_de_um_assessor_de_investimentos.md` | Substack | Post publicado, Syntaxis | não informada | Autoral |
| `amostras/proprias/substack/syntaxis_objetivos_classes.md` | Substack | Post publicado, Syntaxis | não informada | Autoral |
| `amostras/proprias/substack/syntaxis_o_simples_funciona.md` | Substack | Post publicado, Syntaxis | não informada | Autoral |
| `amostras/proprias/substack/syntaxis_tesouro_selic.md` | Substack | Post publicado, Syntaxis | não informada | Autoral |
| `amostras/proprias/substack/syntaxis_títulos_do_tesouro_nacional.md` | Substack | Post publicado, Syntaxis | não informada | Autoral |
| `amostras/proprias/dissertacao/disser3.0.pdf` | Dissertação | "Teorema de Decomposição de Lévy-Itô", dissertação de mestrado em Matemática, PPGMAT/UFES. Orientador: Fabio Julio da Silva Valentim. Autor: Silvano Antonio A. P. Junior | 2014-11-07 (CreationDate do PDF) | Autoral |

Datas de publicação dos posts de Substack não constavam nos arquivos fornecidos — se
precisar delas para o `corpus-manifest.json` ou para o guia de voz, confirme com o autor.

## Amostras admiradas — camada aspiracional

**Nota de copyright (decisão do usuário, Fase 0, 2026-08-09):** como `REPO_PRIVADO = não`,
o texto integral destes artigos **não é commitado** — fica local, listado em `.gitignore`
(`_arquivo/amostras/admiradas/**/*.md`). O que entra no git é só a extração estilométrica
(`estilo/extracoes/admiradas/*.json`, com evidências de até 25 palavras) e este manifesto.
Quem clonar o repositório do zero **não terá as amostras admiradas em disco** — só o
resultado já processado. Para reprocessar, é preciso obter os artigos de novo nas fontes
abaixo.

| Arquivo local (gitignored) | Autor | Título | Fonte | Data |
|---|---|---|---|---|
| `amostras/admiradas/michael-lewis/Faking It Share full article.md` | Michael Lewis | "Faking It" | The New York Times Magazine | 2001-07-15 |
| `amostras/admiradas/michael-lewis/Future Nerd Getting small.md` | Michael Lewis | "Future Nerd — Getting small, very, very small, with Xerox's Ralph Merkle" | Slate | 1998-05-28 |
| `amostras/admiradas/michael-lewis/The Trading Desk Share.md` | Michael Lewis | "The Trading Desk" | The New York Times Magazine | 2003-03-30 |
| `amostras/admiradas/ernest-hemingway/soldiers-home.md` | Ernest Hemingway | "Soldier's Home" (*In Our Time*, Boni & Liveright) | 1925 — domínio público nos EUA | Wikisource |
| `amostras/admiradas/ernest-hemingway/the-battler.md` | Ernest Hemingway | "The Battler" (*In Our Time*, Boni & Liveright) | 1925 — domínio público nos EUA | Wikisource |
| `amostras/admiradas/ernest-hemingway/big-two-hearted-river.md` | Ernest Hemingway | "Big Two-Hearted River" (Partes I e II, *In Our Time*, Boni & Liveright) | 1925 — domínio público nos EUA | Wikisource |
| `amostras/admiradas/malcolm-gladwell/the-ketchup-conundrum.md` | Malcolm Gladwell | "The Ketchup Conundrum" | 2004-09-06, The New Yorker | gladwell.com via Wayback Machine (snapshot 2017; página original hoje devolve 404) |
| `amostras/admiradas/malcolm-gladwell/something-borrowed.md` | Malcolm Gladwell | "Something Borrowed" | 2004-11-22, The New Yorker | gladwell.com via Wayback Machine (snapshot 2017; página original hoje devolve 404) |

Recuperados por pesquisa dirigida em 2026-08-09. Hemingway priorizado por estar genuinamente
em domínio público nos EUA (publicado antes de 1930); Gladwell recuperado de snapshots do
Wayback Machine porque o site atual não mantém mais as páginas de arquivo com o texto
integral (links de spam injetados no HTML arquivado foram removidos antes de salvar).

## Documentos de contexto

| Arquivo | Conteúdo | Uso |
|---|---|---|
| `MARKETING_REVIEW.md` | Marketing Review — Syntaxis Educação: personas, proposta de valor, funil, canais, roadmap | Fonte de `PUBLICO` e de objetivos comerciais por tipo de texto (etapa 1 do pipeline, "Briefing") |

## Design tokens (fora de `_arquivo/`, referenciado aqui por completude)

`marca/tokens.json` — sistema de design "O Sinal no Escuro" (v2.1), já existente, reutilizado
por `marca-syntaxis` e pelo código Plotly de `graficos.md`. Não é um original de leitura —
é um artefato de sistema, por isso vive fora de `_arquivo/` e pode evoluir.
