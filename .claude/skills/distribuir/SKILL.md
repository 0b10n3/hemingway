---
name: distribuir
description: Gera o kit de distribuição da esteira v2 de um post já aprovado no gate (Notes do Substack, post do LinkedIn, legendas e o manifesto kit.json com as datas), valida por script e leva ao mini-gate do autor. Use quando o autor pedir para distribuir, divulgar ou montar o kit de um post aprovado.
disable-model-invocation: true
argument-hint: <slug> [AAAA-MM-DD da publicação no Substack]
allowed-tools: Read Edit Glob Grep Bash(python3 *) Bash(git add *) Bash(git commit *) Bash(git status *) Bash(git diff *) Bash(git log *) Bash(git branch *) Bash(git checkout post/*) Bash(git checkout -b post/*)
---

Orquestrador da etapa Distribuição. Roda na sessão principal porque termina num gate humano.
É uma cadeia fixa, com código entre os passos: `kit.py montar` → `redator-distribuicao` →
`kit.py validar` → (vídeo) `diretor-visual` → `storyboard.py md` + `validar` → mini-gate. A conversa principal não lê o post nem o guia de voz: recebe só os
arquivos gerados e o relatório do validador.

Regras e números: `config/esteira.yaml`. Referência dos subagentes: skill `distribuicao`.

## Antes de começar

1. O post precisa estar aprovado no gate: `posts/<slug>/estado.json` com `"status": "aprovado"`
   (ou a aprovação da etapa 10 registrada em `aprovacoes`). Sem isso, pare e avise o autor: o kit
   cita trechos do texto final.
2. Branch: `git checkout post/<slug>` se ela existir; senão, `git checkout -b post/<slug>` a partir
   de `main`.
3. Se `posts/<slug>/distribuicao/` já existe, mostre o `kit.md` e pergunte se é para refazer. Nada
   de sobrescrita silenciosa. Refazer as datas: `montar … --substituir`. Os textos ficam; para
   refazê-los, o mini-gate pede os IDs.

## Passos

1. `python3 scripts/gerar_catalogo.py`, depois `python3 scripts/kit.py montar <slug> [data]`.
   Sem data, o script usa o próximo dia de publicação da linha a partir de hoje (terça para *Notas
   de um Professor*, sexta para *Spoiler*). Diga ao autor, numa linha, a data que entrou: o campo
   `data` do post é a data do rascunho, não a da publicação.
2. Dispare o `redator-distribuicao` com o slug. Ele preenche `distribuicao/textos.md`.
3. `python3 scripts/kit.py validar <slug>`. Se reprovar, mande os erros ao mesmo subagente e peça
   uma nova versão **uma vez**. Se reprovar de novo, siga: o `kit.md` sai marcado "KIT INVÁLIDO",
   com os erros visíveis. A etapa nunca trava a publicação do post.
4. **Vídeo (só quando o kit tem peça `video`).** O `redator-distribuicao` do passo 2 também escreve
   `distribuicao/video/roteiro.md` (a fala). Depois:
   1. Dispare o `diretor-visual` com o slug e o `post.data_video` de
      `python3 scripts/storyboard.py data <slug>`. Ele escreve `distribuicao/video/storyboard.json`.
   2. `python3 scripts/storyboard.py md <slug>` e `python3 scripts/storyboard.py validar <slug>`. Se
      reprovar, mande os erros ao mesmo subagente **uma vez** (erro de fala vai ao redator, de cartão ao
      diretor-visual). Se reprovar de novo, leve os erros ao mini-gate.
   A montagem é do `../spielberg` (`/spielberg <slug>`), que lê o storyboard. Não o edite.
5. Se o post já tem `url_publicada` (um caso antigo, por exemplo), rode
   `python3 scripts/kit.py url <slug>`.
6. Commit `feat(<slug>): distribuição — textos do kit` (e roteiro e storyboard, se houver vídeo).

## Mini-gate

Mostre o `kit.md` inteiro e, se houver vídeo, o `video/storyboard.md`. Use `AskUserQuestion` com três saídas: **aceitar**, **ajustar por ID**,
**deixar para depois**.

- **Ajustar:** o autor diz os IDs e o que mudar ("N1: gancho mais curto; L2 sem a segunda frase").
  Mande ao `redator-distribuicao` só esses IDs e o pedido, rode `kit.py validar` e mostre de novo só
  os blocos alterados e o relatório. Até **2 iterações**; esgotadas, entregue o estado atual com o
  que não convergiu, e o autor edita à mão.
- **Texto escrito pelo autor** entra literal: Edit no bloco do ID em `textos.md`, depois
  `kit.py validar`.
- Registre em `posts/<slug>/estado.json` a chave `distribuicao`: `data_publicacao`, `iteracoes`,
  `ids_ajustados` e `aprovado` (true ou false).
- Commit `feat(<slug>): distribuição — mini-gate` (com "aprovado" quando for o caso).

## Depois do mini-gate

- Mostre o calendário (a tabela do `kit.md`): o que sai em cada dia e o que é feito à mão.
- Lembre: depois de publicar o post, `/forja-de-voz colher <slug>` registra a `url_publicada` e roda
  `kit.py url`, que troca `{{URL_POST}}` em todos os arquivos do kit e marca as peças como prontas.
  Nenhum modelo mexe nessa troca.
- O `../uther-pendragon` lê `kit.json` e `config/esteira.yaml` para planejar a semana. Não o edite.
- Vídeo e carrossel ficam `aguarda-producao`. O vídeo já sai com roteiro e storyboard (Fatia C); o
  autor grava as tomadas (`roteiro.md`) e roda `/spielberg <slug>` no `../spielberg`. O carrossel
  entra na Fatia B.

## Regras

- A etapa não altera `post.md` nem `marketing.json`. Escreve só em `posts/<slug>/distribuicao/` e
  na chave `distribuicao` de `estado.json`.
- `storyboard.md` e `post.data_video` são do script. Nenhum modelo os escreve.
- Datas, IDs, `kit.json` e `kit.md` são do script. Nenhum modelo os escreve.
- Push só com o ok do autor.
