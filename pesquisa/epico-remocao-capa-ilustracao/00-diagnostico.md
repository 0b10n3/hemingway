# Diagnóstico — remoção de capa e ilustração do pipeline

Pedido do autor (2026-09-09): tirar a etapa de criação de capa e ilustração do `hemingway`.
`graficos.md`, `diagramas.md` e `infograficos.md` continuam existindo, sem mudança de
comportamento. Capa/ilustração devem virar peça de um projeto próprio no futuro — este épico
não cria esse projeto, só remove a etapa daqui.

## O que hoje gera capa/ilustração

- `.claude/skills/prompts-visuais/SKILL.md` — seções `## capa.md` e `## ilustracoes.md`
  (formato, briefing obrigatório, regra de negative prompt).
- `.claude/skills/prompts-visuais/references/`: `briefing-ilustracao.md`,
  `estilos-ilustracao.md`, `templates-prompt.md`, `exemplos-prompts.md`,
  `checagem-graos.md`, `checagem-paleta.md`, `geradores/*.md` (3 arquivos) — todos exclusivos
  de capa/ilustração, nenhum é usado por `graficos.md`/`diagramas.md`
  (`checklist-graficos.md` é o único arquivo de `references/` que sobrevive).

## Quem depende disso, fora do skill que gera

- `post-substack/SKILL.md`: etapa 8 (saída inclui `capa.md`/`ilustracoes.md`), etapa 1
  (nota sobre linha editorial não determinar mais estilo de ilustração), etapa 2 (critério
  de escolha inclui `ilu-NN`), etapa 10 (inventário visual cita status da capa), seção "Os
  entregáveis" (lista `capa.md`/`ilustracoes.md` e placeholder `ilu-NN`).
- `revisao-editorial/SKILL.md`: description, item 4 (placeholders), item 9 (inventário
  visual completo cita capa/gerador), item 10 (grep de hex em `capa.md`/`ilustracoes.md` +
  checagem de pixel via `checagem-paleta.md`), seção "Saída".
- `publicar/SKILL.md`: passo 1 confere `ilustracoes.md` antes de publicar.
- `marca-syntaxis/SKILL.md`: bullet "Quando usar" cita prompt de imagem para
  `GERADOR_IMAGEM`; bullet `illustration.*` aponta para `references/estilos-ilustracao.md`
  (arquivo que sai).
- `CLAUDE.md`, `README.md`, `PROJECT_DESCRIPTION.md` — documentação do pipeline para humano,
  citam `capa.md`/`ilustracoes.md` como entregável fixo.

## Fora de escopo

- Posts já publicados (`posts/2026-*/capa.md`, `ilustracoes.md`) — registro do que foi feito,
  mesma regra de `_arquivo/`: não se maquia (`CLAUDE.md`). Não tocar.
- `pesquisa/epico-*` e `pesquisa/frente-e-visuais/` anteriores — histórico de pesquisa que
  justificou o sistema de ilustração; não tocar, é registro, não instrução ativa.
- `brand/DESIGN.md`, `brand/tokens/`, `brand/ILUSTRACOES/` — repositório separado, usado por
  mais de um projeto; a camada `illustration.*` de lá não é escopo deste épico.
- Criação do "projeto específico" de capa/ilustração — não pedido agora ("por hora").

## Risco

Baixo — só texto de skill/doc, nenhum comportamento de código (Python/Plotly) muda.
`graficos.md`/`diagramas.md` não são tocados.
