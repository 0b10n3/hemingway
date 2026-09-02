# Estrutura — Quando os Modelos se Rebelam

Arco completo (`tecnicas-narrativas.md`): o texto tem múltiplos casos/fontes reais (Derman,
MacKenzie, Black–Scholes/Joesley Day, LTCM, London Whale) e fechamento ensaístico com
aforismo autoral, conforme `01-briefing.md`. A divisão em seções numeradas já existente no
rascunho é sólida e mantida quase 1:1 — só os dois ajustes de conteúdo pedidos pelo próprio
autor (seção 3 e Fechamento) ficam pendentes para a etapa 4.

## Abertura — a moeda de Kempthorne — **gancho**

- **O que prova:** planta a cena (aula do MIT, citação sobre a moeda que sai cara 100 vezes
  seguidas) e a pergunta que o texto inteiro responde: o que significa "esperar o retorno à
  média" quando a própria média pode ter mudado. Fecha antecipando a tese sem ainda
  desenvolvê-la ("o desacoplamento entre modelo e realidade pode levar até vencedores do
  Nobel ao desastre").
- **Ato:** gancho.

## 1. "Três palavras que você usa como sinônimo e não são" — **contexto**

- **O que prova:** instala o vocabulário central — teoria, modelo, intuição (Derman) — e o
  testa contra a filosofia da ciência (Cartwright, Box, Duhem–Quine, a visão semântica de
  Suppes/van Fraassen/Giere). Conclui que a distinção "bate em parte": é ferramenta de
  ancoragem, não parede absoluta. As duas tabelas do rascunho (Teoria x Modelo; ponto de
  Derman x filosofia da ciência) carregam essa comparação.
- **Ato:** contexto — sem isso, "hipótese" e "modelo" nas seções seguintes não têm onde
  pousar.
- **Pilar:** narrativa.
- **Visual:** nenhum além das duas tabelas nativas — ver "O que fica de fora".

## 2. "O radar da rodovia" — **contexto (continuação, fora de finanças)**

- **O que prova:** leva a ideia de "premissa que pode quebrar" para um caso sem viés
  comportamental — um radar de velocidade — e fixa a frase-guia do texto: "a matemática
  seguiria perfeita; o cenário é que teria mudado". Prepara o leitor para reconhecer o mesmo
  padrão nos dois casos financeiros seguintes.
- **Ato:** contexto, última parada antes da ação crescente.
- **Pilar:** visual. Entra **`ilu-01`** aqui — pelo critério 3 da etapa 2
  (`post-substack/SKILL.md`): a metáfora é do próprio autor, tem objeto concreto (carro,
  sensores, intervalo de medição) e carrega o argumento sozinha. Não é `diag-NN`: não é
  relação estrutural entre entidades abstratas, é cena com objeto físico reconhecível.

## 3. "Black–Scholes: o que está na bula" — **ação crescente**

- **O que prova:** primeiro desastre real. As hipóteses do modelo (trajetória contínua,
  rebalanceamento em tempo contínuo) quebram no pregão de 18/05/2017 — ninguém conseguiu
  rebalancear porque não existiu preço no meio do caminho. Fecha com a reflexividade de
  MacKenzie (o modelo que empurra o mercado, não só o descreve) e o caso brasileiro do target
  forward de 2008.
- **Ato:** ação crescente — primeiro caso que prova a tese em dinheiro real.
- **Pilar:** dado. Entra **`graf-01`** aqui — critério 1: há série numérica real a comparar
  (Ibovespa 17/05 vs. 18/05/2017, intradiário -10,47%, fechamento -8,80%; dólar de R$ 3,14 a
  R$ 3,38) mostrando o salto que quebrou a premissa de continuidade. Especificação exata de
  dado fica para as etapas 3 e 7; aqui só se fixa o tipo de peça.
- **Pendência de conteúdo:** falta o parágrafo-definição de Black–Scholes pedido entre
  colchetes no rascunho (ver `01-briefing.md`) — resolvido na etapa 4, não aqui.

## 4. "LTCM: quando dois Nobéis descobrem que o mundo não satisfaz as equações" — **clímax**

- **O que prova:** o caso mais forte do texto — dois ganhadores do Nobel, alavancagem 25:1, e
  a premissa "mais invisível e mais letal": liquidez. Mecânica em ciclo — calote russo → fuga
  para qualidade → spreads divergem em vez de convergir → chamada de margem → venda forçada →
  preços pioram ainda mais contra as posições que restam.
- **Ato:** clímax.
- **Pilar:** dado e visual. Entra **`diag-01`** aqui — critério 2: não há uma métrica central
  única a plotar (o argumento é a mecânica do ciclo, não um número isolado), mas há relação
  estrutural clara entre entidades nomeadas em sequência causal (Rússia, LTCM, Treasuries,
  Fed de Nova York) — fluxo, não comparação abstrata de dois blocos. Os números (perda,
  alavancagem, nocional) entram como anotação dentro do próprio fluxo, evitando fatiar o
  mesmo caso em duas peças concorrentes.

## 5. "As duas patologias" — **resolução (parte 1: diagnóstico)**

- **O que prova:** nomeia os dois erros de interpretação — fundamentalista (nunca admite que
  o modelo errou) e niilista (abandona modelos por completo) — com o London Whale (JPMorgan,
  2012) como caso-limite do primeiro. As duas patologias compartilham a mesma raiz: confundir
  modelo com teoria, fechando o círculo aberto na seção 1.
- **Ato:** resolução, primeira metade — nomeia o problema antes de prescrever a solução
  prática da seção 6.
- **Pilar:** narrativa.
- **Visual:** nenhum — ver "O que fica de fora".

## 6. "A ficha técnica" — **resolução (parte 2: prática)**

- **O que prova:** converte o diagnóstico em ferramenta de uso — os cinco compromissos do
  *Financial Modelers' Manifesto* e a tabela de seis perguntas que o analista deveria saber
  responder antes de entregar qualquer número saído de modelo.
- **Ato:** resolução, segunda parte — "e daí, o que eu faço com isso".
- **Pilar:** nenhum adicional — a tabela nativa do rascunho já é a peça.

## Fechamento — **fechamento (ensaístico)**

- **O que prova:** fecha com a imagem da alavanca ("multiplica competência tanto quanto
  multiplica burrice, e com a mesma indiferença") e o aforismo final. Fechamento ensaístico
  puro, sem CTA explícito no rascunho — etapa 4 decide se adiciona um, seguindo o padrão do
  corpus.
- **Pendência de conteúdo:** o parágrafo sobre "não existem teorias no sentido forte [em
  finanças]" precisa da reescrita pedida entre colchetes — resolvida na etapa 4, ecoando a
  nuance já registrada na seção 1 (visão semântica das teorias), não a frase categórica
  original. **Correção pós-etapa-5:** a primeira passada do draft ecoou essa nuance
  introduzindo um exemplo novo (não-arbitragem como "teoria quase axiomática") que contradiz
  a seção 3, onde não-arbitragem é tratada como consequência derivada das premissas do
  modelo, não teoria autônoma — ver `05-critica.md`, achado 2. O eco correto reaproveita
  literalmente o vocabulário da seção 1 (visão semântica de Suppes/van Fraassen/Giere: teoria
  também é família de modelos; finanças mora do lado em que o objeto reage ao modelo), sem
  introduzir exemplo novo.

## Três pilares — confirmação

- **Dado:** seção 3 (Ibovespa/dólar, 18/05/2017) e seção 4 (números do LTCM).
- **Narrativa:** seção 1 (taxonomia Derman + filosofia da ciência) e seção 5 (as duas
  patologias).
- **Visual:** `ilu-01` (seção 2), `graf-01` (seção 3), `diag-01` (seção 4).

Os três pilares estão representados; nenhum ausente.

## O que fica de fora (deliberadamente)

- **Diagrama para a taxonomia Teoria/Modelo/Intuição (seção 1):** cotado e descartado — é
  comparação de conceitos abstratos sem objeto concreto por trás, exatamente o alerta do
  critério 2 da etapa 2 ("diagrama fantasiado de ilustração"), já registrado como erro real em
  `posts/2026-08-17-o-mundo-invertido-das-carreiras-em-financas/ilustracoes.md` (revisão de
  `ilu-02`). **As duas tabelas nativas (Teoria x Modelo; ponto de Derman x filosofia da
  ciência) entram no draft como tabela markdown de verdade, sem ID de visual** — nunca como
  placeholder `graf-NN`/`diag-NN`/`ilu-NN` (correção pós-etapa-5: a primeira passada do draft
  rotulou esse trecho como `graf-01` por engano, colidindo com o `graf-01` real da seção 3;
  ver `05-critica.md`, achado 1).
- **Ilustração ou diagrama para "as duas patologias" (seção 5):** mesmo motivo — fundamentalista
  vs. niilista é literalmente "dois blocos" sem objeto concreto por trás. Fica como texto com
  subtítulos, já a estrutura do rascunho.
- **Gráfico do sorriso de volatilidade (seção 3):** ideia genuína (superfície de volatilidade
  implícita deixando de ser plana após 1987), mas o rascunho não tem dado quantificado para
  plotar sem inventar número — proibido por "não invente número" (`CLAUDE.md`). Mantido como
  texto; se a etapa 3 encontrar série real de skew, reabrir.
- **Gráfico de balanço do LTCM além de `diag-01`:** descartado para não fatiar o mesmo caso em
  duas peças concorrentes — o mecanismo do ciclo de liquidez importa mais que o tamanho
  absoluto do balanço; os números entram como anotação dentro do próprio diagrama.
- **Peça visual para a tabela de seis perguntas (seção 6):** é checklist de referência, não
  série nem relação estrutural — a tabela markdown já cumpre a função.
- **Infográfico:** padrão é não ter, e nenhum ponto do texto exige leitura conjunta de duas
  peças para fazer sentido — `ilu-01`, `graf-01` e `diag-01` carregam cada um sua própria
  síntese isoladamente. Critério de gatilho do infográfico não se aplica.

## Nota para a etapa 8 (capa)

O rascunho traz sugestão do autor para o criativo de capa (marcador **sugestão de visual**,
inventariado na etapa 0): uma rebelia de máquinas humanoides "como nos filmes de Terminator".
A *ideia* — ferramenta que deixa de obedecer ao criador, eco direto do título e da frase de
fechamento "um modelo é uma ferramenta que não sabe que é uma ferramenta" — é aproveitável e
forte como metáfora de capa. A referência literal ao filme não é: personagem protegido por
direito autoral/marca, e também fora do estilo de ilustração obrigatório se a linha editorial
confirmada em etapa 10 for Spoiler (colagem editorial — ver `references/estilos-ilustracao.md`
— não pôster cinematográfico de ficção científica). A etapa 8 traduz a ideia (ferramenta em
rebelião) para a linguagem visual da marca, sem citar o filme nem reproduzir design de
personagem reconhecível, e só decide o estilo definitivo depois que a etapa 10 confirmar a
linha editorial (ver tensão registrada em `01-briefing.md`).

## Pendências para pesquisa/verificação (não resolvidas nesta etapa)

- Todos os números do caso Joesley Day (Ibovespa intradiário -10,47%, fechamento -8,80%,
  dólar R$ 3,14 → R$ 3,38) e do LTCM (patrimônio ~US$ 4,7 bi, ativos ~US$ 125 bi, alavancagem
  ~25:1, nocional ~US$ 1,25 tri, perda ~US$ 4,6 bi, resgate ~US$ 3,6 bi) ficam para
  verificação técnica (etapa 7) — nada foi conferido contra fonte primária ainda.
- O caso do target forward de 2008 (Aracruz US$ 2,13 bi, Sadia R$ 2,55 bi, volume total
  estimado US$ 35 bi) e o caso London Whale (>US$ 6 bi) — mesma pendência.
- Citação exata de Kempthorne e a fonte precisa (18.S096 vs. 18.642) — confirmar contra o
  material do MIT OCW na etapa 3.
