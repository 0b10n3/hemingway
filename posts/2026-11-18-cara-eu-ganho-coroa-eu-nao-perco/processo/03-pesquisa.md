# Etapa 3: Pesquisa

Slug: `2026-11-18-cara-eu-ganho-coroa-eu-nao-perco` · linha Notas de um Professor (conceito de finanças) · acesso a todas as fontes em **2026-11-18**. Executor: subagente `pesquisador-editorial`.

Escopo: conferir e completar a pesquisa do montador (`00-leitura.md`, "Notas de revisão"), seguindo as seções de `02-estrutura.md`. O laudo traz material de pesquisa, não prosa. Números de cálculo próprio vão marcados **[recalcular na etapa 7]**.

---

## Pendências do rascunho

| # | Item | Veredito |
|---|---|---|
| a | Selic 13,75% na 282ª reunião do Copom, 4/11/2026 | **Confirmado com divergência no corpo.** A 282ª (4/11/2026) **manteve** a Selic em 13,75%. O corte para 13,75% foi na **281ª, em 16/09/2026** (vigente desde 17/09). A frase do corpo "com a Selic em 13,75% desde a reunião do Copom de 4 de novembro" está errada na data |
| b | Ordem de grandeza da curva pré (14,00 / 14,30 / 14,55%) e Tesouro Prefixado 2029 a 14,65% em 11/11/2026 | **Confirmado.** Prefixado 2029 a 14,65% (taxa de compra, 11/11/2026). ETTJ ANBIMA 11/11: 13,77% (126 du), 14,04% (252), 14,32% (378), 14,56% (504). As taxas ilustrativas coincidem com a ETTJ em 252/378/504 du, não em 126/252/378; em 17/11 a ETTJ subiu e ficou em 13,90 / 14,28 / 14,59% nos vértices do exemplo |
| c | Norma vigente do desmembramento de NTN-F | **Parcial: norma geral achada, autorização específica da NTN-F não encontrada.** Regulamento do Selic (Resolução BCB nº 55/2020, art. 45, vigente) permite desmembrar cupons "quando prevista tal faculdade na emissão". Nenhuma fonte oficial atual encontrada que diga que a NTN-F tem essa faculdade. O Comunicado 7.588/2000 foi revogado em 31/07/2000 (fonte secundária). Existem ISINs de principal desmembrado de NTN-F 01/2029 só em agregador (Mais Retorno) |
| d | Cupom pago: R$ 48,81 ou R$ 48,80; último fluxo | **Divergente.** Tesouro: PU de juros = R$ 48,808850 por título (fator arredondado na 8ª casa, 0,04880885; PU truncado na 6ª). O valor financeiro é truncado na 2ª casa: **quem tem 1 título recebe R$ 48,80**, e no vencimento **R$ 1.048,80** (bruto). R$ 1.048,81 não aparece em fonte oficial. O cálculo próprio do rascunho (48,808848) difere do PU de juros do Tesouro (48,808850) na 6ª casa |
| e | Leilões semanais de LTN e NTN-F em 2026 | **Confirmado com ressalva.** Comunicados do Tesouro do 1º e 2º trimestres: NTN-F "disponibilizadas semanalmente em conjunto com as LTN". Ressalva: o leilão de prefixados de **29/10/2026 foi cancelado** e houve recompra extraordinária de NTN-F em 26/10. NTN-F 2029 e LTN 01/01/2029 não estão entre os vencimentos ofertados em 2026 |
| f | ANBIMA, ETTJ: Svensson, títulos usados, versão, URL | **Confirmado.** Svensson (1994), seis parâmetros estimados por dia; curva pré com LTN e NTN-F e um título sintético de 1 du ancorado na Estimativa da Taxa Selic da ANBIMA; ajuste sobre preços **indicativos**, ponderado pelo inverso da *duration*. PDF "Versão Ago/2021" responde (HTTP 200) no URL do rascunho. Não achei versão posterior do documento |
| g | Bibliografia (Tuckman e Serrat cap. 1; Cochrane cap. 4; Shleifer e Vishny) | **Confirmado.** Tuckman e Serrat, 4ª ed. (Wiley, ago/2022), cap. 1 "Prices, Discount Factors, and Arbitrage" (p. 49). Cochrane, *Asset Pricing*, Revised Edition (Princeton, 2005), cap. 4 "The Discount Factor" (p. 61), seções 4.1 "Law of One Price and Existence of a Discount Factor" e 4.2 "No Arbitrage and Positive Discount Factors". Shleifer e Vishny, *JF* 52(1), 35-55, mar/1997 |
| h | Fatos de apoio | **Confirmados, com três ajustes de precisão:** LTCM não "quebrou" no sentido estrito em 1998 (foi socorrido em 23/09/1998 por 14 instituições, US$ 3,6 bi); DI futuro referencia a "Taxa DI, divulgada pela B3" e o ajuste diário é distinto da margem; **não há NTN-B Principal em toda data de cupom** (só 6 vencimentos no Tesouro Direto em 11/11/2026) |
| i | Contrapontos e evidência empírica | **Achado nos EUA** (STRIPS, TIPS × Treasury, notes × bonds). **Nada brasileiro equivalente** com fonte verificável. Cálculo próprio com dados ANBIMA de 11/11/2026 mostra a NTN-F 2029 real **acima** da réplica em LTN (R$ 0,81 por título) [recalcular na etapa 7] |

---

## Abertura (sem H2)

**1. LTN 2029 e NTN-F 2029 existem e vencem em 1º/1/2029.** `contexto para o autor`
- ANBIMA, mercado secundário de 11/11/2026: LTN venc. 20290101, taxa indicativa 14,6468%, PU 748,530029; NTN-F venc. 20290101, taxa indicativa 14,5546%, PU 960,084932. https://www.anbima.com.br/informacoes/merc-sec/arqs/ms261111.txt
- Tesouro Direto, 11/11/2026: "Tesouro Prefixado 01/01/2029" e "Tesouro Prefixado com Juros Semestrais 01/01/2029" disponíveis. Tesouro Transparente, dataset "Preço e taxa dos títulos do Tesouro Direto": https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv

**2. Valor pago no vencimento da NTN-F (pendência d).** `entra no texto`
- Tesouro Nacional, *Metodologia de Cálculo dos Títulos Públicos Federais Ofertados nos Leilões Primários* (arquivo "Metodologia de Calculo - 290424"): "PU de Juros = R$ 1.000 * (1,10^0,5 − 1) = R$ 48,808850", com o fator arredondado na 8ª casa (A-8) e o PU truncado na 6ª (T-6). No exemplo da NTN-F, o fluxo de cada cupom aparece como 48,80885 e o último como 1048,80885. Tabela 3: "Valor Financeiro" truncado na 2ª casa. https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/26310_1658601/Metodologia%20de%20Calculo%20-%20290424.pdf
- ENAP/Tesouro Direto, *Tópicos Avançados*, cap. 2, nota de rodapé: "Embora o valor financeiro do cupom sempre seja truncado na 2ª casa decimal. No caso da compra de um título apenas, o pagamento seria de R$ 48,80." O diagrama do mesmo material mostra R$ 48,80 nos cupons e R$ 1.048,80 no vencimento. https://repositorio.enap.gov.br/bitstream/1/6248/7/T%C3%B3picos%20Avan%C3%A7ados%20Cap%C3%ADtulo%202%20TD.pdf
- Leitura: por título, o Tesouro define R$ 48,808850 (unitário) e o crédito em dinheiro de quem tem 1 título é R$ 48,80; no vencimento, R$ 1.048,80. Valores brutos: no Tesouro Direto o IR é retido sobre o cupom. Para quantidades grandes o truncamento pesa menos (100 títulos: R$ 4.880,88). A escolha do número da abertura fica com a etapa 7.

**3. Data efetiva do pagamento.** `contexto para o autor`
- Regulamento do Selic (Resolução BCB nº 55/2020), art. 65: "Os eventos que recaiam em dia não considerado útil são liquidados no dia útil subsequente." 1º/1/2029 é feriado; a liquidação cai em 2/1/2029. https://www.bcb.gov.br/api/conteudo/app/normativos/exibenormativo?p1=Resolu%C3%A7%C3%A3o%20BCB&p2=55

**4. Desmembramento da NTN-F (pendência c).** `entra no texto` (o que se pode afirmar) / `contexto para o autor` (o resto)
- **Norma geral vigente.** Resolução BCB nº 55, de 16/12/2020 (Regulamento do Selic), não revogada; alterada pelas Res. BCB 129/2021 e 409/2024 em outros artigos. Art. 45: "Os títulos em contas de custódia normal de livre movimentação podem ter seus cupons de juros desmembrados do principal, quando prevista tal faculdade na emissão desses títulos." §1º permite o remembramento; §2º veda desmembrar no dia útil anterior a pagamento de juros ou resgate. O art. 29, XVI, lista "desmembramento e remembramento de cupons de juros" entre as operações do Selic. Mesma fonte acima; espelho: https://www.legisweb.com.br/legislacao/?id=407478
- **Autorização específica da NTN-F: não encontrada em fonte oficial.**
  - Decreto nº 12.814, de 9/1/2026 (DOU 12/1/2026), que hoje estabelece as características dos títulos da DPMF (revogou o Decreto 11.301/2022, que revogara o 9.292/2018): art. 11 (NTN-F) não trata de desmembramento; o decreto não usa a palavra. https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12814.htm
  - BCB, *Main Characteristics of Domestic Federal Securities Registered in the Selic* (PDF de mar/2022): a ficha da NTN-D tem o campo "Trading of interest coupons" (só para emissões de 1/10/1997 a 17/7/2000); a ficha da NTN-F não tem esse campo. https://www.bcb.gov.br/content/financialstability/selicsystem_docs/Domestic-Federal-Securities-Characteristics.pdf
  - BCB, Relatório de Administração do Selic 2025: "as NTN-B, títulos com prazo mais longo, permitem o desmembramento de cupons de juros". Não menciona NTN-F nesse ponto. https://www3.bcb.gov.br/rasselic2025/
- **Comunicado Selic nº 7.588 (31/5/2000):** definia códigos de desmembramento e remembramento de NTN-D e NTN-F; foi **revogado pelo Comunicado 7.744 (31/7/2000)**, que por sua vez foi revogado pelo **Comunicado 12.275 (21/6/2004)**, que passou a dar um código Selic único aos cupons de mesma data (fungibilidade). Fonte secundária: resumos de busca dos espelhos em okai.com.br (https://okai.com.br/documento/2000-05-31/comunicado-n-007588; https://okai.com.br/documento/2004-06-21/comunicado-n-012275), bloqueados para leitura direta. O BCB cita o Comunicado Demab 7.744 na nota (2) do PDF de características acima. Não confirmei no BCB se o 12.275 segue vigente.
- **Indício de mercado (secundário):** Mais Retorno lista "NTN-F - SEM CUPONS - 01/2029", desmembramento "PRINCIPAL", código Selic 950198, emissão 01/10/2019, ISINs BRSTNCNTF1Y0 e BRSTNCNTF1Z7; "NTN-F - SEM CUPONS - 01/2031" (BRSTNCNTF253, emissão 19/02/2025); "NTN-F - SOMENTE CUPONS - 07/2029" (BRSTNCNTF261, emissão 19/02/2025). As páginas têm campos contraditórios ("SEM CUPONS" com "Pagamento de cupom: Sim"). https://maisretorno.com/titulos-publicos/ntn-f-01-01-2029-brstncntf1y0 · https://maisretorno.com/titulos-publicos/ntn-f-01-01-2029-brstncntf1z7 · https://maisretorno.com/titulos-publicos/ntn-f-01-01-2031-brstncntf253 · https://maisretorno.com/titulos-publicos/ntn-f-01-07-2029-brstncntf261 (esta última só vista no resumo da busca, não aberta)
- **Divergência menor com a nota do rascunho:** as emissões de strips de NTN-F que achei são de 2019 e 2025, não de 2026; o que é de 2026 é a atualização das páginas.
- O que a fonte oficial sustenta, sem mais: o Selic admite desmembramento de cupons para títulos cuja emissão preveja a faculdade. O que só fonte secundária sustenta: que a NTN-F 2029 tem principal desmembrado em circulação.

---

## A taxa não manda no preço (Mito)

**5. Como a literatura trata o erro-alvo (a).** `contexto para o autor`
- Cochrane, *Asset Pricing*, Revised Edition, sumário: cap. 4 "The Discount Factor", 4.1 "Law of One Price and Existence of a Discount Factor" (p. 62), 4.2 "No Arbitrage and Positive Discount Factors" (p. 67). A ordem dos capítulos sustenta a tese de que o fator de desconto é consequência da Lei do Preço Único, não convenção. Sumário digitalizado: https://toc.uni.li/FLMF019756.pdf
- ANBIMA trata o valor presente como premissa de estimação, não convenção: "o preço de um título de renda fixa é igual ao fluxo de caixa futuro prometido pelo emissor, trazido a valor presente por uma função desconto" (metodologia da ETTJ, Ago/2021, seção 1). Link no item 17.

---

## A aposta que não sobrevive

**6. Definição de arbitragem (alerta do briefing).** `contexto para o autor`
- O título da seção 4.2 de Cochrane liga não arbitragem a fator de desconto **positivo**, e a 4.1 liga a Lei do Preço Único à **existência** do fator. Isso confere a descrição do rascunho em "Para continuar aprendendo". Não consegui ler o texto do cap. 4 para conferir a definição formal de arbitragem; a etapa 7 confere contra o livro.

### A prova cabe numa LTN

**7. "14,30% ao ano, perto da curva prefixada de novembro de 2026" para um ano (pendência b).** `entra no texto`
- ETTJ prefixada ANBIMA, 11/11/2026, vértice 252 du: **14,0442%**; 17/11/2026, 252 du: **14,2752%**. Arquivo CSV da ANBIMA (formulário em https://www.anbima.com.br/informacoes/est-termo/CZ-down.asp, data de referência 11/11/2026 e 17/11/2026).
- Leilão do Tesouro de 5/11/2026: LTN 1/1/2028 (cerca de 14 meses) colocada a **14,31%** (taxa média e máxima). BCB, Resenha de Mercado Aberto de 2 a 6/11/2026: https://www.bcb.gov.br/content/publicacoes/resenhamercadoaberto/W20261102-20261106.pdf
- Mercado secundário ANBIMA 11/11/2026: LTN 1/10/2027 a 14,0186%; LTN 1/1/2028 a 14,1613%.
- Leitura: 14,30% para um ano fica dentro da faixa de novembro (14,0% a 14,3% conforme a data).

### Quem paga o ganha-ganha

**8. "o próprio Tesouro, que leiloa LTN e NTN-F toda semana" (pendência e).** `entra no texto`
- Comunicado do Tesouro Nacional, Leilões de Títulos 2026, 1º trimestre (https://thot-arquivos.tesouro.gov.br/comunicado/3129) e 2º trimestre (https://thot-arquivos.tesouro.gov.br/comunicado/3228), mesma redação: LTN de 6, 12, 24, 36, 48 e 72 meses "ofertadas em regime de alternância"; "Já as NTN-F, com referências de 5, 7 e 10 anos, serão disponibilizadas semanalmente em conjunto com as LTN." Leilões de prefixados às quintas-feiras. "a programação de emissões poderá ser alterada a qualquer momento".
- 4º trimestre: o calendário foi divulgado em 18/09/2026 (Resenha BCB citada abaixo; documento do calendário não acessado). Leilões efetivos de LTN e NTN-F em 22/10/2026 e 5/11/2026 (Resenhas BCB de 19 a 23/10 e de 2 a 6/11). https://www.bcb.gov.br/content/publicacoes/resenhamercadoaberto/W20261019-20261023.pdf
- **Ressalva:** "Em 26 de outubro, o Tesouro Nacional informou o cancelamento dos leilões tradicionais de títulos públicos indexados a índices de preço e de prefixados, programados para os dias 27/10/2026 e 29/10/2026". No mesmo dia, recompra extraordinária de NTN-F 2031 (15,79%), 2033 (15,61%) e 2037 (15,37%), cerca de R$ 7,1 bi. BCB, Resenha de 26 a 30/10/2026: https://www.bcb.gov.br/content/publicacoes/resenhamercadoaberto/W20261026-20261030.pdf
- Vencimentos de 2026 em oferta: NTN-F 2031, 2033, 2037; LTN do 2º tri: 1/10/2026, 1/4/2027, 1/4/2028, 1/7/2029, 1/1/2030, 1/1/2032. A NTN-F 2029 e a LTN 1/1/2029 da abertura não são ofertadas em 2026.

---

## Preço sem opinião

**9. Svensson e a função desconto da ANBIMA, na mesma forma da fórmula do rascunho.** `contexto para o autor`
- ANBIMA, metodologia da ETTJ (Ago/2021): preço = Σ F·b(T) + erro, com b(T) = 1/(1 + r(T))^T e T em dias úteis/252. É a fórmula P = Σ CF·DF(t) do rascunho, com DF em taxa efetiva base 252.

### A mesma ideia, com mais matemática

**10. Black, Scholes e Merton (1973).** `contexto para o autor` (confirma o que já está dito)
- Black, F.; Scholes, M. "The Pricing of Options and Corporate Liabilities". *Journal of Political Economy*, 81(3), 637-654, mai/1973. https://doi.org/10.1086/260062
- Merton, R. C. "Theory of Rational Option Pricing". *The Bell Journal of Economics and Management Science*, 4(1), 141-183, 1973. https://doi.org/10.2307/3003143

**11. Nobel de 1997 e Black.** `contexto para o autor`
- Comunicado de 14/10/1997: prêmio a Robert C. Merton e Myron S. Scholes "for a new method to determine the value of derivatives", desenvolvido "in close collaboration with Fischer Black, who died in his mid-fifties in 1995". O mesmo texto descreve a réplica: a carteira ação-opção sem risco "must pay exactly the same return as the risk-free market interest rate", senão "arbitrage trading would begin", e a composição tem de mudar gradualmente. Diz também que, antes, se supunha necessário "taking a stance on which risk premium to use". https://www.nobelprize.org/prizes/economic-sciences/1997/press-release/
- Estatutos da Fundação Nobel, §4: "Work produced by a person since deceased shall not be considered for an award. If, however, a prizewinner dies before he has received the prize, then the prize may be presented." https://www.nobelprize.org/organization/statutes-of-the-nobel-foundation/

---

## Uma NTN-F feita de LTNs

**12. Cupom de 10% a.a. pago semestralmente.** `entra no texto`
- Tesouro, Metodologia de Cálculo (Tabela 1): NTN-F, "10% a.a. pago semestralmente", valor de face R$ 1.000. Comunicados 3129 e 3228: "10% a.a., pagos semestralmente". Decreto 12.814/2026, art. 11: taxa definida pelo Ministro da Fazenda na emissão, juros semestrais, resgate pelo valor nominal.
- Nota de cálculo: a fórmula display do rascunho dá 48,808848; o Tesouro usa o fator arredondado (0,04880885) e chega a 48,808850. As quantidades da tabela do rascunho (0,04880885) já são as do Tesouro. [recalcular na etapa 7]

**13. Taxas ilustrativas 14,00 / 14,30 / 14,55% nos vértices 126 / 252 / 378 du (pendência b).** `entra no texto`

| Vértice (du) | ETTJ pré 11/11/2026 | ETTJ pré 17/11/2026 | Rascunho |
|---|---|---|---|
| 126 | 13,77%* | 13,8986% | 14,00% |
| 252 | 14,0442% | 14,2752% | 14,30% |
| 378 | 14,3234% | 14,5920% | 14,55% |
| 504 | 14,5618% | 14,8287% | n/a |

\* O CSV de 11/11 começa no vértice 252; o valor de 126 du saiu da fórmula de Svensson com os parâmetros publicados no mesmo arquivo (a mesma conta reproduz os vértices 252, 378 e 504 publicados até a 4ª casa) [recalcular na etapa 7].
- Leitura: ordem de grandeza confirmada. Em 11/11 as três taxas do rascunho batem com a ETTJ um semestre adiante (252/378/504); em 17/11 batem com os vértices do próprio exemplo, com desvio de até 10 pb. A inclinação do exemplo (cerca de 25 a 30 pb por semestre) é a da curva real.
- Tesouro Prefixado 2029 em 11/11/2026: taxa de compra 14,65%, venda 14,77% (Tesouro Transparente, CSV acima). **Confirmado.**

**14. "A TIR fica abaixo da taxa da LTN do vencimento porque a curva é positivamente inclinada": o mesmo efeito nos títulos reais.** `contexto para o autor`
- ANBIMA 11/11/2026, vencimento 1/1/2029: NTN-F a 14,5546% e LTN a 14,6468% (9 pb abaixo). Tesouro Direto no mesmo dia: Prefixado com Juros Semestrais 2029 a 14,56% e Prefixado 2029 a 14,65%.

### A moeda aparece

**15. Escala de "cerca de 2 pontos-base".** `contexto para o autor`
- R$ 20.307,28 ÷ R$ 94.368.087,53 = 2,15 pb do valor montado [recalcular na etapa 7]. A base do ponto-base (valor da operação, não taxa) é alerta do briefing para a etapa 5/6.

### A mesma conta, todo dia

**16. Desmembramento como decomposição física.** Ver item 4: a afirmação sobre a NTN-F específica não tem fonte oficial.

**17. ETTJ ANBIMA (pendência f).** `entra no texto`
- ANBIMA, *Estrutura a Termo das Taxas de Juros Estimada e Inflação Implícita: Metodologia*, "Versão Ago/2021", 11 p. URL do rascunho responde em 18/11/2026: https://www.anbima.com.br/data/files/9A/F4/E3/1F/4805B710B0F024B7882BA2A8/est-termo_metodologia_v2021.pdf
  - Modelo: "No modelo proposto por Svensson (1994)"; parâmetros "obtidos através da minimização do somatório dos erros quadráticos (quadrado da diferença entre o preço indicativo e o preço resultante do modelo) de todos os títulos ponderados pelo inverso da duration"; a ETTJ divulgada é obtida "através da estimação diária de todos os seis parâmetros do modelo", com algoritmo genético e refinamento.
  - Nota 2: preço indicativo é o "calculado a partir da coleta das taxas consideradas justas pelas instituições para o título, independente de ter havido negócios com o papel".
  - Nota 3: "Para incluir referências de curto prazo na estimação das curvas, são adotados títulos sintéticos com maturidade de 1 dia útil. No caso da ETTJ Prefixada, adota-se a Estimativa da Taxa Selic".
- ANBIMA, *Intervalo Indicativo para títulos públicos*, versão dez/2023, seção 2: "Metodologia da Construção da ETTJ por classes de títulos - prefixados (LTN e NTN-F), atrelados ao IPC-A (NTN-B) e pós-fixados (LFT)". https://www.anbima.com.br/data/files/79/F1/76/70/8FEFC8104606BDC8B82BA2A8/Metodologia%20ANBIMA%20Intervalo%20Indicativo.pdf
- Precisão para a etapa 7: a curva pré usa LTN e NTN-F **mais** um título sintético de 1 du (Selic), e ajusta preços indicativos, não preços de negócio. Os fatores são os que "melhor explicam" os preços: há erro residual por título, ou seja, a curva não impõe a Lei do Preço Único exatamente.
- Contexto de link: a página de curvas da ANBIMA traz aviso de 17/03/2026 de que "esta aba será desligada e as curvas de juros e de crédito ficarão exclusivamente no ANBIMA Data". https://www.anbima.com.br/pt_br/informar/curvas-de-juros-fechamento.htm. O PDF continua no ar; o metadado de título do arquivo diz "Política de Segurança da Informação" (erro da ANBIMA, não do conteúdo).

---

## Nem toda convergência é arbitragem

**18. PETR3 × PETR4: direitos no estatuto.** `entra no texto` (sustenta "a ordinária dá direito a voto, a preferencial dá prioridade no dividendo")
- Estatuto Social da Petrobras, conforme AGE de 16/04/2025, art. 5º: ordinárias "com direito de voto" e preferenciais "sempre sem direito a voto"; §1º inconversíveis; §2º prioridade "no caso de reembolso do capital e no recebimento dos dividendos, no mínimo, de 5% (cinco por cento) calculado sobre a parte do capital representada por essa espécie de ações, ou de 3% (três por cento) do valor do patrimônio líquido da ação, prevalecendo sempre o maior"; §3º participam "em igualdade de condições" dos dividendos acima do mínimo; §4º direito de inclusão em oferta pública por alienação de controle "ao mesmo preço e nas mesmas condições" do controlador. https://api.mziq.com/mzfilemanager/v2/d/25fdf098-34f5-4608-b7fa-17d60b2de47d/ef2195e6-f2b6-8127-240e-1417c9c8be04?origin=2
- **Contraponto genuíno** `contexto para o autor`: pelos §§3º e 4º, sempre que o dividendo supera o mínimo, as duas classes recebem o mesmo por ação, e a PN tem *tag along* integral. Um crítico diria que, na maior parte dos cenários, os fluxos pagos coincidem. O que separa as duas é a ausência de identidade contratual em todos os cenários (voto, prioridade abaixo do mínimo, reembolso) e a ausência de data em que as pontas se encontram, que o rascunho já usa. Não confirmei se este é o estatuto vigente em 18/11/2026.

**19. LTCM em 1998.** `entra no texto` (precisão)
- Federal Reserve History, "Near Failure of Long-Term Capital Management" (Michael Fleming e Weiling Liu, texto de 22/11/2013): em 23/09/1998, "fourteen banks and brokerages" investiram US$ 3,6 bilhões "to prevent the firm's imminent collapse"; credores com 90% do fundo; o investimento foi devolvido até o fim de 1999. O fundo "exploited temporary price differences between similar types of securities", com "betting on the spreads in its portfolios to converge"; alavancagem de cerca de 30 para 1 no fim de 1997. https://www.federalreservehistory.org/essays/ltcm-near-failure
- Divergência de precisão: "quebrou em 1998" × "near failure" e socorro em 1998. O post da série ("Quando os Modelos se Rebelam") descreve o socorro do Fed de Nova York e cita a mesma fonte.

### Os limites da arbitragem de verdade

**20. Shleifer e Vishny (1997).** `entra no texto`
- Shleifer, A.; Vishny, R. W. "The Limits of Arbitrage". *The Journal of Finance*, 52(1), 35-55, mar/1997. https://doi.org/10.1111/j.1540-6261.1997.tb03807.x (metadados e abstract via Crossref, https://api.crossref.org/works/10.1111/j.1540-6261.1997.tb03807.x). Versão de trabalho: NBER WP 5167, jul/1995, https://www.nber.org/papers/w5167
- Abstract publicado: "Textbook arbitrage in financial markets requires no capital and entails no risk. In reality, almost all arbitrage requires capital, and is typically risky." E: "the possibility that arbitrage becomes ineffective in extreme circumstances, when prices diverge far from fundamental values." A paráfrase do rascunho e a descrição em "Para continuar aprendendo" batem com o abstract.

**21. Atrito 1: vender a descoberto via compromissada.** `contexto para o autor`
- O Regulamento do Selic trata compromissadas na Seção III do cap. VII (arts. 33 e seguintes da Res. BCB 55/2020). Não procurei dado de custo de aluguel de LTN.

**22. Atrito 3: "Nem toda data tem LTN".** `entra no texto`
- ANBIMA 11/11/2026, vencimentos de LTN: trimestrais de 1/4/2027 a 1/10/2028; depois 1/1/2029, 1/7/2029, 1/1/2030 e 1/1/2032. Não há LTN em 1/7/2030, 1/1/2031, 1/7/2031 e datas seguintes de cupom das NTN-F 2031, 2033, 2035 e 2037. Mesma fonte do item 1.

**23. DI futuro (DI1).** `entra no texto` (precisão)
- B3, especificações do contrato DI1: "Futuro padronizado de taxa de juro definida pela acumulação da Taxa DI, divulgada pela B3, até o vencimento do contrato"; cotação em "Taxa de juro efetiva anual, base 252 dias úteis"; "O ajuste diário é calculado utilizando VWAP"; liquidação no vencimento "Financeira". https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/programa-de-treinamento-di/04-especificacoes-do-contrato.htm
- Precisão para a etapa 7: o rascunho diz "ajuste diário de margem e referência no CDI". Na B3, ajuste diário (liquidação diária de ganhos e perdas pelo preço de ajuste) e margem de garantia são coisas distintas, e o ativo é a "Taxa DI, divulgada pela B3".

---

## Antes de chamar de arbitragem

**24. Pergunta 2 (mesmo devedor).** `contexto para o autor`
- A nota 1 da metodologia ANBIMA usa o mesmo argumento ao contrário: "Como estamos tratando de títulos de um mesmo emissor (o governo federal), o risco de crédito é o mesmo para todos os títulos e por isto ele já está incorporado nos juros."

**25. Comparar preço com preço.** Nenhum dado novo; o item 27 é o caso real.

---

## A moeda que ninguém lança duas vezes (fecho e exercício da NTN-B)

**26. NTN-B e NTN-B Principal (pendência h).** `entra no texto`
- Cupom: "6% a.a., pagos semestralmente" (Comunicados 3129 e 3228; Metodologia de Cálculo, Tabela 1). Decreto 12.814/2026, art. 7º: valor nominal atualizado pelo IPCA do mês anterior, juros semestrais, resgate em parcela única no vencimento. O decreto não menciona "NTN-B Principal".
- **NTN-B Principal não existe em toda data de cupom.** Tesouro Direto, 11/11/2026, "Tesouro IPCA+" (NTN-B Principal): só 15/05/2029, 15/08/2032, 15/05/2035, 15/08/2040, 15/05/2045 e 15/08/2050. "Tesouro IPCA+ com Juros Semestrais" (NTN-B) no mesmo dia: 2030, 2032, 2035, 2037, 2040, 2045, 2050, 2055, 2060; cada uma paga cupom a cada seis meses (15/2 e 15/8, ou 15/5 e 15/11). Tesouro Transparente, CSV do item 1. ANBIMA 11/11/2026 lista 14 vencimentos de NTN-B, de 2027 a 2060.
- Nuance: o Relatório do Selic 2025 diz que as NTN-B "permitem o desmembramento de cupons de juros", e o Mais Retorno lista séries "NTN-B - SOMENTE CUPONS". Zeros em IPCA para as datas de cupom podem existir na custódia como cupons desmembrados, não como NTN-B Principal emitida. Fonte oficial só para a frase geral do BCB.

---

## Para continuar aprendendo

**27. Tuckman e Serrat (pendência g).** `entra no texto`
- Wiley-VCH, ficha do livro: *Fixed Income Securities: Tools for Today's Markets*, 4ª ed., Bruce Tuckman e Angel Serrat, John Wiley & Sons, ago/2022, ISBN 978-1-119-83555-4, 560 p. Sumário: "Chapter 0 Overview" (p. 1); "Chapter 1 Prices, Discount Factors, and Arbitrage" (p. 49). https://www.wiley-vch.de/en/areas-interest/finance-economics-law/fixed-income-securities-978-1-119-83555-4
- Conteúdo do cap. 1 (STRIPS, Lei do Preço Único, carteira replicante): confirmado só por fonte secundária (guias do FRM baseados no capítulo), ex.: https://analystprep.com/study-notes/frm/part-1/valuation-and-risk-management/prices-discount-factors-and-arbitrage/
- Nota: o livro tem um capítulo 0. "cap. 1" está correto.

**28. Cochrane (pendência g).** `entra no texto`
- *Asset Pricing*, Revised Edition, Princeton University Press, 2005 (ISBN 978-0-691-12137-6 segundo listagens de livraria). Sumário: "4 The Discount Factor" (p. 61); "4.1 Law of One Price and Existence of a Discount Factor" (p. 62); "4.2 No Arbitrage and Positive Discount Factors" (p. 67). https://toc.uni.li/FLMF019756.pdf. O `[VERIFICAR]` do rascunho pode ser resolvido.

**29. Shleifer e Vishny.** Ver item 20. **30. ANBIMA.** Ver item 17.

---

## Contrapontos e o que ninguém está dizendo

**31. A Lei do Preço Único falha no mercado de títulos mais líquido do mundo, e por muito.** `contexto para o autor` (o contraponto mais forte à frase "os desvios de tela são, em geral, o preço desses atritos")
- Fleckenstein, M.; Longstaff, F. A.; Lustig, H. "The TIPS-Treasury Bond Puzzle". *JF*, 69(5), 2151-2197, 2014. https://doi.org/10.1111/jofi.12032. Abstract: o preço de um Treasury e o de um TIPS com swap de inflação "exactly replicating the cash flows of the Treasury bond can differ by more than $20 per $100 notional"; o desvio total "has exceeded $56 billion, representing nearly 8% of the total amount of TIPS outstanding"; "the mispricing narrows as additional capital flows into the markets", apoio à explicação de capital lento (*slow-moving capital*). Versão NBER w16358 (set/2010): https://www.nber.org/papers/w16358
- Musto, D.; Nini, G.; Schwarz, K. "Notes on Bonds: Illiquidity Feedback During the Financial Crisis". *Review of Financial Studies*, 31(8), 2983-3018, 2018. https://doi.org/10.1093/rfs/hhy022. Abstract: na crise de 2008, "bonds fell more than six percent below more-liquid but otherwise identical notes".
- Leitura: nos dois casos, a réplica é exata e o desvio persiste por meses. Isso cabe na tese de Shleifer e Vishny (capital e risco), e não contradiz o rascunho, mas mostra que "atrito" inclui falta de capital, não só aluguel, *spread* e data sem título.

**32. STRIPS: principal e cupom do mesmo vencimento com preços diferentes.** `contexto para o autor`
- Daves, P. R.; Ehrhardt, M. C. "Liquidity, Reconstitution, and the Value of U.S. Treasury Strips". *JF*, 48(1), 315-329, 1993. https://doi.org/10.1111/j.1540-6261.1993.tb04712.x. Abstract (via Consensus): "zero-coupon strips created from principal payments typically trade at significantly higher prices than otherwise identical zero-coupon strips created from coupon payments"; liquidez e características de reconstituição explicam boa parte. Relevante para a abertura: o principal desmembrado e um zero "igual" podem não ser a mesma promessa em preço, porque o principal reconstitui o título e o cupom não.
- Jordan, B. D.; Jorgensen, R. D.; Kuipers, D. R. "The relative pricing of U.S. Treasury STRIPS: empirical evidence". *Journal of Financial Economics*, 2000. https://doi.org/10.1016/s0304-405x(99)00060-4. Abstract: lucros de *stripping* e reconstituição "are fleeting and rarely economically significant". Apoia "pequena, rápida e disputada".
- Grinblatt, M.; Longstaff, F. A. "Financial Innovation and the Role of Derivative Securities: An Empirical Analysis of the Treasury STRIPS Program". *JF*, 55(3), 1415-1436, 2000. https://doi.org/10.1111/0022-1082.00252. Abstract: o programa é usado sobretudo "to make markets more complete and take advantage of tax and accounting asymmetries"; "little evidence that the option to strip and reconstitute securities is used for speculative or arbitrage-related purposes". Contraponto à frase "O mercado leva essa decomposição tão a sério que ela existe fisicamente": nos EUA, o desmembramento serve mais a demanda por zeros do que a arbitragem.
- Links Consensus dos abstracts: https://consensus.app/papers/details/w:e5d967e9-4a90-4798-a524-1741ec8c1e73/?utm_source=claude_desktop · https://consensus.app/papers/details/w:d96121b5-326d-4214-8fb3-84098d73207d/?utm_source=claude_desktop · https://consensus.app/papers/details/w:d7e63ff4-1aed-447f-a95e-6e6e188ece3a/?utm_source=claude_desktop · https://consensus.app/papers/details/w:1620c8b9-4a60-4ae2-9725-2a7b2b36d2ac/?utm_source=claude_desktop
- Não verifiquei Amihud e Mendelson (1991, *JF* 46(4), 1411-1425, notes × bills) nem Krishnamurthy (2002, *JFE* 66(2-3), 463-506, *on-the-run* × *off-the-run*) além dos metadados no Crossref.

**33. Brasil: evidência acadêmica equivalente não encontrada.** `contexto para o autor`
- Busca no Consensus e na web por violação da Lei do Preço Único entre LTN e NTN-F, ou entre NTN-F e seus strips, não trouxe estudo verificável. O mais próximo: Laurini e Westin Neto (2014), *International Econometric Review*, testam restrições de não arbitragem na curva de DI futuro de 2007 a 2009 e concluem que as correções "are not necessary" (https://doi.org/10.33818/ier.278036). Não é teste de Lei do Preço Único em títulos.

**34. O caso real da semana: a NTN-F 2029 cotada acima da sua réplica em LTN.** `contexto para o autor` [recalcular na etapa 7]
- Dados ANBIMA de 11/11/2026 (item 1). Fatores de desconto = PU da LTN ÷ 1.000 em 1/7/2027, 1/1/2028, 1/7/2028 e 1/1/2029; para 1/1/2027, PU da NTN-F 2027 (último fluxo) ÷ 1.048,80885. Cupom 48,80885.
- Réplica: **R$ 959,27**. PU indicativo da NTN-F 2029: **R$ 960,08**. A NTN-F sai **R$ 0,81 mais cara** que as LTNs que a replicam (cerca de 0,08% do preço). Com a LTN 2027 do Tesouro Direto (PU 982,33) no lugar da NTN-F 2027, a réplica dá R$ 959,27 também.
- Leitura: é o sentido oposto ao do *dealer* do exemplo. Explorar exigiria vender a NTN-F a descoberto e comprar as LTNs, o atrito 1 do rascunho. E são preços indicativos, não executáveis. Não prova arbitragem; mostra a ordem de grandeza de um desvio real.

**35. A curva de "novembro de 2026" é uma curva de estresse.** `contexto para o autor`
- LTN 1/1/2028 saiu a 12,89% no leilão de 22/10/2026 e a 14,31% no de 5/11/2026 (Resenhas BCB citadas). Entre as duas datas, o Tesouro cancelou o leilão de prefixados e recomprou NTN-F (item 8). Os 14,00 / 14,30 / 14,55% do exemplo são da curva pós-choque; um mês antes, a ordem de grandeza era cerca de 100 pb menor.
- Lado de lá: na semana de estresse, o próprio emissor atuou comprando NTN-F "para assegurar o bom funcionamento do mercado de títulos públicos" (Resenha BCB, 26 a 30/10/2026). É o Tesouro como parte interessada em preços coerentes, não só beneficiário.

---

## Fontes (acesso em 2026-11-18)

- BCB, série SGS 432 (meta Selic): https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial=01/09/2026&dataFinal=18/11/2026. Leitura: 14,00 até 16/09/2026; 13,75 de 17/09 a 18/11/2026.
- BCB, comunicados do Copom: https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados?quantidade=3 ("282ª reunião - Copom mantém a taxa Selic em 13,75% a.a.", 2026-11-04; "281ª reunião - Copom reduz a taxa Selic para 13,75% a.a.", 2026-09-16) e https://www.bcb.gov.br/api/servico/sitebcb/copom/comunicados_detalhes?nro_reuniao=282
- Fonte secundária do montador (Agência Brasil, Estadão Conteúdo): não consultada; a fonte primária acima basta.
- Demais fontes: citadas com link em cada item.
