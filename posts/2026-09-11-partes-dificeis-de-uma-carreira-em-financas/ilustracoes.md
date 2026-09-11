# Ilustrações — fora do pipeline `/post-substack`

**Nota:** capa e ilustração saíram do pipeline `/post-substack` em 2026-09-09 (ver
`.claude/skills/prompts-visuais/SKILL.md`). Este arquivo registra uma peça gerada **fora**
desse fluxo, a pedido explícito do autor no gate humano (etapa 10, rodada 1) — não é produto
padrão do pipeline e não segue o formato de `graficos.md`/`diagramas.md` (sem código
reproduzível, sem CSV de dados).

## `ilu-01`

**Origem:** sugestão de visual já presente no rascunho de origem (`_arquivo/transcricoes/...`,
ver `processo/00-transcricao.md`, marcador 3) — "uma coluna vertebral de papel recortado,
aberta por um rasgo na lombar, revelando páginas de fórmula por baixo".

**Frase que a peça carrega:** "a competência que sustenta a carreira mora na parte que ninguém
escolhe treinar."

**Ferramenta:** Antigravity CLI (`agy`), gerador Imagen, via skill `agy:image` — não Plotly,
não reproduzível por código (é geração de imagem, não gráfico de dado).

**Paleta:** tokens de `../../../../brand/tokens/syntaxis.tokens.json` usados por referência no
prompt (forest 500/700, lime 500), não lidos em runtime por não haver código — checagem visual
manual confirma aderência (verde floresta escuro dominante, acento lime só no rasgo/brilho da
abertura, sem gradiente 3D, sem canto arredondado).

**Arquivo:** `figuras/ilu-01.png`.

**Alt-text:** "Ilustração: coluna vertebral de papel recortado, em tons de verde floresta,
com um rasgo na região lombar iluminado por um brilho verde-limão, revelando por baixo páginas
de fórmulas de teoria da probabilidade (Bayes, distribuição binomial, variância)."

**Placeholder, se usado no `post.md`:**

```markdown
![Ilustração: coluna vertebral de papel recortado em tons de verde floresta, com um rasgo na lombar revelando fórmulas de probabilidade por baixo](ilu-01)
```
