# Exemplos de prompt por estilo — regeração de posts publicados

Prompts de teste gerados em 31/08/2026 para validar o sistema de estilos de
`estilos-ilustracao.md` antes de ele rodar em post novo.

**São regerações, não substituições.** Os `ilustracoes.md` dos posts publicados continuam
como estão — estes prompts existem para o autor comparar lado a lado o mesmo conceito no
sistema antigo (glow verde sobre fundo escuro) e no novo (estilo por linha editorial, sem
glow). O **conceito de cada peça foi mantido igual de propósito**: o que muda no teste é só o
estilo, senão o A/B não isola nada.

Servem também como referência de calibragem — quando um prompt novo sair torto, compare com
estes.

---

# Estilo B — Notas de um Professor (desenho técnico esquemático)

## Teste 1 — `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`, `ilu-01`

**Conceito original (mantido):** o mesmo CDB que é *ativo* para o investidor é *passivo* para
o banco; entre uma coisa e outra existe o ALM, que transforma prazo curto de captação em prazo
longo de crédito.

**Por que este conceito ganha no estilo esquemático:** "transformação de prazos" é, literalmente,
uma mudança de **dimensão**. Desenho técnico tem uma convenção pronta para isso — a linha de
cota. O argumento central do post vira uma cota curta entrando e uma cota longa saindo, sem
uma palavra escrita na peça. A versão anterior precisava de um "fio de luz" para sugerir o
mesmo, porque o vocabulário de glow não tem como desenhar prazo.

### Prompt (Nano Banana Pro)

```
A flat orthographic technical schematic of a maturity-transformation mechanism, drawn as a
front-elevation cutaway on an engineering plate, no perspective and no depth.

Left third: a short horizontal capsule form representing an incoming short-term deposit,
drawn in flat grove green #78C9A4 with a constant-weight outline. Directly beneath it, a
dimension line spanning only its short width, terminating in two small straight tick marks —
a narrow measurement.

Center: a tall rectangular chamber with perfectly square corners, drawn in the same flat
grove green outline over the plate, its interior divided by one vertical hairline into a
slightly recessed left compartment and a slightly wider right compartment. At the exact
center of that dividing hairline sits a single small square node filled solid in lime
#CDF163 — the only saturated fill anywhere on the plate — marking where the transformation
happens.

Right third: a long horizontal capsule form representing outgoing long-term credit, same flat
grove green outline, clearly several times wider than the one on the left. Beneath it, a
second dimension line spanning its full long width, with the same straight tick terminations,
so the two measurements read as a direct comparison.

A single thin connector line runs left to right through the whole assembly at mid-height,
passing through the lime node, changing thickness slightly as it exits the chamber.

Construction detail: pale mist #E2E8F0 hairlines at one-third the weight of the main outlines
mark the horizontal center axis across the full width and the vertical center of the chamber,
extending slightly past the forms as construction lines do on a real drafting plate. Two thin
leader lines with small dot terminations point inward at the chamber and at the lime node,
ending in empty space with no labels attached.

Background: completely flat deepForest #0F3D27, edge to edge, uniform. A sparse dot grid in
mist #E2E8F0 at very low density occupies only the outer margins, well clear of the mechanism.

Style: precision drafting plate rendered as flat vector art — constant line weight, sharp
square corners, absolutely even fills, orthographic projection. The whole assembly sits
centered with generous empty plate around it. No lettering, no numerals, no annotation text
anywhere in the image.

Aspect ratio 16:9, 2K resolution.
```

**Nota de contexto (pt-BR):** a cota curta à esquerda e a cota longa à direita são o argumento
inteiro do post — captação curta vira crédito longo — desenhadas na convenção de prancha
técnica, sem texto. O lime aparece uma vez só, no nó central: é o ALM, o ponto que o parágrafo
está explicando. Todo o resto do mecanismo fica em grove estrutural, e as linhas de construção
em mist ficam um degrau abaixo em contraste, organizando sem competir.

### Restrições em enquadramento positivo

Fundo chapado de cor única; contorno de espessura constante; cantos retos; projeção
ortogonal; preenchimento saturado presente em exatamente um elemento; superfícies restantes em
verde estrutural; imagem inteiramente livre de letras e algarismos.

### Alt-text

> Esquema técnico sobre fundo verde-escuro: à esquerda, uma forma curta representa o depósito
> de curto prazo, com uma linha de cota estreita marcando seu prazo. Ao centro, uma câmara
> dividida ao meio — passivo de um lado, ativo do outro — com um nó verde-limão exatamente na
> divisória, marcando a área de ALM. À direita, uma forma bem mais longa representa o crédito
> concedido, com uma linha de cota várias vezes mais larga. A comparação entre as duas cotas é
> a transformação de prazos.

---

# Estilo A — Spoiler (colagem editorial)

## Teste 2 — `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`, `ilu-01`

**Conceito original (mantido):** uma escada cortada ao meio por um limiar; acima, degraus em
ordem; abaixo, os mesmos degraus espelhados e se desfazendo — o Upside Down da carreira.

**O que muda na tradução para colagem:** o limiar deixa de ser uma linha que brilha (glow é
anti-padrão agora) e passa a ser o que a colagem já tem de graça — **a emenda entre duas folhas
de papel**. O material faz o trabalho que a luz fazia. E a metade que "se desfaz" deixa de ser
partícula difusa e vira o que colagem faz melhor: papel rasgado e retícula de meio-tom
grosseira, deslocada do registro.

### Prompt (Nano Banana Pro)

```
A cut-paper collage of a single staircase, photographed flat, built from four layers of
opaque colored paper on a chalk-white paper ground #F7F7F5.

Upper half: five plain rectangular steps ascending left to right, each one a separate piece
of scissor-cut forest green paper #1B6A45 with clean straight edges, laid slightly overlapping
so each step's cut edge is visible against the one behind it. Each piece casts a hard-edged
solid drop shadow in deep forest #0A3320, offset a few millimeters down and right, with
completely sharp shadow edges as flat paper produces.

Across the exact middle of the composition: a horizontal band where two sheets of paper meet
edge to edge — a visible seam, one sheet chalk white and the sheet below it mint #E6F4EE,
their straight cut edges butted together with a hairline of shadow between them. This seam is
the threshold, made of nothing but the join between two materials.

Lower half, mirroring the steps above: the same five steps inverted, but cut from mint paper
#E6F4EE overprinted with a coarse visible halftone dot pattern in grove green #2D9E67, the
dots large enough to read clearly as printed screen. The halftone layer is deliberately
misregistered, shifted three or four millimeters off from the paper shapes it should fill, so
green dots spill past the edges on one side and leave bare paper on the other. The two lowest
inverted steps have torn paper edges instead of cut ones, their white fibrous tear showing,
and they sit slightly rotated out of alignment with the rest.

One single element in lime #CDF163: the topmost step of the upper staircase, cut from lime
paper, the one step that is in the right place.

Composition: the staircase runs on a dominant diagonal from lower left to upper right,
positioned off-center with generous empty chalk paper on the left. Flat overhead view,
completely even lighting across the whole sheet, no vignette.

Style: physical paper collage, visible paper fiber texture and cut edges, flat opaque spot
colors, hard-edged offset shadows, coarse halftone screen. No lettering, no numerals, no
handwriting anywhere in the image.

Aspect ratio 4:5, 2K resolution.
```

**Nota de contexto (pt-BR):** a emenda entre duas folhas substitui a linha que brilhava — em
colagem, o limiar é material, não luz. O desalinho de registro do meio-tom e as duas bordas
rasgadas na parte de baixo fazem o "se desfazendo" do conceito original sem partícula difusa
(que cairia em blob, anti-padrão §4.5). O lime aparece uma vez, no degrau do topo: é a virada
— o único degrau que está no lugar certo.

### Restrições em enquadramento positivo

Cor de papel opaca e chapada; borda de corte reta como padrão e rasgo apenas nos dois
fragmentos de baixo; sombra sólida de borda dura; retícula de meio-tom com ponto visível;
quatro cores de papel no total; lime em um único elemento; composição em diagonal fora do
centro; imagem inteiramente livre de letras e algarismos.

### Alt-text

> Colagem de papel recortado sobre fundo branco: na metade de cima, cinco degraus em papel
> verde-escuro sobem em ordem, cada um com sombra sólida — o degrau do topo é verde-limão, o
> único no lugar certo. No meio, a emenda entre duas folhas de papel marca o limiar. Na metade
> de baixo, os mesmos cinco degraus aparecem espelhados de cabeça para baixo, impressos em
> retícula verde fora de registro, e os dois últimos têm a borda rasgada e estão tortos.

---

## Teste 3 — `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`, `ilu-02`

**Conceito original (mantido):** uma árvore em corte — copa completa em cima, raiz curta que
não alcança o solo firme embaixo. Domínio avançado apoiado num alicerce que não terminou de
crescer.

**Peça deliberadamente sem lime.** A regra de `estilos-ilustracao.md` é que lime marca virada
ou conquista real, e esta peça é sobre incompletude: não há virada nenhuma nela. Deixar o lime
de fora aqui é o teste de que a regra tem dente — no sistema antigo, a copa brilhava em verde
saturado justamente porque a regra do "elemento iluminado" obrigava um destaque por peça,
mesmo quando o argumento não pedia.

### Prompt (Nano Banana Pro)

```
A cut-paper collage of a single tree in cross-section, showing canopy above and root system
below, arranged on a deep forest green paper ground #0F3D27.

Upper two-thirds: a full rounded canopy assembled from seven or eight separate scissor-cut
pieces of grove green paper #2D9E67, overlapping in visible layers so every cut edge reads
against the piece behind it. Two of the canopy pieces are overprinted with a coarse visible
halftone dot pattern in forest green #1B6A45, the dots large enough to read as printed screen,
shifted slightly off register from the paper shapes beneath them. Each canopy piece carries a
hard-edged solid drop shadow in deep forest #0A3320 with completely sharp edges.

A narrow straight trunk in slate gray paper #4A5568 runs down from the canopy, cut as one
clean strip.

Lower third, beneath an implied ground line: three thin short root strips in the same slate
gray paper, each one narrower than the trunk, reaching downward but visibly stopping short.
All three have torn bottom edges with white paper fiber showing at the tear.

Near the very bottom edge of the composition: one horizontal band of mist gray paper #E2E8F0
spanning the full width, with a clean straight cut top edge, representing bedrock. A clear
empty gap of bare deep forest ground separates the torn root tips from that band — the roots
plainly do not reach it.

Composition: the tree sits slightly right of center on a vertical axis, with generous empty
ground on the left. Flat overhead view, completely even lighting across the sheet, no vignette.

Style: physical paper collage, visible paper fiber texture and cut edges, flat opaque spot
colors in a restrained four-color palette, hard-edged offset shadows, coarse halftone screen.
No lettering, no numerals, no handwriting anywhere in the image.

Aspect ratio 4:5, 2K resolution.
```

**Nota de contexto (pt-BR):** copa em camadas fartas e recortadas com tesoura; raiz em três
tiras finas com a borda **rasgada**, porque é ali que o argumento está — o que não terminou de
crescer. O vão de papel nu entre a raiz e a faixa de solo firme é o assunto da peça, e por isso
recebe o maior espaço vazio da composição. Sem lime, deliberadamente: nada aqui é conquista.

### Restrições em enquadramento positivo

Cor de papel opaca e chapada; copa com borda de corte reta e raiz com borda rasgada; sombra
sólida de borda dura; retícula de meio-tom em duas peças da copa; quatro cores de papel no
total; vão vazio visível entre a ponta da raiz e a faixa de solo; imagem inteiramente livre de
letras e algarismos.

### Alt-text

> Colagem de papel recortado sobre fundo verde-escuro: em cima, uma copa de árvore farta,
> montada em várias camadas de papel verde recortado com tesoura, duas delas impressas em
> retícula. Um tronco fino cinza desce até três raízes curtas, mais estreitas que o tronco,
> todas com a borda de baixo rasgada. Elas param bem antes de uma faixa cinza-clara no rodapé
> que representa o solo firme — entre a ponta das raízes e essa faixa sobra um vão vazio.
