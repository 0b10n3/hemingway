# Relatório — auditoria de storytelling & dataviz

2026-08-10. Fecha o ciclo do prompt de auditoria: diagnóstico (`pesquisa/auditoria-storytelling.md`),
8 patches aprovados em bloco, todos aplicados e commitados individualmente.

## Patches aplicados (8/8)

| # | Artefato | Resumo | Severidade | Commit |
|---|---|---|---|---|
| 1 | `revisao-editorial/references/tecnicas-narrativas.md` (novo) | SSOT: arco narrativo (condicionado ao subgênero), três pilares, "não abra pela metodologia", "não enterre o achado", fórmula de manchete marcada como técnica a testar | estrutural | `ba4ca6b` |
| 2 | `post-substack/SKILL.md`, etapa 1 | Campo explícito de gancho no briefing | reforço | `3d263a3` |
| 3 | `post-substack/SKILL.md`, etapa 2 | Mapeia seções ao arco e aos três pilares na estrutura | estrutural | `1a61de3` |
| 4 | `critico-editorial.md` | Três pilares, "metodologia primeiro" e "achado enterrado" como critérios de diagnóstico, com poder de mandar de volta à etapa 2 | estrutural | `31969ec` |
| 5 | `revisao-editorial/SKILL.md` | Checagem de manchete (não-bloqueante) + alarme de achado enterrado (sem poder de reestruturar) | estrutural | `6f0fbf1` |
| 6 | `prompts-visuais/references/checklist-graficos.md` (novo) | SSOT: anotação, revelação progressiva, contraste genuíno vs. forçado | reforço | `1b5598f` |
| 7 | `prompts-visuais/SKILL.md` | Aponta para o checklist novo + exige anotação no spec de `graf-NN` | reforço | `72be4a8` |
| 8 | `verificador-tecnico.md` + `revisao-editorial/SKILL.md` (follow-up) | Veredito novo `[FAIXA: ...]`, distinto de `[VERIFICAR: ...]`; `revisao-editorial` trata os dois com a mesma regra de "nunca resolvido silenciosamente" | estrutural | `8ceec08` |

Nenhum patch foi recusado — todos os 8 achados da Fase 2 tinham evidência de linha e foram
aprovados em bloco.

## Tensões registradas para a `forja-de-voz` (não resolvidas por esta auditoria)

1. **Fórmula de manchete pede número técnico no título; nenhum dos 6 títulos do corpus usa
   número.** Resolvido rebaixando a técnica a "teste opcional" (patches 1 e 5) em vez de
   regra obrigatória. Se o autor testar em posts reais e gostar, vira candidato a regra via
   `/forja-de-voz atualizar`, com evidência própria — nunca por dedução deste prompt.
2. **Arco em seis atos termina em "chamada para ação"; a voz explicativa (§4.2 do guia)
   nunca tem CTA.** Resolvido condicionando o último ato ao subgênero dentro do patch 1 —
   `estilo/estilo-autoral.md` não foi tocado por esta auditoria, como exigido pelas regras
   invioláveis do prompt.

## Nota de escopo aplicada (divergência informada do Apêndice B)

O Apêndice B do prompt de auditoria sugeria checar "não enterre o achado" só em
`revisao-editorial`. A auditoria (Fase 2) encontrou que isso conflita com o próprio limite de
escopo dessa skill (ela explicitamente não reabre estrutura). Os patches 1, 4 e 5 dividem a
técnica em duas camadas coerentes com `pesquisa/frente-c-editoracao.md`: `critico-editorial`
(etapa 5, developmental) diagnostica com poder de mandar de volta à etapa 2;
`revisao-editorial` (etapa 9, consolidação) só sinaliza como alarme se ainda estiver
enterrado nesse ponto — nunca corrige sozinha.

## Lacunas

Nenhuma. Todos os cinco artefatos-alvo do Apêndice B já existiam e foram lidos por completo
antes do diagnóstico (Fase 0 confirmou via `git ls-files .claude/`).

## Regressão (teste de disparo, Fase 4 do prompt de auditoria)

**Bloqueado nesta sessão pela mesma causa já documentada em `RELATORIO.md`**: skills e
agentes criados ou editados na sessão corrente do Claude Code não ficam invocáveis por nome
até uma sessão nova. Confirmado tentando `Skill: revisao-editorial` e `Skill: critico-editorial`
agora — ambos retornam "Unknown skill" mesmo após o patch.

**Para completar a regressão:** abra uma sessão nova (`cd hemingway && claude`) e confirme:
- Uma frase natural (“crítica esse rascunho”, “gera os gráficos deste post”) ainda dispara a
  skill/agente certo — o texto do `description` de nenhum artefato mudou nesta auditoria, só
  o corpo, então o risco de regressão de disparo é baixo, mas fica para confirmar.
- `references/tecnicas-narrativas.md` e `references/checklist-graficos.md` são lidos no
  momento certo (a frase de "quando ler" já está no corpo de cada `SKILL.md`/agente que os
  usa — verificado por leitura, não por execução).
- Rodar `/post-substack` ponta a ponta numa transcrição real e confirmar que a etapa 2 agora
  produz o mapeamento seção→ato→pilar, e que a etapa 5 consegue mandar de volta à etapa 2 por
  causa de um achado enterrado (teste específico do patch 4 — vale forçar um rascunho ruim de
  propósito na primeira vez para ver o mecanismo funcionar).
