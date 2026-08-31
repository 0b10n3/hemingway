# Fase B — Proposta

Cada item abaixo corresponde a um achado de `00-diagnostico.md`. Onde o diagnóstico não
encontrou problema real, o item é "sem ação necessária" — não invento diff para preencher.

Classificação de risco usada:
- **Baixo (documentação/regra):** edita texto de documentação/relatório, não muda
  comportamento de skill/agente, reversível trivialmente.
- **Médio (comportamento de skill/agente):** muda o que uma skill instrui ou como um agente
  age; precisa ser testado antes de dar como concluído.
- **Aprovação item a item (posts/`_arquivo` já publicados):** toca conteúdo que já foi
  publicado — por regra do `CLAUDE.md` ("Nada de sobrescrita silenciosa"), cada um destes
  precisa da sua aprovação explícita e separada, não um "sim" geral para a Fase C.

---

## 1. Post `2026-08-10` publicado fora do fluxo git

**Achado:** branch `post/2026-08-10-o-mundo-invertido-dos-investimentos` completa,
aprovada no gate humano, nunca mergeada/tageada. O post já circula na Substack. Stash órfão
associado (`wip: re-render graf-01.svg`).

**Proposta — duas decisões independentes, cada uma pedindo sua aprovação:**

**1a. Registrar a publicação retroativamente (recomendado) ou deixar como exceção documentada.**
- *Opção A (recomendada):* rodar exatamente o passo a passo de `publicar/SKILL.md` contra
  essa branch — `git checkout main && git merge --no-ff post/2026-08-10-...`, depois
  `git tag publicado/2026-08-10-o-mundo-invertido-dos-investimentos`. Não altera nenhum
  conteúdo já escrito (post, figuras, processo) — só faz o git refletir um fato que já é
  público. `git diff --stat` já confirmado: 60 arquivos, todos dentro de
  `posts/2026-08-10-.../`, nenhum conflito esperado com os 3 posts publicados depois (slugs
  diferentes).
- *Opção B:* não mexer no git; só documentar a exceção em `RELATORIO.md` (acréscimo).
- **Risco:** aprovação item a item (mexe em `posts/` e no histórico de branches de um post
  já público) — preciso do seu "sim" específico para esta operação antes da Fase C, com a
  opção escolhida.

**1b. Stash órfão** (`wip: re-render graf-01.svg (unrelated to CDB post)`): aplicar,
descartar, ou deixar como está. Não tenho contexto suficiente para saber se esse trabalho
ainda é desejado — pergunta direta a você, não decido.

---

## 2. `revisao-editorial` item 10 — isenção de paleta pressupõe execução runtime não testada

**Achado:** o item isenta `graficos.md`/`diagramas.md` da checagem mecânica de paleta porque
"o código lê `tokens.json` em runtime" — mas nenhuma etapa do pipeline roda esse código.

**Proposta (baixo risco, documentação — não é redesenho do processo de visuais):** adicionar
uma frase ao item 10 de `.claude/skills/revisao-editorial/SKILL.md` deixando explícito que a
isenção pressupõe que **o autor rode o bloco Python manualmente** antes de aprovar a figura no
gate humano — a checagem mecânica do item verifica só ausência de cor hardcoded no texto do
prompt/código, não que o código de fato execute. Não estou propondo automatizar essa
execução dentro do pipeline (isso seria redesenho do processo de visuais, fora do escopo
combinado) — só fechar a lacuna entre o que o texto do item promete e o que ele de fato
verifica.

**Risco:** baixo — é uma frase de esclarecimento em um arquivo de skill, não uma ferramenta
nova nem um passo novo do pipeline.

---

## 3. Duas figuras não commitadas em `2026-08-14`

**Achado:** `figuras/ilu-01.jpg` e `.png` untracked; `08-17` estabeleceu a prática de
commitar arte final (só um formato, `.jpeg`).

**Proposta:** perguntar a você qual formato manter (`.jpg`, `.png`, ou os dois) antes de
commitar — não decido isso sozinho. Depois de você escolher, o commit em si é uma ação
mecânica (`git add` + `git commit`) sobre um post já publicado.

**Risco:** aprovação item a item (toca `posts/2026-08-14-.../`, já publicado) — preciso da
sua escolha de formato antes de eu tocar nisso na Fase C.

---

## 4. `confianca_global` — sem ação necessária, só registro de distância medida

**Achado:** `confianca_global: media` continua correto; faltam ~4-5 posts / ~4.000-4.900
palavras para o gatilho que `RELATORIO.md` já previa.

**Proposta:** nenhuma mudança em `estilo/estilo-autoral.md`. Registrar a contagem real (3
posts, 5.936 palavras, distância medida) como acréscimo em `RELATORIO.md`, na seção "O que
fazer quando o corpus crescer" — sem reescrever o que já está lá, só somar o dado novo.

**Risco:** baixo (RELATORIO.md é registro de auditoria, não guia operacional).

---

## 5. E-mail do autor e nome completo expostos publicamente

**Achado:** e-mail em todo commit; nome completo do autor + nome do orientador de mestrado
em `_arquivo/MANIFESTO.md`, já público em `origin/main`.

**Proposta:** não há diff de código a propor — são duas perguntas diretas para você decidir,
porque qualquer ação teria custo desproporcional ao problema:
- **E-mail:** mudar `git config user.email` afeta só commits *futuros* (não reescreve
  histórico). Se você quiser um e-mail diferente daqui pra frente, é uma linha de config —
  mas só faço se você confirmar que quer isso, e não mexo no histórico já público sem pedido
  explícito (reescrever histórico é exatamente o tipo de operação que `CLAUDE.md` proíbe sem
  perguntar).
- **Nome no MANIFESTO.md:** `_arquivo/` é imutável por regra, e a única exceção documentada
  é *acrescentar* linha, nunca reescrever uma já preenchida — então mesmo que você decida que
  o nome não deveria estar lá, a correção não é uma edição simples, é uma exceção à regra de
  imutabilidade que precisaria ser negociada à parte. Não proponho nada aqui além de
  confirmar com você se a exposição é aceitável (dado que `REPO_PRIVADO = não` já foi decisão
  consciente) ou se meritia essa conversa separada.

**Risco:** nenhuma ação de código proposta — decisão pura do autor.

---

## 6. `origin/main` 13 commits atrás do `main` local

**Achado:** commits pendentes de push são só sistema/processo (`.claude/skills/`,
`pesquisa/`, `RELATORIO.md`) — nenhum post novo, nenhum dado de `_arquivo/`.

**Proposta:** nenhum diff — é só a pergunta de quando você quer rodar `git push origin main`.
Não vou fazer isso na Fase C sem pedido explícito nesse momento (push para repo público é
ação visível a terceiros, entra na lista de "sempre confirmar antes").

**Risco:** nenhuma ação de código proposta — timing é decisão do autor.

---

## Itens sem ação necessária (achados da Fase A que não viram diff)

- **Disparo por frase natural** (1.1): as 7 skills disparam/bloqueiam corretamente. Nenhuma
  mudança de `description` ou `disable-model-invocation` necessária.
- **Referências mortas** (seção 2): nenhuma nova encontrada além do `marca/tokens.json` já
  conhecido e já com política decidida ("correção vale só daqui pra frente" — `CLAUDE.md`).
  Não retroajo essa política.
- **Branches `post/<slug>`** (3.2): preservadas corretamente, nenhuma ação.
- **Tags `publicado/*` vs. `posts/`** (3.3): batem 1:1 exceto o caso do item 1 acima, já
  tratado.
- **`.gitignore`** (3.4): cobertura confirmada por execução real, nenhuma ação.
- **`allowed-tools` das 7 skills** (4.1): cobrem a responsabilidade atual, inclusive as duas
  que ganharam escopo novo na revisão de visuais. Nenhuma ferramenta faltando.
- **`disable-model-invocation` das 7 skills** (4.2): todos os 7 flags continuam corretos.
  Confirmado que o Achado 1 da `auditoria-2026` (texto de `post-substack` etapa 10) já foi
  corrigido — nenhuma ação nova.
- **Sobreposição entre os 3 agentes de revisão** (4.3): separação limpa confirmada com
  evidência real dos 3 posts. Nenhuma ação.
- **`extrator-de-estilo` dormente** (4.4): esperado, corpus de amostras admiradas não
  cresceu. Nenhuma ação — não crio trabalho para um agente sem motivo para rodar.
- **Sincronia de `README.md`/`CLAUDE.md`/`RELATORIO.md`** (seção 5): confirmada, a conclusão
  da `frente-e-visuais` de que não precisava diff ainda vale no critério em que foi formulada
  (entregável de primeiro nível, não mecanismo interno). Nenhuma ação.
- **CPF/RG real nos posts** (6.3): nenhuma ocorrência real encontrada, só menções genéricas
  ao FGC. Nenhuma ação.

---

## Resumo do que precisa da sua aprovação item a item antes da Fase C

1. Post `2026-08-10`: opção A (merge+tag retroativo) ou opção B (só documentar)?
2. Stash órfão: aplicar, descartar, ou deixar parado?
3. Figuras de `2026-08-14`: manter `.jpg`, `.png`, ou os dois — e então commitar?
4. E-mail do autor: mudar `git config user.email` para commits futuros, ou manter?
5. Nome no `MANIFESTO.md`: aceitável como está, ou quer abrir essa conversa à parte (fora do
   escopo desta auditoria, já que envolve negociar a regra de imutabilidade)?
6. Push de `main` para `origin/main`: agora, ou depois?

Os itens 2 (nota no `revisao-editorial`) e 4 (acréscimo em `RELATORIO.md` sobre
`confianca_global`) são baixo risco e eu seguiria com eles assim que você confirmar o pacote
geral — mas prefiro sua confirmação explícita antes de abrir a branch, já que envolvem editar
arquivo de skill e de relatório.
