# Etapa 7 — Verificação técnica

Laudo do agente `verificador-tecnico`, gravado pelo pipeline principal. Base: corpo de
`04-draft-v2.md` ("lNN" = linha nesse arquivo) + glosas e reformulações aprovadas em
`06-revisao.md`. Fontes acessadas em 04/11/2026; "du252/07" = itens reaproveitados de
`posts/2026-10-30-du252-contagem-de-dias/processo/07-verificacao.md` (30/10/2026).

**Ambiente:** python3 3.14.4; `bizdays` 1.0.19 (`ANBIMA.cal`) em diretório isolado do scratchpad;
normas do BCB pela API JSON (Comunicado 7.684 na íntegra via `exibeoutrasnormas`); PDFs (Garcia,
CMN 5.171, Susep 2022) via `pdftotext`. Planalto bloqueado para as ferramentas.
**Registro de cálculo (scripts e saída):** `_revisoes/2026-11-04_2026-11-02-a-barriga-da-curva_calculo.md`.

## Resumo

- **Todos os números impressos conferem no recálculo.**
- **3 bloqueantes:** B-1 previsão de direção falsa com réguas diferentes (l.193); B-2 `DIATRABALHOTOTAL(...)-1` erra quando a data final não é dia útil (inclusive LTN em 1º/jan); B-3 nome do Samanez.
- **8 recomendadas** (R-1 a R-8). **7 opcionais** (P-1 a P-7).
- **[VERIFICAR] mantido: 1** (over ao mês = diária × 30), do qual dependem l.157, l.159 e l.212 (espinha nominal × efetiva). Ver V-1.
- **[VERIFICAR] resolvidos: 4** (Comunicado 7.684; convenção de pontas; edições de Assaf Neto e Samanez; Hull). **[FAIXA]:** nenhum.
- Itens 28 e 56 da etapa 6: conferem. Dois lados do balcão: atende. Regra de referências: cumprida.

---

## Bloqueantes

### B-1. l.193 — a previsão de direção só vale com a mesma régua
- Texto: "com prazo menor que um ano, a taxa linear vira uma taxa composta maior", logo após a equação que mistura dc/360 e du/252.
- Mesma régua: vale para todo prazo entre 0 e 1 (é a barriga). Réguas diferentes: dos 61.651 pares (início, fim) em dia útil de 2026 com até 364 dc, em 1.069 o 14% linear/360 vira **menos** de 14% exponencial/252 — todos com até 39 dc. Overnight de dia útil: (1 + 0,14/360)^252 − 1 = **10,29%**. Em prazos curtos sem fim de semana, du/252 > dc/360 e a régua vence o motor.
- **Correção mínima:** "E dá para prever o lado antes da conta: com a mesma régua e prazo menor que um ano, a taxa linear vira uma taxa composta maior." Opcional em seguida: "Com réguas diferentes, em prazos de poucos dias, a régua pode puxar para o outro lado." O exemplo de 91 dias segue bom (motor e régua no mesmo sentido).

### B-2. l.205 e l.208 — o "−1" da planilha erra quando a data final não é dia útil
- **Sintaxe confere:** Excel pt-BR `DIATRABALHOTOTAL(data_inicial; data_final; [feriados])`; Google Planilhas pt-BR `DIATRABALHOTOTAL(data_de_inicio; data_de_termino; feriados)`. LibreOffice diz literalmente que as duas pontas contam quando são dias úteis.
- **Convenção confere ([VERIFICAR] sai):** Comunicado BCB 7.684, literal: "número de dias úteis entre a data de liquidação da operação (inclusive) e a data de vencimento (exclusive)"; Tesouro e OC 055/2024-PRE idem; calendário de feriados nacionais da ANBIMA (du252/07).
- **Força bruta (5.000 pares, 2026–2029):** `DIATRABALHOTOTAL(início;fim;feriados)-1` erra 1.571/5.000, exatamente quando a data final não é dia útil. Caso real: LTN 02/01/2026 → 01/01/2027: mercado 249 du; fórmula do texto **248**. `DIATRABALHOTOTAL(início;fim-1;feriados)` acerta 5.000/5.000.
- **Correção da linha 4:** `Dias úteis entre datas:    =DIATRABALHOTOTAL(início;fim-1;feriados)`
- **Correção da l.208, sem o [VERIFICAR]:** "A quarta conta traz de volta as duas perguntas que ficaram no texto anterior, calendário e pontas. O 'menos 1' vai na data final porque a função conta as duas pontas, quando são dias úteis, e o mercado conta a data inicial e exclui a final. Tirar o dia do fim, e não do resultado, mantém a conta certa quando o vencimento cai num feriado, como o 1º de janeiro das LTN. Um calendário de feriados desatualizado muda o du, e o du está no expoente." (Se o "−1" ficar fora da função, a frase precisa de "quando a data final é dia útil".) LTN leva a glosa do du252; ANBIMA, se voltar ao texto, também.

### B-3. Bibliografia — Samanez
- "José Carlos Samanez" → **Carlos Patricio Samanez** (catálogo IFAC, ISBN 9788576057994).

## Recomendadas

- **R-1. l.157, "nascera como taxa 'efetiva-dia'".** A Circular 2.347/1993 trata de taxas de empréstimos bancários informadas ao BCB; prova que em 1993 "taxa over" já era o nome da convenção "efetiva-dia", não onde a over nasceu. Acúmulo composto sustentado pela fórmula da 2.761. Proposta: "A *over*, a taxa das operações de um dia, era uma taxa 'efetiva-dia', acumulada de forma composta."
- **R-2. l.159, ponte over × Selic (C4).** A Selic é a média das compromissadas com títulos federais "para liquidação no dia útil subsequente" (Res. BCB 46/2020, art. 1º). Proposta (com o item 43): "…a Selic (a taxa básica de juros, que é a *over* das operações com títulos públicos) passou a ser expressa ao ano…".
- **R-3. l.173 / item 50, Susep.** Relatório de 23/06/2022, p. 19: converte as taxas da B3 em contínuas **antes** de estimar; as taxas retornadas são "anuais e compostas continuamente"; conversão de volta para discreta **não aparece**. A curva de dólar fica linear anual. Proposta: "…e nas curvas de juros que a Susep (Superintendência de Seguros Privados) estima em taxa contínua para as seguradoras." Sai "antes de converter (para/em) taxa discreta". Se o autor quiser manter: `[VERIFICAR: se a Susep publica as ETTJ convertidas para taxa discreta]`.
- **R-4. l.169, "sempre foram rateados".** Sem fonte para "sempre". Proposta: "onde depósitos de curto prazo são, por convenção, rateados de forma proporcional ao tempo".
- **R-5. l.111, Bernoulli.** Proposta: "Quem fez cálculo reconhece a desigualdade de Bernoulli, na versão para expoentes entre zero e um".
- **R-6. l.119, taxa legal = juros (C3).** CMN 5.171: TL = max[Fator Selic/Fator IPCA-15 − 1; 0] (art. 2º); art. 7º separa atualização monetária. Art. 406 CC (Lei 14.905/2024, via IRIB). Proposta: "…a taxa legal, a taxa de juros que incide sobre uma dívida civil quando o contrato não fixa a taxa (art. 406 do Código Civil)."
- **R-7. l.197, motor do 365/360 (C5).** Linear dá 14,19%; composto base 360 daria 14,21%. Proposta: "14% ao ano linear, base 360, rendem 14% × 365/360 = 14,19%."
- **R-8. Bibliografia — descrições não conferidas.** Sai do Assaf Neto "e a decomposição do montante composto usada no gráfico" (graf-02 é cálculo próprio); sai do Samanez "com mais exercícios" (ver seção 5).

## Opcionais

- **P-1. l.195:** o intervalo 91 dc / 63 du existe (23 de 251 inícios em 2026; moda 61). Exemplo com as duas pontas úteis: **22/04/2026 → 22/07/2026**. Proposta: "…por exemplo de 22 de abril a 22 de julho de 2026, com 63 dias úteis…". Manter também é correto.
- **P-2. l.161, Garcia:** "Com a mesma taxa por dia útil (a de 21,84% ao ano que o mercado projetava), …".
- **P-3. l.163, Comunicado 7.684:** vale "a partir de 1. de agosto de 2000"; cambiais ficam como taxa nominal anual 30/360 semestral. Proposta: "…às operações do Banco Central com títulos públicos, exceto os cambiais: taxa efetiva anual, base 252."
- **P-4. l.91:** corporativos americanos usam 30/360; "dias corridos sobre 360 ou 365" é simplificação aceitável.
- **P-5. l.195:** a divisão 75/17 depende da ordem (régua primeiro: 15,56 + 76,93); o texto define o caminho. Sem mudança.
- **P-6. Item 56:** "Dos 92 pontos-base a mais" deixa 75 + 17 = 92 visível (92,49 pb).
- **P-7. l.49:** contrato linear real de seis meses conta 181–184 dc; "é o que o juro simples paga" com t = 0,5 está correto. Sem mudança.

## V-1. [VERIFICAR] mantido — over ao mês = diária × 30 (l.157)
- Nenhuma norma do BCB manda isso (2.347/1993, 2.720/1996, 2.761 só "efetiva-dia" / "forma de expressão"). Só a Bússola do Investidor (secundária) e Assaf Neto em reproduções não autorizadas. Nada na literatura acadêmica.
- Dependem dele: "linear por fora, composta por dentro", "taxa nominal" (l.157), "Saiu uma taxa nominal, entrou uma efetiva" (l.159) e "Em 1998, trocou uma taxa nominal por uma efetiva" (l.212) — a espinha de A1.
- **Resolução possível pelo autor:** o próprio exemplar do Assaf Neto (capítulo de taxa over, com página).
- **Saída de reserva (só Garcia):** "Antes de 1998, cotava-se ao mês: as taxas 'tornaram-se mensalizadas no Brasil devido à megainflação', escreveu Márcio Garcia." Caem "linear por fora" e "taxa nominal" das três frases — mudança de espinha, vai ao gate.

---

## Item por item

### 1. Números

| l. | Afirmação | Recálculo | Veredito |
|---|---|---|---|
| 49–53 | R$ 70 mil; 67.707,83; 2.292,17 | 70.000,00; 67.707,8252; 2.292,1748 | ✓ |
| 89 | ln(1,14) = 13,10%; e^0,14 → 15,03% | 0,131028; 1,150274 | ✓ |
| 101 | 219.800,00 / 217.186,92 / 2.613,08 | 219.800,0000; 217.186,9207; 2.613,0793 | ✓ |
| 101 | "mesma diferença de meio período, carregada por mais um ano" | identidade exata 1,14 × (1,07 − 1,14^0,5) | ✓ |
| 109–113 | C(1+i) em t = 1; máximo perto de 6 meses; 1.070,00 × 1.067,71; 1.140,00 | t* = 0,5055 ano; distância máx. R$ 2,2924 (em 0,5: 2,2922) | ✓ |
| 133 | 299,60 = 280,00 + 19,60 | 1,14² = 1,2996 | ✓ |
| 137 | virada > 1 década a 14%; > 2 a 6% | 14% → 10,42; 6% → 22,40; **10% → 14,02**; 12% → 11,92 | ✓ |
| 149–153 | 1,1449; 1,14^0,5 × 1,14^0,5 = 1,14 | ✓ | ✓ |
| 161 | Garcia 1,42% / 1,82% / 40 pb (21,84% a.a.) | diária 0,07843%; 1,4212%; 1,8195%; 39,83 pb; fev/98 18 du, jul/98 23 du | ✓ |
| 195 | 1,035389 → 14,92%; 0,75 motor (14,75%) + 0,17 régua | 14,9249%; 14,7523%; 0,7523 + 0,1726 | ✓ (P-5, P-6) |
| 195 | 91 dc com 63 du | existe | ✓ (P-1) |
| 197 | 14% × 365/360 = 14,19% | 14,1944% | ✓ (R-7) |
| 216 | 12% cap. mensal → 12,68% | 12,6825% | ✓ |

**Para a etapa 8:** graf-01 — distância reta–curva = 0,215% do montante em seis meses (invisível em escala natural). graf-02 — em anos inteiros, a virada cai no 11º ano a 14%, no 15º a 10%, no 23º a 6%; parcela do juro sobre juro em 10 anos: 48,3% / 37,3% / 24,1%.
**Realidade:** meta Selic 13,75% (SGS 432), Selic over 13,65% em 04/11/2026 (SGS 1178). 14% plausível; 6% como juro real, aceitável.

### 2. Afirmações matemáticas
- ✓ Corda acima da curva em (0, 1), abaixo fora dele (bate com l.113).
- ⚠ Bernoulli: R-5.
- ✓ "Constante de Euler" → "número de Euler" (item 14 resolve).
- ✗ l.193: B-1.
- ✓ l.117 (mesmo número, mesma régua). ✓ l.89 (identidade contínua). ✓ item 50 "aditivos" (retornos log).
- ✓ Item 28: (a) 15 dias: i·f com f = 15/dc do mês ∈ [0,48; 0,54] ("cerca de metade dela" ✓), e i·f > (1+i)^f − 1; (b) muitos meses: Σiₖ < Π(1+iₖ) − 1 (taxa negativa travada em zero, §3º do art. 406). Ressalva sem mudança: com taxa mensal variável, "reta" é poligonal e "curva" é produto; a imagem vale.

### 3. Fatos e normas
- ✓ Circular 2.761: 18/06/1997; "Altera a forma de expressão…"; art. 1º fator diário médio ^252; art. 4º "01.01.98"; revogada (API: Res. BCB 157/2021). Texto no passado, sem sugerir vigência.
- ⚠ Over "efetiva-dia": R-1. [VERIFICAR] × 30: V-1.
- ✓ Over × Selic: mesma família (Res. BCB 46/2020, art. 1º); ponte R-2.
- ✓ Garcia 1997 (p. 1 inflação; p. 2 fevereiro × julho; p. 3 "não se trata de volatilidade"); item 45 ✓.
- ✓ Comunicado 7.684 (íntegra): 11/07/2000, DEMAB, não revogado; "a partir de 1. de agosto de 2000"; item II "taxa efetiva anual (i), considerando-se 252 dias úteis"; item 3 "em suas operações de compra e venda de títulos públicos federais". Alcance confere; precisão P-3.
- ✓ DDI/FRC linear base 360 dc (du252/07). ⚠ "sempre": R-4.
- ✓ Treasuries accrued linear (31 CFR 356, Ap. B, I.D; exemplo 92/184 × 33,75 = $16,875).
- ✓ CMN 5.171 art. 6º literal; 29/08/2024; não revogada; item 26 ✓; glosa R-6.
- ⚠ Susep: R-3. ✓ Black-Scholes-Merton contínuo (consenso; slides Hull cap. 4).
- ✓ "Quase toda a renda fixa em reais, t = du/252" (Selic, Taxa DI, LTN, DI1; CDB padrão, não regra).
- ✓ "Barriga da curva de juros" (Reuters/Forbes Brasil, 09/02/2022). ✓ Einstein (Quote Investigator). ✓ "Como contei no texto anterior".
- Sem marcador, não conferido: "anatocismo" (definição consolidada); remissões à LCA e à debênture (textos da série).

### 4. Planilha
- ✓ `=(1+i)^(du/252)` · ✓ `=1+i*dc/360` · ✓ `=(1+i_lin*dc/360)^(252/du)-1` (i em decimal; nomes são pseudocódigo) · ✗ `=DIATRABALHOTOTAL(início;fim;feriados)-1`: B-2.

### 5. Bibliografia — redação final proposta
1. **Alexandre Assaf Neto**, *Matemática Financeira e suas Aplicações*, 15ª ed. (GEN Atlas, 2022) — a referência brasileira para regimes, convenção linear e exponencial em prazos quebrados e taxa over. (Edição/ISBN 9786559773237 via livraria; cobertura via programas de disciplina, secundária.)
2. **Carlos Patricio Samanez**, *Matemática Financeira*, 5ª ed. (Pearson Prentice Hall, 2010) — outro manual brasileiro de referência, bom para treinar o teste de transferência. ("Com mais exercícios…" pode voltar se o autor confirmar no exemplar.)
3. **John C. Hull**, *Options, Futures, and Other Derivatives*, 11ª ed. (Pearson, 2021), cap. 4, "Interest Rates" — frequência de capitalização, taxa contínua e conversões, na língua do mercado internacional. (Pearson confirma; não citar seção.)
4. **Márcio G. P. Garcia**, [*Efeitos da anualização da taxa Selic*](https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf) (Departamento de Economia da PUC-Rio, 30/06/1997) — o registro de época da mudança de 1998 e de seus efeitos nas taxas mensais.

## Itens da etapa 6 dependentes

| Item | Veredito |
|---|---|
| 28 | ✓ |
| 56 | ✓ (P-6 opcional) |
| C1 Samanez | ✗ → B-3 |
| C2 Euler | ✓ com item 14 |
| C3 taxa legal | ✓ → R-6 |
| C4 over × Selic | ✓ → R-2 |
| C5 365/360 | ✓ → R-7 |
| C6 ANBIMA | resolvido por B-2; glosa se ficar |
| 43, 45, 26, 38, 49, 54 | ✓ |
| 50 | ✓ menos a cláusula da Susep (R-3) |

## Lista consolidada para o texto final
- **[VERIFICAR] que fica:** l.157 `[VERIFICAR: convenção da taxa over mensal como taxa por dia útil × 30, antes de 1998, com fonte de livro-texto (Assaf Neto, capítulo de taxa over, com página)]` (afeta l.159 e l.212). Só se o autor recusar R-3: `[VERIFICAR: se a Susep publica as ETTJ convertidas para taxa discreta]`.
- **Saem:** [VERIFICAR] do Comunicado 7.684, das pontas/calendário e das edições.
- **[FAIXA]:** nenhum.
- **Bloqueantes:** B-1, B-2, B-3. **Recomendadas:** R-1 a R-8. **Opcionais:** P-1 a P-7.

## Fontes (acesso em 04/11/2026)
- BCB, API de normativos: Circulares 2.347, 2.720, 2.761, 2.780; Comunicado 7.684 (`exibeoutrasnormas`); Res. BCB 46; Res. CMN 5.171 (PDF: https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolu%C3%A7%C3%A3o5171.pdf); SGS 432 e 1178.
- Garcia (1997): https://www.econ.puc-rio.br/mgarcia/Artigos/Macrometrica/!MACROMT.RIC/!anuliz.pdf
- Susep, Relatório Técnico 23/06/2022: https://www.gov.br/susep/pt-br/arquivos/arquivos-solvencia-supervisao-prudencial/capital-minimo-requerido-e-tap/relatorio-ettj-novo-metodo-20220623.pdf/@@download/file
- 31 CFR 356, Ap. B: https://www.law.cornell.edu/cfr/text/31/appendix-B_to_part_356
- Art. 406 CC (Lei 14.905/2024), reprodução: https://www.irib.org.br/lei-n-14-905-de-28-de-junho-de-2024/
- Planilhas: Microsoft https://support.microsoft.com/pt-br/office/fun%C3%A7%C3%A3o-diatrabalhototal-48e717bf-a7a3-495f-969e-5005e3eb18e7 · Google https://support.google.com/docs/table/25273?hl=pt-BR · LibreOffice https://help.libreoffice.org/latest/pt-BR/text/scalc/01/func_networkdays.html
- Bibliografia: Assaf Neto https://www.martinsfontespaulista.com.br/matematica-financeira-e-suas-aplicacoes-1004941/p · Samanez https://biblioteca.ifac.edu.br//bib/33168 · Hull https://www.pearson.com/en-us/subject-catalog/p/options-futures-and-other-derivatives/P200000005938/9780136939979 · sumário secundário https://toc.uni.li/FLMF056124.pdf
- Reaproveitado do du252/07: DDI/FRC (B3), OC 055/2024-PRE, Tesouro, slides Hull cap. 6, ANBIMA, `bizdays`.

---

## Decisões do autor (2026-11-04)

- **Bloqueantes B-1, B-2, B-3:** aplicados por padrão (precedente du252).
- **V-1:** manter a espinha nominal × efetiva com `[VERIFICAR]` na l.157; o autor confere no próprio
  exemplar do Assaf Neto antes de publicar. Vai ao gate como pendência.
- **R-1 a R-8:** aplicar todas.
- **Opcionais P-1 a P-7:** nenhum aplicado.
- Aplicação: etapa 9 (consolidação).
