# Etapa 3 — Pesquisa

Laudo do agente `pesquisador-editorial`, gravado pelo pipeline principal. Fontes acessadas em
**02/11/2026**, salvo indicação. Reaproveita `posts/2026-10-30-du252-contagem-de-dias/processo/03-pesquisa.md`
("du252/03") e `07-verificacao.md` ("du252/07"). Legenda: **[C]** confirmado na fonte primária ·
**[CP]** cálculo próprio, a refazer na etapa 7 (feito à mão, sem executar código) · **[V]** não
encontrado → `[VERIFICAR]`.

---

## Achados que mudam o texto

1. **Samanez: nome errado.** O autor é **Carlos Patricio Samanez**, não "José Carlos Samanez". [C]
2. **"Em 1998 o Brasil escolheu o composto" exagera.** O acúmulo da Selic já era composto por dia útil antes de 1998: a Circular BCB 2.347/1993 chama a taxa média de "efetiva-dia", conhecida como "taxa-over"; a fórmula da própria Circular 2.761 eleva um fator diário à potência 252. O que mudou em 1998 foi a **forma de expressão** (ementa da 2.761: "Altera a forma de expressão…"; Garcia 1997, p. 4: "A medida do BC não alterou os princípios da matemática financeira.").
3. **A consistência entre prazos como motivo de 1998 não aparece nas fontes de época.** Garcia (p. 1): as taxas "tornaram-se mensalizadas no Brasil devido à megainflação; nada mais natural, portanto, que voltem a ser cotadas em termos anuais agora que a inflação anual está em um dígito".
4. **Comunicado BCB nº 7.684 existe, de 11/07/2000.** Alcance mais estreito que "estendeu a padronização aos títulos públicos": padroniza a expressão das taxas nas operações do BCB com títulos públicos e na divulgação dos resultados; títulos cambiais ficam fora da regra anual base 252.
5. **A Circular 2.761 foi revogada integralmente** pela Resolução BCB nº 157/2021 (efeito a partir de 01/12/2021). Nenhuma frase pode sugerir que segue vigente.
6. **"Existe um mercado inteiro na B3 que pagaria exatamente isso [R$ 70 mil]" não confere.** O cupom cambial é linear base 360 por dias corridos (seis meses civis = 181 a 184 dc), e é juro em dólar. R$ 1 mi × 14% × dc/360 = R$ 70.000,00 só com dc = 180 [CP]; 181 → R$ 70.388,89; 182 → R$ 70.777,78; 184 → R$ 71.555,56.
7. **Susep em parte desatualizada.** O exemplo linkado (base 30/12/2010) usa a curva de cupom de IPCA, que hoje a Susep copia da ANBIMA. A taxa contínua vale para as curvas que a Susep estima com método próprio (prefixada, IGP-M, TR, dólar; relatório de jun/2022). Convém trocar o link.
8. **Desigualdade de Bernoulli: o enunciado clássico vai na direção oposta** ((1+x)^r ≥ 1+rx para r ≥ 1). O texto usa a versão para 0 ≤ r ≤ 1: (1+x)^r ≤ 1+rx. Nomear "para expoente entre 0 e 1".

---

## Abertura (R$ 1 mi, 14%, 126 du)

- 1,14^(126/252) = √1,14 = 1,0677078 → **R$ 67.707,83**; 70.000 − 67.707,83 = **R$ 2.292,17** [CP] ✓.
- CDB prefixado em DU/252 composto é padrão, não regra (correção O-2 do du252/07: Caderno de Fórmulas B3 aceita DC/360, DC/365, meses×21/×30, todos compostos). Não dizer "todo CDB".
- "Mercado inteiro na B3 que pagaria exatamente isso": ver achado 6. Fato verificável: DDI e FRC são lineares, base 360, dias corridos.
- "Há quase trinta anos": 01/01/1998 a 02/11/2026 = 28 anos e 10 meses ✓.

## A versão que se aprende cedo (Mito)

**Einstein e a "oitava maravilha" [C, nenhuma fonte primária a favor de Einstein]:**
- Quote Investigator, "The Eighth Wonder of the World Is Compound Interest" (09/09/2019, atualizado em 27/06/2025): https://quoteinvestigator.com/2019/09/09/interest/ — primeira ocorrência: anúncio da Equity Savings & Loan Co. no *Cleveland Plain Dealer*, 1925, sem atribuição; primeira atribuição a Einstein: 1988, *Courier-Post* (Camden, NJ); *The Ultimate Quotable Einstein* a põe em "Probably Not By Einstein".
- Variante "maior invenção": https://quoteinvestigator.com/2011/10/31/compound-interest/ — primeira atribuição em 25/08/1976, *Wall Street Journal*; conclusão "very unlikely that Einstein made this remark".
- A ressalva do rascunho ("sem fonte que a sustente") se sustenta. Fonte, se precisar: Quote Investigator 2019.

**"Juro simples é coisa de agiota" (contraponto):** no Direito brasileiro, o padrão histórico é o simples — Decreto 22.626/1933 (Lei de Usura), art. 4º, proíbe "contar juros dos juros"; Súmula 121 do STF; o composto entrou como exceção do sistema financeiro (Súmula 596 do STF; MP 2.170-36/2001, art. 5º; Súmulas 539 e 541 do STJ). Fontes só secundárias (Planalto bloqueado para a ferramenta): https://barbieriadvogados.com/?p=8786 ; https://jus.com.br/artigos/65835/historico-conciso-da-capitalizacao-de-juros-no-brasil . **[V]** para o literal. A estrutura deixa o jurídico fora; registro como ironia possível ("agiota" é quem a Lei de Usura mirava).

## Anatomia (três regimes + prazo quebrado)

| Conta [CP] | Resultado |
|---|---|
| ln(1,14) | 0,131028 → 13,10% ✓ |
| e^0,14 | 1,150274 → 15,03% ✓ |
| Convenção linear, 1,5 ano: 1,14 × 1,07 | 1,2198 → R$ 219.800,00 ✓ |
| Convenção exponencial, 1,5 ano: 1,14^1,5 | 1,2171869 → R$ 217.186,92 ✓ |
| Diferença | R$ 2.613,08 ✓ |

**"Para quase toda a renda fixa em reais, t = du/252":** Selic (Res. BCB 46/2020, art. 2º), LTN (ANBIMA, *Metodologias de Precificação*, 05/05/2021, p. 35), DI1 (OC 055/2024-PRE) — todos du252/07; Taxa DI: B3, Glossário DI Over (15/12/2025, rev. mar/2026): "A Taxa DI é apurada de forma exponencial, por meio de fator diário de capitalização, considerando um ano padrão de 252 dias úteis" — https://www.b3.com.br/data/files/6A/F7/3F/35/2654D9101BEEB2D9AC094EA8/Glossario_Taxas_DI_Over_balcao%204.pdf [C]. "Quase toda" defensável. **"A imensa maioria das debêntures": [V]**, sem estatística ANBIMA/B3.

**"Lá fora, dias corridos sobre 360 ou 365":** Hull, cap. 6 (via slides; du252/03 §8); tabela 360/365/252 do treinamento B3 [C, derivada].

**Convenção linear (mista) em norma vigente [C]:** a fórmula oficial de preço dos leilões do Tesouro americano usa a convenção linear para o período fracionário — 31 CFR Part 356, App. B, Seção II.A: P[1 + (r/s)(i/2)] = (C/2)(r/s) + (C/2)a_n + 100v_n (r = dias até o primeiro cupom, s = dias do semestre). É a M_linear do rascunho. https://www.law.cornell.edu/cfr/text/31/appendix-B_to_part_356 (lido via resumo; etapa 7 confere o literal). "Street convention" compondo a fração: **[V]**.

## Quem escolhe o motor, e por quê

- 1,07 × 1,07 = 1,1449; 1,14^0,5 × 1,14^0,5 = 1,14 [CP] ✓.
- Consistência entre prazos como propriedade: consenso de livro-texto (fator(t₁+t₂) = fator(t₁)·fator(t₂)). Nenhuma fonte primária a dá como **motivo** do BCB em 1998.
- ANBIMA [C]: a ETTJ parte de "o preço de um título de renda fixa é igual ao fluxo de caixa futuro prometido pelo emissor, trazido a valor presente por uma função desconto", única para todos os prazos (*ETTJ Estimada e Inflação Implícita — Metodologia*, ago/2021, p. 3). Sustenta "montar uma curva inteira sem que um prazo contradiga o outro" como prática atual, não como motivo histórico.

## A virada de 1998

**[VERIFICAR] taxa over mensal (diária × 30):**
- Circular BCB 2.347, de 28/07/1993 [C], art. 1º §1º: "A TAXA MÉDIA A SER INFORMADA É A 'EFETIVA-DIA', CONHECIDA COMO 'TAXA - OVER'". Não fala em "× 30" nem "ao mês". Revogada pela Circular 2.720/1996. https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Circular&p2=2347
- Assaf Neto define "taxa nominal over" (a.m.o.) como diária × 30, mas os trechos só apareceram em reproduções não autorizadas: não servem de fonte. **[V]**, conferir em exemplar.
- Secundária [C]: Bússola do Investidor, "Taxa over": "costuma ser expressa ao mês, obtida pela simples multiplicação da taxa ao dia por 30". https://www.bussoladoinvestidor.com.br/abc_do_investidor/taxa-over/
- Eco jurisprudencial [C]: STJ, REsp 1.826.463/SC, 2ª Seção, j. 14/10/2020, Informativo 682: "A previsão de taxa efetiva mensal superior 30 vezes a taxa diária denotaria a existência capitalização diária". https://informativos.trilhante.com.br/julgados/stj-resp-1826463-sc (resumo).
- Nenhuma norma do BCB anterior a 1998 manda expressar a Selic ao mês como diária × 30. **Recomendação:** manter `[VERIFICAR]` ou trocar pela formulação de Garcia, "as taxas tinham sido mensalizadas".

**Circular BCB 2.761 [C, via API do BCB]:** 18/06/1997; ementa "Altera a forma de expressão da taxa média ajustada dos financiamentos apurados no [SELIC]…"; art. 1º: Selic "expressa sob a forma anual", fórmula eleva a média dos fatores diários à potência 252; art. 2º: TBC e TBAN "na forma de taxa efetiva anualizada… 252 dias úteis"; art. 4º: "surtindo efeito a partir de 01.01.98" (a Circular 2.780/1997 fixou 02/01/1998; nuance P-3 do du252/07). Revogada: art. 1º pela Circular 3.671/2013; integralmente pela Res. BCB 157/2021. https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Circular&p2=2761 ; https://www.bcb.gov.br/pre/normativos/circ/1997/pdf/circ_2761_v1_o.pdf . "Junho de 1997" ✓; "1º de janeiro de 1998" ✓ com a nuance.

**Garcia: fevereiro × julho é dele, literal [C].** *Efeitos da anualização da taxa Selic*, Depto. de Economia–PUC-Rio, 30/06/1997, 6 p.
- p. 2: "Fixando-se a taxa por dia útil para todo o ano de 1998… Fevereiro, com apenas 18 dias úteis, teria uma taxa de 1,42%; enquanto julho, com 23 dias úteis, teria uma taxa de 1,82%. A diferença é de 40 pontos-base, ou cerca de 25% da taxa mensal".
- Premissa omitida no rascunho: 21,84% a.a. (≡ 1,66% a.m., forward do DI futuro para out/1997 em 27/06/1997) → 0,0784% por dia útil.
- p. 3: "tal volatilidade é mero fruto da variação do número de dias úteis em cada mês, ou seja, estritamente, não se trata de volatilidade". A paráfrase do rascunho é fiel.
- p. 5, Conclusão: "O espírito da medida do BC é precisamente o de afirmar a irrelevância das variações de curto prazo. O que importaria numa economia estabilizada são as taxas de mais longo prazo." É o mais próximo de um porquê de época, e não é o argumento de consistência entre prazos.

**Calendário de 1998 [CP]:** fevereiro 18 du (20 dias de semana − Carnaval 23–24/02) ✓; julho 23 du ✓.
**Taxas de Garcia [CP]:** 1,0166^12 = 1,2184; 1,2184^(1/252) − 1 = 0,0784%; 1,000784^18 − 1 = 1,42%; ^23 − 1 = 1,82% ✓. Ilustração possível: na convenção over × 30, a mesma diária seria 2,35% a.m. over, contra 1,66% efetivos num mês de 21 du.

**Comunicado BCB nº 7.684 [C parcial]:** índice oficial do BCB: 11/07/2000, DEMAB, "Comunica a adoção de padrão para a expressão de taxas de juros", não revogado. https://www.bcb.gov.br/api/search/app/normativos/buscanormativos?querytext=ContentType:normativo%20AND%20contentSource:normativos%20AND%20NumeroOWSNMBR:7684&rowlimit=15&startrow=0 . Texto integral não veio pela API; trechos: "no sentido de estabelecer uma padronização para a expressão das taxas de juros"; "em suas operações de compra e venda de títulos públicos"; "divulgar, simultaneamente ao resultado expresso em preço e/ou cotação, a taxa de juros correspondente"; "I - títulos com valor nominal atualizado pela variação da cotação do dólar… como percentual do valor nominal atualizado"; "II - demais títulos… taxa efetiva anual (i), considerando-se 252 dias úteis para o ano". Formulação sustentada: "às operações do BC com títulos públicos". Etapa 7: abrir https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Comunicado&numero=7684 .

**Contraponto central à tese "a régua que não se contradiz" como motivo de 1998:** motivo declarado por Garcia = inflação baixa, volta à cotação anual, irrelevância do curto prazo; o BC só diz "altera a forma de expressão"; o composto já existia (Garcia converte mensal↔anual de forma composta; forward do DI futuro como razão de PUs; Circular 2.347/1993 "efetiva-dia"). O que a consistência explica de fato: a troca de uma **expressão nominal** (over mensal, linear sobre a diária) por uma **expressão efetiva** (anual, exponencial). **O 252 é anterior a 1998:** Circular 2.347/1993, art. 5º ("dividindo-se o número de dias corridos da operação por 365 e multiplicando-se o resultado por 252") [C].

## Onde o linear sobrevive

- **Cupom cambial [C, du252/07]:** DDI "Taxa de juro, expressa em percentual ao ano, linear, base 360 dias corridos" (https://b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/futuro-de-cupom-cambial-de-depositos-interfinanceiros-de-um-dia.htm); FRC "linear, base 360 dias corridos" (https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/operacoes-estruturadas-de-forward-rate-agreement-de-cupom-cambial.htm). Glosa P-9 do du252/07: "o rendimento em dólares para estrangeiros que assumem o risco de investir no Brasil". **"Sempre foram rateados de forma proporcional": [V]** para "sempre"; apoio: Hull cap. 6 (Actual/360); Garcia p. 4.
- **Treasuries, accrued linear [C]:** 31 CFR 356, App. B, Seção I.D (daily interest decimal × dias) e I.A.2 ("actual number of calendar days in the half-year"); exemplo oficial: nota de 6¾%, 92 de 184 dias → $16,875 por $1.000 (= 92/184 × 33,75).
- **Resolução CMN nº 5.171/2024 [C, PDF lido na íntegra]:** 29/08/2024; ementa: metodologia da taxa legal do art. 406 do CC; base: art. 406, §2º. **Art. 6º, literal:** "O regime de juros simples se aplica à taxa legal para fins de acumulação de taxas mensais e de apuração de juros proporcionais (fração *pro rata*)." Parágrafo único: juro diário = taxa legal do mês ÷ dias corridos do mês, × dias corridos a apropriar. **O rascunho está certo e subdimensionado:** o simples vale também na acumulação entre meses. Ironia: a taxa legal mensal é TL = max[Fator Selic/Fator IPCA − 1; 0] (art. 2º), e o Fator Selic é produtório de (1 + Selic)^(1/252) (arts. 3º–4º): composto dentro do mês, simples entre meses e na fração. https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolução5171.pdf
- **Art. 406 do CC (Lei 14.905/2024) [C secundária]:** §1º taxa legal = Selic − IPCA; §2º delega ao CMN; §3º negativo vale zero. Via https://rbdcivil.ibdcivil.org.br/rbdc/article/download/1118/690/2957 e https://www.felsberg.com.br/lei-federal-disciplina-correcao-monetaria-e-a-taxa-legal-de-juros/ . Etapa 7 confere no Planalto. STJ Tema 1368: **[V]** se citado.

## E o contínuo

- **ANBIMA [C]:** *ETTJ Estimada e Inflação Implícita — Metodologia*, ago/2021 (https://www.anbima.com.br/data/files/9A/F4/E3/1F/4805B710B0F024B7882BA2A8/est-termo_metodologia_v2021.pdf): p. 3, T "em anos (dias úteis/252)", "função desconto discreta… b_t(T) = 1/(1 + r_t(T))^T"; p. 4, Svensson (1994). O rascunho está correto.
- **Susep [C, ressalva de atualidade]:** exemplo de 2010 (link do rascunho) é curva de cupom de IPCA — p. 1 Svensson em "taxa à vista anual composta continuamente"; p. 3 R = exp(y) − 1; p. 4 desconto por (1 + R)^(−du/252). Relatório Técnico de 23/06/2022, *Novo Método de Estimação das ETTJ divulgadas pela Susep* (https://www.gov.br/susep/pt-br/arquivos/arquivos-solvencia-supervisao-prudencial/capital-minimo-requerido-e-tap/relatorio-ettj-novo-metodo-20220623.pdf/@@download/file): p. 5, novo método para prefixada, IGP-M, TR e dólar; IPCA segue a da ANBIMA; p. 14–16 Svensson "para taxas à vista compostas continuamente". Conversão para discreta no relatório de 2022: **[V]**. Formulação sustentada: "a Susep estima as curvas prefixada, de IGP-M, de TR e de dólar pelo Svensson em taxa contínua".
- **Black-Scholes e gregas no contínuo:** consenso de livro-texto (Hull, cap. 4); literal **[V]**.

## A barriga da curva (Ponto Cego)

- Máximo de 1 + it − (1+i)^t onde (1+i)^t = i/ln(1+i) = 1,06847 → t = 0,5055 ano, "perto de seis meses" ✓ [CP]. Em t = 0,5: 1.070,00 × 1.067,71 ✓.
- Contínua com a taxa cotada acima das duas para todo t > 0 (e^x ≥ 1 + x; e^0,14 > 1,14) ✓. "O tempo todo" vale para t > 0.
- Bernoulli: ver achado 8. Apoio: https://en.wikipedia.org/wiki/Bernoulli%27s_inequality .
- **"Barriga da curva" como jargão [C de uso]:** Reuters via Forbes Brasil, 09/02/2022: DI subindo "sobretudo na 'barriga' da curva" (https://forbes.com.br/forbes-money/2022/02/dis-seguem-marcha-de-alta-e-taxas-a-termo-apontam-selic-media-de-128-no-comeco-de-2023/); termos próximos: "miolo da curva", "vértices intermediários" (https://www.dgabc.com.br/Noticia/4340831/no-mercado-de-juros-dis-intermediarios-e-longos-sobem-com-risco-fiscal-eleitoral). Nenhum glossário B3/ANBIMA/BCB com o verbete. Ponte possível: ANBIMA (p. 4) chama β₃ e β₄ do Svensson de "componentes de médio prazo"; Susep, "fatores de médio prazo".
- 14% × 365/360 = 14,194% → 14,19% ✓ [CP]; slides de Hull: "the interest earned in an entire year is 365/360 times the quoted rate".

## A bola de neve demora a rolar

- 1,14² = 1,2996 → juro R$ 299,60 = linear R$ 280,00 + juro sobre juro R$ 19,60 ✓ [CP].
- Virada ((1+i)^t = 1 + 2it): 14% ≈ 10,42 anos ✓; 12% ≈ 11,92 anos ✓ (R$ 3.860,8); 6% entre 22 e 23 anos ("mais de duas" décadas ✓); 10% a calcular na etapa 7.
- Gráficos: cálculo do autor, rotular assim.

## Três perguntas (Prateleira)

- 1 + 0,14 × 91/360 = 1,0353889; ^4 = 1,1492487 → 14,92% ✓ [CP]. "91 dc contendo 63 du" depende das datas; etapa 7 decide se fixa datas ou deixa "por exemplo".
- B3, Treinamento DI, módulo 02 [C]: "um ano de 252 dias úteis composto por 12 meses de 21 dias úteis"; bases 360/365/252. https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/s_di_train_prog/02-taxas-de-juros.htm
- **`DIATRABALHOTOTAL − 1`** (du252/07: liquidação inclusive, vencimento exclusive; calendário ANBIMA 2001–2099): o "−1" só bate com [início, fim) **quando as duas pontas são dias úteis**. Se a data final for feriado, a função já não a conta e o "−1" tira um dia a mais. Sintaxe pt-BR: etapa 7.

## Fechamento (teste de transferência)

- 1,01^12 − 1 = 12,68% ✓ [CP].
- Âncora jurídica opcional [C secundária]: Súmula 541 do STJ (taxa anual superior ao duodécuplo da mensal basta para cobrar a efetiva anual) — https://arquivocidadao.stj.jus.br/index.php/sumula-541-2 ; Súmula 539. Uso opcional.

## Para continuar aprendendo (edições)

| Item | Dados conferidos | Situação |
|---|---|---|
| Alexandre Assaf Neto, *Matemática Financeira e suas Aplicações* | 15ª ed., GEN Atlas, 2022, ISBN 9786559773237 (https://www.martinsfontespaulista.com.br/matematica-financeira-e-suas-aplicacoes-1004941/p) | [C]. Cobertura capítulo a capítulo: [V]. |
| **Carlos Patricio** Samanez, *Matemática Financeira* | 5ª ed., Pearson Prentice Hall, 2010, ISBN 9788576057994 (https://biblioteca.ifac.edu.br//bib/33168) | [C]. **Nome errado no rascunho.** "Mais exercícios de taxas equivalentes e nominais": [V]. |
| John C. Hull, *Options, Futures, and Other Derivatives* | 11ª ed., Pearson, 2021 (© 2022), ISBN 9780136939979; cap. 4 "Interest rates", cap. 6 "Interest rate futures" (https://www.pearson.com/store/p/options-futures-and-other-derivatives/P200000005938/9780136939979) | [C]. Sem conflito com o du252 (cap. 6 = day count; cap. 4 = capitalização). |
| Márcio G. P. Garcia | *Efeitos da anualização da taxa Selic*, PUC-Rio, 30/06/1997 | [C]. Acrescentar o título. |

## Contrapontos (consolidado)

1. 1998 não trocou regime de acúmulo; trocou forma de expressão (nominal over mensal → efetiva anual exponencial).
2. A consistência como motivo é inferência, não registro histórico. Ironia: a régua nova "se contradiz" no mês (1,42% × 1,82%); a consistência é entre prazos medidos em du, não entre meses civis.
3. Linear não é "errado" (DDI/FRC, Treasury, CMN 5.171): pesa contra o CTA "quem ainda divide a taxa anual por doze".
4. O 252 é anterior a 1998 (Circular 2.347/1993, art. 5º).

## O que ninguém está dizendo (candidatos)

1. **A taxa legal de 2024 está dos dois lados da barriga, por lei.** Simples na fração (15 dias de atraso → paga mais que no composto) e simples entre meses (muitos meses → paga menos). [C norma; leitura CP]
2. **O Tesouro americano usa a convenção linear do prazo quebrado na fórmula oficial de leilão** (31 CFR 356, App. B, II.A). [C, conferir literal]
3. **Um regulador, três réguas:** a Susep toma DI×PRÉ (exponencial 252) e FRC (linear 360) e estima ambos em contínua (relatório 2022, p. 12–16). [C]
4. **A over nasceu "efetiva-dia"** (Circular 2.347/1993); o "× 30" era embalagem, e o STJ ainda a usa como teste de capitalização diária (REsp 1.826.463/SC). [C; × 30 só em secundária]
5. **No Direito, o padrão histórico é o simples** (Lei de Usura; Súmula 121 do STF). [secundária, [V] literal]

## Descartado

Juros de mora federais (Selic "acumulada mensalmente", Lei 9.430/1996, art. 61): se é soma simples não foi confirmado em fonte primária. Não usar.

## Pendências `[VERIFICAR]`

1. Taxa over "diária × 30" antes de 1998 (sem livro-texto legítimo nem norma).
2. Comunicado 7.684: texto integral.
3. Art. 4º do Decreto 22.626/1933 e art. 406 do CC: literal no Planalto.
4. "Imensa maioria das debêntures" em DU/252: sem dado.
5. "Sempre foram rateados de forma proporcional": sem fonte para "sempre".
6. Cobertura de Samanez e Assaf Neto; título da seção de capitalização contínua no cap. 4 de Hull.
7. Susep 2022: conversão contínua → discreta (p. 17–37).
8. Street convention × Treasury convention na fração.

PDFs baixados ficaram fora do repositório (diretório de resultados de ferramenta da sessão).
