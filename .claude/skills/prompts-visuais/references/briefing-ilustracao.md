# Briefing de ilustração — do texto ao conceito

Método obrigatório da etapa 8, **antes** de escrever qualquer prompt. `estilos-ilustracao.md`
decide *como a peça parece*; este arquivo decide *o que a peça mostra*. São problemas
diferentes e o segundo é o que estava faltando.

Criado em 31/08/2026 depois que as duas primeiras imagens geradas pelo sistema de estilos
saíram tecnicamente corretas e editorialmente vazias.

---

## O defeito que este método corrige

As duas peças de teste ficaram no estilo certo e não diziam nada sobre o texto:

| Peça | O que foi desenhado | Por que falhou |
|---|---|---|
| `ilu-01` de *O Mundo Invertido das Carreiras* | Uma escada espelhada | Escada = "ordem/progresso" é metáfora universal. A mesma imagem serve para crise, demissão, queda de audiência. Nada nela é do texto |
| `ilu-01` de *O Papel do CDB* | Cápsula → câmara → cápsula mais longa | A cota curta/longa funcionou, mas a câmara é uma caixa vazia. Serve para amplificador de sinal, compressor, tubulação. Nada nela é banco |

Diagnóstico: os dois conceitos importaram um objeto genérico de fora do texto. E os dois
textos estavam **cheios** de objeto concreto próprio, jogado fora:

- *Mundo Invertido* entrega o livro do **John Hull com juros nos capítulos 4–6 e opções só no
  capítulo 10** (a ordem do sumário é o argumento inteiro), o **quadro** onde ele provava o
  modelo, o **primeiro módulo do CFA**, a **linha de pré-requisito da GFMI**, e cita
  *Stranger Things* pelo nome.
- *CDB* entrega **21% contra 20% de compulsório**, o **"outro lado do balcão"** como título de
  seção, "**transformação de maturidade**" nomeada pelo Bacen, e o destino do dinheiro sendo
  um **financiamento imobiliário**.

Nenhuma dessas coisas apareceu nas imagens. O método abaixo existe para que isso não se
repita.

---

## Etapa 8a — o briefing, em cinco passos

Rode uma vez por `ilu-NN`. Grave em `posts/<slug>/processo/08-briefing-visual.md`.

### 1. Colheita de material concreto

Varra o `post.md` e liste **só o que está no texto**:

- **Objetos nomeados** — livro, quadro, balcão, cadeira, formulário, sumário, contrato.
- **Instituições e documentos** — Bacen, CVM, FGC, Lei nº 4.728/1965, Relatório de
  Estabilidade Financeira, currículo do CFA, ementa da GFMI.
- **Números que carregam argumento** — 21% e 20%, capítulos 4–6 e 10, R$ 250 mil, 4 anos.
- **Referências culturais que o autor usou** — *Upside Down* de *Stranger Things*.
- **Verbos de ação** — transformar, reter, emprestar, abrir mão, derivar, provar.
- **Frases-âncora** — a que o parágrafo fecha, literal, entre aspas.

Regra dura: **nada entra nessa lista que não esteja no texto.** Se você precisa importar um
objeto de fora para o conceito funcionar, o conceito ainda não está pronto.

### 2. A frase que a imagem carrega

Uma frase, e não é o tema do post. É a afirmação específica do ponto onde a `ilu-NN` está
ancorada. Cite o parágrafo literal ao lado.

Errado: "a imagem é sobre aprender fora de ordem."
Certo: "a ordem correta está impressa no sumário de um livro que ele já tinha na estante —
juros no capítulo 4, opções no capítulo 10."

### 3. Divergência — no mínimo três conceitos

Nunca vá do texto direto a um conceito só. A literatura de ilustração editorial é unânime
nisso: o processo é gerar várias miniaturas e escolher, não acertar de primeira. Use as três
**estruturas formais de metáfora visual** (Forceville; Phillips & McQuarrie) para forçar
divergência real em vez de três variações da mesma ideia:

| Estrutura | Como funciona | Verbaliza como | Complexidade |
|---|---|---|---|
| **Justaposição** | Fonte e alvo lado a lado, comparáveis | "A é como B" | Menor |
| **Fusão / híbrido** | Fonte e alvo fundidos num objeto só | "A com B" | Média |
| **Substituição** | Só um elemento aparece; o outro é ausência apontada | "A é B" | Maior |

Gere **um conceito por estrutura**, no mínimo. Substituição costuma render a imagem mais
forte, mas é a que mais escorrega para o genérico quando a fonte não vem do texto — foi
exatamente o que aconteceu nas duas peças reprovadas.

**Sobre clichê:** conceito forte não precisa de objeto original. A prática corrente da área é
o contrário — pegar o objeto familiar *certo* e torcê-lo no ponto exato. Um livro aberto é
clichê; um livro aberto **lido na ordem errada, com o capítulo 10 antes do 4**, é o argumento
do post. A originalidade está na torção, não no objeto.

### 4. Testes de rejeição

Cada conceito passa pelos quatro. Reprovou em um, morreu — anote por quê, não conserte na
marra.

- **Teste da troca.** Essa imagem funcionaria num artigo sobre outro assunto? Se um post sobre
  demissão em massa, sobre queda de engajamento ou sobre qualquer "coisa que dá errado"
  pudesse usar a mesma peça sem ajuste, o conceito é genérico. **Este é o teste que as duas
  peças reprovadas falharam.**
- **Teste do substantivo.** A imagem contém pelo menos um objeto concreto vindo da lista do
  passo 1? Forma geométrica abstrata não conta.
- **Teste do alt-text cego.** Escreva o alt-text e leia sem o post ao lado. Ele afirma algo que
  o post afirma, ou só descreve formas ("uma escada cortada ao meio por uma linha")? Descrição
  de forma é sintoma de conceito vazio.
- **Teste da legenda.** A imagem precisa de legenda para ser entendida? Então quem está
  explicando é o texto, não ela.

### 5. Escolha e defesa

Registre o conceito escolhido, a estrutura de metáfora usada, e **por que os outros perderam**.
O descarte anotado é o que impede a próxima peça de repetir a ideia fraca.

---

## Erros recorrentes

- **Ilustrar o tema em vez da frase.** O post é sobre CDB; a imagem não é "sobre CDB", é sobre
  a afirmação daquele parágrafo específico.
- **Metáfora de dicionário.** Escada, ponte, quebra-cabeça, ampulheta, iceberg, labirinto,
  engrenagem solta, alvo com flecha. Se o objeto podia ter vindo de um banco de imagens, veio.
- **Diagrama disfarçado de ilustração.** Se a peça tem eixo, série e comparação de valor, é
  gráfico — vai para `graf-NN` com dado real, não para `ilu-NN`.
- **Número desenhado sem ser desenhável.** 21% contra 20% é ótimo material; virar dois
  retângulos com rótulo é gráfico ruim. A imagem mostra a *consequência* da diferença, não a
  diferença.
- **Duas ideias na mesma peça.** Uma peça, uma afirmação. Se há duas, são duas `ilu-NN` ou
  uma foi cortada na etapa 2.

---

## O briefing pronto alimenta o prompt

Só depois dos cinco passos vá para `estilos-ilustracao.md` e escreva o prompt. A ordem
importa: **estilo é a última decisão, não a primeira.** O conceito define o que a peça mostra;
o estilo define com que material ela mostra. Inverter isso é como escolher a fonte antes de
saber o que o texto diz — foi assim que as duas primeiras peças saíram bonitas e mudas.
