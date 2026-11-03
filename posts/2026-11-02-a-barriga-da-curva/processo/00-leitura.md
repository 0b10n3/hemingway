# Etapa 0 — Leitura do rascunho

Fonte: `_arquivo/drafts/2026-11-02_A_Barriga_da_Curva.md` (intocado; commitado em `main` em `fbb8ee4`).

**Front-matter:** ausente. O arquivo abre direto com o H1 "# Notas de um Professor — A Barriga
da Curva \[draft v1\]", seguido de "Nov 2, 2026 · @0b10n3" (cabeçalho de exportação).

**Linha editorial:** sem campo `linha_editorial`; o pipeline parou e perguntou. **Autor confirmou
Notas de um Professor (2026-11-02).** Consequências: a etapa 2 preenche a Ficha de Saída
(`docs/BACKWARDS_DESIGN.md` §2), a etapa 5 roda sem validação argumentativa e a 5a não roda.

**Título e slug:** título "A Barriga da Curva" (o prefixo "Notas de um Professor —" é a linha, não
o título). Subtítulo provisório: "Juro simples, composto e contínuo além dos livros". Slug:
`2026-11-02-a-barriga-da-curva`.

**Autoria — tensão resolvida nesta etapa.** As "Notas de processo" do próprio rascunho dizem:
"O anexo trouxe só a pesquisa de pauta; nenhum rascunho autoral veio junto. O draft segue o
roteiro da pesquisa encaixado nos movimentos da linha editorial". O texto não foi escrito pelo
autor. **Autor decidiu: tratar como rascunho (2026-11-02).** Consequência para a etapa 4: a
revisão de voz contra `estilo/estilo-autoral.md` pesa mais que o normal, sem reordenar a
argumentação; trecho que pede memória ou opinião própria vira `[PREENCHER: …]`, nunca é inventado.

**Continuidade de série — tensão resolvida nesta etapa.** O post
`2026-10-30-du252-contagem-de-dias` (aprovado em 30/10) já explica a origem do 252 (Circular
2.761, Garcia), já separa régua (contagem) de motor (linear/composto), já usa "O problema do
professor é que ele esquece que foi aluno" e fecha com "O próximo volta à série de crédito com o
FIDC". Este rascunho abre com "Nunca expliquei de onde ele vem" e "antes do FIDC". **Autor
decidiu: reenquadrar (2026-11-02)** — a abertura vira continuação do du252 (aquele explicou o
du, este explica por que o expoente/regime), sai a frase repetida, a ponte para o FIDC é
ajustada. Etapa 1 fixa o ângulo, etapa 4 escreve com nota lateral.

**Natureza do rascunho:** completo e já com verificação parcial feita pelo montador: abertura com
cálculo-gancho (R$ 1 mi, 14%, 126 du), sete seções, seis blocos LaTeX, um bloco de fórmulas de
planilha, dois visuais (`graf-01` descrito; `graf-02` como "embedded content" não incluído no
arquivo), bibliografia comentada de quatro itens, e uma seção "Notas de processo (não publicar)"
com tabela de correções à pesquisa, cinco pendências, plano de visuais e fontes consultadas.

**Limpeza aplicada na cópia:** `&#91;` → `[`; `\[`/`\]` → `[`/`]`; removido um `## ` vazio
logo depois do cabeçalho de exportação. Nada mais mudou.

**Observações de formato para etapas posteriores** (não são marcadores do autor):
- Seis fórmulas em bloco ` ```latex `. A Substack tem bloco LaTeX nativo; a etapa 2/9 decide.
- Bloco de planilha com `DIATRABALHOTOTAL` — etapa 7 confere a sintaxe pt-BR do Excel/Sheets e o
  "-1".
- Corpo publicável: ~2.300 palavras até "Para continuar aprendendo" (estimativa; o arquivo tem
  ~3.000 com as notas de processo).

---

## Cópia de trabalho (verbatim, com a limpeza acima)

# Notas de um Professor — A Barriga da Curva [draft v1]

Nov 2, 2026 · @0b10n3


Subtítulo provisório: Juro simples, composto e contínuo além dos livros

Nos últimos textos desta série, a mesma conta apareceu várias vezes. Na LCA (Letra de Crédito do Agronegócio), para achar a taxa em que um CDB empata com ela depois do imposto. Na debênture, para converter percentual do CDI em CDI mais spread e para estimar quanto o PU (preço unitário, o valor de mercado de cada título) cai quando o spread do devedor abre.

Em todas elas havia um expoente: du/252.

Nunca expliquei de onde ele vem.

Esta linha editorial nasceu de uma frase que repito para mim mesmo: o problema do professor é que ele esquece que foi aluno. Esqueci.

Então, antes do FIDC, uma pergunta que parece de primeiro período da faculdade.

Você aplica R$ 1 milhão a 14% ao ano por seis meses, ou 126 dias úteis. Quanto rende?

Se a sua resposta foi R$ 70 mil, você acertou. Existe um mercado inteiro na B3 que pagaria exatamente isso.

E você errou. Num CDB prefixado à mesma taxa, o rendimento é de R$ 67.707,83.

A diferença, R$ 2.292,17, não é arredondamento. É a distância entre duas réguas.

A régua que o mercado brasileiro adotou por norma, há quase trinta anos, é justamente a que paga menos em seis meses. Por quê? E o que isso muda na hora de ler qualquer taxa que alguém coloca na sua frente?

## A versão que se aprende cedo

A história costuma ser contada assim. Juro simples é coisa de livro escolar e de agiota de bairro. Juro composto é o regime dos profissionais, a 'bola de neve', a força que uma frase atribuída a Einstein, sem fonte que a sustente, chamaria de oitava maravilha do mundo.

Então o composto rende mais. Sempre. E começa a trabalhar desde o primeiro dia.

As duas afirmações são falsas. A primeira, entre zero e um período. A segunda, por mais tempo do que quase todo mundo imagina.

Capitalização não é lei da natureza. É cláusula.

## Três réguas para o mesmo tempo

Um regime de capitalização é a regra que diz o que acontece com o juro de cada período: se ele fica parado ao lado do capital ou se passa a render junto. Nas três fórmulas abaixo, C é o capital, M o montante (capital mais juros), i a taxa por período e t o prazo medido em períodos da própria taxa.

Na capitalização simples, ou regime linear, o juro incide só sobre o capital inicial. O montante cresce em progressão aritmética, uma reta:

```latex
M = C\,(1 + i\,t)
```

Na capitalização composta, ou regime exponencial, o juro de cada período se incorpora ao saldo e passa a render no período seguinte. É o 'juro sobre juro', que o Direito chama de anatocismo. O montante cresce em progressão geométrica:

```latex
M = C\,(1 + i)^{t}
```

Na capitalização contínua, o juro é reinvestido a cada instante, como se o número de capitalizações por período tendesse ao infinito. Entra a constante de Euler, e ≈ 2,71828, e uma taxa instantânea r:

```latex
M = C\,e^{r\,t}, \qquad r = \ln(1 + i)
```

A segunda igualdade importa. Com r = ln(1,14) = 13,10%, a régua contínua dá exatamente o mesmo montante que 14% compostos. Quem aplica e elevado a 0,14 vezes t, usando o número cotado como se fosse taxa instantânea, está calculando 15,03% ao ano sem perceber.

Resta medir t. No Brasil, para quase toda a renda fixa em reais, t = du/252: dias úteis do período sobre um ano convencional de 252 dias úteis. É o expoente dos textos anteriores. Lá fora, o mais comum é contar dias corridos sobre 360 ou 365.

### O prazo quebrado

Quando o prazo tem uma parte inteira n e uma fração f de período, há duas formas de fechar a conta dentro do regime composto. A convenção linear, ou mista, compõe a parte inteira e aplica juro simples na fração. A convenção exponencial compõe tudo:

```latex
M_{\text{linear}} = C\,(1 + i)^{n}\,(1 + i\,f) \qquad M_{\text{exponencial}} = C\,(1 + i)^{n + f}
```

R$ 1 milhão a 14% ao ano por um ano e meio: R$ 219.800,00 de juros pela convenção linear, R$ 217.186,92 pela exponencial. A fração vale R$ 2.613,08 para um dos lados do contrato.

Até aqui, é o segundo capítulo de qualquer livro de matemática financeira. O interessante começa quando se pergunta por que cada mercado escolheu a sua régua.

## Quem escolhe a régua, e por quê

Cada régua embute uma hipótese. A linear supõe que o juro fica parado até o fim do período. A composta supõe que ele é reinvestido à mesma taxa. Para quem cota juros para muitos prazos ao mesmo tempo, essa diferença não é filosófica.

Volte ao exemplo da abertura. A 14% ao ano no regime linear, quem aplica por seis meses e renova por mais seis termina o ano com um fator de 1,07 × 1,07 = 1,1449. Rendeu 14,49%, contra 14% de quem aplicou direto por um ano, à mesma taxa cotada.

Uma taxa linear única não consegue valer para todos os prazos ao mesmo tempo. Fatiar o prazo vira estratégia.

No regime composto, o fatiamento não muda nada: 1,14 elevado a 0,5, vezes 1,14 elevado a 0,5, dá 1,14. Aplicar por 63 dias úteis e reaplicar por mais 63 gera o mesmo fator que aplicar por 126. É essa propriedade que permite montar uma curva de juros inteira, do overnight ao título de dez anos, sem que um prazo contradiga o outro.

### A virada de 1998

O Brasil chegou a essa régua por decisão do regulador, não por gosto acadêmico. Com a inflação alta, as taxas do mercado de um dia tinham sido 'mensalizadas': cotava-se a taxa over ao mês [VERIFICAR: convenção da taxa over mensal como taxa por dia útil × 30, com fonte de livro-texto].

A Circular BCB nº 2.761, divulgada em junho de 1997, mudou isso: a partir de 1º de janeiro de 1998, a taxa Selic passou a ser expressa ao ano, com base em 252 dias úteis. Num texto da época, o economista Márcio Garcia, da PUC-Rio, apontou um efeito colateral curioso. Com a mesma taxa por dia útil, fevereiro de 1998, com 18 dias úteis, renderia 1,42% no mês; julho, com 23, renderia 1,82%. Quarenta pontos-base de diferença que pareciam volatilidade e eram só calendário.

Em 2000, o Comunicado BCB nº 7.684 estendeu a padronização aos títulos públicos, com a taxa expressa como taxa efetiva anual em base 252 [VERIFICAR: data e alcance exatos do Comunicado 7.684]. Hoje, Taxa DI, LTN, NTN-B, LFT, contrato futuro de DI, CDB e a imensa maioria das debêntures falam essa língua.

### Onde o linear sobrevive

O regime linear não morreu. Ele ficou onde resolve melhor o problema de quem cota.

No cupom cambial, a taxa de juro em dólar negociada no Brasil, os contratos futuros da B3 (DDI) e o FRC, sua operação a termo, são cotados em taxa linear ao ano, base 360 dias corridos. É a língua do mercado monetário internacional em dólar, onde depósitos de curto prazo sempre foram rateados de forma proporcional ao tempo.

Nos títulos do Tesouro americano, o juro acumulado entre dois pagamentos de cupom, o que o comprador paga ao vendedor pelos dias já corridos, também é apropriado de forma linear.

E há um caso recente, aqui mesmo. Em 2024, a Resolução CMN nº 5.171 definiu o cálculo da taxa legal, a que corrige uma dívida civil quando o contrato não fixa juros (art. 406 do Código Civil). O art. 6º manda acumulá-la em juros simples, com a fração do mês apropriada por dias corridos.

### E o contínuo

A régua contínua é a dos modelos. Ela torna os retornos aditivos no tempo e deixa o cálculo diferencial trabalhar, e por isso aparece no modelo de Black-Scholes-Merton e no cálculo das 'gregas', as sensibilidades do preço de uma opção. A Susep (Superintendência de Seguros Privados), por exemplo, estima sua estrutura a termo pelo modelo de Svensson em taxa contínua e depois converte para a taxa discreta.

A ANBIMA usa o mesmo modelo de Svensson para a curva que publica todo dia, mas já na régua local: o fator de desconto é 1 sobre (1 + r) elevado ao prazo em anos de 252 dias úteis.

Nenhuma das três réguas é a certa. Cada uma é a que resolve o problema de quem está cotando.

## A barriga da curva

Eis a peça que separa quem decorou as fórmulas de quem as entende.

As duas réguas passam pelos mesmos dois pontos. Em t = 0, as duas valem C. Em t = 1, as duas valem C vezes (1 + i): no fim do primeiro período ainda não há juro anterior para render juro.

Entre esses dois pontos, a reta do juro simples é a corda de uma curva convexa. E a corda de uma curva convexa passa por cima dela. Para qualquer fração de período, o juro composto rende menos que o simples. Quem fez cálculo reconhece a desigualdade de Bernoulli; quem não fez, pode confiar no desenho.

> [graf-01] Gráfico: montante de R$ 1.000 a 14% ao ano entre zero e dois anos, em três réguas: a reta do juro simples, a curva do juro composto e, tracejada, a contínua com a taxa cotada usada como instantânea. Entre zero e um ano, a reta fica acima da curva composta, com a maior distância perto de seis meses (R$ 1.070,00 contra R$ 1.067,71). As duas se encontram em um ano, em R$ 1.140,00, e a curva composta passa por cima da reta dali em diante. A contínua fica acima das duas o tempo todo.

Na prática, isso quer dizer que, com o mesmo número cotado, a régua linear paga mais a quem aplica e cobra mais de quem toma sempre que o prazo é menor que o período da taxa. Seis meses de uma taxa anual. Quinze dias de uma taxa mensal. A fração de mês de uma dívida em atraso.

O contraste com um vizinho deixa isso concreto. Ponha lado a lado um CDB prefixado a 14% ao ano e uma operação cotada a 14% ao ano, linear, base 360. O número na tela é o mesmo. Em seis meses, a operação linear paga mais.

E a base ainda acrescenta uma camada. Num ano civil de 365 dias corridos, 14% ao ano na base 360 rendem 14% × 365/360 = 14,19%. Mesmo em um ano inteiro, o número cotado não é o número recebido.

Por isso a frase "14% ao ano", sozinha, não diz quanto você vai receber. Ela é a metade de uma cláusula.

## A bola de neve demora a rolar

Depois do primeiro período, o composto passa à frente. A pergunta seguinte é quanto do rendimento é, de fato, juro sobre juro.

O montante composto se decompõe em três camadas: o capital; o juro simples sobre o capital, que cresce em linha reta; e o juro sobre juro, a parte que só existe porque o juro anterior foi reinvestido.

```latex
J_{\text{juro sobre juro}} = C\,\left[(1 + i)^{t} - 1 - i\,t\right]
```

Em dois anos a 14% ao ano, R$ 1.000 rendem R$ 299,60. Desses, R$ 280,00 são juro linear. O juro sobre juro responde por R$ 19,60.

[embedded content: cálculo próprio · R$ 1.000 a 6%, 10% e 14% ao ano, juros compostos, prazos de 1 a 30 anos]

A virada, o prazo em que o juro sobre juro passa a valer mais que o juro linear, chega depois de uma década a 14% ao ano. A 6%, uma taxa na ordem de grandeza de um juro real, leva mais de duas.

Quem aplica por dois anos está comprando, essencialmente, juro simples com uma correção pequena. Quem aplica por trinta está comprando outra coisa.

O motor do juro composto não é a taxa. É o tempo.

> [graf-02] No post, este gráfico entra como imagem exportada, com o mesmo título e a mesma fonte.

## Três perguntas antes de qualquer taxa

Como nos textos anteriores, quase todo erro de leitura nasce de misturar três perguntas. Aqui, elas são:

qual é o regime, linear ou exponencial;

qual é a base, 252, 360 ou 365;

que dias contam, os úteis ou os corridos.

Com as três respondidas, duas taxas de réguas diferentes viram comparáveis. Basta igualar os fatores do mesmo período:

```latex
(1 + i_{252})^{du/252} = 1 + i_{360}\,\frac{dc}{360}
```

Uma operação de 91 dias corridos, que no calendário contém 63 dias úteis, cotada a 14% ao ano linear base 360, tem fator de 1 + 0,14 × 91/360 = 1,035389. Na régua brasileira, isso equivale a 1,035389 elevado a 252/63, menos 1: 14,92% ao ano. O mesmo "14%" virou quase 15%.

Na planilha, as quatro contas que resolvem quase tudo:

```
Fator exponencial 252:     =(1+i)^(du/252)
Fator linear 360:          =1+i*dc/360
Linear 360 → exponencial:  =(1+i_lin*dc/360)^(252/du)-1
Dias úteis entre datas:    =DIATRABALHOTOTAL(início;fim;feriados)-1
```

O "menos 1" da última linha existe porque a função conta as duas pontas, e o mercado conta a data inicial e exclui a final [VERIFICAR: confirmar a convenção de inclusão de datas da ANBIMA e o calendário de feriados a usar].

A quarta conta é a que mais erra na prática. Um calendário de feriados desatualizado muda o du, e o du está no expoente.

## Fechamento: o expoente que faltava

O juro simples ganha do composto em qualquer fração de período. O composto só começa a ganhar depois do primeiro período, e a bola de neve leva anos para valer mais que o juro linear. O que o mercado brasileiro escolheu em 1998 não foi a régua que paga mais. Foi a que não se contradiz de um prazo para o outro.

Capitalização não é lei da natureza. É cláusula.

Se o texto funcionou, você consegue dar o próximo passo sozinho. Pegue um contrato de financiamento que mostre, lado a lado, uma 'taxa nominal' e uma 'taxa efetiva'. Faça as três perguntas. Por que 12% ao ano capitalizados mensalmente viram 12,68% efetivos? E qual dos dois números é o que você de fato paga?

Agora, sim, o FIDC. Com o du/252 explicado, dá para olhar uma carteira de devedores dividida em cotas e perguntar quem recebe primeiro, e quanto isso vale hoje.

Se este texto te ajudou a destravar uma conta que você fazia no automático, encaminhe para quem ainda divide a taxa anual por doze.

## Para continuar aprendendo

Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações* (Atlas) [VERIFICAR: edição e ano] — a referência brasileira para regimes, convenção linear e exponencial em prazos quebrados, taxa over e a decomposição do montante composto usada no gráfico.

José Carlos Samanez, *Matemática Financeira* (Pearson) [VERIFICAR: edição e ano] — tratamento paralelo, com mais exercícios de taxas equivalentes e nominais; bom para o teste de transferência.

John C. Hull, *Options, Futures, and Other Derivatives* (Pearson), cap. 4, "Interest Rates" [VERIFICAR: edição e número do capítulo] — frequência de capitalização, taxa contínua e conversões, na língua do mercado internacional.

Márcio G. P. Garcia, nota sobre a anualização da taxa Selic (PUC-Rio, junho de 1997) — o registro de época da mudança de régua de 1998 e de seus efeitos nas taxas mensais. [link](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf)

## Notas de processo (não publicar)

O anexo trouxe só a pesquisa de pauta; nenhum rascunho autoral veio junto. O draft segue o roteiro da pesquisa encaixado nos movimentos da linha editorial, e todos os números foram recalculados (cálculo próprio, Python).

### Correções à pesquisa de pauta

| Ponto da pesquisa | O que mudou no draft | Por quê |
| --- | --- | --- |
| ETTJ da ANBIMA listada como capitalização contínua | Tratada como Svensson em taxa discreta base 252 | A metodologia da ANBIMA desconta por 1/(1+r)^T, T em anos de 252 du; quem usa taxa contínua e converte é a Susep |
| Exemplo de R$ 20 mil a 21% ao mês | Trocado por R$ 1 milhão a 14% ao ano, 126 du | 21% ao mês não existe na renda fixa brasileira; 14% está perto do CDI de 2026 |
| Decomposição a 12% ao ano (virada em 11,92 anos) | Refeita a 14% (virada em 10,42 anos), com 6% e 10% para comparação | Uma taxa só no texto inteiro; os números da pesquisa a 12% conferem |
| Coluna "contínua" calculada com e^(0,12t) | Texto explica que isso usa a taxa cotada como instantânea | Com r = ln(1+i), contínua e composta dão o mesmo montante; o "teto" só aparece quando se troca a taxa |
| Linha de 11,92 anos: R$ 3.860,80 | R$ 3.860,78 | Arredondamento do prazo na pesquisa; irrelevante, mas registrado |

### Pendências [VERIFICAR]

- Convenção da taxa over mensal antes de 1998 (taxa por dia útil × 30): falta fonte de livro-texto.
- Comunicado BCB nº 7.684: data exata (julho de 2000, pelo que achei) e alcance.
- Convenção de contagem de du (inclui a data inicial, exclui a final) e calendário de feriados.
- Edições e anos de Assaf Neto, Samanez e Hull.
- A frase atribuída a Einstein: mantive como ironia sinalizada; corte se preferir.

### Visuais

- graf-01 (a barriga da curva, 0 a 2 anos): só descrito no texto, falta produzir.
- graf-02 (parcela do juro sobre juro por prazo): desenhado acima, a partir dos próprios dados; exportar para o post.

### Fontes consultadas

- [Márcio G. P. Garcia, nota sobre a anualização da Selic (PUC-Rio, 1997)](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf) — Circular 2.761, base 252 a partir de 1/1/1998, exemplo de fevereiro e julho.
- [B3 — FRC de cupom cambial](https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/operacoes-estruturadas-de-forward-rate-agreement-de-cupom-cambial.htm) — cotação em taxa linear ao ano, base 360 dias corridos.
- [Resolução CMN nº 5.171/2024](https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolução5171.pdf) — art. 6º, taxa legal em juros simples, pro rata por dias corridos.
- [ANBIMA — metodologia da ETTJ](https://www.anbima.com.br/data/files/9A/F4/E3/1F/4805B710B0F024B7882BA2A8/est-termo_metodologia_v2021.pdf) — Svensson, prazo em anos base 252.
- [Susep — exemplo de aplicação da ETTJ](https://www.gov.br/susep/pt-br/arquivos/arquivos-solvencia-supervisao-prudencial/arquivos/2Exemplo_pratico_aplicacao_ETTJ.pdf) — taxa contínua convertida em discreta.

---

## Marcadores extraídos do rascunho

| # | Trecho (verbatim ou resumido) | Classificação | Resolução |
|---|---|---|---|
| 1 | Ausência de front-matter; H1 "Notas de um Professor — A Barriga da Curva \[draft v1\]" | Estrutural | **Resolvido (etapa 0)**: autor confirmou Notas de um Professor (2026-11-02). |
| 2 | "Subtítulo provisório: Juro simples, composto e contínuo além dos livros" | Estrutural | Pendente (etapa 1): fixar ou propor alternativa. |
| 3 | "O anexo trouxe só a pesquisa de pauta; nenhum rascunho autoral veio junto." | Estrutural | **Resolvido (etapa 0)**: tratar como rascunho; etapa 4 pesa a voz (autor, 2026-11-02). |
| 4 | Abertura: "Nunca expliquei de onde ele vem." / "Esta linha editorial nasceu de uma frase que repito para mim mesmo: o problema do professor é que ele esquece que foi aluno. Esqueci." / "Então, antes do FIDC, …" — colide com o du252 | Nota de conteúdo | **Resolvido (etapa 0)**: reenquadrar como continuação do du252 (autor, 2026-11-02). Etapa 1 define o ângulo, etapa 4 escreve. |
| 5 | "a força que uma frase atribuída a Einstein, sem fonte que a sustente, chamaria de oitava maravilha do mundo" + pendência "mantive como ironia sinalizada; corte se preferir" | Nota de conteúdo | Pendente (etapa 1): tensão nomeada — manter ou cortar. |
| 6 | "[VERIFICAR: convenção da taxa over mensal como taxa por dia útil × 30, com fonte de livro-texto]" | Nota de conteúdo | Pendente (etapa 3 levanta, etapa 7 confere). |
| 7 | "[VERIFICAR: data e alcance exatos do Comunicado 7.684]" | Nota de conteúdo | Pendente (etapa 3/7). |
| 8 | "[VERIFICAR: confirmar a convenção de inclusão de datas da ANBIMA e o calendário de feriados a usar]" | Nota de conteúdo | Pendente (etapa 7). O du252 já verificou isso (semântica `(from, to]`); reaproveitar o laudo `posts/2026-10-30-du252-contagem-de-dias/processo/07-verificacao.md`. |
| 9 | "[VERIFICAR: edição e ano]" ×2 (Assaf Neto, Samanez); "[VERIFICAR: edição e número do capítulo]" (Hull, "cap. 4") | Nota de conteúdo | Pendente (etapa 7). Obs.: o du252 aprovado cita Hull "capítulo 6" — conferir consistência. |
| 10 | "> [graf-01] Gráfico: montante de R$ 1.000 a 14% ao ano entre zero e dois anos, em três réguas…" | Sugestão de visual | Pendente (etapa 2 confirma pelo critério; etapa 8 produz). |
| 11 | "[embedded content: cálculo próprio · R$ 1.000 a 6%, 10% e 14% ao ano, juros compostos, prazos de 1 a 30 anos]" + "> [graf-02] No post, este gráfico entra como imagem exportada…" | Sugestão de visual | Pendente (etapa 2/8). O conteúdo embutido não veio no arquivo; a etapa 8 reconstrói a partir da fórmula do juro sobre juro. |
| 12 | Tabela "Correções à pesquisa de pauta" (ANBIMA discreta × Susep contínua; 14% no lugar de 21% a.m.; virada 10,42 anos a 14%; R$ 3.860,78) | Nota de conteúdo | Pendente (etapa 7): reconferir cada correção. |
| 13 | Números do texto: R$ 70.000 × R$ 67.707,83 (Δ 2.292,17); ln(1,14) = 13,10%; e^0,14 → 15,03%; prazo quebrado 219.800,00 × 217.186,92 (Δ 2.613,08); 1,07² = 1,1449; Garcia fev/98 18 du 1,42% × jul/98 23 du 1,82%; 299,60 / 280,00 / 19,60; virada >10 anos a 14%, >20 a 6%; 14%×365/360 = 14,19%; 91 dc/63 du → 1,035389 → 14,92%; 12% a.m.-cap. → 12,68% | Nota de conteúdo | Pendente (etapa 7): recalcular tudo. |
| 14 | Fatos normativos: Circular BCB 2.761 (jun/1997, vigência 1/1/1998); Comunicado 7.684 (2000); DDI/FRC linear base 360; Treasuries com accrued linear; Resolução CMN 5.171/2024 art. 6º e art. 406 do CC; Susep Svensson contínua; ANBIMA ETTJ Svensson base 252 discreta | Nota de conteúdo | Pendente (etapa 3/7, fonte primária). |
| 15 | "Pendências [VERIFICAR]", "Visuais", "Fontes consultadas" (Notas de processo) | Nota de conteúdo | Registro: a seção inteira não vai para `post.md`; pendências entram nos itens #6–#9, visuais nos #10–#11, fontes alimentam a etapa 3. |
