# Fase A — Diagnóstico do processo texto → visuais

Fonte teórica: `pesquisa/frente-e-visuais/relatorio-design-editorial-ia.md` (relatório
"Design Editorial, Semiótica Visual e Automação de Ilustrações via IA"), tratado como
pesquisa a destilar — números e specs marcados abaixo continuam `[VERIFICAR]` até
confirmação em fonte oficial atual (Fase B).

**Aviso de contexto, antes dos cinco testes:** este diagnóstico não parte do zero. A
`pesquisa/auditoria-2026/` (Fases 0–3, merge `e8c40d5`) já rodou nesta mesma sessão de
trabalho e já entregou boa parte do que um redesenho pediria — `capa.md` como entregável
obrigatório, a etapa 8a de briefing (`briefing-ilustracao.md`), o sistema de dois estilos por
linha editorial (`estilos-ilustracao.md`), o critério escrito de `graf-NN`/`diag-NN`/`ilu-NN`/
`info-NN` na etapa 2. O que os cinco testes abaixo encontram, portanto, não é ausência de
processo — é a **defasagem entre o sistema novo (documentado, válido a partir de 31/08/2026) e
os três posts publicados antes dele**, que não foram e não deveriam ser regenerados
(`CLAUDE.md`: registro do que foi feito não se maquia). Essa defasagem é o material real deste
diagnóstico.

Posts existentes em `posts/`: `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos` (Notas de
um Professor), `2026-08-17-o-mundo-invertido-das-carreiras-em-financas` (Spoiler, por
conteúdo — ver teste 3), `2026-08-25-dividir-para-nao-correr-risco` (linha ambígua, caso já
documentado). Nenhum dos três tem `processo/08-briefing-visual.md` nem `capa.md` — os dois
nasceram depois deles.

---

## 1. Teste de literalismo

Critério do relatório (§3): o *Literal Superiority Bias* faz modelos generativos colapsarem
ao processar abstração direta; a mitigação é a cadeia semente-do-autor → operação (extensão/
cruzamento/torção) → cena. `briefing-ilustracao.md` já formaliza exatamente essa cadeia — mas
só existe desde hoje. Os três posts publicados foram gerados sem ela. Resultado:

### `2026-08-14-.../ilustracoes.md`, `ilu-01`

Prompt real: *"a minimal circular or diamond glyph... a thin luminous thread/beam flows
rightward... a central geometric structure — a vertical dark monolith..."* — fio de luz que
atravessa um monólito genérico representando "o banco". O texto do post usa a expressão **"o
outro lado do balcão"** como título de seção (`post.md`, seção "O outro lado do balcão: o CDB
como passivo do banco") — a semente de Camada 1 que `briefing-ilustracao.md` exigiria colher
primeiro. A ilustração publicada não usa essa imagem: usa nó-fio-monólito, um vocabulário que
serviria para qualquer texto sobre "transformação financeira dentro de uma instituição" —
reprova no **teste da troca** do próprio método novo (`briefing-ilustracao.md`, Passo 5). É
também exatamente o padrão de "metáfora de dicionário" que o método lista como erro recorrente
(fio de luz genérico ≈ engrenagem, ampulheta).

Achado de controle: `references/exemplos-prompts.md` já contém, para este mesmo post, um
conceito de validação que usa o balcão em corte técnico — construído *depois* do post
publicado, como peça de teste do método novo, não como substituto do publicado.

### `2026-08-17-.../ilustracoes.md`, `ilu-01`

Prompt real: escada espelhada onde a metade inferior "**visibly coming apart the farther it
gets from the line — edges dissolving into a faint drifting particulate texture**". Isto é o
erro nomeado, com este exato exemplo, em `briefing-ilustracao.md` ("Como este método chegou
aqui"): *"foi o erro da 1ª rodada, onde a escada se desfazia em partículas: virou fatalidade,
e o post não é sobre catástrofe, é sobre ordem trocada com conserto disponível."* O post
termina com a promessa de conserto ("dá para voltar e preencher o alicerce depois") — a peça
publicada desenha decomposição, não conserto. Reprova no **teste da fatalidade** (Passo 5) tal
como o próprio método relata.

### `2026-08-17-.../ilustracoes.md`, `ilu-02`

Prompt real: árvore em corte, copa cheia e brilhando, raiz curta que não alcança o "bedrock".
`briefing-ilustracao.md`, seção "Erros recorrentes", lista literalmente: *"Árvore com copa
cheia e raiz curta | Metáfora de dicionário, e já tinha sido a escolha fraca da 1ª rodada"* —
é a mesma peça, hoje classificada pelo próprio sistema como o exemplo canônico de metáfora de
dicionário a evitar.

### `2026-08-25-.../ilustracoes.md`, Capa A e Capa B

Duas peças abstratas (fio casa→monólito; certificado fatiado com uma faixa acesa) — mais
próximas de diagrama conceitual do que de metáfora ancorada em Camada 1, porque o post não tem
uma imagem própria do autor equivalente ao *Upside Down* ou ao balcão (é o post
estruturalmente mais taxonômico dos três, por decisão registrada em `ilustracoes.md`: "o
argumento é estrutural/taxonômico... não construído em torno de uma imagem sustentada"). Não é
erro do mesmo tipo que os dois acima — é um caso onde a Camada 1 é mais fraca no próprio texto,
e a peça reflete isso honestamente. Ainda assim, "certificado se dividindo em faixas" está
próximo do território que `briefing-ilustracao.md` chamaria de solução geométrica pura sem
objeto de Camada 2 — candidato a reexame quando este post passar pela cadeia nova.

**Veredito do teste 1:** três de cinco peças publicadas (`08-14/ilu-01`, `08-17/ilu-01`,
`08-17/ilu-02`) são exemplos do padrão que o próprio método novo já nomeia como erro. Isto não
é uma falha do sistema atual — é evidência de que o sistema atual (`briefing-ilustracao.md`)
foi desenhado *em resposta* a esses três casos reais. O diagnóstico aqui não é "conserte o
briefing", é "nenhuma peça publicada passou pelo briefing ainda — o primeiro teste real dele
é o próximo post".

---

## 2. Teste de plataforma

- **`capa.md` como arquivo próprio: 0 de 3 posts.** `2026-08-25` tem duas opções de capa, mas
  documentadas dentro de `ilustracoes.md` (seção "O que segue são duas opções de capa"), não em
  `capa.md` — o arquivo `capa.md` só passou a existir no `SKILL.md` no commit `beeeb38`
  (31/08, 14:02), depois dos três posts. Nenhum post tem hoje o entregável que o sistema atual
  exige.
- **Dimensão/proporção declarada:** as duas capas de `2026-08-25` especificam "Aspect ratio:
  exactly 16:9, landscape. Resolution: at least 2400×1350px" — mas isso foi escrito como
  parte do prompt de imagem, não como spec de plataforma auditável (não há seção "Zona segura"
  nem referência a limite de corte da Substack). O `SKILL.md` atual (`capa.md` §) já corrige
  isso para peças futuras: exige campo "Zona segura" explícito e mantém a mesma faixa
  2400×1350/16:9 como convenção, com `[VERIFICAR: dimensão oficial exata... fontes secundárias
  divergem entre 1200×630 e 1456×1048]`.
- **Confronto com o relatório:** `relatorio-design-editorial-ia.md` §2 (tabela) declara capa de
  artigo da Substack em **1456×816px, 16:9, JPG**, e capa do LinkedIn (feature image) em
  1200×644px (1.91:1) mais post de feed 1080×1350 (4:5). Isso resolve parcialmente o
  `[VERIFICAR]` do `SKILL.md` (confirma a proporção 16:9 já adotada; dá um terceiro candidato
  numérico à disputa 1200×630 vs. 1456×1048 vs. 1456×816) — mas o próprio prompt-mãe desta
  revisão instrui não fixar número sem confirmar na documentação oficial atual, e o relatório é
  fonte secundária como as outras duas. Fica **aberto para Fase B**: rodar a verificação
  (`WebFetch`/`WebSearch`) contra a documentação Substack/LinkedIn vigente antes de escrever um
  número definitivo em `SKILL.md`.
- **Texto embutido na imagem:** nenhuma das cinco peças publicadas pede texto renderizado —
  todos os `Negative prompt` (peças antigas) e `estilos-ilustracao.md` (regra 4, sistema novo)
  proíbem. Sem violação encontrada aqui.
- **Variantes por destino (LinkedIn feature/feed):** nenhum post tem variante derivada da capa
  hoje — item da B.2 do prompt original ainda não existe em nenhum lugar do sistema, nem no
  `SKILL.md` novo. Gap real, não só defasagem de post antigo.

---

## 3. Teste de marca

- **Cor:** as três `ilustracoes.md`/`graficos.md` publicadas leem cor de **`marca/tokens.json`**
  (ex. `2026-08-14/graficos.md`: `TOKENS_PATH = "marca/tokens.json"`; mesma linha em
  `2026-08-25/graficos.md`). Essa pasta **não existe mais no repositório**
  (`ls marca/` → *No such file or directory*; removida no commit `d1c664a`,
  "aposenta tokens.json local em favor de brand/DESIGN.md"). Consequência concreta, não só
  estética: **o bloco Python de `graf-01` dos dois posts com gráfico não roda mais como está**
  — `open(TOKENS_PATH)` falha com `FileNotFoundError` se alguém tentar reproduzir a etapa
  "teste com `python3` antes de considerar a etapa concluída" hoje. Isto quebra a garantia de
  reprodutibilidade que o próprio `SKILL.md` de `graficos.md` promete ("um gráfico cujo dado
  não está no repositório não é reproduzível seis meses depois" — aqui é o token que sumiu, não
  o dado, mas o efeito prático é o mesmo).
- **Paleta:** as peças antigas usam volt-green `#1FE07A`/`#3DE889` sobre obsidian `#0A0F0D` —
  paleta "O Sinal no Escuro v2.1", explicitamente aposentada. Nenhum hex de Forest/Grove/Lime
  aparece em nenhuma das cinco `ilu-NN`/capas publicadas. Consistente e esperado — já
  documentado como não-referência em `SKILL.md` e `marca-syntaxis/SKILL.md` — não é achado
  novo, é confirmação com evidência.
- **Estilo artístico:** nenhuma das cinco peças usa colagem ou desenho técnico esquemático — as
  cinco usam o registro "dark minimalist... soft glow" do sistema antigo, incluindo a regra do
  "elemento iluminado" que `SKILL.md` revogou explicitamente em 31/08 ("Revogado em
  31/08/2026" — `DESIGN.md` §4.5 lista glow como anti-padrão). Ou seja: **100% das peças
  publicadas violam, hoje, uma regra que só passou a existir depois delas.** Sem deriva real
  dentro do sistema atual (ele é recente demais para ter tido chance de derivar) — a deriva
  mora inteira na fronteira entre sistema antigo e novo.
- **`hemingway.tokens.json` órfão:** `brand/tokens/hemingway.tokens.json` existe (mesmo
  conteúdo/estrutura do antigo "O Sinal no Escuro v2.1") mas não é referenciado em nenhum
  arquivo do repositório hemingway (`grep -rn "hemingway.tokens.json" pipelines/hemingway/` →
  vazio). Não é bug funcional — nada quebra por causa dele — mas é confusão de nomenclatura
  candidata a backlog: um arquivo chamado "hemingway" que o hemingway não usa.
- **Campo `linha_editorial`:** `post-substack/SKILL.md` (etapa 1: *"linha editorial é campo
  obrigatório"*; etapa 9: entregável `post.md` deve ter `linha_editorial` no frontmatter) exige
  o campo — mas nenhum dos três `post.md` publicados o tem (frontmatter confirmado nos três:
  título/subtítulo/data/tags/status, sem `linha_editorial`). `2026-08-14` tem a tag "Notas de
  um Professor" (dá para inferir a linha por tag, plano B do `estilos-ilustracao.md`);
  `2026-08-17` (tags: carreira, educação financeira, formação, mercado financeiro) e
  `2026-08-25` (tags: Renda Fixa, LCI, Educação Financeira, Banco Master) **não têm nenhuma tag
  que nomeie a linha** — `2026-08-25` é, aliás, o caso que `estilos-ilustracao.md` já cita
  nominalmente como ambíguo. Achado de arquitetura: a regra "declare a linha, senão pare e
  pergunte" depende de um campo que a etapa 1 diz ser obrigatório mas que na prática, em 3 de 3
  posts, não foi preenchido. Vale para Fase B avaliar se `linha_editorial` devia ser validado
  automaticamente na etapa 1 (bloqueio, não só instrução).

---

## 4. Teste de Tufte nos gráficos

Dois `graf-NN` reais existem (`2026-08-14/graf-01`, `2026-08-25/graf-01`); o terceiro post
(`2026-08-17`) teve seu `graf-01` removido a pedido do autor e substituído por `ilu-02`,
documentado em `graficos.md` ("Nenhum gráfico neste post").

### `2026-08-14/graf-01` — Eixo Y

`yaxis=dict(title="Capital acumulado (R$)", gridcolor=grid, zerolinecolor=grid,
color=axis_text, tickprefix="R$ ", tickformat=",.0f")` — **sem `rangemode="tozero"`**. Os três
cenários (90/100/110% do CDI) terminam em R$ 11.872,34 / R$ 12.100,00 / R$ 12.331,84, partindo
de R$ 10.000,00 — sem baseline fixado, o autorange do Plotly tende a enquadrar o eixo próximo
da faixa de dados (algo como R$ 9.800–12.500), não de zero. Isso amplia visualmente a diferença
entre as três curvas: a diferença real ao final (R$ 459,50 sobre R$ 10.000, **4,6 pontos
percentuais de amplitude entre o cenário mais alto e o mais baixo**) ocuparia proporção maior
da altura do gráfico do que ocuparia com eixo zerado. **Lie Factor estimado** (efeito visual
percebido ÷ efeito real): não calculável com precisão sem rodar o código (o CSV/tokens não
estão mais executáveis, ver teste 3), mas a ausência de `rangemode="tozero"` é, por si, a
condição que o relatório (§4.2) descreve como a mais comum fonte de Lie Factor alto em
comparações financeiras. **Achado, não `[VERIFICAR]`: falta o rangemode.**

### `2026-08-25/graf-01` — Eixo Y

`yaxis=dict(..., rangemode="tozero")` — correto, zero fixado, série cresce de ~R$141bi a
~R$544bi, amplitude real grande o suficiente para que zero-baseline não distorça a leitura.
Nenhum chartjunk (`paper_bgcolor`/`plot_bgcolor` sólidos, sem sombra, sem 3D, grid em cor de
baixa saturação `grid`). Anotações diretas nos pontos de interesse (recuo regulatório, alta de
29%, valor final) — cumpre a regra de `checklist-graficos.md` ("anotação direta, não só
legenda"). O trecho sem dado intermediário (2020–2024) é tracejado e em cor apagada — é
exatamente o tratamento honesto que Tufte pede para não fingir trajetória contínua sem dado
(princípio de integridade contextual, relatório §4.2). **Este gráfico passa nos critérios de
Tufte já capturados no sistema atual.**

### `2026-08-14/graf-01` — comparação com o par

A inconsistência (zero explícito em um post, ausente no outro) é o achado central deste teste:
**não é falta de regra no craft (`checklist-graficos.md` cobre anotação/revelação
progressiva/contraste), é falta de regra específica sobre baseline/Lie Factor** —
`checklist-graficos.md` não menciona eixo zerado, Lie Factor, chartjunk ou pequenos múltiplos
em nenhum lugar. O relatório (§4) traz exatamente essas quatro peças que faltam no checklist
atual. Isto é o gap real que a Fase B (item B.3 do prompt original) precisa fechar — o
checklist de craft e o gate de Tufte são coisas diferentes hoje, e só o primeiro existe.

### Chartjunk geral

Nenhum dos dois `graf-NN` usa 3D, sombra, textura ou moldura — ambos já seguem essa parte do
princípio, mesmo sem checklist formal cobrindo. O achado não é "há chartjunk", é "a ausência de
chartjunk hoje é convenção seguida por quem escreveu o código, não regra auditável escrita em
lugar nenhum".

---

## 5. Teste de arquitetura

**Onde a decisão visual acontece hoje**, por etapa (`post-substack/SKILL.md`):

- **Etapa 1** declara `linha_editorial` obrigatória (mas ver teste 3 — não é validada na
  prática).
- **Etapa 2** (`02-estrutura.md`) decide, com critério escrito desde a auditoria-2026, qual
  `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` cada seção leva e por quê (`post-substack/SKILL.md`,
  seção "Etapa 2" — a árvore de decisão com os quatro critérios, incluindo o precedente citado
  nominalmente de `2026-08-17/ilustracoes.md ilu-02`).
- **Etapa 8** (skill `prompts-visuais`) é onde o conceito de facto nasce — e, desde hoje, **não
  é mais um passo só**: `08-briefing-visual.md` (etapa 8a, colheita + motor de três operações +
  testes de rejeição) roda **antes** do prompt final em `ilustracoes.md`/`capa.md`. Isso já é,
  na prática, a cadeia de dois passos que o relatório (B.1 do prompt original) pede — falta
  formalmente **um terceiro passo separado**: hoje `briefing-ilustracao.md` termina no "conceito
  escolhido" (Passo 6, com estrutura de metáfora) e o próprio `SKILL.md` de `prompts-visuais`
  já pede a "cena narrada" na hora de escrever o prompt (formato `[Sujeito] + [Ação/estado] +
  [Contexto] + [Composição] + [Estilo] + [Paleta] + [Proporção]`) — ou seja, **composição de
  cena e redação de prompt final estão fundidas no mesmo passo**, não separadas como o relatório
  propõe em B.1 (destilação → composição → prompt). Diferença real, mas pequena: o sistema atual
  tem duas paradas (briefing; prompt), o relatório sugere três (destilação; composição; prompt).
  Vale avaliar em Fase B se a separação adicional compensa a fricção extra, ou se o "Passo 3 —
  motor" do briefing atual já faz esse trabalho implicitamente (a "tradução material que fecha
  o conceito", vista nos exemplos de `exemplos-prompts.md`, já é composição de cena antes da
  sintaxe do gerador).
- **Nenhuma camada de roteamento por gerador existe.** `estilos-ilustracao.md` e
  `templates-prompt.md` escrevem regras de prompting (sem negative prompt, proporções
  suportadas, formato de cena narrada) **diretamente na referência principal**, nomeando
  "Google Nano Banana Pro" dentro do corpo do texto, não como um adaptador plugável. Se o
  `GERADOR_IMAGEM` mudar amanhã (cenário que o prompt original da revisão pede para o sistema
  suportar — B.4), hoje seria preciso editar `estilos-ilustracao.md` e `templates-prompt.md`
  diretamente, misturando regra de marca/composição (agnóstica) com regra de sintaxe de gerador
  (condicional). **Gap real, não defasagem de post antigo** — é ausência de camada, mesmo no
  sistema novo.
- **Etapa 9** (skill `revisao-editorial`) já valida "inventário visual e paleta fora dos
  tokens" (commit `e02640f`, Fase 2 da auditoria) — não confirmei aqui se essa validação cobre
  também "capa presente" e "prompt com gerador declarado" (specs pedidas pelo B.5 do prompt
  original); marcado para leitura em Fase B, fora do escopo dos cinco testes desta Fase A.

---

## Resumo — o que já está resolvido vs. o que a Fase B precisa decidir

| Item do prompt original | Estado |
|---|---|
| B.1 — cadeia semiótica (destilação → composição → prompt) | **Parcial.** Briefing (destilação+parte da composição) existe desde hoje; separação explícita de um 3º passo de "composição de cena" não existe — hoje é 2 passos, não 3. |
| B.2 — capa como entregável de 1ª classe | **Estrutura existe** (`capa.md` no `SKILL.md`), **zero posts publicados a implementam**; dimensão exata segue `[VERIFICAR]`; variantes LinkedIn não existem em lugar nenhum. |
| B.3 — gate de Tufte executável | **Não existe.** `checklist-graficos.md` cobre craft (anotação/revelação/contraste), não cobre baseline zero, Lie Factor, chartjunk ou small multiples — e há uma inconsistência real de baseline entre os dois `graf-NN` publicados. |
| B.4 — roteamento por gerador | **Não existe.** Regras de Nano Banana Pro estão fundidas nas referências agnósticas de marca/composição. |
| B.5 — integração no pipeline (etapas 2/8/9) | **Etapas 2 e 8 já integradas** pela auditoria-2026; **etapa 9 não confirmada** para os itens novos (capa presente, gerador declarado, gate de Tufte). |
| Achado fora do escopo do prompt original | `marca/tokens.json` foi removido mas ainda é `import`ado por código Python committado em 2 de 3 posts — quebra de reprodutibilidade real, não hipotética. |
| Achado fora do escopo do prompt original | Campo `linha_editorial`, obrigatório por `SKILL.md`, ausente em 3 de 3 `post.md` publicados. |
| Achado fora do escopo do prompt original | `brand/tokens/hemingway.tokens.json` existe e não é referenciado em nenhum lugar do repo hemingway. |

**Pare aqui para revisão do autor antes da Fase B**, conforme o prompt original.
