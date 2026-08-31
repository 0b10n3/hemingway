# Fase 2 — Evolução do processo visual (capa, ilustração, diagrama, infográfico)

## Evidência real que ancora esta proposta

Duas coisas já aconteceram na prática, sem categoria formal para acomodá-las:

1. **Capa ad hoc.** `posts/2026-08-25-.../estado.json.reentradas` registra o autor pedindo,
   no gate humano, "duas opções de imagem de capa (16:9)" — não previstas em nenhuma etapa,
   resolvidas com uma reentrada manual à etapa 8 e um parágrafo de aviso dentro de
   `ilustracoes.md` explicando que aquilo "não são `ilu-NN` de corpo". Sinal de categoria
   faltando, não de exceção pontual.
2. **Diagrama disfarçado de ilustração, pego manualmente.** Em
   `posts/2026-08-17-.../ilustracoes.md`, a nota de revisão de `ilu-02` documenta que o
   conceito original ("duas linhas de luz lado a lado") foi rejeitado pelo próprio autor por
   ser "ainda, no fundo, um diagrama disfarçado de ilustração" — duas séries comparadas sem
   dado real, resolvido só porque o autor pegou no gate, não porque o processo tinha um
   critério escrito para evitar chegar lá. `briefing-ilustracao.md` já lista esse erro
   ("diagrama disfarçado de ilustração") na seção de erros recorrentes, mas hoje é prosa, não
   critério de decisão na etapa 2.

Confirmando o achado da Fase 0/1: **nenhuma ilustração publicada usa o sistema de estilo por
linha editorial** (`estilos-ilustracao.md`, criado 31/08) — as três `ilu-NN` existentes são
todas do sistema anterior "O Sinal no Escuro" (glow único), anteriores à distinção
colagem/esquemático. A proposta abaixo, portanto, não está corrigindo um padrão estabelecido —
está formalizando categorias para um sistema que ainda vai gerar sua primeira peça real.

---

## 2.1 — Capa (nova, obrigatória)

**Onde mora:** arquivo novo `posts/<slug>/capa.md`, irmão de `ilustracoes.md`/`graficos.md`,
não uma seção dentro de `ilustracoes.md`. Motivo: a capa é **obrigatória e única** por post
(zero-ou-N para `ilu-NN`), tem consumidor diferente (a UI de upload do Substack, não um
placeholder inline em `post.md`) e a evidência real já mostra o problema de misturar as duas —
o `ilustracoes.md` do post 08-25 precisou de um parágrafo inteiro só para avisar "isto aqui não
é `ilu-NN`". Arquivo separado elimina a ambiguidade na fonte, não com aviso.

**Especificação do bloco `capa`:**

- **Origem obrigatória: `processo/01-briefing.md`, não o texto final.** O prompt de capa nasce
  da tese em uma frase e do gancho escolhido na etapa 1 — nunca de um detalhe do corpo. Isso já
  é como a `capa` ad hoc de 08-25 funcionou de fato (Capa A e B carregam a tese "o risco tem
  endereço", não um parágrafo específico) — a regra só formaliza o que já aconteceu certo.
- **Estilo:** segue a mesma tabela de `estilos-ilustracao.md` — colagem para Spoiler, desenho
  técnico esquemático para Notas de um Professor. Mesma paleta fechada, mesmas regras
  compartilhadas (sem glow, sem texto renderizado, geometria reta).
- **Dimensão — `[VERIFICAR]` o número oficial exato.** Fontes secundárias divergem entre si
  (1200×630 a 1456×1048; proporção citada como 14:10, 3:2 ou 16:9 dependendo da fonte) e a
  página oficial da Substack bloqueou fetch direto nesta sessão. Uma fonte prática
  (Karo Zieminski, "Substack Cover Image Dimensions: The Safe Zone That Survives All 9 Crops")
  é a mais específica: canvas de **1200×630px**, com **zona segura de só 345×195px centrada**
  (~29% da largura, ~31% da altura) — tudo fora disso é cortado em algum dos nove recortes que
  a Substack aplica. Isto muda uma prática real da versão ad hoc: os prompts de Capa A/B atuais
  pedem "generous negative space" e curva ampla ocupando boa parte do quadro — sob a zona
  segura de 29%/31%, esse tipo de composição arrisca ter o ponto de foco cortado.
  **Recomendação até confirmar o número oficial:** manter a convenção já usada (16:9,
  ≥2400×1350px, que cobre com folga qualquer mínimo citado) e **acrescentar a regra da zona
  segura ao formato do prompt** — o elemento único iluminado/aceso (o argumento da peça) deve
  ocupar o terço central da composição, não a periferia, independente do aspect ratio final de
  geração. `[VERIFICAR: página oficial support.substack.com — tentar de novo com outro user
  agent ou pedir para o autor colar o texto, já que o fetch automático foi bloqueado (403)]`.
- **Formato do bloco em `capa.md`:** mesmo formato de bloco já usado para `ilu-NN`
  (conceito + estrutura de metáfora, linha editorial e estilo aplicado, prompt completo,
  restrições em enquadramento positivo, alt-text) — com um campo a mais, **"Zona segura"**,
  descrevendo em uma frase onde o elemento de foco fica posicionado no quadro.
- **Promoção a `ilu-01`:** se o autor decidir reusar a capa no corpo, ela é *promovida* — ganha
  placeholder próprio em `ilustracoes.md`, nunca é referenciada por caminho cruzado. Regra já
  seguida ad hoc em 08-25; só estou tornando explícita.

## 2.2 — Ilustrações internas (revisão do existente)

Não há, hoje, prompt algum gerado sob o sistema novo para auditar por consistência real — os
três `ilu-NN` publicados são todos pré-31/08. O que a evidência antiga oferece é padrão de
**craft de composição** que vale preservar no template novo (foco único, negative space,
elemento estrutural nunca competindo em destaque com o elemento de foco — presente nos três
exemplos antigos e coerente com os critérios de beleza de `briefing-ilustracao.md`).

**Proposta: dois templates de prompt, um por estilo, como referência nova**
`prompts-visuais/references/templates-prompt.md`. Não duplica a tabela de hex nem as regras de
`estilos-ilustracao.md` — só dá o esqueleto preenchível, reduzindo a chance de um prompt vago
que obriga reprocessamento:

```
### Template — Colagem editorial (Spoiler)
[Sujeito/objeto único, papel recortado] + [camadas visíveis, sombra chapada sem blur] +
[retícula/desalinho de registro, se aplicável] + [fundo: chalk ou deepForest — ver estilos-
ilustracao.md] + [até 4 cores de papel, lime só se há virada] + [proporção]

### Template — Desenho técnico esquemático (Notas de um Professor)
[Peça/mecanismo único, projeção ortogonal] + [linha de construção visível, eixo/centro] +
[corte ou vista explodida, se o argumento for "por dentro"] + [fundo: deepForest ou chalk] +
[lime marca só a peça que o parágrafo explica agora] + [proporção]
```

Cada template aponta para "ver tabela de hex autorizados em `estilos-ilustracao.md`" em vez de
listar valores — mesma disciplina de fonte única já em vigor.

## 2.3 — Diagramas (novo)

**Ferramenta escolhida: Plotly, estendendo o mesmo padrão já em produção em `graf-NN`** (nós e
setas via `add_shape`/`add_annotation`, não uma biblioteca de diagrama dedicada.

**Por quê, contra os critérios pedidos:**

| Critério | Plotly (proposto) | Mermaid | Graphviz |
|---|---|---|---|
| Reproduzível via código versionável | ✅ já é o padrão de `graf-NN` | ✅ | ✅ |
| Estilizável com tokens do `DESIGN.md` | ✅ já lê `tokens.json` em runtime, testado | parcial (`themeVariables`, sem token JSON nativo) | ✅ (`fillcolor`/`fontcolor`) |
| Executável localmente sem dependência pesada nova | ✅ `plotly`/`kaleido` já instalados e testados nesta máquina (`kaleido 1.3.0`) | ❌ requer Mermaid CLI, que baixa Chromium/Puppeteer — dependência pesada não documentada em `README.md` | ⚠️ requer binário `dot` do sistema — confirmei que **não está instalado** nesta máquina, dependência nova ainda que leve |
| Layout automático de nós | ❌ posicionamento manual | ✅ | ✅ |

A desvantagem real é perder layout automático — para os exemplos citados no prompt (fluxo
emissor-distribuidor-investidor, linha do tempo, balanço) o número de nós é baixo (3-6) e
linha-do-tempo/balanço já são tipos de gráfico que Plotly resolve nativamente (scatter com eixo
de data, barra empilhada), então o custo de posicionar manualmente é pequeno perto do ganho de
**zero dependência nova** e **zero superfície de revisão nova** para `verificador-tecnico` (que
já lê e executa código Plotly na etapa 7 — revisar `diag-NN` não pede nenhuma habilidade que
ele não tenha hoje). Se algum diagrama futuro precisar de layout de grafo com muitos nós
(>8-10), reabra esta decisão — não vale pagar o custo do Mermaid/Graphviz por antecipação.

**Onde mora:** `posts/<slug>/diagramas.md`, irmão de `graficos.md`, mesmo formato de bloco
(pergunta que o diagrama responde, fonte se houver dado real embutido, código Python
executável, escolha justificada, alt-text) — sem seção de dados/CSV quando o diagrama for
puramente estrutural (sem série numérica).

## 2.4 — Infográficos (novo, condicional — padrão é não ter)

**Critério de gatilho, por escrito:** só quando **nenhum** `graf-NN`/`diag-NN`/`ilu-NN` isolado
carrega a síntese sozinho — ou seja, quando o ponto só existe na leitura conjunta de ≥2 peças
que, separadas, forçam o leitor a montar a relação de cabeça. Não é gatilho: "ficaria bonito
consolidado", "tenho 3 fatos soltos" ou "quero variar o formato". O padrão é **não infográfico**
— cada `graf-NN`/`diag-NN`/`ilu-NN` que responde sua própria pergunta em uma frase (já exigido
pelo formato de `graficos.md`) fica separado.

**Onde mora:** `posts/<slug>/infograficos.md`, criado só quando o gatilho se aplica. Formato
híbrido: hierarquia de leitura (o que o olho vê primeiro/segundo/terceiro, obrigatório e
explícito — não implícito no layout), dado com fonte (como `graf-NN`), tokens usados, e
código/prompt de geração (Plotly para a parte de dado real, mesmo prompt de ilustração para
elemento de apoio, se houver).

---

## Integração no pipeline

### Placeholders

`capa` (arquivo único, sem placeholder inline em `post.md` — vai direto pro campo de capa do
Substack), `ilu-NN`, `graf-NN`, `diag-NN`, `info-NN` (todos com placeholder
`![Tipo: legenda](tipo-NN)` em `post.md`, mesmo padrão já em uso).

### Diff em `post-substack/SKILL.md`, etapa 2 — critério escrito, não gosto

Nova subseção, no mesmo padrão da já existente "Etapa 1 — linha editorial é campo obrigatório":

```markdown
## Etapa 2 — ilustração, gráfico, diagrama ou infográfico: critério, não gosto

Para cada ponto que a etapa 2 decidir que precisa de visual, decida o tipo por este critério,
nesta ordem — e registre por que os outros três perderam:

1. Há série numérica real a comparar/mostrar trajetória? → **`graf-NN`**.
2. Não há série, mas há relação estrutural entre entidades, fluxo, processo ou linha do tempo
   sem métrica central? → **`diag-NN`**. (Sinal de que devia ser isto e não `ilu-NN`: se o
   conceito se resolve em formas geométricas comparadas — duas linhas, dois blocos — sem um
   objeto concreto do texto por trás, é diagrama fantasiado de ilustração. Já aconteceu:
   `posts/2026-08-17-.../ilustracoes.md`, revisão de `ilu-02`.)
3. Nenhuma das duas, mas o texto tem metáfora/analogia/imagem própria do autor que carrega
   argumento? → **`ilu-NN`**, via `briefing-ilustracao.md`.
4. Só considere **`info-NN`** se nenhuma peça isolada acima carregar a síntese sozinha — ver
   critério de gatilho em `prompts-visuais/references/`. Default: não.

Toda decisão vai em `02-estrutura.md`, junto com o que cada peça prova (já exigido hoje).
```

### Diff em `prompts-visuais/SKILL.md`, etapa 8

Acrescentar, ao lado das seções `ilustracoes.md`/`graficos.md` já existentes, duas novas
seções curtas (`capa.md` e `diagramas.md`/`infograficos.md` condicional) apontando para as
regras acima, sem repeti-las — mesma disciplina de referência por caminho relativo já em vigor
no arquivo.

### O que a etapa 9 (`revisao-editorial`) passa a validar

Acrescentar ao checklist de 8 itens já existente: **(9) inventário visual completo** — todo
post tem `capa.md`; todo `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` referenciado em `post.md` tem
bloco correspondente no arquivo certo; **(10) verificação mecânica de paleta** — script
`python3` que varre `capa.md`/`ilustracoes.md`/`infograficos.md` procurando qualquer hex
citado no texto do prompt e confere contra `brand/tokens/skill_test.tokens.json` (para
`graf-NN`/`diag-NN` isso já é estrutural, porque o código lê o token em runtime — não precisa
de verificação separada).

### O que a etapa 10 (gate humano) passa a mostrar

Acrescentar ao que já é apresentado: um inventário visual do post — capa (status: gerada/
pendente) + lista de `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN` com tipo e status. Simples adição
de uma seção ao que a etapa 10 já lê antes do `AskUserQuestion`.

---

**Aguardando sua aprovação antes de implementar.** Pontos que pedem decisão sua especificamente:

1. Dimensão de capa: seguir com 16:9/2400×1350 + regra de zona segura central, até eu
   confirmar o número oficial (vou tentar de novo, ou você pode colar o texto da página se o
   fetch continuar bloqueado)?
2. Ferramenta de diagrama: Plotly (zero dependência nova, layout manual) — de acordo, ou prefere
   que eu avalie Graphviz a sério (instala `dot`, ganha layout automático, mas é dependência
   nova a documentar no `README.md`)?
3. Os quatro diffs de integração (placeholders, etapa 2, etapa 8, etapa 9, etapa 10) — aprovo
   tudo, ou quer ir item a item como na Fase 1?
