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

## Transcrições de áudio

| Arquivo | Conteúdo | Data | Origem |
|---|---|---|---|
| `transcricoes/2026-08-10_O_Mundo_Invertido_dos_Investimentos.md` | Ideia de post: equívoco de investidores iniciantes que começam por produtos de maior risco (day trade, derivativos) em vez de seguir uma progressão natural (crédito bancário/Tesouro → ETFs de renda fixa → fundos → ações → derivativos). Analogia central: mundo invertido de Stranger Things + preparação para corrida (5km → maratona → ultramaratona) | 2026-08-08 (gravação, conforme título interno `POST_MUNDO_INVERTIDO_20260808`) | Autoral (nota de voz do autor, ditada para orientar o post) |
| `transcricoes/2026-0817_O_Mundo_Invertido_das_Carreiras_em_Financas.md` | Ideia de post: primeiro texto da nova linha editorial "Spoiler" (carreira). Analogia central: mesma ideia do "mundo invertido" do post anterior, agora aplicada à carreira — profissionais que começam pela ponta mais complexa (ex.: precificação de opções, mesa de risco/VaR) sem ter primeiro o domínio de conceitos básicos (dinâmica de juros, dívida pública, mercado de crédito). Exemplo concreto: formação do próprio autor (mestrado em precificação de opções antes de dominar produtos mais simples). Gancho comercial: divulgação do curso gratuito ao vivo no YouTube (setembro) sobre valor do dinheiro no tempo | 2026-08-17 (conforme nome do arquivo) | Autoral (nota de voz do autor, ditada para orientar o post) |
| `transcricoes/2026-08-25_Dividir_para_nao_correr_risco.md` | Draft quase completo (não é nota ditada solta, já vem com subtítulos, referências numeradas, marcadores `[VALIDAR:]` e placeholder `[graf-01]`): o que a LCI (Letra de Crédito Imobiliário) realmente é — dívida comum do banco emissor, lastreada em crédito imobiliário mas sem segregação patrimonial, versus CRI (securitização, sem FGC) e LIG (patrimônio de afetação, duplo recurso). Tese: "dividir para não correr risco" não é força de expressão — é a estrutura descrevendo onde o risco fica (risco de crédito do banco emissor, mitigado até o teto do FGC). Gancho: liquidação extrajudicial do Banco Master (nov/2025) e o desembolso do FGC (~R$ 44 bi). Fecha com CTA para o próximo texto da série (CRI) | 2026-08-25 (conforme nome do arquivo) | Autoral (nota de voz do autor, ditada para orientar o post) |

**Nota de 2026-09-13 (refatoração do pipeline v2):** esta pasta foi renomeada para
`drafts/` — os arquivos acima (e mais um não catalogado individualmente nesta tabela:
`2026-08-14_O Papel do CDB na Transformação de Prazos.md`) foram movidos com `git mv` para
`drafts/`, preservando histórico. O insumo do pipeline deixou de ser transcrição de áudio e
passou a ser rascunho pré-estruturado pelo autor — ver `CLAUDE.md`. Nenhum conteúdo destes
arquivos foi alterado, só a pasta que os contém. Um sexto arquivo
(`2026-09-11_O Díficil...md`) existe na branch de um post ainda não publicado
(`post/2026-09-11-partes-dificeis-de-uma-carreira-em-financas`) e será migrado quando essa
branch chegar a `main`.

## Documentos de contexto

| Arquivo | Conteúdo | Uso |
|---|---|---|
| `MARKETING_REVIEW.md` | Marketing Review — Syntaxis Educação: personas, proposta de valor, funil, canais, roadmap | Fonte de `PUBLICO` e de objetivos comerciais por tipo de texto (etapa 1 do pipeline, "Briefing") |

## Design tokens (fora de `_arquivo/`, referenciado aqui por completude)

`marca/tokens.json` — sistema de design "O Sinal no Escuro" (v2.1), já existente, reutilizado
por `marca-syntaxis` e pelo código Plotly de `graficos.md`. Não é um original de leitura —
é um artefato de sistema, por isso vive fora de `_arquivo/` e pode evoluir.

## Posts publicados — captura do site (desde 2026-11-15)

| Pasta | Conteúdo | Origem | Datas | Licença |
|---|---|---|---|---|
| `publicados/` | JSON bruto de cada post publicado na Syntaxis (31 na primeira captura: 15 anteriores ao pipeline e 16 da era pipeline), um arquivo por post: `AAAA-MM-DD_<slug-do-site>.json` (data = `post_date`). Recaptura de post alterado no site entra como arquivo novo `AAAA-MM-DD_<slug>__cap-<data-da-captura>.json`, nunca sobrescreve | API pública do Substack (`/api/v1/archive` e `/api/v1/posts/<slug>`), sem autenticação, via `scripts/corpus_publicado.py` | posts de 2024-09-06 a 2026-11-15; primeira captura em 2026-11-15 | Autoral (Silvano A. A. P. Junior) |

O campo `comments` da API é removido antes de gravar: traz nome, handle e foto de leitores, não
serve ao estudo de estilo e este repositório é público. Fora isso, o JSON é o que a API devolveu.
A lista item a item (post, slug no repositório, rascunho correspondente, captura vigente) mora em
`estilo/corpus/mapa-publicados.json`, gerado pelo mesmo script — não é repetida aqui.

**Nota de 2026-11-15 sobre as amostras próprias de Substack (acima):** as datas de publicação que
faltavam constam agora do mapa (campo `post_date` das entradas que têm `amostra_v1`). A comparação
com a captura do site mostrou que
os seis arquivos de `amostras/proprias/substack/` perderam formatação na conversão original: o
negrito do site sumiu e as aspas duplas curvas (“…”) viraram aspas simples retas ('…'). Os
arquivos continuam intocados; a evidência está em `pesquisa/epico-revisao-editorial/00-corpus.md`.
