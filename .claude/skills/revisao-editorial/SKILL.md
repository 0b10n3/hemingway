---
name: revisao-editorial
description: Passada final de coerência sobre um post já com crítica estrutural, revisão de linha e verificação técnica aplicadas — confere se as três etapas não se contradisseram e se os três entregáveis (post.md, ilustracoes.md, graficos.md) estão consistentes entre si. Use na etapa 9 do pipeline post-substack, ou isoladamente quando pedirem para "dar uma revisão final" num texto já pronto.
disable-model-invocation: true
argument-hint: [caminho-do-slug-em-posts/]
allowed-tools: Read Edit Glob Grep
---

Esta skill roda **depois** das etapas 5 (crítica estrutural), 6 (linha/norma) e 7
(verificação técnica) — ela não refaz o trabalho delas, confere se o resultado combinado
ainda faz sentido como um todo. Editoração em camadas existe justamente para não misturar
essas responsabilidades (ver `pesquisa/frente-c-editoracao.md`); esta skill é o único ponto
que olha as três juntas.

## Checklist de consolidação

1. **Coerência entre etapas.** A crítica estrutural (`05-critica.md`) pediu corte ou
   reordenação que a revisão de linha (`06-revisao.md`) não aplicou? A verificação técnica
   (`07-verificacao.md`) mudou um número que quebra uma frase da revisão de linha? Resolva
   divergências lendo os três arquivos de `processo/` antes de tocar em `post.md`.

2. **Checklist de aderência à voz** (§9 de `estilo/estilo-autoral.md`, via skill
   `voz-syntaxis`) — os dez itens, um a um.

3. **Zero `[VERIFICAR]` sem review humano.** Se `07-verificacao.md` deixou algum item aberto,
   ele deve aparecer no `post.md` como `[VERIFICAR: ...]` visível — nunca silenciosamente
   resolvido a favor de uma suposição.

4. **Placeholders consistentes entre os três entregáveis.** Todo `ilu-NN`/`graf-NN` citado em
   `post.md` tem bloco correspondente em `ilustracoes.md`/`graficos.md`, e vice-versa —
   nenhum placeholder órfão em nenhuma direção.

5. **Antipadrões de IA.** Passe `references` de `voz-syntaxis` (`antipadroes.md`) e, se
   houver tempo, a lista completa em `pesquisa/frente-d-antipadroes-ia-ptbr.md` sobre o texto
   final — a revisão de linha (etapa 6) já deve ter pego a maioria, esta é a rede de segurança.

6. **Frontmatter do `post.md`** — título, subtítulo, data, tags, status — está preenchido e
   coerente com o briefing (`01-briefing.md`)?

## Saída

Aplica as correções diretamente nos três entregáveis (`post.md`, `ilustracoes.md`,
`graficos.md`) e devolve um resumo curto do que mudou desde a etapa 7, para o gate humano
(etapa 10) mostrar ao autor.
