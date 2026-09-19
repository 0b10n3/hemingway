# Etapa 3 — Pesquisa editorial

Feita pelo agente `pesquisador-editorial`. Organizado pelos 5 pontos do pedido, não pela
estrutura do post (cada achado indica a que seção/`[VERIFICAR]` do rascunho ele se conecta).
Nada aqui é veredito técnico final — isso é etapa 7.

---

## 1. Tratamento do tema na literatura/mercado — a conta linear é mesmo a regra dominante?

Confirma o "erro-alvo" da Ficha de Saída: a divisão simples `Taxa_LCA / (1 − IR)` (gross-up)
é a fórmula padrão em praticamente todo material de mercado voltado a pessoa física, sem
menção a capitalização composta ou prazo como variável de erro.

- **brapi.dev**, calculadora de equivalência LCI/LCA/CDB — usa `Taxa Bruta = Taxa Líquida /
  (1 − IR%)` como fórmula central. https://brapi.dev/calculadoras/equivalencia-lci-lca-cdb
  (acesso 2026-09-18)
- **Meelion**, "Calculadora de Gross Up" — mesmo formato, sem tratamento de prazo.
  https://www.meelion.com/calculadora-gross-up/ (acesso 2026-09-18)
- **Investidor Top**, "Gross up: CDB a 100% do CDI ou LCI/LCA a 90% do CDI?" — usa a fórmula
  linear explicitamente, com exemplo de 92%/(1−0,225) = 118,7% para 180 dias.
  https://investidortop.com.br/gross-up/ (acesso 2026-09-18)
- **InvestNews**, calculadora comparativa CDB × LCI/LCA — mesmo padrão.
  https://investnews.com.br/investimentos/quando-uma-lci-ou-lca-isenta-de-ir-rende-mais-do-que-um-cdb-veja-a-resposta-nesta-calculadora/
  (acesso 2026-09-18)

**Achado relevante:** nenhuma das fontes de mercado pesquisadas discute o efeito da
capitalização composta sobre o gap entre a regra linear e o break-even real — o ângulo que o
rascunho explora (tabela de 6 meses a 5 anos) não aparece na cobertura padrão. Isso sustenta
diretamente o campo 4 da Ficha de Saída ("erro-alvo") como um ângulo pouco coberto, não
redundante com o que já circula.

**Não encontrado:** nenhuma fonte de mercado ou acadêmica que já faça a comparação por juros
compostos como o rascunho propõe. Se a etapa 7 quiser um paper/livro-texto de apoio à fórmula
de break-even composto, os títulos já citados no rascunho (Fabozzi; Santos & Rangel) são a
referência mais provável — o agente não localizou versão web aberta de nenhum dos dois para
conferir o tratamento específico de gross-up multiperíodo.

---

## 2. Estoque de LCA/LCI em 2026 — o dado da nota do autor

**Confirmado, com números um pouco diferentes do que a nota do autor menciona — a etapa 4
precisa decidir com o número certo, não o aproximado.**

- **InfoMoney**, "Isentos em queda: LCI e LCA remuneram menos e exigem atenção redobrada",
  publicado **11/06/2026**, fonte citada no próprio artigo: **Quantum Finance** (fonte
  exclusiva para taxas médias e volume de emissões; o artigo não cita B3 para esses números
  específicos).
  https://www.infomoney.com.br/onde-investir/lci-lca-remuneracao-menor-2026/ (acesso
  2026-09-18)
  - Taxa média da **LCA de 12 meses**: **90,05% do CDI (2025) → 88,24% do CDI (2026)** —
    **bate exatamente** com o número que a nota do autor cita.
  - Taxa média da **LCI de 12 meses**: 94,41% do CDI (2025) → 88,00% do CDI (2026) — a LCI
    também caiu, não subiu, nesta métrica de taxa.
  - Volume de **emissões** (não estoque), jan-maio: LCA subiu de 6.172 para 7.278 títulos;
    LCI caiu de 197 para 16 títulos.

- **B3** (via borainvestir.b3.com.br, matéria não lida na íntegra, só resumo de busca) —
  **estoque de LCA em R$ 563 bilhões ao fim do 1º semestre de 2026, queda de 4% na
  comparação anual** — dado publicado **27/07/2026**. Fonte a conferir diretamente na
  etapa 7: https://borainvestir.b3.com.br/tipos-de-investimentos/renda-fixa/renda-fixa-estoque-de-produtos-de-captacao-bancaria-na-b3-cresce-13-no-primeiro-semestre/
  (fetch completo não feito — só resumo de busca; **a etapa 7 deve abrir o link e confirmar
  o número e se o "cresce 13%" do título se refere ao estoque agregado de captação bancária,
  não à LCA isolada** — os dois números parecem coexistir em textos diferentes do mesmo
  veículo, o que sugere agregados diferentes: total de captação bancária sobe, LCA
  especificamente cai).

**O que não bate com a nota do autor:** a nota diz "LCI sobe ~20%" — não há fonte encontrada
que sustente alta de estoque de LCI em 2026; ao contrário, a taxa média de LCI caiu mais que
a da LCA (94,41% → 88,00%, queda de 6,4 p.p., maior que os 1,81 p.p. da LCA), e o volume de
novas emissões de LCI despencou (197 → 16 títulos). **Não confirmado** — pode ser um número de
outra métrica (estoque em R$, não taxa nem contagem de emissões) não localizada pelo agente,
ou pode ser lembrança imprecisa do autor.

**Resumo para a decisão da etapa 4:** o dado de taxa (90,05% → 88,24%) está confirmado com
fonte e data. O dado de "estoque caindo ~4%" tem uma fonte plausível (B3, jul/2026) mas não
verificada em detalhe. O dado de "LCI subindo ~20%" não tem sustentação encontrada — o oposto
(queda) é o que as fontes mostram.

---

## 3. Contraponto — a isenção beneficia desproporcionalmente o banco?

**Sim, esse debate existe e tem pelo menos duas camadas — uma sobre quem fica com o benefício
fiscal, outra sobre se o direcionamento realmente garante crédito rural mais barato.**

### 3a. Isenção como benefício repartido — quem fica com a maior fatia

- **Investing.com**, "Fim da isenção de LCI e LCA: quem pagará essa conta?" — argumenta que a
  crítica que "ganhou força nos últimos anos" é que a isenção se descolou do propósito
  original: parte relevante dos recursos captados via LCI/LCA não vai proporcionalmente para
  novos financiamentos, mas complementa o caixa geral do banco. O texto também nota
  explicitamente que "ainda se sabe pouco sobre quanto do benefício fiscal chega ao tomador"
  — ou seja, a crítica não afirma que o banco fica com tudo, afirma que a proporção é opaca.
  https://br.investing.com/analysis/fim-da-isencao-de-lci-e-lca-quem-pagara-essa-conta-200479112
  (acesso 2026-09-18)

**Isso é um contraponto genuíno à tese do rascunho.** O rascunho diz "quem define a divisão
[banco/investidor] é oferta e demanda" — tecnicamente correto como mecanismo, mas a crítica de
mercado vai além: questiona se há transparência suficiente para qualquer parte (regulador,
investidor, produtor) saber que fração do benefício chega a cada um. O rascunho não afirma o
contrário disso, mas também não menciona essa opacidade — é um ângulo que poderia reforçar a
tese sem contradizê-la ("a isenção é repartida, e ninguém mede bem como").

### 3b. Direcionamento de crédito rural — mudança recente e resposta ao `[VERIFICAR]` do item 8

- **Resolução CMN nº 5.216, de 22/05/2025** — confirmado por múltiplas fontes: **elevou de
  50% para 60%** o percentual de recursos captados via LCA que o banco precisa aplicar em
  crédito rural (ou títulos do agro elegíveis), vigência a partir de 01/07/2025.
  - Nota do Ministério da Fazenda/CMN (conteúdo não confirmado por bloqueio de acesso, só
    título e data): https://www.gov.br/fazenda/pt-br/canais_atendimento/imprensa/notas-do-cmn/2025/maio/cmn-altera-percentuais-de-direcionamentos-e-subdirecionamentos-dos-recursos-captados-pelas-instituicoes-financeiras-para-aplicacao-em-credito-rural
  - Editora Roncarati (Diário Oficial), "Resolução CMN nº 5.216, de 22.05.2025".
    https://www.editoraroncarati.com.br/v2/Diario-Oficial/Diario-Oficial/RESOLUCAO-CMN-N%C2%BA-5-216-DE-22-05-2025.html
  - Agência Brasil, "CMN simplifica uso de recursos da LCA por cooperativas de crédito"
    (maio/2025), mesmo pacote normativo.
    https://agenciabrasil.ebc.com.br/economia/noticia/2025-05/cmn-simplifica-uso-de-recursos-da-lca-por-cooperativas-de-credito

  **Corrobora o número de 60% que o rascunho usa.** Etapa 7 deve abrir o texto oficial
  diretamente (bloqueado para o agente de pesquisa) e checar o MCR do BCB.

- **Res. CMN 5.315/2026** existe e é real, mas **não altera percentual de direcionamento de
  LCA**, pelas fontes encontradas — publicada com a **Res. CMN 5.314/2026** em 25/06/2026,
  vigência 01/07/2026, trata de **regras do Proagro** (taxas, apuração de perdas) e de
  **restrições socioambientais** em crédito rural. Achado relevante para o rascunho: recursos
  captados via LCA passam a contar como recursos direcionados pela política oficial de crédito
  rural por causa do benefício fiscal associado à isenção — confirmação regulatória explícita,
  em 2026, do argumento central do texto (a isenção é o que amarra a LCA ao crédito rural).
  - Portal do Cooperativismo Financeiro, "CMN muda regras do crédito rural e do Proagro às
    vésperas do Plano Safra 2026/27".
    https://cooperativismodecredito.coop.br/2026/06/cmn-muda-regras-do-credito-rural-e-do-proagro-as-vesperas-do-plano-safra-2026-27/
  - PSAA, "Informativo 10/2026 – Publicada Resolução CMN 5.314/2026".
    https://psaa.com.br/informativo-10-2026-publicada-resolucao-cmn-5-314-2026-que-altera-as-regras-de-prorrogacao-do-credito-rural-e-fontes-de-recursos/

  **Conclusão para o `[VERIFICAR]` item 8:** pelas fontes encontradas, a Res. 5.315/2026 trata
  de Proagro e regra socioambiental, **não** de percentual de direcionamento — o 60% continua
  vindo da Res. 5.216/2025. Nenhum dos dois textos legais foi aberto diretamente (bloqueios de
  acesso) — etapa 7 deve confirmar no site oficial do CMN/BCB.

### 3c. Participação da LCA no crédito rural caindo — contraponto na direção oposta

- **CNA** (via CNN Brasil), "Taxação de LCAs desestimula investidores e impacta crédito rural,
  diz CNA" — dado: a participação da LCA no financiamento total do crédito rural **caiu de
  43% na safra 2023/2024 (R$ 169,12 bi) para 29% na safra 2024/2025 (R$ 97,89 bi de um total
  de R$ 333,74 bi)**. CNA propôs elevar a exigibilidade de direcionamento para 85% (posição de
  lobby setorial, não confirmado se foi aceita).
  https://www.cnnbrasil.com.br/economia/macroeconomia/taxacao-de-lca-desestimula-investidores-e-impacta-credito-rural-avalia-cna/
  (acesso 2026-09-18)
- **Campo Grande News**, "Tributação para compensar perda do IOF ameaça crédito rural e
  produção agrícola", 10/06/2025 — mesmo dado (43% → 29%), fontes nomeadas: senadora Tereza
  Cristina (PP-MS), CNA, advogado Rodrigo Totino.
  https://www.campograndenews.com.br/lado-rural/tributacao-para-compensar-perda-do-iof-ameaca-credito-rural-e-producao-agricola
  (acesso 2026-09-18)

  **Contraponto genuíno, mas na direção oposta à hipótese original:** não é "a isenção
  beneficia demais o banco", é "mesmo com a isenção, a LCA está perdendo relevância como fonte
  de crédito rural" ano após ano — efeito combinado de ameaça de tributação, prazo mínimo e
  concorrência de CPR e CRA. O fato bruto (queda de participação) tem número oficial; o
  diagnóstico de causa vem de fonte interessada (CNA representa o setor, quer mais
  exigibilidade).

### 3d. Fiscalização do lastro — achado fraco, não usar como afirmação

Não encontrada fonte de mercado ou regulatória que critique diretamente a fiscalização do
lastro da LCA como insuficiente. Único achado adjacente: o MCR do Bacen (resumo indireto, não
texto completo) menciona que transferências interfinanceiras não podem lastrear LCA por
dificuldade de supervisão — só o DIR (depósito interfinanceiro vinculado a crédito rural,
registrado em câmara de compensação) é lastro elegível. É restrição normativa preventiva, não
crítica ativa de falha de fiscalização. **Sem fonte para afirmar que a fiscalização atual é
insuficiente** — se o texto quiser esse ângulo, precisa de fonte própria.

---

## 4. Leads para os `[VERIFICAR]` do rascunho (não veredito — só sinalização, para a etapa 7)

| Item do inventário (`00-leitura.md`) | O que a pesquisa de mercado sugere |
|---|---|
| **#8** — direcionamento 60% (Res. CMN 5.216/2025) e se Res. 5.315/2026 alterou percentual | 60% confirmado por 3 fontes independentes, vigência 01/07/2025. Res. 5.315/2026 trata de Proagro e regra socioambiental, não de percentual de direcionamento, pelas fontes encontradas. Etapa 7 deve confirmar direto no texto legal (MCR do Bacen e nota do Ministério da Fazenda bloquearam o fetch do agente). |
| **#14** — resolução do CMN de maio/2025, prazo mínimo LCA de 9 para 6 meses | **Confirmado com número exato: Resolução CMN nº 5.215/2025**, válida para títulos emitidos a partir de 23/05/2025. Fontes concordantes: ABBC (https://abbc.org.br/resolucao-cmn-no-5-215-2025-ajuste-nos-prazos-minimos-de-vencimento-da-lci-e-da-lca/), Exame (https://exame.com/economia/cmn-reduz-prazo-minimo-das-lcas-e-lcis-de-9-para-6-meses/), SABZ Advogados, IRIB, Pinheiro Guimarães. |
| **#15** — MP 1.303/2025 (5% IR sobre novas emissões, caducidade 8/10/2025) | Corroborado: IRRF de 5% sobre rendimentos de títulos isentos para emissões a partir de 01/01/2026; caducou em outubro/2025 por não conversão em lei no prazo de 120 dias. Fontes: InfoMoney (https://www.infomoney.com.br/minhas-financas/mp-1-303-cai-no-congresso-veja-como-fica-a-tributacao-dos-investimentos-agora/), Senado Notícias (https://www12.senado.leg.br/noticias/materias/2025/07/22/mp-de-compensacao-do-iof-e-prorrogada-ate-outubro). **Data exata "8/10/2025" não confirmada** — fontes falam em "outubro de 2025"/120 dias, sem cravar o dia. |
| **#13** — teto global do FGCoop | Pesquisa de mercado indica R$ 250 mil por CPF/CNPJ por instituição (igual ao FGC), mas **não encontrada confirmação de teto global agregado a cada 4 anos** equivalente ao do FGC. Etapa 7 deve checar direto em fgcoop.coop.br (bloqueou o fetch do agente). |
| **#19** — edição do Fabozzi, referência do artigo do Caffagni | Fora do escopo de pesquisa de mercado — checagem bibliográfica pontual, mais adequada à etapa 7 diretamente. |

---

## 5. LCA × CRA por risco (teste de transferência da Ficha de Saída)

- **Melver**, "Entenda as Diferenças entre LCA e CRA" — LCA é emitida só por bancos, "menos
  risco (e retorno)" por ser garantida pelo FGC; CRA é emitida por securitizadora, sem
  cobertura do FGC, com a saúde financeira da companhia como garantia do negócio.
  https://www.melver.com.br/blog/lca-ou-cra-voce-conhece-as-diferencas/ (acesso 2026-09-18)
- **StoneX**, "CRA: o que é, como funciona e diferenças à LCA" — CRA carrega risco de
  crédito, de liquidez e de garantia (sem FGC, depende do emissor, garantias reais não
  eliminam inadimplência); posiciona CRA como alternativa de maior risco que paga mais
  precisamente pela ausência de proteção do FGC.
  https://www.stonex.com/pt-br/empresas/glossario-financeiro/cra/ (acesso 2026-09-18)

Ambas sustentam exatamente a tabela "LCA não é CRA" do rascunho — nenhuma fonte de mercado
pesquisada contesta essa distinção (é consenso, não há debate genuíno aqui). Achado
complementar: as fontes tratam a diferença de retorno como consequência direta da diferença de
risco — o mesmo enquadramento que o rascunho já usa na frase "olhar para o risco errado".

---

## O que ficou sem fonte confiável (sinalizar, não aproximar)

1. **"LCI sobe ~20%" (nota do autor, item 9 do inventário)** — sem dado encontrado que
   sustente alta de estoque de LCI em 2026; os dados de taxa e de volume de emissão apontam
   queda de LCI, não alta. Tratar como não confirmado até a etapa 7 achar a fonte primária
   B3/Quantum exata.
2. **Data exata "8/10/2025" da caducidade da MP 1.303/2025** — confirmado "outubro de 2025" e
   o mecanismo, não o dia exato.
3. **Teto global agregado do FGCoop** — não encontrado; só o teto individual de R$ 250 mil por
   instituição foi confirmado.
4. **Crítica direta e nomeada à fiscalização do direcionamento como insuficiente** — não
   encontrada; achado mais próximo foi uma restrição normativa preventiva sobre lastro por
   transferência interfinanceira, que não é a mesma coisa.
5. **Texto legal integral da Res. CMN 5.216/2025 e do MCR do Bacen sobre LCA** — fetch direto
   bloqueado (conteúdo restrito/redirecionamento). Confirmação do 60% vem de fontes
   secundárias consistentes entre si, não da fonte primária lida diretamente.
