# Épico — sobrevivência do grão à recompressão de plataforma

06/09/2026.

## Origem

`illustration.grainMaxLuminanceAmplitude` (teto de 0,028, `syntaxis.tokens.json`) especifica a
granulação de fundo desde a rodada 3 de `/marca-zero`. A lacuna estava registrada em três
lugares do monorepo (`brand/DESIGN.md` §11 item 9, `03-proposta.md` B9/L2 — arquivado em
`brand/_arquivo/revisao-2026-2026-09-06/`, `brand/_arquivo/DECISOES-HERDADAS.md` P4) e nunca
tinha número real por trás: nenhuma peça foi testada contra a recompressão de fato de LinkedIn,
Instagram ou YouTube.

## O que foi feito

1. **Peça de teste gerada** — `raw/teste-grao-v1.png` (1024×1024, Nano Banana Pro), seguindo
   `_bloco-marca.md` à risca: fundo Deep Forest (`#0F3D27`) com grão fino uniforme, pilha
   `nodeBranch` em forest.700/forest.500/grove.500, acento lime. Peça nova, não reaproveitada —
   `ilu-01` (agosto) é anterior à regra de degrau de tom/grão e não serviria de baseline válido
   para esta medição.
2. **Script de medição** — `.claude/skills/prompts-visuais/references/checagem-graos.md`:
   Pillow + numpy puro (sem scipy, sem dependência nova), no molde de `checagem-paleta.md`.
   Isola o fundo por quantização de área, mede grão como desvio-padrão de um Laplaciano de
   luminância nos pixels interiores da máscara de fundo (evita capturar borda de recorte ou
   vinheta como se fosse grão).
3. **Três perfis de recompressão** aplicados à mesma peça: LinkedIn (1200px, JPEG 80), YouTube
   thumbnail (1280×720, JPEG 90), Instagram feed (1080×1080, JPEG 80). Artefatos em
   `compressed/`.

## Resultado

| Perfil | `grain_std` | Sobrevivência |
| --- | --- | --- |
| Original | 0,03633 | — |
| LinkedIn | 0,02019 | 55,6% |
| YouTube thumbnail | 0,02157 | 59,4% |
| Instagram feed | 0,01719 | 47,3% |

O grão perde entre 40% e 53% da amplitude nos três perfis — nenhum o zera, nenhum o preserva
integralmente. Instagram foi o mais destrutivo dos três, apesar do redimensionamento mais
brando (1080×1080 contra 1024×1024 original) — a qualidade JPEG 80 dominou o efeito.

**Nota de escala, importante:** o `grain_std` desta medição (desvio-padrão de Laplaciano) não é
diretamente comparável ao valor absoluto de `illustration.grainMaxLuminanceAmplitude` (0,028,
medido como diferença simples entre duas regiões chapadas). São métricas diferentes. O que esta
medição responde — e que nenhum documento respondia antes — é a **razão de sobrevivência**
através da recompressão real, não uma comparação byte a byte com o teto.

## Consequência para o prompt-kit

`estilos-ilustracao.md` atualizado: ao escrever o prompt de uma peça nova, mirar a metade
superior da faixa de granulação aceitável (mais perto do teto de 0,028, não do meio ou do
piso) — uma peça pedida com grão sutil demais no limite inferior arrisca chegar quase lisa
depois de publicada, porque a distribuição social corta a amplitude quase pela metade. O teto
em si não muda.

## Onde isto pode estar errado

1. **Uma peça de teste, um valor de grão.** A medição não varia a intensidade do grão pedida
   no prompt — não sabemos se a razão de sobrevivência (47–59%) é constante em diferentes
   intensidades de grão de entrada, ou se peças com mais grão sobrevivem proporcionalmente
   melhor ou pior. Testar em mais de um ponto da faixa é o próximo passo óbvio se este número
   se tornar decisão de produto (não só de prompt-kit).
2. **Valores de qualidade JPEG por plataforma são prática comum documentada, não confirmados
   pela plataforma.** LinkedIn, Instagram e YouTube não publicam a qualidade de recompressão
   real, e ela muda sem aviso. Se o parâmetro mudar, esta medição precisa ser refeita — o
   script está pronto para isso, o número não é permanente.
3. **A métrica de grão (Laplaciano) é nova e provisória**, no mesmo espírito da tolerância
   `RGB_DIST_MAX` de `checagem-paleta.md` — só uma peça real passou por ela até agora.

## Pendência fechada nos documentos do monorepo

- `brand/DESIGN.md` §11 item 9 — marcada resolvida, aponta para este documento.
- `brand/_arquivo/DECISOES-HERDADAS.md` P4/L2 — atualizada com o achado.
