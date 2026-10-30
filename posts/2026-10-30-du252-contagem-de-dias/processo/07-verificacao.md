# Etapa 7 — Verificação técnica

Laudo do agente `verificador-tecnico`, gravado pelo pipeline principal. Post
`2026-10-30-du252-contagem-de-dias`, linha Notas de um Professor. Verificado: corpo de
`processo/04-draft-v2.md` (l. 35–291; números de linha desse arquivo) e o conteúdo das glosas e
reformulações aprovadas de `processo/06-revisao.md`. Fontes acessadas em 30/10/2026.

**Ambiente:** python3 3.14.4, numpy 2.5.2, pandas 3.0.5, `bizdays` 1.0.19 (diretório isolado).
PDFs que a leitura web não decodificava (CE 006/2024, CE 013/2024, OC 207/2023 e outros) foram
baixados para o scratchpad da sessão e lidos com `pdftotext`. CMN 4.880 e Res. BCB 46 lidas pela
API JSON do BCB (`/api/conteudo/app/normativos/exibenormativo`), a que a página em JS consome.

**Registro de cálculo completo** (blocos, script, saída):
`_revisoes/2026-10-30_2026-10-30-du252-contagem-de-dias_calculo.md`.

## Resumo

- **1 bloqueante matemático (O-1):** tabela do CDB, "+ R$ 218,19" → a subtração dos resgates
  mostrados dá R$ 218,18.
- **2 outras correções obrigatórias de fato:** O-2 (M-5 da l. 77) e O-3 (causalidade do CE
  013/2024 na nota 7).
- **15 ajustes opcionais de precisão** (P-1 a P-15).
- **Os cinco blocos de código:** todas as saídas comentadas batem (43; 248/249; os dois
  `enddate`; `40 101815.15`; 40).
- **Recálculos:** todos batem, exceto O-1 (LTN, fatores, resgates, taxas equivalentes, R$ 137,
  R$ 96,9 mil e R$ 218,2 mil, 22 × 20, R$ 90, série 2001–2030 com 3 anos em 252, média 251,0,
  11,95%, os 249 da nota 2).
- **Dois lados do balcão:** não bloqueante; observação à etapa 5.
- **Regra de referências:** cumprida.
- **Marcadores:** 1 `[VERIFICAR]`, 0 `[FAIXA]`.

---

## Correções obrigatórias

### O-1. BLOQUEANTE — tabela do CDB, l. 129, "Diferença" da linha DC/360 linear

- 102.033,33 − 101.815,15 = **218,18**. O texto traz 218,19 (diferença exata 218,1882
  arredondada). As outras linhas batem pelos dois métodos (96,89 e 123,70); a tabela fica
  internamente inconsistente por R$ 0,01, que é a conta que o leitor refaz.
- **Correção:** "+ R$ 218,19" → "+ R$ 218,18". A prosa ("R$ 218"; "R$ 218,2 mil") não muda. O
  graf-02 usa 218,18.

### O-2. M-5, l. 77 — DU/252 composto é padrão, não regra, para CDB

- Caderno de Fórmulas B3 de CDB/DI/LF (28/06/2021), §5.4.1, aceita quatro critérios, todos
  compostos: "252 – número de dias úteis…"; "252 – Número de meses … x 21"; "360 – Número de
  dias corridos…" ou "365 – Número de dias corridos…" (p. 40, exponencial); "360/365 – … meses
  x 30". Debêntures: critério próprio não conferido; nenhuma afirmação além de "padrão".
- **Original (v2):** "Na renda fixa brasileira em reais (Selic, DI, títulos públicos, CDB,
  debêntures, futuro de DI), a combinação é **régua DU/252 com motor composto**:"
- **Corrigido** (já com as glosas `norma` da etapa 6, sem negrito): "Na renda fixa brasileira
  em reais, a combinação padrão é régua DU/252 com motor composto. É a da Selic (a taxa básica
  de juros), do DI (a taxa dos empréstimos entre bancos), dos títulos públicos e do futuro de
  DI, e é o padrão também no CDB (Certificado de Depósito Bancário) e nas debêntures. Padrão,
  não regra: a B3 aceita registrar CDB em dias corridos, base 360 ou 365, e é o emissor quem
  escolhe a régua no registro. A fórmula do padrão é:"
- A oração "é o emissor quem escolhe a régua no registro" é opcional (apoio: CE 013/2024, "valor
  de emissão … valor de resgate, ambos informados pelo Emissor"; Caderno, "Sugere-se sempre
  verificar o critério utilizado nas características do instrumento") e torna explícito o lado
  de quem emite.
- Efeito: as linhas DC/365 e DC/360 compostas da tabela viram alternativas reais de registro.
  A DC/360 linear não é critério de CDB na B3; é a leitura do mercado monetário internacional.

### O-3. Nota 7, l. 161 — CE 013/2024-VPC com a causalidade invertida

- **CE 006/2024-VPC (08/02/2024), item 1:** instrumentos "em base de 252 dias … serão
  impactados pelo feriado"; "base de 360/365 dias … não sofrerão impactos"; "A B3 não fará
  nenhuma alteração automática das características dos instrumentos financeiros".
- **CE 013/2024-VPC (04/04/2024):** a B3 "recalculará, no dia 19/04/2024 … a taxa de juros de
  [CDB] e [DI] emitidos, exclusivamente, com a forma de pagamento 'Registro Simplificado
  Prefixado Final'", para o "reenquadramento dos instrumentos de acordo com o novo calendário";
  "a taxa apurada é informativa, não impactando o valor financeiro a ser liquidado no
  vencimento, que permanece sendo aquele presente nas características do ativo"; é a "taxa …
  equivalente para atualizar o valor de emissão até o valor de resgate, ambos informados pelo
  Emissor"; "os demais instrumentos … em base 252 dias, não serão recalculados".
- **OC 207/2023-PRE (07/12/2023), item 1:** "o ajuste diário a ser liquidado na janela de
  liquidação multilateral de D+2 terá o impacto financeiro da mudança na contagem de dias úteis
  até vencimento".
- O resgate não mudou porque é o dado registrado; a B3 não recalculou "para que o resgate não
  mudasse". O dinheiro mexeu nos outros papéis em base 252, que não foram recalculados. A
  primeira frase ("todo contrato em dias úteis … um dia útil a menos até o vencimento") está
  correta e fica.
- **Original (versão da etapa 6):** "A B3 recalculou a taxa dos CDBs prefixados registrados por
  valor final (aqueles em que o registro fixa o valor de resgate), para que o resgate não
  mudasse, e o ajuste dos futuros de juros absorveu o impacto da nova contagem."
- **Corrigido:** "Na maioria dos papéis em base 252, nada foi recalculado: eles simplesmente
  passaram a render um dia a menos. A exceção foram os CDBs prefixados registrados por valor
  final (em que o emissor registra o valor de emissão e o de resgate, e a taxa é só
  informativa): ali o resgate ficou como estava, e a B3 recalculou a taxa equivalente. Nos
  futuros de juros, o impacto da nova contagem passou de uma vez pelo ajuste diário."
- Substitui a glosa `norma` da etapa 6 para "registrados por valor final". Opcional: "CDBs (e
  DIs)".

---

## Item por item

### Abertura e "12% ao ano de quê?" (l. 41–60)
- ✅ l. 41, LTN 12% → 11,85%: 1,12^(249/252) − 1 = 11,8490%. Ver P-1, P-2.
- ✅ l. 41, vencimento 01/01/2027: "Tesouro Prefixado; 01/01/2027" na série oficial
  PrecoTaxaTesouroDireto (Tesouro Transparente).
- ✅ l. 45, "2026 tem 249 dias úteis": ANBIMA 2026, 13 feriados (15/11 no domingo).
- ✅ l. 45, "12% a cada 252 dias úteis": ANBIMA, *Metodologias* (05/05/2021), p. 35, LTN:
  PU = VN/(1+Taxa/100)^(du/252); Res. BCB nº 46/2020, art. 2º: Selic "considerando a convenção
  de 252 … dias úteis" (vigente pela API do BCB).

### A régua e o motor (l. 64–87)
- ✅ l. 66–68, as três réguas: treinamento DI da B3 ("252 dias úteis…"; "internacional … 360
  dias corridos"); slides baseados em Hull, cap. 6 ("T-bills and Money Market Instruments:
  Actual/360; Corporate and Municipal Bonds: 30/360").
- ✅ Glosa da etapa 6 "Actual/360 (no Brasil, DC/360, de dias corridos)": tabela do treinamento
  B3, "360 — Aproximado: 30/360; Correto: dc/360".
- ⚠️ l. 77: O-2.
- ✅ l. 79, 81, 83, Fator, PU, R$ 1.000, 100.000 pontos: ANBIMA p. 35 (VN = R$ 1.000); OC
  055/2024-PRE, Anexo I (DI1), "PO = 100.000/(1+i/100)^(n/252)".
- ✅ l. 85, liquidação (inclusive) e vencimento (exclusive): Tesouro, *Methodology…* ("bd = number
  of business days between settlement date (inclusive) and maturity date (exclusive)"); OC 055
  ("entre a data da operação, inclusive, e a data de vencimento do contrato, exclusive").
  Divergência 10 da pesquisa: nenhuma mudança, o texto não atribui a frase à ANBIMA.
- ✅ l. 87 (nota 2), "é paga no dia útil seguinte, 4 de janeiro": dados oficiais de vencimentos do
  Tesouro Direto (LTN 01/01/2023 resgatada em 02/01/2023; 01/01/2025 em 02/01/2025; 01/01/2026
  em 02/01/2026); `following` = 04/01/2027. Divergência 7 resolvida.
- ✅ l. 87 (nota 2), "os mesmos 249": [02/01/2026, 01/01/2027) = 249 e [02/01/2026, 04/01/2027) =
  249. Prova independente: PU Base (D0) oficial de 02/01/2026 (880,31 a 13,77%) implica du =
  249,02.

### Por que o relógio para no sábado (l. 93–109)
- ✅ l. 93, DI de um dia útil: B3, *Metodologia de Apuração da Taxa DI* (DI "pactuad[o] por um dia
  útil", "Extra-grupo", média ponderada pelo volume). Ver P-11.
- ✅ l. 93, uma "diária" de sexta a domingo: OC 055, fator (1+DI)^(1/252) por dia útil; "datas
  especiais" de 1 e 2 overs na metodologia B3.
- ✅ l. 99, Selic ao mês até 1997 / hiperinflação: Garcia, p. 1 ("tornaram-se mensalizadas no
  Brasil devido à megainflação…"); ementa da Circular ("Altera a forma de expressão").
- ✅ l. 99, Circular BCB nº 2.761: 18/06/1997; art. 1º Selic "sob a forma anual", expoente 252;
  art. 2º "252 … dias úteis para o ano"; art. 4º "surtindo efeito a partir de 01.01.98". Ver P-3.
- ✅ l. 99, "12 meses de 21 dias úteis": treinamento B3, literal.
- ✅ l. 101, Garcia: "Efeitos da anualização da taxa Selic", 30/Junho/97, Depto. de
  Economia–PUC-Rio; p. 5, item b, literal: "1998 tem 249 dias úteis, enquanto a fórmula do BC usa
  252 dias úteis". "Quase três décadas" confere.
- ✅ l. 105 (nota 4), só 2004, 2025, 2030 com 252 (20 abaixo, 7 acima, faixa 248–254). 2027–2030
  são projeção pelo calendário vigente; o rodapé do graf-01 deve dizer isso.
- ✅ l. 107, 11,85% e 12,05%; 2024 = 253 (11,8490% e 12,0504%).
- ✅ l. 109 (nota 5), média 251,0 e 11,95% (11,9496%); média geométrica dos 30 rendimentos
  11,9496%, aritmética 11,9497%. "Em média" e o ★ "Nesse ritmo" corretos.
- ⚠️ Deck, "quase nunca": P-8.

### Quanto custa a régua errada (l. 113–142)
- ✅ l. 117–120: 01/10/2026 quinta, 01/12/2026 terça; 61 dias corridos; 12/10 e 02/11 segunda,
  20/11 sexta; 40 DU.
- ✅ Tabela, fatores com 8 casas (1,01815145; 1,01912036; 1,01938848; 1,02033333), resgates
  (101.815,15; 101.912,04; 101.938,85; 102.033,33), diferenças 96,89 e 123,70.
- ❌ Tabela, 218,19: O-1.
- ✅ l. 131, escala: "entre R$ 97 e R$ 218"; "R$ 96,9 mil e R$ 218,2 mil" (96.890,83 e
  218.188,23).
- ✅ l. 133, R$ 1.815,15 de juros.
- ✅ l. 135–138, taxas equivalentes 11,3644%, 11,2003%, 10,7123% → 11,36%, 11,20%, 10,71%.
- ✅ l. 142, Nota de rigor: ANBIMA p. 32, LTN (taxa T-4/I-4, exponencial T-14, PU T-6); Caderno
  B3 com "Critérios de Precisão" por emissor e ativo.
- ✅ Aderência do CDB a 12% pré em out/2026: Selic meta 13,75% (SGS 432); LTN jan/27 a 13,33% em
  01/10/2026. CDB pré de 2 meses a 12% fica abaixo do DI, mas dentro do varejo bancário:
  simplificação aceitável.

### ANBIMA ou B3? (l. 146–166)
- ✅ l. 150, CMN 4.880, art. 6º: "sábados, domingos e feriados de âmbito nacional, bem como: I - a
  segunda-feira e a terça-feira de Carnaval; e II - o dia dedicado a Corpus Christi". Texto
  oficial pela API do BCB (mesmos parâmetros do link): "Revogado: false", vigência desde
  01/03/2021. Divergências 12 e 2 resolvidas. Feriados estaduais e municipais fora.
- ✅ Glosa da etapa 6 "Resolução nº 4.880/2020 do Conselho Monetário Nacional (CMN)".
- ✅ l. 155, sem pregão em 24/12 e 31/12: OC 041/2026-VNC (errata, 30/06/2026).
- ✅ l. 155, dias úteis ANBIMA com DI apurado: nenhum dos dois no `ANBIMA.cal` 2026; SGS 12 (CDI)
  com valor em 24/12/2025 e 31/12/2025 (0,055131% a.d.) e em 24/12/2024 e 31/12/2024.
- ⚠️ l. 155, "as agências não abrem ao público": P-4.
- ✅ l. 157, OC 055/2024-PRE, literal: "'Dia Útil' … de acordo com o significado atribuído na
  Resolução 4.880"; "'Dia de Sessão de Negociação', quaisquer dos dias em que houver sessão de
  negociação na B3"; "Quando houver mais de um Dia Útil … o fator de correção representará a
  acumulação de todas as Taxas DI". Ver P-15.
- ✅ Glosa "ajuste (o acerto diário de ganhos e perdas)": OC 055, item 2 ("pagamento dos débitos
  e recebimento dos ganhos").
- ✅ Glosa "pregão (a sessão de negociação da B3)".
- ✅ l. 159, dezembro 22 × 20, ~R$ 90 (89,98) e R$ 90 mil (89.983,86).
- ✅ l. 161, feriados de SP até 2021: OC 003/2020-VOP, Quadro 2 (09/07 e 20/11/2020) e item 4.1
  ("Não haverá negociação nos mercados de renda variável, renda fixa privada e de derivativos
  listados"); o balcão Cetip funcionava. Ver P-5.
- ✅ l. 161, B3 aberta nos feriados paulistas desde 2022: CE 109/2021-VNC; OC 041/2026 (09/07/2026
  "funcionamento normal").
- ✅ l. 161, Lei nº 14.759/2023, "desde 2024": Planalto, vigência na publicação, DOU 22/12/2023.
- ✅ l. 161 (nota 7), "um dia útil a menos até o vencimento": CE 006 ("01 dia a menos de
  accrual") e OC 207.
- ⚠️ l. 161 (nota 7), recálculo da taxa dos CDBs: O-3.
- ✅ l. 161 (nota 7), ajuste dos futuros absorveu o impacto: OC 207, item 1.

### Python (l. 170–251)
- ✅ Bloco 1, `# 43` (no REPL do numpy 2, `np.int64(43)`; ver P-14).
- ⚠️ l. 172, `bdate_range`: P-7. Executado: sem feriados, 43; com feriados e frequência padrão,
  `ValueError: a custom frequency string is required when holidays or weekmask are passed, got
  frequency B`; com `freq="C"`, 40.
- ✅ l. 181, R$ 137: resgate com 43 DU = 101.952,60, 137,45 acima.
- ✅ Bloco 2, `# 248` e `# 249`; `following("2027-01-01")` = 2027-01-04.
- ✅ l. 196, "exclui a data inicial e inclui a final": `bizdays("2013-01-02","2013-01-05")` = 2
  (05/01/2013 sábado). O mecanismo descrito confere.
- ✅ l. 200 (nota 8): 1.0.19 continua a mais recente no PyPI (04/01/2026; 1.0.18 em 03/01/2026);
  B3 termina em 31/12/2026 e levanta `DateOutOfRange` ("Given date out of calendar range") em
  `bizdays` e `isbizday`; ANBIMA até 2099-12-25. "Dois meses de vida" confere.
- ✅ Bloco 3, os dois `enddate`.
- ✅ l. 211, autoria e conteúdo (PyPI: autor "wilsonfreitas"; `.cal` no pacote).
- ✅ Bloco 4, `# 40 101815.15`.
- ✅ Bloco 5, `# 40`; `feriados_2026` idêntica à ANBIMA 2026 (13 datas); comentário "(Resolução
  CMN 4.880/2020 + Lei 14.759/2023)" aceitável como simplificação.
- ✅ l. 251, `inclusive="left"`.

### Outros relógios (l. 257–261)
- ✅ l. 257, convenções dos EUA e acúmulo linear: slides baseados em Hull, cap. 6 ("Treasury Bonds:
  Actual/Actual"; "8% Actual/Actual in period"; "$4 x (31/184)"). Glosas da etapa 6
  (Actual/Actual = "dias corridos divididos pelos dias corridos do período de juros";
  "*Treasuries* (os títulos públicos americanos)") ✅.
- ⚠️ l. 257, tabela do treinamento B3 também tem base 365: P-6.
- ✅ l. 259, DDI ("Taxa de juro, expressa em percentual ao ano, linear, base 360 dias corridos")
  e FRC ("linear, base 360 dias corridos"). Ver P-9.
- ✅ l. 261 (nota 8), na renda fixa a data vai para o dia útil seguinte: resgates do Tesouro; CE 006
  ("liquidação postergada para o próximo dia útil").
- ✅ l. 261, opções antecipadas para 19/11/2026: calendário de vencimentos B3 (out 16/10 e dez 18/12
  na terceira sexta; nov, terceira sexta é 20/11); especificação da opção de compra sobre ação
  (Anexo do OC 057/2024-PRE): "Caso esse dia não seja Dia de Sessão de Negociação, o vencimento
  ocorrerá na data imediatamente anterior em que houver sessão de negociação". Esse ofício traz
  "Revogado pelo Ofício Circular 107/2024-PRE"; o vigente não foi aberto, mas o calendário de 2026
  aplica a regra. Divergência 11 resolvida para as mensais.

### Fecho (l. 276)
- ✅ FIDC prometido no texto das debêntures: `_arquivo/drafts/2026-10-15_Renda_Fixa_Condições_Variáveis.md`
  l. 281 ("No texto do CRA, prometi o FIDC. Ele vem no próximo"); `01-briefing.md` l. 134–135.

### Glosas e reformulações da etapa 6

| Item | Veredito |
|---|---|
| cupom cambial = "o juro em dólar" | ⚠️ opcional, P-9 |
| Actual/Actual = "dias corridos ÷ dias corridos do período de juros" | ✅ (Hull, "in period") |
| "ajuste" = acerto diário de ganhos e perdas | ✅ (OC 055, item 2) |
| "registrados por valor final (… fixa o valor de resgate)" | ⚠️ substituída em O-3 |
| DC/360 como nome brasileiro do Actual/360 | ✅ (treinamento B3) |
| ANBIMA publica a metodologia e o calendário | ✅ (05/05/2021; feriados 2001–2099). Nome: P-13 |
| PyPI = "o repositório de pacotes do Python" | ✅ |
| Selic = "a taxa básica de juros" | ✅ (Tesouro Transparente: "taxa de juros básica da economia") |
| "Nesse ritmo" (l. 109) | ✅ |
| "taxa média" do DI (l. 93) | ✅, P-11 |
| "fórmulas oficiais" | ⚠️, P-12a |
| título do Garcia | falta, P-12b |
| Atlas × GEN Atlas | ✅ as duas, P-12c |
| `bdate_range`, freq 'B' com holidays | dá erro, P-7 |
| LTN = "o título público prefixado" | ⚠️ opcional, P-10 |
| CDI / *over* | ✅ |
| NTN-F, NTN-B, LFT = títulos públicos federais | ✅ |

---

## Opcionais (precisão; o autor decide)

- **P-1. l. 41, "comprada" × "liquidada".** O du conta da liquidação; no Tesouro Direto a compra
  liquida em D+1 (OC 031/2017-DO; metadado "PU Compra Manhã … com liquidação para o próximo dia
  útil (D+1)"). Os PUs oficiais de compra da LTN jan/27 implicam du − 1 nas 207 datas de 2026.
  Quem compra no TD em 02/01/2026 liquida em 05/01: 248 DU e 11,80%. **Proposta:** "Uma LTN
  comprada a 12% ao ano no primeiro dia útil de 2026" → "Uma LTN comprada a 12% ao ano, com
  liquidação no primeiro dia útil de 2026,".
- **P-2. l. 41, aderência.** Em 02/01/2026 a LTN jan/27 estava a 13,65% (compra), Selic 15,00%, DI
  14,90% a.a. Os 12% são hipotéticos e aceitáveis, mas a data precisa pode fazê-los parecer taxa
  real. **Proposta:** "comprada a, digamos, 12% ao ano" e, se quiser, "11,85% brutos".
- **P-3. l. 99.** "a partir de 1º de janeiro de 1998" é o art. 4º literal; a Circular 2.780/1997
  fixou "a partir de 02.01.98, inclusive". Manter, ou "a partir de 1998".
- **P-4. l. 155.** CMN 4.880, art. 3º: "Não haverá atendimento presencial no último dia útil do
  ano" (autoatendimento não suspenso). **Proposta:** "as agências não abrem ao público" → "não há
  atendimento presencial nas agências".
- **P-5. l. 161.** Em 2020 balcão e câmbio funcionavam. **Proposta:** "até 2021, a B3 fechava nos
  feriados de São Paulo" → "até 2021, a B3 não tinha pregão nos feriados de São Paulo".
- **P-6. l. 257.** **Proposta:** "base 360, com contagem aproximada (30/360) ou correta (dc/360),
  contra base 252 (du/252)" → "base 360 (aproximada 30/360 ou correta dc/360) e base 365 (30/365
  ou dc/365), contra base 252 (du/252)". Reforça O-2.
- **P-7. l. 172 (a mais recomendada).** A frase sugere que passar a lista resolve, e no
  `bdate_range` não resolve. **Proposta:** "Sem a lista de feriados, `numpy.busday_count` e
  `pandas.bdate_range` só tiram sábado e domingo. E, no `bdate_range`, passar a lista não basta:
  com a frequência padrão (`"B"`) ele recusa os feriados com erro, e é preciso pedir `freq="C"`."
- **P-8. Deck, "quase nunca".** 2001–2030: 3 de 30. Calendário vigente (com 20/11), 2024–2098: 20
  de 75 (26,7%, ~1 em 4). O texto ancora na janela 2001–2030; manter é defensável. Alternativa:
  "raramente". Vai ao gate.
- **P-9. Glosa do cupom cambial.** A B3 define o cupom como "o rendimento em dólares para
  estrangeiros que assumem o risco de investir no Brasil"; o FRC "não é considerado contrato para
  fins de posição em aberto". **Proposta:** "(o juro em dólar, negociado nos contratos DDI e
  FRC)" → "(o juro em dólar de uma aplicação no Brasil, negociado no DDI e no FRC)".
- **P-10. Glosa da LTN.** A NTN-F também é prefixada. **Proposta:** "o título público prefixado"
  → "o título público prefixado sem cupom".
- **P-11. l. 93, ★ "taxa média".** Correto (a B3 chama o DI de "taxa média de depósitos
  interfinanceiros de um dia"). Precisão opcional: "a média, ponderada pelo volume, das taxas…".
- **P-12. Bibliografia.** (a) ANBIMA: "As fórmulas oficiais" → "As fórmulas de referência do
  mercado" (associação privada). (b) Garcia: acrescentar o título, *Efeitos da anualização da
  taxa Selic* (Depto. de Economia–PUC-Rio, 30/06/1997). (c) Tosi: "Atlas" correto (ISBN
  978-85-224-9892-5, prefixo da Editora Atlas; varejo lista "GEN Atlas"); 4ª ed. 2015, 368 p.,
  confirmada; sinopse cita "CDI, Selic, Cetip, taxa over". (d) Hull: ver `[VERIFICAR]`; 11ª ed.
  Pearson saiu em 22/02/2021 (copyright 2022), "2021" ok.
- **P-13. Glosa da ANBIMA.** Nome oficial: "Associação Brasileira das Entidades dos Mercados
  Financeiro e de Capitais". **Proposta:** "a associação das instituições do mercado financeiro"
  → "a associação das entidades dos mercados financeiro e de capitais".
- **P-14. Bloco 1.** No REPL, `np.int64(43)`. Sem mudança (convenção de comentário do texto).
- **P-15. Link da OC 055/2024-PRE.** Sem carimbo de revogação; o irmão OC 057/2024-PRE tem
  ("Revogado pelo OC 107/2024-PRE"). Vigência atual não confirmada; definições citadas são as
  usuais dos contratos B3. Sem mudança.

### Divergências 2–12 da pesquisa

| # | Proposta |
|---|---|
| 2 | Nenhuma: execução confirma 2099-12-25 (a documentação do pacote, 2078, está desatualizada) |
| 3 | P-3 |
| 4 | Nenhuma (✅ literal) |
| 5 | P-8 |
| 6 | O-2 |
| 7 | Resolvida (✅ dados oficiais de resgate) |
| 8 | P-6 |
| 9 | P-4 |
| 10 | Nenhuma no texto; âncora explícita: Tesouro e OC 055 |
| 11 | Resolvida (✅ especificação mensal + calendário) |
| 12 | Resolvida (✅ API do BCB) |

---

## Verificações da linha Notas de um Professor

- **Fórmula, simbólica e numérica:** Fator, PU, linear e composto corretos; numericamente, só O-1
  diverge. Prova extra: os PUs do Tesouro Direto confirmam liquidação (inclusive) / vencimento
  (exclusive) em DU/252 (02/01/2026: PU D0 implica du = 249,02; PU D+1, 248,01).
- **Aderência à realidade brasileira:** exemplos plausíveis (CDB de R$ 100 mil, carteira de R$ 100
  mi, 2 meses); 12% abaixo do mercado na data (P-2), mas não irreal.
- **Dois lados do balcão: não bloqueante.** O protagonista é quem calcula no meio (mesa, *back
  office*, desenvolvedor), e quem define a régua aparece (BCB em 1997, B3, ANBIMA), o que atende
  ao §4.2 para post de conceito. O emissor só aparece implícito ("o contratado"). Observação à
  etapa 5: O-2 ("é o emissor quem escolhe a régua no registro") e O-3 ("o emissor registra o valor
  de emissão e o de resgate") tornam o lado de quem emite explícito sem mudar a estrutura.
- **Regra de referências (§5.7): cumpre.** 4 itens, 2 livros (Hull, Tosi); nenhuma lei na
  bibliografia.
- **Para a etapa 8:** graf-02 usa 218,18; graf-01 com rodapé "cálculo próprio a partir do
  `ANBIMA.cal` (`bizdays` 1.0.19); 2027–2030 projetados pelo calendário vigente".

---

## Lista consolidada para o texto final

**`[VERIFICAR: ...]`**
1. Bibliografia, Hull: `[VERIFICAR: título da seção do cap. 6 na 11ª ed. ("Day Count and
   Quotation Conventions") — a Pearson confirma só o capítulo ("Interest rate futures"); o título
   da seção 6.1 foi confirmado na 9ª ed.]`

**`[FAIXA: ...]`**: nenhum.

**Correções obrigatórias** (entram na consolidação): O-1 (bloqueante), O-2, O-3.

---

## Fontes primárias (acesso em 30/10/2026)

- **BCB:** Circular 2.761/1997 (https://www.bcb.gov.br/pre/normativos/circ/1997/pdf/circ_2761_v1_o.pdf);
  Circular 2.780/1997 (https://www.bcb.gov.br/pre/normativos/circ/1997/pdf/circ_2780_v1_o.pdf);
  CMN 4.880 via API (https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20CMN&p2=4880);
  Res. BCB 46 (mesmo endpoint, p1=Resolução BCB, p2=46); SGS 12
  (https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json&dataInicial=24/12/2025&dataFinal=02/01/2026);
  SGS 432.
- **Planalto:** Lei 14.759/2023 (https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/L14759.htm).
- **B3:** CE 006/2024-VPC (https://www.b3.com.br/data/files/34/E1/2E/AD/D0A8D8103152D4C8AC094EA8/CE%20006-2024-VPC%20Feriado%2020_nov_vfinal.pdf);
  CE 013/2024-VPC (https://www.b3.com.br/data/files/AC/52/46/F9/E6AAE8100E866AE8AC094EA8/CE%20013-2024-VPC%20Feriado%2020Nov_Calculo%20das%20taxas_v02.pdf);
  OC 207/2023-PRE (https://www.b3.com.br/data/files/75/C1/52/35/F854C810719CE3C8DC0D8AA8/OC%20207-2023-PRE%20Procedimentos%20para%20Tratamento%20de%20Novo%20Feriado%20Nacional%20no%20Dia%2020%20de%20Novembro%20(PT).pdf);
  OC 055/2024-PRE (link do texto); OC 057/2024-PRE
  (https://www.b3.com.br/data/files/EA/A1/15/CB/C88EE810C54843E8DC0D8AA8/OC%20057-2024%20PRE%20Contratos%20FE%20-%20Equities%20(PT).pdf);
  OC 041/2026-VNC e CE 109/2021-VNC (URLs em `03-pesquisa.md` §6); OC 003/2020-VOP
  (https://www.b3.com.br/data/files/97/C7/BB/E1/F50BF6109A4874F6AC094EA8/OC%20003-2020-VOP%20Feriados%202020.pdf);
  Caderno de Fórmulas CDB (`03-pesquisa.md` §2); treinamento DI, metodologia da Taxa DI, DDI,
  FRC, calendário de vencimentos de opções (`03-pesquisa.md` §2, §4, §8).
- **ANBIMA:** Metodologias (link do texto); feriados (https://www.anbima.com.br/feriados/feriados.asp,
  https://www.anbima.com.br/feriados/fer_nacionais/2026.asp).
- **Tesouro:** Metodologia (`03-pesquisa.md` §3); PrecoTaxaTesouroDireto.csv e metadado
  (https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3);
  vencimentos do TD (https://www.tesourotransparente.gov.br/ckan/dataset/f30db6e4-6123-416c-b094-be8dfc823601).
- **PyPI:** https://pypi.org/project/bizdays/
- **Hull:** Pearson (https://www.pearson.com/store/p/options-futures-and-other-derivatives/P200000005938/9780136939979);
  slides FIU (https://faculty.fiu.edu/~dupoyetb/Financial_Risk_Mgt/lectures/Ch06.pdf).
- **Tosi:** https://www.martinsfontespaulista.com.br/matematica-financeira-com-enfase-em-produtos-bancarios-762375/p
- **Garcia:** link do texto.
- **Busca secundária** (só para localizar documentos): https://www.infomoney.com.br/?p=1547692,
  https://oreilly.com/library/view/options-futures-and/9780133456318
