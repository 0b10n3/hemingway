
---

## titulo: 2026-09-18_O_Agro_é_POP_O_Agro_é_Produto_Financeiro 
### subtitulo LCA: quanto rende, quanto custa, quanto vale"

<!-- NOTAS DO AUTOR PARA O PIPELINE (não fazem parte do texto) Tese central: a LCA é uma dívida do banco, não do agro. O lastro rural define para onde o dinheiro vai; quem paga o investidor é o balanço do banco. E, como todo produto da série, a isenção não é generosidade: é um benefício fiscal repartido entre banco e investidor. Fio condutor: separar três perguntas que se confundem — (1) quanto a LCA rende para quem compra; (2) quanto custa para quem emite (qual taxa o banco oferece); (3) quanto ela vale hoje (marcação a mercado). Insumo para a Ficha de Saída (etapa 2). Ao final, o leitor deve conseguir: - explicar por que o risco da LCA é o banco, e não o produtor rural; - calcular o break-even real de uma LCA contra um CDB, sabendo por que a regra linear erra; - precificar uma LCA prefixada bullet e descrever a marcação de uma pós-fixada em % do CDI; - distinguir taxa contratual de taxa de mercado; - diferenciar LCA de CRA pelo risco que cada uma carrega. Material aproveitável do draft v2 (conversa anterior sobre LCA): tabela de break-even, FGC sobre principal + juros, FGC × FGCoop, direcionamento de 60%, MP 1.303 e IRPFM. Trouxe aqui só o que serve ao fio das três perguntas. 

[CAPA] - Como capa podemos construir uma imagem de paper cut que mostre uma cena de transformação do agro  para o banco 
-->

No texto sobre LCI, terminei sugerindo que, para entender a LCA, poderíamos  trocar "imobiliário" por "agronegócio". É um bom começo, mas não suficiente. 

A estrutura do produto é parecida. Mudam o lastro, a regra de direcionamento, a trajetória de preço e, principalmente, a forma de fazer a conta. E muitos erros em de análise sobre LCA nasce de misturar três perguntas diferentes:

- quanto a LCA rende para quem compra;
- quanto ela custa para quem emite;
- quanto ela vale hoje.

Este texto responde uma de cada vez.

## O que é uma LCA

A Letra de Crédito do Agronegócio é um título de renda fixa **emitido por uma instituição financeira**, que representa uma promessa de pagamento em dinheiro e fica vinculado a direitos creditórios do agronegócio. Foi criada pela Lei nº 11.076, de 30 de dezembro de 2004 — a mesma que instituiu CDCA, CRA, CDA e WA.

Sim, o título é do agronegócio mas emitido por insituição financeira.

Em termos simples: o investidor empresta dinheiro ao banco, o banco emite a LCA como comprovante dessa dívida e mantém uma carteira de créditos ao agro vinculada à emissão.

Existem, portanto, **duas relações de crédito** distintas:

1. o crédito do banco para o agronegócio, que forma o lastro;
2. o crédito do investidor contra o banco, representado pela LCA.

[diag-01: fluxo produtor/cooperativa ← banco ← investidor, com as duas relações de crédito rotuladas separadamente]

Esse é o ponto que sustenta todo o resto: quem compra LCA não assume o risco do produtor rural. A contraparte é o banco emissor. O lastro não transforma o investidor em credor de cada produtor — se o banco quebrar, a carteira rural não é "sua".

## O lado de quem emite: por que o banco capta com LCA

O banco não emite LCA porque "precisa de dinheiro". Ele compara fontes de captação — o chamado funding — e escolhe a mais barata que consegue sustentar: CDB, depósitos, Letras Financeiras, LCA.

A LCA ganha essa comparação por causa da isenção de IR para pessoa física. Uma LCA a 90% do CDI pode entregar ao investidor um retorno líquido maior que um CDB a 100% do CDI, e ainda assim custar menos ao banco. É aqui que a tese da série aparece de novo: a isenção é um benefício fiscal, e ele é repartido. Parte vira retorno líquido maior para o investidor, parte vira funding mais barato para o banco. Quem define a divisão é oferta e demanda.

Essa vantagem tem condições. A emissão depende de lastro elegível — operações ligadas à produção, comercialização, beneficiamento ou industrialização agropecuária — e das regras de direcionamento, que obrigam o banco a aplicar parte dos recursos captados em crédito rural. [VERIFICAR: direcionamento de 60% (Res. CMN 5.216/2025) e se a Res. CMN 5.315/2026 alterou percentuais; reconferir no MCR na semana da publicação]

Cabe ao emissor casar volume, prazo e indexador das LCAs com os créditos que as lastreiam. É gestão de ativos e passivos, não formalidade: se o lastro encolhe, a capacidade de emitir encolhe junto.

<!-- Nota do autor: decidir se entra o parágrafo sobre 2026 (estoque de LCA caindo 4% no 1º semestre enquanto LCI sobe 20%; taxa média da LCA de 12 meses de 90,05% para 88,24% do CDI). Ilustra bem que o limite da LCA é o lastro, não a demanda. Se entrar, fontes: B3 e Quantum Finance. -->

## O lado de quem compra: quanto a LCA rende de verdade

### A conta que todo mundo faz

A comparação de bolso entre uma LCA isenta e um CDB tributado é:

$$ \text{Taxa}_{\text{CDB equivalente}} = \frac{\text{Taxa}_{\text{LCA}}}{1 - IR} $$

Com uma LCA a 90% do CDI e alíquota de 15%: 90% / 0,85 ≈ 105,88% do CDI.

### Por que essa conta erra

O IR do CDB é uma mordida única sobre o ganho acumulado no resgate. A diferença de taxa entre os dois papéis, por outro lado, capitaliza todos os dias. Quanto mais longo o prazo, maior o efeito dos juros compostos sobre essa diferença — e mais a regra linear exagera o quanto o CDB precisa pagar.

O break-even correto é o percentual $x$ do CDI que iguala os ganhos líquidos:

$$ (1 - IR)\left[(1 + x \cdot d)^{n} - 1\right] = (1 + p \cdot d)^{n} - 1 $$

onde $p$ é o percentual da LCA, $d = (1 + CDI)^{1/252} - 1$ é o CDI diário e $n$ o número de dias úteis.

Com CDI de 14% ao ano e LCA a 90% do CDI:

|Prazo|IR do CDB|Regra linear|Break-even real|
|---|---|---|---|
|6 meses|20%|112,5%|111,7%|
|1 ano|17,5%|109,1%|107,8%|
|2 anos|15%|105,9%|103,9%|
|3 anos|15%|105,9%|103,0%|
|5 anos|15%|105,9%|101,6%|

[graf-01: prazo no eixo X; duas linhas — regra linear (em degraus) e break-even real (descendente); a área entre elas é o erro] [VERIFICAR: CDI vigente na data de publicação; recalcular a tabela. 6 meses = 126 d.u. ≈ 182 dias corridos, faixa de 20%]

Numa LCA de cinco anos, o CDB precisa de bem menos do que a regra diz. A isenção vale mais no curto e médio prazo; no papel longo, ou o emissor compensa na taxa, ou a vantagem quase some.

### O risco é o banco

Duas LCAs a 90% do CDI, com o mesmo prazo e a mesma liquidez, não são equivalentes se os emissores forem diferentes. O risco principal é a capacidade de pagamento do banco.

A LCA tem cobertura do FGC: até R$ 250 mil por CPF ou CNPJ, por instituição ou conglomerado, com teto global de R$ 1 milhão a cada quatro anos. Dois detalhes que mudam a conta:

- o limite vale para principal mais rendimentos, não para o valor aplicado;
- LCAs de marcas diferentes do mesmo conglomerado dividem o mesmo limite.

<!-- Nota do autor: LCA de cooperativa de crédito é coberta pelo FGCoop, não pelo FGC. Decidir se entra aqui em uma frase. -->

[VERIFICAR: teto global do FGCoop, se a menção entrar]

### Carência e liquidez

Desde maio de 2025, o prazo mínimo de vencimento de LCAs sem atualização por índice de preços é de seis meses (antes, nove). Liquidez antes disso depende do contrato de cada emissão, e o mercado secundário é raso. [VERIFICAR: número da resolução do CMN de maio/2025]

<!-- Nota do autor: MP 1.303/2025 propôs 5% de IR sobre novas emissões e caducou em 8/10/2025. Serve para lembrar que a isenção é política pública, não propriedade do título. Decidir se entra. IRPFM (Lei 15.270/2025) preserva LCA fora da base — relevante só para alta renda; talvez fique para o texto "Por quanto tempo vale ser isento?". -->

## Como o banco define a taxa de emissão

Do ponto de vista da tesouraria, a taxa oferecida pode ser decomposta assim:

$$ \text{Taxa}_{\text{LCA}} = \text{Taxa}_{\text{base}} + \text{Spread}_{\text{crédito}} + \text{Prêmio}_{\text{liquidez}} + \text{Ajuste}_{\text{prazo}} - \text{Benefício}_{\text{tributário}} $$

Não é uma fórmula operacional. É uma forma de enxergar o que entra no preço. [VERIFICAR: numa LCA em % do CDI os componentes não se somam literalmente; deixar explícito que a decomposição é conceitual ou reescrever em termos de spread sobre a curva]

O que move cada parcela cabe em três blocos:

|Bloco|O que pesa|
|---|---|
|Risco do emissor|qualidade de crédito, capital, liquidez, concentração, rating|
|Características do título|vencimento, indexador, carência, resgate antecipado, tamanho da emissão|
|Condições de mercado|nível da Selic, inclinação da curva, competição entre bancos, demanda de pessoa física, mudanças regulatórias|

Some a isso a urgência do banco: quem precisa captar rápido paga mais; quem tem fila de investidor paga menos.

## Quanto a LCA vale hoje

### Taxa contratual não é taxa de mercado

Este é o erro mais comum na precificação:

- a taxa contratual determina o que o título paga;
- a taxa de mercado determina quanto esse pagamento vale hoje.

### LCA prefixada bullet

Numa LCA prefixada bullet — principal e juros pagos de uma vez no vencimento —, o preço unitário é o valor de vencimento descontado pela taxa de mercado:

$$ PU = \frac{VF}{(1 + y)^{du/252}} $$

Com VF de R$ 1.100, 252 dias úteis até o vencimento e taxa de mercado de 12% a.a.: PU = 1.100 / 1,12 = R$ 982,14. Se a taxa de mercado sobe para 14%: PU = 1.100 / 1,14 = R$ 964,91.

Taxa sobe, preço cai. É a base de toda marcação a mercado.

Com fluxos intermediários, cada pagamento é descontado pela taxa do seu prazo:

$$ PU = \sum_{i=1}^{n} \frac{FC_i}{(1 + y_i)^{du_i/252}} $$

### LCA em percentual do CDI

Numa LCA a 90% do CDI, o saldo acumulado até a data de avaliação é:

$$ \text{Saldo}_t = \text{Principal} \times \prod_{j=1}^{m} \left[1 + 0{,}90 \times \left((1 + CDI_j)^{1/252} - 1\right)\right] $$

Na prática, valem as convenções do contrato: truncamento, arredondamento, defasagem.

Para marcar antes do vencimento: acumula-se o que já foi apropriado, projeta-se o CDI futuro pela curva DI, estima-se o valor no vencimento e desconta-se esse valor pela curva de mercado do emissor.

### Qual curva usar para descontar

Sem negócios no secundário, a taxa de desconto precisa ser construída. Uma ordem razoável de referências:

1. negócios recentes da própria LCA;
2. ofertas firmes de compra e venda;
3. outras LCAs do mesmo banco;
4. Letras Financeiras do mesmo emissor, ajustadas;
5. CDBs do mesmo banco;
6. bancos comparáveis;
7. taxa de emissão, ajustada pela mudança de curva e de risco.

A curva de LF é tentadora porque é a melhor leitura do risco da tesouraria do banco. Mas LF e LCA diferem em prazo mínimo, senioridade, tributação, cobertura do FGC e público investidor. A LF serve de referência relativa, não de curva final.

## LCA não é CRA

||LCA|CRA|
|---|---|---|
|Emissor|instituição financeira|companhia securitizadora|
|Risco primário|banco emissor|créditos e garantias do patrimônio separado|
|Lastro|direitos creditórios do agro vinculados|direitos creditórios securitizados|
|FGC|coberta, dentro dos limites|sem cobertura|
|Como analisar|crédito bancário e funding|crédito do devedor, estrutura, garantias e fluxo|

Analisar CRA como se fosse LCA — ou o contrário — é olhar para o risco errado.

## Fechamento: do produto ao balanço

Um banco tem uma carteira de crédito rural remunerada a CDI + 4% ao ano e emite uma LCA de dois anos a 88% do CDI.

A leitura ingênua é olhar a diferença entre as duas taxas e chamar de margem. A leitura correta pergunta pelo que essa diferença precisa pagar: inadimplência esperada, custo de capital alocado ao crédito, descasamento de prazo entre ativo e passivo, pré-pagamento dos créditos, custo alternativo de funding e as exigências de lastro e direcionamento. [VERIFICAR: com 60% de direcionamento, nem todo real captado vai para a carteira a CDI + 4%; ajustar o exemplo ou explicitar a premissa]

Esse é o salto entre entender a LCA como produto de investimento e entendê-la como instrumento de gestão do balanço de um banco.

<!-- Nota do autor: manter ou não a pergunta ao leitor — "sem negócios no secundário, o que deveria pesar mais na curva de uma LCA: a LF do mesmo banco, CDBs comparáveis ou LCAs de bancos pares?". Funciona como exercício e abre comentário. -->

## Para continuar aprendendo

- Lei nº 11.076, de 30 de dezembro de 2004 (texto compilado) — fonte primária da definição, emissão e lastro da LCA.
- José Carlos de Souza Santos e Armênio de Souza Rangel, _Precificação e risco nos mercados de renda-fixa_ (Editora CRV, 2016).
- Frank J. Fabozzi, _Bond Markets, Analysis and Strategies_.
- Luiz Cláudio Caffagni, "LCA: o título de crédito bancário para o agro".

[VERIFICAR: edição do Fabozzi e referência completa do artigo do Caffagni]