# Capa — "Quando os Modelos se Rebelam"

Nasce da tese e do gancho de `processo/01-briefing.md`, não de um detalhe do corpo do texto.
Briefing completo (três camadas, três operações, testes de rejeição) em
`processo/08-briefing-visual.md`.

**Linha editorial:** Spoiler → estilo **colagem editorial**
(`.claude/skills/prompts-visuais/references/estilos-ilustracao.md`, Estilo A).

## Conceito e estrutura de metáfora

Uma alavanca de papel recortado, montada num eixo fixo, continua apontando em linha reta ao
longo de um traçado — até o ponto exato em que esse traçado é interrompido por um corte reto,
revelando um vão vazio. A alavanca não desvia, não quebra, não reage: continua fazendo
exatamente o que sempre fez, indiferente ao fato de que o chão que ela seguia já não está
mais lá.

**Proveniência:** o autor sugeriu, para a capa, "uma rebelia de máquinas humanoides como nos
filmes de Terminator". A referência cinematográfica foi descartada (propriedade de terceiros;
incompatível com o estilo de colagem editorial da linha Spoiler) — mas a estrutura da ideia
foi levada adiante e invertida (Operação de Torção, `08-briefing-visual.md`): não é uma
ferramenta que decide se voltar contra quem a construiu — é uma ferramenta que nunca decide
nada, e é essa obediência cega à regra original que produz o desastre quando o mundo muda por
baixo dela. É a leitura que o próprio post defende: "um modelo é uma ferramenta que não sabe
que é uma ferramenta."

**Operação geradora:** cruzamento (a metáfora da alavanca, do fechamento do post, aplicada à
cena do corte no traçado, da seção 2). **Estrutura de metáfora:** justaposição — o mecanismo
intacto ao lado do vão vazio.

## Linha editorial e estilo aplicado

Spoiler → colagem editorial: papel recortado em camadas com sombra chapada (sem blur),
retícula de meio-tom discreta em uma camada, corte reto (guilhotina) marcando a ruptura do
traçado, composição assimétrica com diagonal dominante. Fundo chalk (o post não é sobre
perda pessoal nem "mundo invertido" — é sobre indiferença mecânica, tom mais frio e claro que
os posts de erro/perda do corpus).

## Prompt completo (Nano Banana Pro)

Formato: cena narrada, enquadramento positivo, sem negative prompt
(`references/geradores/nano-banana-pro.md`).

> A flat cut-paper collage illustration, editorial style. A single mechanical lever — a
> straight paper arm mounted on a simple circular pivot, cut from solid-color grove-green
> paper (#2D9E67), layered with a flat solid drop shadow (no blur, hard offset in
> forest-900 #0A3320) — extends horizontally across the frame, perfectly aligned with a
> narrow straight paper strip beneath it representing a track or roadway, cut from slate
> paper (#4A5568). In the center third of the frame, the straight paper strip ends abruptly
> at a clean guillotine-straight vertical cut — not a torn edge — and beyond that cut the
> paper strip simply does not continue: an empty gap of bare chalk background (#F7F7F5)
> occupies the space where the strip should keep going. The lever's arm keeps pointing
> straight ahead, unbroken and undeviating, directly into that empty gap. A single thin
> line of lime-colored paper (#CDF163) marks the exact edge of the cut, the one accent
> color in the whole piece, precise and small — not a glow, a flat lime paper edge. One
> layer of the lever's paper arm carries a visible halftone dot pattern, large dots, printed
> texture, evoking the brand's data-grid motif. One other paper layer is offset by a few
> pixels from the shape it should align with, a slight risograph-style color misregistration,
> flat spot color only, no gradient anywhere in the image. Background is solid flat chalk
> (#F7F7F5) with no texture. Asymmetric composition, the lever and track running along a
> dominant diagonal from lower-left to upper-right, the cut and the empty gap positioned in
> the center third of the frame. No text, no numbers, no labels anywhere in the image. No
> human figure, no face, no generic finance iconography (no coins, no dollar signs, no
> candlestick charts, no vaults, no handshakes, no robot or AI brain, no bank building, no
> pie chart). Sharp right-angle geometry throughout, no rounded corners except the lever's
> circular pivot point. 16:9 aspect ratio, 2400x1350px.

**Nota de contexto (para quem reler este arquivo depois, não para o gerador):** a cena é o
mecanismo da capa descrito em `08-briefing-visual.md` — uma alavanca (a metáfora de
fechamento do post) cruzada com o corte no traçado (a cena da seção 2, "O radar da
rodovia"). Lime aparece uma única vez, marcando a linha do corte — é a "virada" da peça.
Fundo chalk, não deepForest: o registro é frio/indiferente, não de perda.

## Restrições em enquadramento positivo

- A imagem deve conter exatamente um mecanismo (a alavanca) e um traçado com corte — nenhum
  segundo símbolo, nenhuma figura adicional.
- O vão além do corte deve ficar visivelmente vazio, sem preenchimento decorativo.
- Toda cor deve ser chapada (flat), com sombra sólida sem desfoque.
- Geometria de canto reto em toda a peça, exceto o pivô circular da alavanca.
- Nenhum texto, número, rótulo, moeda, cifrão, candlestick, cofre, aperto de mão, robô/
  cérebro de IA, prédio de banco, gráfico de pizza ou figura humana reconhecível.

## Proporção e resolução

16:9 — gerar em 2400×1350px, exportar em 1456×816px para a capa do artigo
(`prompts-visuais/SKILL.md`).

## Zona segura

O corte no traçado (o ponto de foco, marcado em lime) fica no terço central do quadro — não
na periferia — para sobreviver aos recortes automáticos que a Substack aplica em outros
formatos (e-mail, redes).

## Alt-text final

Ilustração em colagem de papel recortado: uma alavanca verde, montada num eixo, aponta em
linha reta ao longo de uma faixa que representa um trajeto — até o ponto onde a faixa é
cortada abruptamente, marcado por uma fina linha lime, revelando um vão vazio. A alavanca
continua apontando para o vão, sem desviar.
