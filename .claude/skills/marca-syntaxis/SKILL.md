---
name: marca-syntaxis
description: Identidade visual e design tokens do Syntaxis ("O Sinal no Escuro" — Dark Evolution). Use sempre que for gerar prompt de imagem, código de gráfico Plotly, ou qualquer decisão de cor/tipografia/proporção para os visuais de um post.
---

A fonte de verdade é `marca/tokens.json` — hex + oklch sincronizados, já existente antes
deste bootstrap. **Não recrie identidade visual**: leia o arquivo, não repita cores literais
de memória.

## Estrutura do tokens.json

- `neutrals` — obsidian (fundo principal), graphite, carbon, carbon_hi, pine, line, line_hi.
- `volt` — a cor de destaque da marca, em escala 300-900 (verifique o arquivo para a escala
  completa); é o "elemento iluminado" que dá identidade ao sistema "Sinal no Escuro".
- Cada token tem `hex`, `role` (quando usar) e `oklch` (para interpolação/gradiente correto
  em vez de blend ingênuo em RGB).

## Quando usar

- **`prompts-visuais` (etapa 8 do pipeline):** todo prompt de imagem para o gerador
  (`GERADOR_IMAGEM`) embute a paleta e a regra do elemento iluminado — leia `marca/tokens.json`
  antes de escrever o prompt, não invente hex.
- **Código Plotly em `graficos.md`:** o bloco Python deve importar as cores de
  `marca/tokens.json` (ex.: lendo o JSON em runtime, ou copiando os valores hex exatos com
  comentário apontando a origem) — nunca hardcode um hex que não esteja no arquivo.
- **Qualquer decisão de proporção/grid:** `$meta.grid` (8px) e `$meta.radius_base` (12px) do
  tokens.json são os valores canônicos para espaçamento e raio de borda, quando relevante
  para composição de imagem.

## Regra de ouro

Se o token que você precisa não existe no `tokens.json`, **pare e pergunte** antes de
inventar um hex novo — não é decisão de skill, é decisão de marca.
