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

## `ilu-01-16x9`

Mesma imagem/ideia de `ilu-01`, variante widescreen pedida pelo autor em 2026-09-11 (proporção
16:9, para uso em formatos que exigem horizontal — ex. capa de e-mail, banner).

**Arquivo:** `figuras/ilu-01-16x9.png` — 1376×768px (proporção 1,79:1, o bucket nativo de
"16:9" do gerador).

**Resolução — limitação conhecida:** o pedido original era 2K (2048px+); a ferramenta
`agy:image` não expõe parâmetro de resolução (só `--name`/`--output`), então pedir "2K" no
texto do prompt não teve efeito — o gerador decide o tamanho de pixel sozinho. Aceito como
está por decisão do autor (768px de altura é adequado para uso em newsletter/web, não para
impressão ou tela grande).

Paleta e estilo idênticos a `ilu-01` (fundo claro nesta variante, em vez de verde escuro — a
mesma composição funciona nos dois tons, sem inconsistência com a marca).

**Alt-text:** "Ilustração: coluna vertebral de papel recortado, em tons de verde floresta
sobre fundo claro, com um rasgo horizontal na região lombar iluminado por um brilho
verde-limão, revelando por baixo fórmulas de teoria da probabilidade — formato widescreen."

## `ilu-01-16x9-dark`

Variante dark de `ilu-01-16x9`, pedida pelo autor em 2026-09-11 — mesma composição e ideia,
fundo trocado de claro para verde muito escuro (mais próximo da versão original `ilu-01`, que
já era dark).

**Arquivo:** `figuras/ilu-01-16x9-dark.png` — 1376×768px (proporção 1,79:1), mesma limitação
de resolução já registrada em `ilu-01-16x9` (sem controle de resolução exposto pela
ferramenta, 2K pedido não foi atendido, aceito pelo autor).

**Alt-text:** "Ilustração: coluna vertebral de papel recortado em tons de verde floresta sobre
fundo verde muito escuro, com um rasgo horizontal na região lombar iluminado por um brilho
verde-limão, revelando por baixo fórmulas de teoria da probabilidade (Bayes, variância) —
formato widescreen, variante dark."
