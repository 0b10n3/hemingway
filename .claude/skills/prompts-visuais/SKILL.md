---
name: prompts-visuais
description: Gera a capa obrigatória (capa.md), os prompts de imagem (ilustracoes.md), as specs de gráfico e diagrama com código Plotly executável (graficos.md, diagramas.md) e, condicional, o infográfico (infograficos.md) de um post, a partir da estrutura definida na etapa 2 do pipeline. Use na etapa 8 do post-substack, ou isoladamente quando pedirem para "gerar os visuais" de um texto que já tem os placeholders ilu-NN/graf-NN/diag-NN/info-NN marcados.
disable-model-invocation: true
argument-hint: [caminho-do-slug-em-posts/]
allowed-tools: Read Write Edit Glob Grep Bash(python3 *)
---

Lê `posts/<slug>/processo/02-estrutura.md` (onde cada `ilu-NN`/`graf-NN`/`diag-NN`/`info-NN`
foi decidido e por quê, pelo critério da "Etapa 2" em `post-substack/SKILL.md`) e
`posts/<slug>/04-draft-v1.md` ou o draft mais recente em `processo/`, e produz os entregáveis
visuais: `capa.md` sempre, os demais quando o post tiver a peça correspondente. Usa
`marca-syntaxis` para paleta/tipografia — leia `../../../../../brand/DESIGN.md` e
`../../../../../brand/tokens/syntaxis.tokens.json` antes de escrever qualquer prompt ou código
(ver nota de 31/08/2026 em `marca-syntaxis/SKILL.md`: posts publicados antes dessa data usam o
sistema anterior e não são referência para trabalho novo).

**Gerador ativo hoje:** Nano Banana Pro (Gemini) — ver
`references/geradores/nano-banana-pro.md`. Trocar de gerador é trocar esta linha e apontar
para o adaptador correspondente (`references/geradores/<gerador>.md`); nenhuma outra
referência deste sistema muda. Todo prompt final em `ilustracoes.md`/`capa.md` declara no
cabeçalho para qual gerador foi escrito.

## `capa.md`

Sempre presente — todo post tem exatamente uma capa. Nasce da **tese em uma frase e do gancho
escolhido em `processo/01-briefing.md`**, nunca de um detalhe do corpo do texto: a capa
comunica a tese, não uma evidência de apoio.

- **Estilo:** colagem editorial, mesma referência de `references/estilos-ilustracao.md` usada
  por `ilu-NN` — vale para todo post, qualquer linha editorial (unificado em 2026-09-01).
  Mesma paleta fechada, mesmas regras.
- **Proporção:** 16:9. Gerar em 2400×1350px (margem confortável acima do alvo de publicação)
  e exportar em 1456×816px para a capa do artigo — dimensão convergente em múltiplas fontes
  secundárias (a Substack gera separadamente um thumbnail 1200×630 por recorte automático
  para e-mail/redes, não é ativo que este sistema precise produzir).
  `[VERIFICAR: página oficial de suporte da Substack bloqueou fetch automático em duas
  tentativas (auditoria-2026 e a revisão de pesquisa/frente-e-visuais/) — número acima é
  convergência de fontes secundárias, não confirmação primária; revisitar se a Substack
  disponibilizar acesso]`.
- **Zona segura.** O elemento de foco da composição (o ponto que carrega o argumento) deve
  ocupar o terço central do quadro, nunca a periferia — a Substack recorta a mesma imagem em
  nove formatos diferentes, e composições com respiro nas bordas arriscam ter o foco cortado.
- **Formato do bloco:** mesmo formato de `ilu-NN` abaixo (conceito e estrutura de metáfora,
  linha editorial e estilo aplicado, prompt completo, restrições em enquadramento positivo,
  alt-text), com um campo a mais — **Zona segura** — descrevendo em uma frase onde o elemento
  de foco fica posicionado no quadro.
- **Promoção a `ilu-01`:** se o autor decidir reusar a capa também no corpo do post, ela ganha
  placeholder próprio em `ilustracoes.md` — nunca é referenciada por caminho cruzado entre os
  dois arquivos.
- **Variantes derivadas (opcional, só quando o post for divulgado no LinkedIn):** campo
  "Variantes" ao final do bloco de `capa.md` — não vira arquivo à parte, é a mesma decisão de
  capa reenquadrada, e `capa.md` já é a fonte única da capa.
  - **LinkedIn feature image** — 1200×627px, 1.91:1.
  - **LinkedIn feed** — 1080×1350px, 4:5, retrato.
  - Mesma metáfora da capa principal, reenquadrada — nunca um conceito novo. A composição
    original já deve prever essa margem de recorte (zona segura mais generosa no eixo que
    muda de proporção entre as variantes).
  - Gerado só quando o post for de fato programado para divulgação no LinkedIn — não é
    obrigatório por padrão.

## `ilustracoes.md`

### Antes de escrever qualquer prompt

Desde 2026-09-01, o estilo artístico **não depende mais da linha editorial** — colagem
editorial vale para todo post (ver `references/estilos-ilustracao.md`, "Por que um estilo
só"). A linha editorial ainda importa para outras decisões do pipeline (frontmatter, encaixe
no funil), mas não bloqueia mais a etapa 8: não é preciso confirmar linha editorial antes de
escrever um prompt de ilustração.

O que a etapa 8 ainda decide, por post, é a **composição**: registro pessoal/assimétrico
(quando o argumento é relato ou virada) ou registro de precisão mecânica/centrado (quando o
argumento é mostrar um mecanismo por dentro) — ver "Quando o argumento pede precisão mecânica"
em `references/estilos-ilustracao.md`. Essa escolha vem do conceito de cada `ilu-NN`
(`processo/08-briefing-visual.md`), não de uma regra fixa por linha.

Especificação completa do estilo, hex autorizados e checklist de prompt:
**`references/estilos-ilustracao.md`** — leia antes de escrever o primeiro prompt.
**`references/templates-prompt.md`** dá o esqueleto preenchível, com a extensão de precisão
mecânica — não repete a tabela de hex nem as regras, só acelera a escrita e reduz prompt vago.

### Etapa 8a — briefing antes do prompt (obrigatório)

**Nunca vá do texto direto ao prompt.** Rode primeiro o método de
**`references/briefing-ilustracao.md`** e grave o resultado em
`processo/08-briefing-visual.md`: colheita de material em três camadas (a metáfora do autor
primeiro) → a frase que a peça carrega → as três operações geradoras (extensão / cruzamento
/ torção) → critérios positivos de beleza → testes de rejeição, incluindo o teste da
fatalidade → escolha com os descartes anotados → composição de cena (Passo 7 — objetos,
disposição espacial, foco, sem sintaxe de gerador ainda).

Esse passo existe porque a primeira rodada do sistema de estilos produziu peças tecnicamente
corretas e editorialmente mudas: escada espelhada e cápsula-câmara-cápsula, conceitos
importados de fora do texto enquanto os posts ofereciam o sumário do Hull, o compulsório de
21% contra 20% e o "outro lado do balcão" sem ninguém pegar. **Estilo é a última decisão, não
a primeira.**

### Formato de cada bloco `ilu-NN`

- Onde entra no texto e que ideia carrega (referencie o parágrafo/seção de `post.md`).
- **Conceito e estrutura de metáfora** — o conceito escolhido em `08-briefing-visual.md`, a
  estrutura usada (justaposição / fusão / substituição) e o material do texto que ele usa.
- **Registro de composição aplicado**, em uma linha — pessoal/assimétrico ou precisão
  mecânica/centrado (ver `estilos-ilustracao.md`) e por quê. Deixa auditável, na própria peça,
  por que ela ficou com essa cara.
- Prompt completo para `GERADOR_IMAGEM` (Google Nano Banana Pro): cena narrada seguindo
  `[Sujeito] + [Ação/estado] + [Contexto] + [Composição] + [Estilo e materialidade] +
  [Paleta com hex] + [Proporção]`, com os hex citados por nome do token (ex. "flat deepForest
  background #0F3D27"), proporção e resolução explícitas.
  Escreva o prompt em inglês se o gerador responde melhor assim, mas sempre com uma nota de
  contexto em português logo abaixo — quem relê esse arquivo depois é o autor, não o gerador.
- **Restrições em enquadramento positivo** — o que a peça deve ter, não o que deve evitar.
  O Nano Banana Pro **não suporta negative prompt** (ver `references/estilos-ilustracao.md`,
  "Como escrever o prompt"): o guia oficial recomenda enquadramento positivo no lugar. Por isso
  esta seção substituiu o antigo bloco `### Negative prompt` — escrever um era teatro, o
  gerador nunca leu.
- Alt-text final — vai para o `post.md` como texto alternativo do placeholder e sustenta o
  post caso a imagem não carregue, então precisa ser descritivo por si só, não decorativo.

### Revogado em 31/08/2026

A regra do **"elemento iluminado"** (contraste por glow verde sobre fundo escuro), que
governava as ilustrações dos posts de agosto/2026, **não vale mais**: `brand/DESIGN.md` §4.5
lista "gradientes, glassmorphism, blobs desfocados, **glows**" como anti-padrão verificável.
Contraste agora se faz por cor chapada, densidade e escala. As `ilustracoes.md` já publicadas
não foram reescritas (mesma regra de `_arquivo/`: registro do que foi feito não se maquia) —
mas não são referência para peça nova.

## `graficos.md`

Antes de escrever qualquer spec, leia `references/checklist-graficos.md` — anotação,
revelação progressiva e contraste genuíno vs. forçado.

Um bloco por `graf-NN`:

- **Pergunta que o gráfico responde**, em uma frase. Se não couber numa frase, o gráfico está
  fazendo duas coisas — volte à etapa 2 e separe em dois `graf-NN`.
- **Fonte dos dados**, com link e data de acesso — ou `[VERIFICAR]` se `07-verificacao.md`
  não fechou essa fonte.
- **Dados** salvos em `posts/<slug>/graficos/dados/graf-NN.csv`, versionados junto — um
  gráfico cujo dado não está no repositório não é reproduzível seis meses depois.
- **Código Plotly executável**, em bloco ` ```python `, autocontido: lê o CSV ao lado por
  caminho relativo, aplica os tokens de `../../../../../brand/tokens/syntaxis.tokens.json` (leia o
  JSON em runtime ou copie os valores `$value` exatos com comentário apontando a origem —
  nunca hardcode cor fora do tokens.json), exporta para `posts/<slug>/figuras/graf-NN.svg` e
  `.png`. Cada bloco roda sozinho, sem preâmbulo — teste com `python3` antes de considerar a
  etapa concluída.
- **Escolha de tipo de gráfico justificada** em uma linha, e o que foi descartado.
- **Alt-text e legenda.**
- **Anotação**: todo ponto de interesse tem `add_annotation` apontando para ele (ver
  `references/checklist-graficos.md`).

## `diagramas.md`

Presente quando `02-estrutura.md` decidiu por `diag-NN` (relação estrutural, fluxo, processo
ou linha do tempo sem métrica central — ver critério da "Etapa 2" em `post-substack/SKILL.md`).
**Ferramenta: Plotly**, estendendo o mesmo padrão de `graf-NN` — nós e setas via `add_shape`/
`add_annotation`, não uma biblioteca de diagrama dedicada. Decisão registrada e justificada em
`pesquisa/auditoria-2026/02-processo-visual.md`: já testado neste ambiente (`plotly`/`kaleido`
instalados), mesma fidelidade a `DESIGN.md` já obtida em `graf-NN`, sem dependência de sistema
nova. Se um diagrama futuro precisar de layout automático com muitos nós (>8-10), reabra a
decisão — nenhum caso previsto hoje chega perto disso.

Um bloco por `diag-NN`, mesmo formato de `graf-NN`: pergunta que o diagrama responde em uma
frase; fonte dos dados só se houver número real embutido (senão, omitir a seção); código
Plotly executável, autocontido, lendo `../../../../../brand/tokens/syntaxis.tokens.json` em
runtime, exportando `posts/<slug>/figuras/diag-NN.svg` e `.png`; escolha de layout justificada
em uma linha; alt-text.

## `infograficos.md` (condicional — padrão é não ter)

Só existe quando **nenhum** `graf-NN`/`diag-NN`/`ilu-NN` isolado carrega a síntese sozinho —
quando o ponto só existe na leitura conjunta de duas ou mais peças, e separá-las forçaria o
leitor a montar a relação de cabeça. Não é gatilho: "ficaria bonito consolidado", "tenho fatos
soltos" ou variar o formato. Antes de propor um `info-NN`, confirme que nenhuma peça separada
resolveria — esse é o teste, não gosto de quem está montando o post.

Um bloco por `info-NN`: hierarquia de leitura explícita (o que o olho vê primeiro/segundo/
terceiro — obrigatório, não implícito no layout); dado com fonte, como `graf-NN`; tokens
usados; código/prompt de geração (Plotly para a parte de dado real; formato de `ilu-NN` para
elemento de apoio ilustrativo, se houver); alt-text.

## Regra de placeholder no `post.md`

Cada imagem/gráfico/diagrama/infográfico vira, no texto:

```markdown
![Ilustração: <legenda descritiva curta>](ilu-01)
![Gráfico: <legenda descritiva curta>](graf-01)
![Diagrama: <legenda descritiva curta>](diag-01)
![Infográfico: <legenda descritiva curta>](info-01)
```

A capa não tem placeholder inline — vai direto ao campo de capa/imagem de destaque do
Substack, nunca referenciada dentro do corpo de `post.md`.

A legenda no alt-text não é opcional — é o que sustenta o post se a imagem falhar ao
carregar, então tem que carregar a ideia sozinha.
