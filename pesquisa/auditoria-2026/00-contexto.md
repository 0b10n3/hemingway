# Fase 0 — Entendimento do sistema (para confirmação do autor)

## O que é

`hemingway` não é código de produto: é um pipeline editorial de 11 etapas (0–10),
orquestrado por `/post-substack`, que leva transcrição de áudio a post publicável na
Substack Syntaxis, com voz autoral verificada, checagem técnica e visuais especificados.
Cada etapa grava em `posts/<slug>/processo/`, atualiza `estado.json`, commita
(`feat(<slug>): <etapa>`) — confirmado real no `git log` do post mais recente, um commit por
etapa, sem exceção. Gate humano na etapa 10 via `AskUserQuestion`.

## Inventário (bate com `RELATORIO.md`, sem deriva)

7 skills — `voz-syntaxis`, `marca-syntaxis` (referência, sem `disable-model-invocation`);
`forja-de-voz`, `revisao-editorial`, `publicar`, `post-substack`, `prompts-visuais` (tarefa,
todas com `disable-model-invocation: true`). 5 agentes — `critico-editorial`,
`extrator-de-estilo`, `pesquisador-editorial`, `revisor-gramatical`, `verificador-tecnico`,
todos `model: inherit`, só `revisor-gramatical` pré-carrega uma skill (`voz-syntaxis`).

## Fonte única de cada coisa

Voz autoral: `estilo/estilo-autoral.md` + `voz.fingerprint.json` (9 regras, corpus de 7
textos/25.685 palavras, confiança média) — dois subgêneros Substack (ensaística/explicativa)
mais um acadêmico não aplicável ao Substack. Marca/design: `../../brand/DESIGN.md` v2.0 +
`.../brand/tokens/skill_test.tokens.json`, únicos desde que `marca/tokens.json` foi
aposentado (31/08) — path relativo de 5 hops verificado, resolve. Duas linhas editoriais
(`PROJECT_DESCRIPTION.md`): Spoiler (colagem) e Notas de um Professor (desenho técnico
esquemático) — decisão **separada** da voz, com caso real comprovando isso
(`2026-08-25-dividir-para-nao-correr-risco` é ensaística e não é Spoiler). Briefing de
ilustração (`briefing-ilustracao.md`) está na v2: hierarquia de material em três camadas
(metáfora do autor no topo), motor de três operações (extensão/cruzamento/torção), critérios
positivos de beleza, teste da fatalidade.

## Achados já visíveis (evidência real, para Fase 1)

1. **Nenhum post rodou a etapa 8a nova de ponta a ponta.** Os 3 posts publicados são
   anteriores ao motor generativo; o mais recente (`2026-08-25`) ainda referencia
   `marca/tokens.json` (removido), a regra revogada do "elemento iluminado", e tem blocos
   `Negative prompt` — que a própria `prompts-visuais/SKILL.md` diz que o Nano Banana Pro não
   suporta. Consistente com a regra de não reescrever `_arquivo`/entregáveis publicados, mas
   confirma que o sistema novo é **não testado em produção**.
2. **`prompts-visuais/SKILL.md` está desatualizada em relação ao próprio arquivo que cita:**
   o resumo inline da etapa 8a ainda descreve o método v1 ("quatro testes de rejeição, no
   mínimo três conceitos"), não o motor v2 de `briefing-ilustracao.md`.
3. **Bloqueio real já documentado em produção** (`estado.json`, `pendencias`): a etapa 10 diz
   "Aprovar → invoque a skill `publicar`", mas `publicar` (e o próprio `post-substack`) tem
   `disable-model-invocation: true` — o autor precisou rodar `/publicar` manualmente. Vale
   investigar na Fase 1 se isso é o comportamento pretendido do flag ou uma inconsistência de
   design.
4. **Precedente real para a Fase 2 (capa):** o mesmo post já teve reentrada ad hoc na etapa 8
   pedindo "duas opções de capa 16:9", registrada em `estado.json.reentradas` — evidência
   direta de que a demanda por capa dedicada já apareceu na prática, sem categoria formal.

## O que não foi relido nesta sessão (transparência, não silêncio)

`../../brand/DESIGN.md` e `tokens/skill_test.tokens.json` — confirmados por path, não
relidos por inteiro (conhecimento fresco de tê-los editado na sessão imediatamente anterior).
`taxonomia-estilometrica.md`, `references/antipadroes.md` e `references/exemplos-pareados.md`
de `voz-syntaxis`/`forja-de-voz` — citados pelas skills que os usam, não lidos
independentemente (baixo risco: conteúdo resumido inline em `extrator-de-estilo.md` e
`estilo-autoral.md`). `claude --version` local = 2.1.251, acima do mínimo do README
(2.1.196+).

## Branch

Criada `chore/auditoria-2026` a partir de `main`. Nenhuma mudança em arquivo existente até
agora — sessão inteiramente de leitura.

---

**Se este entendimento estiver certo, sigo para a Fase 1 (auditoria de skills/agentes).**
