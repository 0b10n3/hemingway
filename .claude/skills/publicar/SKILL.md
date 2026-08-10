---
name: publicar
description: Faz o merge de um post aprovado da branch post/<slug> para main, tageia e publica no GitHub. Use só depois do "aprovar e publicar" no gate humano do pipeline post-substack — nunca antes de aprovação explícita do autor.
disable-model-invocation: true
argument-hint: [slug]
allowed-tools: Read Glob Grep Bash(git add *) Bash(git commit *) Bash(git checkout *) Bash(git merge --no-ff *) Bash(git tag *) Bash(git push origin *) Bash(git log *) Bash(git status *)
---

Roda só após o "aprovar" explícito na etapa 10 do `post-substack`. Não chame esta skill como
atalho para pular o gate humano.

## Passo a passo

1. **Confere completude.** `post.md`, `ilustracoes.md` e `graficos.md` existem em
   `posts/<slug>/`? Algum tem `[VERIFICAR]` pendente? Se tiver, liste cada um e pergunte ao
   autor se publica assim mesmo — não decida sozinho.

2. **Commita o que restar solto** na branch `post/<slug>` (`git status` primeiro; nunca
   `git add -A` cego — revise o que está sendo adicionado).

3. **Merge para main:**
   ```
   git checkout main
   git merge --no-ff post/<slug>
   ```
   Mensagem de merge resume o post em três linhas (título, tese, para quem é).

4. **Tag:** `git tag publicado/AAAA-MM-DD-<slug>`.

5. **Push:** `git push origin main --follow-tags`.

6. **Reporta a URL do commit** no repositório remoto (`REPO` do `CLAUDE.md`/config) para o
   autor colar diretamente na Substack.

## Depois de publicar

**Não apague a branch `post/<slug>`.** O histórico das versões descartadas ao longo do
pipeline (drafts anteriores, críticas, revisões) é material de entrada para
`/forja-de-voz atualizar` — apagar a branch destrói esse rastro.

## Segurança

Nunca `--force`, nunca `reset --hard`, nunca deleção de branch. Se o merge tiver conflito,
pare e mostre o conflito ao autor — não resolva automaticamente escolhendo um lado.
