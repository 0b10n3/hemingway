# Etapa 7: Verificação técnica

Executor: subagente `verificador-tecnico`. Texto conferido: corpo de `processo/04-draft-v1.md`, de
"# A Peça Mais Simples" até "Para continuar aprendendo". Fontes acessadas em **2026-11-23**. Os
vereditos de `03-pesquisa.md` foram reaproveitados onde a fonte primária já estava citada. O que pesa
foi reaberto: os números do texto, o superlativo da abertura, as séries do Tesouro Direto, o Focus, os
anexos do RMD e o calendário da ANBIMA.

**Registro do cálculo.** Por restrição desta rodada, só este arquivo pode ser escrito. O registro que
`verificador-tecnico.md` pede em `_revisoes/2026-11-23_2026-11-23-a-peca-mais-simples_calculo.md`
está no **Apêndice A**: dois scripts em `python3`, só com biblioteca padrão, e a saída integral. Se a
conversa principal quiser o arquivo em `_revisoes/`, basta mover o apêndice para lá e deixar aqui um
ponteiro, para manter uma fonte por fato.

**Placar:** 109 itens conferidos. São 3 correções bloqueantes (C1 a C3), 3 imprecisões (C4 a C6, das
quais C5 e C6 são leves) e 1 `[VERIFICAR]` novo (V1, na descrição do Securato). Nenhum `[FAIXA]`.
- O superlativo da abertura passa a ter **fonte primária**: a API de leilões do Selic, do BCB. Fica
  como a etapa 4 deixou.
- "Suspendeu as negociações mais de uma vez" fica, apoiado em fonte secundária.
- Os demais números do texto conferem no recálculo, inclusive a frase nova da etapa 4 (Focus +0,75 e
  +0,5; divisão de 2,58 em 0,54 + 2,04).

---

## Correções (aceitar por ID)

**C1. Bloqueante (cálculo).** Tabela dos três cenários, linha "Segue o Focus". As premissas do próprio
rascunho são:
- Selic interpolada em linha reta entre os fins de ano (13,75% → 12,75% → 11%);
- CDI = meta − 0,10;
- 529 du, de 18/11/2026 a 01/01/2029.

Com elas, R$ 10 mil viram **R$ 12.811,95**: R$ 12.812,12 se a interpolação for em dias úteis, e
R$ 12.812,17 com a "Selic média de 12,53%" das Notas de revisão. Os R$ 12.818 saem quando só essa
linha conta **530 du**, a partir de 17/11 (R$ 12.818,46). As outras duas linhas e o Prefixado usam
529. A diferença é de R$ 6, mas é divergência de cálculo e é a linha que o texto manda o leitor
"repar[ar]".
- `| Segue o Focus (trajetória interpolada entre os fins de ano) | R$ 12.818 | R$ 13.405 |`
  → `| Segue o Focus (trajetória interpolada entre os fins de ano) | R$ 12.812 | R$ 13.405 |`

"Cerca de 2,5 pontos percentuais" não muda: a diferença é de 2,45 p.p. contra a Selic diária média.
`graficos.md` e `infograficos.md` não usam esse número.

**C2. Bloqueante (premissa não declarada).** Os R$ 13.081 e os R$ 13.631 só saem com a Selic diária
(over) 0,10 ponto abaixo da meta. O leitor que refizer a conta com o rótulo da tabela chega a outros
números:

| Linha | Número do texto | Premissa que o reproduz | Com o rótulo ao pé da letra |
|---|---|---|---|
| "Fica parada em 13,75%" | R$ 13.081 | over de 13,65% | R$ 13.106 |
| "Média de 16% ao ano" | R$ 13.631 | meta de 16% e CDI de 15,90% | R$ 13.656 |

**Sim, a tabela precisa dizer que o cenário é de meta e que o Tesouro Selic rende 0,10 ponto abaixo
dela.** O texto se apresenta como aula, e o leitor que conferir a linha de 16% erra por R$ 25.
Proposta exata, que exige uma inserção curta (se o autor não aceitar o texto como está, a correção
volta à etapa 4):
- `| Cenário para a Selic | No Tesouro Selic | No Prefixado 2029 |`
  → `| Cenário para a meta da Selic | No Tesouro Selic | No Prefixado 2029 |`
- `Para medir a distância, três cenários para R$ 10 mil aplicados em 17 de novembro, até 1º de janeiro de 2029, em valores brutos e cálculo próprio:`
  → `Para medir a distância, três cenários para R$ 10 mil aplicados em 17 de novembro, até 1º de janeiro de 2029, em valores brutos e cálculo próprio, com o Tesouro Selic rendendo a Selic de cada dia, 0,10 ponto abaixo da meta:`

Não recomendo a alternativa sem prosa nova, que seria recalcular tudo com over = meta (R$ 12.836,
R$ 13.106 e R$ 13.656). Ela superestima o que o Tesouro Selic paga, porque a SGS 1178 ficou em 13,65%
com a meta em 13,75% em todos os dias de 13/10 a 19/11.

**C3. Bloqueante (o −3,6% atribuído a quem comprou; M16, pesquisa item 39).** O −3,6% compara **dois
preços de compra**: R$ 746,00 contra R$ 773,74, ou −3,585%. A posição de quem comprou em 13/10 era
marcada, em 17/11, pelo **PU base** (taxa de venda, D0) de R$ 743,95. É o valor do extrato e o que
receberia quem vendesse: **−3,85%** (CSV oficial do Tesouro Transparente; metadados: o PU base
"valoriza os títulos para marcar a mercado os títulos adquiridos no Tesouro Direto").

**Redação correta (opção A, recomendada):** o 3,6% fica como queda do preço do título, que é a mesma
base da decomposição (compra contra compra). As frases que o atribuem a quem comprou ou a quem vende
perdem o número. São três trocas curtas, aplicáveis na etapa 9:
- `Quem comprou em 13 de outubro via 3,6% a menos na tela.` → `Na tela, 3,6% a menos que em 13 de outubro.`
- `Os −3,6% de novembro só viram prejuízo para quem vende.` → `A queda de novembro só vira prejuízo para quem vende.`
- `Os −3,6% não são o resultado da aposta. São o preço de sair dela hoje.` → `A queda não é o resultado da aposta. É o preço de sair dela hoje.`

Ficam como estão, porque falam do preço:
- "o Prefixado 2029 perdeu 3,6%" (Mito);
- "as duas dão os −3,58% da tela" (decomposição): 1,0112 × 0,9535 − 1 = −3,58%, e a tela de compra
  dá −3,585%.

**Opção B (volta à etapa 4):** manter o ponto de vista de quem comprou, com "cerca de 3,9%" no extrato.
Uma frase teria de explicar os 0,27 ponto de diferença para o −3,58% da decomposição, que vêm do
*spread* de 0,12 ponto entre a taxa de compra e a de venda.

**C4. Impreciso.** "Na prateleira do Tesouro Direto, as respostas formam cinco papeis". O CSV oficial
mostra **oito** nomes à venda em 17/11/2026: os cinco da tabela, mais Tesouro IGPM+ com Juros
Semestrais (NTN-C), Tesouro Renda+ Aposentadoria Extra e Tesouro Educa+ (os dois últimos são NTN-B1).
A troca da etapa 4 (de "Nos leilões de hoje", que eram quatro) resolveu um erro e abriu outro. A
correção é de uma palavra, aplicável na etapa 9:
- `Na prateleira do Tesouro Direto, as respostas formam cinco papeis:` → `Na prateleira do Tesouro Direto, as respostas formam cinco papeis principais:`

O acento de "papéis" fica com a etapa 6.

**C5. Impreciso (leve).** "Em 8 de outubro, a curva cobrava pouco prêmio: LTNs de 2028 e 2029 a
12,5%, menos de um ponto acima do que o Focus da época esperava". Pelo método do próprio texto (Focus
de 2/10: 13,50 / 12,00 / 10,50 / 10,00; interpolação; over = meta − 0,10):

| Título | Taxa | Selic média esperada | Diferença |
|---|---|---|---|
| LTN 01/01/2028 (leilão) | 12,55% | 12,80% | **−0,25 p.p.** (abaixo) |
| LTN 01/07/2029 (leilão) | 12,51% | 11,72% | +0,79 p.p. |
| Prefixado 01/01/2029 (Tesouro Direto, 8/10) | 12,53% | 12,06% | +0,47 p.p. |

A tese do "pouco prêmio" sai mais forte, mas "acima" não vale para 2028. Correção por supressão:
- `LTNs de 2028 e 2029 a 12,5%, menos de um ponto acima` → `LTNs de 2029 a 12,5%, menos de um ponto acima`

**C6. Impreciso (leve).** *Dealers*: "Em troca, só eles entram na segunda rodada, logo depois do
leilão, ao mesmo preço." Na Resenha do BCB de 5 a 9/10 (Tabela 2), as operações especiais do leilão de
8/10 têm data de **9/10** (o dia útil seguinte), liquidação em 13/10 e a mesma taxa média. O "logo"
não se sustenta para o caso do texto. Correção por supressão:
- `Em troca, só eles entram na segunda rodada, logo depois do leilão, ao mesmo preço.` → `Em troca, só eles entram na segunda rodada, depois do leilão, ao mesmo preço.`

**Sem correção (marcadores fechados):** M12 (suspensões) e M13 (superlativo). Ver F5 e N43; nenhum
dos dois vira `[VERIFICAR]`.

---

## Decisões pedidas pela conversa principal

1. **Superlativo da abertura (M13): fica como a etapa 4 deixou.** Agora há fonte primária. A API
   pública de leilões do Selic (BCB, `olinda.bcb.gov.br/.../leiloes_selic`) dá o volume de primeira
   rodada de prefixados (LTN + NTN-F) por leilão, de 2020 a 2026. Em 8/10/2026 foram
   **R$ 33.283,9 milhões**. Os quatro leilões maiores desde 2020 são todos de 2020, e o último deles
   foi em **10/12/2020** (R$ 44.282,9 milhões). Depois dele, os maiores foram 16/04/2026
   (R$ 27.170,9 milhões) e 03/09/2026 (R$ 26.579,2 milhões).

   O dado também confirma duas leituras que o texto não usa. Só em LTN, os R$ 27,86 bi também são a
   maior primeira rodada desde 10/12/2020; o seguinte é 14/01/2021, com R$ 23,4 bi. Com a segunda
   rodada, os R$ 41,0 bi também são o maior volume desde então. A redação original do rascunho
   (superlativo ao lado dos R$ 27,86 bi de LTN) também estaria certa. A da etapa 4 está certa e é mais
   precisa: decisão de estilo do autor, não de fato.
2. **"O Tesouro Direto suspendeu as negociações mais de uma vez" (M12): fica.** Não existe fonte
   oficial com horário: as páginas de aviso do Tesouro Direto bloqueiam leitura automática.
   - A suspensão em si tem quatro fontes secundárias. A InvestNews cita o aviso oficial das 10h; Seu
     Dinheiro, Times Brasil e Investidor10 confirmam.
   - O "mais de uma vez" está no Investidor10, que reli nesta etapa (26/10, 18h). A matéria diz
     "suspensas" por volta do meio-dia, "retomadas" às 15h38 e "o Tesouro Direto suspendeu novamente
     as negociações" por volta das 16h25.
   - Um resumo de busca do EuQueroInvestir fala em nova suspensão por volta das 13h25, mas a página
     devolveu 404 e não a li.
   - Se o autor preferir risco zero, a supressão de "mais de uma vez" é aplicável na etapa 9.
3. **"Na tela" (M16):** a redação correta é a da opção A em C3.
4. **Tabela dos cenários:** precisa declarar "meta" e o −0,10 (C2). Os números das linhas 2 e 3
   estão certos com essa premissa; o da linha 1 tem de ser corrigido (C1).

---

## Números, item a item

| # | Afirmação no texto | Recálculo (python3, Apêndice A) | Veredito |
|---|---|---|---|
| N1 | 529 du de 18/11/2026 a 01/01/2029 (ANBIMA) | 529 (feriados nacionais ANBIMA 2026–2028, lidos do site; 20/11 incluído) | ✅ |
| N2 | 553 du a partir de 14/10/2026; 24 du entre as datas | 553; 553 − 529 = 24; du(14/10, 18/11) = 24 | ✅ |
| N3 | Expoente 529/252 = 2,09920634920634 (T-14) | 2,09920634920634 | ✅ Metodologia, Tabela 3 ("Exponencial de Dias" T-14, PU T-6) |
| N4 | 1,1498 elevado a ele = 1,340475 | 1,34047502 | ✅ |
| N5 | PU = 746,004202 | trunc₆(1000 / 1,1498^2,09920634920634) = 746,004202 | ✅ |
| N6 | "A tela do Tesouro Direto mostrava R$ 746,00" | CSV oficial, 17/11: PU compra 746,00. A fórmula com D+1 reproduz ao centavo as **34 de 34** datas-base de 01/10 a 19/11 | ✅ |
| N7 | R$ 773,741961 e 553 du devolvem 12,40% | 12,400000% (e trunc₆ a 12,40% dá 773,741961) | ✅ |
| N8 | Planilha `DIATRABALHOTOTAL(liquidação; vencimento-1; feriados)` | conta de 18/11/2026 a 31/12/2028 inclusive = 529 | ✅ |
| N9 | "Quem divide os 14,98% por 252 erra o preço" | (1 + 0,1498/252)^529 dá R$ 730,25, contra R$ 746,00 | ✅ |
| N10 | *Duration* de 2,10 anos | 529/252 = 2,0992 | ✅ |
| N11 | *Duration* modificada de 1,83 | 2,0992 / 1,1498 = 1,8257 | ✅ |
| N12 | DV01 de R$ 0,14 por título | 746,004 × 1,8257 × 0,0001 = 0,1362 (diferença finita: 0,1362) | ✅ |
| N13 | R$ 182,57 por R$ 1 milhão | 1.000.000 × 1,8257 × 0,0001 = 182,57 (finita: 182,57) | ✅ |
| N14 | +1 p.p. tira 1,80%; −1 p.p. põe 1,85% | −1,8014% e +1,8506% | ✅ |
| N15 | "cerca de R$ 1.800" por ponto em R$ 100 mil | −R$ 1.801 / +R$ 1.851 (1ª ordem: R$ 1.826) | ✅ |
| N16 | 24 du de 13/10 a 17/11 | 24 (nas duas convenções) | ✅ |
| N17 | Carregamento de +1,12% | PU a 12,40% com 529 du = 782,403955; +1,1195% (sem truncar, 1,124^(24/252) − 1 = 1,1195%) | ✅ |
| N18 | Alta de 2,58 pontos tirou 4,65% | 14,98 − 12,40 = 2,58; 746,004202 / 782,403955 − 1 = −4,6523% | ✅ |
| N19 | Compostas (1,0112 × 0,9535) dão −3,58% | −3,5821% (exato: −3,5849%) | ✅ |
| N20 | "o Prefixado 2029 perdeu 3,6%" (preço) | 746,00 / 773,74 − 1 = −3,5852% | ✅ |
| N21 | "Quem comprou em 13 de outubro via 3,6% a menos na tela" | posição marcada pelo PU base: 743,95 / 773,74 − 1 = **−3,8501%** | ⚠️ **C3** |
| N22 | Tesouro Selic rendeu "cerca de 1,2%" | over de 13,65% em 24 du: 1,2261%. CSV, Tesouro Selic 2029, compra 13/10 → compra 17/11: 1,2129% (PU base → PU base: 1,2139%) | ✅ |
| N23 | 5/10: taxa caiu "mais de um ponto", de 13,83% para 12,74% | −1,09 p.p. (CSV: 2/10 → 5/10, pregões seguidos) | ✅ |
| N24 | Empate pede Selic média "perto de 15%" | over de 14,98%; em meta, 15,08%; com o Tesouro Selic 2029 a Selic + 0,05%, 14,92% | ✅ |
| N25 | Cenário Focus: R$ 12.818 | **R$ 12.811,95** (529 du); 530 du daria R$ 12.818,46 | ⚠️ **C1** (bloqueante) |
| N26 | Fica parada em 13,75%: R$ 13.081 | R$ 13.081,32 com over de 13,65%; R$ 13.105,50 com 13,75% | ✅ o número; ⚠️ **C2** a premissa |
| N27 | Média de 16%: R$ 13.631 | R$ 13.630,89 com meta de 16% e CDI de 15,90%; R$ 13.655,59 com 16% | ✅ o número; ⚠️ **C2** a premissa |
| N28 | Prefixado 2029: R$ 13.405 | 10.000 × 1000 / 746,004202 = R$ 13.404,75 | ✅ |
| N29 | "cerca de 2,5 pontos percentuais por ano acima da Selic média esperada" | 14,98 − 12,53 = 2,45 p.p. (contra a meta média: 2,35) | ✅ (a base certa é a over, que é o que a LFT paga) |
| N30 | Selic média esperada de 12,53% (premissa nas Notas) | 12,529% (dias corridos) / 12,530% (dias úteis) | ✅ |
| N31 | Focus subiu 0,75 ponto (fim de 2027) e meio ponto (fim de 2028) | PDFs do Focus: 2/10 e 9/10 com 12,00 e 10,50; 13/11 com 12,75 e 11,00. +0,75 e +0,50 | ✅ (ver Contexto 2) |
| N32 | Dos 2,58 pontos, cerca de meio ponto de expectativa e dois de prêmio | Selic média esperada: 11,99% em 14/10 (Focus de 9/10) e 12,53% em 18/11 (Focus de 13/11). **0,54 + 2,04**. Com o Focus de 2/10: 0,47 + 2,11 | ✅ |
| N33 | 8/10: LTNs de 2028 e 2029 "menos de um ponto acima" do Focus | 2028: −0,25; jul/2029: +0,79; jan/2029 (Tesouro Direto): +0,47 | ⚠️ **C5** |
| N34 | 100 títulos custavam R$ 74.600,42 | 100 × 746,004202 = 74.600,4202 → T-2 = 74.600,42 (Tabela 3, valor financeiro T-2) | ✅ |
| N35 | IR de 15% "como o prazo passa de 720 dias" | 18/11/2026 → 01/01/2029 = 775 dias corridos | ✅ |
| N36 | Cada título entrega R$ 961,90 | 1000 − 0,15 × 253,995798 = 961,900630 | ✅ |
| N37 | Taxa líquida de 12,87% | (961,900630 / 746,004202)^(252/529) − 1 = 12,8720% | ✅ |
| N38 | CDB a 16%: "cerca de R$ 732" por R$ 1.000 de face (M9) | 1000 / 1,16^(529/252) = 732,30 (com 530 du, D0: 731,87) | ✅ |
| N39 | "em 18 dias" (8/10 → 26/10) | 18 dias corridos | ✅ |
| N40 | NTN-F 2031 "vendido caro e recomprado barato" | PU médio no leilão de 8/10: 950,119225 (BCB, API de leilões); na recompra de 26/10: R$ 4.351,2 mi / 5 milhões = 870,24. PU teórico: 950,06 a 12,61% e 870,24 a 15,79% | ✅ (−8,4% por título) |
| N41 | Recompra de 5 milhões de NTN-F 2031 a 15,79%, "cerca de R$ 7,1 bilhões em prefixados" | BCB, API: 2031 (5.000.000; 15,79%; R$ 4.351,2 mi) + 2033 (R$ 1.983,2 mi) + 2037 (R$ 773,4 mi) = R$ 7.107,8 mi | ✅ |
| N42 | R$ 33,28 bi em prefixados, R$ 27,86 bi em LTN | primeira rodada: LTN R$ 27.856,2 mi + NTN-F R$ 5.427,8 mi = R$ 33.283,9 mi | ✅ |
| N43 | "o maior volume em prefixados numa primeira rodada desde dezembro de 2020" | BCB, API de leilões do Selic: maior desde 10/12/2020 (ver Decisões, item 1) | ✅ fonte primária |
| N44 | Taxas "perto de 12,5%" | 12,5462 / 12,5078 / 12,7028%; média ponderada da primeira rodada de 12,54% | ✅ |
| N45 | "Travou dívida barata por dois anos" | prazo médio ponderado das LTN de 8/10: 1,89 ano | ✅ |
| N46 | Prazos "de alguns meses a pouco mais de cinco anos" | Tesouro Direto em 17/11: Prefixado 2027 (≈1,5 mês) a 2032 (≈5,1 anos); leilão de 8/10 até 1/1/2032 (≈5,2 anos) | ✅ |

---

## Fatos, fontes e definições

| Item | Afirmação | Fonte | Veredito |
|---|---|---|---|
| F1 | Selic em 13,75%; "não se mexeu" entre 13/10 e 17/11 | SGS 432: 13,75 em todos os dias de 13/10 a 19/11 (38 observações). 281ª (16/9) e 282ª (4/11) na pesquisa | ✅ |
| F2 | "o Copom se reuniu uma vez, não mudou nada" | 282ª reunião, 04/11/2026 (pesquisa) | ✅ |
| F3 | Lula reeleito em 25/10 | TSE (pesquisa) | ✅ |
| F4 | "No pregão seguinte, os juros futuros dispararam" | BCB, Resenha de 26 a 30/10, Tabela 4: *swap* de 2 anos de 12,67% para 15,18% (pesquisa) | ✅ |
| F5 | "o Tesouro Direto suspendeu as negociações mais de uma vez" | Investidor10 (relido), InvestNews, Seu Dinheiro, Times Brasil | ✅ fonte secundária; fica (Decisões, item 2) |
| F6 | "o Tesouro cancelou o leilão de prefixados da semana para, no lugar dele, recomprar títulos" | BCB, Resenha de 26 a 30/10; API de leilões (recompras de 26/10) | ✅ |
| F7 | Prefixado 2029 em 13/10: R$ 773,74 a 12,40% | CSV do Tesouro Transparente (baixado nesta etapa) | ✅ |
| F8 | Em 17/11: R$ 746,00 a 14,98% | Idem | ✅ |
| F9 | "Na prateleira do Tesouro Direto, as respostas formam cinco papeis" | CSV, 17/11: oito nomes à venda | ⚠️ **C4** |
| F10 | Tabela: indexador, cupom de 10% e de 6% ao ano em duas parcelas, sem cupom nos demais | Metodologia, Tabela 1; Decreto 12.814 | ✅ |
| F11 | Selic (sistema) operado pelo BCB, onde a propriedade e os pagamentos são controlados | Decreto 12.814, art. 27 (pesquisa); BCB, página do Selic | ✅ |
| F12 | Vencimentos sempre no primeiro dia de jan/abr/jul/out | CSV (prática desde 2004); o decreto não fixa datas (pesquisa) | ✅ como prática; o texto não diz que é norma |
| F13 | Leilão de 8/10 vendeu vencimentos de 2028, 2029 e 2032 | BCB, API de leilões e Resenha | ✅ |
| F14 | IR regressivo de 22,5% a 15%; IOF nos 30 primeiros dias; não residente com alíquota zero, salvo paraíso fiscal | Lei 11.033/2004, art. 1º; Decreto 6.306/2007; Lei 11.312/2006, art. 1º (pesquisa, Planalto) | ✅ |
| F15 | R$ 42,9 bi de prefixados no secundário em 5/10 | BCB, Resenha de 5 a 9/10, Tabela 3 (pesquisa) | ✅ |
| F16 | Recompra diária pelo Tesouro, a preço de mercado; em 26/10, "suspensa por horas" | Tesouro Direto; aviso das 10h e retomada às 15h38 (InvestNews, Investidor10) | ✅ |
| F17 | "A LFT costuma sair mais barata" | RMD, Anexo 4.3: em 102 de 121 meses (2010–2020) (pesquisa) | ✅ com a nuance do "costuma" |
| F18 | PAF revisado em 26/08: 20–24% de prefixados, 49–53% atrelados à Selic; 21,14% em setembro | *Informe* de 26/08/2026; RMD de set/2026 (pesquisa) | ✅ ("atrelados à Selic" traduz "taxa flutuante") |
| F19 | LTN e NTN-F às quintas; LFT e NTN-B às terças | Resenha de 5 a 9/10 (terça 6/10, quinta 8/10) | ✅ |
| F20 | *Dealers*: até 12, "bancos e corretoras", Portaria STN/MF 182/2024 | Tesouro, página de *dealers* (modificada em 03/11/2026): "12 dealers, dos quais nove são bancos e três são corretoras ou distribuidoras", rege a Portaria 182/2024 | ✅ |
| F21 | Segunda rodada "logo depois do leilão, ao mesmo preço" | Resenha de 5 a 9/10, Tabela 2: data de 9/10, mesma taxa | ✅ o preço; ⚠️ **C6** o "logo" |
| F22 | NTN-F 2031 vendida a 12,61% em 8/10, no mesmo leilão das LTNs | BCB, API: taxa média de 12,6079%, 4.178.100 títulos | ✅ |
| F23 | BCB não emite títulos desde 2002, LRF art. 34 | LC 101/2000, art. 34 (pesquisa, Planalto) | ✅ |
| F24 | Compromissadas de um dia com média de R$ 885,7 bi por dia (5 a 9/10); lastro LFT, LTN, NTN-B e NTN-F nas mais longas | Resenha de 5 a 9/10, texto (relido) | ✅ |
| F25 | Detentores em set/2026: 31,33% / 22,93% / 22,41% / 9,58%; Tesouro Direto 3,09% | RMD set/2026, Anexo 2.7 (relido do XLSX): 0,31327 / 0,22933 / 0,22407 / 0,09577 / 0,03091; estoque de R$ 9.037,54 bi | ✅ |
| F26 | Focus de 16/11: 13,75% / 12,75% / 11% | BCB, `R20261113.pdf` (data-base 13/11; relido) | ✅ |
| F27 | Focus "da época": 12% no fim de 2027 e 10,5% no fim de 2028 | `R20261002.pdf` (relido): 13,50 / 12,00 / 10,50 / 10,00 | ✅ |
| F28 | O BCB mede o prêmio, que sobe nas turbulências, como em 2008 e nas eleições de 2022 (RI de dez/2022) | Boxe do RI de dez/2022 (pesquisa, item 6, com citação literal) | ✅ |
| F29 | Custódia da B3 de 0,20% ao ano | B3, tarifas do Tesouro Direto (pesquisa) | ✅ |
| F30 | "a LTN só vence em quatro dias por ano" | prática de emissão (F12) | ✅ (no Tesouro Direto, só janeiro: Contexto 6) |
| F31 | Quatro textos seguidos com a LTN; títulos citados entre aspas | `posts/*/post.md` (LTN aparece nos quatro); título publicado de 30/10: "Você está contando os dias errado" (`estilo/corpus/mapa-publicados.json`); "A Corda e o Arco", "Frequência de Capitalização", "Cara, eu ganho. Coroa, eu não perco." | ✅ |
| F32 | "No fim do último texto, prometi … *bootstrapping*"; "uma NTN-F foi montada com três LTNs" | `posts/2026-11-18-…/post.md`, linhas 147 e 268 | ✅ |
| F33 | *Bootstrapping*: façanha impossível de se erguer pelas alças da bota; "na versão alemã", Münchhausen sai do pântano pelo próprio cabelo | Wikipedia, "Bootstrapping": a expressão era usada no século XIX "as an example of an impossible task"; nas histórias, o barão sai do pântano "by his hair (specifically, his pigtail), not by his bootstraps" | ✅ Na versão inglesa de Raspe que busquei (Standard Ebooks), o episódio não aparece, o que é coerente com "versão alemã" (Bürger) |
| F34 | Skill Check: gratuito; dimensões "mercados e produtos" e "matemática financeira" | `marketing/catalogo.json` (`oferta:skill-check`); link responde HTTP 200 | ✅ |
| F35 | Garantia: "o lastro mais aceito no interbancário, em compromissadas e em chamadas de margem" | Compromissadas do BCB lastreadas em títulos federais (Resenha); B3 lista o título público federal entre as garantias aceitas; Circular 3.749, art. 6º | ✅ qualitativo. Não há ranking numérico; a gaveta é candidata a corte (M8) |
| F36 | Banco que empresta prefixado e capta no CDI carrega a mesma aposta da LTN | descasamento ativo prefixado × passivo pós-fixado | ✅ conceito |
| D1 | LTN: valor nominal múltiplo de R$ 1.000, rendimento pelo deságio, resgate no vencimento (art. 2º) | Decreto 12.814/2026, art. 2º (relido no Planalto): incisos III, IV e V literais | ✅ |
| D2 | *Duration*: "prazo médio dos fluxos, ponderado pelo valor presente de cada um"; numa LTN, o próprio prazo | definição de Macaulay; Tuckman e Serrat, cap. 4; Securato (sinopse: "duration e convexidade") | ✅ |
| D3 | *Duration* modificada = *duration* / (1 + i): variação percentual do preço por ponto de taxa | com capitalização anual (du/252 no expoente), −(1/P)·dP/di = (du/252)/(1 + i) | ✅ (aproximação de 1ª ordem; N14 mostra a diferença) |
| D4 | DV01: valor de um ponto-base | Tuckman e Serrat, cap. 4 ("DV01, Duration, and Convexity") | ✅ |
| D5 | Convexidade como a assimetria entre +1 e −1 p.p. | idem; N14 | ✅ |
| D6 | 1/(1 + i)^(du/252): fator de desconto, o preço hoje de R$ 1 no vencimento | Tuckman e Serrat, cap. 1 ("Prices, Discount Factors, and Arbitrage") | ✅ |
| D7 | Prêmio de prazo: "o que o mercado cobra para travar dinheiro por dois anos numa taxa fixa"; taxa = previsão + seguro | BCB, RI de dez/2022: "diferença de rentabilidade esperada entre um investidor de longo prazo de outro que rola os recursos no overnight" | ✅ simplificação compatível |
| D8 | Compromissada: venda com recompra marcada, que funciona como empréstimo garantido | Resenhas do BCB; prática do Selic | ✅ |
| D9 | LCR: índice de Basileia III que exige ativos líquidos para 30 dias de estresse; título federal é "de primeira linha" | Circular BCB 3.749/2015 (consolidada, v8): LCR = HQLA ÷ saídas líquidas "para um período de trinta dias"; art. 6º, VI: títulos públicos federais aceitos pelo BCB em redesconto intradia são **HQLA de Nível 1** | ✅ |
| D10 | DI futuro: contrato da B3 que troca uma taxa prefixada pelo CDI do período | DI1 da B3 (taxa média de DI de um dia, com ajuste diário) | ✅ simplificação aceitável (economicamente, a posição troca pré por DI acumulado) |
| D11 | *Dealer*: compromisso de comprar no leilão e dar liquidez no secundário; acesso exclusivo à segunda rodada | Tesouro, página de *dealers*; Resenhas ("operações especiais do Tesouro, restritas às instituições dealers") | ✅ |
| D12 | du: liquidação inclusive, vencimento exclusive, sobre 252 | Metodologia (PDF relido): "entre a data de liquidação (inclusive) e a data de vencimento (exclusive)" | ✅ |
| D13 | Taxa efetiva ao ano, base 252 | Metodologia, fórmula da LTN | ✅ |
| D14 | Curva: "a fila de taxas prefixadas, uma por prazo" | definição usual de estrutura a termo | ✅ |
| D15 | Sem FGC no título público "porque não há banco no meio" | o devedor é a União; o FGC cobre depósitos e títulos de instituições associadas | ✅ |
| L1 | Lei nº 10.179/2001 autoriza a emissão | Planalto (pesquisa; arts. 1º e 7º) | ✅ vigente |
| L2 | Decreto nº 12.814, de janeiro de 2026, art. 2º | Planalto (relido): Decreto de 9/1/2026, DOU de 12/1/2026; sem anotação de revogação; o art. 31 revoga o Decreto 11.301/2022 | ✅ vigente |
| L3 | Lei nº 11.033/2004 (IR regressivo) | Planalto (pesquisa); a MP 1.303/2025 perdeu a vigência | ✅ vigente |
| L4 | Lei nº 11.312/2006 (não residente) | Planalto (pesquisa): "reduz a zero a alíquota", com a exceção | ✅ vigente; a redação do texto está precisa |
| L5 | LRF, art. 34 | Planalto (pesquisa) | ✅ vigente |
| L6 | Portaria STN/MF nº 182/2024 | DOU de 8/2/2024 (título da cópia oficial); página do Tesouro de 03/11/2026 a cita como vigente | ✅ (o texto integral não abriu; ver pesquisa, item 42) |
| R1 | Tuckman e Serrat, *Fixed Income Securities: Tools for Today's Markets*, 4ª ed. (Wiley, 2022); capítulos sobre fatores de desconto e sobre DV01 e *duration* | Wiley-VCH: 4ª ed., agosto de 2022, ISBN 978-1-119-83555-4; cap. 1 "Prices, Discount Factors, and Arbitrage"; cap. 4 "DV01, Duration, and Convexity" | ✅ |
| R2 | Securato (coord.), *Cálculo Financeiro das Tesourarias: Bancos e Empresas*, 5ª ed. (Saint Paul, 2015) | Martins Fontes Paulista: "5ª EDIÇÃO - 2015", Saint Paul, ISBN 9788580041149, 544 p.; Securato como autor e organizador | ✅ a ficha |
| R2b | "LTN, LFT e NTN com as convenções locais, du/252 e taxa over incluídas" | a sinopse confirma "formação de preços de títulos públicos", "carregamento de ativos", "duration e convexidade" e tópicos de dívida pública; não menciona LTN, LFT, NTN, du/252 nem taxa over. Sumário não encontrado | ❓ **V1** |
| R3 | Link da Metodologia (PDF em português) | HTTP 200, `application/pdf`; título "Metodologia de Cálculo dos Títulos Públicos Federais Ofertados nos Leilões Primários" | ✅ |
| R4 | Link do PAF 2026 "com a revisão dos limites de 26 de agosto" | HTTP 200; página "Plano Anual de Financiamento (PAF) - 2026"; o *Informe* de 26/08 está na pesquisa (item 17) | ✅ |
| R5 | Regra de referências | 4 itens: 2 livros, 2 documentos do Tesouro; nenhuma lei na bibliografia | ✅ |

---

## Verificações adicionais da linha Notas de um Professor

- **Fórmula, simbólica e numérica.** PU = 1000/(1 + i)^(du/252), com truncamentos e taxa inversa,
  confere com a Metodologia e reproduz a tela do Tesouro Direto em 34 de 34 dias. *Duration*, DV01,
  convexidade, decomposição, IR e CDB conferem. As divergências são C1 (530 × 529 du) e C2 (premissa
  da tabela). Nenhuma é erro de modelo.
- **Aderência à realidade brasileira.** Selic, taxas, du/252 e feriados ANBIMA (inclusive 20/11),
  D+1, IR regressivo, custódia de 0,20% e CDB de banco médio a 16% (cerca de 1 ponto acima da LTN):
  tudo compatível com novembro de 2026.
- **Dois lados do balcão.** ✅ Presentes e fortes. O emissor tem seção própria (custo × risco, PAF,
  leilão, recompra de 26/10 com os números das duas pontas). O BCB aparece como usuário do título
  (compromissadas), os bancos em três gavetas e o investidor em três usos. Não bloqueia.
- **Regra de referências.** ✅ 4 itens, 2 livros. O boxe do BCB de dez/2022 fica citado no corpo, sem
  link (decisão da etapa 4).

---

## Contexto para o autor e para o gate (sem correção no texto)

1. **O superlativo também vale para a redação original do rascunho.** Os R$ 27,86 bi só de LTN são a
   maior primeira rodada de LTN desde 10/12/2020. A troca da etapa 4 partiu de uma dúvida que a fonte
   primária desfez. As duas redações estão certas; a atual é a mais precisa.
2. **A janela do Focus.** Os +0,75 e +0,5 valem para a janela da decomposição: do Focus de 9/10, o
   disponível em 13/10, ao de 13/11. Medido do último Focus antes do 2º turno (23/10: 11,75 e 10,00),
   a alta foi de 1,0 ponto nos dois anos. O comunicado da 282ª reunião também cita inflação acima do
   teto e petróleo (pesquisa, item 23). A frase "a eleição … mudou um pouco a Selic esperada" atribui
   à eleição toda a revisão do Focus na janela, o que é uma leitura e não um dado. Precisão opcional,
   que exige redação: dizer a janela entre parênteses.
3. **O "prêmio" por resíduo.** LTN − Selic média do Focus mistura o prêmio a termo com a distância
   entre o mercado e os economistas (pesquisa, item 35). O texto declara o método ("Pela mesma conta
   dos cenários"), o que basta como aproximação.
4. **Deságio da LFT (M16).** O certo para 2029 é Selic + 0,05% (Tesouro Selic 01/03/2029, CSV de
   17/11), não + 0,11% (que é o de 2031). Só aparece nas Notas de revisão, e o corpo já diz "deixando
   de lado o pequeno deságio". Com + 0,05%, a linha Focus iria a cerca de R$ 12.826 e o empate a
   14,92%. Nada muda no texto.
5. **Detentores só da LTN (pesquisa, item 22).** Reconferido no RMD de set/2026, Anexo 2.8 (XLSX).
   - Estoque de LTN: R$ 1.271,58 bi.
   - Instituições financeiras 43,62%; não residentes 26,38%; fundos 10,06%; previdência 7,61%.
   - Governo 5,23%; outros 2,81%; Tesouro Direto 2,56%; seguradoras 1,73%.

   Pode entrar no gate sem nova verificação.
6. **"Quatro dias por ano".** No Tesouro Direto, em 17/11, só há Prefixados com vencimento em 1º de
   janeiro (2027, 2028, 2029, 2031 e 2032). Para quem compra lá, a escolha é ainda mais estreita
   (pesquisa, item 29).
7. **NTN-F 2031, as duas pontas em reais.** Cerca de R$ 950 por título na venda de 8/10 e R$ 870 na
   recompra de 26/10, ou −8,4%. Fica disponível se o autor quiser um número para "caro" e "barato".
8. **Tensões que não são minhas.** "Aposta contra a curva" × "recebe o prêmio" (pesquisa, item 37)
   segue para a etapa 5. Para a etapa 8: a série do `graf-01` de 2002 a 2026 precisa de emenda entre
   fontes (pesquisa, item 4).
9. **Feriados de 2029 e 2030.** Só entram no PU teórico da NTN-F 2031 (N40). Saíram do calendário da
   Páscoa, não do site da ANBIMA. O PU de 950,06 bate com o implícito de 950,12, então a conferência
   não depende deles.

---

## `[VERIFICAR]` e `[FAIXA]` para o texto final

- `[VERIFICAR]`: **um.**
  - **V1**, logo depois da descrição do Securato em "Para continuar aprendendo": `[VERIFICAR: o autor confirma no exemplar da 5ª ed. que o livro trata de LTN, LFT e NTN com du/252 e taxa over; a sinopse da editora só confirma "formação de preços de títulos públicos", "carregamento de ativos" e "duration e convexidade"]`
  - Saídas possíveis:
    - o autor confirma no exemplar, e o marcador sai;
    - a etapa 4 reescreve a descrição com o que a sinopse confirma;
    - corta-se a segunda frase do item.
- `[FAIXA]`: **nenhum.** "Perto de 12,5%" já é aproximação declarada (12,51% a 12,70%; média
  ponderada de 12,54%).
- Os marcadores M10 a M15 da pesquisa ficam fechados, com M12 e M13 nesta etapa. M16 e M18 fecham
  com C1, C2 e C3; M9 fecha com N38.

---

## Fontes novas desta etapa (acesso em 2026-11-23)

- BCB, API de resultados dos leilões de títulos públicos (Selic/Ofpub), 2020–2026: `https://olinda.bcb.gov.br/olinda/servico/leiloes_selic/versao/v1/odata/leiloesTitulosPublicos(dataMovimentoInicio=@a,dataMovimentoFim=@b,dataLiquidacao=@c,codigoTitulo=@d,dataVencimento=@e,edital=@f,tipoPublico=@g,tipoOferta=@h)?@a='AAAA-01-01'&@b='AAAA-12-31'&@c=''&@d=''&@e=''&@f=null&@g=''&@h=''&$format=json&$top=100000` (dataset: https://dadosabertos.bcb.gov.br/dataset/leiloes-selic)
- Tesouro Transparente, CSV do Tesouro Direto (atualizado em 20/11, última data-base 19/11): https://www.tesourotransparente.gov.br/ckan/dataset/df56aa42-484a-4a59-8184-7676580c81e3/resource/796d2059-14e9-44e3-80c9-2d9e30b405c1/download/PrecoTaxaTesouroDireto.csv
- Tesouro, histórico de leilões (sisweb): HTTP 500 de novo, substituído pela API do BCB.
- ANBIMA, feriados nacionais: https://www.anbima.com.br/feriados/fer_nacionais/2026.asp · 2027.asp · 2028.asp
- BCB, Focus: https://www.bcb.gov.br/content/focus/focus/R20261002.pdf · R20261009.pdf · R20261023.pdf · R20261113.pdf
- BCB, SGS 1178 e 432: `https://api.bcb.gov.br/dados/serie/bcdata.sgs.{1178,432}/dados?formato=json&dataInicial=13/10/2026&dataFinal=19/11/2026`
- BCB, Resenha de 5 a 9/10/2026 (Tabela 2, operações especiais): https://www.bcb.gov.br/content/publicacoes/resenhamercadoaberto/W20261005-20261009.pdf
- Tesouro, RMD de set/2026, anexos 2.7 e 2.8: https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/56137_1773677/anexos/29569_940811/Anexo%20RMD_Setembro_26.zip
- Tesouro, Metodologia de Cálculo (Tabela 3; du inclusive/exclusive): https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/26310_1658601/Metodologia%20de%20Calculo%20-%20290424.pdf
- Tesouro, página de *dealers* (modificada em 03/11/2026): https://www.gov.br/tesouronacional/pt-br/divida-publica-federal/mercado-interno/dealers
- Planalto, Decreto 12.814/2026: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D12814.htm
- BCB, Circular 3.749/2015 (LCR, consolidada v8): https://normativos.bcb.gov.br/Lists/Normativos/Attachments/48569/Circ_3749_v8_L.pdf
- Wiley-VCH, Tuckman e Serrat, 4ª ed.: https://www.wiley-vch.de/en/areas-interest/finance-economics-law/fixed-income-securities-978-1-119-83555-4
- Martins Fontes Paulista, Securato: https://www.martinsfontespaulista.com.br/calculo-financeiro-das-tesourarias-768937/p
- Investidor10 (26/10/2026, 18h): https://investidor10.com.br/noticias/tesouro-direto-marca-prejuizo-de-ate-37-em-pico-das-taxas-pos-eleicoes-2026-123523/
- Wikipedia, "Bootstrapping" e "Baron Munchausen"; Standard Ebooks, Raspe: https://standardebooks.org/ebooks/rudolph-erich-raspe/the-surprising-adventures-of-baron-munchausen/text/single-page

---

## Apêndice A: registro do cálculo

Rodado com `python3 -I` a partir de cópias temporárias no *scratchpad* da sessão. Os scripts não
foram gravados no repositório. Os insumos de mercado vêm das fontes acima: CSV do Tesouro Direto,
API de leilões do BCB e feriados ANBIMA.

### A.1 `calc.py` (contas do texto; argumento opcional: caminho do CSV do Tesouro Direto)

```python
# Etapa 7 — recálculo de 2026-11-23-a-peca-mais-simples (python3, só stdlib)
from datetime import date, timedelta
from decimal import Decimal, ROUND_DOWN

# Feriados nacionais ANBIMA 2026–2028 (anbima.com.br/feriados/fer_nacionais/AAAA.asp, acesso 23/11/2026)
FER = {date(2026,1,1),date(2026,2,16),date(2026,2,17),date(2026,4,3),date(2026,4,21),date(2026,5,1),
       date(2026,6,4),date(2026,9,7),date(2026,10,12),date(2026,11,2),date(2026,11,15),date(2026,11,20),date(2026,12,25),
       date(2027,1,1),date(2027,2,8),date(2027,2,9),date(2027,3,26),date(2027,4,21),date(2027,5,1),
       date(2027,5,27),date(2027,9,7),date(2027,10,12),date(2027,11,2),date(2027,11,15),date(2027,11,20),date(2027,12,25),
       date(2028,1,1),date(2028,2,28),date(2028,2,29),date(2028,4,14),date(2028,4,21),date(2028,5,1),
       date(2028,6,15),date(2028,9,7),date(2028,10,12),date(2028,11,2),date(2028,11,15),date(2028,11,20),date(2028,12,25),
       date(2029,1,1)}
def util(d): return d.weekday()<5 and d not in FER
def du(a,b):  # a inclusive, b exclusive
    n=0; d=a
    while d<b:
        n+=util(d); d+=timedelta(1)
    return n
def dias_uteis(a,b):
    d=a
    while d<b:
        if util(d): yield d
        d+=timedelta(1)
def trunc(x,n): return float(Decimal(repr(x)).quantize(Decimal(1).scaleb(-n),rounding=ROUND_DOWN))
def pu_ltn(i,n): return trunc(1000/(1+i)**trunc(n/252,14),6)

V=date(2029,1,1)
print("== 1. du e PU")
d17=du(date(2026,11,18),V); d13=du(date(2026,10,14),V)
print("du 18/11/26->01/01/29 =",d17,"| du 14/10/26->01/01/29 =",d13,"| diferença =",d13-d17,
      "| du 14/10->18/11 =",du(date(2026,10,14),date(2026,11,18)))
e=trunc(529/252,14); print("expoente trunc14 =",f"{e:.14f}","| 1,1498^exp =",f"{1.1498**e:.8f}")
p17=pu_ltn(0.1498,529); p13=pu_ltn(0.1240,553)
print("PU 14,98% 529du =",f"{p17:.6f}","| PU 12,40% 553du =",f"{p13:.6f}")
print("taxa de 773,741961 em 553du =",f"{(1000/773.741961)**(252/553)-1:.6%}")
print("taxa de 746,004202 em 529du =",f"{(1000/746.004202)**(252/529)-1:.6%}")
# planilha DIATRABALHOTOTAL(liq; venc-1): conta liq..venc-1 inclusive = du(liq, venc)
print("NETWORKDAYS(18/11/26; 31/12/28) =",du(date(2026,11,18),date(2028,12,31)+timedelta(1)))

print("== 2. duration, DV01, ±1 p.p.")
i=0.1498; n=529; D=n/252; MD=D/(1+i)
print("D =",f"{D:.4f}","| MD =",f"{MD:.4f}")
p=lambda r: 1000/(1+r)**(n/252)
print("DV01/título analítico =",f"{p17*MD*1e-4:.4f}","| diferença finita (14,97-14,99)/2 =",f"{(p(i-1e-4)-p(i+1e-4))/2:.4f}")
print("DV01 por R$ 1 mi =",f"{1e6*MD*1e-4:.2f}","| finita =",f"{1e6*(p(i-1e-4)-p(i+1e-4))/2/p(i):.2f}")
up=p(i+0.01)/p(i)-1; dn=p(i-0.01)/p(i)-1
print("+1 p.p. ->",f"{up:.4%}","| -1 p.p. ->",f"{dn:.4%}","| 1ª ordem (MD x 1 p.p.) =",f"{MD/100:.4%}")
print("R$ 100 mil: +1pp",f"{1e5*up:.0f}","| -1pp",f"{1e5*dn:.0f}","| MD x 1pp",f"{1e5*MD/100:.0f}")

print("== 3. decomposição 13/10 -> 17/11")
carry_pu=pu_ltn(0.1240,529)
carry=carry_pu/p13-1; choque=p17/carry_pu-1; tot=p17/p13-1
print("PU a 12,40% com 529du =",f"{carry_pu:.6f}","| carregamento =",f"{carry:.4%}","| sem truncar (1,124^(24/252)-1) =",f"{1.124**(24/252)-1:.4%}")
print("choque (12,40->14,98) =",f"{choque:.4%}","| total =",f"{tot:.4%}","| 1,0112*0,9535-1 =",f"{1.0112*0.9535-1:.4%}")
print("tela (preços de compra 746,00/773,74) =",f"{746.00/773.74-1:.4%}","| PU base 17/11 (743,95)/773,74 =",f"{743.95/773.74-1:.4%}")
print("Tesouro Selic, over 13,65%, 24du =",f"{1.1365**(24/252)-1:.4%}",
      "| du 13/10->17/11 =",du(date(2026,10,13),date(2026,11,17)))
print("CSV: Tesouro Selic 2029 PU base 13/10 20041,75 -> 17/11 20285,04:",f"{20285.04/20041.75-1:.4%}",
      "| PU compra 20056,78 -> PU base 17/11:",f"{20285.04/20056.78-1:.4%}")

print("== 4. empate e cenários (R$ 10 mil, 18/11/26 -> 01/01/29)")
print("empate over =",f"{0.1498:.4%}","| em meta (over+0,10) = 15,08% | com LFT a Selic+0,05%:",f"{1.1498/1.0005-1:.4%}")
def fator_focus(start, path, spread=0.10, base="corridos"):
    # path: lista (data, meta) de nós; interpolação linear da meta entre nós; over = meta - spread
    days=list(dias_uteis(start,V)); f=1.0
    for d in days:
        for (d0,m0),(d1,m1) in zip(path,path[1:]):
            if d0<=d<=d1:
                if base=="corridos": w=(d-d0).days/(d1-d0).days
                else: w=du(d0,d)/max(du(d0,d1),1)
                m=m0+(m1-m0)*w; break
        else: m=path[-1][1]
        over=(m-spread)/100; f*=(1+over)**(1/252)
    return f, len(days), f**(252/len(days))-1
nov=[(date(2026,11,18),13.75),(date(2026,12,31),13.75),(date(2027,12,31),12.75),(date(2028,12,31),11.00)]
for base in ("corridos","uteis"):
    f,n_,avg=fator_focus(date(2026,11,18),nov,base=base)
    print(f"Focus 13/11 ({base}): fator {f:.6f} -> R$ {1e4*f:,.2f} | over média {avg:.4%} | meta média {avg+0.001:.4%} | n={n_}")
f,_,_=fator_focus(date(2026,11,18),nov,spread=0.0)
print(f"Focus 13/11 sem o -0,10: R$ {1e4*f:,.2f}")
for lab,o in (("parada 13,75 (over 13,65)",0.1365),("parada 13,75 sem -0,10",0.1375),("meta 16 (over 15,90)",0.1590),("over 16",0.16)):
    print(f"{lab}: R$ {1e4*(1+o)**(529/252):,.2f}")
print(f"Prefixado 2029: R$ {1e4*1000/p17:,.2f} | R$ {1e4*1.1498**(529/252):,.2f} (sem truncar)")
f,_,avg=fator_focus(date(2026,11,18),nov)
print("spread LTN - Selic média esperada (over) =",f"{(0.1498-avg)*100:.2f} p.p.","| razão",f"{(1.1498/(1+avg)-1)*100:.2f} p.p.")
print("vs meta média:",f"{(0.1498-avg-0.001)*100:.2f} p.p.")

print("== 5. expectativa x prêmio, 13/10 -> 17/11")
out=[(date(2026,10,14),13.75),(date(2026,12,31),13.25),(date(2027,12,31),12.00),(date(2028,12,31),10.50)]
for base in ("corridos","uteis"):
    f13,n13,a13=fator_focus(date(2026,10,14),out,base=base)
    f17,n17,a17=fator_focus(date(2026,11,18),nov,base=base)
    dexp=(a17-a13)*100; dtot=14.98-12.40
    print(f"({base}) Selic média esperada 14/10 (Focus 9/10): {a13:.4%} [n={n13}] | 18/11 (Focus 13/11): {a17:.4%} [n={n17}]")
    print(f"   expectativa {dexp:.2f} p.p. | prêmio (resíduo) {dtot-dexp:.2f} p.p. | prêmio 13/10 {12.40-a13*100:.2f} | 17/11 {14.98-a17*100:.2f}")
out2=[(date(2026,10,14),13.75),(date(2026,12,31),13.50),(date(2027,12,31),12.00),(date(2028,12,31),10.50)]
f,n_,a=fator_focus(date(2026,10,14),out2); print(f"variante Focus 2/10 em 14/10: {a:.4%} -> expectativa {(a17-a)*100:.2f}, prêmio {2.58-(a17-a)*100:.2f}")
print("Focus: 2027 12,00->12,75 =",12.75-12.00,"| 2028 10,50->11,00 =",11.00-10.50,"| desde 23/10 (11,75/10,00):",12.75-11.75,11.00-10.00)

print("== 6. 8/10: 'menos de um ponto acima do Focus da época' (Focus 2/10: 13,50/12,00/10,50/10,00)")
f02=[(date(2026,10,9),13.75),(date(2026,12,31),13.50),(date(2027,12,31),12.00),(date(2028,12,31),10.50),(date(2029,12,31),10.00)]
def media(start,venc,path,spread=0.10):
    days=list(dias_uteis(start,venc)); f=1.0
    for d in days:
        for (d0,m0),(d1,m1) in zip(path,path[1:]):
            if d0<=d<=d1: m=m0+(m1-m0)*(d-d0).days/(d1-d0).days; break
        f*=(1+(m-spread)/100)**(1/252)
    return f**(252/len(days))-1, len(days)
for lab,venc,tx in (("LTN 01/01/2028 leilão",date(2028,1,1),12.55),("LTN 01/07/2029 leilão",date(2029,7,1),12.51),
                    ("Prefixado 01/01/2029 TD 8/10",date(2029,1,1),12.53),("LTN 01/01/2032 leilão",date(2032,1,1),12.70)):
    a,n_=media(date(2026,10,9),venc,f02); print(f"{lab}: taxa {tx:.2f} | Selic média (over) {a:.4%} | diferença {tx-a*100:+.2f} p.p. | du {n_}")
# (para 2029–2032 a função só conhece feriados até 01/01/2029: a LTN 2032 é indicativa, não entra em correção)

print("== 7. carteira")
print("100 títulos:",f"{100*p17:,.4f}")
g=1000-p17; ir=0.15*g; liq=1000-ir
print("ganho",f"{g:.6f}","IR",f"{ir:.6f}","líquido",f"{liq:.6f}","taxa líquida",f"{(liq/p17)**(252/529)-1:.4%}")
print("dias corridos 18/11/26 -> 01/01/29 =",(V-date(2026,11,18)).days)
print("CDB 16% (529 du, D+1) =",f"{1000/1.16**(529/252):.2f}","| (530 du, D0) =",f"{1000/1.16**(du(date(2026,11,17),V)/252):.2f}",
      "| du 17/11 =",du(date(2026,11,17),V))
print("dias corridos 8/10 -> 26/10 =",(date(2026,10,26)-date(2026,10,8)).days)
print("erro de quem divide 14,98% por 252:",f"{1000/(1+0.1498/252)**529:.2f}","contra",f"{p17:.2f}")

print("== 8. origem provável dos R$ 12.818")
nov17=[(date(2026,11,17),13.75),(date(2026,12,31),13.75),(date(2027,12,31),12.75),(date(2028,12,31),11.00)]
f,n_,a=fator_focus(date(2026,11,17),nov17); print(f"Focus contado de 17/11 (D0): {n_} du, R$ {1e4*f:,.2f}, média {a:.4%}")
print(f"12,53% em 529 du: R$ {1e4*1.1253**(529/252):,.2f} | em 530 du: R$ {1e4*1.1253**(530/252):,.2f}")

print("== 9. NTN-F 2031: caro x barato (PU teórico, cupom 48,80885)")
# feriados 2029–2030 derivados da Páscoa (só para esta conferência)
FER2=set(FER)|{date(2029,2,12),date(2029,2,13),date(2029,3,30),date(2029,4,21),date(2029,5,1),date(2029,5,31),date(2029,9,7),
 date(2029,10,12),date(2029,11,2),date(2029,11,15),date(2029,11,20),date(2029,12,25),date(2030,1,1),date(2030,3,4),date(2030,3,5),
 date(2030,4,19),date(2030,4,21),date(2030,5,1),date(2030,6,20),date(2030,9,7),date(2030,10,12),date(2030,11,2),date(2030,11,15),
 date(2030,11,20),date(2030,12,25),date(2031,1,1)}
def du2(a,b):
    n=0; d=a
    while d<b:
        n+=(d.weekday()<5 and d not in FER2); d+=timedelta(1)
    return n
def pu_ntnf(i,liq,venc=date(2031,1,1)):
    c=trunc((1.10**0.5-1)*1000,5)
    datas=[date(yy,mm,1) for yy in range(liq.year,venc.year+1) for mm in (1,7) if liq<date(yy,mm,1)<=venc]
    return sum(((c+(1000 if d==venc else 0))/(1+i)**trunc(du2(liq,d)/252,14)) for d in datas)
print(f"PU a 12,61% (liq. 09/10/26): {pu_ntnf(0.1261,date(2026,10,9)):.2f} | a 15,79% (liq. 27/10/26): {pu_ntnf(0.1579,date(2026,10,27)):.2f}")
print(f"PU médio implícito nas Resenhas: venda {3969.7e6/4178100:.2f} | recompra {4351.2e6/5e6:.2f}")

print("== 10. prazo médio das LTN vendidas em 8/10 (1ª rodada, R$ mi)")
vol={date(2028,1,1):17317.9,date(2029,7,1):9463.1,date(2032,1,1):1075.1}
print("anos (corridos/365), ponderado:",f"{sum(v*(d-date(2026,10,9)).days/365 for d,v in vol.items())/sum(vol.values()):.2f}","| total",f"{sum(vol.values()):,.1f}")
print("LTN+NTN-F 1ª rodada:",f"{27856.1+5427.8:,.1f}")

print("== 11. a fórmula reproduz a tela do Tesouro Direto? (Prefixado 2029, CSV oficial, liquidação D+1)")
import csv, sys
if len(sys.argv)>1:
    ok=0; tot=0; bad=[]
    for r in csv.reader(open(sys.argv[1],encoding='latin1'),delimiter=';'):
        if r[0]=='Tesouro Prefixado' and r[1]=='01/01/2029':
            dd,mm,yy=map(int,r[2].split('/')); d=date(yy,mm,dd)
            if d<date(2026,10,1): continue
            liq=d+timedelta(1)
            while not util(liq): liq+=timedelta(1)
            n=du(liq,V); tx=float(r[3].replace(',','.'))/100; pu=pu_ltn(tx,n); tela=float(r[5].replace(',','.'))
            tot+=1; ok+= (trunc(pu,2)==tela or round(pu,2)==tela)
            if not (trunc(pu,2)==tela or round(pu,2)==tela): bad.append((r[2],n,pu,tela))
    print(f"{ok} de {tot} datas-base (01/10 a 19/11) batem ao centavo; divergentes: {bad}")
vol={12.5462:17317.9,12.5078:9463.1,12.7028:1075.1}
print("taxa média ponderada das LTN de 8/10 (1ª rodada):",f"{sum(k*v for k,v in vol.items())/sum(vol.values()):.2f}%")
```

Saída:

```
== 1. du e PU
du 18/11/26->01/01/29 = 529 | du 14/10/26->01/01/29 = 553 | diferença = 24 | du 14/10->18/11 = 24
expoente trunc14 = 2.09920634920634 | 1,1498^exp = 1.34047502
PU 14,98% 529du = 746.004202 | PU 12,40% 553du = 773.741961
taxa de 773,741961 em 553du = 12.400000%
taxa de 746,004202 em 529du = 14.980000%
NETWORKDAYS(18/11/26; 31/12/28) = 529
== 2. duration, DV01, ±1 p.p.
D = 2.0992 | MD = 1.8257
DV01/título analítico = 0.1362 | diferença finita (14,97-14,99)/2 = 0.1362
DV01 por R$ 1 mi = 182.57 | finita = 182.57
+1 p.p. -> -1.8014% | -1 p.p. -> 1.8506% | 1ª ordem (MD x 1 p.p.) = 1.8257%
R$ 100 mil: +1pp -1801 | -1pp 1851 | MD x 1pp 1826
== 3. decomposição 13/10 -> 17/11
PU a 12,40% com 529du = 782.403955 | carregamento = 1.1195% | sem truncar (1,124^(24/252)-1) = 1.1195%
choque (12,40->14,98) = -4.6523% | total = -3.5849% | 1,0112*0,9535-1 = -3.5821%
tela (preços de compra 746,00/773,74) = -3.5852% | PU base 17/11 (743,95)/773,74 = -3.8501%
Tesouro Selic, over 13,65%, 24du = 1.2261% | du 13/10->17/11 = 24
CSV: Tesouro Selic 2029 PU base 13/10 20041,75 -> 17/11 20285,04: 1.2139% | PU compra 20056,78 -> PU base 17/11: 1.1381%
== 4. empate e cenários (R$ 10 mil, 18/11/26 -> 01/01/29)
empate over = 14.9800% | em meta (over+0,10) = 15,08% | com LFT a Selic+0,05%: 14.9225%
Focus 13/11 (corridos): fator 1.281195 -> R$ 12,811.95 | over média 12.5291% | meta média 12.6291% | n=529
Focus 13/11 (uteis): fator 1.281212 -> R$ 12,812.12 | over média 12.5298% | meta média 12.6298% | n=529
Focus 13/11 sem o -0,10: R$ 12,835.87
parada 13,75 (over 13,65): R$ 13,081.32
parada 13,75 sem -0,10: R$ 13,105.50
meta 16 (over 15,90): R$ 13,630.89
over 16: R$ 13,655.59
Prefixado 2029: R$ 13,404.75 | R$ 13,404.75 (sem truncar)
spread LTN - Selic média esperada (over) = 2.45 p.p. | razão 2.18 p.p.
vs meta média: 2.35 p.p.
== 5. expectativa x prêmio, 13/10 -> 17/11
(corridos) Selic média esperada 14/10 (Focus 9/10): 11.9878% [n=553] | 18/11 (Focus 13/11): 12.5291% [n=529]
   expectativa 0.54 p.p. | prêmio (resíduo) 2.04 p.p. | prêmio 13/10 0.41 | 17/11 2.45
(uteis) Selic média esperada 14/10 (Focus 9/10): 11.9892% [n=553] | 18/11 (Focus 13/11): 12.5298% [n=529]
   expectativa 0.54 p.p. | prêmio (resíduo) 2.04 p.p. | prêmio 13/10 0.41 | 17/11 2.45
variante Focus 2/10 em 14/10: 12.0555% -> expectativa 0.47, prêmio 2.11
Focus: 2027 12,00->12,75 = 0.75 | 2028 10,50->11,00 = 0.5 | desde 23/10 (11,75/10,00): 1.0 1.0
== 6. 8/10: 'menos de um ponto acima do Focus da época' (Focus 2/10: 13,50/12,00/10,50/10,00)
LTN 01/01/2028 leilão: taxa 12.55 | Selic média (over) 12.8001% | diferença -0.25 p.p. | du 307
LTN 01/07/2029 leilão: taxa 12.51 | Selic média (over) 11.7216% | diferença +0.79 p.p. | du 684
Prefixado 01/01/2029 TD 8/10: taxa 12.53 | Selic média (over) 12.0605% | diferença +0.47 p.p. | du 555
LTN 01/01/2032 leilão: taxa 12.70 | Selic média (over) 10.8406% | diferença +1.86 p.p. | du 1337
== 7. carteira
100 títulos: 74,600.4202
ganho 253.995798 IR 38.099370 líquido 961.900630 taxa líquida 12.8720%
dias corridos 18/11/26 -> 01/01/29 = 775
CDB 16% (529 du, D+1) = 732.30 | (530 du, D0) = 731.87 | du 17/11 = 530
dias corridos 8/10 -> 26/10 = 18
erro de quem divide 14,98% por 252: 730.25 contra 746.00
== 8. origem provável dos R$ 12.818
Focus contado de 17/11 (D0): 530 du, R$ 12,818.46, média 12.5312%
12,53% em 529 du: R$ 12,812.17 | em 530 du: R$ 12,818.18
== 9. NTN-F 2031: caro x barato (PU teórico, cupom 48,80885)
PU a 12,61% (liq. 09/10/26): 950.06 | a 15,79% (liq. 27/10/26): 870.24
PU médio implícito nas Resenhas: venda 950.12 | recompra 870.24
== 10. prazo médio das LTN vendidas em 8/10 (1ª rodada, R$ mi)
anos (corridos/365), ponderado: 1.89 | total 27,856.1
LTN+NTN-F 1ª rodada: 33,283.9
== 11. a fórmula reproduz a tela do Tesouro Direto? (Prefixado 2029, CSV oficial, liquidação D+1)
34 de 34 datas-base (01/10 a 19/11) batem ao centavo; divergentes: []
taxa média ponderada das LTN de 8/10 (1ª rodada): 12.54%
```

Notas:
- Na seção 6, a LTN de 2032 (+1,86) é só indicativa, porque o calendário do script vai até
  01/01/2029. Não entra em correção. As três linhas de 2028 e 2029 usam só feriados lidos da ANBIMA.
- Tesouro Selic 2029, compra contra compra (20.056,78 → 20.300,05): +1,2129%.

### A.2 `leiloes.py` (ranking dos leilões de prefixados; argumento: pasta com `y2020.json` … `y2026.json` da API do BCB)

```python
import json,sys,glob,collections
rows=[]
for f in sorted(glob.glob(sys.argv[1]+'/y*.json')):
    rows+=json.load(open(f))['value']
pre={'100000','950199'}  # códigos Selic: LTN, NTN-F
agg=collections.defaultdict(lambda: [0.0,0.0,0.0,0.0])  # 1ª rodada LTN, NTN-F, -, financeiro (com 2ª rodada)
for r in rows:
    if r['tipoOferta']!='Venda' or r['ofertante']!='Tesouro Nacional' or r['codigoTitulo'] not in pre: continue
    d=r['dataMovimento'][:10]
    v1=float(r['quantidadeAceita'] or 0)*float(r['cotacaoMedia'] or 0)/1e6   # 1ª rodada = quantidade aceita × PU médio
    agg[d][0 if r['codigoTitulo']=='100000' else 1]+=v1
    agg[d][3]+=float(r['financeiro'] or 0)
lst=sorted(((v[0]+v[1],d,v) for d,v in agg.items()),reverse=True)
print("Top 15 leilões de prefixados (LTN+NTN-F), 1ª rodada, R$ mi, 2020–2026:")
for t,d,v in lst[:15]: print(f"  {d}: {t:,.1f} (LTN {v[0]:,.1f}; NTN-F {v[1]:,.1f}) | 'financeiro' c/ 2ª rodada {v[3]:,.1f}")
d0='2026-10-08'; t0=agg[d0][0]+agg[d0][1]
print("8/10/2026:",f"{t0:,.1f}","| leilões maiores desde 2020:",sorted((d,round(v[0]+v[1],1)) for d,v in agg.items() if v[0]+v[1]>t0))
pos=[(v[0],d) for d,v in agg.items() if d>'2020-12-10']
print("LTN só, depois de 10/12/2020, top 3:",[(d,round(x,1)) for x,d in sorted(pos,reverse=True)[:3]])
pos=[(v[0]+v[1],d) for d,v in agg.items() if d>'2020-12-10']
print("LTN+NTN-F 1ª rodada, depois de 10/12/2020, top 3:",[(d,round(x,1)) for x,d in sorted(pos,reverse=True)[:3]])
print("NTN-F 2031 em 8/10:",[(r['quantidadeAceita'],r['cotacaoMedia'],r['taxaMedia']) for r in rows if r['dataMovimento'][:10]=='2026-10-08' and r['codigoTitulo']=='950199' and r['dataVencimento'][:4]=='2031'])
print("Recompras 26/10:",[(r['codigoTitulo'],r['dataVencimento'][:10],r['tipoOferta'],r['quantidadeAceita'],r['taxaMedia'],r['financeiro']) for r in rows if r['dataMovimento'][:10]=='2026-10-26'])
```

Saída (resumida às linhas que sustentam N40 a N43):

```
Top 15 leilões de prefixados (LTN+NTN-F), 1ª rodada, R$ mi, 2020–2026:
  2020-12-10: 44,282.9 (LTN 41,275.2; NTN-F 3,007.7) | 'financeiro' c/ 2ª rodada 53,141.0
  2020-09-10: 38,337.7 (LTN 36,545.0; NTN-F 1,792.8) | 'financeiro' c/ 2ª rodada 41,472.3
  2020-08-13: 37,438.4 (LTN 37,077.7; NTN-F 360.7) | 'financeiro' c/ 2ª rodada 37,438.4
  2020-09-24: 34,351.2 (LTN 33,003.7; NTN-F 1,347.5) | 'financeiro' c/ 2ª rodada 41,256.2
  2026-10-08: 33,283.9 (LTN 27,856.2; NTN-F 5,427.8) | 'financeiro' c/ 2ª rodada 40,987.2
  2020-11-26: 32,459.1 (LTN 30,366.6; NTN-F 2,092.5) | 'financeiro' c/ 2ª rodada 38,951.8
  …
  2026-04-16: 27,170.9 (LTN 21,039.2; NTN-F 6,131.7) | 'financeiro' c/ 2ª rodada 33,967.1
  2026-09-03: 26,579.2 (LTN 14,390.5; NTN-F 12,188.7) | 'financeiro' c/ 2ª rodada 31,311.1
8/10/2026: 33,283.9 | leilões maiores desde 2020: [('2020-08-13', 37438.4), ('2020-09-10', 38337.7), ('2020-09-24', 34351.2), ('2020-12-10', 44282.9)]
LTN só, depois de 10/12/2020, top 3: [('2026-10-08', 27856.2), ('2021-01-14', 23441.9), ('2026-04-16', 21039.2)]
LTN+NTN-F 1ª rodada, depois de 10/12/2020, top 3: [('2026-10-08', 33283.9), ('2026-04-16', 27170.9), ('2026-09-03', 26579.2)]
NTN-F 2031 em 8/10: [(4178100, 950.119225, 12.6079)]
Recompras 26/10: [('950199', '2031-01-01', 'Compra', 5000000, 15.79, 4351.2), ('760199', '2030-08-15', 'Compra', 271000, 7.75, 1239.6), ('760199', '2050-08-15', 'Compra', 486850, 7.25, 2040.2), ('760199', '2035-05-15', 'Compra', 1000000, 7.72, 4419.5), ('950199', '2037-01-01', 'Compra', 1000000, 15.3725, 773.4), ('950199', '2033-01-01', 'Compra', 2400000, 15.6113, 1983.2)]
```

Na API do BCB, a segunda rodada vem no mesmo registro do leilão (`quantidadeAceitaSegundaRodada`). O
"financeiro" soma as duas rodadas. A primeira rodada é quantidade aceita × PU médio, e bate com a
Tabela 2 da Resenha (R$ 17.317,9 + 9.463,1 + 1.075,1 mi de LTN).
