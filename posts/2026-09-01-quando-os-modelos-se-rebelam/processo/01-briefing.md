# Briefing — Quando os Modelos se Rebelam

## Tese em uma frase

O que separa um modelador competente de um "extremista frustrado" (fundamentalista ou
niilista) é entender que, em finanças, não existem teorias — só modelos, analogias com
domínio de validade —, e que todo desastre de modelo real (Black–Scholes no 18/05/2017,
LTCM em 1998) nasce do descolamento entre a premissa e o mundo, não de erro de conta.

## Gancho escolhido

A citação do professor Peter Kempthorne (MIT OCW) sobre a moeda que sai cara 100 vezes
seguidas — cena/dado concreto e datável (aula de *Probability Theory*, 18.S096) que abre o
texto antes de qualquer tese. Não é a mesma coisa que a tese: a tese só aparece formulada
depois, na seção 1 (Derman: teoria x modelo x intuição).

## Analogias do autor (preservar — são dele, não do repórter)

- **O radar de solo na rodovia** (seção 2): velocidade média tratada como instantânea; a
  aproximação só funciona sob a premissa de movimento contínuo. Serve de exemplo "fora de
  finanças, onde ninguém tem viés comportamental" antes de entrar no caso técnico.
- **"A bula do remédio"**: as hipóteses de um modelo não são conjecturas a testar, são o
  domínio de validade do instrumento — ignorá-las é "usar o aparelho fora da faixa de
  operação".
- **"O modelo pressupõe um filme; o que aconteceu foi um corte do editor"** (18/05/2017,
  Joesley Day) — frase de fechamento de cena, alto valor de retenção, preservar verbatim.
- **"O cometa não muda de órbita porque o astrônomo publicou. / O mercado muda."** — par de
  frases curtas (movimento Hemingway: justaposição sem explicar o porquê) sobre
  reflexividade (MacKenzie, Soros). Preservar a quebra de linha/ritmo.
- **O modelo como alavanca**: "não decide nada por você e não sabe nada sobre o mundo — ela
  apenas multiplica a força que você aplica. Ela multiplica competência tanto quanto
  multiplica burrice, e com a mesma indiferença." Imagem de fechamento do texto, carrega o
  argumento central — não é decoração.

## Encaixe no funil (`_arquivo/MARKETING_REVIEW.md` §5)

Texto de audiência/educação (topo do funil gratuito), mas com profundidade técnica acima da
média do corpus até aqui (estocástico, VaR, precificação de opções). Fala diretamente à
objeção-mestra de `#GENZ-GREED` e `#Millennials-GREED` ("consigo aprender isso de graça" /
"vale o investimento de tempo?") ao mostrar rigor que não se encontra em conteúdo
fragmentado, e ecoa a trilha paga "Fundamentos Matemáticos para Finanças" citada em
`MARKETING_REVIEW.md` §5 — funciona como prova de competência técnica antes de qualquer
oferta, sem vender nada explicitamente no corpo.

## Qual voz (`estilo/estilo-autoral.md` §4)

**Ensaística.** Critério de decisão do guia: "se o post tem tese defensável ou opinião, é
ensaístico" — este tem (a tese acima, mais o julgamento explícito sobre as duas patologias
do modelador). Confirmação adicional pelos sinais do próprio texto:
- abre com cena/anedota (aula do MIT), não com definição;
- primeira pessoa singular de opinião presente o tempo todo ("um dos meus momentos
  favoritos", "minha leitura", "o que eu proponho");
- ironia constante contra a própria prática financeira (o "extremista frustrado", o
  "modeleiro", o CIO do JPMorgan trocando de modelo até a perda virar meia);
- metáfora/analogia frequente (ver seção acima), inclusive retomada no fechamento — o que o
  guia nota como aspiracional ainda não testado na voz atual (`estilo-autoral.md` §6);
- fecha sem resumo genérico, com aforismo autoral ("Um modelo é uma ferramenta que não sabe
  que é uma ferramenta. Cabe a você saber.").

Não fecha com CTA de compartilhamento explícito no rascunho da transcrição — a etapa 4
decide se adiciona um, seguindo o padrão dos outros posts ensaísticos do corpus.

## Linha editorial

O arquivo de origem já traz a anotação do autor: `[LINHA EDITORIAL: Spoiler]`.

**Registro de tensão, não bloqueio:** pelo critério literal de `PROJECT_DESCRIPTION.md`
(Spoiler = relato de jornada de carreira pessoal; Notas de um Professor = conceito/produto
com rigor técnico), o conteúdo deste texto — modelagem financeira, Black–Scholes, LTCM, sem
narrativa de carreira própria do autor — se pareceria mais, pelo assunto, com "Notas de um
Professor". Mas a decisão de linha editorial é separada da voz e do assunto (já houve
precedente inverso documentado em
`posts/2026-08-25-dividir-para-nao-correr-risco/estado.json`), e aqui é o próprio autor quem
já declarou a linha antes mesmo do briefing — tratando isto, presumivelmente, como mais um
"spoiler" de como ele pensa/decide na prática profissional diante de modelos, não como
definição de produto. Honro a decisão explícita do autor e sigo com **Spoiler**. Levo o
registro da tensão ao gate humano (etapa 10) para confirmação, não para reabrir a escolha
sem necessidade.

## Pendências que a etapa 4 (draft) precisa resolver

O texto de origem tem duas notas do autor entre colchetes, tratadas como instrução de
escrita, não como conteúdo a preservar literalmente:

1. Seção 3 (Black–Scholes): `[escrever um breve parágrafo sobre o que é o modelo e pq ele é
   tão famoso.]` — falta uma frase-definição de Black–Scholes antes da lista de hipóteses.
2. Fechamento: `[tentar reescrever o parágrafo acima. Existem teorias em finanças.]` — o
   autor sinaliza que o parágrafo "não existem teorias no sentido forte [em finanças]" está
   forte demais / impreciso e quer revisão. Nota: a própria seção 1 já registra essa mesma
   tensão de forma mais matizada (a "visão semântica" de Suppes/van Fraassen/Giere, onde
   teoria também é família de modelos) — o fechamento deve ecoar essa mesma nuance em vez de
   reafirmar a frase categórica original.
