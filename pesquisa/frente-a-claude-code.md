# Frontmatter válido para Agent Skills e Subagentes — Claude Code (agosto de 2026)

Pesquisa feita em 2026-08-09 contra a documentação oficial em `code.claude.com/docs/en/skills.md` e `code.claude.com/docs/en/sub-agents.md`, com conteúdo lido diretamente do fetch (não de memória). Versão instalada de referência: 2.1.226 — as tabelas abaixo indicam quando um campo é mais novo que isso.

## 1. SKILL.md — frontmatter

| Campo | Válido | Nota | Fonte |
|---|---|---|---|
| `name` | Sim | Opcional; default = nome do diretório. Em skill pessoal/projeto só define o rótulo de exibição, não o comando. Não pode conter `:`. | skills.md §Frontmatter reference |
| `description` | Sim (recomendado) | Não é tecnicamente obrigatório, mas sem ele Claude não sabe quando aplicar a skill. Se omitido, usa o primeiro parágrafo do corpo. | skills.md §Frontmatter reference |
| `disable-model-invocation` | Sim | Aceita `true/false` (e desde v2.1.218 também `yes/no/on/off/1/0`, case-insensitive). Ver seção 4. | skills.md §Control who invokes a skill |
| `argument-hint` | Sim | Texto de autocomplete, ex. `[issue-number]`. | skills.md §Frontmatter reference |
| `allowed-tools` | Sim | Sintaxe: string separada por espaço/vírgula ou lista YAML. Exemplo real da doc: `allowed-tools: Bash(git add *) Bash(git commit *) Bash(git status *)`. **Confirmado: o wildcard é `nome *` (espaço + asterisco), não `nome:*`.** Grant vale só no turno que invoca a skill. | skills.md §Pre-approve tools for a skill |
| `context: fork` | Sim, existe | Roda a skill como subagente forkado (isolado, sem histórico da conversa). Roda em background por padrão. | skills.md §Run skills in a subagent |
| `background` | Sim, mas só combinado com `context: fork` | `false` faz esperar o resultado no mesmo turno em vez de rodar em background. Requer v2.1.218+. | skills.md §Run skills in a subagent |
| `paths` | Sim | Glob patterns (string separada por vírgula ou lista YAML) que restringem quando a skill é auto-carregada, conforme os arquivos em jogo. | skills.md §Frontmatter reference |
| `model`, `effort`, `agent`, `hooks`, `shell`, `metadata`, `license`, `compatibility`, `disallowed-tools`, `when_to_use`, `arguments`, `user-invocable` | Sim, todos existem | Não pedidos originalmente, mas documentados. Destaque: `disallowed-tools` remove ferramentas do pool enquanto a skill está ativa; `user-invocable: false` esconde do menu `/` mas Claude ainda pode invocar. | skills.md §Frontmatter reference |
| Injeção dinâmica `` !`comando` `` | Sim, no corpo do SKILL.md | Roda o shell antes de enviar o conteúdo a Claude; a saída substitui o placeholder. Funciona também em skills com `context: fork`. | skills.md §Inject dynamic context |
| Orçamento de contexto para a listagem de descriptions | Documentado com fórmula | Não é um número fixo por skill: o orçamento total da listagem é **1% da janela de contexto do modelo** (configurável via `skillListingBudgetFraction`, ex. `0.02`). Dentro disso, cada entrada (`description` + `when_to_use`) tem um teto individual de **1.536 caracteres**, configurável via `skillListingMaxDescChars`. Quando estoura, Claude Code corta as descriptions das skills menos usadas primeiro. `/doctor` estima o custo real. | skills.md §Skill descriptions are cut short |

## 2. Subagentes (`.claude/agents/*.md`) — frontmatter

| Campo | Válido | Nota | Fonte |
|---|---|---|---|
| `name` | Sim, obrigatório | Minúsculas e hífen; não pode conter `:`. | sub-agents.md §Supported frontmatter fields |
| `description` | Sim, obrigatório | Usado para decidir delegação automática. | sub-agents.md §Supported frontmatter fields |
| `tools` | Sim | Campo é literalmente `tools` (não `allowed-tools`, que é exclusivo de skills). String separada por vírgula/espaço ou lista YAML. Se omitido, herda todas as ferramentas disponíveis para subagentes. | sub-agents.md §Supported frontmatter fields |
| `model` | Sim | Aceita `sonnet`, `opus`, `haiku`, `fable`, ID completo, ou **`inherit`** (confirmado). Default é `inherit`. Desde v2.1.196, `CLAUDE_CODE_SUBAGENT_MODEL=inherit` equivale a não setar a variável. | sub-agents.md §Choose a model |
| `effort` | Sim, existe | Aceita `low/medium/high/xhigh/max`, dependendo do modelo. Não existe campo `reasoning_effort`. | sub-agents.md §Supported frontmatter fields |
| `disallowedTools` (camelCase) | Sim, existe | Denylist; se ambos `tools` e `disallowedTools` estiverem presentes, `disallowedTools` é aplicado primeiro e depois `tools` é resolvido sobre o que sobrou. Também aceita padrões de MCP (`mcp__servidor`, `mcp__*`). | sub-agents.md §Available tools |
| `permissionMode`, `maxTurns`, `skills`, `mcpServers`, `hooks`, `memory`, `background`, `isolation`, `color`, `initialPrompt` | Sim, todos existem | `isolation: worktree` dá cópia isolada do repo; `skills` pré-carrega conteúdo completo (não só a description) no startup. | sub-agents.md §Supported frontmatter fields |

### Restrição a somente-leitura — garantia real ou convenção?

**É garantia real do sistema, não só convenção.** A doc é explícita: com `tools: Read, Grep, Glob, Bash`, "o subagente não pode editar arquivos, escrever arquivos, ou usar nenhuma ferramenta MCP". Há também um filtro adicional automático e obrigatório: subagentes que rodam em background (default desde v2.1.198) têm o conjunto de ferramentas nativas reduzido a uma lista fixa (`Read, Grep, Glob, Bash, PowerShell, Edit, Write, NotebookEdit, WebFetch, WebSearch, TodoWrite, Skill, ToolSearch, ...`) independentemente do que está em `tools:` — isto é aplicado pelo runtime, não pelo modelo. Se `tools:` não resolver nenhuma ferramenta válida, o subagente falha ao iniciar (erro nomeando as entradas não resolvidas), em vez de rodar sem restrição.
Fonte: sub-agents.md §Available tools.

## 3. Limite de tamanho do SKILL.md

**Confirmado, é documentado e explícito**, não é estimativa da comunidade: a doc traz uma dica textual — "Keep `SKILL.md` under 500 lines. Move detailed reference material to separate files." Uma skill referencia arquivos de suporte (`reference.md`, `examples.md`, `scripts/`) descrevendo-os no corpo do SKILL.md sob um cabeçalho tipo "## Additional resources", para que Claude saiba o que cada arquivo contém e quando carregá-lo (via leitura sob demanda com a ferramenta Read, ou script executado sem carregar seu conteúdo).
Fonte: skills.md §Add supporting files.

## 4. `disable-model-invocation: true`

Confirmado exatamente como assumido: impede que Claude invoque a skill automaticamente — só o usuário via `/nome` pode acioná-la. Adicionalmente: a description da skill deixa de entrar no contexto (economiza espaço); a skill não é pré-carregada em subagentes; e (desde v2.1.196) também impede que a skill rode quando uma tarefa agendada (scheduled task) a dispara como prompt. Se Claude tentar mesmo assim, Claude Code bloqueia a chamada e instrui o modelo a não reproduzir os passos manualmente.
Fonte: skills.md §Control who invokes a skill.

## Divergências do que foi assumido

- **Sintaxe de wildcard em `allowed-tools`**: a premissa inicial (`Bash(git add *)`) estava correta — é exatamente o exemplo oficial da doc. Uma pesquisa preliminar de um subagente auxiliar sugeriu erroneamente que a sintaxe correta seria `Bash(nome:*)` (dois-pontos) — isso **não é confirmado pela doc oficial** e foi descartado; não usar essa forma.
- **Orçamento de contexto das descriptions não é um número fixo por skill** — é uma fração do context window do modelo (1%, configurável), com teto individual de 1.536 caracteres por entrada. Não existe um "orçamento em tokens por skill" fixo documentado além disso.
- **`allowed-tools` não é exclusivo de skills** — subagentes usam o campo `tools` (mais `disallowedTools` para denylist), com semântica e nome diferentes; não confundir os dois.
- **Subagentes em background têm um segundo filtro automático de ferramentas nativas** (lista fixa, independente de `tools:`), algo não previsto nas premissas originais — importante para quem depende de Bash/outras ferramentas nativas específicas em subagentes "sujos" que rodam em background.
- O limite de ~500 linhas por SKILL.md não é uma regra rígida imposta pelo sistema, é uma recomendação de estilo na doc — mas é uma recomendação explícita e oficial, não estimativa de terceiros.

## Fontes

- https://code.claude.com/docs/en/skills.md
- https://code.claude.com/docs/en/sub-agents.md
