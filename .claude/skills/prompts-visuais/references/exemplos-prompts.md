# Exemplos de prompt — briefing + estilo aplicados a posts publicados

Prompts de validação gerados em 31/08/2026, **segunda rodada**. Regeram peças de posts já
publicados para o autor comparar antes de o sistema rodar em post novo.

## O que mudou da primeira rodada para esta

A primeira rodada aplicou só `estilos-ilustracao.md`. As imagens saíram no estilo certo e sem
conteúdo: uma escada espelhada e um conjunto cápsula-câmara-cápsula, conceitos importados de
fora do texto. Reprovaram no **teste da troca** — serviriam para qualquer artigo sobre
"coisa que dá errado" ou "transformação".

Esta rodada roda `briefing-ilustracao.md` (etapa 8a) antes do estilo: colheita do material
concreto do post, três conceitos divergentes por estrutura de metáfora, quatro testes de
rejeição, escolha com descarte anotado. **O estilo não mudou** — o que mudou é o que a peça
mostra. É esse o A/B desta rodada.

Servem também como calibragem: quando um briefing novo sair fraco, compare com estes.

---

# Estilo A — Spoiler (colagem editorial)

Post: `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`

## Material concreto colhido do post

**Objetos:** o quadro onde ele provava o modelo ("se você me pedisse para provar o resultado
no quadro, eu provava"); o livro de John Hull; o sumário; a cadeira onde o estagiário senta;
a "porta errada"; a "régua de produtos". **Números:** capítulos 4 a 6 (juros) contra capítulo
10 (opções); primeiro módulo do CFA. **Documentos:** pré-requisito da GFMI, que pede só
"entender conceitos financeiros simples, como valor presente". **Referência cultural do
autor:** o *Upside Down* de *Stranger Things*. **Verbos:** derivar, provar, explicar,
preencher. **Frases-âncora:** "A conta batia. O produto, não." / "O gargalo raramente é a
matemática. É o alicerce."

---

## `ilu-01` — o quadro

**Onde entra:** fim da seção 1, após "O problema nunca foi a complexidade do modelo. Foi eu
ter aprendido as coisas fora de ordem."

**Frase que a peça carrega:** ele provava o modelo inteiro no quadro e não sabia dizer o que o
contrato fazia — a demonstração estava completa em volta de um vazio.

### Divergência

| # | Estrutura | Conceito | Veredito |
|---|---|---|---|
| A | Justaposição | Dois quadros lado a lado: um com a derivação completa, outro com um buraco | Descartado — a comparação exige que o leitor infira a relação entre os dois painéis; e dois objetos iguais lado a lado é o dispositivo que já morreu na primeira versão do post ("duas trilhas de luz") |
| B | **Fusão** | **Um quadro só, derivação impecável de ponta a ponta, e no meio dela um recorte vazado com a silhueta de um contrato — a prova envolve o buraco** | **Escolhido** |
| C | Substituição | Só o giz gasto até o toco, sem quadro | Descartado — reprova no teste do substantivo: giz sozinho é objeto de "esforço", não do argumento. E o post não fala de esforço, fala de ordem |

**Testes do conceito B:** troca — um artigo sobre outro assunto não tem uma demonstração
matemática completa cercando um vazio com forma de contrato; passa. Substantivo — o quadro
vem do texto, literal. Alt-text cego — afirma a tese do post, não descreve formas. Legenda —
dispensa.

**A torção:** quadro cheio de fórmula é clichê de "matemática difícil". A torção é que aqui a
fórmula está **certa e completa** — o que falta não é a conta, é o objeto que ela descreve.
Inverte o clichê em vez de repeti-lo.

### Prompt (Nano Banana Pro)

```
A cut-paper collage of a single school blackboard, photographed flat against a chalk-white
paper ground #F7F7F5.

The blackboard is one large rectangle of deep forest green paper #0F3D27 with clean
scissor-cut edges, occupying most of the frame, carrying a hard-edged solid drop shadow in
#0A3320 offset a few millimeters down and right, with completely sharp shadow edges as flat
paper produces.

Across the whole surface of the board: a dense, orderly, continuous handwritten mathematical
derivation in white chalk — many lines of equations flowing left to right and top to bottom,
line after line, evenly spaced and confidently written, filling the board edge to edge like a
proof that was completed without hesitation. The chalk strokes have real chalk texture, dusty
and slightly broken, with faint eraser smudges between some lines.

At the visual center of the board, interrupting the derivation: a rectangular hole cut clean
through the board, its edges torn rather than cut, showing the white paper fiber of the tear
and revealing the chalk-white ground behind it. The hole has the plain silhouette of a
document or contract — a simple upright rectangle with one corner folded. The chalk equations
run right up to the edges of the hole on all sides and continue past it, as if the derivation
were written around something that was never there.

One single element in lime #CDF163: a small chalk-drawn arrow at the right edge of the board,
pointing at the hole, drawn in lime chalk instead of white.

Composition: the board sits on a slight diagonal, off-center toward the upper right, with
generous empty chalk-white paper along the lower left. Flat overhead view, completely even
lighting across the whole sheet, no vignette.

Style: physical paper collage combined with real chalk mark-making, visible paper fiber, cut
edges on the board and a torn edge on the hole, flat opaque spot colors, hard-edged offset
shadow. The equations are handwriting, dense and continuous.

Aspect ratio 4:5, 2K resolution.
```

**Nota de contexto (pt-BR):** a derivação precisa parecer **completa e segura** — é esse o
ponto: a conta batia. O buraco é a única borda rasgada da peça, e é onde o argumento está.
O lime aparece uma vez, na seta de giz que aponta para o vazio — a virada é perceber a falta,
não a conta.

**Se a equação sair ilegível ou com símbolo inventado, está correto** — não se trata de uma
fórmula real e não deve ser lida; o que precisa ler é a densidade e a ordem da escrita.

### Restrições em enquadramento positivo

Equação em escrita à mão contínua e densa, cobrindo a superfície inteira; buraco com borda
rasgada e fibra visível; borda do quadro cortada reta; sombra sólida de borda dura; três cores
de papel no total; lime em um único elemento; composição em diagonal fora do centro; imagem
livre de palavras legíveis, título e rótulo.

### Alt-text

> Colagem: um quadro-negro de papel verde-escuro, coberto de ponta a ponta por uma derivação
> matemática em giz branco, escrita de forma contínua e segura. No centro do quadro, um buraco
> de bordas rasgadas com o formato de um contrato — as equações passam ao redor dele e seguem
> em frente, como se a demonstração tivesse sido escrita em volta de algo que nunca esteve
> ali. Uma seta de giz verde-limão aponta para o buraco.

---

## `ilu-02` — o livro lido de trás para frente

**Onde entra:** fim da seção "A segunda lacuna: dinheiro no tempo", após "o gargalo raramente
é a matemática. É o alicerce." — o parágrafo que cita Hull (capítulos 4–6 antes do 10), o
primeiro módulo do CFA e o pré-requisito da GFMI.

**Frase que a peça carrega:** a ordem correta estava impressa no livro que ele já tinha —
juros primeiro, opções depois. Ele leu ao contrário.

### Divergência

| # | Estrutura | Conceito | Veredito |
|---|---|---|---|
| A | Justaposição | O sumário do livro ao lado da trajetória real dele, como duas colunas | Descartado — exige numeral e nome de capítulo legíveis, e a regra da marca mantém a peça sem texto. Vira tabela, não ilustração |
| B | Fusão | Uma árvore cujo tronco é feito de páginas | Descartado — é a peça antiga (copa e raiz) com fantasia nova. Árvore/alicerce é metáfora de dicionário e já tinha sido a escolha fraca da primeira rodada |
| C | **Substituição** | **O miolo do livro visto de perfil: as primeiras páginas ainda seladas, sem terem sido abertas; as últimas gastas e dobradas. O leitor está ausente — o estado do papel conta a história inteira** | **Escolhido** |

**Testes do conceito C:** troca — páginas iniciais seladas e finais gastas é a assinatura
exata de "li fora de ordem"; nenhum outro assunto reivindica isso. Substantivo — o livro vem
do texto (Hull, citado com capítulo). Alt-text cego — afirma o argumento sem o post ao lado.
Legenda — dispensa.

**Por que este conceito é forte no estilo colagem:** o assunto é papel e o material é papel.
A borda não cortada das primeiras páginas e a dobra das últimas não são representações de
desgaste — são desgaste real do próprio material da peça. Livro aberto é clichê; livro com as
primeiras páginas ainda **fechadas** é o argumento.

### Prompt (Nano Banana Pro)

```
A cut-paper collage showing a single thick book seen from its fore-edge, lying flat, so the
viewer looks straight at the stacked edges of all its pages. Photographed flat against a deep
forest green paper ground #0F3D27.

The page block is built from many thin horizontal strips of chalk-white paper #F7F7F5 stacked
one on top of another, each strip a separate visible layer, so the block reads as hundreds of
page edges seen from the side.

The lower third of the stack — the first pages — is different from the rest: those strips are
still joined at their outer edge, sealed shut in pairs with an unbroken folded edge, never
slit open. They lie perfectly flat, pristine, tightly aligned, their edges clean and
untouched.

The upper two thirds — the later pages — are visibly used: strips fanned slightly apart at
irregular intervals, several with soft torn edges showing white paper fiber, three or four
folded over at the corner into dog-ears, the whole upper section looser and thumbed.

Standing upright out of the used upper section, planted deep in the back of the book: one
narrow ribbon bookmark in grove green paper #2D9E67, rising clear of the block. Nothing marks
the sealed lower section at all.

Along the left side of the page block, a coarse visible halftone dot pattern in grove green
#2D9E67 printed over the white strips, its registration shifted three millimeters off from
the paper edges it should align with, dots spilling past on one side.

One single element in lime #CDF163: the very lowest strip of the sealed section, cut from
lime paper — the first page, still closed.

Composition: the book block runs on a strong diagonal from lower left to upper right, placed
off-center with generous empty deep forest ground in the upper left. Flat overhead view,
completely even lighting, no vignette.

Style: physical paper collage, visible paper fiber and cut edges, flat opaque spot colors,
hard-edged offset shadows in #0A3320, coarse halftone screen. No lettering, no numerals, no
page numbers anywhere in the image.

Aspect ratio 4:5, 2K resolution.
```

**Nota de contexto (pt-BR):** a distinção entre as duas seções do miolo é o argumento inteiro
e precisa ser inequívoca — embaixo, páginas **ainda seladas, nunca abertas**; em cima, páginas
gastas, dobradas e com marcador enfiado fundo. O lime marca a primeira página, a que ficou
fechada: é a virada do post ("dá para voltar e preencher o alicerce depois"). O marcador verde
no fim, sem nenhuma marca no começo, é o que fecha a leitura sem precisar de número de
capítulo.

### Restrições em enquadramento positivo

Miolo visto de perfil, com cada página como tira de papel separada; terço inferior com bordas
dobradas e seladas, perfeitamente alinhado; dois terços superiores com bordas rasgadas, orelhas
dobradas e espaçamento irregular; marcador plantado na parte de cima; retícula de meio-tom fora
de registro na lateral; lime em uma única tira; imagem livre de letras, algarismos e numeração
de página.

### Alt-text

> Colagem: um livro grosso visto de lado, com as páginas empilhadas à mostra. O terço de
> baixo — as primeiras páginas — está com as bordas ainda dobradas e seladas, nunca abertas,
> perfeitamente alinhado; a primeira de todas é verde-limão. Os dois terços de cima estão
> gastos: páginas rasgadas, cantos dobrados e um marcador verde enfiado bem no fim do livro.
> Nada marca o começo.

---

# Estilo B — Notas de um Professor (desenho técnico esquemático)

Post: `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`

## Material concreto colhido do post

**Objetos:** o balcão — "O outro lado do balcão" é título de seção; a conta corrente; o
financiamento imobiliário, dado no texto como destino do dinheiro. **Instituições e
documentos:** Bacen, CVM, FGC, Lei nº 4.728/1965, Relatório de Estabilidade Financeira de
abril de 2018. **Números:** compulsório de 21% sobre recursos à vista contra 20% a prazo; FGC
até R$ 250 mil, teto de R$ 1 milhão a cada 4 anos. **Termo do regulador:** "transformação de
maturidade", nomeada pelo próprio Bacen. **Verbos:** captar, reter, transformar, emprestar,
abrir mão da disponibilidade.

---

## `ilu-01` — os dois lados do balcão

**Onde entra:** fim da seção "O outro lado do balcão: o CDB como passivo do banco", após o
parágrafo que nomeia a transformação de maturidade.

**Frase que a peça carrega:** muitos depósitos curtos, do lado do investidor, viram um
financiamento longo do outro lado do balcão — é o mesmo dinheiro, e o balcão é a linha que
separa os dois papéis.

### Divergência

| # | Estrutura | Conceito | Veredito |
|---|---|---|---|
| A | Justaposição | Uma pilha de retângulos curtos ao lado de um retângulo longo, com cotas | Descartado — reprova no teste do substantivo: são formas puras, nenhum objeto do texto. É a peça da primeira rodada com outro arranjo |
| B | **Fusão** | **O balcão como linha-base do desenho: acima dele, muitos depósitos curtos; abaixo, os mesmos volumes recompostos numa viga longa que sustenta a elevação de uma casa. Um objeto só, atravessando a linha** | **Escolhido** |
| C | Substituição | Só a casa, com a fundação feita de depósitos empilhados como tijolos | Forte, mas descartado por posição: perde o balcão, que é justamente o título e o assunto da seção onde a peça está ancorada. Fica como alternativa se o autor quiser a peça em outro ponto do texto |

**Testes do conceito B:** troca — depósitos curtos virando financiamento imobiliário através
de um balcão não serve para outro assunto; passa com folga. Substantivo — balcão e casa, os
dois do texto. Alt-text cego — descreve o mecanismo que o Bacen chama de transformação de
maturidade. Legenda — dispensa.

**Por que funciona no estilo esquemático:** desenho técnico tem uma convenção pronta para
"linha que separa dois domínios" — a linha de terreno da elevação arquitetônica. O balcão do
texto e a linha de terreno do desenho são a mesma linha. E a diferença de prazo continua sendo
cota, que foi o único elemento que funcionou na primeira rodada — mantido de propósito.

### Prompt (Nano Banana Pro)

```
A flat orthographic technical elevation drawing on an engineering plate, no perspective and
no depth, background completely flat deepForest #0F3D27 edge to edge.

One continuous horizontal datum line in pale mist #E2E8F0 runs the full width of the plate at
mid-height, dividing the drawing into an upper and a lower half. This line is the counter.

Above the line: eleven small identical upright rectangles standing in a row along the line,
each one narrow and short, drawn in flat grove green #78C9A4 with constant-weight outlines and
perfectly square corners, evenly spaced with equal gaps. Beneath the row, a single dimension
line spans the width of just one of those rectangles, terminating in two small straight tick
marks — a very narrow measurement, showing how short one unit is.

Below the line, directly beneath the row: one long horizontal beam spanning nearly the full
width of the plate, drawn in the same flat grove green outline, its length clearly equal to
the eleven rectangles above placed end to end. A second dimension line runs beneath the beam
across its entire length, with the same straight tick terminations, so the two measurements
read as a direct comparison of one short unit against one long span.

Resting on that beam, in the lower portion of the plate: the front elevation of a simple house
— a plain rectangle with a triangular pitched roof, two square window openings and one door
opening, drawn in the same constant-weight grove green outline, orthographic and flat, sitting
squarely on the beam as a building sits on its foundation.

Construction detail: mist #E2E8F0 hairlines at one-third the weight of the main outlines mark
the vertical center axis of the plate and extend the datum line slightly past the drawing on
both sides, as construction lines do on a real drafting plate. One thin leader line with a
small dot termination points at the junction where the row above meets the beam below,
ending in empty space with no label attached.

One single element in lime #CDF163: the short dimension line above, drawn solid in lime
instead of mist — the measurement of what the depositor gave up.

A sparse dot grid in mist #E2E8F0 at very low density occupies only the outer margins, well
clear of the drawing.

Style: precision drafting plate rendered as flat vector art — constant line weight, sharp
square corners, absolutely even fills, strict orthographic projection, everything aligned to
the datum. No lettering, no numerals, no annotation text anywhere in the image.

Aspect ratio 16:9, 2K resolution.
```

**Nota de contexto (pt-BR):** o balcão virou a linha de terreno do desenho — a mesma linha que
o texto usa como título de seção. Acima, os muitos depósitos curtos; abaixo, o mesmo
comprimento recomposto numa viga só, sustentando a casa que o texto nomeia (financiamento
imobiliário). A equivalência entre as onze unidades de cima e a viga de baixo é o argumento:
não é dinheiro novo, é o mesmo dinheiro com outro prazo. O lime marca a cota curta — o que o
investidor abriu mão.

### Restrições em enquadramento positivo

Projeção ortogonal estrita; contorno de espessura constante; cantos retos; linha de terreno
única atravessando a largura inteira; unidades de cima idênticas e igualmente espaçadas; viga
de baixo com comprimento equivalente à soma delas; casa em elevação frontal simples apoiada na
viga; duas cotas comparáveis; lime em um único elemento; imagem livre de letras e algarismos.

### Alt-text

> Desenho técnico sobre fundo verde-escuro: uma linha horizontal atravessa a prancha ao meio —
> é o balcão. Acima dela, onze retângulos curtos e idênticos, enfileirados, representam os
> depósitos de curto prazo; uma cota verde-limão mede a largura de um só deles. Abaixo da
> linha, o mesmo comprimento total aparece recomposto numa única viga longa, medida por uma
> segunda cota, e sobre essa viga se apoia a elevação de uma casa. O mesmo dinheiro, com outro
> prazo, do outro lado do balcão.
