# Épico — rascunhos como entrada, capa/ilustração com validação, colagem revisada

Proposta em resposta ao diagnóstico de `00-diagnostico.md`. Três frentes, cada uma com
histórias, critério de pronto e classificação de risco (mesma escala de
`pesquisa/auditoria-sistema/01-proposta.md`: baixo = documentação, sem mudar comportamento;
médio = muda o que uma skill instrui, precisa ser testado num post real antes de dar como
concluído). Nenhum item aqui mexe em post/`_arquivo` já publicado — é tudo mudança de skill,
para posts futuros.

**Fora de escopo, por pedido do autor:** `graficos.md` e `diagramas.md` continuam exatamente
como estão.

---

## Frente 1 — o arquivo de entrada é um rascunho, não uma transcrição

### Por que é a de maior impacto por menor esforço

O caso real (`2026-09-01`) já provou que o executor consegue lidar bem com marcadores de
rascunho — o problema não é capacidade, é que nada garante repetição. Formalizar isso é, na
maior parte, redação: nomear uma prática que já funcionou uma vez.

### 1.1 — Etapa 0 passa a produzir um inventário de marcadores, não só o texto limpo

**Mudança:** `.claude/skills/post-substack/SKILL.md`, etapa 0. Hoje: "cópia limpa (hesitação
removida, palavras do autor preservadas)". Passa a exigir também: **toda anotação entre
colchetes (ou qualquer outra marca visualmente distinta de prosa corrida) é extraída, listada
verbatim, e classificada** — não como taxonomia fechada nova, mas nomeando os quatro padrões
já observados no corpus real, para reconhecimento rápido:

- **Estrutural** — decide algo do pipeline (`[LINHA EDITORIAL: ...]`).
- **Sugestão de visual** — ideia de capa/ilustração (`[CAPA: ...]`, e qualquer equivalente que
  apareça solto no corpo — ver Frente 2).
- **Instrução de escrita** — pede um trecho novo ou revisão de um existente
  (`[escrever um parágrafo sobre X]`, `[tentar reescrever o parágrafo acima]`).
- **Nota de conteúdo** — dado, fonte ou ressalva que o autor quer garantir que apareça, sem
  ditar a frase.

Sem inventar sintaxe nova obrigatória — o autor já escreve colchetes livremente e isso
funciona; a regra é *sempre extrair e listar*, nunca deixar um marcador se perder dentro da
prosa "limpa" sem registro à parte.

**Saída:** `00-transcricao.md` continua existindo (texto limpo), mas ganha uma seção final
"Marcadores extraídos do rascunho" — cada um com o texto literal, a classificação, e (vazio
nesta etapa) um campo "resolução", preenchido pelas etapas seguintes.

**Risco:** baixo — muda o texto de uma etapa de skill, não o comportamento de subagente.

### 1.2 — Etapa 1 (briefing) fecha todo marcador estrutural e de conteúdo, ou registra tensão explícita

**Mudança:** `post-substack/SKILL.md`, etapa 1, ganha frase obrigatória: para cada marcador
**estrutural** ou de **nota de conteúdo** listado em `00-transcricao.md`, o briefing declara
a resolução — ou aplica, ou registra a tensão **como pergunta binária nomeada**, não como
prosa dissolvida em uma lista de pendências genéricas. É a correção direta do achado 2 do
diagnóstico: a tensão de linha editorial existiu, mas nunca virou uma pergunta que alguém
respondesse "sim" ou "não" — foi carregada em silêncio até a aprovação final.

**Critério de pronto:** se o gate humano (etapa 10) aprova um post e existia uma tensão
estrutural registrada na etapa 1, o resumo apresentado ao autor tem que citar essa tensão
**nominalmente**, separada da lista de `[VERIFICAR]` técnicos — não misturada.

**Risco:** médio — muda o que a etapa 1 e a etapa 10 exigem uma da outra; testar no próximo
post que tiver algum marcador estrutural real.

### 1.3 — Instrução de escrita vira item de saída da etapa 4, com registro de como foi atendida

**Mudança:** etapa 4 (draft) do `post-substack/SKILL.md` ganha frase: toda marcador do tipo
**instrução de escrita** listado em `00-transcricao.md` precisa aparecer, no `04-draft-v1.md`,
com uma nota lateral de "como foi atendida" (o parágrafo que resolve, ou por que não foi
possível) — hoje isso existiu só porque `01-briefing.md` (achado 1) improvisou uma seção
"Pendências que a etapa 4 precisa resolver"; a proposta é garantir que a ponte entre etapa 0/1
e etapa 4 não dependa de o executor lembrar de criar essa seção por conta própria.

**Risco:** baixo — é rastreabilidade, não muda a prosa final em si.

---

## Frente 2 — capa e ilustração: validar sugestão do rascunho, dar espaço a ideia própria

### 2.1 — Toda sugestão de visual no rascunho vira um veredito escrito, com três saídas possíveis

**Mudança:** `.claude/skills/prompts-visuais/references/briefing-ilustracao.md`, Passo 1
(Camada 1), ganha uma sub-regra nomeada: quando o rascunho contém uma **sugestão de visual
explícita** (marcador `[CAPA: ...]` ou equivalente identificado pela Frente 1), o Passo 6
(Escolha e defesa) é obrigado a incluir uma seção **"Proveniência"** com um veredito entre três
saídas, cada uma com justificativa:

1. **Aproveitar a estrutura** — extrai a lógica da sugestão, descarta a referência literal se
   ela violar regra de marca ou propriedade (é exatamente o que `capa.md` já fez com a
   referência a Terminator — a proposta é tornar esse comportamento exigido, não incidental).
2. **Aproveitar literalmente** — a sugestão já cabe nas regras de estilo/marca sem ajuste;
   registrar por que não havia conflito a resolver.
3. **Descartar** — com motivo por escrito (ex.: contradiz a linha editorial, força um clichê,
   reprova em algum teste de rejeição do Passo 5) — nunca descarte silencioso.

Formaliza o padrão de `capa.md` linhas 18–25 como regra, não como exceção de sorte.

### 2.2 — O executor sempre gera pelo menos uma alternativa própria, mesmo com sugestão do autor

**Mudança:** mesma seção de `briefing-ilustracao.md`, Passo 3 (as três operações). Ganha
regra: **quando existe sugestão do autor**, rode as três operações (extensão, cruzamento,
torção) sobre ela **e também**, independentemente, gere pelo menos um conceito que não parta
da sugestão — usando só Camada 2/3 (objetos concretos do texto) como semente. O Passo 6
(Escolha e defesa) compara os dois lados lado a lado e diz qual venceu e por quê — igual ao
que já faz para conceitos concorrentes vindos da mesma semente. Isso não é desconfiança da
ideia do autor: é a mesma disciplina que qualquer outro passo do pipeline já aplica (a etapa 5
existe para testar o draft contra alternativas, não para aceitá-lo de primeira).

**Sem sugestão do autor**, nada muda — o método já é gerativo por padrão (Passo 3 já exige
pelo menos um conceito por operação).

### 2.3 — Varredura do rascunho inteiro por sugestão de visual solta, não só o marcador dedicado

**Mudança:** `post-substack/SKILL.md`, etapa 0 (via a mesma extração da Frente 1.1) — a
categoria "sugestão de visual" não fica restrita ao marcador `[CAPA: ...]` no topo do arquivo;
qualquer trecho do corpo que proponha, sugira ou descreva uma imagem (mesmo sem colchete
formal — um parêntese, uma frase solta) entra no inventário de marcadores com essa
classificação e chega à etapa 8 pelo mesmo caminho.

**Critério de pronto (2.1–2.3):** o próximo post cujo rascunho tiver qualquer sugestão de
visual — de capa ou de corpo — precisa produzir, em `processo/08-briefing-visual.md`, a seção
"Proveniência" com veredito explícito e pelo menos duas alternativas comparadas por escrito.

**Risco:** médio — muda o método de briefing visual; testar no próximo post com sugestão real
antes de considerar fechado (o post `2026-09-01` já serve de caso de regressão: reaplicar o
método novo a ele, mentalmente, deveria reproduzir uma decisão pelo menos tão boa quanto a que
já existe em `capa.md`).

---

## Frente 3 — colagem como padrão, com revisão de marca antes e depois da geração

### 3.1 — Enriquecer o vocabulário compositivo do Estilo A, filtrado pela marca

**Mudança:** `.claude/skills/prompts-visuais/references/estilos-ilustracao.md`, seção
"Estilo A", ganha uma tabela nova (no mesmo formato da tabela de candidatos descartados do
Estilo B, linhas 114–121) avaliando as abordagens compositivas de colagem que **não** têm
equivalente hoje (fonte: Olga Tkachenko, "10 Collage Approaches You're About to Use and Get
Inspired by", Muzli/Medium — ver Fontes):

| Abordagem nova candidata | Veredito proposto | Justificativa |
|---|---|---|
| Multiplicação/fragmentação de um objeto | **Adotar, com limite** | Serve para argumento sobre repetição, escala ou padrão sistêmico (ex.: um post sobre efeito em cascata) — mas conflita com "Uma ideia, uma família de objetos" (`briefing-ilustracao.md` linha 123) se usada fora desse caso; usar só quando a multiplicação *é* o argumento, não decoração |
| Objeto reconhecível como dispositivo de escala | **Adotar** | Já é compatível com "Estranhamento de objeto comum" (`briefing-ilustracao.md` linha 117) — só nomeia um uso específico dessa regra já existente |
| Composição suprematista harmonizada | **Adotar, nomear formalmente** | Já permitido implicitamente em "Quando o assunto é abstrato" (`estilos-ilustracao.md` linha 102); a mudança é só dar critério explícito de "harmonização" (poucas formas geométricas, relação de peso e eixo clara) em vez de deixar aberto |
| Colagem com traço desenhado à mão | **Rejeitar** | Introduz variação caligráfica; conflita com a regra de geometria reta e sem traço à mão que já separa o Estilo A do Estilo B (`estilos-ilustracao.md` linha 155, aplicada por oposição) |
| Caos deliberado, influência Dada | **Rejeitar (mantém regra atual)** | Já explicitamente descartado — "isso é o que separa esta colagem de colagem bagunçada genérica" |

**Nota de proveniência cultural:** mesma regra que já vale para referência de cultura pop
(`briefing-ilustracao.md` linhas 169–181) — da fonte externa se extrai a **abordagem
compositiva**, nunca um exemplo visual específico de um artista vivo a copiar. A tabela acima
já é essa extração.

**Risco:** baixo — é enriquecimento de referência, não muda um prompt já escrito.

### 3.2 — Checagem mecânica da imagem gerada, não só do prompt

**Mudança:** o item 10 de `.claude/skills/revisao-editorial/SKILL.md` audita hoje só o texto
do prompt. Proposta: quando `ilu-NN` ou a capa tiverem sido de fato geradas (PNG salvo em
`posts/<slug>/figuras/`), a etapa 9 roda uma checagem adicional — extrair a paleta dominante
do PNG (ex.: `Pillow` + quantização de cor, já que `python3` está liberado em
`allowed-tools` de `revisao-editorial` e `prompts-visuais`) e comparar contra os hex
autorizados de `brand/tokens/skill_test.tokens.json`, com tolerância definida (a definir com o
autor — cor de compressão JPEG/PNG nunca bate 100% com o hex pedido). Confirmado nesta sessão:
`Pillow` 12.1.1 já está instalado no ambiente — a Frente 3.2 não depende de instalar nada
novo. Cor fora da tolerância
vira pendência para o gate humano, no mesmo padrão do item 10 atual — não é bloqueio automático,
é sinalização.

**Por que isso importa mais do que parece:** é o único ponto do sistema onde uma peça final
passa por um gerador de imagem externo sem nenhuma garantia determinística de cor — todo o
resto (`graf-NN`, `diag-NN`) já é seguro porque o código lê o token em runtime.
Pesquisa de mercado confirma que esse é um problema conhecido e ativamente enfrentado por
ferramentas de conformidade de marca em 2026 — ver Fontes.

**Risco:** médio-alto — é a única história do épico que introduz uma ferramenta técnica nova
(extração de paleta de imagem), não só texto de skill. Proposta de implementação mínima antes
de qualquer coisa mais sofisticada: script Python simples, sem dependência nova além do que
já estiver disponível (`Pillow` — confirmar se já está instalado, como `plotly`/`kaleido` já
estão para `graf-NN`). Não vale a pena adotar uma ferramenta SaaS de terceiros para isso —
volume de imagens do repositório (uma capa + poucas ilustrações por post) não justifica.

---

## Priorização por impacto

1. **Frente 1 (rascunho → marcadores)** — maior impacto, menor esforço. É nomear uma prática
   já provada, sem ferramenta nova.
2. **Frente 2 (capa/ilustração: veredito + alternativa)** — impacto editorial alto (evita
   literal-copy de referência de terceiros, evita ancoragem na primeira ideia), esforço médio
   (muda método de um subagente, precisa validação em post real).
3. **Frente 3.1 (vocabulário de colagem)** — impacto qualitativo, esforço baixo — pode andar
   em paralelo, não depende das outras duas.
4. **Frente 3.2 (checagem mecânica de pixel)** — maior impacto de risco (fecha o único ponto
   sem garantia de marca), mas maior esforço técnico e o menos urgente hoje, porque nenhuma
   imagem de `ilu-NN`/capa foi gerada ainda em nenhum post do corpus — vale endereçar antes da
   primeira geração real acontecer, não necessariamente antes das Frentes 1 e 2.

## Não fazer

- Não redesenhar `graficos.md`/`diagramas.md` — fora do pedido, e o diagnóstico (achado 7-8)
  já mostra que eles não têm o mesmo problema.
- Não impor uma sintaxe de marcador fechada e obrigatória (tags fixas tipo `[ESCREVER: ]`) —
  o padrão livre já funciona; a mudança é garantir extração e resolução, não sintaxe.
- Não reabrir ou regenerar visuais de posts já publicados — vale só para posts novos, mesma
  regra que já existe para a mudança de sistema de marca (`CLAUDE.md`, nota de 31/08/2026).
- Não adotar ferramenta SaaS de verificação de marca por imagem — volume não justifica; script
  local resolve.

## Perguntas em aberto para o autor

1. Tolerância de cor da Frente 3.2 (achado 7 do diagnóstico) — quanto de desvio de hex é
   aceitável antes de virar pendência? Depende de testar com uma imagem real gerada, que ainda
   não existe no corpus.
2. A Frente 1.2 propõe que toda tensão estrutural apareça como pergunta nomeada no gate
   humano — isso pode tornar a etapa 10 mais longa em posts com múltiplas tensões. Aceitável,
   ou prefere um teto (ex.: só a primeira tensão vira pergunta obrigatória, as demais ficam em
   lista)?
3. Ordem de implementação sugerida (1 → 2 → 3.1 → 3.2) ou o autor prefere atacar primeiro o
   que afeta o próximo post em fila?

## Fontes

- Olga Tkachenko, ["10 Collage Approaches You're About to Use and Get Inspired by"](https://medium.muz.li/10-collage-approaches-youre-about-to-use-and-get-inspired-by-5c45bcb1aba4), Muzli/Medium — catálogo de abordagens compositivas usado na Frente 3.1 (acesso via busca; fetch direto bloqueado por 403 do Medium nesta sessão, conteúdo confirmado por múltiplos resultados de busca convergentes).
- TheArtStory, ["Collage - Modern Art Terms and Concepts"](https://www.theartstory.org/definition/collage/) — vocabulário de papiers collés, decoupage, fotomontagem, usado para checar terminologia da Frente 3.1.
- Pesquisa de mercado (WebSearch, 2026-09-01) sobre ferramentas de conformidade de marca para imagem gerada por IA — confirma que "drift" de cor entre prompt e imagem final é problema ativo do setor (ex.: verificadores semânticos que comparam paleta gerada contra paleta de marca e rejeitam/regeneram), usado para fundamentar a Frente 3.2. Fontes específicas: [goodeye.dev](https://goodeye.dev/guides/best-tools-ai-images-on-brand), [goodeyelabs.com](https://www.goodeyelabs.com/articles/top-ai-brand-compliance-tools-2026).
