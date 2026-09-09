# Proposta — remoção de capa e ilustração do pipeline

Em resposta a `00-diagnostico.md`. Uma frente só, puramente de documentação/skill (risco
baixo). Critério de pronto: nenhuma skill ativa do `hemingway` instrui gerar capa ou
ilustração; `graf-NN`/`diag-NN`/`info-NN` continuam exatamente como estavam.

## Mudanças

1. **`prompts-visuais/SKILL.md`** — remove `## capa.md` e `## ilustracoes.md` inteiros;
   ajusta frontmatter/descrição; ajusta `## infograficos.md` (elemento de apoio ilustrativo
   deixa de ser opção); ajusta "Regra de placeholder" (tira `ilu-NN` e a nota de capa); ganha
   nota datada explicando a remoção e a regra de não tocar posts já publicados.
2. **Apaga** os arquivos de `references/` exclusivos de ilustração: `briefing-ilustracao.md`,
   `estilos-ilustracao.md`, `templates-prompt.md`, `exemplos-prompts.md`,
   `checagem-graos.md`, `checagem-paleta.md`, `geradores/` (pasta inteira). Mantém
   `checklist-graficos.md`.
3. **`post-substack/SKILL.md`** — etapa 8 (tabela), etapa 1 (nota de linha editorial), etapa 2
   (critério, remove opção `ilu-NN`, tira parágrafo de capa obrigatória), etapa 10 (inventário
   visual), "Os entregáveis".
4. **`revisao-editorial/SKILL.md`** — description, itens 4/9/10 (remove item 10 inteiro —
   checagem de paleta só fazia sentido para arquivo baseado em prompt; sem capa/ilustração,
   não sobra nenhum), renumera item 11→10, "Saída".
5. **`publicar/SKILL.md`** — passo 1 (completude) para de exigir `ilustracoes.md`.
6. **`marca-syntaxis/SKILL.md`** — tira bullet de "Quando usar" sobre prompt de imagem; ajusta
   bullet `illustration.*` para não apontar mais para `references/estilos-ilustracao.md`
   (arquivo apagado).
7. **`CLAUDE.md`** — Estrutura (`posts/<slug>/`) e a linha de entregáveis do pipeline.
8. **`README.md`** — diagrama de fluxo, tabela (linhas 2 e 8), passo 5 (copiar pra Substack),
   estrutura do repositório, frase de abertura.
9. **`PROJECT_DESCRIPTION.md`** — tira os dois bullets "Estilo de ilustração" (apontam para
   arquivo apagado).

## Não muda

`graficos.md`, `diagramas.md`, `checklist-graficos.md`, qualquer coisa em `posts/` já
publicado, `pesquisa/` histórico, `brand/`.
