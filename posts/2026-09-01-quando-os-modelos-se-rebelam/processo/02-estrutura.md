# Estrutura — Quando os Modelos se Rebelam

Arco completo (`tecnicas-narrativas.md`), porque o texto tem 2+ fontes/casos (Derman,
MacKenzie, Black–Scholes/Joesley Day, LTCM, London Whale, Lakatos/Duhem-Quine) e fechamento
ensaístico (aforismo autoral, conforme `01-briefing.md`) — a estrutura de seções numeradas já
existente na transcrição é sólida e é mantida quase 1:1, só com os dois ajustes de conteúdo
que o próprio autor pediu (ver `01-briefing.md`, "Pendências").

## Abertura — a moeda de Kempthorne — **gancho**

- **O que prova:** planta o gancho (cena da aula do MIT, a citação sobre a moeda com 100
  caras seguidas) e a pergunta que o resto do texto responde — o que significa realmente
  "esperar o retorno à média" quando a própria média pode ter mudado. Fecha antecipando a
  tese em uma frase ainda não desenvolvida ("o desacoplamento entre modelo e realidade pode
  levar até vencedores do Nobel ao desastre").
- **Ato:** gancho.

## 1. "Três palavras que você usa como sinônimo e não são" — **contexto**

- **O que prova:** instala o vocabulário central do texto — teoria, modelo, intuição
  (Derman) — e testa esse vocabulário contra a filosofia da ciência (Cartwright, Box,
  Duhem–Quine, a visão semântica de Suppes/van Fraassen/Giere), concluindo que a distinção
  "bate em parte" e é uma ferramenta de ancoragem, não uma parede absoluta. As duas tabelas já
  existentes no rascunho (Teoria x Modelo; ponto de Derman x filosofia da ciência) carregam
  essa comparação.
- **Ato:** contexto — sem essa seção, "hipótese" e "modelo" nas seções seguintes não têm
  onde pousar.
- **Pilar:** narrativa (o porquê estrutural que sustenta todo o resto).
- **Visual:** nenhum além das tabelas já existentes — ver "O que fica de fora".

## 2. "O radar da rodovia" — **contexto (continuação, fora de finanças)**

- **O que prova:** transporta a ideia de "premissa que pode quebrar" para um caso sem viés
  comportamental (um radar de velocidade), estabelecendo a frase-guia do texto: "a matemática
  seguiria perfeita; o cenário é que teria mudado". Prepara o leitor para reconhecer o mesmo
  padrão nos dois casos financeiros que vêm a seguir.
- **Ato:** contexto, última parada antes da ação crescente.
- **Pilar:** visual. Entra aqui **`ilu-01`** — a metáfora do radar/rodovia é do próprio autor,
  tem objeto concreto (carro, radar, intervalo entre sensores) e carrega o argumento central
  do texto sozinha, pelo critério 3 da etapa 2 (`post-substack/SKILL.md`). Não é `diag-NN`
  porque não é uma relação estrutural entre entidades abstratas — é uma cena com objeto físico
  reconhecível.

## 3. "Black–Scholes: o que está na bula" — **ação crescente**

- **O que prova:** primeiro desastre real. As hipóteses do modelo (trajetória contínua,
  rebalanceamento contínuo) quebram no pregão de 18/05/2017 (Joesley Day) — ninguém conseguiu
  rebalancear porque não existiu preço no meio do caminho. Fecha com a reflexividade de
  MacKenzie (o modelo que "empurra" o mercado, não só o descreve) e o caso brasileiro do
  target forward de 2008 (Aracruz, Sadia).
- **Ato:** ação crescente — primeiro caso concreto que prova a tese em dinheiro real.
- **Pilar:** dado. Entra aqui **`graf-01`** — critério 1 da etapa 2: há série numérica real
  (Ibovespa fechamento 17/05 vs. 18/05/2017, queda intradiária de 10,47%, fechamento a
  -8,80%; dólar de R$ 3,14 a R$ 3,38) a comparar/mostrar o salto que quebrou a premissa de
  continuidade. Especificação de dados fica para a etapa 3 (pesquisa) e etapa 7 (verificação);
  aqui só se registra que a peça é gráfico, não ilustração — o ponto do texto é o número do
  salto, não uma cena.
- **Pendência de conteúdo:** falta o parágrafo-definição de Black–Scholes que o autor pediu
  entre colchetes na transcrição (ver `01-briefing.md`) — resolvido na etapa 4 (draft), não
  aqui.

## 4. "LTCM: quando dois Nobéis descobrem que o mundo não satisfaz as equações" — **clímax**

- **O que prova:** o caso mais forte do texto — dois ganhadores do Nobel, alavancagem 25:1,
  e a "premissa mais invisível e mais letal": liquidez. O mecanismo do desastre é um
  ciclo — calote russo → fuga para qualidade → spreads divergem em vez de convergir → chamada
  de margem → venda forçada → preços pioram ainda mais contra as posições que restam.
- **Ato:** clímax.
- **Pilar:** dado (perdas, alavancagem, valor do resgate) e visual. Entra aqui **`diag-01`** —
  critério 2 da etapa 2: não há uma métrica central única a plotar (a peça central do
  argumento é a mecânica do ciclo, não um número isolado), mas há uma relação estrutural
  clara entre entidades nomeadas e reais (Rússia, LTCM, mercados de Treasury, Fed de Nova
  York) encadeadas em sequência causal — um fluxo, não uma comparação abstrata de dois
  blocos. Não é `graf-NN` isolado: os números (US$ 4,6 bi perdidos, 25:1, US$ 1,25 tri de
  nocional) funcionam melhor como anotações dentro do próprio fluxo do que como série a
  plotar sozinha — evita fatiar o mesmo caso em duas peças concorrentes.

## 5. "As duas patologias" — **resolução (parte 1: diagnóstico)**

- **O que prova:** nomeia os dois erros de interpretação (fundamentalista, que nunca admite
  que o modelo errou; niilista, que abandona modelos por completo), com o caso do London
  Whale (JPMorgan, 2012) como exemplo-limite do primeiro. Mostra que as duas patologias têm a
  mesma raiz: confundir modelo com teoria — fechando o círculo aberto na seção 1.
- **Ato:** resolução, primeira metade — nomeia o problema geral antes de prescrever a
  solução prática da seção 6.
- **Pilar:** narrativa.
- **Visual:** nenhum — ver "O que fica de fora" (é exatamente o padrão de risco já registrado
  no critério 2 da etapa 2).

## 6. "A ficha técnica" — **resolução (parte 2: prática)**

- **O que prova:** converte o diagnóstico em ferramenta de uso — os cinco compromissos do
  *Financial Modelers' Manifesto* e a tabela de seis perguntas que o analista deveria saber
  responder antes de entregar qualquer número saído de modelo.
- **Ato:** resolução, segunda parte — "e daí, o que eu faço com isso" (mesma função que a
  seção 5 cumpriu em `2026-08-25-dividir-para-nao-correr-risco`).
- **Pilar:** nenhum adicional — a tabela de seis perguntas já existente no rascunho é a peça;
  ver "O que fica de fora".

## Fechamento — **fechamento (ensaístico)**

- **O que prova:** fecha com a imagem da alavanca ("multiplica competência tanto quanto
  multiplica burrice, e com a mesma indiferença") e o aforismo final ("um modelo é uma
  ferramenta que não sabe que é uma ferramenta. Cabe a você saber."). Fechamento ensaístico
  puro — sem CTA de compartilhamento explícito no rascunho; etapa 4 decide se adiciona um,
  seguindo o padrão do corpus.
- **Pendência de conteúdo:** o parágrafo sobre "não existem teorias no sentido forte [em
  finanças]" precisa da reescrita que o autor pediu entre colchetes — resolvida na etapa 4,
  ecoando a nuance já registrada na seção 1 (visão semântica das teorias), não a frase
  categórica original.

## Fontes e leituras

Mantida como está — insumo direto para a etapa 3 (pesquisa) e a etapa 7 (verificação
técnica), não entra na análise de arco.

## Três pilares — confirmação

- **Dado:** seção 3 (Ibovespa/dólar, 18/05/2017) e seção 4 (números do LTCM).
- **Narrativa:** seção 1 (taxonomia Derman + filosofia da ciência) e seção 5 (as duas
  patologias).
- **Visual:** `ilu-01` (seção 2), `graf-01` (seção 3), `diag-01` (seção 4).

Os três representados; nenhum pilar ausente.

## O que fica de fora (deliberadamente)

- **Diagrama para a taxonomia Teoria/Modelo/Intuição (seção 1):** cotada e descartada. É
  comparação de conceitos abstratos sem objeto concreto por trás — exatamente o sinal de
  alerta do critério 2 da etapa 2 ("diagrama fantasiado de ilustração"), já registrado como
  erro real em `posts/2026-08-17-o-mundo-invertido-das-carreiras-em-financas/ilustracoes.md`
  (revisão de `ilu-02`). As duas tabelas já existentes no texto cobrem essa comparação melhor
  do que uma peça visual forçaria.
- **Ilustração ou diagrama para "as duas patologias" (seção 5):** mesmo motivo — fundamentalista
  vs. niilista é literalmente "dois blocos" sem objeto concreto do texto por trás. Fica como
  texto com subtítulos (já é a estrutura do rascunho: `### O fundamentalista` /
  `### O niilista`).
- **Gráfico do sorriso de volatilidade (seção 3):** a ideia (superfície de volatilidade
  implícita deixando de ser plana após 1987) é genuína, mas o rascunho não tem dado
  quantificado para plotar sem inventar número — ficaria como curva estilizada sem fonte, o
  que a regra "não invente número" (`CLAUDE.md`) proíbe. Mantido como texto; se a etapa 3
  (pesquisa) encontrar uma série real de skew, reabrir esta decisão.
- **Gráfico de balanço do LTCM (patrimônio/ativos/nocional) além de `diag-01`:** descartado
  para não fatiar o mesmo caso em duas peças concorrentes — o mecanismo do ciclo de liquidez
  é o argumento mais importante da seção, mais do que o tamanho absoluto do balanço; os
  números entram como anotação dentro do próprio diagrama.
- **Peça visual para a tabela de seis perguntas (seção 6):** é checklist de referência, não
  série nem relação estrutural — a tabela markdown já existente cumpre a função melhor do que
  qualquer gráfico ou diagrama.
- **Infográfico:** padrão é não ter, e nenhum ponto do texto exige leitura conjunta de duas
  peças para fazer sentido — `ilu-01`, `graf-01` e `diag-01` carregam cada um sua própria
  síntese isoladamente. Critério de gatilho do infográfico não se aplica.

## Nota para a etapa 8 (capa)

O arquivo de origem já traz uma sugestão do autor para o criativo de capa: `[CAPA: como ideia
para criativo de capa, podemos utilizar algo como uma rebelia de máquinas humanoides como nos
filmes de Terminator]`. Registro aqui, para a etapa 8 não perder o insumo: a *ideia* (máquinas
que deixam de obedecer ao criador — eco direto do título "Quando os Modelos se Rebelam" e da
frase "um modelo é uma ferramenta que não sabe que é uma ferramenta") é aproveitável e forte
como metáfora de capa. A referência literal a "Terminator" não é — é propriedade de terceiros
(design de personagem protegido por direito autoral/marca) e também foge do estilo de
ilustração obrigatório para a linha editorial Spoiler (colagem editorial, não pôster de
ficção científica cinematográfica — ver `references/estilos-ilustracao.md`). A etapa 8 deve
traduzir a ideia (rebelião/desobediência da ferramenta) para a linguagem visual da marca, sem
citar o filme nem reproduzir design de personagem reconhecível.

## Pendências para pesquisa/verificação (não resolvidas nesta etapa)

- Todos os números do caso Joesley Day (Ibovespa intradiário -10,47%, fechamento -8,80%,
  dólar R$ 3,14 → R$ 3,38) e do LTCM (patrimônio ~US$ 4,7 bi, ativos ~US$ 125 bi, alavancagem
  ~25:1, nocional ~US$ 1,25 tri, perda ~US$ 4,6 bi, resgate ~US$ 3,6 bi) ficam para
  verificação técnica (etapa 7) — nada aqui foi conferido contra fonte primária ainda.
- O caso do target forward de 2008 (Aracruz US$ 2,13 bi, Sadia R$ 2,55 bi, volume total
  estimado US$ 35 bi) e o caso London Whale (>US$ 6 bi) — mesma pendência.
- Citação exata de Kempthorne e a fonte precisa (18.S096 vs. 18.642) — confirmar contra o
  material do MIT OCW na etapa 3.
