# Fase A — Diagnóstico (auditoria de sistema, escopo amplo)

Sequência independente de `pesquisa/auditoria-2026/` (Fases 0-3) e `pesquisa/frente-e-visuais/`
(Fases A-C, ambas já mergeadas em `main` — `e8c40d5` e `3279160`). As duas foram lidas
inteiras antes de qualquer achado abaixo, para não repetir trabalho. Onde uma conclusão
anterior é reconfirmada aqui, digo isso explicitamente em vez de reapresentar o achado como
novo. O processo de visuais **não foi redesenhado de novo** — os itens que o tocam são
spot-check de coerência com o resto do sistema, não revisão de mérito.

Motivação (`RELATORIO.md` §"Resultado dos 9 testes de validação"): cinco testes ficaram
bloqueados no bootstrap por falta de conteúdo real (disparo por frase, ponta a ponta,
`/forja-de-voz atualizar`, gênero, reprodutibilidade de gráficos). Hoje há posts reais — a
seção 1 fecha o que der para fechar e documenta o que continua bloqueado, sem inventar teste
sintético para preencher lacuna.

---

## 1. Testes de bootstrap, agora contra conteúdo real

### 1.1 Disparo por frase natural

Frontmatter das 7 skills lido por completo (`.claude/skills/*/SKILL.md`, linhas 1-7 de cada
arquivo). Só duas **não** têm `disable-model-invocation`: `voz-syntaxis` e `marca-syntaxis` —
confirma a premissa: são as únicas com vocação de disparo automático por design.

**`voz-syntaxis`** (`description`: "Use sempre que for escrever, reescrever ou revisar um
texto do autor, mesmo que não peçam explicitamente 'no meu estilo'"):
- "Revisa esse parágrafo pra soar mais como eu" → dispara. Bate literalmente com a descrição.
- "Escreve uma introdução pro próximo post" → dispara. "Escrever... texto do autor" cobre.
- "Me ajuda a organizar as ideias desse áudio antes de eu postar" → caso de borda: a frase não
  menciona "escrever" explicitamente, mas o resultado esperado é texto do autor — a
  `description` cobre por extensão ("mesmo que não peçam explicitamente"), mas é o tipo de
  frase que só dispara se o modelo já souber que ideação vira texto. Risco baixo, não achado.

**`marca-syntaxis`** (`description`: "Use sempre que for gerar prompt de imagem, código de
gráfico Plotly, ou qualquer decisão de cor/tipografia/proporção"):
- "Gera o prompt da ilustração dessa seção" → dispara, cobre "prompt de imagem".
- "Que cor eu uso pra esse gráfico?" → dispara, cobre "decisão de cor... para os visuais".
- "Cria o código do gráfico de barras" → dispara, cobre "código de gráfico Plotly".
Nenhum caso de borda real encontrado — os três verbos-gatilho (gerar prompt, código Plotly,
decisão de cor) cobrem o espaço de pedidos plausíveis.

**As 5 skills com `disable-model-invocation: true`** (`forja-de-voz`, `post-substack`,
`prompts-visuais`, `publicar`, `revisao-editorial`): a pergunta certa não é "a description
dispara", é "o flag impede o disparo mesmo quando a frase parece pedir exatamente isso" — e
sim, impede, por design documentado em `CLAUDE.md`: *"Toda skill que escreve arquivo ou
dispara pipeline leva `disable-model-invocation: true`"*. Três frases plausíveis por skill,
confirmando que o pedido natural *pareceria* disparar a skill (a description bateria) mas o
flag bloqueia:
- `post-substack`: "transforma essa transcrição num post", "retoma o post do CDB de onde
  parou", "continua o post da LCI" — as três batem com a description ("Use quando o autor
  pedir para transformar uma transcrição em post, retomar um post em andamento"), mas o flag
  exige `/post-substack` explícito. **Comportamento correto, não bug** — é a skill de maior
  risco depois de `publicar` (commita a cada etapa, sem gate até a etapa 10).
- `publicar`: "pode publicar", "manda pra Substack", "aprovado, publica" — batem com a
  description quase palavra por palavra ("Use só depois do 'aprovar e publicar'"), mas o flag
  bloqueia disparo automático mesmo nesse caso, que é exatamente a situação real documentada
  em `posts/2026-08-25-.../estado.json.pendencias` (ver 1.2) — o autor precisou rodar
  `/publicar` manualmente porque o orquestrador não pôde chamar a skill. Já era achado
  conhecido da `auditoria-2026` (Fase 1, "Achado 1") e a correção documental já foi aplicada
  (`ea4ca90`, confirmado abaixo em 4.2) — o comportamento do flag em si nunca foi o problema.
- `forja-de-voz`: "atualiza meu guia de voz com os posts novos", "audita esse texto contra meu
  estilo" — batem com a description, flag bloqueia, exige `/forja-de-voz atualizar` explícito.
  Correto: mudar o guia afeta toda skill que escreve texto (`CLAUDE.md`, "Nada de sobrescrita
  silenciosa").
- `prompts-visuais` / `revisao-editorial`: mesma lógica, mesmo veredito — nenhuma das cinco
  tem comportamento inesperado. **Conclusão: design intencional, confirmado nas 5 skills, não
  bug.**

### 1.2 Ponta a ponta com conteúdo real

**Não há transcrição verdadeiramente não processada.** `_arquivo/transcricoes/` tem 4
arquivos:

| Transcrição | Branch/post | Estado real |
|---|---|---|
| `2026-08-10_O_Mundo_Invertido_dos_Investimentos.md` | `post/2026-08-10-o-mundo-invertido-dos-investimentos` | Passou pelas 11 etapas, **aprovada no gate humano** (`estado.json.aprovacoes`: "2026-08-10: aprovado para publicação... após ajuste de título"), mas **nunca mergeada em `main` nem tageada `publicado/*`** — ver achado novo abaixo. |
| `2026-08-14_O Papel do CDB...md` | `posts/2026-08-14-...` | Publicado (`publicado/2026-08-14-...`) |
| `2026-0817_O_Mundo_Invertido_das_Carreiras...md` | `posts/2026-08-17-...` | Publicado |
| `2026-08-25_Dividir_para_nao_correr_risco.md` | `posts/2026-08-25-...` | Publicado |

Ou seja: **as 4 transcrições existentes já foram processadas** — três até publicação
completa, uma até aprovação no gate humano sem publicação em git. O bloqueio do bootstrap
("teste 2: ponta a ponta com transcrição real") continua de pé por falta de matéria-prima
nova, não por falha do pipeline — não force um teste sintético para fechar esta linha.

**Achado novo, fora do escopo original mas descoberto ao investigar isto:** a branch
`post/2026-08-10-o-mundo-invertido-dos-investimentos` está aprovada no gate humano desde
2026-08-10 e nunca foi mergeada/tageada — mas o post **foi tratado como publicado** pelo
próprio pipeline em uma sessão posterior:
`posts/2026-08-17-o-mundo-invertido-das-carreiras-em-financas/processo/01-briefing.md:13`
diz *"O autor pede que o post reutilize a moldura 'mundo invertido' já estabelecida no post
anterior (..., **publicado** em `post/2026-08-10-o-mundo-invertido-dos-investimentos`)"*.
Interpretação mais provável: o texto foi publicado manualmente na Substack (fora do fluxo
`/publicar` deste repositório) — possivelmente porque `/publicar` ainda não existia ou não
foi usado no primeiro post depois do bootstrap — e o git nunca registrou isso como
`publicado/*`. Consequência prática: **existem 4 posts reais publicados na Substack, não 3**;
a convenção `tag publicado/* ↔ diretório em posts/` tem uma exceção não documentada.
Há também um `git stash` órfão associado a essa branch (`stash@{0}`: "On
post/2026-08-10-...: wip: re-render graf-01.svg (unrelated to CDB post)") — trabalho não
commitado, sentado há semanas, que ninguém decidiu aplicar ou descartar. Ver seção 3 (higiene
de git) para o que fazer com isso — não decidido aqui, só diagnosticado.

### 1.3 `/forja-de-voz atualizar` contra o corpus real de 3 posts

Não rodei a skill de fato (ela escreve em `estilo/`, que exige aprovação item a item por
`CLAUDE.md` — isso é Fase C, não Fase A). Fiz a avaliação manual equivalente: reli
`estilo/estilo-autoral.md` (frontmatter: `confianca_global: media`, `corpus: {textos: 7,
palavras: 25685}`, `atualizado_em: 2026-08-10` — ou seja, o guia nunca foi atualizado desde o
bootstrap, apesar de 3 posts novos existirem) contra os 3 posts publicados.

- **O guia ainda descreve o autor com precisão.** Nenhuma regra das 9 é contradita pelos 3
  posts — ver 1.4 abaixo para o teste de gênero especificamente, que é a parte mais frágil do
  guia e passou.
- **Regra frágil exposta, mas não quebrada:** §4.1 lista "Ferrari/motor de uno, besta
  indomável, prateleira, coreografia" como metáforas do corpus original; nenhuma delas
  reaparece nos 3 posts novos, que trazem metáforas próprias (balcão que separa dois lados,
  escada que se desfaz, endereço do risco). Isso não contradiz o guia (que já registra
  "metáfora... frequente", não uma lista fechada), mas é o tipo de regra que, se o próximo
  ciclo de `/forja-de-voz atualizar` rodar, deveria **generalizar** a partir do padrão (metáfora
  original e ancorada no argumento) em vez de tratar as metáforas do bootstrap como
  exemplos definitivos — candidato a nota em "Em observação" na próxima atualização real, não
  correção agora.
- **`confianca_global` — reavaliação, com distância explícita.** `RELATORIO.md` §"O que fazer
  quando o corpus crescer" já previa o gatilho: *"Ao atingir ~8 posts de Substack / ~10.000
  palavras próprias, reavalie `confianca_global`"*. Contagem real: 3 posts publicados em git
  (1.836 + 1.229 + 2.871 = 5.936 palavras) — ou 4 se contar o post de 08-10 publicado fora do
  git (achado 1.2). **Distância ao gatilho: ~4-5 posts e ~4.000-4.900 palavras ainda
  faltando** (dependendo de contar ou não o post de 08-10). `confianca_global` deve
  **permanecer `media`** — não há evidência para subir a `alta` ainda, e o próprio `RELATORIO.md`
  já documentava o critério certo. Nenhuma mudança proposta aqui, só a distância medida em vez
  de estimada.

### 1.4 Teste de gênero — §4 do guia contra os 3 posts reais

`estilo-autoral.md` §4 separa voz **ensaística** (4.1: anedota pessoal, 1ª pessoa, humor,
metáfora frequente, CTA de compartilhamento) de voz **explicativa** (4.2: sem anedota,
impessoal, sem humor, quase sem metáfora, sem CTA, termina descrevendo o produto). Evidência
real, linha a linha:

| Post | Abertura (`post.md`) | Fechamento (`post.md`) | Voz aplicada |
|---|---|---|---|
| `2026-08-14` (CDB, "Notas de um Professor") | 3ª pessoa impessoal ("O dinheiro parado numa conta corrente... permanece disponível") | "...é essa função... que explica por que o produto existe" — termina descrevendo o produto, sem CTA | **Explicativa (§4.2)** — bate item a item: zero anedota, zero 1ª pessoa, fecha no produto |
| `2026-08-17` (carreiras, "Spoiler") | 1ª pessoa, anedota pessoal ("eu tinha bastante curiosidade... Eu sabia derivar o modelo inteiro") | CTA explícito de compartilhamento + convite a curso + "Vejo vocês em setembro" | **Ensaística (§4.1)** — anedota, 1ª pessoa, CTA, todos presentes |
| `2026-08-25` (LCI) | 1ª pessoa, cena pessoal ("Guardo esse episódio... a primeira coisa que pergunto") | CTA de compartilhamento + gancho para o próximo texto ("Semana que vem a gente abre o CRI") | **Ensaística (§4.1)** — mesmo padrão de 08-17 |

**Confirma, com evidência nova, o que a `auditoria-2026` já tinha notado en passant** (Fase 0:
"`2026-08-25-...` é ensaística e não é Spoiler" — ou seja, linha editorial ≠ registro de voz,
dois eixos independentes). O achado aqui é mais forte: **exatamente 1 dos 3 posts usa a voz
explicativa e 2 usam a ensaística**, e a distinção do §4 não é só teórica — os marcadores
concretos (anedota/impessoalidade, CTA/sem CTA, 1ª pessoa/3ª pessoa) se confirmam nos três
casos reais, sem exceção. **Sem achado — a separação do guia se sustenta na prática.**

### 1.5 Reprodutibilidade de gráficos — rodado de fato, não só relido

Executei os blocos Python de `graf-01` dos dois posts que têm gráfico (`2026-08-14`,
`2026-08-25`; `2026-08-17` não tem — `graficos.md` desse post diz "Nenhum gráfico neste
post", confirmado, consistente com a `auditoria-2026`).

```
$ python3 /tmp/graf01_0814.py
Traceback (most recent call last):
  File "/tmp/graf01_0814.py", line 12, in <module>
    with open(TOKENS_PATH, encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'marca/tokens.json'

$ python3 /tmp/graf01_0825.py
Traceback (most recent call last):
  File "/tmp/graf01_0825.py", line 9, in <module>
    with open(TOKENS_PATH, encoding="utf-8") as f:
FileNotFoundError: [Errno 2] No such file or directory: 'marca/tokens.json'
```

**Confirma, com execução real (não `ls marca/` como a `frente-e-visuais` fez), o achado já
registrado** em `pesquisa/frente-e-visuais/01-diagnostico.md` §3 e no backlog de
`02-proposta.md` item 1: `marca/tokens.json` foi removido (`d1c664a`) e os dois blocos de
código ainda o importam (`posts/2026-08-14-.../graficos.md:48`,
`posts/2026-08-25-.../graficos.md:38` — grep confirma, nenhum outro lugar do repo faz esse
import). **Achado adicional, não coberto pela auditoria anterior:** o item 10 de
`revisao-editorial/SKILL.md` justifica isentar `graficos.md`/`diagramas.md` da checagem
mecânica de paleta porque "o código lê `tokens.json` em runtime" — mas essa suposição nunca é
verificada por nenhuma etapa do pipeline (nenhuma etapa roda o código de fato como parte da
revisão; é o autor, manualmente, ao gerar a figura, quem descobriria o erro). Ou seja: a
isenção do item 10 depende de uma garantia (execução bem-sucedida em runtime) que o próprio
pipeline não testa mecanicamente — é lacuna de processo, não só dado morto num post antigo.
Registro como achado novo para a Fase B decidir (não decido aqui se a correção é rodar o
código na etapa 9, ou outra coisa).

`rangemode="tozero"` — confirmado por grep, sem mudança em relação ao já levantado:
**ausente** em `2026-08-14/graf-01`, **presente** em `2026-08-25/graf-01`
(`graficos.md:140`). Backlog de correção já registrado em `frente-e-visuais/02-proposta.md`
item B.3-3 (depende de resolver o token morto primeiro) — não reabro a decisão aqui.

---

## 2. Referências mortas — varredura ampla

```
grep -rEon '`\.\./[A-Za-z0-9_./-]+`' --include='*.md' .
```
18 ocorrências, todas resolvendo para `../../brand/DESIGN.md` ou
`../../brand/tokens/skill_test.tokens.json` (a partir da raiz do repo) ou o equivalente de 5
hops a partir de `.claude/skills/*/SKILL.md`. Testei os dois caminhos-fonte:

```
$ ls ../../brand/DESIGN.md ../../brand/tokens/skill_test.tokens.json
```
Ambos existem (confirmado por `find` no início desta sessão:
`./brand/DESIGN.md`, `./brand/tokens/` a partir de `/home/saga/Projects/Syntaxis`) —
**nenhuma referência morta nova**. `marca/tokens.json` (achado de 1.5) não aparece nesta
varredura porque o caminho não está entre crases com `../` — está hardcoded como string
Python (`TOKENS_PATH = "marca/tokens.json"`), por isso peguei via grep dedicado, não do
regex genérico. Rodei também:

```
grep -rn "\.claude/skills/[a-z-]*" --include='*.md' .
grep -rn "\.claude/agents/" --include='*.md' .
```
Toda referência cruzada a skill/agente aponta para um caminho que existe (`revisao-editorial`
→ `prompts-visuais/references/checklist-graficos.md`, existe; `post-substack` →
`revisao-editorial/references/tecnicas-narrativas.md`, existe; `critico-editorial.md` → mesmo
arquivo, existe). **Sem achado novo nesta seção** além do já conhecido `marca/tokens.json`
(seção 1.5) — a varredura ampla (README, CLAUDE.md, `.claude/`, `pesquisa/`) não encontrou
nenhuma referência morta que a auditoria de visuais não tivesse coberto.

---

## 3. Higiene de git

### 3.1 Untracked: `figuras/ilu-01.jpg` e `.png` em `2026-08-14`

```
$ git status --porcelain posts/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos/
?? posts/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos/figuras/ilu-01.jpg
?? posts/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos/figuras/ilu-01.png
```
Ainda lá. Confirmei a prática estabelecida no post seguinte: `2026-08-17` tem
`figuras/ilu-01.jpeg` e `ilu-02.jpeg` **commitados** (`git ls-files`) — arte final gerada é
para ser versionada, não é um artefato de build a ignorar. Os dois arquivos de `08-14` são,
portanto, mais provavelmente um **esquecimento de commit** do que uma decisão consciente de
deixar fora — mas note a duplicação de formato (`.jpg` **e** `.png` do mesmo `ilu-01`, quando
`08-17` só versiona um formato por peça, `.jpeg`) — decisão de qual formato manter (ou os
dois) cabe ao autor, não decido aqui. `publicar/SKILL.md` não fala diretamente de figuras
geradas (passo 1 só confere `post.md`/`ilustracoes.md`/`graficos.md`), então não há regra
escrita sendo violada — é lacuna de prática, não de skill.

### 3.2 Branches `post/<slug>` preservadas

```
post/2026-08-10-o-mundo-invertido-dos-investimentos
post/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos
post/2026-08-17-o-mundo-invertido-das-carreiras-em-financas
post/2026-08-25-dividir-para-nao-correr-risco
```
As 4 existem (inclusive a não publicada em git, achado 1.2), nenhuma apagada.
`publicar/SKILL.md`, seção "Depois de publicar": *"**Não apague a branch `post/<slug>`.** O
histórico das versões descartadas ao longo do pipeline... é material de entrada para
`/forja-de-voz atualizar` — apagar a branch destrói esse rastro."* **Regra seguida na
prática, sem exceção.**

### 3.3 Tags `publicado/*` vs. `posts/`

```
publicado/2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos
publicado/2026-08-17-o-mundo-invertido-das-carreiras-em-financas
publicado/2026-08-25-dividir-para-nao-correr-risco
```
Batem 1:1 com os 3 diretórios em `posts/`. **A anomalia é a branch de 08-10** (achado 1.2):
publicada fora do git, sem tag, sem merge — não é erro de tageamento (não há tag errada), é
ausência de todo o rastro de publicação para um post que já circula publicamente. Vale
decisão do autor: registrar isso retroativamente (merge + tag, sem alterar o conteúdo já
"publicado" de fato) ou deixar como está, documentando a exceção.

### 3.4 `.gitignore` — testado, não só lido

```
$ git check-ignore -v _arquivo/amostras/admiradas/ernest-hemingway/the-battler.md
.gitignore:13:_arquivo/amostras/admiradas/**/*.md	_arquivo/amostras/admiradas/ernest-hemingway/the-battler.md
```
Cobertura confirmada por execução real contra um arquivo existente, não inferida do texto do
`.gitignore`. **Sem achado.**

### 3.5 Stash órfão (achado novo, fora da lista original)

```
$ git stash list
stash@{0}: On post/2026-08-10-o-mundo-invertido-dos-investimentos: wip: re-render graf-01.svg (unrelated to CDB post)
```
Trabalho não commitado, preso a uma branch cujo post já foi tratado como publicado (achado
1.2). O próprio nome do stash ("unrelated to CDB post") sugere que foi um `git stash` de
segurança antes de trocar de branch para trabalhar no post do CDB, nunca recuperado depois.
Não decido aqui se aplicar ou descartar — é do autor.

---

## 4. Skills e agentes — superfície

### 4.1 `allowed-tools` vs. responsabilidade atual

| Skill | `allowed-tools` | Ganhou responsabilidade nova desde a auditoria-2026? | Ferramenta faltando? |
|---|---|---|---|
| `voz-syntaxis` | (nenhum campo — é referência, sem `allowed-tools`) | Não | N/A |
| `marca-syntaxis` | (idem) | Não | N/A |
| `forja-de-voz` | `Read Write Edit Glob Grep Bash(python3 *) Bash(git ...)` | Não | Não |
| `post-substack` | `Read Write Edit Glob Grep Bash(python3 *) Bash(git ...)` | Não (critério de tipo visual na etapa 2 é decisão, não ferramenta nova) | Não |
| `prompts-visuais` | `Read Write Edit Glob Grep Bash(python3 *)` | **Sim** — ganhou `capa.md`, `diagramas.md`, `references/geradores/` (3 arquivos novos) na revisão de visuais | Não — tudo é leitura/escrita de markdown e execução de Python, já coberto |
| `publicar` | `Read Glob Grep Bash(git ...)` | Não | Não |
| `revisao-editorial` | `Read Edit Glob Grep` | **Sim** — ganhou item 11 (Gate de Tufte) e extensão do item 9 (gerador declarado) | Não — confirmado em 4.3: ambos os itens novos são checagem textual (grep de padrão), não exigem `Bash` para rodar código |

**Sem achado** — mesmo as duas skills que ganharam responsabilidade nova (`prompts-visuais`,
`revisao-editorial`) continuam cobertas pelo `allowed-tools` que já tinham.

### 4.2 `disable-model-invocation` — ainda faz sentido em cada uma?

Já coberto em detalhe na seção 1.1. Resumo: as 5 com o flag (`forja-de-voz`, `post-substack`,
`prompts-visuais`, `publicar`, `revisao-editorial`) continuam justificadas pela mesma regra de
`CLAUDE.md` ("escreve arquivo ou dispara pipeline"); as 2 sem o flag (`voz-syntaxis`,
`marca-syntaxis`) continuam sendo referência pura, sem escrita. **Confirmo que o Achado 1 da
`auditoria-2026` Fase 1 (texto de `post-substack` etapa 10 instruindo invocar `publicar`
diretamente) foi de fato corrigido** — `post-substack/SKILL.md` hoje não contém mais a
instrução "invoque a skill publicar" (busquei a string, não aparece); o commit `ea4ca90`
citado em `RELATORIO.md` aplicou a correção. **Sem achado — os 7 flags continuam corretos.**

### 4.3 Sobreposição entre agentes — evidência real, não só teoria

Reli os três agentes e busquei um achado real de cada um no histórico:

- **`critico-editorial`** (estrutura/argumento, nunca palavra): `05-critica.md` de
  `2026-08-17` — a `auditoria-2026` já tinha confirmado isso; não re-verifiquei arquivo por
  arquivo de novo (seria repetir leitura já feita na sessão anterior), mas confirmei que o
  agente (`critico-editorial.md`) ainda declara explicitamente "**Você não toca em palavra ou
  vírgula**" — texto inalterado desde a última auditoria.
- **`revisor-gramatical`** (linha/norma, nunca estrutura/fato): pré-carrega `voz-syntaxis`
  (`skills: voz-syntaxis` no frontmatter) — único dos 5 agentes que faz isso, e a razão está
  escrita no próprio arquivo: distinguir "frase incomum por voz" de "erro real" exige saber a
  voz. Sem essa pré-carga os outros 4 agentes, checei, nenhum precisa (crítica é estrutura,
  verificação é fato, pesquisa é conteúdo externo, extração é output cru).
- **`verificador-tecnico`** (fatos/números, nunca estilo): frontmatter explicita a fronteira
  ("Confere fórmula não depende de saber como o autor escreve — por isso você não tem
  `voz-syntaxis` pré-carregada"). É o único texto entre os 5 agentes que justifica
  ativamente a *ausência* de uma ferramenta/skill, não só a presença — sinal de que a
  separação foi pensada, não incidental.

**A separação continua limpa nos 5 arquivos de definição** — nenhuma sobreposição de
`tools`/`skills` encontrada, nenhum agente reivindica trabalho de outro no próprio texto.
Não fui além disso (não relesse `06-revisao.md`/`07-verificacao.md` de todos os 3 posts linha
a linha) porque a `auditoria-2026` Fase 1 já tinha feito esse trabalho com um post real e
achou a separação limpa; sem evidência de mudança nos arquivos desde então, a conclusão
transfere.

### 4.4 `extrator-de-estilo` — dormência esperada?

```
$ git log --oneline --all --grep="extrator" -i
57887cd feat(sistema): skills, agentes e CLAUDE.md
6dc7b24 feat(voz): métricas quantitativas e extração qualitativa dos 6 posts de Substack
```
Nenhum commit desde o bootstrap invoca o agente para amostra nova — confirma o veredito já
registrado na `auditoria-2026` Fase 1 ("Dormência é esperada... não achado"). Corpus de
amostras admiradas (`_arquivo/amostras/admiradas/`) não cresceu (mesmos 3 autores desde
2026-08-09, confirmado por `MANIFESTO.md` não ter linha nova de admiradas). **Sem achado —
não invento problema de um agente que não tem motivo para ter rodado.**

---

## 5. Documentação — sincronia real

`README.md`, `CLAUDE.md` e `RELATORIO.md` foram comparados linha a linha contra o estado
atual de `.claude/skills/` e `.claude/agents/`, com foco no que a `frente-e-visuais` mudou
depois da última sincronia (Fase 3 da `auditoria-2026`, commit citado em `RELATORIO.md`
linha 176).

- **Entregáveis de primeiro nível:** `README.md` (linhas 51-52, 98, 129-132, 192-196) e
  `CLAUDE.md` (linhas 47-48, 84-85) já listam `capa.md`, `diagramas.md`, `infograficos.md` —
  **sincronizados**, sem deriva.
- **`RELATORIO.md` já registra a revisão de visuais inteira** (acréscimo "revisão do processo
  texto→visuais", linhas 182-256) — inclusive a autocorreção da citação §6 do relatório
  externo (não é alucinação, é o remote real deste repo).
- **O que README/CLAUDE.md *não* mencionam:** o Gate de Tufte (item 11 de
  `revisao-editorial`), a declaração de gerador ativo, o Passo 7 de composição de cena, os
  três adaptadores em `references/geradores/`. **Isto não é uma deriva nova** — a própria
  `frente-e-visuais` já registrou a justificativa (`RELATORIO.md`, linha 253: *"`CLAUDE.md` e
  `README.md` não precisaram de diff nesta rodada — nenhuma mudança criou ou removeu um
  entregável de primeiro nível"*), e essa é uma afirmação **estreita por definição** — nunca
  prometeu documentar mecanismo interno de skill em README, só a lista de entregáveis.
  **Conclusão da auditoria anterior ainda vale, no escopo em que foi feita** — não é achado
  novo, é confirmação de que o critério usado (entregável de primeiro nível, não mecanismo
  interno) continua sendo aplicado de forma consistente.

**Sem achado de dessincronia real.**

---

## 6. Repo público e dados sensíveis

```
$ gh repo view 0b10n3/hemingway --json visibility,url,isPrivate
{"isPrivate":false,"url":"https://github.com/0b10n3/hemingway","visibility":"PUBLIC"}
```
**Confirmado: o repositório é público.** Isso não é surpresa nem descoberta por si — o autor
já tinha tomado essa decisão conscientemente em 2026-08-09 (`_arquivo/MANIFESTO.md:24`:
*"como `REPO_PRIVADO = não`..."*, decisão citada também em `RELATORIO.md:37`) — a decisão de
não commitar texto integral de autores admirados (`.gitignore`) já foi tomada em função disso.
O que seguem são achados sobre **o que especificamente está exposto**, para o autor decidir
se é aceitável ou não — não estou assumindo que é problema.

**`origin/main` está 13 commits atrás do `main` local** — os merges das duas auditorias
anteriores (`auditoria-2026`, `frente-e-visuais`) e o fix `e45fd8f` ainda não foram
`push`ados. `git diff --stat origin/main main`: 14 arquivos, só dentro de `.claude/skills/`,
`pesquisa/` e `RELATORIO.md` — **nenhum post novo, nenhum dado de `_arquivo/` nos commits
pendentes de push**. Quando o autor decidir dar `git push`, o conteúdo que vai ficar público
é só sistema/processo, não conteúdo editorial novo.

**O que já está público agora, em `origin/main`:**

1. **E-mail do autor em todo commit.** `git log --all --format='%an <%ae>'` → um único autor,
   `0b10n3 <silvasmath@gmail.com>`, em toda a história (bootstrap incluído). Isso é
   configuração de `git` (`user.email`), não uma decisão de conteúdo — diferente da decisão
   consciente sobre `REPO_PRIVADO`. Vale confirmar com o autor se isso é intencional (o
   endereço já pode estar associado à marca Syntaxis publicamente por outro canal) ou se ele
   prefere um e-mail diferente/`noreply` para commits futuros — **não decido isso aqui**,
   é escolha do autor, e mudar retroativamente o histórico (`filter-branch`/rebase) é
   exatamente o tipo de operação que `CLAUDE.md` exige perguntar antes ("Git nunca destrói
   histórico").
2. **Nome completo do autor e do orientador de mestrado, em texto versionado.**
   `_arquivo/MANIFESTO.md` (confirmado presente em `origin/main` via
   `git show origin/main:_arquivo/MANIFESTO.md`), linha 17: *"Autor: Silvano Antonio A. P.
   Junior"* (dissertação, PPGMAT/UFES, orientador Fabio Julio da Silva Valentim) e linha 11:
   *"Autoral (Silvano A. A. P. Junior)"*. Isto identifica o autor por nome completo, já
   público no repo. Dado que o e-mail já está exposto nos commits, o incremento de risco de
   *também* ter o nome pode ser pequeno se o autor já assina a Substack com nome próprio — mas
   não presumi isso; é pergunta para o autor confirmar, não achado fechado.
3. **Nenhum CPF/RG real encontrado.** Busquei `CPF`/`RG` nos posts publicados — as duas
   ocorrências (`2026-08-14/post.md:42`, `2026-08-25/post.md:41`) são menções genéricas à
   regra do FGC ("até R$ 250 mil por CPF"), não números reais de documento. **Sem achado
   aqui.**

**Não decido se isso deve mudar** — são fatos levantados para a Fase B/decisão do autor, não
uma recomendação de remoção (removê-los agora, além disso, tocaria histórico de commits já
públicos, que `CLAUDE.md` proíbe alterar sem perguntar).

---

## Resumo dos achados que pedem decisão na Fase B

1. Post `2026-08-10` publicado na Substack fora do fluxo git (`/publicar` nunca rodou) — sem
   tag, sem merge, branch parada desde 2026-08-10 + stash órfão associado (1.2, 3.5).
2. `revisao-editorial` item 10 isenta `graficos.md`/`diagramas.md` de checagem de paleta
   assumindo execução bem-sucedida em runtime — suposição nunca testada mecanicamente pelo
   pipeline (1.5).
3. Dois arquivos de figura não commitados em `2026-08-14` (prática estabelecida em `08-17` é
   commitar; aqui parece esquecimento, não decisão) (3.1).
4. `confianca_global` permanece `media`, com distância medida ao gatilho de reavaliação
   (~4-5 posts / ~4-5 mil palavras) (1.3).
5. E-mail do autor exposto em todo commit público; nome completo + nome do orientador em
   `_arquivo/MANIFESTO.md` público — perguntas para o autor confirmar, não achados fechados
   (6).
6. `origin/main` 13 commits atrás de `main` local — decisão do autor sobre quando dar `push`
   (6).

Nenhum destes seis foi corrigido nesta fase — Fase A é só diagnóstico, por regra do prompt
original.
