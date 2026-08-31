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
`../../../../../brand/DESIGN.md` e `../../../../../brand/tokens/skill_test.tokens.json` antes de escrever
qualquer prompt ou código (ver nota de 31/08/2026 em `marca-syntaxis/SKILL.md`: posts
publicados antes dessa data usam o sistema anterior e não são referência para trabalho novo).

## `ilustracoes.md`

### Antes de escrever qualquer prompt: identifique a linha editorial

O estilo artístico da ilustração é **determinado pela linha editorial do post**, não pela voz
do texto e não pelo gosto de quem gera o prompt:

- **Spoiler** (carreira, relato pessoal) → colagem editorial
- **Notas de um Professor** (conceito, produto, mecanismo) → desenho técnico esquemático

Onde ler a linha, nesta ordem: o campo `linha_editorial` no frontmatter de `post.md`; a seção
"Linha editorial" de `processo/01-briefing.md`; a tag correspondente em `tags`.

**Se a linha não estiver declarada em nenhum desses lugares, ou se as fontes discordarem,
pare e pergunte ao autor.** Não deduza a partir da voz — voz e linha editorial não coincidem
sempre, e o repositório já tem um caso real de post ambíguo (ver
`references/estilos-ilustracao.md`, última seção).

Especificação completa dos dois estilos, hex autorizados e checklist de prompt:
**`references/estilos-ilustracao.md`** — leia antes de escrever o primeiro prompt.

### Etapa 8a — briefing antes do prompt (obrigatório)

**Nunca vá do texto direto ao prompt.** Rode primeiro o método de
**`references/briefing-ilustracao.md`** e grave o resultado em
`processo/08-briefing-visual.md`: colheita de material concreto do post → a frase que a peça
carrega → no mínimo três conceitos divergentes (justaposição / fusão / substituição) → quatro
testes de rejeição → escolha com os descartes anotados.

Esse passo existe porque a primeira rodada do sistema de estilos produziu peças tecnicamente
corretas e editorialmente mudas: escada espelhada e cápsula-câmara-cápsula, conceitos
importados de fora do texto enquanto os posts ofereciam o sumário do Hull, o compulsório de
21% contra 20% e o "outro lado do balcão" sem ninguém pegar. **Estilo é a última decisão, não
a primeira.**

### Formato de cada bloco `ilu-NN`

- Onde entra no texto e que ideia carrega (referencie o parágrafo/seção de `post.md`).
- **Conceito e estrutura de metáfora** — o conceito escolhido em `08-briefing-visual.md`, a
  estrutura usada (justaposição / fusão / substituição) e o material do texto que ele usa.
- **Linha editorial e estilo aplicado**, em uma linha — deixa auditável, na própria peça, por
  que ela ficou com essa cara.
- Prompt completo para `GERADOR_IMAGEM` (Google Nano Banana Pro): cena narrada seguindo
  `[Sujeito] + [Ação/estado] + [Contexto] + [Composição] + [Estilo e materialidade] +
  [Paleta com hex] + [Proporção]`, com os hex citados por nome do token (ex. "flat deepForest
  background #0F3D27"), proporção e resolução explícitas.
  Escreva o prompt em inglês se o gerador responde melhor assim, mas sempre com uma nota de
  contexto em português logo abaixo — quem relê esse arquivo depois é o autor, não o gerador.
- **Restrições em enquadramento positivo** — o que a peça deve ter, não o que deve evitar.
  O Nano Banana Pro **não suporta negative prompt** (ver `references/estilos-ilustracao.md`,
  "Como escrever o prompt"): o guia oficial recomenda enquadramento positivo no lugar. Por isso
  esta seção substituiu o antigo bloco `### Negative prompt` — escrever um era teatro, o
  gerador nunca leu.
- Alt-text final — vai para o `post.md` como texto alternativo do placeholder e sustenta o
  post caso a imagem não carregue, então precisa ser descritivo por si só, não decorativo.

### Revogado em 31/08/2026

A regra do **"elemento iluminado"** (contraste por glow verde sobre fundo escuro), que
governava as ilustrações dos posts de agosto/2026, **não vale mais**: `brand/DESIGN.md` §4.5
lista "gradientes, glassmorphism, blobs desfocados, **glows**" como anti-padrão verificável.
Contraste agora se faz por cor chapada, densidade e escala. As `ilustracoes.md` já publicadas
não foram reescritas (mesma regra de `_arquivo/`: registro do que foi feito não se maquia) —
mas não são referência para peça nova.

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
  caminho relativo, aplica os tokens de `../../../../../brand/tokens/skill_test.tokens.json` (leia o
  JSON em runtime ou copie os valores `$value` exatos com comentário apontando a origem —
  nunca hardcode cor fora do tokens.json), exporta para `posts/<slug>/figuras/graf-NN.svg` e
  `.png`. Cada bloco roda sozinho, sem preâmbulo — teste com `python3` antes de considerar a
  etapa concluída.
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
