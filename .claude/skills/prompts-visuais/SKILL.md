---
name: prompts-visuais
description: Gera os prompts de imagem (ilustracoes.md) e as specs de gráfico com código Plotly executável (graficos.md) para um post, a partir da estrutura definida na etapa 2 do pipeline. Use na etapa 8 do post-substack, ou isoladamente quando pedirem para "gerar os visuais" de um texto que já tem os placeholders ilu-NN/graf-NN marcados.
disable-model-invocation: true
argument-hint: [caminho-do-slug-em-posts/]
allowed-tools: Read Write Edit Glob Grep Bash(python3 *)
---

Lê `posts/<slug>/processo/02-estrutura.md` (onde cada `ilu-NN`/`graf-NN` foi decidido e por
quê) e `posts/<slug>/04-draft-v1.md` ou o draft mais recente em `processo/`, e produz os dois
entregáveis visuais. Usa `marca-syntaxis` para paleta/tipografia — leia
`marca/tokens.json` antes de escrever qualquer prompt ou código.

## `ilustracoes.md`

Um bloco por `ilu-NN`:

- Onde entra no texto e que ideia carrega (referencie o parágrafo/seção de `post.md`).
- Prompt completo para `GERADOR_IMAGEM` (Google Nano Banana Pro), com a identidade de marca
  embutida: paleta de `marca/tokens.json` (cite os hex/oklch relevantes por nome do token,
  ex. "fundo obsidian #0A0F0D"), tipografia se aplicável, a regra do elemento iluminado
  (contraste entre fundo escuro e um elemento na cor `volt`), proporção e resolução.
  Escreva o prompt em inglês se o gerador responde melhor assim, mas sempre com uma nota de
  contexto em português logo abaixo — quem relê esse arquivo depois é o autor, não o gerador.
- *Negative prompt*.
- Alt-text final — vai para o `post.md` como texto alternativo do placeholder e sustenta o
  post caso a imagem não carregue, então precisa ser descritivo por si só, não decorativo.

## `graficos.md`

Antes de escrever qualquer spec, leia `references/checklist-graficos.md` — anotação,
revelação progressiva e contraste genuíno vs. forçado.

Um bloco por `graf-NN`:

- **Pergunta que o gráfico responde**, em uma frase. Se não couber numa frase, o gráfico está
  fazendo duas coisas — volte à etapa 2 e separe em dois `graf-NN`.
- **Fonte dos dados**, com link e data de acesso — ou `[VERIFICAR]` se `07-verificacao.md`
  não fechou essa fonte.
- **Dados** salvos em `posts/<slug>/graficos/dados/graf-NN.csv`, versionados junto — um
  gráfico cujo dado não está no repositório não é reproduzível seis meses depois.
- **Código Plotly executável**, em bloco ` ```python `, autocontido: lê o CSV ao lado por
  caminho relativo, aplica os tokens de `marca/tokens.json` (leia o JSON em runtime ou copie
  os hex exatos com comentário apontando a origem — nunca hardcode cor fora do tokens.json),
  exporta para `posts/<slug>/figuras/graf-NN.svg` e `.png`. Cada bloco roda sozinho, sem
  preâmbulo — teste com `python3` antes de considerar a etapa concluída.
- **Escolha de tipo de gráfico justificada** em uma linha, e o que foi descartado.
- **Alt-text e legenda.**
- **Anotação**: todo ponto de interesse tem `add_annotation` apontando para ele (ver
  `references/checklist-graficos.md`).

## Regra de placeholder no `post.md`

Cada imagem/gráfico vira, no texto:

```markdown
![Ilustração: <legenda descritiva curta>](ilu-01)
![Gráfico: <legenda descritiva curta>](graf-01)
```

A legenda no alt-text não é opcional — é o que sustenta o post se a imagem falhar ao
carregar, então tem que carregar a ideia sozinha.
