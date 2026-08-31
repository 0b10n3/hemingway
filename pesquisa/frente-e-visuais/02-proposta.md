# Fase B — Proposta de redesenho

Nada neste documento foi implementado. É a lista de diffs propostos, para aprovação item a
item antes da Fase C — conforme pedido no prompt original desta revisão.

## Duas ressalvas sobre o relatório, antes de qualquer proposta

1. **Correção (registrada depois do merge desta Fase B — ver `RELATORIO.md`):** a versão
   original deste item chamava a §6 do relatório ("Análise Estrutural Aplicada: O Sistema
   'Projeto Hemingway'") de citação fabricada, por citar como fonte um repositório GitHub
   `0b10n3/hemingway` (referência 70) que eu não tinha verificado. **Isso estava errado.**
   `git remote -v` confirma que `0b10n3/hemingway` é o remote real deste próprio
   repositório (`git@github.com:0b10n3/hemingway.git`) — a citação é válida, não fabricada.
   Eu afirmei "não corresponde a nada verificável" sem checar o remote antes de escrever;
   é exatamente o tipo de afirmação sem lastro que o `CLAUDE.md` deste repositório proíbe, e
   caí nela ao tentar aplicá-la ao relatório. §6 pode ser lida como um case study real deste
   projeto (presumindo que o repositório é público ou foi acessado de outra forma pelo
   processo que gerou o relatório) — o que não muda o tratamento dado aos números específicos
   dela ou de qualquer outra seção: continuam sujeitos à mesma régua de "confirme antes de
   fixar" do prompt original, não porque a fonte é suspeita, mas porque é sempre terciária.
2. **A conta do relatório para o LinkedIn não fecha.** §2 (resumo executivo) recomenda
   "1080 x 1350 px vertical (4:5)" para o feed — correto, 1080/1350 = 0,8 = 4:5 exato. Mas a
   tabela de §2 lista "LinkedIn - Capa de Artigo: 1200 x 644, proporção 1.91:1" — 1200/644 ≈
   1,86, não 1,91. A dimensão que de fato fecha 1.91:1 é **1200×627**. Tratado como erro do
   relatório, não como dado a copiar — ver B.2 abaixo.

---

## B.1 — Cadeia de abstração semiótica

**Diagnóstico (Fase A, teste 5):** hoje são duas paradas, não três — `briefing-ilustracao.md`
(Passo 1–6) entrega um "conceito escolhido" com estrutura de metáfora, e o prompt final em
`ilustracoes.md`/`capa.md` já mistura composição de cena com sintaxe de gerador no mesmo passo.

**Proposta:** acrescentar um **Passo 7 — Composição de cena** a
`.claude/skills/prompts-visuais/references/briefing-ilustracao.md`, entre o Passo 6 (Escolha e
defesa) e a seção "Referência de cultura pop". Conteúdo proposto:

```markdown
## Passo 7 — Composição de cena

Ainda sem sintaxe de gerador. Transforme o conceito do Passo 6 em cena: que objetos existem
na composição, onde cada um fica (centro, periferia, eixo), o que está em primeiro plano e o
que é fundo, onde entra o único ponto de acento (lime, se houver) e por que ali, e qual frase
resume "o que esta composição prova" — a mesma frase do Passo 2, agora traduzida em
disposição espacial. Só depois deste passo o prompt do gerador é redigido (ver
`templates-prompt.md` e `references/geradores/`).
```

Reaproveita a estrutura existente (mesmo arquivo, mesmo `processo/08-briefing-visual.md` —
não cria arquivo novo), só formaliza um passo que hoje é implícito no Passo 6 + no template.
Ajuste de uma linha em `SKILL.md` (etapa 8a): trocar "as três operações geradoras... →
critérios positivos de beleza..." para citar também a composição como etapa própria.

**Peso da mudança:** pequeno. Achado da Fase A já registrava que a separação extra pode não
compensar a fricção — a "tradução material que fecha o conceito" nos exemplos validados
(`exemplos-prompts.md`) já faz esse trabalho em prosa, só não como campo com nome próprio no
método. Proponho a versão mínima acima porque dá auditabilidade (o campo existe, pode ser
citado por revisão futura) sem duplicar o que o Passo 6 já produz.

---

## B.2 — Capa como entregável de primeira classe

**Dimensão da capa Substack.** Tentei confirmar na documentação oficial: a página de suporte
(`support.substack.com/.../4408381685268`) bloqueou fetch automático de novo nesta sessão
(HTTP 403 — mesma barreira já registrada na auditoria-2026, Fase 2). Busca cruzada em fontes
secundárias (não o relatório) converge em dois números com papéis diferentes, não
concorrentes: **1456×816px** para a capa que aparece no topo do artigo (o que este sistema
chama de `capa.md`) e **1200×630px** para o thumbnail recortado automaticamente para e-mail/
redes. Isso resolve a ambiguidade do `[VERIFICAR]` atual do `SKILL.md` (que tratava
1200×630 e 1456×1048 como concorrentes) — não são concorrentes, são dois ativos diferentes, e
só o primeiro nos interessa (Substack gera o segundo por recorte automático). Proposta: trocar
o texto de `capa.md` § em `SKILL.md`:

```diff
- **Proporção:** 16:9, resolução mínima 2400×1350px.
-   `[VERIFICAR: dimensão oficial exata recomendada pela Substack para a imagem de destaque/
-   thumbnail — fontes secundárias divergem entre 1200×630 e 1456×1048; página oficial
-   bloqueou fetch automático nesta auditoria]`.
+ **Proporção:** 16:9. Gerar em 2400×1350px (margem confortável acima do alvo de publicação)
+   e exportar em 1456×816px para a capa do artigo — dimensão convergente em múltiplas fontes
+   secundárias (Substack gera separadamente um thumbnail 1200×630 por recorte automático
+   para e-mail/redes, não é ativo que este sistema precise produzir).
+   `[VERIFICAR: página oficial de suporte da Substack bloqueou fetch automático em duas
+   tentativas (auditoria-2026 e esta revisão) — número acima é convergência de fontes
+   secundárias, não confirmação primária; revisitar se a Substack disponibilizar acesso]`.
```

Continua marcado `[VERIFICAR]` — não é confirmação primária, é a melhor convergência
disponível sem acesso à fonte oficial. Isto segue a regra do prompt original: números não
confirmados em documentação oficial atual ficam `[VERIFICAR]`, com a fonte anotada.

**Variantes derivadas (LinkedIn).** Proponho que morem no próprio `capa.md`, seção nova
opcional — não em `ilustracoes.md` nem arquivo à parte — porque é a mesma decisão de capa
reenquadrada para outro destino, e `capa.md` já é a fonte única da capa (`CLAUDE.md`: uma
fonte por fato). Texto proposto para `SKILL.md`, dentro da descrição de `capa.md`:

```markdown
- **Variantes derivadas (opcional, só quando o post for divulgado no LinkedIn):**
  - **LinkedIn feature image** — 1200×627px, 1.91:1. (O relatório de pesquisa citava
    1200×644 como 1.91:1, mas a conta não fecha: 1200/644 ≈ 1,86. 1200×627 é a dimensão que
    de fato fecha 1,91:1 — usar esta.)
  - **LinkedIn feed** — 1080×1350px, 4:5, retrato.
  - Mesma metáfora da capa principal, reenquadrada — nunca um conceito novo. Composição
    original já deve prever essa margem de recorte (zona segura mais generosa no eixo que
    muda de proporção).
  - Onde registrar: mesmo bloco de `capa.md`, campo "Variantes" ao final — gerado só quando o
    post for de fato programado para divulgação no LinkedIn (não é obrigatório por padrão).
```

---

## B.3 — Gate de Tufte para gráficos

**Diagnóstico (Fase A, teste 4):** `checklist-graficos.md` cobre craft (anotação, revelação
progressiva, contraste genuíno) mas não cobre baseline zero, Lie Factor, chartjunk ou small
multiples — e há uma inconsistência real: `2026-08-14/graf-01` não fixa
`rangemode="tozero"`, `2026-08-25/graf-01` fixa.

**Proposta 1 — nova seção em `checklist-graficos.md`:**

```markdown
## Gate de Tufte (integridade da forma, não do craft de leitura)

Os três critérios acima (anotação, revelação progressiva, contraste genuíno) tratam de como o
gráfico se lê. Estes tratam de se o gráfico mente:

- **Eixo Y começa em zero para gráfico de barras.** Exceção exige justificativa escrita no
  spec (ex.: série já é uma variação percentual pequena onde zero não é o ponto de
  comparação relevante). Para linha/série temporal, avalie caso a caso: se a amplitude real
  entre as séries é pequena frente ao valor absoluto (como em `2026-08-14/graf-01` — R$
  459,50 de diferença sobre uma base de R$ 10.000), o eixo sem zero exagera visualmente a
  diferença mesmo sendo linha, não barra — declare `rangemode="tozero"` como padrão, e
  justifique por escrito a exceção.
- **Lie Factor declarado quando há ênfase visual** (tamanho, cor, área carregando o
  argumento) — fórmula: (variação visual do efeito) ÷ (variação real do efeito nos dados).
  Alvo 0,95–1,05. Fora dessa faixa, redesenhe o encoding.
- **Sem 3D, sombra, textura ou moldura.** Grid mínimo, opacidade baixa (os dois `graf-NN`
  publicados já seguem isto — formalizar como regra, não deixar implícito no código de quem
  escreveu antes).
- **Rótulos adjacentes ao dado**, não só legenda distante — já coberto pela regra de anotação
  acima, citado aqui só para lembrar que os dois testes se reforçam.
- **Dimensão visual ≤ dimensão dos dados** — nunca escalar raio de círculo (área) para dado
  unidimensional; nunca altura de barra 3D fingindo profundidade que não é dado.
- **Small multiples quando ≥3 séries competem visualmente** — mesmo critério que já existe
  em "Revelação progressiva" (não duplicar; esta seção só lembra que small multiples é a
  ferramenta formal de Tufte para o mesmo problema que a revelação progressiva já ataca).
```

**Proposta 2 — item novo no checklist de `revisao-editorial/SKILL.md`** (hoje o item 10 só
audita hex fora de token; itens de `graf-NN`/`diag-NN` não são revisitados na etapa 9 porque o
comentário do item 10 os declara "estruturalmente seguros" por lerem `tokens.json` em
runtime — verdade para cor, não para o Gate de Tufte):

```diff
 10. **Paleta fora dos tokens — checagem mecânica.** [...]

+11. **Gate de Tufte — checagem mecânica.** Para cada bloco de código em `graficos.md`/
+    `diagramas.md`: `rangemode="tozero"` presente (ou exceção justificada por escrito no
+    spec)? Nenhuma menção a `3d`, sombra (`shadow` fora de `shadow.syntaxis*`), textura ou
+    moldura no código? Se o spec já traz "Lie Factor" declarado, confere a conta; se a peça
+    tem ênfase visual e não declara, sinalize para o gate humano — não calcule por conta
+    própria sem o dado bruto.
```

**Proposta 3 — o achado concreto de `2026-08-14/graf-01` (falta `rangemode="tozero"`).**
Este é o único item desta fase que toca um arquivo já publicado (`posts/.../graficos.md`), e
por regra do `CLAUDE.md` precisa da sua aprovação item a item antes de qualquer edição — não
está pré-aprovado por estar nesta lista. Diff proposto, se aprovado:

```diff
 yaxis=dict(
     title="Capital acumulado (R$)",
     gridcolor=grid, zerolinecolor=grid, color=axis_text,
     tickprefix="R$ ", tickformat=",.0f",
+    rangemode="tozero",
 ),
```

Consequência de aplicar: o gráfico teria que ser regerado (`figuras/graf-01.svg`/`.png`) — mas
o código não roda mais como está (ver achado da Fase A: `marca/tokens.json` não existe mais),
então esse conserto também exige decidir *para onde* apontar os tokens agora (provavelmente
`../../brand/tokens/skill_test.tokens.json`, reescrevendo os nomes de chave — o schema mudou
de `neutrals.obsidian.hex` para o formato DTCG novo). **Não proponho fazer isso agora** — é
mudança de escopo maior que um ajuste de eixo, e toca um post já publicado; melhor tratar como
item de backlog explícito (ver final deste documento) do que empurrar para dentro da Fase C
desta revisão.

---

## B.4 — Roteamento por gerador (camada condicional)

**Diagnóstico (Fase A, teste 5):** hoje as regras do Nano Banana Pro (sem negative prompt,
proporções suportadas, formato de cena narrada) estão soldadas dentro de
`estilos-ilustracao.md` (seção "Como escrever o prompt") e de `templates-prompt.md`, junto com
o vocabulário agnóstico de marca/composição. Trocar de gerador hoje exigiria editar essas duas
referências diretamente.

**Proposta:** criar `.claude/skills/prompts-visuais/references/geradores/`, um arquivo por
motor:

1. **`nano-banana-pro.md`** — extração literal da seção "Como escrever o prompt" que já existe
   em `estilos-ilustracao.md` (fonte: guia oficial Google Cloud, já citado lá). Nenhum
   conteúdo novo, só realocação — `estilos-ilustracao.md` fica só com o vocabulário
   agnóstico (paleta, geometria, estilo A/B) e um ponteiro de uma linha para o adaptador.
2. **`flux-1-1-pro.md`** — esboço, **não-validado**, a partir do relatório §5.1: gramática
   fotográfica sequencial (sujeito → contexto → luz → especificação técnica de câmera →
   atmosfera/resolução); `guidance_scale` 2,5–3,5 como faixa de equilíbrio; `inference_steps`
   40–50; RoPE permite proporções nativas sem distorção. Marcado no topo do arquivo: *"Nunca
   testado neste ambiente — validar com uma peça real antes de confiar nestes parâmetros."*
3. **`midjourney-v6-1.md`** — esboço, **não-validado**, a partir do relatório §5.2:
   `--style raw` para tirar o verniz padrão do modelo; `--stylize`/`--s` 0–1000 (baixo =
   fotográfico, alto = pictórico); `--sref` para consistência de estilo entre peças do mesmo
   post via URL de referência — capacidade que o Nano Banana Pro **não tem**; se um post
   precisar de várias peças com a mesma atmosfera exata e o gerador ativo continuar sendo Nano
   Banana Pro, a alternativa registrada é descrição verbal de estilo consistente repetida em
   cada prompt (mesmos termos de material/luz/paleta), não paridade real de recurso — sem
   fingir que o Nano Banana Pro tem o mesmo controle.

**Declaração do gerador ativo.** Uma linha no topo de `prompts-visuais/SKILL.md`:

```markdown
**Gerador ativo hoje:** Nano Banana Pro (Gemini) — ver
`references/geradores/nano-banana-pro.md`. Trocar de gerador é trocar esta linha e apontar
para o adaptador correspondente; nenhuma outra referência deste sistema muda.
```

E cada prompt final em `ilustracoes.md`/`capa.md` já declara o gerador no próprio cabeçalho
("Prompt para GERADOR_IMAGEM (Google Nano Banana Pro)") — formalizar isso como campo
obrigatório do formato de bloco (já é convenção de fato nos posts publicados, só falta estar
escrito como regra no `SKILL.md`).

---

## B.5 — Integração no pipeline

**Etapas 2 e 8:** já integradas pela auditoria-2026 (critério de tipo visual na etapa 2;
`capa.md` + briefing na etapa 8). Diff adicional proposto pela B.1: uma linha em "Etapa 8a" do
`SKILL.md` citando o Passo 7 novo.

**Etapa 9 (`revisao-editorial`):** dois diffs propostos, ambos já detalhados acima —

- item 11 novo: Gate de Tufte, checagem mecânica de `rangemode`/chartjunk em `graf-NN`/
  `diag-NN` (B.3).
- extensão do item 9 (inventário visual): confirmar que todo prompt em `ilustracoes.md`/
  `capa.md` declara o gerador (B.4) — mesma lógica do item 9 atual, só mais um campo a
  checar por post.

**Etapa 10 (gate humano):** já exibe "a lista de `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` com
tipo e status" (`SKILL.md`, linha 122) — nenhuma mudança necessária, o inventário cresce
automaticamente com os itens novos que a etapa 9 passa a checar.

---

## Backlog (fora do escopo desta revisão, registrado para não perder)

1. **`marca/tokens.json` morto em código committed.** `2026-08-14/graficos.md` e
   `2026-08-25/graficos.md` importam um caminho que não existe mais. Consertar exige migrar o
   schema de chaves (formato antigo `neutrals.obsidian.hex` → DTCG novo
   `color.neutral.chalk.$value` etc.) em código de posts já publicados — mudança que toca
   `posts/` e precisa aprovação item a item, fora do escopo de "revisão do processo visual".
2. **Campo `linha_editorial` ausente em 3 de 3 `post.md` publicados**, apesar de
   `post-substack/SKILL.md` chamá-lo obrigatório. Considerar, em revisão futura do pipeline
   (não desta), bloquear a etapa 1 mecanicamente se o campo não vier preenchido, em vez de só
   instruir.
3. **`brand/tokens/hemingway.tokens.json`** existe e não é referenciado em lugar nenhum do
   repo hemingway — candidato a remoção ou documentação de propósito (parece ser o backup do
   sistema aposentado "O Sinal no Escuro v2.1"), decisão de quem mantém `brand/`, não deste
   repositório.

---

**Pare aqui para sua aprovação item a item antes da Fase C**, conforme o prompt original.
Lista curta do que precisa de "sim"/"não"/"ajuste" individual:

1. B.1 — Passo 7 (Composição de cena) em `briefing-ilustracao.md`.
2. B.2 — reescrita do `[VERIFICAR]` de dimensão de capa em `SKILL.md` (1456×816, ainda
   marcado `[VERIFICAR]` por falta de fonte primária).
3. B.2 — seção "Variantes derivadas" (LinkedIn) em `capa.md`.
4. B.3 — nova seção "Gate de Tufte" em `checklist-graficos.md`.
5. B.3 — item 11 novo em `revisao-editorial/SKILL.md`.
6. B.3 — **não incluído nesta rodada**: patch de `rangemode` em `2026-08-14/graf-01` (backlog
   item 1, por causa da dependência do token morto).
7. B.4 — criação de `references/geradores/` com os três adaptadores (1 extraído, 2
   esboçados e marcados não-validados).
8. B.4 — linha de "gerador ativo" em `prompts-visuais/SKILL.md`.
9. B.5 — diffs em `revisao-editorial/SKILL.md` (mesmo diff do item 5 acima) e nota de uma
   linha na etapa 8a do `post-substack/SKILL.md`.
