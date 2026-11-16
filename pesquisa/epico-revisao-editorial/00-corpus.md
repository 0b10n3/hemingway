# Fase A — Corpus publicado e triplas de edição

2026-11-15. Branch `epico/revisao-editorial-2026-11`, base `main` em `22d3dc8`.
Prompt do épico: `../../PROMPT_CLAUDE_CODE_EPICO_HEMINGWAY_2026-11.md` (na raiz `Syntaxis/`).

Scripts desta fase (stdlib pura, nenhuma dependência nova):

| Script | O que faz | Teste |
|---|---|---|
| `scripts/corpus_publicado.py` | captura o site em `_arquivo/publicados/` e gera `estilo/corpus/publicados/*.md` e o mapa `estilo/corpus/mapa-publicados.json` | `scripts/test_corpus_publicado.py` (8 fixtures + checagem de volume) |
| `scripts/diff_edicoes.py` | alinha rascunho → `post.md` → publicado e grava `estilo/corpus/edicoes/<slug>.json` e `_resumo.json` | `scripts/test_diff_edicoes.py` (7 casos) |

`python3 -m unittest discover -s scripts -p 'test_*.py'`: 43 testes, todos passam (inclui os do
parecer, que não foram tocados).

---

## 1. Cobertura

- **31 posts capturados, 0 falhas.** São 15 anteriores ao pipeline (de 2024-09-06 a 2026-03-02) e 16 da era
  pipeline (de 2026-08-10 a 2026-11-15). Todos são `audience: everyone`. Ocupam 1,1 MB em `_arquivo/publicados/`.
  A segunda execução de `capturar` gravou 0 arquivos ("31 sem mudança"), então a captura é idempotente.
- **Fidelidade do parser.** As palavras do `.md` normalizado batem com o `wordcount` da API, com desvio
  máximo de 2,0% e médio de 0,5% (tolerância de 3%). O Substack conta legenda de imagem, legenda de CTA e
  código, e a checagem faz o mesmo. Componentes convertidos: parágrafo, H2–H4, negrito, itálico,
  riscado, link, lista, citação, separador, imagem com legenda, LaTeX (`persistentExpression`),
  CTA com e sem legenda, pullquote, bloco de código, vídeo e enquete. Nenhuma classe de `div` ficou sem
  tratamento.
- **Privacidade.** O campo `comments` sai antes de gravar, porque traz nome, handle e foto de leitores
  e o repositório é público. Isso está registrado em `_arquivo/MANIFESTO.md`.
- **Mapa: 16 de 16 posts do repositório pareados.**
  - 14 foram pareados por `url_publicada`.
  - 2 foram inferidos por data e slug, e conferi os dois: `2026-11-09-frequencia-de-capitalizacao` →
    `/p/frequencia-de-capitalizacao` e `2026-11-13-should-i-stay` → `/p/should-i-stay-or-should-i-go`.
  - Os 16 rascunhos de `_arquivo/drafts/` foram pareados pela data do nome do arquivo.
  - As 6 amostras do guia v1 foram reconhecidas no site (campo `amostra_v1`).
- **Três rascunhos são transcrição de áudio, não texto do autor:** 08-10, 08-14 e 08-17. Neles quase
  todo o `post.md` foi escrito pelo pipeline, então o sinal de reversão é fraco. O laudo os separa
  sempre que isso muda a leitura.
- **Três posts têm como base uma versão histórica do `post.md`, e não a atual.** O autor parte da versão
  que existia quando publicou. Por isso o script procura no histórico do git a versão mais próxima do
  publicado:

  | Post | Commit base | Similaridade com o site (base / atual) | Por quê |
  |---|---|---|---|
  | 09-01 quando-os-modelos | `4a8a1ee` (etapa 9, 31/08) | 0,938 / 0,790 | A rodada 4 (02/09) apagou e regerou o conteúdo **depois** da publicação (01/09) |
  | 10-30 du252 | `1839193` (09/11) | 0,973 / 0,967 | Em 09/11 o repositório cortou do `post.md` a promessa do FIDC; o site não mudou |
  | 11-02 barriga-da-curva | `00dcfe0` (05/11) | 0,988 / 0,979 | Mesma correção do FIDC em 09/11, só no repositório |

  Sem essa correção, 09-01 apareceria com 221 "edições do autor" em vez de 62.

## 2. Similaridade por post

Similaridade é a razão do `difflib` sobre a sequência de palavras: 1,0 quer dizer texto idêntico.
Ela não enxerga formatação nem quebra de parágrafo, que estão nas operações da Seção 3.

| Post | Linha | Rascunho | rascunho→post.md | post.md→site | rascunho→site | Operações | Reversões | Acréscimos |
|---|---|---|---|---|---|---|---|---|
| 08-10 o-mundo-invertido-dos-investimentos | — | transcrição | 0,164 | 0,977 | 0,164 | 20 | 5 | 2 |
| 08-14 o-papel-do-cdb | Notas | transcrição | 0,279 | 0,847 | 0,255 | 109 | 27 | 17 |
| 08-17 o-mundo-invertido-das-carreiras | Spoiler | transcrição | 0,152 | 0,847 | 0,152 | 72 | 28 | 30 |
| 08-25 dividir-para-nao-correr-risco | Notas | rascunho | 0,892 | 0,950 | 0,860 | 89 | 3 | 6 |
| 09-01 quando-os-modelos-se-rebelam | Spoiler | rascunho | 0,859 | 0,938 | 0,833 | 62 | 7 | 3 |
| 09-11 partes-dificeis | Spoiler | rascunho | 0,899 | 0,941 | 0,836 | 95 | 4 | 14 |
| 09-18 o-agro-e-pop | Notas | rascunho | 0,678 | 0,936 | 0,676 | 64 | 8 | 3 |
| 09-24 borboletas-caos-e-carreira | Spoiler | rascunho | 0,921 | 0,994 | 0,920 | 13 | 2 | 1 |
| 09-28 o-certificado-nao-muda-o-devedor | Notas | rascunho | 0,842 | 0,954 | 0,801 | 71 | 7 | 10 |
| 10-12 coqueiros-e-cacaueiros | Spoiler | rascunho | 0,867 | 0,992 | 0,867 | 37 | 9 | 3 |
| 10-15 renda-fixa-condicoes-variaveis | Notas | rascunho | 0,782 | 0,978 | 0,769 | 56 | 4 | 4 |
| 10-27 samurais-e-duelos | Spoiler | rascunho | 0,826 | 0,956 | 0,811 | 72 | 4 | 12 |
| 10-30 du252-contagem-de-dias | Notas | rascunho | 0,776 | 0,973 | 0,758 | 67 | 4 | 6 |
| 11-02 a-barriga-da-curva | Notas | rascunho | 0,470 | 0,988 | 0,471 | 21 | 10 | 8 |
| 11-09 frequencia-de-capitalizacao | Notas | rascunho | 0,751 | 0,992 | 0,750 | 30 | 4 | 11 |
| 11-13 should-i-stay | Spoiler | rascunho | 0,724 | 0,972 | 0,713 | 55 | 7 | 6 |

Leitura:
- Nos 13 rascunhos de verdade, o pipeline muda em mediana 17% das palavras do rascunho
  (rascunho→post.md = 0,826).
- Depois, o autor muda em mediana 4% das palavras do `post.md` (post.md→site = 0,964 nos 16 posts).
- A edição do autor é pequena em volume, mas é **sistemática em forma**: parágrafo, negrito,
  travessão, aspas e título. É isso que a próxima seção mostra.

Dois casos fora da curva:
- **11-02 (0,470).** O pipeline reescreveu mais da metade do rascunho. O commit `00dcfe0` diz "rodada
  pós-gate sobre a versão do autor (A Corda e o Arco)", então o autor reescreveu o texto durante o
  gate, e o rascunho de `_arquivo/` deixou de ser o ponto de partida. Fica para a B1.
- **08-14 e 08-17 (0,847).** São os dois maiores desvios post.md→site. Os dois partem de transcrição.

## 3. Distribuição das operações (post.md → site)

São 923 operações nos 16 posts. Cada uma está em `estilo/corpus/edicoes/<slug>.json`, com o contexto.

| Classe | Ocorrências | Posts | Natureza atribuída |
|---|---|---|---|
| tipografia (aspas retas → curvas) | 291 | 16 | layout-substack (o editor converte; não se aprende estilo disso) |
| divisão de parágrafo | 174 | 16 | estilo |
| pontuação | 158 | 14 | estilo |
| negrito adicionado | 128 | 14 | estilo |
| substituição de palavra/frase | 117 | 16 | estilo (108), conteúdo/fato, ambíguo |
| remoção | 98 | 16 | estilo (63), conteúdo/fato (33), ambíguo (2) |
| itálico adicionado | 60 | 12 | estilo |
| legenda (alt-text do pipeline × legenda do site) | 29 | 15 | layout-substack (28) |
| inserção | 27 | 9 | estilo, conteúdo/fato, ambíguo |
| subtítulo H2 | 26 | 12 | estilo |
| separador / imagem | 23 / 23 | 7 / 14 | layout-substack |
| subtítulo do post / título do post | 8 / 4 | 8 / 4 | ambíguo |
| CTA / link adicionado | 8 / 5 | 5 / 5 | marketing |
| tabela (o Substack não tem tabela nativa) | 6 | 2 | layout-substack |
| fusão de parágrafo | 5 | 1 | estilo |
| itálico removido, código, fórmula | 3, 3, 2 | — | estilo, conteúdo, ambíguo |

- **Por natureza:** estilo 748, layout-substack 96, conteúdo/fato 45, ambíguo 21, marketing 13.
- **Sinais:**
  - 132 reversões e 136 acréscimos autorais, estes com 842 palavras.
  - Nos rascunhos de verdade: 73 reversões e 87 acréscimos. Nas transcrições: 59 e 49.
  - As reversões se concentram em substituição (57), remoção (44) e negrito (13).
  - O sinal é conservador: quando não há âncora confiável no rascunho, ele fica vazio em vez de chutar.

## 4. As dez edições mais recorrentes

**1. O autor divide parágrafos.** São 174 divisões, em 16 de 16 posts.
- 114 são divisões novas, porque o próprio rascunho tinha aquele trecho junto. Só 4 restauram o rascunho, e 56 não têm âncora.
- O pipeline entrega 45,7 palavras por parágrafo, com 34% de parágrafos de uma frase. O site fica
  com 35,0 palavras e 47%. Os posts pré-pipeline têm 37,3 palavras e 40%.
- Exemplos:
  - 11-13: "A gravação aconteceu no meio de uma crise. ¶ A banda tinha acabado de trocar de empresário…"
  - 11-13: "O chefe é difícil. ¶ O time é frio. ¶ A segunda-feira pesa."

**2. O autor acrescenta negrito.** São 128 trechos, em 14 posts. Somando os 16 posts, há 3 negritos no `post.md` e 144 no site.
- 13 deles devolvem um negrito que estava no rascunho e que o pipeline tirou.
- O negrito cai em três tipos de lugar:
  - nome e obra: "Cal Newport", "Steven Levitt", "Freakonomics";
  - definição: "Certificado de Depósito Bancário", "sem FGC";
  - frase-tese: "olhe a derivada, não o nível" (que estava em negrito no rascunho) e "O problema é a que nunca fica barata."

**3. O autor corta travessões.** O `post.md` tem 236 travessões, e o site 127, um corte de 46%.
- Nas operações diretas, 24 viram vírgula, 11 somem e 2 viram dois-pontos. Em 4 subtítulos, a continuação depois do travessão some.
- Exemplos:
  - 08-14: "captar recursos — via CDB" → "captar recursos, via CDB"
  - 08-25 (subtítulo): "Não é favor, é 'spread' — e o risco que sobra…" → "Não é favor, é spread. E o risco que sobra…"
- Nos posts pré-pipeline o travessão é raro: de 0 a 11 por post.

**4. O autor troca aspas simples por itálico, ou por nada.** Os termos entre aspas simples caem de 113 para 61, e 93 aspas simples somem, em 7 posts.
- O estrangeirismo vira itálico: são 60 itálicos novos, em 12 posts.
- Exemplos: 'spread' → *spread* (08-14); *Liquidity Coverage Ratio*, *gross-up*, *core*, *Value at Risk*.

**5. Substituições curtas.** São 117, em 16 posts, e 57 delas desfazem texto do pipeline. Na maior parte, a troca é idiossincrática: nenhum par antes→depois se repete.
- Hipótese fraca, para a Fase B: em 7 casos, de 5 posts, o autor acrescenta modalização ("Está" → "Mas pode estar"; "usa" → "pode usar"; "é" → "pode ser"; "separo" → "busco separar"). O movimento contrário aparece em 3 casos.
- Ainda não há evidência para regra.

**6. O autor corta texto.** São 98 remoções, em 16 posts, e 44 são reversões de texto do pipeline. As maiores:
- 11-13: corte de 99 palavras de um levantamento da NFL que o pipeline trouxe da pesquisa;
- 09-18: corte de 60 palavras sobre a taxa média da LCA (Quantum/InfoMoney);
- notas de rigor e parênteses explicativos.

Além disso, **7 `[VERIFICAR]` e 1 `[PREENCHER]` foram apagados no site em vez de resolvidos.** O caso
de 10-30 é "[PREENCHER: memória do autor…]", que chegou ao `post.md` final.

**7. O autor mexe nos subtítulos H2.** São 26 trocas, em 12 posts.
- Ele tira o rótulo "Fechamento:" que o pipeline põe em H2, em 3 posts (09-28, 10-15, 11-02).
- Também encurta subtítulos ("Clima é uma coisa. Capital é outra." → "… Capital de Carreira é outra.").

**8. O autor troca título e subtítulo.** Foram 4 títulos e 8 subtítulos, todos ficando mais curtos.
- "Você está contando os dias úteis errado (e isso está custando dinheiro)" → "Você está contando os dias errado".
- "O Certificado Não Muda o Devedor" → "A anatomia e o verdadeiro risco do CRA".

**9. Imagens e legendas.**
- O site tem 23 imagens que o `post.md` não tem, em 14 posts. São capa e ilustração, que saíram do pipeline.
- 28 dos alt-texts descritivos do pipeline não viram legenda no site.
- **Nenhuma das 60 imagens dos posts de 2026 tem alt-text no site.** O alt-text que a etapa 8 escreve nunca chega à publicação.

**10. Os acréscimos longos do autor são quase todos fora do estilo:**
- aviso legal ("Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões…"), em 3 posts;
- botão de compartilhar ou assinar: 8 CTAs, em 5 posts;
- links: 5;
- fechos de série ("Na próxima semana, voltamos para falar sobre…").

## 5. Adiantamento para a B4: a regra 4 do guia v1 nasceu de um artefato de conversão

A regra 4 diz: "nunca usa negrito ou itálico de ênfase; aspas simples fazem esse trabalho". Ela
saiu das 6 amostras em `_arquivo/amostras/proprias/substack/`. Comparei cada uma com a captura do site:

| Post | Negrito na amostra | Negrito no site | Aspas na amostra | Aspas no site |
|---|---|---|---|---|
| titulos-do-tesouro-nacional | 0 | 23 | 2 simples retas | duplas curvas |
| eu-preciso-de-um-assessor | 0 | 7 | 2 simples retas | duplas curvas |
| tesouro-selic | 0 | 12 | 0 | — |
| o-simples-funciona | 0 | 6 | 20 simples retas | 10 duplas curvas |
| objetivos-and-classes | 0 | 0 | 18 simples retas | 8 duplas curvas |
| a-ciencia-da-separacao | 0 | 14 | 22 simples retas | 11 duplas curvas |

O exemplo que o próprio guia usa para justificar a regra (✅ `'internamente homogêneo'`) está no site
como **“internamente homogêneo”**, com aspas duplas curvas. A conversão que gerou as amostras apagou
o negrito e trocou “…” por '…'.

Nos 15 posts pré-pipeline do site, 14 usam negrito. Desde agosto, o pipeline aplica a regra 4 em todo
post: tira o negrito, inclusive o que o autor pôs no rascunho, e põe aspas simples. Depois o autor
desfaz isso no Substack. É a maior fonte individual de retrabalho que este levantamento achou. A
decisão sobre a regra é sua e entra na Fase D, mas a evidência já está aqui.

## 6. Achados no site que pedem ação sua (fora do épico)

1. **Dois `[VERIFICAR]` estão no ar:**
   - *A Corda e o Arco* (`/p/a-corda-e-o-arco`): "[VERIFICAR: convenção da taxa over mensal como taxa por dia útil × 30, antes de 1998…]".
   - *Frequência de Capitalização*: na bibliografia, "Eli Maor, *e: A História de um Número* (Record) [VERIFICAR: ano da edição]".
2. ***Você está contando os dias errado* (10-30) ainda promete o próximo texto sobre FIDC**, que foi
   cancelado. A frase foi cortada do repositório em 09/11 (commit `cfd92a9`), mas o site não foi atualizado.
3. **Erros de digitação no site, todos conferidos no texto:**
   - "Ficarprocrastinando" e "conteto histórico" (09-11);
   - "crédito rura." (09-18);
   - "O coqueiro o símbolo do que é nativo" (10-12; o `post.md` diz "O coqueiro seria o símbolo");
   - "um calculo importante" (10-15);
   - "o juro simples ganha do compost" (11-02);
   - "## No munda das opções" (11-09).

   A heurística do script também apontou `Antifrágil`, `ilha`, `evidências` e `separam`, que conferi e são falsos positivos.
4. **Parágrafo com só "." em *Should I stay or should I go***, logo depois de "…para quem tem margem para escolher".

## 7. Limites do método

- A **natureza** de cada operação é heurística:
  - número → conteúdo/fato;
  - mais de 40 palavras → ambíguo;
  - link → marketing.

  Ela serve para não aprender estilo com edição de fato, mas não substitui o seu julgamento nos casos ambíguos.
- O alinhamento global pode fragmentar uma reescrita longa em várias substituições (aconteceu em 09-01
  antes da correção da base). Os H2 reescritos às vezes aparecem partidos no JSON.
- Há uma captura só por post. Uma edição feita no site depois da publicação não se distingue de
  uma feita antes. O `updated_at` mostra que 3 dos 16 posts da era pipeline (08-10, 09-11 e 10-27)
  e 4 dos 15 anteriores foram editados depois do dia da publicação.
- A similaridade por palavra ignora formatação. As métricas de forma (parágrafo, negrito, travessão)
  foram contadas à parte e vão para a B3 com o script de métricas estendido.

## 8. Perguntas para o GATE A

1. **Negrito e aspas (regra 4).** Pela Seção 5, você usa negrito e aspas duplas curvas desde 2024, e a
   regra "nunca negrito, aspas simples" veio da conversão das amostras. Confirma? Se sim, a Fase D
   revoga a regra 4 (o que faz o guia ir para v2.0.0, versão major) e a substitui pelo padrão medido aqui: negrito em nome, obra,
   definição e frase-tese; itálico em estrangeirismo; aspas duplas para citação e termo.
2. **Casos ambíguos.** Classifique cada um como estilo, conteúdo, marketing ou ignorar:
   - os 4 títulos e 8 subtítulos trocados: estilo de manchete ou decisão de marketing?
   - o aviso legal inserido em 09-11, 10-15 e 10-27: proponho tratar como "fora do estilo" e, se você quiser, virar item fixo da etapa 9a;
   - 08-17: o parágrafo de 111 palavras acrescentado ("Eu sabia explicar o modelo inteiro…") e o CTA reescrito ("…[Valor do Dinheiro no Tempo]…" → "Youtube!");
   - 10-30: as duas fórmulas acrescentadas no site ($$ Fator = (1+i)^τ $$ e $$ Fator = 1 + i × τ $$) e a "Nota de rigor" cortada.
3. **`url_publicada` de 11-09 e 11-13.** Posso preencher o campo nos dois `post.md`?
   Os valores são `https://syntaxis.substack.com/p/frequencia-de-capitalizacao` e
   `https://syntaxis.substack.com/p/should-i-stay-or-should-i-go`.
4. **Commit.** Aprovada a fase, faço os commits na branch do épico, um por item: os scripts e os testes, a captura com o acréscimo
   ao `MANIFESTO.md`, o corpus normalizado com as edições, e este laudo.

## 9. Decisões do GATE A (2026-11-15)

1. **Regra 4: revogar e medir.** A Fase D revoga a regra 4, e o guia vai para v2.0.0. O substituto é o
   padrão medido: negrito em nome, obra, definição e frase-tese; itálico em estrangeirismo; aspas duplas
   para citação e termo.
2. **Casos ambíguos: proposta aceita.**
   - Título e subtítulo contam como estilo de manchete e entram no aprendizado.
   - O aviso legal ganha natureza própria (`aviso-legal`), fora do estilo, e é candidato a item fixo na Fase C.
   - O parágrafo de 08-17, as fórmulas e a nota de rigor de 10-30, e o `[PREENCHER]` cortado contam como conteúdo.
   - O CTA reescrito em 08-17 conta como marketing.
   - O "." de 11-13 é deslize do editor (`layout-substack`).

   Onde ficou registrado:
   - as regras gerais estão em `scripts/diff_edicoes.py`;
   - os 5 casos pontuais estão em `estilo/corpus/natureza-decidida.json`, que o script lê a cada execução.

   Natureza depois da decisão: estilo 757, layout-substack 97, conteúdo/fato 50, marketing 14,
   aviso-legal 5, ambíguo 0.
3. **`url_publicada` preenchida em 11-09 e 11-13**, só essas duas linhas. O mapa agora pareia os 16
   posts por `url_publicada`. O catálogo de marketing (`marketing/catalogo.json`) não foi regerado aqui;
   a etapa 9a faz isso no próximo post.
4. **Fase A aprovada para commit.** Sigo para a Fase B.
