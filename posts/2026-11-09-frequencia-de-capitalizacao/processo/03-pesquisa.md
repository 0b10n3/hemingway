# Etapa 3 — Pesquisa

Slug: `2026-11-09-frequencia-de-capitalizacao` · linha Notas de um Professor (matemática financeira) · acesso a todas as fontes em **2026-11-09**. Executor: subagente `pesquisador-editorial`.

Escopo: conferir e completar a pesquisa do montador (`processo/00-leitura.md`, "Fontes consultadas"), seguindo as seções de `02-estrutura.md`. O laudo traz material de pesquisa, não prosa. Os números de cálculo próprio que aparecem aqui só ilustram contrapontos e vão marcados **[recalcular na etapa 7]**.

---

## Quadro-resumo: vereditos dos 10 itens pedidos

| # | Item | Veredito |
|---|---|---|
| 1a | Bernoulli 1683, limite entre 2 e 3, binômio | **Confirmado** (MacTutor original). Nuance: a publicação impressa é de 1690, nas *Acta Eruditorum* |
| 1b | Data em que Euler usa a letra *e*; "quase cinquenta anos depois" | **Divergente.** Os 48 anos só se sustentam com a carta de 1731. Há uso anterior (1727/28, manuscrito) e o primeiro impresso é de 1736 |
| 2 | Manual de Opções da B3: versão, eq. (1.5), T = DU/252, "taxa de juro exponencial, em regime contínuo", volatilidade por retorno log | **Confirmado com correções.** A versão vigente é a **v27 (16/09/2026)**, não a v26. A eq. (1.5) está confirmada. A frase completa é "…em regime contínuo **e base anual**". A volatilidade por retornos log vale **só no modelo de ativos ilíquidos** |
| 3 | DI1 em taxa efetiva anual base 252; "conversão exponencial 252"; capitalização só em dias úteis | **Confirmado** |
| 4 | Tesouro, LTN: expoente truncado na 14ª casa, PU na 6ª | **Confirmado.** O termo "Exponencial de Dias" existe e está no documento do Tesouro |
| 5 | Hull 11ª ed.: capítulo/seção; frase sobre uso extensivo | **Cap. 4, seção 4.4 "Measuring interest rates"** (não 4.2). **A frase "extensively" não foi encontrada** em fonte verificável |
| 6 | Lei 12.703/2012 | **Confirmado.** A TR está no inciso I do art. 12 da Lei 8.177/1991, não na redação da 12.703 |
| 7 | Maor, edição Record | **Apêndice 2 confirmado**. **Ano não confirmado**: as fontes divergem (2006 × 2019) |
| 8 | Excel pt-BR: EFETIVA, NOMINAL, TRUNCAR, LN, EXP com `;` | **Confirmado** (EFETIVA/NOMINAL truncam `npera` para inteiro) |
| 9 | Contrapontos e onde a frequência importa no Brasil | **Material encontrado** (cartão, CET, SFH, Súmulas 539/541, Meucci). **Nenhum caso real documentado** de "DI usado direto como r" |
| 10 | O que ninguém está dizendo | Cinco ângulos, abaixo |

---

## Abertura: Bernoulli, 1683

- O'Connor & Robertson, "The number e", MacTutor, Univ. St Andrews: https://mathshistory.st-andrews.ac.uk/HistTopics/e/ (acesso 2026-11-09). Trechos literais:
  - "In 1683 Jacob Bernoulli looked at the problem of compound interest"
  - "he tried to find the limit of (1+1/n)^n as n tends to infinity."
  - "He used the binomial theorem to show that the limit had to lie between 2 and 3"
  - "Also if we accept this as a definition of e, it is the first time that a number was defined by a limiting process."
- **Correção às notas do montador:** a frase "primeira vez que um número foi definido por um processo de limite" **está** na página original, mas com a condicional "if we accept this as a definition of e". Se for recuperada, a ressalva vai junto.
- **Data da publicação:** "Quæstiones nonnullæ de usuris…", *Acta Eruditorum*, maio de 1690, pp. 219–223 (cálculo na p. 222). Fontes: referências da Wikipedia "e (mathematical constant)" → https://books.google.com/books?id=s4pw4GyHTRcC&pg=PA222; Univ. Münster, https://uni-muenster.de/FB10/HotNews/zeige_anlage.php?id=2089. 1683 é a data que MacTutor e Wikipedia dão para quando Bernoulli estudou o problema. **Não há fonte primária que explique o 1683.** Uma saída para blindar a data: "estudou em 1683 e publicou em 1690".
- Contexto: o primeiro símbolo da constante foi **b**, de Leibniz, em cartas a Huygens (1690–91).

## Dois motores rivais (Mito)

- **Consenso de livro-texto:** na matemática atuarial, a força de juros δ é o limite da nominal i^(m) quando m → ∞, com δ = ln(1 + i). A cadeia 1 + i = (1 + i^(m)/m)^m = e^δ é material padrão do exame FM da SOA. Fontes (notas de curso): Newcastle Univ., https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/finance/force-of-interest.html; formulário SOA FM, https://freefellow.org/free/exam-fm/formula-sheet/soa-fm-formula-sheet.pdf; https://sanghuynh0929.github.io/notes/interest_theory/Interest/section-4-constant-force-of-interest.html. Kellison, *The Theory of Interest*, não foi consultado.
- A "escada de etiquetas" do post é o i^(m) atuarial. Nada contradiz a tese.

## Nominal, frequência, efetiva / A escada de Bernoulli

- Binômio: o terceiro termo é (1/2!)(1 − 1/n) ≤ 1/2, e para k ≥ 2 vale 1/k! ≤ 1/2^(k−1). A soma do terceiro termo em diante fica ≤ 1, e o total < 3. **A indexação do rascunho está correta.**
- Do diário para o horário: ≈ 0,0036, coerente com "menos de quatro milésimos" **[recalcular na etapa 7]**.
- **"Quase cinquenta anos depois":**

| Evento | Data | Desde 1683 | Fonte |
|---|---|---|---|
| *Meditatio…* (E853), manuscrito | 1727/28; publicado em 1862 | 44–45 anos | https://scholarlycommons.pacific.edu/euler-works/853/ |
| Carta de Euler a Goldbach | **25/11/1731** | **48 anos** | MacTutor; Fuss (1843), *Correspondance…*, vol. 1, Lettre XV, p. 58: https://books.google.com/books?id=gf1OEXIQQgsC&pg=PA58 |
| *Mechanica*, primeiro uso impresso | 1736 | 53 anos | https://books.google.com/books?id=qalsP7uMiV4C&pg=PA68 |
| *Introductio in Analysin Infinitorum* | 1748 | 65 anos | MacTutor |

  Veredito: "quase cinquenta" só se sustenta ancorado na carta de 1731. A decisão fica com o pipeline principal: ancorar na carta, ou trocar o intervalo por algo que não dependa do documento.
- O MacTutor rejeita que o *e* venha do nome de Euler. O rascunho não afirma isso.

## De onde vem o e / Mesma curva, outra etiqueta

- A identidade (1 + i)^t = e^{t·ln(1+i)} é algébrica. Hull, cap. 4, seção 4.4, traz R_c = m·ln(1 + R_m/m) e R_m = m(e^{R_c/m} − 1). A seção foi conferida pelo sumário, sem o texto.

## Um aviso de vocabulário ("exponencial")

- **B3, Programa de Treinamento DI, "02 – Taxas de Juros"**: https://www.b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/programa-de-treinamento-di/02-taxas-de-juros.htm. Trechos literais: "a chamada conversão exponencial 252"; "taxas de juros são baseadas em um ano de 252 dias úteis"; "A capitalização ocorre apenas em dias úteis no período entre a data do investimento e a data da liquidação."; "Este formato se aplica à taxa Selic e a taxa DI." **Confirmado.** A expressão "taxa efetiva anual" vem da especificação do DI1, não desta página.
- **Manual de Apreçamento – Opções v27, p. 11–12:** "r_n = taxa de juro exponencial, em regime contínuo e base anual, correspondente ao vencimento n e calculada pela equação (1.5)". O rascunho corta as aspas em "regime contínuo". A frase completa inclui "e base anual".
- **Reforço:** na mesma eq. (1.5), o manual diz que TPre vem da "**interpolação exponencial** dos preços de ajuste do contrato futuro de taxa média de DI de um dia (DI1)" (p. 12). Na mesma página, "exponencial" quer dizer composto 252 e "taxa de juro exponencial" quer dizer contínuo.
- O Tesouro chama (1 + taxa)^(du/252) de "**Exponencial de Dias**" (Tabela 3).

## Rende todo dia não é render mais

- **B3, Futuro de DI1**: https://b3.com.br/pt_br/produtos-e-servicos/negociacao/juros/futuro-de-taxa-media-de-depositos-interfinanceiros-de-um-dia.htm. Cotação: "Taxa de juro efetiva anual, base 252 dias úteis, com até três casas decimais." **Confirmado.**
- **Taxa DI ao ano base 252:** metodologia do Índice DI da B3 (https://b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/di/metodologia-de-calculo-do-indice-di/): a DI over é "expressa ao ano de 252 dias úteis". O fator diário sai com 8 casas, arredondado. O documento atual de apuração da Taxa DI (pós-01/10/2018) não foi encontrado.
- Apoio de contrato real a (1 + DI)^(1/252) − 1: caderno de fórmulas de LIG do Santander (https://cms.santander.com.br/sites/WPS/documentos/arq-investimentos-lig-detalhes-listadownload-4/21-05-26_132702_cadernodeformula.pdf), fonte secundária.
- **Contraponto:** a distância até o teto é ≈ e^j·j²/(2m) e cresce com j². A 14% a frequência quase não pesa. No cartão, pesa muito.

## Por que a mesa de opções fala contínuo

**Manual de Apreçamento – Contratos de Opções, v27 (16/09/2026):** https://b3.com.br/data/files/0E/32/10/AB/5FBA0A105BF9020AAC094EA8/Manual%20de%20Aprecamento%20-%20Opcoes%20v27.pdf. A v27 só corrigiu o Capítulo 5. A seção 1 não mudou desde a v24 (12/12/2025), então a eq. (1.5) tem o mesmo número.

- Seção 1.1, "Contratos de opções sobre ações, ETFs e índices" (p. 11–12): (1.1) PRCALL = S·e^(−qT)·N(d1) − K·e^(−rT)·N(d2); **(1.5) r_n = ln(1 + TPre^n_DI1)**; T_n = DU_n/252, em que "DU_n [é] o número de dias de saque". (1.6) q_n = ln(1 + TCY_n) aplica a mesma tradução ao custo de carregamento.
- A seção 1.1 não nomeia o modelo. Mais adiante o manual fala em "equação de Black & Scholes". "Black-Scholes-Merton" é rótulo nosso, descritivamente correto.
- **"Define o prêmio de referência":** o manual apresenta "as metodologias para os cálculos dos prêmios de referência das opções" (p. 4). A marcação é primeiro por preço de mercado (p. 5–9), e o preço teórico só entra quando faltam negócios ou ofertas válidos (p. 10).
- **Volatilidade e retornos log, divergente em parte.** Nos ilíquidos (1.2.1), o manual usa "retornos logarítmicos", r(j) = ln(S_j/S_{j−1}), com GARCH(1,1) (p. 14–17). Nos líquidos (1.2.2), a volatilidade é implícita, tirada de superfícies (SABR, Corrado & Su, VLFit, VLGARCH) e da "inversão da equação de Black & Scholes" (p. 18–20). O argumento conceitual se mantém (no BSM a volatilidade é o desvio-padrão do retorno log), mas a atribuição ao manual precisa de ressalva.

**Hull:** sumário da 11ª ed. (https://toc.uni.li/FLMF056124.pdf): cap. 4 "Interest rates", **4.4 Measuring interest rates (p. 101)**. Cap. 6, 6.1 "Day count and quotation conventions", bate com o "capítulo 6" do du252. A editora data a edição de 2021, e a British Library registra "[2022]". **A frase "used extensively in the analysis of derivatives" não foi verificada.** O link O'Reilly dá 403, e as variantes que circulam são secundárias ("Rates used in option pricing are nearly always expressed with continuous compounding", curso que cita a 9ª ed.: https://tomasplihal.github.io/financial_derivatives/interest_rates.html). Para atribuir a frase, é preciso conferir no livro. "É conveniência, não precisão" é conclusão do autor, não do Hull.

**As três conveniências:** (1) a soma vale no tempo, não entre ativos (Meucci); (2) o cálculo e o e^(−rT) são o padrão do modelo; (3) a volatilidade leva a ressalva acima.

## Onde mora o erro

- **Caso real documentado de "DI usado direto como r": não encontrado.** A conversão ser norma na B3 (eq. 1.5) não prova que o erro aconteça. O exemplo numérico em cálculo próprio se sustenta como ilustração, mas não há fonte para dizer que o erro é comum.

## Uma pergunta antes das outras três (Prateleira)

- **EFETIVA(taxa_nominal; npera)**, com `npera` truncado para inteiro: https://support.microsoft.com/pt-br/office/efetiva-fun%C3%A7%C3%A3o-efetiva-910d4e4c-79e2-4009-95e6-507e04f11bc4
- **NOMINAL(taxa_efet; npera)**, com o mesmo truncamento: https://support.microsoft.com/pt-br/office/nominal-fun%C3%A7%C3%A3o-nominal-7f1ae29b-6b92-435e-b950-ad8b190ddd2b
- **TRUNCAR(número;[núm_dígitos])**: https://support.microsoft.com/pt-br/office/truncar-fun%C3%A7%C3%A3o-truncar-8b86a64c-3127-43db-ba14-aa5ceb292721
- LN e EXP têm o mesmo nome em pt-BR. EFETIVA/NOMINAL não servem para a contínua, o que justifica as linhas LN/EXP. **O bloco está correto.**
- **Tesouro, LTN:** https://cdn.tesouro.gov.br/sistemas-internos/apex/producao/sistemas/thot/arquivos/publicacoes/26310_1658601/Metodologia%20de%20Calculo%20-%20290424.pdf. Preço = 1.000/(1 + taxa)^(du/252). Tabela 3: taxa T6, **PU T6**, **"Exponencial de Dias" T14**. du conta "da data de liquidação (inclusive) [à] data de vencimento (exclusive)". **Caso de teste do próprio documento: 14,3600% a.a., 532 du, PU = 753,315323.** O documento também manda truncar a taxa na 6ª casa.

## Fechamento (teste de transferência, poupança)

- **Lei nº 12.703/2012**: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2012/lei/l12703.htm. Nova redação do art. 12, II, da Lei 8.177/1991: "a) 0,5% (cinco décimos por cento) ao mês, enquanto a meta da taxa Selic ao ano… for superior a 8,5%…; b) 70% … da meta da taxa Selic … mensalizada…". Vale para depósitos a partir de 4/5/2012.
- A TR está no inciso I do art. 12 da Lei 8.177/1991 (https://www.planalto.gov.br/ccivil_03/leis/l8177.htm). O rascunho não atribui a TR à 12.703, então está correto.
- **A poupança capitaliza mensalmente:** Lei 8.177/1991, art. 12, §2º, I ("o mês corrido, a partir da data de aniversário da conta") e §4º, I (crédito "mensalmente, na data de aniversário"). O "6% ao ano" é nominal com m = 12.
- A meta Selic está acima de 8,5% (13,75% em 16/09/2026, fonte secundária; a reunião de 04/11/2026 não foi conferida). A regra do 0,5% a.m. vale hoje.

## Bibliografia

- **Maor**: *e: The Story of a Number*, Princeton, 1994. **Apêndice 2, "The Existence of lim (1+1/n)^n as n→∞"**, confirmado em catálogo (https://www.oeaw.ac.at/resources/Record/9781400832347?lng=de). **Edição Record: ano não confirmado.** O Skoob diz 2006, com ISBN incoerente. O marketplace diz ISBN 978-85-01-05847-8, "2019, 1ª edição". Manter `[VERIFICAR]` até conferir a ficha catalográfica.
- **Hull**: cap. 4, seção 4.4 se quiser precisão.
- **MacTutor**: O'Connor e Robertson, URL `/HistTopics/e/`. A página original abriu e confirma 1683, o binômio, o intervalo entre 2 e 3 e a carta de 1731.

## Contrapontos genuínos

1. **"Contínuo é mais preciso":** nenhuma literatura séria defende isso. O consenso é de equivalência com conveniência analítica. O contraponto real: a etiqueta contínua também tem armadilhas. **Meucci (2010), "Quant Nugget 2: Linear vs. Compounded Returns – Common Pitfalls in Portfolio Management"**, *GARP Risk Professional*, abr. 2010, pp. 49–51, SSRN https://papers.ssrn.com/abstract=1586656: o retorno log de uma carteira não é a média ponderada dos retornos log dos ativos. "O retorno vira soma" vale no tempo, não entre ativos. Só o resumo foi lido.
2. **Onde a frequência pesa de verdade no Brasil:**
   - **Rotativo do cartão:** 451,7% a.a. em set/2026, segundo o BCB via O Povo (https://mais.opovo.com.br/jornal/economia/2026/10/30/juro-medio-do-rotativo-do-cartao-de-credito-sobe-a-4517-ao-ano-em-setembro-diz-bc.html). Cálculo próprio **[recalcular]**: ≈ 15,3% a.m.; nominal ≈ 183%; contínua ≈ 170,8%. A essas taxas, a diferença é de centenas de pontos percentuais. A frase "diária contra contínua cabe no arredondamento" precisa da condição "para taxas da ordem do DI".
   - **CET:** Resolução CMN 4.881/2020, art. 4º, com expoente (d_j − d_0)/365 em dias corridos, taxa anual com duas casas (https://www.bcb.gov.br/content/estabilidadefinanceira/especialnor/Resolu%C3%A7%C3%A3o4881.pdf). É efetiva anual, base 365.
   - **SFH:** Lei 8.692/1993, art. 25: "a taxa efetiva de juros será de, no máximo, doze por cento ao ano" (https://www.planalto.gov.br/ccivil_03/leis/l8692.htm). Nominal mensal máxima ≈ 11,39% **[recalcular]**.
3. **Caso real de erro de etiqueta:** não encontrado.

## O que ninguém está dizendo

1. **A etiqueta é matéria de tribunal.**
   - Decreto 22.626/1933, art. 4º: "É proibido contar juros dos juros" (https://www.planalto.gov.br/ccivil_03/decreto/d22626.htm).
   - MP 2.170-36/2001, art. 5º: capitalização "com periodicidade inferior a um ano" admitida no SFN (https://www.planalto.gov.br/ccivil_03/mpv/2170-36.htm).
   - **Súmula 539/STJ** (DJe 15/06/2015): permitida a capitalização inferior à anual a partir de 31/3/2000, "desde que expressamente pactuada" (https://arquivocidadao.stj.jus.br/index.php/sumula-539-2?sf_culture=en).
   - **Súmula 541/STJ** (DJe 15/06/2015): "A previsão no contrato bancário de taxa de juros anual superior ao duodécuplo da mensal é suficiente para permitir a cobrança da taxa efetiva anual contratada." (https://arquivocidadao.stj.jus.br/index.php/sumula-541?sf_culture=en). O SCON deu 403, e a etapa 7 confere a pontuação.
   - Para o post: o STJ decidiu que a diferença entre 12 × a mensal (a nominal) e a anual (a efetiva) é em si prova de capitalização pactuada. A conta da abertura (1% a.m. → 12% × 12,68%) é o exemplo dos comentários jurídicos da 541. A 539 não se aplica ao SFI.
2. **Cada norma escolhe sua etiqueta:** DI/DI1/Tesouro (efetiva 252 du), CET (efetiva 365 dc), SFH (teto sobre a efetiva), poupança (0,5% ao mês, lido como "6% ao ano" nominal), manual de opções da B3 (contínua).
3. **A tradução para contínua é sistemática na B3:** ln(1 + ·) em (1.5) e (1.6). "Exponencial" tem os dois sentidos na mesma página.
4. **A precisão também é cláusula no DI:** o fator diário é arredondado na 8ª casa. Se isso se compara aos 0,5 pb da frequência, a etapa 7 decide.
5. **O limite tem dono na atuária:** i^(m) → δ, a força de juros. Uso opcional.

## Correções às notas do montador

| Nota do montador | Situação |
|---|---|
| MacTutor original não abriu; "primeira vez definido por limite" não confirmada | Abriu; a frase está lá, condicional |
| Manual de opções v26 | Vigente: **v27 (16/09/2026)**; eq. (1.5) inalterada |
| "Exponencial de Dias" não achado na ANBIMA | Está no **documento do Tesouro** (Tabela 3) |
| Hull, seção 4.2 | 11ª ed.: **seção 4.4** |
| Hull, uso "extensivo" | **Não verificado** |
| Volatilidade por retornos log | Só **ilíquidos**; líquidos usam volatilidade implícita |

## Sem fonte confiável (decisão do pipeline principal)

- Ano da edição Record do Maor.
- Frase do Hull sobre uso "extensivo" de taxas contínuas.
- Origem documental do 1683 (a publicação é de 1690).
- Caso real de "DI direto como r".
- Documento atual da B3 de apuração da Taxa DI.
