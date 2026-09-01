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
| 0 | Ingestão | principal | `00-transcricao.md` — cópia limpa (hesitação removida, palavras do autor preservadas) **e** inventário de marcadores do rascunho, se houver (ver "Etapa 0" abaixo). A crua fica intocada em `_arquivo/` |
| 1 | Briefing | principal + `voz-syntaxis` + `marca-syntaxis` | `01-briefing.md` — tese em uma frase; gancho escolhido (cena, dado ou pergunta que abre o texto — não é a mesma coisa que a tese); analogias usadas no áudio (preservar, são do autor); encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §5); qual voz (§4 do guia — ensaística ou explicativa); **qual linha editorial** (ver abaixo); resolução de todo marcador **estrutural** e **nota de conteúdo** do inventário da etapa 0 (ver "Etapa 0" abaixo) |
| 2 | Estrutura | principal | `02-estrutura.md` — subtítulos; o que cada seção prova; em qual ato do arco cada seção entra (setup/conflito/resolução, ou a versão completa — ver `.claude/skills/revisao-editorial/references/tecnicas-narrativas.md`); confirmação de que dado, narrativa e visual (os três pilares) estão cada um representados em pelo menos uma seção; onde entra `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` e por quê, pelo critério da seção "Etapa 2" abaixo; o que fica de fora |
| 3 | Pesquisa | agente `pesquisador-editorial` | `03-pesquisa.md` com fontes — tratamento do tema, dados, contrapontos |
| 4 | Draft | principal, com `voz-syntaxis` | `04-draft-v1.md` — toda **instrução de escrita** do inventário da etapa 0 aparece atendida, com nota lateral de como (ver "Etapa 0" abaixo) |
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

## Etapa 0 — o arquivo de origem é rascunho, não transcrição

O arquivo em `_arquivo/transcricoes/` nem sempre é fala de áudio limpa de hesitação — pode ser
um rascunho escrito pelo autor, com instruções para o próprio processo embutidas no texto
(caso real: `2026-09-01-quando-os-modelos-se-rebelam`, que já chegou com
`[LINHA EDITORIAL: Spoiler]`, `[CAPA: ...]` e notas como `[escrever um parágrafo sobre X]`).
Colchetes, ou qualquer outra marca visivelmente fora da prosa corrida, não são fala a limpar —
são ordem de serviço para o pipeline. A etapa 0 é a única que lê o arquivo cru inteiro, então é
dela a responsabilidade de não deixar nenhuma se perder.

Além da cópia limpa de sempre, `00-transcricao.md` ganha uma seção final **"Marcadores
extraídos do rascunho"** (vazia se o arquivo não tiver nenhum): cada marcador citado verbatim,
classificado por um destes quatro padrões observados no corpus real — não é taxonomia fechada
nem sintaxe obrigatória para o autor, é reconhecimento rápido do que já apareceu:

- **Estrutural** — decide algo do pipeline (`[LINHA EDITORIAL: ...]`). Resolvido na etapa 1.
- **Sugestão de visual** — ideia de capa ou ilustração, marcada (`[CAPA: ...]`) ou solta no
  corpo do texto sem marcador formal. Resolvida na etapa 8
  (`prompts-visuais/references/briefing-ilustracao.md`).
- **Instrução de escrita** — pede um trecho novo ou revisão de um existente
  (`[escrever um parágrafo sobre X]`, `[tentar reescrever o parágrafo acima]`). Resolvida na
  etapa 4.
- **Nota de conteúdo** — dado, fonte ou ressalva que o autor quer garantir que apareça, sem
  ditar a frase. Resolvida na etapa 1 ou 7, conforme o caso.

Cada marcador tem um campo "resolução", vazio nesta etapa e preenchido pela etapa que o
resolve. Nenhum marcador desaparece silenciosamente entre etapas: se a etapa responsável não
achar solução, ele vira tensão registrada como pergunta nomeada (ver Etapa 1 abaixo) — nunca é
descartado sem registro escrito de por quê.

## Etapa 1 — linha editorial é campo obrigatório

A Substack tem duas linhas (`PROJECT_DESCRIPTION.md` §Linhas Editoriais):

- **Spoiler** — carreira, relato de jornada pessoal, "spoiler" do que o leitor vai viver.
- **Notas de um Professor** — conceito, produto ou mecanismo explicado com rigor técnico.

O briefing declara a linha em uma seção própria (`## Linha editorial`), e ela é **decisão
separada da voz**: já houve post em voz ensaística que não era Spoiler
(`2026-08-25-dividir-para-nao-correr-risco`). Quando o texto não couber claramente em nenhuma
das duas, **registre a ambiguidade e leve ao gate humano (etapa 10)** — não decida sozinho.

**"Levar ao gate humano" significa uma pergunta nomeada, não uma frase dissolvida numa lista.**
Todo marcador **estrutural** ou **nota de conteúdo** do inventário da etapa 0 (ver acima) que
não tiver resolução clara nesta etapa vira, aqui, uma tensão registrada com essa mesma
exigência: um rótulo curto e uma pergunta do tipo "A ou B?" que a etapa 10 apresenta ao autor
separada de qualquer `[VERIFICAR]` técnico — nunca misturada na mesma lista de pendências. Foi
exatamente isso que faltou no post `2026-09-01-quando-os-modelos-se-rebelam`: a tensão entre a
linha "Spoiler" que o autor já havia declarado no rascunho e o assunto do texto (mais próximo,
pelo critério literal, de "Notas de um Professor") foi registrada em prosa no briefing e
acabou aprovada por inércia — carregada como item de uma lista de pendências genéricas até a
etapa 10, sem nunca virar, de fato, uma pergunta que alguém respondesse.

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

**Toda tensão estrutural registrada na etapa 1** (ver "Etapa 1" acima) aparece aqui como
pergunta própria, com rótulo (ex.: "Tensão — linha editorial") — nunca dissolvida dentro da
lista de `[VERIFICAR]` técnicos ou do inventário visual. Se houver mais de uma tensão, cada
uma vira uma pergunta separada; não resuma várias em uma só.

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
