# Etapa 6 — Revisão de linha e norma

Laudo do agente `revisor-gramatical`, gravado pelo pipeline principal. Post
`2026-10-30-du252-contagem-de-dias`, linha Notas de um Professor, voz ensaística em registro
técnico (§4.1 com o rigor do §4.3). Texto revisado: corpo de `processo/04-draft-v2.md`, do H1
(l. 35) ao aviso legal (l. 291); números de linha desse arquivo. As correções são aplicadas na
consolidação (etapa 9).

**Legenda**
- `norma`: erro objetivo, ou aplicação das regras 1 ou 4 do guia (obrigatórias). Entra.
- `linha`: clareza ou ritmo; o autor decide. ★ = as que o revisor aplicaria. Cinco ★ (R-1 a
  R-5) são as decisões sobre rótulos que o briefing deixou para esta etapa: sem ★, o negrito
  fica.
- **(pipeline)**: trecho redigido pelo pipeline (notas laterais 2, 4, 5, 7 e 8 do v2, rótulo
  da nota histórica, anotações de Hull, Tosi e ANBIMA), lido com atenção dobrada para tique de
  IA.

**O que não mexi (voz ou já correto)**
- Fragmentos e frases curtas: "Faltaram três.", "São duas.", "Quase.", "Mas:", "Quatro
  armadilhas que já vi em código de gente boa.", "Agora a parte que eu acho mais bonita."
- Aforismos protegidos: "É um número esperando uma régua."; "O fim de semana não é de graça.
  Ele está embutido no período da sexta."; "252 é uma convenção, não uma contagem."; "A taxa é
  a mesma. O ano é que muda de tamanho."; "Mesmo dinheiro, quatro números. Nenhum está errado.
  Errado é ler um número com a régua do outro."; "antes de perguntar quanto rende, pergunte em
  que régua."; "O problema do professor é que ele esquece que foi aluno."; "ele tem dois meses
  de vida."
- Registro: "te" junto de "você" (l. 278; precedente samurais), "dá para fazer na mão", "no
  automático", "Exemplo fresco", "então" conclusivo depois de vírgula (l. 161).
- "Não é X. É Y.": cerca de 7 ocorrências, todas do rascunho (l. 45, 53, 97, 101, 140, 142).
  O pipeline não acrescentou nenhuma.
- Crases conferidas ("volta à série", "responde às quatro", "a duas perguntas", "a perguntas
  diferentes", "a qualquer taxa", "até a bolsa" = "mesmo"); reduzidas ("Tirando sábados…,",
  "usando o calendário da B3,", "Com isso em mente,", "comprada… e levada até o vencimento, em
  1º de janeiro de 2027,"); concordâncias ("cada emissor e a própria ANBIMA aplicam", "sobram
  40 dias úteis", "só três anos têm", "os 12% rendem").
- "Qual a contagem…?" (elipse aceita), "São o mesmo?" e "VF" (l. 81: "um valor de face VF" já
  apresenta o símbolo, como "τ (tau)").
- Comentários em português dentro dos blocos de código (l. 178, 219, 221, 236): sem erro. Blocos,
  LaTeX, `[PREENCHER: …]` e `[graf-01 — …]` intactos.

---

## Transversais

**T-1. Negrito (regra 4), em três usos**

(a) Ênfase no meio da frase: sai, `norma`. 13 ocorrências:
- "régua" (l. 64) e "motor" (l. 70) viram 'régua' e 'motor' (termos cunhados na primeira
  ocorrência, como o 'internamente homogêneo' do corpus).
- Nas demais só sai o negrito: DU/252, Actual/360, 30/360 (l. 66–68); "régua DU/252 com motor
  composto" (l. 77); "um dia útil" (l. 93); "anual, base 252 dias úteis" (l. 99); "11,85%"
  (l. 107); "40 dias úteis" (l. 120); "22 dias úteis" e "20 dias de pregão" (l. 159);
  "quinta-feira, 19/11" (l. 261).

(b) Rótulos, `linha`:
- **R-1 ★ Listas.** Nas listas de perguntas (l. 57–58, l. 269–272), sai o negrito e a numeração
  vira o rótulo. Dados do CDB (l. 115–118) e regra prática (l. 165–166): texto simples com
  dois-pontos (regra 3), ex. "- Valor aplicado: R$ 100.000,00". ANBIMA e B3 (l. 150–151): o
  rótulo ganha artigo ("- O calendário ANBIMA responde: …"); sem negrito, "Calendário ANBIMA
  responde" fica telegráfico.
- **R-2 ★ Parágrafos de "ANBIMA ou B3?"** (l. 155, 161; detalhe abaixo). Corta "Fim de ano
  (todo ano)." (a l. 153 já diz isso); o rótulo da nota histórica se funde à primeira frase.
- **R-3 ★ Armadilhas viram H3** (l. 172, 183, 185, 200): "### Armadilha 1: dia útil sem
  feriado", sem ponto final. Paralelo com "### Caminho A/B" na mesma H2; H3 é vocabulário da
  linha (09-18, 09-28). Efeito colateral aceitável: a l. 207 ("Com isso em mente…") fica sob o
  H3 da Armadilha 4 e se lê como fecho das quatro.
- **R-4 ★ "Outros relógios"** (l. 257, 259, 261): rótulo fundido à primeira frase com
  dois-pontos. São notas de um parágrafo, e "Três notas rápidas" já anuncia o bloco. Resolve
  também a repetição da l. 257 ("o juro não descansa. … os juros correm").
- **R-5 ★ Bibliografia** (l. 284–287): formato da casa (09-28, 10-27): autor, *título*, ed.
  (editora, ano) — anotação. Sem negrito, link no título no lugar de "[Link]".

(c) Linha do contratado na tabela (l. 126): não mexida; etapa 8.

**T-2. Aspas ★ (`linha`).** Convenção da casa (regra 4; 09-28, 10-27): duplas para citação,
fala e rótulo do mercado; simples para distanciamento e uso metalinguístico.
- Passam a simples: 'anos' (l. 57), 'pacote' (l. 75), 'inclusive/exclusive' (l. 87), 'diária'
  (l. 93), 'dia' (l. 97), 'oficiais' (l. 146), 'quase' (l. 148), 'perder' (l. 159), 'aplicação
  inclusive, vencimento exclusive' (l. 251, que também deixa de encostar nas duplas do código
  `inclusive="left"`).
- Ficam duplas: "12% ao ano" (deck, l. 55 e H2), "12% a cada ano do calendário" (l. 45), a fala
  da l. 60, "ao ano, base 252" (l. 107), "ao ano" (l. 109), "Dia Útil" e "Dia de Sessão de
  Negociação" (l. 157, citação), título da seção do Hull.

**T-3. Itálico**
- Ênfase vira aspas (`norma`, regra 4): "*o juro correu hoje?*" e "*a bolsa abriu hoje?*" →
  'o juro correu hoje?' e 'a bolsa abriu hoje?' (l. 150–151).
- Estrangeirismo não incorporado (`norma`): *stack* (l. 230), *Treasuries* (l. 257), *over*
  (l. 285).
- Redondo: nomes de convenção (Actual/360, Actual/Actual, 30/360, DU/252) e nomes próprios
  (Corpus Christi, PyPI, Python, pandas). *day count* e *du* já estão certos.
- Nota de rigor (l. 142) ★ `linha`: sai o itálico, fica a citação (o bloco já marca o aparte).
- Deck em itálico (l. 37) vai para o frontmatter na etapa 9.

**T-4. Consistência** (`norma`): "A `bizdays`" (l. 196) × "do `bizdays`" (l. 200) →
masculino (o pacote) nas duas. Se o autor preferir o feminino, vale nas duas.

---

## Glosas (regra 1; §5.1, definição funcional)

| Termo | 1ª ocorrência | Decisão | Base |
|---|---|---|---|
| LTN | l. 41 | glosa (`norma`) | pesquisa §1, §3 |
| Selic, DI, CDB | l. 77 | glosa (`norma`) | Selic: glosa do corpus ("a taxa básica de juros da economia", `títulos_do_tesouro_nacional`); DI: pesquisa §4; CDB: precedente |
| títulos públicos, debêntures, futuro de DI | l. 77 | sem glosa | vocabulário da série; a glosa do DI1 (l. 81) cobre o futuro de DI |
| DI1, PU | l. 81 | glosa e sigla (`norma`) | pesquisa §3; precedente 09-28 (PU) |
| VF, liquidação, *day count*, τ | l. 81, 85, 57, 64 | já glosados | — |
| DU | l. 66 | glosado pela fórmula | — |
| DC (DC/360, DC/365) | tabela, l. 127 | glosa na l. 67 (`norma`) | treinamento B3 "dc/360" (pesquisa §8) |
| marcação | l. 131 | glosa (`norma`) | — |
| ANBIMA | l. 142 | glosa (`norma`) | precedente 09-28; pesquisa §3, §6 |
| B3, Banco Central, BCB, PUC-Rio | l. 99–101 | sem glosa | instituições (regra 8); "a bolsa abriu hoje?" faz o papel para a B3 |
| CMN | l. 150 | expansão (`norma`) | precedente 09-28 |
| pregão | l. 151 | glosa (`norma`) | OC 055/2024 ("Dia de Sessão de Negociação") |
| ajuste | l. 157 | glosa (`norma`); fora da lista do briefing | pesquisa §6, §10 |
| "registrados por valor final" | l. 161 (pipeline) | glosa (`norma`) | CE 013/2024-VPC; etapa 7 confere |
| `bizdays` | l. 196 (1ª em prosa) | glosa (`norma`) | l. 211 |
| numpy, pandas | l. 172 | sem glosa | bibliotecas-padrão da leitora-alvo (Camila) |
| PyPI | l. 200 | glosa (`norma`) | pesquisa §7 |
| *Treasuries*, Actual/Actual | l. 257 | glosa (`norma`) | pesquisa §8 (slides de Hull, "$4 × (31/184)"); etapa 7 confere |
| cupom cambial, DDI, FRC | l. 259 | glosa (`norma`); siglas identificadas como contratos | pesquisa §8; etapa 7 confere "juro em dólar" |
| rolagem | l. 261 | glosada pela própria frase | — |
| mesa | l. 267 | sem glosa | precedente samurais |
| taxa *over*, CDI | l. 285 (pipeline) | glosa (`norma`) | pesquisa §4 ("overs"), §11 |
| NTN-F, NTN-B, LFT | l. 286 (pipeline) | glosa por classe (`norma`) | pesquisa §3 |
| FIDC | l. 276 | já glosado | — |

---

## Diff por parágrafo

### Título e deck (l. 35–37)
Sem mudança.

### Abertura (l. 41–49)
- **l. 41** `norma` (regra 1): "Uma LTN comprada a 12% ao ano" → "Uma LTN (Letra do Tesouro
  Nacional, o título público prefixado) comprada a 12% ao ano". Curta para não pesar na
  primeira frase; o "paga R$ 1.000 no vencimento" já vem na l. 81.
- **l. 43–45:** sem mudança.
- **l. 47** `linha`, opcional: "o júnior que senta do seu lado" → "o júnior que senta ao seu
  lado" ("do seu lado" também se lê como "a seu favor"). Se o autor quiser o registro oral,
  fica.
- **l. 49:** intocado.

### "12% ao ano" de quê? (l. 53–60)
- **l. 57–58** R-1 ★ e T-2: "1. **Quanto tempo passou, medido em "anos"?** Essa é…" → "1.
  Quanto tempo passou, medido em 'anos'? Essa é…". Mesmo tratamento no item 2.
- **l. 60** `linha`, opcional: "inclusive em sala de aula" → "até em sala de aula" ("inclusive"
  vira termo técnico 25 linhas depois e cria eco).

### A régua e o motor (l. 64–87)
- **l. 64** `norma` (regra 4): "como uma **régua**" → "como uma 'régua'".
- **l. 66–68** `norma` (regra 4): tirar o negrito de DU/252, Actual/360, 30/360.
  `norma` (regra 1, sigla e consistência): "- Régua do mercado monetário internacional,
  Actual/360: τ = dias corridos ÷ 360." → "- Régua do mercado monetário internacional,
  Actual/360 (no Brasil, DC/360, de dias corridos): τ = dias corridos ÷ 360." A tabela
  (l. 127–129), as taxas equivalentes (l. 137–138) e a pergunta 1 (l. 269) usam DC/360 e
  DC/365 sem que o texto diga que DC é "dias corridos" nem que DC/360 é o Actual/360 da lista;
  a l. 257 volta a Actual/360.
- **l. 70** `norma` (regra 4): "é o **motor**" → "é o 'motor'".
- **l. 75** T-2: "pacote" → 'pacote'. `linha`, opcional: "aprender as duas peças separadas" →
  "aprender as duas peças em separado".
- **l. 77** (M-5 segue com a etapa 7; se a frase mudar lá, as glosas vão junto)
  `norma` (regra 4): tirar o negrito.
  `norma` (regra 1): "Na renda fixa brasileira em reais (Selic, DI, títulos públicos, CDB,
  debêntures, futuro de DI), a combinação é **régua DU/252 com motor composto**:" → "Na renda
  fixa brasileira em reais, a combinação é régua DU/252 com motor composto. Vale para a Selic
  (a taxa básica de juros), o DI (a taxa dos empréstimos entre bancos), os títulos públicos, o
  CDB (Certificado de Depósito Bancário), as debêntures e o futuro de DI. A fórmula é:". A
  lista sai do parêntese para não aninhar glosas; "A fórmula é:" (corpus, regra 9) reintroduz
  o bloco. A glosa do DI é curta de propósito: a l. 93 completa com "um dia útil". Alternativa
  pior, mantendo o parêntese: glosar a Selic na l. 97 e o CDB na l. 113; a glosa chega ~20
  linhas depois.
- **l. 81** `norma` (regra 1 e sigla): "(R$ 1.000 numa LTN, 100.000 pontos num contrato de DI1),
  o preço unitário hoje é:" → "(R$ 1.000 numa LTN; 100.000 pontos no DI1, o contrato futuro de
  DI da B3), o preço unitário (PU) hoje é:".
- **l. 85 (pipeline)** `linha` ★: "O dia em que o dinheiro sai conta; o dia em que ele volta,
  não." → "Entra na contagem o dia em que o dinheiro sai; o dia em que ele volta, não." Em voz
  alta, "o dinheiro sai conta" se ouve como "sai da conta".
- **l. 87 (pipeline)** `linha` ★: "A LTN do começo do texto vence em" → "A nossa LTN vence em"
  (a l. 107 do autor usa "a LTN do começo do texto" para fechar o loop; repetida 20 linhas
  antes, perde força; "nossa" como em "No nosso CDB", l. 181). `linha` + T-2: "e é aí que o
  "inclusive/exclusive" volta, no código." → "e é no código que o 'inclusive/exclusive' volta."

### Por que o relógio para no sábado (l. 91–109)
- **l. 93** `norma` (regra 4): tirar o negrito de "um dia útil". `linha` ★: "A taxa DI é a
  média dos empréstimos entre bancos" → "A taxa DI é a taxa média dos empréstimos entre bancos".
  T-2: "diária" → 'diária'. `linha`, opcional: "cobrindo sexta, sábado e domingo" → "para sexta,
  sábado e domingo".
- **l. 97** T-2: "dia" → 'dia'.
- **l. 99** `norma` (regra 4): tirar o negrito de "anual, base 252 dias úteis".
- **l. 101–105:** sem mudança (l. 105, do pipeline, sem achado).
- **l. 107** `norma` (regra 4): tirar o negrito de "11,85%".
- **l. 109 (pipeline)** `linha` ★: "De 2001 a 2030, o ano tem em média 251 dias úteis, e os 12%
  "ao ano" rendem, em média, 11,95% por ano de calendário." → "De 2001 a 2030, o ano tem em
  média 251 dias úteis. Nesse ritmo, os 12% "ao ano" rendem 11,95% por ano de calendário." (três
  "média" em duas frases). A primeira frase ("E, na média, ele é menor do que a convenção.")
  fica.

### Quanto custa a régua errada (l. 113–142)
- **l. 115–118** R-1 ★: "- **Valor aplicado:** R$ 100.000,00" → "- Valor aplicado: R$
  100.000,00", idem nos outros três.
- **l. 120** `norma` (regra 4): tirar o negrito de "40 dias úteis".
- **l. 122** `linha`, opcional: "Agora veja o que acontece" → "Veja o que acontece" (dois
  parágrafos seguidos começando com "Agora"; o da l. 133 é o mais forte).
- **l. 124–129:** tabela intocada (etapa 8; DC resolvido na l. 67).
- **l. 131** `norma` (regra 1): "na marcação, em dois meses" → "na marcação (o valor atribuído
  todo dia a cada título da carteira), em dois meses".
- **l. 133–140:** sem mudança.
- **l. 142** `linha` ★ (T-3): "> *Nota de rigor: … conclusão.*" → "> Nota de rigor: …
  conclusão." `norma` (regra 1): "a própria ANBIMA" → "a própria ANBIMA (a associação das
  instituições do mercado financeiro, que publica a metodologia de preço dos títulos e o
  calendário de feriados)".

### ANBIMA ou B3? (l. 146–166)
- **l. 146, 148** T-2: "oficiais" → 'oficiais'; "quase" → 'quase'.
- **l. 150** R-1 ★: "- **Calendário ANBIMA** responde:" → "- O calendário ANBIMA responde:".
  `norma` (regra 4): "*o juro correu hoje?*" → "'o juro correu hoje?'". `norma` (sigla): "Pela
  [Resolução CMN nº 4.880/2020](…)" → "Pela [Resolução nº 4.880/2020 do Conselho Monetário
  Nacional (CMN)](…)".
- **l. 151** R-1 ★: "- **Calendário B3** responde:" → "- O calendário B3 responde:". `norma`
  (regra 4): "*a bolsa abriu hoje?*" → "'a bolsa abriu hoje?'". `norma` (regra 1): "São os dias
  de pregão." → "São os dias de pregão (a sessão de negociação da B3)."
- **l. 153 (pipeline):** sem achado.
- **l. 155** R-2 ★: cortar "**Fim de ano (todo ano).**"; o parágrafo começa em "A B3 não tem
  pregão em 24 de dezembro…".
- **l. 157** `linha` ★: "no contrato de futuro de DI" → "no contrato futuro de DI". `norma`
  (regra 1): "o ajuste acumula" → "o ajuste (o acerto diário de ganhos e perdas do contrato)
  acumula" (vale para a l. 161). `linha`: "Taxa DI" → "taxa DI" (como nas l. 93 e 155). `linha`:
  "pela Resolução CMN 4.880" → "pela mesma Resolução nº 4.880".
- **l. 159** `norma` (regra 4): tirar o negrito de "22 dias úteis" e "20 dias de pregão". T-2:
  "perder" → 'perder'.
- **l. 161 (rótulo e duas frases finais do pipeline)**
  - R-2 ★: "**Uma nota histórica, para quem mexe em série antiga: os feriados de São Paulo (até
    2021).** A B3 fechava em 25 de janeiro, 9 de julho e 20 de novembro." → "Uma nota
    histórica, para quem mexe em série antiga: até 2021, a B3 fechava nos feriados de São Paulo
    (25 de janeiro, 9 de julho e 20 de novembro)." `linha`, opcional: "série antiga" → "série
    histórica".
  - `linha` ★: abrir parágrafo novo em "A mudança mexeu em dinheiro:" (~130 palavras com duas
    ideias; §5.4).
  - `linha` ★ (pipeline): "ganhou um dia útil a menos até o vencimento" → "passou a ter um dia
    útil a menos até o vencimento".
  - `norma` (regra 1, pipeline): "registrados por valor final" → "registrados por valor final
    (aqueles em que o registro fixa o valor de resgate)".
  - `linha`, opcional: "desde 2024, o 20 de novembro virou feriado nacional" → "desde 2024, o 20
    de novembro é feriado nacional".
  - Resultado com as ★ e a norma:
    > Uma nota histórica, para quem mexe em série antiga: até 2021, a B3 fechava nos feriados
    > de São Paulo (25 de janeiro, 9 de julho e 20 de novembro). Nesses dias, o juro corria
    > normalmente no resto do país, mas a bolsa estava parada. A partir de 2022, a B3 passou a
    > funcionar nos feriados municipais e estaduais paulistas. E, desde 2024, o 20 de novembro
    > virou feriado nacional (Lei nº 14.759/2023), então hoje ele fecha os dois calendários.
    >
    > A mudança mexeu em dinheiro: todo contrato em dias úteis que atravessava a data passou a
    > ter um dia útil a menos até o vencimento. A B3 recalculou a taxa dos CDBs prefixados
    > registrados por valor final (aqueles em que o registro fixa o valor de resgate), para que
    > o resgate não mudasse, e o ajuste dos futuros de juros absorveu o impacto da nova
    > contagem.
- **l. 165–166** R-1 ★: "- **Para acumular juros e precificar renda fixa:** calendário
  ANBIMA." → "- Para acumular juros e precificar renda fixa: calendário ANBIMA.", idem no item
  da B3.

### Na prática: Python sem cair em armadilhas (l. 170–251)
- **l. 172** R-3 ★: "### Armadilha 1: dia útil sem feriado". `linha`: "`numpy.busday_count` e
  `pandas.bdate_range` só tiram sábado e domingo se você não passar a lista de feriados." →
  "Sem a lista de feriados, `numpy.busday_count` e `pandas.bdate_range` só tiram sábado e
  domingo." (com o H3, o parágrafo começaria por identificador em minúscula; "só… se não" pede
  releitura).
- **l. 181** `linha`: "isso viraria 43 dias úteis em vez de 40, e um resgate R$ 137 acima" →
  "isso daria 43 dias úteis em vez de 40 e um resgate R$ 137 acima".
- **l. 183** R-3 ★: vira H3; texto não muda (B-4: autor manteve).
- **l. 185 (pipeline)** R-3 ★: vira H3. `linha` ★: "A biblioteca não precisa seguir a convenção
  das pontas." → "Nenhuma biblioteca é obrigada a seguir a convenção das pontas." (artigo
  definido sem antecedente; o `bizdays` só é apresentado no Caminho A).
- **l. 196** `norma` (T-4): "A `bizdays` conta" → "O `bizdays` conta". `norma` (regra 1):
  acrescentar "(biblioteca Python que já traz os calendários ANBIMA e B3, apresentada no
  Caminho A)" depois de "O `bizdays`". `linha`: "o 2 de janeiro sai da conta, o 1º de janeiro
  não entra no lugar" → "o 2 de janeiro de 2026 sai da conta, o 1º de janeiro de 2027 não entra
  no lugar".
- **l. 200** R-3 ★: vira H3. `norma` (regra 1 e pontuação): "Na versão 1.0.19 do `bizdays` (a
  mais recente no PyPI enquanto escrevo), o calendário" → "Na versão 1.0.19 do `bizdays`, a mais
  recente no PyPI (o repositório de pacotes do Python) enquanto escrevo, o calendário". `linha`:
  "Qualquer data depois disso levanta um `DateOutOfRange`." → "Com qualquer data depois disso,
  a função levanta um `DateOutOfRange`."
- **l. 207:** sem mudança (ver R-3).
- **l. 211** `linha`, opcional: "foi feita para essa realidade" → "foi feita para o calendário
  brasileiro".
- **l. 230** `norma` (T-3): "stack de dados" → "*stack* de dados".
- **l. 251** T-2: aspas da frase passam a simples.

### Outros relógios (l. 255–261)
- **l. 257** R-4 ★: "**Lá fora, o juro não descansa.** Nos Estados Unidos, os juros correm no
  fim de semana." → "Lá fora, o juro não descansa: nos Estados Unidos, ele corre no fim de
  semana." `norma` (T-3 e regra 1): "Os Treasuries usam Actual/Actual," → "Os *Treasuries* (os
  títulos públicos americanos) usam Actual/Actual (dias corridos divididos pelos dias corridos
  do período de juros),". `linha`: "base 360 com contagem aproximada 30/360 ou correta dc/360,
  contra base 252 com du/252." → "base 360, com contagem aproximada (30/360) ou correta
  (dc/360), contra base 252 (du/252)."
- **l. 259** R-4 ★: "**Dois relógios no mesmo prédio.** Dentro da própria B3," → "Dois relógios
  no mesmo prédio: dentro da própria B3,". `norma` (regra 1): "o cupom cambial (DDI e FRC)" →
  "o cupom cambial (o juro em dólar, negociado nos contratos DDI e FRC)". `linha` ★: "Isso
  merece uma nota só para ele." → "O cupom cambial merece uma nota só para ele."
- **l. 261 (duas primeiras frases do pipeline)**
  - R-4 ★: "**O terceiro relógio: a rolagem.** A regra que decide…" → "O terceiro relógio é a
    rolagem: a regra que decide para onde vai uma data que cai num feriado."
  - `linha` ★ (pipeline): "também muda de mercado" → frase nova "Ela também varia de um mercado
    para outro."
  - `linha` ★ (pipeline): "Na renda fixa, já vimos, ela vai para o dia útil seguinte" → "Na
    renda fixa, já vimos, a data vai para o dia útil seguinte".
  - `norma` (regra 4): tirar o negrito de "quinta-feira, 19/11".
  - `linha` ★: "Quem planejou rolar na sexta" → "Quem planejou rolar a posição na sexta".
  - Resultado: "O terceiro relógio é a rolagem: a regra que decide para onde vai uma data que
    cai num feriado. Ela também varia de um mercado para outro. Na renda fixa, já vimos, a data
    vai para o dia útil seguinte (o `following` do código). Nas opções sobre ações da B3, ela é
    antecipada. Exemplo fresco: em novembro de 2026, a terceira sexta-feira é o feriado de
    20/11, e o vencimento das opções sobre ações foi antecipado para quinta-feira, 19/11. Quem
    planejou rolar a posição na sexta vai encontrar a série já vencida."

### Antes de perguntar quanto rende (l. 265–278)
- **l. 267** `norma` (regência): "a qualquer taxa que chegar na sua mesa" → "a qualquer taxa que
  chegar à sua mesa".
- **l. 269–272** R-1 ★: tirar o negrito ("1. Qual a contagem de dias? DU/252, DC/360, DC/365,
  30/360?" etc.).
- **l. 274–278:** sem mudança.

### Para ir além (l. 284–287)
R-5 ★ (formato) e `norma` (glosas e itálico, anotações do pipeline). Resultado:
- "John C. Hull, *Options, Futures, and Other Derivatives*, 11ª ed. (Pearson, 2021), capítulo
  6, seção "Day Count and Quotation Conventions" — as réguas do mercado americano
  (Actual/Actual, 30/360, Actual/360) e como cada uma acumula juros dentro do período."
- "Armando José Tosi, *Matemática Financeira com Ênfase em Produtos Bancários*, 4ª ed. (Atlas,
  2015) — taxa *over* (a de um dia útil), CDI (Certificado de Depósito Interbancário; no
  mercado, também o nome da taxa DI) e Selic do ponto de vista do produto bancário
  brasileiro." (CDI e "over" sem glosa hoje; única ocorrência de CDI no post.)
- "ANBIMA, [*Metodologias ANBIMA de Precificação*](…) — as fórmulas oficiais de PU e taxa em
  base 252 para os títulos públicos federais (LTN, NTN-F, NTN-B e LFT), com as regras de
  truncamento." (ver "Sinalizado" sobre "oficiais")
- "Márcio G. P. Garcia (PUC-Rio), [comentário de 30/06/1997](…) — escrito logo após a Circular
  BCB nº 2.761, com a observação dos 249 dias úteis de 1998." (falta o título; ver
  "Sinalizado")

**l. 291 (aviso legal):** fora do escopo, padrão da casa.

---

## Tiques de IA (`frente-d`), trechos do pipeline

| Trecho | Linha | Veredito |
|---|---|---|
| "O dia em que o dinheiro sai conta…" | 85 | ambiguidade em voz alta (★) |
| vencimento em feriado | 87 | eco de "LTN do começo do texto" (★); vírgula antes de "no código" |
| "só três anos têm exatamente 252…" | 105 | sem achado |
| viés do 252 | 109 | "média" três vezes (★) |
| "A diferença que vale hoje…" | 153 | sem achado |
| rótulo da nota histórica | 161 | fundido (R-2) |
| "20/11 mexeu em dinheiro" | 161 | "ganhou… a menos" (★); jargão sem glosa; parágrafo longo (★) |
| "A biblioteca não precisa…" | 185 | artigo sem antecedente (★) |
| rolagem | 261 | "muda de mercado" (★); referente de "ela" (★) |
| anotações Hull, Tosi, ANBIMA | 284–286 | Hull sem achado; siglas sem glosa em Tosi e ANBIMA (`norma`) |

Sem "é importante ressaltar", "crucial", "fundamental", "jornada", "cenário" ou fecho genérico.
Perguntas retóricas (l. 87, 99, 146) introduzem o conteúdo seguinte. Tríades são listas
factuais.

---

## Sinalizado para outras etapas

**Estrutural (não corrigido)**
1. A Armadilha 3 usa o `bizdays` (código l. 187–194, prosa l. 196) antes de a biblioteca ser
   apresentada (l. 211). A glosa da l. 196 remenda; a ordem é da estrutura (M-4 já decidida).
2. M-5 continua com a etapa 7. Se a l. 77 for reescrita (CDB e debênture DU/252 por padrão, não
   por regra), as glosas de Selic, DI e CDB vão para a frase nova; se o CDB sair da l. 77, a
   glosa do CDB vai para a l. 113.

**Factual (etapa 7)**
1. Glosas com conteúdo a conferir: cupom cambial = "o juro em dólar"; Actual/Actual = "dias
   corridos divididos pelos dias corridos do período de juros"; "ajuste" = acerto diário de
   ganhos e perdas; "registrados por valor final" (CE 013/2024-VPC); DC/360 como nome
   brasileiro do Actual/360; ANBIMA como publicadora da metodologia e do calendário; PyPI;
   Selic = "a taxa básica de juros".
2. l. 172: segundo a pesquisa §7, com frequência 'B' o `bdate_range` ignora os feriados mesmo
   quando passados; "se você não passar a lista de feriados" (e a reordenação "Sem a lista de
   feriados") pode ser imprecisa para o pandas. Testar.
3. l. 109: se o ★ entrar, conferir se "Nesse ritmo" diz o mesmo que "em média" (1,12^(251/252)
   − 1 = 11,95% é o rendimento do ano médio e a média geométrica do período).
4. l. 93: se o ★ "taxa média" entrar, a metodologia da B3 fala em média ponderada; a etapa 7
   decide o adjetivo.
5. Bibliografia: "fórmulas oficiais" (a ANBIMA é associação privada; "de referência" é mais
   exato); Garcia sem título ("Efeitos da anualização da taxa Selic", Depto. de Economia da
   PUC-Rio, pesquisa §4); Tosi com editora "Atlas" × "GEN Atlas" (pesquisa §12).

**Etapa 8:** destaque da linha do contratado na tabela do CDB (l. 126).
**Etapa 9:** deck e título para o frontmatter sem formatação; links da bibliografia no título
(R-5).

---

## Contagem

| Classe | Contagem |
|---|---|
| `norma`, regra 4 (negrito de ênfase) | 13 (2 viram aspas simples: 'régua', 'motor') |
| `norma`, regra 4 (itálico de ênfase) | 2 (l. 150, 151) |
| `norma`, regra 1 (glosas e siglas) | 21 termos: LTN, DC, Selic, DI, CDB, DI1, PU, marcação, ANBIMA, CMN, pregão, ajuste, valor final, `bizdays`, PyPI, Treasuries, Actual/Actual, cupom cambial, taxa *over*, CDI, NTN-F/NTN-B/LFT |
| `norma`, itálico de estrangeirismo | 3 (*stack*, *Treasuries*, *over*) |
| `norma`, outras | 2 (gênero do `bizdays`; "chegar à") |
| **Total `norma`** | **41** |
| `linha` | 35 |
| ★ | 19: R-1 a R-5, T-2, Nota de rigor, l. 85, 87, 93, 109, 157, 161 ×2, 185, 259, 261 ×3 (9 em trecho do pipeline) |
| Glosas avaliadas e mantidas | 13: títulos públicos, debêntures, futuro de DI, VF, liquidação, DU, B3, BCB, PUC-Rio, numpy, pandas, rolagem, mesa |
| Sinalização estrutural | 2, nenhuma nova de severidade |
| Aforismos alterados | 0 |
