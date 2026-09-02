# Briefing — Quando os Modelos se Rebelam

## Tese em uma frase

Em finanças não existem teorias, só modelos — analogias emprestadas com domínio de validade
limitado —, e todo desastre real de modelagem (Black–Scholes em 18/05/2017, LTCM em 1998) não
nasce de erro de conta, mas do descolamento entre a premissa calibrada e o regime em que ela
foi aplicada; saber operar dentro dessa fronteira é o que separa um modelador competente de um
extremista frustrado (fundamentalista ou niilista).

## Gancho escolhido

A citação atribuída a Peter Kempthorne (aula de *Probability Theory*, MIT OCW 18.S096) sobre a
moeda que sai cara 100 vezes seguidas. É cena/dado concreto e datável — uma disciplina real,
localizável — que abre o texto antes de qualquer formulação de tese. Não confundir com a tese
em si: a tese só se fecha depois, na seção 1, com a separação de Derman entre teoria, modelo e
intuição.

**Nota que carrega para a etapa 7 (verificação técnica):** a atribuição da fala a Kempthorne
precisa ser conferida contra a gravação/material do curso antes de publicar — é exatamente o
tipo de dado factual verificável que a regra "evidência ou silêncio" do `CLAUDE.md` cobre. Isso
já foi investigado em rodadas anteriores deste post (`03-pesquisa.md` e `07-verificacao.md` de
01/09) e segue sem confirmação definitiva — carrega como pendência conhecida.

## Analogias do autor (preservar — são dele, não do repórter)

- **O radar de solo na rodovia** (seção 2): troca velocidade média por velocidade
  instantânea; a aproximação só vale sob a premissa de movimento contínuo. Funciona como
  exemplo fora de finanças, "onde ninguém tem viés comportamental", antes de entrar no caso
  técnico.
- **"A bula do remédio"**: as hipóteses de um modelo não são conjecturas a testar, são o
  domínio de validade do instrumento — ignorá-las é "usar o aparelho fora da faixa de
  operação".
- **"O modelo pressupõe um filme; o que aconteceu foi um corte do editor"** (18/05/2017,
  vazamento Joesley/Temer) — frase de fechamento de cena, preservar verbatim.
- **"O cometa não muda de órbita porque o astrônomo publicou. / O mercado muda."** — par de
  frases curtas sobre reflexividade (MacKenzie, Soros); preservar a quebra de linha e o
  ritmo de justaposição sem explicação (movimento Hemingway).
- **O modelo como alavanca** — imagem de fechamento: "não decide nada por você e não sabe
  nada sobre o mundo — ela apenas multiplica a força que você aplica. Ela multiplica
  competência tanto quanto multiplica burrice, e com a mesma indiferença." Carrega o
  argumento central, não é decoração; candidata a retomar no fechamento do post.

## Encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §5)

Conteúdo de topo de funil (audiência/educação via Substack), mas com densidade técnica acima
da média do corpus (estocástico, VaR, precificação de opções, alavancagem). Fala diretamente
à objeção-mestra das personas `#GENZ-GREED` e `#Millennials-GREED` — "isso não dá pra achar de
graça em qualquer lugar" — funcionando como prova de competência técnica antes de qualquer
oferta explícita, e ecoa a trilha paga "Fundamentos Matemáticos para Finanças" do funil sem
vender nada no corpo do texto. Não fecha com CTA de compartilhamento no rascunho de origem — a
etapa 4 decide se adiciona um, seguindo o padrão predominante nos posts ensaísticos já
publicados do corpus.

## Qual voz (`estilo/estilo-autoral.md` §4)

**Ensaística.** O critério do guia é direto: "se o post tem tese defensável ou opinião, é
ensaístico" — este texto tem (a tese acima, mais o julgamento explícito do autor sobre as
duas patologias do modelador). Sinais adicionais no próprio rascunho:

- abre com cena/anedota (a aula do MIT), não com definição;
- primeira pessoa singular de opinião o tempo todo ("um dos meus momentos favoritos", "minha
  leitura", "o que eu proponho");
- ironia constante contra a própria prática financeira ("extremista frustrado",
  "modeleiro", o CIO do JPMorgan trocando de modelo de VaR para liberar espaço de aposta);
- metáfora e analogia frequentes (ver seção acima);
- fecha com aforismo autoral, não com resumo genérico ("Um modelo é uma ferramenta que não
  sabe que é uma ferramenta. Cabe a você saber.").

## Linha editorial — tensão registrada, mas sem mais efeito sobre o visual

O arquivo de origem traz a anotação do próprio autor: `[LINHA EDITORIAL: Spoiler]` (marcador
**estrutural**, inventariado na etapa 0).

Pelo critério literal de `PROJECT_DESCRIPTION.md` — Spoiler é relato de jornada de carreira
pessoal; Notas de um Professor é conceito/produto explicado com rigor técnico — o assunto
deste texto (teoria vs. modelo, Black–Scholes, LTCM, sem narrativa de carreira própria do
autor) se encaixaria melhor em **Notas de um Professor**. Essa tensão já foi levada ao gate
humano na rodada de 01/09/2026 e respondida explicitamente pelo autor: manter **Spoiler**.
Registro mantido aqui por rastreabilidade, mas não repito a pergunta nomeada nesta rodada — já
foi respondida uma vez para este mesmo post, e reabrir sem motivo novo seria ruído.

**Mudança de sistema desde a última rodada:** a linha editorial **não determina mais o estilo
das ilustrações** (`estilos-ilustracao.md`, "Por que um estilo só", unificação de 2026-09-01).
Colagem editorial vale para o post inteiro independentemente da resposta acima — a linha
segue relevante só para frontmatter e encaixe de funil, não bloqueia mais a etapa 8.

## Pendências que a etapa 4 (draft) precisa resolver

Duas instruções de escrita inventariadas na etapa 0:

1. Seção 3 (Black–Scholes): `[escrever um breve prágrafo sobre o que é o modelo e pq ele é
   tao famoso.]` — falta uma frase-definição de Black–Scholes (o que precifica, quando
   publicado, por que virou padrão de mercado) antes da lista de hipóteses.
2. Fechamento: `[tentar reescrever o parágrafo acima. Existem teorias em financas.]` — o
   autor sinaliza que "não existem teorias no sentido forte [em finanças]" está categórico
   demais. A seção 1 já registra a mesma tensão de forma mais matizada, na tabela sobre a
   visão semântica de Suppes/van Fraassen/Giere (onde teoria também é família de modelos) —
   o fechamento deve ecoar essa nuance em vez de reafirmar a frase absoluta original.
