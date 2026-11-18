# Etapa 1 — Briefing

## Linha editorial

**Notas de um Professor**, lida do campo `linha_editorial` do próprio rascunho (etapa 0). O
rascunho declara o tipo **conceito de finanças** (`docs/BACKWARDS_DESIGN.md` §4.2), e o corpo
confirma. O que muda nos movimentos é isto:

- o 4 vira "que problema o conceito foi inventado para resolver, e por quem": a seção "Preço sem
  opinião" abre com a própria pergunta ("Que problema esse princípio resolve, e para quem?") e
  responde com a soma, o fator de desconto e Black-Scholes;
- o 5 vira "onde a intuição comum falha e por quê", por contraste com um vizinho nomeado: a
  seção "Nem toda convergência é arbitragem", com PETR3 × PETR4 e o LTCM;
- o 8 vira "que decisão real muda": a seção "Antes de chamar de arbitragem", com o preço contra
  a réplica, o bloco de planilha e as três perguntas.

O texto tem também a conta de matemática financeira (a réplica da NTN-F). Ela fica dentro do
movimento 3/4 e não muda o tipo. A etapa 5 roda sem validação argumentativa, e a 5a não roda.

## Voz

**Ensaística em registro técnico** (§4.2 do guia), a voz padrão da linha, declarada no rascunho.
Sinais no texto:

- **tese em refrão de duas frases**, plantada no Mito e repetida no fecho: "Preço não é opinião.
  É o custo da réplica." O subtítulo a antecipa em outra forma ("Preço não é opinião: é o custo
  de montar o mesmo fluxo.");
- **segundo refrão**, a moeda: "Cara, eu ganho. Coroa, eu não perco." No título, na definição de
  arbitragem, na montagem da NTN-F ("Cara, a mesa ganha. Coroa, não perde.") e no fecho. É o
  movimento 3 dos aspiracionais (repetir a palavra-chave em vez de variar);
- fórmula display anunciada por dois-pontos e glosada depois ("em que CF_t é…");
- conta resolvida até o número final (R$ 4,89; R$ 943,88; R$ 20.307,28);
- quadro de perguntas no fim ("três perguntas") e exercício ("Se o texto funcionou, você
  consegue…");
- primeira pessoa só para costurar a série ("deixei uma fórmula", "Contei essa história em");
  "você" didático; imperativo que conduz ("Comece por uma aposta", "Repare", "Pense", "Volte");
- negrito na frase-tese e nos termos na primeira definição (arbitragem, princípio da não
  arbitragem, Lei do Preço Único, fator de desconto, portfólio equivalente, trading de
  correlação), dentro da regra 4 da v2.0.0.

**A etapa 4 dá mais peso à voz**, pelo precedente da etapa 0 (texto montado a partir de pauta).
Ela confere o texto contra `estilo/estilo-autoral.md` §3, §4.2 e §7.2 e contra
`estilo/preferencias-de-edicao.md`, sem reordenar o argumento.

## Tese em uma frase

Num mercado em que a arbitragem não dura, o preço de um fluxo não depende da opinião de ninguém:
é o custo de montar o mesmo fluxo com o que já tem preço. Daí saem a Lei do Preço Único, o valor
presente como soma de fatores de desconto (e, com mais matemática, Black-Scholes) e o critério
que separa arbitragem, que vive de identidade de fluxos, de aposta de correlação, que vive de
estatística.

Aforismo do texto: "Preço não é opinião. É o custo da réplica." Aparece no Mito e no fecho, de
propósito (§5.4).

## Gancho

**Modo B** (moldura conceitual + enigma, §4.1), declarado no rascunho. A abertura cobra a palavra
que o texto anterior deixou ("replicar"), lança a aposta da moeda, dá a ela o nome de arbitragem
e a materializa num caso concreto: em 1º/1/2029 o Tesouro paga R$ 1.000 a quem tem uma LTN 2029
e R$ 1.048,81 a quem tem uma NTN-F 2029, e o principal desmembrado da NTN-F é a mesma promessa
que a LTN.

O caso é datado no futuro e não é evento de mercado. Por isso o movimento 7 não é obrigatório,
e o fecho volta à moeda ("A moeda que ninguém lança duas vezes"), absorvendo a função.

Pergunta-âncora, explícita no fim da abertura: "O que obriga duas promessas idênticas a custarem
o mesmo? E o que mais se tira daí, além dessa igualdade?"

## Continuidade de série

O texto continua "Frequência de Capitalização" (`posts/2026-11-09-frequencia-de-capitalizacao/post.md`,
aprovado em 09/11). O que já foi dito lá e o que isso pede aqui:

- **O gancho bate.** Lá: "Para replicar o preço na planilha:" e o bloco `=TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6)`,
  e no fecho "Com a régua, o motor e agora a etiqueta, o expoente du/252 desta série está
  explicado de ponta a ponta." Aqui: "deixei uma fórmula de planilha para replicar o preço de uma
  LTN" e "a série de convenções fechou: a régua, o motor e a etiqueta". Coerente.
- **Vocabulário:** régua, motor e etiqueta ficam no passado da série. O termo novo é **réplica**.
  A etapa 4 confere que "etiqueta" e "motor" não reaparecem em outro sentido.
- **Glosa da LTN:** lá, "(Letra do Tesouro Nacional, o título público prefixado)"; aqui, "(…, o
  título público prefixado sem cupom)". O acréscimo é necessário, porque o texto contrasta com a
  NTN-F.
- **Black-Scholes:** "a fórmula que o manual de opções da B3 usa, a do texto anterior" bate com a
  seção "Por que a mesa de opções fala contínuo" de lá. Fica só a menção (decisão do autor).
- **LTCM:** o link para "Quando os Modelos se Rebelam" bate. Aquele post tem a seção "LTCM:
  quando dois Nobéis descobrem que o mundo não satisfaz as equações" e já diz que Scholes e Merton
  eram sócios do fundo.
- **Formato de fórmula:** o post publicado usa `$$ … $$`; o rascunho usa blocos ```` ```latex ````.
  A etapa 4 converte para o formato publicado.
- **Skill Check:** o texto anterior pôs o CTA no mesmo lugar (fim da Prateleira, antes do fecho).
  Este repete o padrão, com duas dimensões em vez de uma.
- **Ponte para a frente:** *bootstrapping* (decisão do autor) e um texto futuro sobre trading de
  correlação.

## Briefing de funil (`../../strategy/FUNIL.md` §1 e §5)

- **Segmento:** `#GENZ-GREED` e `#GENZ-FEAR`: o estagiário ou analista júnior de mesa, de
  tesouraria ou de risco que já ouviu "arbitragem" e "TIR" e nunca montou uma réplica. O gancho da
  promessa para esse segmento é "provar competência rápido" (a pergunta "é arbitragem ou aposta?"
  é exatamente a que um júnior é cobrado a responder). Quem encaminha é o leitor `#Millennials-*`,
  e o CTA do fecho já mira nele ("encaminhe para quem chama de arbitragem qualquer *long-short*").
- **Estágio:** topo gratuito (§5).
- **Objetivo do post:** educar e fazer a lista crescer por encaminhamento. O CTA do Skill Check
  (gratuito, topo) já está no corpo. Curso ou preço não entram no corpo; oferta, se houver, é
  decisão da etapa 9a.

## Analogias e movimentos a preservar

Vieram do rascunho e da pauta, não deste pipeline:

- **A moeda** ("Cara, eu ganho. Coroa, eu não perco."): a aposta que não custa nada, não perde e
  pode ganhar. É o fio do título ao fecho.
- **O ganha-ganha em duas camadas:** o de uma pessoa só (a arbitragem) e o coletivo (o
  equilíbrio). O rascunho diz que segue a pauta nisso.
- **"O almoço do arbitrador saiu do prato de quem cotou errado"**: a versão do autor para o
  *free lunch*.
- **"A moeda aparece"**: o desvio de preço visto como a aposta da abertura.
- **A réplica** como objeto: preço é o custo dela; a TIR sai do preço.
- **A pergunta-critério**: "se a diferença de preço dobrar amanhã, você perde dinheiro no
  vencimento?"

## Resolução dos marcadores da etapa 0

| # | Marcador | Resolução nesta etapa |
|---|---|---|
| 1 | Linha editorial, voz, tipo, modo B | Resolvido. Voz e tipo confirmados acima. |
| 2 | Ficha de Saída curta | Etapa 2. |
| 3 | Título e subtítulo | Resolvido pelo autor no rascunho. |
| 4 | Ponte de série | Resolvido pelo autor no rascunho (*bootstrapping*). |
| 5 | Exemplo estilizado | Resolvido pelo autor no rascunho. |
| 6 | Black-Scholes só menção | Resolvido pelo autor no rascunho. |
| 7 | Movimentos 6 e 7 omitidos | Etapa 2 confere. |
| 8–10 | `[VERIFICAR]` (desmembramento, cupom R$ 48,81, Cochrane) | Etapa 3 levanta, etapa 7 confere. |
| 11–12 | Números e fatos | Etapa 7 (recalcular tudo; fonte primária). A etapa 3 confere a Selic e as taxas de novembro de 2026. |
| 13 | Links | Etapa 7. |
| 14 | CTA do Skill Check | Fica; a 9a não duplica. |
| 15 | Promessa do texto sobre correlação | Alerta para o gate (abaixo). |
| 16 | Visual sugerido | Etapa 2 decide o tipo, etapa 8 produz. |
| 17–20 | Processo, checagem, aviso legal, notas | Fora do `post.md`; aviso legal na etapa 9. |

## Tensões registradas (perguntas nomeadas)

Nenhuma. As quatro decisões que o rascunho levantou já vieram respondidas pelo autor, e nenhum
marcador estrutural ou nota de conteúdo ficou sem resolução clara nesta etapa.

## Alertas para as etapas seguintes (não são decisões)

- **Definição de arbitragem.** A frase geral ("custa zero (ou menos que zero) hoje, nunca dá
  prejuízo no futuro e dá lucro em pelo menos um cenário") não descreve bem a forma 1, em que o
  lucro é o dinheiro recebido hoje e não há lucro futuro. A etapa 7 confere contra a definição de
  livro (Tuckman e Serrat; Cochrane).
- **A abertura tem cerca de 14 parágrafos curtos**, contra 3–6 do §3 do BACKWARDS_DESIGN. Os
  parágrafos são de uma ou duas frases, então a extensão em palavras é menor do que parece. A
  etapa 5 avalia se o leitor chega à pergunta-âncora sem cansar.
- **O refrão da moeda aparece quatro vezes** (mais o título). A etapa 5 avalia se a repetição
  carrega o argumento ou vira cadência; a 6 confere a regra 20 (antítese "não é X. É Y.": "Ela
  não diz que elas nunca aparecem. Diz que não duram", "Ela não pergunta… Pergunta…", "Ela não
  começou como… Começou com…", "A TIR sai do preço, e não o contrário", "não são, em geral,
  dinheiro esquecido… são o preço desses atritos").
- **Selic de 13,75% desde 4/11/2026 (282ª reunião)** e "perto da curva prefixada de novembro de
  2026": a etapa 3 confere em fonte primária (BCB, ANBIMA ou Tesouro), e a 7 fecha.
- **Leilões semanais de LTN e NTN-F**: conferir no cronograma de leilões de 2026 do Tesouro.
- **Desmembramento de NTN-F**: a norma vigente é o `[VERIFICAR]` aberto. Se a etapa 3 não achar
  fonte oficial, a frase precisa ser reescrita sem afirmar a norma (pergunta no gate).
- **Cupom pago**: R$ 48,81 × R$ 48,80. A metodologia do Tesouro define o truncamento; a etapa 7
  decide qual número entra na abertura (R$ 1.048,81 ou outro).
- **NTN-F e LTN "do mesmo devedor"**: a réplica usa LTNs vencendo nas datas dos cupons. A seção
  dos atritos já diz que "nem toda data tem LTN". O exemplo é estilizado (decisão do autor), mas o
  texto precisa deixar claro onde é hipotético. A etapa 5 olha.
- **Exercício da NTN-B**: "Quantas NTN-B Principal de cada data replicam uma NTN-B?" supõe NTN-B
  Principal em todas as datas de cupom, o que não existe no mercado. A etapa 7 confere; a
  pergunta pode ficar como exercício, desde que o texto não afirme que a réplica existe.
- **Ponto-base da arbitragem**: "cerca de 2 pontos-base" é sobre o valor montado (R$ 20 mil em
  R$ 94 milhões); conferir se a frase deixa a base clara.
- **"O marca a mercado"**: gênero e forma (marcação a mercado). Etapa 6.
- **Glosas na primeira ocorrência** (regra 14; §5.1), para a etapa 6: LTN, NTN-F, TIR, venda a
  descoberto, marcar a mercado, fator de desconto, taxa *spot*, vértice, PU, curva positivamente
  inclinada, *dealer*, ponto-base, PETR3/PETR4, trading de correlação, LTCM, compromissada,
  *spread*, DI futuro, VNA, NTN-B, NTN-B Principal, *bootstrapping*, *STRIPS* estão glosados.
  Sem glosa: ANBIMA, Svensson, B3, CDI, CDB, Copom, Selic, IPCA, Tesouro Direto. A etapa 6 decide
  quais o leitor da linha já domina.
- **Estrangeirismo em itálico** (regra 4): *dealer*, *spot*, *long-short*, *bootstrapping*,
  *STRIPS* já estão; "spread" e "trading" não. Etapa 6.
- **Tamanho:** cerca de 2.900 palavras de corpo, na faixa do texto anterior (cerca de 2.600).
  Não há pedido de corte.
- **Promessa de série dupla:** *bootstrapping* no próximo texto e "um texto próprio" sobre
  trading de correlação. O autor aprovou as duas no rascunho. Fica registrado, porque a
  promessa do FIDC foi feita duas vezes e cancelada depois.
