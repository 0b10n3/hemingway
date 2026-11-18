# Etapa 7: Verificação técnica

Executor: subagente `verificador-tecnico`. Texto conferido: corpo de `processo/04-draft-v2.md`, a
partir de "# Cara, eu ganho. Coroa, eu não perco.". Fontes acessadas em 2026-11-18. Os vereditos de
`03-pesquisa.md` foram reaproveitados onde a fonte primária já estava citada; o que pesa foi reaberto.
Registro do cálculo (script, saída e dados de mercado):
`_revisoes/2026-11-18_2026-11-18-cara-eu-ganho-coroa-eu-nao-perco_calculo.md`.

**Placar:** 2 divergências de cálculo bloqueantes (C1, C2), 9 imprecisões (C3 a C11, das quais
C8, C10 e C11 são leves), 1 marcador que pode sair (C12). Nenhum `[VERIFICAR]` e nenhum `[FAIXA]`
pendente. O `[VERIFICAR]` do desmembramento da NTN-F foi fechado com fonte oficial (BCB). Todos os
outros números do texto conferem no recálculo.

## Decisão sobre a convenção do Tesouro (ponto b)

**O exemplo hipotético não deve adotar a convenção do Tesouro.** Motivos:

1. **A cadeia do texto está certa.** Com C = 48,808848 sem arredondar, todos os números conferem até
   o centavo: tabela, PU de R$ 943,88, TIR, dealer, montagem, sobra de R$ 115,18, VP de R$ 302,60 e
   lucro de R$ 20.307,28. O único defeito é de exibição: a coluna de quantidade (C1).
2. **A convenção completa quebra a identidade que o parágrafo ensina.** Com fluxo A-5, PU T-6 e
   valor financeiro T-2, o lucro sai em R$ 20.307,22, e 100.000 × a diferença dá R$ 20.307,24. Os
   R$ 0,02 de truncamento precisariam de explicação no texto.
3. **Ela desalinha a planilha da Prateleira.** O `SOMARPRODUTO` sem `TRUNCAR` daria 943,883953, e a
   tabela daria 943,883952. Para casar as duas, seria preciso pôr `TRUNCAR` na fórmula.
4. **Adotar só metade recria a mistura que o ponto b aponta.** Um exemplo seria fluxo do Tesouro com
   PU sem truncar.
5. **O autor já decidiu "cálculo próprio" na nota lateral 4.** Nada na cadeia do texto está errado a
   ponto de justificar reverter essa decisão.

O custo de não adotar é este: dois dos três PUs de LTN da tabela não batem, na 6ª casa, com a fórmula
`TRUNCAR` que o texto anterior deixou (936,585811 e 874,890638 contra 936,585812 e 874,890639). O aviso
cobre essa diferença se disser "arredondamentos e truncamentos" (C7). Se o autor preferir a
convenção do Tesouro, a cadeia inteira está pronta em C1-alt.

**O par da abertura e do exemplo fica coerente.** A abertura dá o valor real para um título:
1.000 + trunc₂(48,808850) = R$ 1.048,80 (Tesouro, Tabela 3; ENAP/Tesouro Direto: "No caso da compra
de um título apenas, o pagamento seria de R$ 48,80"). O exemplo dá 48,808848 arredondado ao centavo,
R$ 48,81, e o aviso explica a diferença no mesmo parágrafo. ✅

## Correções (aceitar por ID)

**C1. Bloqueante (cálculo).** Tabela de "Uma NTN-F feita de LTNs", coluna "Quantidade de LTN". Com
os valores que a tabela exibe, 0,04880885 × 936,585812 dá 45,713676, e não 45,713675. As três linhas
divergem na 6ª casa (45,713676 / 42,702406 / 855,467870), e o total diverge na 6ª (943,883952 contra
943,883948). Com 9 casas, a 3ª linha ainda falha. Com 10 casas, a tabela inteira se reproduz.
- `| 126 | 14,00 | 936,585812 | 0,04880885 | 45,713675 |` → `| 126 | 14,00 | 936,585812 | 0,0488088482 | 45,713675 |`
- `| 252 | 14,30 | 874,890639 | 0,04880885 | 42,702404 |` → `| 252 | 14,30 | 874,890639 | 0,0488088482 | 42,702404 |`
- `| 378 | 14,55 | 815,656609 | 1,04880885 | 855,467869 |` → `| 378 | 14,55 | 815,656609 | 1,0488088482 | 855,467869 |`

**C1-alt.** Esta opção substitui C1, C2 e C7, e não é a recomendada: adotar a convenção do Tesouro em
toda a cadeia. Os números ficam assim:
- fluxo de R$ 48,80885 por título (fórmula display = 48,80885);
- PUs de LTN 936,585811 / 874,890638 / 815,656609;
- custos 45,713676 / 42,702406 / 855,467870, total 943,883952;
- dealer 943,680880;
- compra −94.368.088,00, vendas +94.388.697,34, líquido +20.609,34;
- sobra de R$ 115,00 por data, com VP de R$ 302,12;
- lucro de R$ 20.307,22, que fica R$ 0,02 abaixo de 100.000 × 0,2030724 por causa do truncamento.

PU de R$ 943,88, TIR de 14,53%, dealer de R$ 943,68, R$ 0,20 e "cerca de 2 pontos-base" não mudam.
Exige reescrever o aviso, a frase do "exatamente" e a planilha (ver a decisão acima).

**C2. Bloqueante (cálculo).** "A moeda aparece". 100.000 × R$ 0,20 = R$ 20.000,00. O lucro é
100.000 × 0,2030728.
- "Descontada essa sobra, o lucro travado é de R$ 20.307,28: exatamente 100.000 vezes os R$ 0,20 de diferença."
  → "Descontada essa sobra, o lucro travado é de R$ 20.307,28: exatamente 100.000 vezes a diferença de preço, que, sem arredondar, é de R$ 0,2031 por título."

**C3. Definição de arbitragem (ponto a).** A frase geral não descreve a forma 1. Na forma 1, o fluxo
futuro é zero em todo cenário, e o lucro é o dinheiro recebido hoje, de modo que "dá lucro em pelo
menos um cenário" não se cumpre. A definição formal de Cochrane é a forma 2 com preço ≤ 0. A forma 1
é o que ele chama de uso coloquial: "a violation of the law of one price, a riskless way of buying
something cheap and selling it for a higher price" (*Asset Pricing*, rascunho de 1998, seção sobre
ausência de arbitragem).
- "Arbitragem é uma carteira que custa zero (ou menos que zero) hoje, nunca dá prejuízo no futuro e dá lucro em pelo menos um cenário. Ela aparece de duas formas:"
  → "Arbitragem é uma carteira que custa zero (ou menos que zero) hoje, nunca dá prejuízo no futuro e deixa lucro em algum ponto: no dinheiro recebido hoje ou em pelo menos um cenário futuro. Ela aparece de duas formas:"

Com a correção, o refrão que vem logo depois das duas formas continua no lugar: ele ilustra a forma 2.

**C4. "Nas três datas, os cupons e o principal da NTN-F pagam as LTNs vendidas" (ponto c).** A frase
não é precisa. Logo antes, o texto diz que faltam R$ 115,18 em cada data: a mesa deve 4.881.000 e
recebe 4.880.884,82; no vencimento, deve 104.881.000 e recebe 104.880.884,82. Os R$ 302,60 investidos
na curva hoje cobrem exatamente essa falta.
- "Nas três datas, os cupons e o principal da NTN-F pagam as LTNs vendidas."
  → "Nas três datas, os cupons e o principal da NTN-F pagam as LTNs vendidas, e os R$ 302,60 separados na montagem cobrem os R$ 115,18 que faltam em cada uma."

**C5. Legenda do diag-02.** Tem o mesmo problema de C4. A etapa 8 precisa mostrar os R$ 115,18 no
próprio diagrama.
- "A mesa recebe dinheiro hoje e, nas três datas, a NTN-F comprada paga as LTNs vendidas."
  → "A mesa recebe dinheiro hoje e, nas três datas, a NTN-F comprada paga as LTNs vendidas, menos os R$ 115,18 de cada data, cobertos pela reserva de R$ 302,60."

**C6. "centavo por centavo" ("Nem toda convergência é arbitragem").** Também falta a sobra aqui. A
grafia "O marca a mercado" fica para a etapa 6 (alerta do briefing).
- "mas no vencimento as LTNs vendidas são pagas, centavo por centavo, pelos fluxos da NTN-F comprada."
  → "mas no vencimento as LTNs vendidas são pagas pelos fluxos da NTN-F comprada e pela reserva separada na montagem."

**C7. O aviso do exemplo.** A diferença entre 48,808848 e o PU de juros do Tesouro (48,808850) vem
do arredondamento do fator na 8ª casa (A-8), não de truncamento. Os truncamentos são o do PU (T-6) e
o do valor financeiro (T-2).
- "sem os truncamentos da metodologia do Tesouro, que paga R$ 48,80 a quem tem um título."
  → "sem os arredondamentos e truncamentos da metodologia do Tesouro, que paga R$ 48,80 a quem tem um título."

**C8. Vencimento em feriado (ponto d). Leve.** 01/01/2029 é feriado (cai numa segunda-feira). Pela
Res. BCB 55/2020, art. 65, "os eventos que recaiam em dia não considerado útil são liquidados no dia
útil subsequente", ou seja, em 02/01/2029. "No mesmo dia" continua certo: as duas pagam em 02/01.
- "Em 1º de janeiro de 2029, o Tesouro Nacional vai pagar R$ 1.000 a quem tiver uma LTN 2029."
  → "No vencimento de 1º de janeiro de 2029, o Tesouro Nacional vai pagar R$ 1.000 a quem tiver uma LTN 2029."

**C9. PETR3 × PETR4.** O Estatuto da Petrobras (AGE de 16/04/2025, art. 5º) diz duas coisas que
pesam aqui:
- §2º: a PN tem prioridade no dividendo **mínimo** (5% do capital PN ou 3% do PL da ação, o maior).
- §3º: acima do mínimo, a PN participa "em igualdade de condições".

Na maior parte dos cenários, as duas recebem o mesmo por ação. O que não existe é a identidade
contratual em todo cenário. Não achei sinal de mudança no art. 5º em 2026. A ordem das razões
(crítica, item 13) fica para o gate.
- "Mas não pagam o mesmo fluxo: a ordinária dá direito a voto, a preferencial dá prioridade no dividendo."
  → "Mas não prometem o mesmo fluxo em todo cenário: a ordinária dá direito a voto, a preferencial dá prioridade no dividendo mínimo."

**C10. Unidade do prazo. Leve.** No texto, os vértices são em dias úteis.
- "4.881 LTNs de 126 dias, 4.881 de 252 e 104.881 de 378." → "4.881 LTNs de 126 dias úteis, 4.881 de 252 e 104.881 de 378."

**C11. Exercício da NTN-B. Leve.** Comprar a NTN-B e vender a réplica só é arbitragem se a NTN-B
estiver mais barata. O resto do exercício confere: "Se houvesse…" não afirma que a NTN-B Principal
existe em toda data (ela só existe em 6 vencimentos no Tesouro Direto; pesquisa, item 26). A resposta
esperada é 0,02956301 por data de cupom e 1,02956301 no vencimento.
- "E por que comprar a NTN-B e vender essa réplica seria arbitragem, mas comprar a NTN-B e vender LTNs não é?"
  → "E, se a NTN-B estivesse mais barata que essa réplica, por que comprá-la e vender a réplica seria arbitragem, mas comprar a NTN-B e vender LTNs não é?"

**C12. Fechar o `[VERIFICAR]` do desmembramento (ponto f).** A frase "Na custódia dos títulos
públicos, a NTN-F pode ser desmembrada: o principal e cada cupom passam a circular como títulos
separados." **fica como está**, e o marcador sai.
- "[VERIFICAR: fonte oficial de que a NTN-F admite desmembramento no Selic; … código Selic 950198)]" → (remover)

A fonte oficial é o BCB/Demab, arquivo de negociações de títulos federais no mercado secundário de
outubro de 2026 (NegT202610). Para o vencimento de 01/01/2029, o Selic registra três NTN-F
negociadas no mês:
- **950199** (BRSTNCNTF1Q6, o título inteiro): 2.243 operações;
- **950198** (BRSTNCNTF1Z7, emissão 01/10/2019): valor par R$ 1.000, 41 operações em 13 dias. É o
  principal;
- **950197** (BRSTNCNTF1Y0): sem valor par, 135 operações. É o cupom.

A identificação sai do próprio arquivo. Em 02/10/2026, o PU de lastro do 950198 era 740,74570968,
idêntico ao da LTN 01/01/2029. O do 950197 era 36,15494623, exatamente 48,80885 × 0,74074570968.
Há códigos de principal também para 2031, 2033, 2035 e 2037, e de cupom para várias datas.

A base normativa é a Res. BCB 55/2020, art. 45 (vigente): o desmembramento vale "quando prevista
tal faculdade na emissão". A cláusula de emissão da NTN-F ("Os cupons de juros das NTN-F poderão ser
negociados separadamente do principal, mantidas as características da emissão") apareceu em
resultado de busca de dois atos: o DOU de 20/01/2012 (p. 31, seção 1) e um documento da STN de
oferta de NTN-F 2025 e 2029. Não consegui abrir nenhum dos dois (jusbrasil devolve 403; sisweb,
500). A mesma redação, para a NTN-B, está no Edital STN nº 73/2024, que abriu.

Nota: o Mais Retorno troca os ISINs. O principal 2029 é BRSTNCNTF1Z7, não BRSTNCNTF1Y0.

## Números, item a item

| # | Afirmação no texto | Recálculo (python3) | Veredito |
|---|---|---|---|
| 1 | LTN 2029 paga R$ 1.000; NTN-F 2029, R$ 1.048,80 (um título) | 1.000 + trunc₂(48,808850) = 1.048,80 | ✅ Tesouro, Metodologia, Tabela 3 e exemplo da NTN-F |
| 2 | LTN de 1 ano a 14,30%: R$ 874,89 | 874,8906387 | ✅ |
| 3 | Principal a R$ 870,00: +R$ 4,89 hoje, 0 no vencimento | 874,89 − 870,00 = 4,89 | ✅ |
| 4 | C = 1.000 × (1,10^½ − 1) = 48,808848 | 48,808848170 | ✅ (PU de juros do Tesouro: 48,808850, ver C7) |
| 5 | Fluxos R$ 48,81 / 48,81 / 1.048,81 | arredondamento de 48,808848 | ✅ com o aviso |
| 6 | PUs de LTN 936,585812 / 874,890639 / 815,656609 | 936,5858116 / 874,8906387 / 815,6566094 | ✅ (arredondados; com `TRUNCAR`: …811 / …638 / …609) |
| 7 | Quantidades 0,04880885 / 0,04880885 / 1,04880885 | exatas: 0,0488088482 / 1,0488088482 | ⚠️ C1 |
| 8 | Custos 45,713675 / 42,702404 / 855,467869; total 943,883948 | 45,7136747 / 42,7024043 / 855,4678690; 943,8839481 | ✅ com as quantidades exatas; ⚠️ com as exibidas (C1) |
| 9 | PU justo de R$ 943,88 | 943,883948 | ✅ |
| 10 | TIR de 14,53%, abaixo dos 14,55% | 14,532754% | ✅ |
| 11 | Dealer a 14,55%: R$ 943,68 (tabela: 943,680875), R$ 0,20 abaixo | 943,680875273; diferença de 0,203073 | ✅ |
| 12 | 4.881 / 4.881 / 104.881 LTNs | teto de 4.880,885 e 104.880,885 | ✅ |
| 13 | Compra −94.368.087,53 | 100.000 × 943,680875273 | ✅ |
| 14 | Venda das LTNs +94.388.697,41 | 4.571.475,35 + 4.270.341,21 + 85.546.880,85 | ✅ |
| 15 | Líquido +20.609,88 | 20.609,88 | ✅ |
| 16 | Sobra de R$ 115,18 por data | 4.881.000 − 4.880.884,817 = 115,183 (igual nas três) | ✅ |
| 17 | Sobra vale R$ 302,60 hoje | 115,183 × (0,9365858 + 0,8748906 + 0,8156566) = 302,601 | ✅ |
| 18 | Lucro de R$ 20.307,28 | 20.609,88 − 302,60 = 20.307,28 = 100.000 × 0,2030728 | ✅ |
| 19 | "exatamente 100.000 vezes os R$ 0,20" | 100.000 × 0,20 = 20.000 | ⚠️ C2 (bloqueante) |
| 20 | R$ 20 mil em R$ 94 milhões, cerca de 2 pontos-base | 20.307,28 ÷ 94.368.087,53 = 2,15 pb | ✅ (a base, o valor montado, está clara) |
| 21 | Planilha `=SOMARPRODUTO(B2:B4/(1+C2:C4)^(D2:D4/252))` | 943,883948 | ✅ reproduz a tabela |
| 22 | "A réplica tem quatro pontas" | 1 NTN-F + 3 LTNs | ✅ |
| 23 | Exercício NTN-B: 6% a.a. em duas parcelas | 1,06^½ − 1 = 2,956301% por semestre | ✅ |

## Afirmações técnicas, fatos e fontes

| Item | Afirmação | Fonte | Veredito |
|---|---|---|---|
| a | Definição geral de arbitragem e as duas formas | Cochrane, rascunho de 1998 (definição de ausência de arbitragem; uso coloquial) | ⚠️ C3 |
| a | Lei do Preço Único como consequência; P(C) = P(A) + P(B); P = Σ CF·DF(t) | Cochrane, cap. 4 (4.1 e 4.2, sumário); ANBIMA, metodologia ETTJ, seção 1 | ✅ |
| b | Abertura com R$ 1.048,80 × exemplo com R$ 1.048,81 | Tesouro, Metodologia (Tabela 3, T-2); ENAP/Tesouro Direto, cap. 2 | ✅ coerente; C1, C2 e C7 |
| c | "os cupons e o principal da NTN-F pagam as LTNs vendidas" | recálculo (sobra de 115,18) | ⚠️ C4, C5 e C6 |
| d | "Em 1º de janeiro de 2029, o Tesouro Nacional vai pagar" | Res. BCB 55/2020, art. 65 | ⚠️ C8 (leve) |
| e | Selic em 13,75%, "mantida pelo Copom na reunião de 4 de novembro" | BCB, comunicado da 282ª reunião (04/11/2026: "Copom mantém a taxa Selic em 13,75% a.a."); SGS 432: 13,75 desde 17/09 | ✅ |
| e | Taxas de 14,00 / 14,30 / 14,55% "na ordem de grandeza da curva prefixada de novembro de 2026" | ANBIMA ETTJ, 10 a 17/11: 126 du 13,78 a 13,96; 252 du 14,04 a 14,40; 378 du 14,32 a 14,75 | ✅ (14,00% fica de 4 a 22 pb acima do vértice de 126 du; o texto diz "ilustrativas") |
| e | "14,30% ao ano, perto da curva prefixada de novembro de 2026" (1 ano) | mesma fonte: 252 du de 14,04 a 14,40 | ✅ (não é valor pontual, então não cabe `[FAIXA]`) |
| f | NTN-F desmembrável; principal e cupons circulam separados | BCB/Demab NegT202610; Res. BCB 55/2020, art. 45 | ✅ C12 |
| g | Tesouro "leiloa LTN e NTN-F toda semana" | Tesouro, calendário do 4º tri/2026 (comunicado 3348): "NTN-F … will be offered on a weekly basis alongside the LTNs"; 1º e 2º tri, idem | ✅ Ressalva: os leilões de 27 e 29/10 foram cancelados (Resenha BCB, 26 a 30/10) |
| g | ETTJ da ANBIMA estimada com LTN e NTN-F, pelo modelo de Svensson | ANBIMA, ETTJ, ago/2021 (Svensson, minimização sobre "todos os títulos"); ANBIMA, Intervalo Indicativo, seção 2 ("prefixados (LTN e NTN-F)") | ✅ Precisão: usa preços indicativos e um título sintético de 1 du na Selic; não muda a frase |
| g | Black e Scholes, e Merton, em 1973; réplica com ação e título; retorno esperado ausente | JPE 81(3), 637-654; Bell J. 4(1), 141-183; comunicado do Nobel de 1997 | ✅ |
| g | Nobel de 1997 a Merton e Scholes | nobelprize.org, comunicado de 14/10/1997 | ✅ |
| g | Fórmula "que o manual de opções da B3 usa, a do texto anterior" | B3, Manual de Apreçamento de Opções v27, seção 1.1 (conferido na etapa 7 de 09/11); texto publicado de 10/11 | ✅ |
| g | LTCM, "socorrido em 1998" | Federal Reserve History: em 23/09/1998, 14 instituições, US$ 3,6 bi | ✅ |
| g | LTCM "chamava de arbitragem muitas operações de convergência entre títulos parecidos" | Fed History: "exploited temporary price differences between similar types of securities"; President's Working Group (1999): "Convergence trading (also sometimes known as relative value arbitrage)" | ✅ |
| g | PETR3 voto × PETR4 prioridade no dividendo; "não pagam o mesmo fluxo" | Estatuto da Petrobras, art. 5º | ✅ os direitos; ⚠️ o fluxo (C9) |
| g | DI futuro: contrato da B3 sobre a taxa DI, com ajuste diário | B3, especificações do DI1 | ✅ |
| g | "O Tesouro não emite LTN para todo semestre" | calendário do 4º tri/2026 (LTN em abr/27, jan/28, out/28, jul/29, jan/30 e jan/32); ANBIMA, 11/11 | ✅ |
| g | NTN-B: 6% a.a. sobre o VNA, em duas parcelas; NTN-B Principal paga só o VNA | Tesouro, Metodologia, Tabela 1; comunicados de 2026 | ✅ |
| g | "Se houvesse uma NTN-B Principal em cada data de cupom…" | pesquisa, item 26 | ✅ contrafactual explícito; ⚠️ C11 (leve) |
| g | Atrito 1: venda a descoberto via compromissada | Res. BCB 55/2020 (compromissadas); pesquisa, item 21 | ✅ |
| g | "Um CDB e uma LTN … não carregam o mesmo risco de crédito" | ANBIMA, nota 1 (mesmo emissor, mesmo risco) | ✅ |
| h | Link para o texto anterior | HTTP 200, título "Frequência de Capitalização"; `post.md` com `url_publicada` | ✅ Ver a nota do catálogo abaixo |
| h | Link para "Quando os Modelos se Rebelam" | HTTP 200, título confere; catálogo: disponível e citável; o post traz o LTCM e cita Scholes e Merton como sócios | ✅ |
| h | Link para skill.syntaxis.com.br | HTTP 200; catálogo `oferta:skill-check`, topo gratuito; as duas dimensões citadas existem no resumo do catálogo | ✅ |
| h | Link para o PDF da ANBIMA | HTTP 200, `application/pdf`, "Versão Ago/2021" | ✅ |
| i | Tuckman e Serrat, 4ª ed. (Wiley, 2022), cap. 1, "Prices, Discount Factors, and Arbitrage" | Wiley-VCH, sumário (cap. 1, p. 49) | ✅ Título primário; o conteúdo (STRIPS, P-STRIPS × C-STRIPS, Lei do Preço Único, carteira replicante) vem só de fontes secundárias de curso do FRM |
| i | Cochrane, ed. revisada (Princeton, 2005), cap. 4, "The Discount Factor"; a Lei do Preço Único dá a existência do fator, e a não arbitragem, que ele é positivo | sumário (4.1 e 4.2); rascunho de 1998: "There is a strictly positive discount factor … if and only if there are no arbitrage opportunities" | ✅ |
| i | Shleifer e Vishny, *JF* 52(1), 35-55 (1997); a de livro não exige capital nem risco, a de verdade quase sempre exige | Crossref, abstract: "almost all arbitrage requires capital, and is typically risky" | ✅ ("quase sempre exige os dois" condensa "almost all … requires capital, and is typically risky": paráfrase aceitável) |
| i | Frase nova: "quem arbitra costuma usar capital de terceiros, que sai depois da perda. A arbitragem pode falhar justo quando os preços mais se afastam do valor." | Artigo, p. 37: os investidores "refuse to provide him with more capital, and even withdraw some of the capital"; "arbitrageurs can become most constrained when they have the best opportunities"; abstract: "arbitrage becomes ineffective in extreme circumstances, when prices diverge far from fundamental values" | ✅ fiel |
| i | Regra de referências | 4 itens: 2 livros (Tuckman e Serrat, Cochrane), 1 artigo, 1 metodologia; nenhuma lei | ✅ |
| j | Dois lados do balcão | ver abaixo | ✅ não bloqueante |

## Verificações adicionais da linha Notas de um Professor

- **Fórmula, simbólica e numérica.** A Lei do Preço Único, a soma, P = Σ CF·DF(t) com
  DF = (1 + r)^−(du/252) e a planilha conferem com a função desconto da ANBIMA. O recálculo com os
  valores do texto fecha, exceto C1 e C2 (bloqueantes, ambos de exibição ou redação, nenhum de
  modelo).
- **Aderência à realidade brasileira.** Taxas, Selic, cupom de 10%, base 252, lotes de R$ 1.000,
  leilões e a falta de LTN em todo semestre: tudo compatível com novembro de 2026.
- **Dois lados do balcão.** ✅ Presentes:
  - quem arbitra (a mesa);
  - quem cota errado e paga a diferença (o *dealer*, "o almoço do arbitrador saiu do prato de quem
    cotou errado");
  - o emissor (o Tesouro, que leiloa e passa a operar com preços coerentes);
  - quem marca a mercado e a ANBIMA.

  O emissor aparece leve, só como beneficiário. Isso já está no gate como item 14 da crítica
  (recompra de NTN-F em 26/10/2026). Não bloqueia.
- **Regra de referências.** ✅ 4 itens, 2 livros.

## Contexto para o autor e para o gate (sem correção no texto)

1. **O BCB aplica a Lei do Preço Único ao par da abertura.** Nos 13 dias de outubro de 2026 em que
   os dois negociaram, o PU de lastro do principal da NTN-F 2029 foi idêntico ao da LTN 2029.

   Os negócios contam outra história. O PU médio negociado do principal ficou acima do da LTN em 11
   desses 13 dias (de −R$ 29,49 a +R$ 13,33), mas com 1 a 10 operações por dia. É a direção de Daves
   e Ehrhardt (crítica, item 9), numa amostra pequena demais para entrar no texto.
2. **Caso real de 11/11 (crítica, item 10), recalculado.** Com os PUs indicativos da ANBIMA, a
   réplica sai em R$ 959,27 e a NTN-F 2029 em R$ 960,08: R$ 0,81 acima (0,085%). Confere com a
   pesquisa, item 34. A decisão de incluir continua no gate.
3. **`marketing/catalogo.json` está desatualizado para o texto anterior.** Gerado em 13/11, ele traz
   `post:2026-11-09-frequencia-de-capitalizacao` com `url: null`, "não publicado" e `citavel: false`.
   O `post.md` ganhou `url_publicada` em 16/11, e a página responde com o título certo. O link do
   texto está certo; é o catálogo que precisa ser regenerado (`scripts/gerar_catalogo.py`) antes da
   etapa 9a, para o parecer não acusar link a post "não publicado".
4. **"Trading de correlação".** A glosa "operação de valor relativo" tem apoio em duas fontes:
   - Gatev, Goetzmann e Rouwenhorst, "Pairs Trading: Performance of a Relative Value Arbitrage Rule",
     NBER w7032, 1999;
   - President's Working Group, 1999.

   A literatura chama esse tipo de operação de *arbitrage*, que é justamente o abuso que o texto
   ataca. Cochrane diz isso com todas as letras: "The word 'arbitrage' is also widely abused. 'Risk
   arbitrage' is an oxymoron that means taking bets." Se o autor quiser, a frase serve de lastro para
   a seção; não é correção.
5. **Black-Scholes (crítica, item 8b).** "Se a réplica existe, a opção tem de custar o mesmo que ela"
   é condicional, então está certo. A réplica dinâmica depende das hipóteses do modelo (negociação
   contínua, sem custos). Fica no gate, como já está.

## `[VERIFICAR]` e `[FAIXA]` para o texto final

- `[VERIFICAR]`: **nenhum.** O único que havia (desmembramento da NTN-F, na abertura) sai com C12.
- `[FAIXA]`: **nenhum.** As taxas de novembro aparecem como "ilustrativas" e "perto da curva", e não
  como valor pontual.

## Fontes novas desta etapa (acesso em 2026-11-18)

- BCB/Demab, negociações de títulos federais no mercado secundário, out/2026: https://www4.bcb.gov.br/pom/demab/negociacoes/download/NegT202610.ZIP
- BCB, *Main Characteristics of Domestic Federal Securities Registered in the Selic*, nota 2 (códigos Selic): https://www.bcb.gov.br/content/financialstability/selicsystem_docs/Domestic-Federal-Securities-Characteristics.pdf
- Res. BCB 55/2020, arts. 45 e 65 (vigente): https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20BCB&p2=55
- BCB, Copom (282ª) e SGS 432: https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados?quantidade=3 · https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/09/2026&dataFinal=18/11/2026
- Tesouro, calendário de leilões do 4º tri/2026 (comunicado 3348): https://thot-arquivos.tesouro.gov.br/comunicado/3348
- Tesouro, Edital nº 73/2024 (cláusula de cupons, NTN-B): https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/49237_1559777/1a.%20Edital%2073
- STN, documento de oferta de NTN-F 2025 e 2029 (só no resultado de busca; HTTP 500): https://sisweb.tesouro.gov.br/apex/cosis/thot/obtem_arquivo/25412:801089
- Tesouro, Metodologia de Cálculo (Tabela 3 e exemplo da NTN-F): https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/26310_1658601/Metodologia%20de%20Calculo%20-%20290424.pdf
- ANBIMA, ETTJ diária de 10 a 17/11 (formulário): https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp · mercado secundário de 11/11: https://www.anbima.com.br/informacoes/merc-sec/arqs/ms261111.txt · Intervalo Indicativo: https://www.anbima.com.br/data/files/79/F1/76/70/8FEFC8104606BDC8B82BA2A8/Metodologia%20ANBIMA%20Intervalo%20Indicativo.pdf
- Cochrane, *Asset Pricing*, rascunho de 1998 (cópia de curso): https://terpconnect.umd.edu/~wermers/ftpsite/fnce7100/Cochrane.pdf
- Shleifer e Vishny (1997), Crossref e texto: https://api.crossref.org/works/10.1111/j.1540-6261.1997.tb03807.x · https://ms.mcmaster.ca/%7Egrasselli/ShleiferVishny97.pdf
- President's Working Group on Financial Markets (1999), via CFTC: https://www.cftc.gov/tm/tmhedgefundreport.htm
- Federal Reserve History, LTCM: https://www.federalreservehistory.org/essays/ltcm-near-failure
- Gatev, Goetzmann e Rouwenhorst, NBER w7032: https://doi.org/10.3386/w7032
- Wiley-VCH, sumário de Tuckman e Serrat, 4ª ed.: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/fixed-income-securities-978-1-119-83555-4
