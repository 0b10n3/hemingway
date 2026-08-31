---
name: post-substack
description: Pipeline completo de transcrição de áudio a post publicável no Syntaxis, com verificação técnica, visuais e commit por etapa. Use quando o autor pedir para transformar uma transcrição em post, retomar um post em andamento, ou continuar o trabalho de um slug existente em posts/.
disable-model-invocation: true
argument-hint: [caminho-da-transcrição-em-_arquivo/ | slug-existente-em-posts/]
allowed-tools: Read Write Edit Glob Grep Bash(python3 *) Bash(git add *) Bash(git commit *) Bash(git status *) Bash(git diff *) Bash(git log *) Bash(git checkout -b *) Bash(git branch *)
---

Orquestrador do sistema. Roda na sessão principal (não em subagente) porque a etapa 10 é um
gate humano — um subagente em background não consegue perguntar nada.

## Invocação

- `/post-substack _arquivo/transcricoes/2026-08-10_titulo.txt` — começa um post novo.
- `/post-substack <slug>` — retoma um post existente a partir de `posts/<slug>/estado.json`,
  na última etapa concluída.

## Primeiro ato: branch e estado

Se é post novo: `git checkout -b post/<slug>` a partir de `main` (slug = data + título
resumido em kebab-case). Crie `posts/<slug>/estado.json`:

```json
{
  "etapa_atual": 0,
  "loops_consumidos": 0,
  "aprovacoes": [],
  "pendencias": [],
  "commit_inicial": "<sha curto de main no momento da criação>"
}
```

Se é retomada: `git checkout post/<slug>` e leia `estado.json` para saber onde continuar.
**Nunca refaça uma etapa já marcada concluída sem que o gate humano (etapa 10) tenha pedido
isso explicitamente** — é assim que o pipeline sobrevive a `/clear` e à retomada no dia
seguinte.

## As onze etapas

Ordem fixa: primeiro o que muda estrutura (5), depois o que muda frase (6), por último o que
muda letra (7) — inverter significa revisar gramática de parágrafo que a etapa 5 ainda vai
cortar (ver `pesquisa/frente-c-editoracao.md`).

| # | Etapa | Executor | Saída em `posts/<slug>/processo/` |
|---|---|---|---|
| 0 | Ingestão | principal | `00-transcricao.md` — cópia limpa (hesitação removida, palavras do autor preservadas). A crua fica intocada em `_arquivo/` |
| 1 | Briefing | principal + `voz-syntaxis` + `marca-syntaxis` | `01-briefing.md` — tese em uma frase; gancho escolhido (cena, dado ou pergunta que abre o texto — não é a mesma coisa que a tese); analogias usadas no áudio (preservar, são do autor); encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §5); qual voz (§4 do guia — ensaística ou explicativa); **qual linha editorial** (ver abaixo) |
| 2 | Estrutura | principal | `02-estrutura.md` — subtítulos; o que cada seção prova; em qual ato do arco cada seção entra (setup/conflito/resolução, ou a versão completa — ver `.claude/skills/revisao-editorial/references/tecnicas-narrativas.md`); confirmação de que dado, narrativa e visual (os três pilares) estão cada um representados em pelo menos uma seção; onde entra `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` e por quê, pelo critério da seção "Etapa 2" abaixo; o que fica de fora |
| 3 | Pesquisa | agente `pesquisador-editorial` | `03-pesquisa.md` com fontes — tratamento do tema, dados, contrapontos |
| 4 | Draft | principal, com `voz-syntaxis` | `04-draft-v1.md` |
| 5 | Crítica estrutural | agente `critico-editorial` | `05-critica.md` — diagnóstico com severidade por item, não reescreve |
| 6 | Linha e norma | agente `revisor-gramatical` | `06-revisao.md` — diff comentado, não toca estrutura |
| 7 | Verificação técnica | agente `verificador-tecnico` | `07-verificacao.md` — veredito por item, fórmulas recalculadas |
| 8 | Visuais | skill `prompts-visuais` | `08-briefing-visual.md` (conceito de cada `ilu-NN`, com os descartes) + rascunho consolidado em `capa.md`, `ilustracoes.md`, `graficos.md`, `diagramas.md` e, condicional, `infograficos.md` |
| 9 | Consolidação | skill `revisao-editorial` | aplica 5+6+7, emite os entregáveis finais (ver "Os entregáveis" abaixo) |
| 10 | **Gate humano** | principal | apresenta o post, o que mudou, pendências `[VERIFICAR]`; **para e espera** |

Cada etapa: grava seu arquivo em `processo/`, atualiza `estado.json.etapa_atual`, **commita**
(`feat(<slug>): <nome da etapa>`). Etapas com subagente: push depois do commit (trabalho caro,
não vale perder).

**Se a etapa 5 devolver severidade alta** (tese frágil, seção que não prova o que promete),
volte à etapa 2 antes de seguir, e avise o autor — não maqueie problema estrutural na etapa 6.

## Etapa 1 — linha editorial é campo obrigatório

A Substack tem duas linhas (`PROJECT_DESCRIPTION.md` §Linhas Editoriais):

- **Spoiler** — carreira, relato de jornada pessoal, "spoiler" do que o leitor vai viver.
- **Notas de um Professor** — conceito, produto ou mecanismo explicado com rigor técnico.

O briefing declara a linha em uma seção própria (`## Linha editorial`), e ela é **decisão
separada da voz**: já houve post em voz ensaística que não era Spoiler
(`2026-08-25-dividir-para-nao-correr-risco`). Quando o texto não couber claramente em nenhuma
das duas, **registre a ambiguidade e leve ao gate humano (etapa 10)** — não decida sozinho.

A linha escolhida vai para o frontmatter de `post.md` como `linha_editorial:` na etapa 9, e é
o que determina o **estilo artístico das ilustrações** na etapa 8
(`prompts-visuais/references/estilos-ilustracao.md`). Sem esse campo, a etapa 8 para e
pergunta.

## Etapa 2 — ilustração, gráfico, diagrama ou infográfico: critério, não gosto

Para cada ponto que a etapa 2 decidir que precisa de visual, decida o tipo por este critério,
nesta ordem — e registre em `02-estrutura.md` por que os outros três perderam:

1. Há série numérica real a comparar/mostrar trajetória? → **`graf-NN`**.
2. Não há série, mas há relação estrutural entre entidades, fluxo, processo ou linha do tempo
   sem métrica central? → **`diag-NN`**. Sinal de que devia ser isto e não `ilu-NN`: se o
   conceito se resolve em formas geométricas comparadas — duas linhas, dois blocos — sem um
   objeto concreto do texto por trás, é diagrama fantasiado de ilustração. Já aconteceu:
   `posts/2026-08-17-o-mundo-invertido-das-carreiras-em-financas/ilustracoes.md`, revisão de
   `ilu-02`.
3. Nenhuma das duas, mas o texto tem metáfora/analogia/imagem própria do autor que carrega
   argumento? → **`ilu-NN`**, via `prompts-visuais/references/briefing-ilustracao.md`.
4. Só considere **`info-NN`** se nenhuma peça isolada acima carregar a síntese sozinha — ver
   critério de gatilho em `prompts-visuais/SKILL.md`. Padrão: não tem infográfico.

Toda ideia visual do post tem, além disso, uma **capa** obrigatória (`capa.md`) — não é uma
opção da lista acima, é item separado e sempre presente, especificado na etapa 8 a partir da
tese e do gancho de `01-briefing.md` (não do corpo do texto).

## Etapa 10 — gate humano

Use `AskUserQuestion` com três saídas: **aprovar e publicar**, **ajustar**, **abortar**.

- Aprovar → informe o autor que a publicação requer `/publicar` manual (a skill tem
  `disable-model-invocation: true` de propósito — merge, tag e push são ação de alto risco
  demais para disparo automático).
- Ajustar → pergunte o que mudar, reentre no **ponto mais raso que resolve o pedido**:
  - reentrada na etapa 4 ou anterior → **consome um loop** (o texto está sendo refeito);
  - reentrada nas etapas 5-9 → **não consome** (é acabamento, é para isso que o gate serve).
  Registre a reentrada em `estado.json` (`ponto_retorno`, `motivo`, incrementa
  `loops_consumidos` só se aplicável).
- Esgotado `MAX_LOOPS_REVISAO` (3 por padrão): entregue o estado atual com um resumo honesto
  do que não convergiu e o que o autor precisaria decidir para destravar. **Nunca aprove por
  conta própria.**
- Abortar → deixa a branch `post/<slug>` como está (não deleta — histórico de versões
  descartadas alimenta o modo `atualizar` da forja de voz), avisa o autor onde ela ficou.

Antes do `AskUserQuestion`, apresente também o **inventário visual do post**: status da capa
(gerada/pendente) e a lista de `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` com tipo e status — o
autor decide com o inventário completo à vista, não só com o texto.

## Os entregáveis (etapa 9, na raiz de `posts/<slug>/`)

**`post.md`** — texto revisado, frontmatter (título, subtítulo, data, `linha_editorial`, tags,
status), placeholders `![Ilustração: ...](ilu-NN)` / `![Gráfico: ...](graf-NN)` /
`![Diagrama: ...](diag-NN)` / `![Infográfico: ...](info-NN)` com alt-text descritivo.
**`capa.md`** — sempre presente, uma capa por post, especificada a partir de
`01-briefing.md`, não do corpo. **`ilustracoes.md`**, **`graficos.md`** e **`diagramas.md`** —
presentes quando o post tiver a peça correspondente. **`infograficos.md`** — só quando o
critério de gatilho do infográfico se aplicar (padrão: não existe). Ver skill
`prompts-visuais` para o formato exato de cada um.

## Regras que valem para toda etapa

- `_arquivo/` nunca é editado (ver `CLAUDE.md`).
- Número, fonte, fórmula ou citação sem verificação vira `[VERIFICAR: ...]` — nunca invente.
- Cada subagente devolve só um laudo (arquivo em `processo/`) — o transcript sujo dele não
  entra no contexto principal.
- Nada de sobrescrita silenciosa: retomar um slug existente sempre mostra o que já foi feito
  antes de prosseguir.
