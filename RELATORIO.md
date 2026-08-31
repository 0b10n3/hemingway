# Relatório de bootstrap — sistema editorial Syntaxis

Gerado ao final da Fase 4, 2026-08-10. Cobre o que foi construído, por quê, o que a
validação encontrou (incluindo um bug real), e o que fazer a seguir.

## O que foi criado

### `_arquivo/` — originais imutáveis
6 posts de Substack, 1 dissertação de mestrado (PDF, via Git LFS), 3 textos de Michael Lewis,
3 contos de Hemingway, 2 textos de Gladwell (os 8 últimos **não commitados** — copyright, ver
abaixo), `MARKETING_REVIEW.md`, e `MANIFESTO.md` documentando proveniência de cada item.

### `estilo/` — guia de voz
`estilo-autoral.md` (v1.0.0, aprovado pelo autor), `voz.fingerprint.json`,
`corpus-manifest.json` (hash SHA-256 de cada amostra própria), `CHANGELOG.md`,
`scripts/metricas.py` (camada quantitativa, Python puro), `metricas.json` (saída),
`extracoes/` (15 arquivos JSON — 7 próprias + 8 admiradas, o rastro de auditoria de cada
regra do guia).

### `.claude/` — o sistema operacional
7 skills (`voz-syntaxis`, `marca-syntaxis` — referência; `forja-de-voz`,
`revisao-editorial`, `prompts-visuais`, `post-substack`, `publicar` — tarefa, todas com
`disable-model-invocation: true`) e 5 subagentes (`extrator-de-estilo`,
`pesquisador-editorial`, `critico-editorial`, `revisor-gramatical`, `verificador-tecnico`).

### `pesquisa/` — as quatro frentes
Claude Code hoje (frontmatter confirmado contra doc oficial), estilometria (limiares de
evidência), editoração (fronteira das três camadas), antipadrões de IA em pt-BR (43 pares
❌/✅).

### `marca/tokens.json`
Reaproveitado do material fornecido (`initial/tokens.json`) — sistema "O Sinal no Escuro"
v2.1, não recriado.

## Decisões e razão

- **Copyright das amostras admiradas.** `REPO_PRIVADO = não` + amostras de Michael Lewis,
  Hemingway e Gladwell são texto protegido de terceiros → decisão do autor (Fase 0) de não
  commitar o texto-fonte. `.gitignore` cobre `_arquivo/amostras/admiradas/**/*.md`; só a
  extração (JSON, evidências ≤25 palavras) e a citação em `MANIFESTO.md` vão para o git.
  Quem clonar o repo do zero não terá os artigos completos em disco — só o resultado
  processado. Reprocessar exige buscar os textos de novo nas fontes listadas no manifesto.
- **Subagentes custom criados nesta sessão não ficam invocáveis por nome até reiniciar a
  sessão.** Confirmado duas vezes: `extrator-de-estilo` (Fase 2) e `voz-syntaxis` como skill
  (Fase 4, teste de disparo) — ambos deram erro "not found"/"Unknown skill" ao tentar invocar
  pelo nome na mesma sessão em que foram criados. Contornado na Fase 2 rodando as extrações
  via agente `general-purpose` com as mesmas instruções embutidas no prompt. **Isso significa
  que os testes de disparo, ponta a ponta, atualização e gênero (itens 1, 2, 4, 6 abaixo) só
  podem ser completados numa sessão nova.**
- **Duas vozes, não uma.** O achado mais importante da Fase 2: os posts de Substack se
  dividem em subgênero ensaístico e explicativo (§4 do guia). Isso veio da agregação cruzando
  as 6 extrações — nenhuma pediu isso explicitamente, mas a evidência era grande demais para
  ignorar (metade do corpus nunca usa 1ª pessoa nem humor; a outra metade sempre usa).
- **`marca/tokens.json` na raiz**, não dentro de `_arquivo/` nem de `.claude/` — é um
  artefato de sistema que evolui, não um original de leitura nem parte do pipeline de skills.
  Decisão minha, não especificada no meta-prompt original; documentada aqui por transparência.

## Limitações conhecidas

1. **Corpus abaixo do piso recomendado.** 6.742 palavras em 6 posts de Substack — a pesquisa
   de estilometria recomenda ~8 textos/~10.000 palavras para confiança alta. O autor aprovou
   seguir mesmo assim; `confianca_global: media` no guia reflete isso.
2. **Subgênero explicativo assenta em só 2 textos** (~2.000 palavras). Real, mas com margem
   de erro maior que o ensaístico (4 textos).
3. **Confiança "cross-gênero" pode estar inflada.** Regras confirmadas em Substack *e*
   dissertação têm o selo `[cross-gênero]` como sinal de força — mas convenções acadêmicas
   (Definição numerada, estrutura ABNT) são em parte impostas pelo gênero/orientador, não só
   escolha de voz. Registrado no guia, não resolvido.
4. **Regra "nunca negrito"** pode ser parcialmente artefato de conversão dos arquivos
   fornecidos (extrações repetidas sinalizaram perda de formatação markdown na origem), não
   só escolha do autor.
5. **Discrepância de contagem de palavras na dissertação**: 18.943 (leitura visual) vs.
   10.735 (pdftotext, usado em `metricas.json`) — fórmulas/símbolos LaTeX se perdem
   parcialmente na extração de texto puro. Documentado em `corpus-manifest.json`.
6. **Bug real encontrado pelo teste de imutabilidade (item 7 abaixo):**
   `_arquivo/MANIFESTO.md` foi editado (não só criado) num commit da Fase 1, para preencher
   placeholders "a preencher" com a proveniência de Hemingway/Gladwell. Isso viola a letra da
   regra "`_arquivo/` é imutável". Corrigido registrando uma exceção explícita e estreita em
   `CLAUDE.md`: `MANIFESTO.md` pode receber acréscimo/preenchimento de lacuna, nunca
   reescrita de linha já assentada sobre item existente. Nenhum outro arquivo de `_arquivo/`
   foi tocado — confirmado via `git log --diff-filter=MDR -- _arquivo/`.
7. **Teste do §9.4 do meta-prompt (blind com dois posts reais)** não foi refeito
   separadamente na Fase 4 — já tinha sido feito antes da aprovação do autor na Fase 2 (três
   pontos frágeis apontados então). O item 3 da checklist abaixo usa um teste equivalente
   (dois parágrafos novos, tema fora do corpus) para não repetir o mesmo exercício.

## Resultado dos 9 testes de validação (§9)

| # | Teste | Resultado |
|---|---|---|
| 1 | Disparo (3 frases por skill) | **Bloqueado nesta sessão** — skills criadas agora não estão na listagem carregada. Ver "Como completar" abaixo. |
| 2 | Ponta a ponta (transcrição real curta) | **Bloqueado nesta sessão**, mesma causa. |
| 3 | Cego de voz | ✅ Feito — dois parágrafos novos (CDB, tema fora do corpus), um por subgênero. Achado: o guia generaliza "anedota pessoal" mas perde a nuance de que a anedota do autor é sempre autobiográfica-intelectual (formação em matemática), nunca sobre terceiros genéricos — candidato a "Em observação" na próxima atualização. Registrado em `/tmp/.../teste-cego-voz.md` (scratchpad, não commitado — é rascunho de validação, não artefato do sistema). |
| 4 | Atualização (`/forja-de-voz atualizar` com amostra fora do padrão) | **Bloqueado nesta sessão**, mesma causa (skill de tarefa). |
| 5 | Idempotência | ✅ Passa — todos os 7 hashes de `corpus-manifest.json` batem com os arquivos atuais; uma nova rodada do bootstrap detectaria corretamente modo `auditoria`. |
| 6 | Gênero (post de Substack não herda traço de dissertação) | **Parcialmente verificável sem o pipeline** — o guia separa explicitamente §4.3 (acadêmico) de §4.1/§4.2 (Substack) e marca qual regra é `[cross-gênero]` vs. exclusiva de um gênero. Teste completo requer rodar `/post-substack`. |
| 7 | Imutabilidade | ⚠️ **Encontrou e corrigiu um bug real** — ver limitação 6 acima. |
| 8 | Reprodutibilidade dos gráficos | **Bloqueado** — nenhum post foi gerado ainda (depende do teste 2), então não há `graficos.md` para testar. |
| 9 | Este relatório | ✅ |

## Como completar os testes bloqueados

Abra uma sessão nova do Claude Code nesta pasta (`cd hemingway && claude`) e rode:

1. Três frases naturais por skill (ex. "escreve um post sobre Tesouro IPCA" deveria puxar
   `post-substack` sozinho, mesmo sem `/`) — confirme carregamento, ajuste `description` se
   não disparar.
2. `/post-substack _arquivo/transcricoes/<algo curto>.txt` — se não houver transcrição real
   ainda, este teste espera a primeira gravação real do autor.
3. `/forja-de-voz atualizar <amostra fora do padrão>` — confirme que cai em "ruído amostral".
4. Peça um post de Substack e confirme que a resposta não usa estrutura
   Definição/Teorema/Demonstração nem evita primeira pessoa por padrão.
5. Depois de um post real passar pela etapa 8, rode cada bloco de `graficos.md` num diretório
   limpo e confirme que gera o SVG sem editar nada.

## O que fazer quando o corpus crescer

- A cada ~5 posts novos publicados, rode `/forja-de-voz atualizar` (ver
  `.claude/skills/forja-de-voz/references/protocolo-de-atualizacao.md`).
- Assim que houver a primeira amostra de LinkedIn, rode `atualizar` mesmo com menos de 5
  posts — preenche uma lacuna estrutural do corpus (hoje não há como distinguir "traço geral"
  de "traço não-LinkedIn").
- Ao atingir ~8 posts de Substack / ~10.000 palavras próprias, reavalie `confianca_global`
  no frontmatter do guia — pode subir de `media` para `alta` se as regras atuais se
  confirmarem sem contradição.

## Acréscimo — auditoria de 2026-08-31 (`chore/auditoria-2026`)

Primeira auditoria do sistema desde o bootstrap acima, motivada por três posts publicados
desde então e pela virada de marca de 31/08 (`marca/tokens.json` aposentado em favor de
`../../brand/DESIGN.md` v2.0). Processo documentado em
`pesquisa/auditoria-2026/00-contexto.md` a `03-backlog.md`; cada fase é um ou mais commits
próprios (`git log --grep auditoria`).

### Fase 0 — Entendimento (`00-contexto.md`)

Confirmou o inventário (7 skills, 5 agentes, fonte única de cada coisa) sem deriva em
relação a este relatório. Levantou 4 achados reais a partir de evidência em
`posts/2026-08-25-.../` — nenhum hipotético.

### Fase 1 — Auditoria de skills e subagentes (`01-auditoria-skills.md`)

Veredito: **nenhuma skill/agente para substituir ou aposentar** — a separação de
responsabilidades entre `critico-editorial`/`revisor-gramatical`/`verificador-tecnico` se
confirmou limpa na prática. Dois ajustes aprovados e aplicados (commit `ea4ca90`):

1. `post-substack` instruía invocar a skill `publicar` diretamente na etapa 10, mas
   `publicar` tem `disable-model-invocation: true` de propósito (merge+tag+push é a ação de
   maior risco do repo) — texto corrigido para instruir `/publicar` manual.
2. `prompts-visuais/SKILL.md` resumia inline o método v1 de briefing de ilustração
   (superado); resumo removido em favor de apontar só para
   `references/briefing-ilustracao.md`, eliminando a categoria de bug (duas fontes do mesmo
   método), não só a instância.

Ponto registrado e **não decidido**: paralelizar as etapas 6 (linha/norma) e 7 (verificação
técnica), que hoje leem o mesmo `04-draft-v1.md` sem se citar. Não há evidência de retrabalho
que justifique o risco de edição concorrente no mesmo arquivo — ver `03-backlog.md`.

### Fase 2 — Evolução do processo visual (`02-processo-visual.md`)

A partir de dois precedentes reais (capa ad hoc pedida no gate humano de 08-25; um diagrama
disfarçado de ilustração pego manualmente em 08-17), formalizou quatro categorias de visual
com critério escrito (não gosto) na etapa 2: `graf-NN` (série numérica), `diag-NN` (relação
estrutural sem métrica), `ilu-NN` (metáfora do autor), `info-NN` (só quando nenhuma peça
isolada carrega a síntese — condicional, padrão é não ter). `capa.md` virou entregável novo,
obrigatório, separado de `ilustracoes.md` (evita a ambiguidade que exigiu aviso manual em
08-25). Diagramas usam Plotly (mesmo padrão de `graf-NN`), não Mermaid (dependência pesada
de Chromium) nem Graphviz (leve, mas layout genérico exigiria trabalho extra para bater a
fidelidade de marca já resolvida no padrão Plotly). Dimensão oficial de capa da Substack
ficou `[VERIFICAR]` — página de suporte bloqueou fetch automático (403); convenção adotada
enquanto isso (16:9, ≥2400×1350px) cobre com folga as fontes secundárias levantadas. Quatro
diffs aprovados e aplicados, um commit cada: `20c9ba2`, `3253fc6`, `beeeb38`, `e02640f`.

### Fase 3 — Consolidação

Sincronizou `CLAUDE.md` e `README.md` (este relatório incluído) com os entregáveis novos da
Fase 2, que só existiam em `.claude/skills/*/SKILL.md` até aqui. Backlog dos itens abertos
das Fases 1-2 em `pesquisa/auditoria-2026/03-backlog.md`. Smoke test dos skills de referência
(`voz-syntaxis`, `marca-syntaxis`) nesta sessão nova — ver resultado no próprio backlog ou na
sessão em questão.
