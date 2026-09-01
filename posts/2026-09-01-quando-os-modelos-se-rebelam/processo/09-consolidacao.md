# Consolidação — "Quando os Modelos se Rebelam"

Etapa 9. Aplica 5 (crítica estrutural) + 6 (revisão de linha) + 7 (verificação técnica) sobre
`04-draft-v1.md` e emite `post.md` (mais `capa.md`, `ilustracoes.md`, `graficos.md`,
`diagramas.md`, já produzidos na etapa 8). Checklist de `revisao-editorial/SKILL.md`, item a
item.

## 1. Coerência entre etapas

Sem contradição entre os três laudos — aplicados juntos sem conflito:

- **Crítica (05), os 4 achados médios**: todos resolvidos por corte/reordenação leve, sem
  reabrir estrutura (autorizado pelo próprio veredito de `05-critica.md`). (a) Abertura
  reescrita — corta o preâmbulo sobre hábito de compartilhar conteúdo, vai direto ao curso e
  à citação de Kempthorne em duas frases. (b) Seção 1: acrescentada uma frase-ponte ao final
  ("É essa fronteira — não abstrata, mas com data e prejuízo — que os dois casos a seguir
  tornam impossível de ignorar.") para aliviar a transição para os casos concretos. (c) Nota
  brasileira do target forward: comprimida — a descrição do payoff assimétrico virou aposto
  parentético, uma frase inteira cortada, mantendo os números e a conclusão. (d) Ordem do
  fechamento invertida: o CTA de compartilhamento agora vem antes, e "Um modelo é uma
  ferramenta que não sabe que é uma ferramenta. Cabe a você saber." fecha o texto, como o
  briefing pedia.
- **Crítica (05), achado baixo**: a linha "O cometa não muda de órbita porque o astrônomo
  publicou. / O mercado muda." voltou à forma de justaposição pura, sem a cláusula
  explicativa que o draft v1 tinha acrescentado — a nuance de contraperformatividade
  continua no parágrafo anterior, em prosa, então nada se perde.
- **Revisão de linha (06)**: todos os 25 itens de "norma" aplicados (marcação de jargão em
  aspas simples, gloss de siglas — CFO, OCC, Fed, PIB —, regência de "responder a" e "vendido
  em", comma splice, tempo verbal de "descreveria" → "descreveu"). Dos 5 itens de "linha"
  (sugestão), 4 aplicados; o item sobre o antecedente de "Eles" na abertura ficou resolvido
  por reescrita completa do parágrafo (item 1), não pela correção pontual sugerida.
- **Verificação técnica (07)**: as duas pendências abertas viraram, respectivamente, um
  `[VERIFICAR]` visível (Kempthorne) e outro (`volume ~US$35bi do target forward`) — nenhum
  resolvido silenciosamente, conforme regra 3 do checklist. As três correções pontuais
  (LTCM 25:1→26:1, datação do "US$125bi em ativos", precisão do "8,06%") foram aplicadas
  como correção direta, não como `[VERIFICAR]`, porque a verificação já entregou o número
  certo contra fonte primária — não é incerteza, é precisão. O nocional do LTCM mudou de
  "US$1,25 tri" (não encontrado em nenhuma fonte) para "US$1,3 tri" (citação direta do PWG
  1999), evitando tanto a invenção quanto um `[FAIXA]` desnecessário.

## 2. Checklist de aderência à voz (§9 do guia)

1. Jargão glossado na primeira ocorrência — ✅ (hedge, delta, VaR, CFO, Fed, OCC, PIB).
2. Exemplo depois do conceito — ✅, estrutura mantida do draft.
3. Zero negrito/itálico de ênfase — ✅ (`grep` confirma: só a tabela Teoria×Modelo usa `**`,
   uso estrutural de cabeçalho de tabela, não ênfase de frase).
4. Subtítulo H2 por seção — ✅.
5. Autoridade por autor+ano nomeado — ✅ (Derman 2011, MacKenzie 2006, Cartwright 1983,
   Knight 1921, Lakatos 1970, Dempster 2012).
6. Uma voz só, sem mistura — ✅ ensaística; a densidade da seção 1 (achado da crítica) foi
   aliviada, não eliminada — é conteúdo genuinamente denso, a frase-ponte ajuda sem forçar
   humor onde não cabe.
7. Voz ensaística — CTA + gancho + pergunta retórica genuína — ✅. Pergunta retórica: "essa
   taxonomia é rigorosa ou é a licença poética de um físico que virou banqueiro?".
8. N/A — não é voz explicativa.
9. Tiques de IA — ✅, `grep` por frases genéricas ("é importante ressaltar", "em suma",
   "estudos mostram", "pode-se dizer") não encontrou ocorrência.
10. Instituição/norma citada corretamente — ✅ (Fed, OCC, SR 11-7, PWG 1999).

## 3. `[VERIFICAR]`/`[FAIXA]` visíveis — confirmado

Dois marcadores no `post.md`, ambos visíveis no corpo do texto, não resolvidos
silenciosamente:

1. Citação de Kempthorne (abertura) — `[VERIFICAR: atribuição... não confirmada...]`.
2. Volume do target forward 2008 (~US$35 bi) — `[VERIFICAR: cifra é consenso de
   imprensa...]`.

## 4. Placeholders consistentes

`ilu-01`, `graf-01`, `diag-01` — todos citados em `post.md` com bloco correspondente em
`ilustracoes.md`/`graficos.md`/`diagramas.md`, e vice-versa. Nenhum órfão. Confirmado por
`grep` nos quatro arquivos.

## 5. Antipadrões de IA

Varredura por frases genéricas de `voz-syntaxis/references/antipadroes.md` — nenhuma
ocorrência. A revisão de linha (etapa 6) já tinha coberto a maioria dos casos relevantes
(marcação de jargão); esta passada não achou nada novo.

## 6. Frontmatter

`título`, `subtítulo` (retomado do gancho/tese do briefing), `data: 2026-09-01`,
`linha_editorial: Spoiler` (decisão do autor, tensão registrada em `01-briefing.md`),
`tags`, `status: rascunho` — preenchido e coerente.

## 7. Manchete

Título temático mantido ("Quando os Modelos se Rebelam") — não testada a fórmula
conceito+quebra+prática porque o título atual já carrega o gancho central (a "rebelião" é a
imagem que a capa também usa) e nenhum título testado com a fórmula superou isso em clareza.
Não bloqueante.

## 8. Achado enterrado

Nenhum sinalizado pela crítica estrutural — o achado central (Derman: teoria x modelo x
intuição) está na abertura da seção 1, não enterrado.

## 9. Inventário visual completo

- `capa.md` — presente, uma capa (alavanca sobre traçado rompido).
- `ilu-01` — presente em `ilustracoes.md`, bloco completo com prompt Nano Banana Pro.
- `graf-01` — presente em `graficos.md`, código testado e executado (`figuras/graf-01.svg`
  e `.png` gerados).
- `diag-01` — presente em `diagramas.md`, código testado e executado (`figuras/diag-01.svg`
  e `.png` gerados).
- `infograficos.md` — não existe, corretamente: nenhum ponto do texto exige leitura conjunta
  de duas peças (ver `02-estrutura.md`, "O que fica de fora").
- Todo prompt em `capa.md`/`ilustracoes.md` declara "Nano Banana Pro" no cabeçalho — ✅.

## 10. Paleta fora dos tokens — checagem mecânica

`grep -oE '#[0-9A-Fa-f]{6}'` em `capa.md` e `ilustracoes.md`: `#0A3320`, `#2D9E67`,
`#4A5568`, `#CDF163`, `#F7F7F5`, `#1B6A45` — todos presentes em
`brand/tokens/skill_test.tokens.json`. Nenhum hex fora da lista.

## 11. Gate de Tufte — checagem mecânica

`graficos.md`: `rangemode="tozero"` presente nos dois painéis de `graf-01`. Nenhuma menção a
`3d`, `shadow` (fora de `shadow.syntaxis*`), textura ou moldura em `graficos.md` nem
`diagramas.md` (`grep` confirma). `diag-01` não é gráfico de eixo quantitativo (eixos
`visible=False`, é diagrama de fluxo) — gate de eixo-zero não se aplica.

## Resumo do que mudou desde a etapa 7

- Abertura reescrita (mais curta, gancho mais rápido) + `[VERIFICAR]` inserido na citação de
  Kempthorne.
- Seção 1: uma frase-ponte adicionada ao final.
- Seção 3: definição de Black–Scholes revisada (regência), cotações do dólar trocadas para
  precisão maior (R$3,1283→R$3,3805), Nota brasileira comprimida e com `[VERIFICAR]` no
  volume total.
- Seção 4: LTCM nocional corrigido para US$1,3 tri (fonte primária), datação de "US$125bi em
  ativos" corrigida para agosto/1998, alavancagem ajustada para "mais de 26 vezes" em duas
  ocorrências (corpo e fechamento).
- Seção 5: London Whale já com "44%"/"US$6,2bi" desde o draft; SR 11-7 com OCC glosado.
- Fechamento: CTA reordenado para antes do aforismo final; linha do cometa revertida à forma
  de justaposição pura.
- 30 itens de marcação/norma da revisão de linha aplicados integralmente.
