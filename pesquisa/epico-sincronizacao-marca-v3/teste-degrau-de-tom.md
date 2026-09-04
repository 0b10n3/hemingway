# Teste de validação — degrau de tom em vez de sombra chapada

Peça de teste autocontida, **não é asset de post nenhum** — valida que a instrução corrigida em
`.claude/skills/prompts-visuais/references/estilos-ilustracao.md` ("A escada") de fato produz
separação de camada legível sem sombra projetada, antes de considerar a Fase 5 (sincronização
com `brand/DESIGN.md` v3.0) pronta para uso real no próximo post. Segue o template corrigido de
`templates-prompt.md` linha a linha.

## Conceito

Uma pilha de quatro folhas de papel recortado, cada uma um documento financeiro estilizado
(borda reta, sem texto legível), empilhadas em profundidade decrescente — a mesma metáfora da
"escada" que a regra descreve, escolhida de propósito porque é o teste mais direto do
mecanismo: se a escada de tom não ler como pilha sem sombra, nenhuma outra composição vai.

## Prompt (Nano Banana Pro, cena narrada, enquadramento positivo)

A flat paper-cut collage illustration, four rectangular sheets of paper stacked at a slight
diagonal offset, each sheet a single perfectly uniform flat color from edge to edge with no
shading, no highlight and no darkening at any edge — like a tabletop scanner image, one
uniform studio light source evenly across the whole frame. The four sheets, from the bottom of
the stack (darkest) to the top (lightest), are exactly: hex #141414, hex #0F3D27, hex #125233,
hex #1B6A45 — cite each hex precisely, each sheet is its own flat uniform color, never a
gradient or blend between sheets. A small paper-cut arrow shape in flat color hex #2D9E67 sits
on top of the stack, pointing toward the top-right sheet, clearly a separate object resting on
the pile, not another layer of it. One small paper-cut circle in flat color hex #CDF163 marks
a single corner of the topmost sheet — the only accent-colored shape in the frame, covering
well under one percent of the total image area. Straight paper-cut edges throughout, 90-degree
or 45-degree cuts only, no curved or torn edges anywhere. Background is a solid flat color hex
#F7F7F5 filling at least half the frame, with generous negative space around the stack. No
drop shadow, no soft shadow, no blur, no glow, no gradient, no bevel, no emboss, no 3D
rendering, no rounded corners, no text or lettering anywhere in the image. Square 1:1
composition, 2K resolution.

## Checklist (antes de gerar, `geradores/nano-banana-pro.md` + `estilos-ilustracao.md`)

- [x] Conceito simples, autocontido — não depende de briefing de post real (peça de validação).
- [x] Composição centrada/simétrica é aceitável aqui — é teste de mecanismo, não de registro
      pessoal/assimétrico (`estilos-ilustracao.md`, "Quando o argumento pede precisão mecânica"
      cobre esse caso; aqui a simetria não é sequer o foco, mas não viola a regra).
- [x] Todo hex citado por valor exato — âncora absoluta, nunca "mais claro que a folha
      anterior" (lição de "A escada").
- [x] Nenhuma das palavras banidas ("glow"/"glowing"/"luminous"/"bloom"/"gradient"/"shadow"/
      "drop shadow"/"soft shadow") aparece em forma afirmativa — só nas restrições negativas em
      enquadramento positivo ("no drop shadow" etc., seguindo o formato que o guia oficial do
      Nano Banana Pro recomenda apesar de não suportar negative prompt de fato).
- [x] Lime aparece em exatamente um elemento, cobertura mínima.
- [x] Nenhum texto pedido na imagem.
- [x] Proporção suportada (1:1), resolução 2K.

## Resultado

Ver `raw/2026-09-04-v1.png` — gerado via `agy` (Nano Banana Pro).

## Avaliação

**Verificação por pixel feita nesta sessão** (não só inspeção visual) — `Pillow`, mesmo método
de `checagem-paleta.md`, adaptado para inspecionar transições em vez de cor dominante:

- **A escada funciona.** Nas quatro folhas, a transição de uma folha para a seguinte (ex.:
  fundo `#F7F7F5` → folha `#0F3D27` em `x=300`, `y≈276→280`) é um corte de 1 amostra em passo
  de 4px — instantâneo, sem gradiente, hex batendo com o pedido (`(18,63,40)` medido vs.
  `#125233`/`#0F3D27` pedidos, bem dentro da tolerância de geração). O mecanismo central do
  achado S7 — profundidade por degrau de tom, sem sombra — **se comprova na prática** para a
  separação entre camadas da pilha.
- **Achado real, não ignorado:** há uma sombra suave e localizada no canto inferior-direito da
  pilha, contra o fundo — verificada por varredura fina de pixel (`x=750→798`, `y=700`): uma
  faixa de ~28px com gradiente de `(28,87,55)` até `(245,245,243)` (chalk), visivelmente mais
  larga que antialiasing de borda reta (1–3px esperado). O gerador não seguiu a restrição
  "no drop shadow" nessa região específica, apesar dela estar explícita no prompt. Não é um
  problema da instrução (o resto da peça obedece), é uma aderência parcial do gerador — mesma
  classe de ressalva que `checagem-paleta.md` já documenta para `ilu-NN`/capa ("geradores de
  imagem podem não aderir 100% ao prompt").
- **Figura e acento corretos:** a seta grove fica claramente sobre a pilha, não como mais uma
  folha; o círculo lime é único, pequeno, num canto — dentro do teto de 1% de área a olho (não
  medido por script nesta rodada).

**Conclusão:** a correção da instrução está certa e majoritariamente eficaz — o problema
residual é de aderência do gerador numa região localizada, não da regra em si. Recomendação
antes do próximo uso real: reforçar a restrição negativa especificamente perto de bordas
externas da pilha (ex.: "the outer edge of the stack meets the background with a hard cut, no
falloff, no vignette") e rodar `checagem-paleta.md`/checagem de borda equivalente na primeira
peça real gerada. `[PENDENTE — decisão do autor]`: aceitar a técnica como está (a falha é
pequena e localizada) ou iterar mais uma vez o prompt antes de liberar para posts reais.
