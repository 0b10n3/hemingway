---
name: marca-syntaxis
description: Identidade visual e design tokens do Syntaxis (DESIGN.md v2.0 — Forest/Grove/Lime, cantos retos). Use sempre que for gerar prompt de imagem, código de gráfico Plotly, ou qualquer decisão de cor/tipografia/proporção para os visuais de um post.
---

**Nota de 31/08/2026:** este repositório não mantém mais cópia própria de tokens. A fonte é
`../../../../../brand/DESIGN.md` (regras e racional) + `../../../../../brand/tokens/skill_test.tokens.json`
(valores exatos, formato DTCG). **Não recrie identidade visual**: leia os dois arquivos, não
repita cores literais de memória — inclusive as usadas em posts já publicados, que refletem
o sistema anterior ("O Sinal no Escuro" v2.1, paleta Volt) e não devem servir de referência
para trabalho novo.

## Estrutura de `../../../../../brand/tokens/skill_test.tokens.json` (formato DTCG)

- `color.forest` / `color.grove` / `color.lime` — escalas 100–900. **Forest** é a âncora
  institucional; **Grove** é estrutura em movimento (links, progresso); **Lime** é o único
  acento de ação/conquista — "o sinal no escuro" desta versão do sistema.
- `color.neutral` — chalk (fundo light), ink (fundo dark e texto sobre lime), slate (único
  cinza de texto permitido), mist (hairlines), mint, deepForest (banda escura).
- `color.theme.light` / `color.theme.dark` — mapeamento semântico já resolvido (background,
  foreground, primary, accent etc.) — prefira usar esses aliases a montar a cor na mão.
- `typography.fontFamily` — display: Space Grotesk; body: Hanken Grotesk; data: Space Mono.
- `radius` — sistema de **cantos retos**: `none` (0px, padrão), `sm` (2px, máximo permitido
  em chips), `full` (exclusivo para avatar/símbolo circular do logo). Nunca use radius
  intermediário (8–16px) — isso é anti-padrão explícito em `brand/DESIGN.md` §4.5.
  Cada valor tem `$value` (o que usar) e, quando aplicável, `$description` (quando/por quê).
- `pattern.nodeBranch` / `pattern.dataGrid` / `pattern.growthLine` — os três padrões
  geométricos da marca (ver `brand/DESIGN.md` §5). `growthLine` é o único ligado a conquista
  real (certificados, badges) — nunca decoração ambiente.

## Quando usar

- **`prompts-visuais` (etapa 8 do pipeline):** todo prompt de imagem para o gerador
  (`GERADOR_IMAGEM`) embute a paleta e a regra do "sinal no escuro" (Lime sobre Deep
  Forest/Ink) — leia `../../../../../brand/tokens/skill_test.tokens.json` antes de escrever o prompt,
  não invente hex.
- **Código Plotly em `graficos.md`:** o bloco Python deve importar as cores de
  `../../../../../brand/tokens/skill_test.tokens.json` (ex.: lendo o JSON em runtime, ou copiando os
  valores `$value` exatos com comentário apontando a origem) — nunca hardcode um hex que não
  esteja no arquivo.
- **Qualquer decisão de proporção/grid:** `spacing.*` (grid de 8px) e `radius.*` de
  `skill_test.tokens.json` são os valores canônicos para espaçamento e raio de borda, quando
  relevante para composição de imagem. Cantos retos, não arredondados.

## Regra de ouro

Se o token que você precisa não existe no `tokens.json`, **pare e pergunte** antes de
inventar um hex novo — não é decisão de skill, é decisão de marca.
