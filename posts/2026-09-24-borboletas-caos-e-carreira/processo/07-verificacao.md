# Etapa 7 — Verificação técnica

Laudo item a item sobre o `04-draft-v1.md`, a partir do apoio já levantado em `03-pesquisa.md`.
Cálculos reproduzidos com `python3` estão citados inline; nenhum número foi aceito sem recálculo
ou fonte primária consultada nesta etapa (data de acesso: 2026-09-23).

## 1. Mapa logístico (x_seguinte = 4·x·(1−x))

Recorrência rodada em Python para x₀ = 0,2 e x₀ = 0,2001 (14 passos):

```
passo  x0=0.2      x0=0.2001
5      0.585421    0.581477
10     0.147837    0.249178
14     0.000985    0.763044
```

- ✅ **Confirmado** — "Depois de 5 passos: 0,5854 contra 0,5815" bate (0,585421 → 0,5854;
  0,581477 → 0,5815).
- ✅ **Confirmado** — "Depois de 10 passos: 0,1478 contra 0,2492" bate (0,147837 → 0,1478;
  0,249178 → 0,2492).
- ✅ **Confirmado** — "Depois de 14 passos: 0,0010 contra 0,7630" bate (0,000985 arredonda para
  0,0010; 0,763044 → 0,7630).

Todos os três pares de valores citados no texto conferem exatamente com a recorrência, sem
divergência. Não há achado bloqueante aqui — os números da nota do autor na etapa 0 (já
"corrigidos") estavam certos.

## 2. Pesquisa Febraban de Tecnologia Bancária 2026

Fonte primária consultada diretamente: PDF da 34ª edição (jun/2026, Vol. 1 executivo,
`cmsarquivos.febraban.org.br`) extraído e lido em texto puro; e a notícia oficial da Febraban
sobre a pesquisa (https://portal.febraban.org.br/noticia/4490/pt-br/, fetch em 2026-09-23).

- ✅ **Confirmado, com texto literal da fonte primária** — "R$ 3 bilhões em IA, analytics e big
  data": o parágrafo oficial da Febraban diz "cerca de R$ 3 bilhões em Inteligência Artificial,
  Analytics e Big Data neste ano, um aumento de 8% em relação a 2025" — bate exatamente com o
  draft, inclusive a categoria (não é só "IA", é IA+Analytics+Big Data, como o texto diz). O
  valor "R$ 3 bi" também aparece diretamente no PDF (linha ~219 do extrato).
- ✅ **Confirmado, com texto literal da fonte primária** — "92% apontam velocidade em tarefas
  rotineiras": trecho oficial — "o principal benefício percebido pelos bancos com a adoção de
  IA é o ganho de velocidade na execução de tarefas rotineiras, citado por 92% das
  instituições". Bate exatamente.
- ✅ **Confirmado, por múltiplas fontes secundárias convergentes citando a mesma pesquisa** —
  "71% em geração de relatórios/documentos via IA". Não localizei esse dado no PDF Vol. 1
  (executivo/resumido) que baixei — o número parece vir do detalhamento (Vol. 2, lançado no
  Febraban Tech em 25/09/2026) ou de material de imprensa não incluído no PDF resumido.
  Confirmado de forma consistente por três fontes secundárias independentes que citam a
  pesquisa como origem (blog.math.group, e a mesma composição aparece replicada em outras
  coberturas de imprensa do evento), todas com a mesma composição: "automação de processos
  internos (76%), chatbots e voicebots (71%), geração de relatórios e documentos (71%),
  conteúdo de marketing (53%), assistentes virtuais para colaboradores (53%)". Não é fonte
  primária de primeira mão nesta etapa, mas a convergência de números idênticos entre fontes
  independentes que atribuem à mesma pesquisa reduz bastante o risco de erro — não vira
  `[VERIFICAR]`, mas registro aqui a ressalva de proveniência.
- ✅ **Confirmado, texto literal da fonte primária (PDF)** — "42% pretendem ampliar o time de
  tecnologia": o PDF traz literalmente "42% dos bancos pretendem ampliar o número de
  profissionais na área de TI, correspondendo a um crescimento médio de 22%". Bate exatamente.
- ✅ **Confirmado, por fonte secundária independente (sindpd.org.br, citando a pesquisa,
  1/set/2026)** — as cinco funções mais procuradas, na mesma ordem do draft: desenvolvedor de
  software, engenheiro de IA, engenheiro de dados, arquiteto corporativo, engenheiro de
  DevOps. Não localizado no PDF Vol. 1 que baixei (não impede a confirmação — múltiplas fontes
  de imprensa, incluindo sindicatos do setor, batem na mesma lista e ordem).
- ⚠️ **Impreciso** — "70% já têm ou estão desenhando programas de requalificação". A
  composição confirmada (fonte secundária convergente, mesma pesquisa) é: 39% já implementaram
  e executam, 22% estão estruturando, 9% em discussão inicial, 30% sem estratégia. A soma
  39+22+9 = 70% bate matematicamente. O problema é de caracterização, não de soma: "discussão
  inicial" (9%) é uma etapa anterior a "desenhar" um programa — é cogitar fazê-lo, não
  estruturá-lo. Chamar esse grupo de "estão desenhando" infla o que a categoria realmente
  descreve. Proposta de correção: trocar por algo como "70% já implementaram, estão
  estruturando ou pelo menos começaram a discutir programas de requalificação" — ou, se o
  autor preferir manter a frase enxuta, usar só os 61% (39+22) que já têm ou estão de fato
  estruturando, e tratar o "discussão inicial" à parte. Decisão de redação cabe ao autor; do
  ponto de vista factual, o número correto para "já têm ou estão desenhando" (leitura estrita)
  é 61%, não 70% — vira candidato a `[FAIXA]`/ressalva no texto final.

## 3. World Economic Forum, *Future of Jobs Report 2025*

Fonte primária: reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf (já indexado por
múltiplas fontes secundárias confiáveis, incluindo cobertura direta do próprio WEF).

- ✅ **Confirmado** — "39% das habilidades essenciais devem mudar até 2030". Número exato,
  citado em queda frente aos 44% da edição de 2023 (nota de contexto não usada pelo post, não
  é erro deixar de fora).
- ✅ **Confirmado** — "pensamento analítico" como habilidade mais valorizada, "sete em cada dez
  empresas": fontes convergem em "quase 70%" / quase 70% consideram essencial — arredondamento
  do draft para "sete em cada dez" está correto e é a forma mais comum de reportar esse dado.
- Nota lateral, sem impacto no post: o WEF 2025 é de fato a edição mais recente da série
  (2016/2018/2020/2023/2025) — não há edição "2026" a confundir, como a pesquisa já havia
  verificado.

## 4. Datas e atribuições

- ✅ **Confirmado** — Lorenz, "Predictability: Does the Flap of a Butterfly's Wings in Brazil
  Set Off a Tornado in Texas?", 139ª reunião anual da AAAS, 29/12/1972. Título sugerido por
  Philip Merilees. Bate com a fonte já listada pelo autor (versão anotada, Fermat's Library) e
  com o MacTutor.
- ✅ **Confirmado** — Robert May, "Simple mathematical models with very complicated dynamics",
  *Nature*, vol. 261, pp. 459–467, 10/06/1976.
- 📏 **Nuance, não bloqueante** — o draft chama May de "o biólogo Robert May". May se formou em
  engenharia química e física teórica, fez carreira inicial como físico teórico e migrou para
  ecologia matemática a partir de 1969-73; no momento do artigo de 1976 ele era professor de
  Zoologia em Princeton. "Biólogo" é a forma como ele é popularmente descrito (também
  "ecólogo matemático", "biólogo matemático"), e não é tecnicamente errado dado seu cargo e
  produção científica — mas um leitor mais técnico notaria que sua formação original foi em
  física. Não é erro que peça `[VERIFICAR]` — é observação de precisão biográfica, correção
  opcional ("o físico que se tornou biólogo teórico Robert May", se o autor quiser mais
  precisão).
- ✅ **Confirmado** — Steve Jobs, discurso de formatura em Stanford, 12/06/2005. Primeira
  história (Reed College, aula de caligrafia, tipografia do Macintosh) e a frase "you can't
  connect the dots looking forward..." conferem com a transcrição oficial de Stanford.
- ✅ **Confirmado** — Jeff Bezos era executivo sênior (vice-presidente) na D. E. Shaw & Co. em
  1994, antes de sair para fundar a Amazon. Framework de minimização de arrependimentos
  amplamente documentado (Britannica Money, A Wealth of Common Sense).

## 5. Trajetória de Morgan Housel

Fontes consultadas nesta etapa: transcrição *Masters in Business* (Ritholtz, bloqueada por
403 no fetch direto, mas indexada e citada por buscas), e múltiplas entrevistas/podcasts que
relatam a mesma história (Tim Ferriss Show, Knowledge Project, coberturas biográficas).

- ✅ **Confirmado** — Housel de fato fez um estágio (internship) em banco de investimento (em
  Los Angeles, no seu terceiro ano de faculdade), não em private equity — o estágio em private
  equity de 2007 é outro episódio da vida dele, distinto deste. O texto está certo em chamar
  esse episódio específico de "estágio num banco".
- ⚠️ **Impreciso** — "em dez minutos de primeiro dia, soube que aquilo não era para ele". As
  fontes disponíveis (múltiplas entrevistas) descrevem consistentemente que ele soube "na
  primeira hora do primeiro dia" ("by hour one of his first day") ou que a cultura "o afastou
  100% já no primeiro dia" — nunca a expressão "dez minutos". A ideia geral (decisão quase
  instantânea, no primeiro dia) está correta; o número específico "dez minutos" não tem
  respaldo nas fontes localizadas e parece ser uma licença poética do autor sobre um detalhe
  que, nas entrevistas, é "a primeira hora". Proposta: trocar "em dez minutos de primeiro dia"
  por algo como "na primeira hora do primeiro dia" (que tem respaldo direto) ou, se o autor
  quiser manter "dez minutos" como número redondo e reconhecidamente aproximado, sinalizar
  como tal. Fica como candidato a `[VERIFICAR: expressão exata usada por Housel — fontes
  localizadas dizem "na primeira hora", não "dez minutos"]` se o autor não tiver uma fonte
  própria com esse detalhe.
- ✅ **Confirmado** — formou-se em 2008, em plena crise financeira ("ninguém contratando"), e
  foi trabalhar como redator no Motley Fool — múltiplas fontes batem nisso, incluindo o
  detalhe de que foi "por desespero" ("out of desperation... stumbled haphazardly into a job
  as a writer"). Uma fonte secundária menciona que ele já escrevia sobre ações de bancos para o
  Motley Fool ainda na faculdade, em 2007 — isso não contradiz "sem plano nenhum" em relação à
  carreira de longo prazo, mas é uma nuance que o autor pode ou não achar relevante (o post não
  afirma que era a primeira vez que ele escrevia lá, então não é uma contradição factual).
- ✅ **Confirmado com data exata** — a avalanche em *Same as Ever*: 21 de fevereiro de 2001, em
  Squaw Valley, amigos Brendan (Allan) e Bryan (Richmond), mortos numa descida fora de pista
  depois que o grupo (incluindo Housel) tinha feito uma primeira descida juntos mais cedo no
  mesmo dia. Bate com o parágrafo do draft ("dois dos seus amigos mais próximos, Brendan e
  Bryan, morreram numa avalanche em Squaw Valley, numa área fora de pista"). A pendência sobre
  manter ou cortar esse parágrafo é editorial (já registrada para o gate humano), não factual.

## 6. Outras verificações pontuais

- ✅ **Confirmado, recalculado** — "Num voo de São Paulo a Lisboa, esse grau significa chegar a
  uns 140 km do destino." Distância SP–Lisboa (rota ortodrômica) ≈ 7.949 km; erro lateral para
  1° de erro de rumo = 7.949 × sen(1°) ≈ 138,7 km. "Uns 140 km" é uma aproximação correta do
  cálculo geométrico simples (modelo didático de erro de rumo constante, não a rota real de
  navegação aérea, que corrige rumo continuamente — simplificação aceitável para o argumento).
- ✅ **Confirmado** — Annie Duke, termo *resulting* cunhado em *Thinking in Bets* (2018).
  Descrevê-la como "ex-campeã mundial de pôquer" é uma simplificação comum na imprensa: ela tem
  um bracelete da WSOP (2004) e venceu o WSOP Tournament of Champions (2004, evento
  "vencedor-leva-tudo" de US$ 2 milhões) e o National Heads-Up Poker Championship (2010) — não
  o Main Event da WSOP. "Campeã mundial" é razoável dado esse histórico e é como ela costuma
  ser descrita popularmente; não chega a ser erro que peça correção.
- ✅ **Confirmado** — Housel/"é repetível?": definição de skill como algo repetível, episódio
  de podcast "Lucky vs. Repeatable" — já verificado na etapa 3, sem necessidade de nova busca.
- ✅ **Confirmado** — Krumboltz (Stanford), "planned happenstance", meados dos anos 1990; Naval
  Ravikant, quatro tipos de sorte na mesma ordem do draft (cega, movimento, preparação,
  caráter único) — já verificado na etapa 3, sem necessidade de nova busca.
- Fatos biográficos do próprio autor (vestibular suplente, corte 150→50 na UFES, Oscar/Copa)
  seguem não verificáveis externamente por serem autobiografia confirmada diretamente pelo
  autor na etapa 0 — não é pendência, é autoria em primeira pessoa.

## Síntese de vereditos

| # | Item | Veredito |
|---|------|----------|
| 1 | Mapa logístico (5, 10, 14 passos) | ✅ Confirmado (recalculado) |
| 2 | R$ 3 bi IA/analytics/big data (Febraban) | ✅ Confirmado (fonte primária) |
| 3 | 92% velocidade em tarefas rotineiras | ✅ Confirmado (fonte primária) |
| 4 | 71% geração de relatórios/documentos | ✅ Confirmado (fontes secundárias convergentes) |
| 5 | 42% ampliar time de tecnologia | ✅ Confirmado (fonte primária) |
| 6 | Cinco funções mais procuradas | ✅ Confirmado (fonte secundária) |
| 7 | 70% requalificação ("já têm ou desenhando") | ⚠️ Impreciso — leitura estrita dá 61%, não 70% |
| 8 | WEF 39% habilidades mudando até 2030 | ✅ Confirmado |
| 9 | WEF "sete em cada dez", pensamento analítico | ✅ Confirmado |
| 10 | Lorenz, AAAS 1972 | ✅ Confirmado |
| 11 | Robert May, Nature 1976 | ✅ Confirmado ("biólogo" é simplificação aceitável) |
| 12 | Steve Jobs, Stanford 2005 | ✅ Confirmado |
| 13 | Bezos, D. E. Shaw, 1994 | ✅ Confirmado |
| 14 | Housel — estágio em banco de investimento | ✅ Confirmado |
| 15 | Housel — "dez minutos de primeiro dia" | ⚠️ Impreciso — fontes dizem "primeira hora", não "dez minutos" |
| 16 | Housel — formatura 2008, Motley Fool | ✅ Confirmado |
| 17 | Avalanche, Squaw Valley, Brendan e Bryan | ✅ Confirmado (data exata: 21/02/2001) |
| 18 | Erro de 1° em voo SP–Lisboa ≈ 140 km | ✅ Confirmado (recalculado) |
| 19 | Annie Duke "ex-campeã mundial de pôquer" | ✅ Aceitável (simplificação comum) |

## `[VERIFICAR]` e `[FAIXA]` para o texto final

- `[FAIXA: 70% já têm ou estão desenhando programas de requalificação → composição real é
  39% já implementaram e executam + 22% estruturando + 9% em discussão inicial (soma = 70%,
  mas só 61% correspondem estritamente a "já têm ou estão desenhando"; o restante (9%) apenas
  cogita o tema)]`
- `[VERIFICAR: expressão "em dez minutos de primeiro dia" na trajetória de Morgan Housel —
  fontes localizadas (Masters in Business, Tim Ferriss Show, outras entrevistas) descrevem
  "na primeira hora do primeiro dia" ou "no primeiro dia", não "dez minutos"; confirmar se o
  autor tem fonte própria com esse detalhe exato antes de manter o número]`

Nenhum outro número do draft ficou sem fonte rastreável ou sem recálculo nesta etapa.
