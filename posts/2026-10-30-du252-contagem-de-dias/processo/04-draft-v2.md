# Etapa 4 — Draft v2

Base: `04-draft-v1.md`, com as respostas do autor à crítica (`05-critica.md`), dadas em
2026-10-30. Mesmas regras do v1: norma, negrito e glosas ficam para a etapa 6, e verificação
para a etapa 7. A tabela do CDB segue até a etapa 9. A tabela de dias úteis já saiu nesta
versão, porque o conteúdo do graf-01 mudou (M-7). Os números novos (série 2001–2030, média 251,
11,95%) foram conferidos pelo pipeline no `ANBIMA.cal` do `bizdays` 1.0.19 e são cálculo
próprio. A etapa 7 refaz a conta.

Não consome loop: é resposta à etapa 5, antes do gate (precedente
`2026-10-27-samurais-e-duelos`, draft v2).

## Notas laterais: o que mudou do v1 para o v2

| # | Onde | Mudança | Origem |
|---|---|---|---|
| 1 | Abertura, [PREENCHER] | O marcador ganha a nota "Ela faz a ponte com o título…". O gancho não muda | Autor: M-1, "a memória faz a ponte" |
| 2 | "A régua e o motor", fim | "Guarde o 'inclusive/exclusive': ele volta mais adiante, no código." vira dois parágrafos. O primeiro traz a convenção em linguagem leiga ("O dia em que o dinheiro sai conta; o dia em que ele volta, não."). O segundo, o vencimento em feriado com a LTN de 01/01/2027: 249 dias úteis até 01/01 ou até 04/01, e a ponte para o código | Autor: M-4, "parágrafo na Anatomia"; `03-pesquisa.md` §3, §9 |
| 3 | Armadilha 3 | Sai a exposição da convenção, que agora está na Anatomia. Fica "a biblioteca não precisa seguir a convenção das pontas", o código e a explicação do (início, fim] | Autor: M-4 |
| 4 | "Por que o relógio para no sábado", tabela | A tabela 2024–2028 dá lugar ao marcador do graf-01 (série 2001–2030) e à frase "Entre 2001 e 2030, só três anos têm exatamente 252 dias úteis: 2004, 2025 e 2030." | Autor: M-7, "série 2001–2030"; `03-pesquisa.md` §0; execução local |
| 5 | Idem, depois de "O ano é que muda de tamanho." | Entra o viés: "E, na média, ele é menor do que a convenção. De 2001 a 2030, o ano tem em média 251 dias úteis, e os 12% 'ao ano' rendem, em média, 11,95% por ano de calendário." | Autor: B-6, "viés do 252"; cálculo próprio (1,12^(251/252) − 1 = 11,95%) |
| 6 | "ANBIMA ou B3?" | Ordem invertida. O fim de ano vem primeiro, como "a diferença que vale hoje", seguido da OC 055/2024 e de dezembro de 2026. Os feriados de São Paulo descem para depois da prova, como "uma nota histórica, para quem mexe em série antiga". Sai a numeração "1."/"2." e o "as diferenças estão em dois lugares" | Autor: M-6, "inverter a ordem" |
| 7 | Idem, nota histórica | Depois da Lei nº 14.759/2023, entra o 20/11 "mexeu em dinheiro": um dia útil a menos até o vencimento; a B3 recalculou a taxa dos CDBs prefixados registrados por valor final; o ajuste dos futuros absorveu o impacto | Autor: B-6, "20/11 mexeu em dinheiro"; `03-pesquisa.md` §10, item 3 (CE 006/2024-VPC, CE 013/2024-VPC, OC 207/2023-PRE) |
| 8 | "Outros relógios", rolagem | "Além de contar dias e capitalizar, existe a regra… Na renda fixa, ela vai para o dia útil seguinte." → "A regra que decide para onde vai uma data que cai num feriado também muda de mercado. Na renda fixa, já vimos, ela vai para o dia útil seguinte (o `following` do código)." O caso das opções fica | Autor: M-3, "corte parcial" |

**Decisões do autor sem mudança no texto:** M-2 (moldura de duas para quatro perguntas:
manter) e B-4 (Armadilha 2: manter).

**Para a etapa 7, além das divergências da pesquisa:** conferir as frases novas das notas 4, 5
e 7. A da nota 7 descreve três documentos da B3 de uma vez e é a que mais depende da letra das
fontes.

---

# Você está contando os dias úteis errado (e isso está custando dinheiro)

*Por que o juro brasileiro não corre no sábado, por que "12% ao ano" quase nunca rende 12% em um ano e como impedir que o calendário errado entre no seu código.*

---

Uma LTN comprada a 12% ao ano no primeiro dia útil de 2026 e levada até o vencimento, em 1º de janeiro de 2027, entrega 11,85% no período.

Ninguém errou a conta. Ninguém ficou com a diferença.

Acontece que 2026 tem 249 dias úteis. E a taxa da LTN não é "12% a cada ano do calendário". É 12% a cada 252 dias úteis. Faltaram três.

Se essa frase soou estranha, este texto é para você. Se soou óbvia, talvez ele seja para o júnior que senta do seu lado. O problema do professor é que ele esquece que foi aluno.

[PREENCHER: memória do autor — a primeira vez que uma conta sua não bateu com a tela da mesa por causa do calendário. Duas ou três frases. Ela faz a ponte com o título: é o primeiro "contar errado" do texto (crítica M-1).]

## "12% ao ano" de quê?

Uma taxa de juros, sozinha, não é informação completa. É um número esperando uma régua.

"12% ao ano" só vira dinheiro quando alguém responde a duas perguntas:

1. **Quanto tempo passou, medido em "anos"?** Essa é a convenção de contagem de dias (*day count*).
2. **Como a taxa se aplica a esse tempo?** Essa é a convenção de capitalização: linear ou composta.

O mercado mistura as duas o tempo todo, inclusive em sala de aula. "No Brasil é 252 composto, lá fora é 360 linear" soa como uma coisa só. São duas.

## A régua e o motor

Pense na contagem de dias como uma **régua**. Ela recebe duas datas e devolve uma fração de ano, que vou chamar de τ (tau).

- Régua brasileira, **DU/252**: τ = dias úteis ÷ 252.
- Régua do mercado monetário internacional, **Actual/360**: τ = dias corridos ÷ 360.
- Régua dos títulos corporativos americanos, **30/360**: todo mês vale 30 dias, e o ano, 360.

A capitalização é o **motor**. Ele recebe τ e a taxa e devolve o fator que multiplica o seu dinheiro.

- Motor composto: Fator = (1 + i)^τ
- Motor linear: Fator = 1 + i × τ

Régua e motor são peças independentes. Trocar uma não troca a outra. O mercado monta combinações diferentes conforme o produto, e é por isso que vale aprender as duas peças separadas, e não o "pacote".

Na renda fixa brasileira em reais (Selic, DI, títulos públicos, CDB, debêntures, futuro de DI), a combinação é **régua DU/252 com motor composto**:

$$\text{Fator} = (1 + i)^{du/252}$$

E, para um título prefixado que paga um valor de face VF no vencimento (R$ 1.000 numa LTN, 100.000 pontos num contrato de DI1), o preço unitário hoje é:

$$PU = \frac{VF}{(1 + i)^{du/252}}$$

Aqui, *du* é o número de dias úteis entre a data de liquidação (inclusive) e a data de vencimento (exclusive). O dia em que o dinheiro sai conta; o dia em que ele volta, não.

E se o vencimento cair num feriado? A LTN do começo do texto vence em 1º de janeiro de 2027, que é feriado, e é paga no dia útil seguinte, 4 de janeiro. Para a conta, tanto faz: de 2 de janeiro de 2026 (inclusive) até qualquer uma das duas datas (exclusive), os dias úteis são os mesmos 249. Quem programa nem sempre conta assim, e é aí que o "inclusive/exclusive" volta, no código.

## Por que o relógio para no sábado

A explicação que mais me ajudou não está em nenhuma fórmula. Está no próprio DI.

A taxa DI é a média dos empréstimos entre bancos pelo prazo de **um dia útil**. O banco que empresta na sexta recebe o dinheiro de volta na segunda. Entre uma ponta e outra, não existe liquidação. Logo, existe uma única "diária" cobrindo sexta, sábado e domingo.

O fim de semana não é de graça. Ele está embutido no período da sexta.

Em outras palavras: no mercado brasileiro, o "dia" financeiro não tem 24 horas. Ele é o intervalo entre duas liquidações. Como praticamente toda a renda fixa em reais é precificada a partir do DI e da Selic, a régua natural passa a ser o dia útil.

E de onde vem o 252? De uma decisão do Banco Central. Até 1997, a Selic era expressa como taxa ao mês, um hábito herdado da hiperinflação. A Circular BCB nº 2.761, de junho de 1997, mudou a forma de expressar a taxa para **anual, base 252 dias úteis**, a partir de 1º de janeiro de 1998. A [B3 descreve essa base](https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/s_di_train_prog/02-taxas-de-juros.htm) como um ano de 12 meses de 21 dias úteis.

Repare no detalhe: 252 é uma convenção, não uma contagem. Em junho de 1997, o economista Márcio Garcia (PUC-Rio) já apontava que 1998 teria 249 dias úteis, enquanto a fórmula usava 252. Quase três décadas depois, o calendário continua não colaborando:

[graf-01 — dias úteis por ano no calendário ANBIMA, 2001–2030, com linha de referência em 252. Substitui a tabela 2024–2028 do rascunho (decisão do autor, crítica M-7).]

Entre 2001 e 2030, só três anos têm exatamente 252 dias úteis: 2004, 2025 e 2030.

É daí que vem a LTN do começo do texto. Uma taxa "ao ano, base 252" é uma taxa por 252 dias úteis. Num ano com 249, você recebe 1,12^(249/252) − 1 = **11,85%**. Num ano com 253, como foi 2024, receberia 12,05%. A taxa é a mesma. O ano é que muda de tamanho.

E, na média, ele é menor do que a convenção. De 2001 a 2030, o ano tem em média 251 dias úteis, e os 12% "ao ano" rendem, em média, 11,95% por ano de calendário.

## Quanto custa a régua errada

Vamos a um exemplo concreto. Um CDB prefixado:

- **Valor aplicado:** R$ 100.000,00
- **Taxa:** 12,00% ao ano, base 252
- **Aplicação:** 01/10/2026 (quinta-feira)
- **Vencimento:** 01/12/2026 (terça-feira)

São 61 dias corridos. Mas o intervalo atravessa três feriados nacionais em dia de semana: 12 de outubro (segunda), 2 de novembro (segunda) e 20 de novembro (sexta). Tirando sábados, domingos e esses três feriados, com a aplicação incluída e o vencimento excluído, sobram **40 dias úteis**.

Agora veja o que acontece quando o mesmo número, 12%, é lido com réguas e motores diferentes:

| Cálculo | Fórmula | Fator | Valor de resgate | Diferença |
|---|---|---|---|---|
| **DU/252, composto (o contratado)** | 1,12^(40/252) | 1,01815145 | **R$ 101.815,15** | — |
| DC/365, composto | 1,12^(61/365) | 1,01912036 | R$ 101.912,04 | + R$ 96,89 |
| DC/360, composto | 1,12^(61/360) | 1,01938848 | R$ 101.938,85 | + R$ 123,70 |
| DC/360, linear | 1 + 0,12 × 61/360 | 1,02033333 | R$ 102.033,33 | + R$ 218,19 |

Num CDB de R$ 100 mil, a régua errada promete entre R$ 97 e R$ 218 que o contrato não vai pagar. Numa carteira de R$ 100 milhões, a mesma confusão gera uma divergência entre R$ 96,9 mil e R$ 218,2 mil na marcação, em dois meses.

Agora a parte que eu acho mais bonita. Inverta a pergunta: qual taxa, em cada régua, produz exatamente os R$ 1.815,15 de juros que esse CDB paga?

- 12,00% ao ano em DU/252 composto
- 11,36% ao ano em DC/365 composto
- 11,20% ao ano em DC/360 composto
- 10,71% ao ano em DC/360 linear

Mesmo dinheiro, quatro números. Nenhum está errado. Errado é ler um número com a régua do outro.

> *Nota de rigor: ignorei aqui os truncamentos de casas decimais que cada emissor e a própria ANBIMA aplicam no fator e no PU. Eles mexem nos centavos, não na conclusão.*

## ANBIMA ou B3? Duas perguntas diferentes

Quem vai automatizar essa conta esbarra cedo numa dúvida: existem dois calendários "oficiais" circulando, o da ANBIMA e o da B3. São o mesmo?

Quase. E o "quase" importa, porque eles respondem a perguntas diferentes.

- **Calendário ANBIMA** responde: *o juro correu hoje?* É o calendário bancário nacional. Pela [Resolução CMN nº 4.880/2020](https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20CMN&numero=4880), não são dias úteis para o mercado financeiro os sábados, os domingos, os feriados nacionais, a segunda e a terça de Carnaval e o Corpus Christi. Feriados estaduais e municipais não entram.
- **Calendário B3** responde: *a bolsa abriu hoje?* São os dias de pregão.

Na maior parte do ano, os dois coincidem. A diferença que vale hoje está no fim de ano.

**Fim de ano (todo ano).** A B3 não tem pregão em 24 de dezembro nem no último dia útil do ano. No calendário ANBIMA, os dois são dias úteis: o sistema interbancário funciona, a taxa DI é apurada e o juro corre. No último dia útil, as agências não abrem ao público, mas as operações entre instituições seguem.

A própria B3 faz essa separação no contrato de futuro de DI. A [especificação](https://www.b3.com.br/data/files/FF/C5/51/86/158EE810C54843E8DC0D8AA8/OC%20055-2024%20PRE%20Contratos%20FE%20-%20Juros%20(PT).pdf) define "Dia Útil" pela Resolução CMN 4.880 e "Dia de Sessão de Negociação" como dia com pregão. Quando há mais de um dia útil entre duas sessões, o ajuste acumula mais de uma Taxa DI. Ou seja: até a bolsa usa o calendário bancário para contar juros.

Em números: dezembro de 2026 tem **22 dias úteis** no calendário ANBIMA e **20 dias de pregão** no da B3. Se você acumular os juros de um CDB de R$ 100 mil a 12% usando o calendário da B3, vai "perder" dois dias úteis, cerca de R$ 90 no mês. Numa carteira de R$ 100 milhões, R$ 90 mil.

**Uma nota histórica, para quem mexe em série antiga: os feriados de São Paulo (até 2021).** A B3 fechava em 25 de janeiro, 9 de julho e 20 de novembro. Nesses dias, o juro corria normalmente no resto do país, mas a bolsa estava parada. A partir de 2022, a B3 passou a funcionar nos feriados municipais e estaduais paulistas. E, desde 2024, o 20 de novembro virou feriado nacional (Lei nº 14.759/2023), então hoje ele fecha os dois calendários. A mudança mexeu em dinheiro: todo contrato em dias úteis que atravessava a data ganhou um dia útil a menos até o vencimento. A B3 recalculou a taxa dos CDBs prefixados registrados por valor final, para que o resgate não mudasse, e o ajuste dos futuros de juros absorveu o impacto da nova contagem.

A regra prática:

- **Para acumular juros e precificar renda fixa:** calendário ANBIMA.
- **Para saber quando dá para negociar ou liquidar algo listado em bolsa:** calendário B3.

## Na prática: Python sem cair em armadilhas

Quatro armadilhas que já vi em código de gente boa.

**Armadilha 1: dia útil sem feriado.** `numpy.busday_count` e `pandas.bdate_range` só tiram sábado e domingo se você não passar a lista de feriados.

```python
import numpy as np

np.busday_count("2026-10-01", "2026-12-01")
# 43 — contou 12/10, 02/11 e 20/11 como dias úteis
```

No nosso CDB, isso viraria 43 dias úteis em vez de 40, e um resgate R$ 137 acima do contratado.

**Armadilha 2: o calendário certo para a pergunta errada.** Usar o calendário da B3 para acumular juros. Já vimos o custo acima.

**Armadilha 3: as pontas.** A biblioteca não precisa seguir a convenção das pontas. A LTN de 1º de janeiro de 2027 tem 249 dias úteis, como vimos. Mas:

```python
from bizdays import Calendar

cal = Calendar.load("ANBIMA")

cal.bizdays("2026-01-02", "2027-01-01")                 # 248
cal.bizdays("2026-01-02", cal.following("2027-01-01"))  # 249
```

A `bizdays` conta ao contrário da convenção: exclui a data inicial e inclui a final. Com as duas pontas em dia útil, o número sai igual. Com o vencimento num feriado, não: o 2 de janeiro sai da conta, o 1º de janeiro não entra no lugar, e some um dia.

O remédio é simples: leve a data de vencimento para o dia útil seguinte (`following`) antes de contar.

**Armadilha 4: o calendário tem data de validade.** Na versão 1.0.19 do `bizdays` (a mais recente no PyPI enquanto escrevo), o calendário da B3 termina em 31/12/2026. Qualquer data depois disso levanta um `DateOutOfRange`. O da ANBIMA vai até 2099. Se o seu código usa o calendário da B3, ele tem dois meses de vida. Confira:

```python
Calendar.load("B3").enddate      # datetime.date(2026, 12, 31)
Calendar.load("ANBIMA").enddate  # datetime.date(2099, 12, 25)
```

Com isso em mente, os dois caminhos limpos para o dia a dia:

### Caminho A: `bizdays`

A [biblioteca de Wilson Freitas](https://pypi.org/project/bizdays) foi feita para essa realidade. É leve e já vem com os calendários ANBIMA e B3.

```python
from bizdays import Calendar

cal = Calendar.load("ANBIMA")

aplicacao  = "2026-10-01"
vencimento = cal.following("2026-12-01")  # garante que a ponta final é dia útil

du = cal.bizdays(aplicacao, vencimento)   # conta (aplicação, vencimento]: com as duas pontas em dia útil, dá o du da convenção
fator = (1 + 0.12) ** (du / 252)

print(du, round(100_000 * fator, 2))
# 40 101815.15
```

### Caminho B: `pandas` puro, com [`CustomBusinessDay`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.offsets.CustomBusinessDay.html)

Se o ambiente não deixa instalar pacotes além da stack de dados, dá para fazer na mão. O preço é manter a lista de feriados você mesmo.

```python
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

# Feriados bancários nacionais de 2026 (Resolução CMN 4.880/2020 + Lei 14.759/2023)
feriados_2026 = [
    "2026-01-01", "2026-02-16", "2026-02-17", "2026-04-03",
    "2026-04-21", "2026-05-01", "2026-06-04", "2026-09-07",
    "2026-10-12", "2026-11-02", "2026-11-15", "2026-11-20",
    "2026-12-25",
]

dia_util_br = CustomBusinessDay(holidays=feriados_2026)
dias = pd.date_range("2026-10-01", "2026-12-01", freq=dia_util_br, inclusive="left")

print(len(dias))
# 40
```

O `inclusive="left"` é o "aplicação inclusive, vencimento exclusive" escrito em pandas.

## Outros relógios

Três notas rápidas para quem quer enxergar além do DU/252.

**Lá fora, o juro não descansa.** Nos Estados Unidos, os juros correm no fim de semana. Os Treasuries usam Actual/Actual, os títulos corporativos usam 30/360 e o mercado monetário usa Actual/360, todos com acúmulo linear dentro de cada período. O treinamento de DI da B3 resume o contraste numa tabela: base 360 com contagem aproximada 30/360 ou correta dc/360, contra base 252 com du/252.

**Dois relógios no mesmo prédio.** Dentro da própria B3, o cupom cambial (DDI e FRC) é cotado em taxa linear, base 360 dias corridos, enquanto o DI que entra na mesma conta corre em dias úteis. Na virada de um fim de semana, os dias corridos andam e os dias úteis não. Isso merece uma nota só para ele.

**O terceiro relógio: a rolagem.** A regra que decide para onde vai uma data que cai num feriado também muda de mercado. Na renda fixa, já vimos, ela vai para o dia útil seguinte (o `following` do código). Nas opções sobre ações da B3, ela é antecipada. Exemplo fresco: em novembro de 2026, a terceira sexta-feira é o feriado de 20/11, e o vencimento das opções sobre ações foi antecipado para **quinta-feira, 19/11**. Quem planejou rolar na sexta vai encontrar a série já vencida.

## Antes de perguntar quanto rende

Se fosse para levar uma única ideia deste texto: antes de perguntar quanto rende, pergunte em que régua.

Quatro perguntas para fazer a qualquer taxa que chegar na sua mesa:

1. **Qual a contagem de dias?** DU/252, DC/360, DC/365, 30/360?
2. **Qual o regime?** Composto ou linear?
3. **Qual o calendário?** ANBIMA para juros, B3 para pregão.
4. **E as pontas?** A data inicial entra? A final sai? E se o vencimento cair num feriado?

Quem responde às quatro sem hesitar já entendeu algo que muita gente experiente só sabe aplicar no automático.

Este texto foi um parêntese de ferramenta. O próximo volta à série de crédito com o FIDC (Fundo de Investimento em Direitos Creditórios), como ficou prometido no texto das debêntures.

Se este texto te poupou uma conta errada, encaminhe para quem está começando na mesa. E me conte, nos comentários, a pior pegadinha de calendário que você já encontrou.

---

## Para ir além

- **John C. Hull, *Options, Futures, and Other Derivatives*** (11ª ed., Pearson, 2021), capítulo 6, seção "Day Count and Quotation Conventions". As réguas do mercado americano (Actual/Actual, 30/360, Actual/360) e como cada uma acumula juros dentro do período.
- **Armando José Tosi, *Matemática Financeira com Ênfase em Produtos Bancários*** (4ª ed., Atlas, 2015). Taxa over, CDI e Selic do ponto de vista do produto bancário brasileiro.
- **ANBIMA — Metodologias ANBIMA de Precificação.** As fórmulas oficiais de PU e taxa em base 252 para LTN, NTN-F, NTN-B e LFT, com as regras de truncamento. [Link](https://www.anbima.com.br/data/files/5D/92/EC/E7/E82F971013C70F976B2BA2A8/Metodologias-ANBIMA-de-precificacao.pdf)
- **Márcio G. P. Garcia (PUC-Rio), 30/06/1997.** O comentário escrito logo após a Circular BCB nº 2.761, com a observação dos 249 dias úteis de 1998. [Link](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf)

---

*Os textos publicados na Syntaxis expressam exclusivamente minhas opiniões pessoais, formadas a partir da minha experiência profissional, e não representam a posição de meu empregador atual ou de empregadores anteriores. O conteúdo tem finalidade educacional e informativa: não constitui recomendação de investimento, análise de valores mobiliários ou consultoria financeira.*
