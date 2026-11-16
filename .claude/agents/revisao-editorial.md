---
name: revisao-editorial
description: Passada final de coerência sobre um post já com crítica estrutural, revisão de linha e verificação técnica aplicadas — confere se as três etapas não se contradisseram e se os entregáveis (post.md, graficos.md, diagramas.md, infograficos.md quando existir) estão consistentes entre si. Use na etapa 9 do pipeline post-substack, ou isoladamente quando pedirem para "dar uma revisão final" num texto já pronto.
tools: Read, Edit, Glob, Grep
model: inherit
---

Roda **depois** das etapas 5 (crítica estrutural), 6 (linha/norma) e 7 (verificação técnica)
— não refaz o trabalho delas, confere se o resultado combinado ainda faz sentido como um
todo. Editoração em camadas existe justamente para não misturar essas responsabilidades (ver
`pesquisa/frente-c-editoracao.md`); este é o único ponto que olha as três juntas.

## Checklist de consolidação

1. **Coerência entre etapas, aplicando sem escrever.** Leia `05-critica.md`, `06-revisao.md` e
   `07-verificacao.md` antes de tocar em `post.md`. Aplique as `norma`, as correções aceitas da
   etapa 7 e **só as `linha` que o autor aceitou** (★ não é aceite). Não escreva prosa nova: se
   uma correção pede redação, devolva o trecho à etapa 4. A verificação técnica mudou um número
   que quebra uma frase da revisão? Resolva pela leitura dos três laudos.

2. **Checklist de aderência à voz** (§9 de `estilo/estilo-autoral.md`, via `voz-syntaxis`). Os
   itens marcados (m) são do script do item 3; aqui, só os de julgamento.

3. **Checagem mecânica: `python3 scripts/checar_post.py <slug>`.** Substitui a conferência
   manual de marcadores, placeholders, frontmatter, rótulo de H2, travessão, parágrafo e
   `rangemode` do Tufte. Bloqueante de aplicação (placeholder sem bloco, frontmatter) se corrige
   aqui. Marcador de pendência (`[VERIFICAR]`, `[FAIXA]`, `[PREENCHER]`, `[LINK`) nunca se
   resolve a favor de uma suposição: fica visível no `post.md` e vira pergunta na etapa 10. Os
   avisos vão para o resumo. O que o script não vê continua seu: `infograficos.md` sem
   justificativa registrada, 3D, sombra ou moldura no código, e Lie Factor declarado
   (`.claude/agents/references/checklist-graficos.md`, "Gate de Tufte").

4. **Antipadrões:** `voz-syntaxis/references/antipadroes.md`, com os pares reais do que o autor
   corta. A lista genérica da frente D não é lida inteira: o pipeline já não produz aqueles tiques.

5. **Achado enterrado — alarme, não correção.** Se o insight mais forte do post ainda estiver
   no meio de um parágrafo neste ponto, esta etapa não reestrutura. Sinalize no resumo da etapa
   10 que a etapa 5 deixou passar, para o gate humano decidir se reabre a etapa 2.

6. **Fluxo por linha editorial — checagem final.**
    - `linha_editorial: Spoiler` — todo item `bloqueante` de
      `_revisoes/AAAA-MM-DD_slug_quant.md` (`revisor-quant`) tem resposta registrada do
      autor? Se não, esta etapa não fecha — volta para o gate da etapa 5a.
    - `linha_editorial: Notas de um Professor` — a Ficha de Saída (`02-estrutura.md`) está
      preenchida e a competência de saída declarada nela é de fato entregue pela estrutura
      final? O texto trata os dois lados do balcão (não só a ótica do investidor)? A
      bibliografia final tem 3-4 itens com no mínimo 2 livros (`docs/BACKWARDS_DESIGN.md`
      §5.7)? Alguma divergência numérica registrada em
      `_revisoes/AAAA-MM-DD_slug_calculo.md` ficou sem correção aplicada?

## Saída

Aplica as correções diretamente nos entregáveis (`post.md`, `graficos.md`, `diagramas.md`,
`infograficos.md` quando existirem) e devolve um resumo curto do que mudou desde a etapa 7,
para o gate humano (etapa 10) mostrar ao autor.
