---
titulo: O Agro é POP, o Agro é Produto Financeiro!
subtitulo: A LCA é dívida do banco, não do agro — e a isenção que parece favor é benefício fiscal repartido entre os dois lados do balcão
slug: 2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro
data: 2026-09-18
linha_editorial: Notas de um Professor
status: rascunho
---

No texto sobre LCI, terminei sugerindo que, para entender a LCA, poderíamos trocar "imobiliário" por "agronegócio". É um bom começo, mas não suficiente.

A estrutura do produto é parecida. Mudam o lastro, a regra de direcionamento, a trajetória de preço e, principalmente, a forma de fazer a conta. E muitos erros de análise sobre LCA nascem de misturar três perguntas diferentes:

- quanto ela custa para quem emite;
- quanto a LCA rende para quem compra;
- quanto ela vale hoje.

Este texto responde uma de cada vez, começando pela mais básica: o que exatamente você compra quando compra uma LCA?

## O que é uma LCA

A Letra de Crédito do Agronegócio é um título de renda fixa 'emitido por uma instituição financeira', que representa uma promessa de pagamento em dinheiro e fica vinculado a direitos creditórios do agronegócio. Foi criada pela Lei nº 11.076, de 30 de dezembro de 2004, que também instituiu a CRA (Certificado de Recebíveis do Agronegócio) — o produto securitizado que compara com a LCA mais adiante neste texto.

Sim, o título é do agronegócio mas emitido por insituição financeira.

Em termos simples: o investidor empresta dinheiro ao banco, o banco emite a LCA como comprovante dessa dívida e mantém uma carteira de créditos ao agro vinculada à emissão.

Existem, portanto, 'duas relações de crédito' distintas:

1. o crédito do banco para o agronegócio, que forma o lastro;
2. o crédito do investidor contra o banco, representado pela LCA.

[diag-01: fluxo produtor/cooperativa ← banco ← investidor, com as duas relações de crédito rotuladas separadamente]

Esse é o ponto que sustenta todo o resto: quem compra LCA não assume o risco do produtor rural. A contraparte é o banco emissor. Diferente da CRA, a LCA não tem patrimônio separado — o regime que, numa securitização, isola os créditos do resto da empresa emissora. A carteira rural fica vinculada à emissão, mas dentro do balanço do próprio banco; o lastro não transforma o investidor em credor de cada produtor. Se o banco quebrar, a carteira rural não é "sua".

Até aqui, é a definição que qualquer prospecto do banco traz. O interessante começa agora — no lado de quem emite, e no lado de quem faz a conta errada na hora de comprar.

## O lado de quem emite: por que o banco capta com LCA

O banco não emite LCA porque "precisa de dinheiro". Ele compara fontes de captação — o chamado funding — e escolhe a mais barata que consegue sustentar: CDB, depósitos, Letras Financeiras, LCA.

A LCA ganha essa comparação por causa da isenção de IR para pessoa física. Uma LCA a 90% do CDI pode entregar ao investidor um retorno líquido maior que um CDB a 100% do CDI, e ainda assim custar menos ao banco. É aqui que a tese da série aparece de novo: a isenção é um benefício fiscal, e ele é repartido. Parte vira retorno líquido maior para o investidor, parte vira funding mais barato para o banco. Quem define a divisão é oferta e demanda — e quanto disso chega a cada lado é, na prática, pouco transparente: nem o regulador nem o investidor têm hoje uma forma simples de medir a proporção exata.

Essa vantagem tem condições. A emissão depende de lastro elegível — operações ligadas à produção, comercialização, beneficiamento ou industrialização agropecuária — e das regras de direcionamento, que obrigam o banco a aplicar 60% dos recursos captados em crédito rural — percentual elevado de 50% pela Resolução do CMN (Conselho Monetário Nacional, o órgão que define as regras do sistema financeiro) nº 5.216/2025, em vigor desde 1º de julho daquele ano. Uma resolução mais recente do CMN, a de nº 5.315/2026, mexeu em regras do Proagro e em restrição socioambiental ao crédito rural — não nesse percentual. [VERIFICAR: confirmar os dois números e vigências direto no texto das resoluções (MCR do Bacen) antes de publicar — a pesquisa da etapa 3 só confirmou via fontes secundárias]

Cabe ao emissor casar volume, prazo e indexador das LCAs com os créditos que as lastreiam. É o mesmo raciocínio por trás do compulsório e dos índices de liquidez que os bancos reportam ao regulador: captação e crédito precisam ficar emparelhados, não só em volume, mas em prazo. Se o lastro encolhe, a capacidade de emitir encolhe junto — não é formalidade, é gestão de ativos e passivos.

Em 2026, esse limite já aparece nos números: a taxa média da LCA de 12 meses caiu de 90,05% para 88,24% do CDI entre 2025 e 2026 (Quantum Finance, via InfoMoney, 11/06/2026). [VERIFICAR: estoque de LCA em queda de cerca de 4% no primeiro semestre de 2026 — fonte plausível é B3 (27/07/2026), mas o número não foi confirmado com o artigo original antes de publicar]

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

A LCA tem cobertura do FGC (Fundo Garantidor de Créditos, o seguro que cobre depósitos e alguns títulos bancários até um limite por CPF/CNPJ): até R$ 250 mil por CPF ou CNPJ, por instituição ou conglomerado, com teto global de R$ 1 milhão a cada quatro anos. Dois detalhes que mudam a conta:

- o limite vale para principal mais rendimentos, não para o valor aplicado;
- LCAs de marcas diferentes do mesmo conglomerado dividem o mesmo limite.

LCA de cooperativa de crédito, porém, é coberta pelo FGCoop (Fundo Garantidor do Cooperativismo de Crédito, o equivalente ao FGC para cooperativas), não pelo FGC — sistema de garantia separado, com o mesmo teto individual de R$ 250 mil por instituição. [VERIFICAR: teto global do FGCoop, equivalente ao R$ 1 milhão a cada quatro anos do FGC — não encontrado na pesquisa da etapa 3, confirmar direto em fgcoop.coop.br]

### Carência e liquidez

Desde maio de 2025, o prazo mínimo de vencimento de LCAs sem atualização por índice de preços é de seis meses (antes, nove) — mudança trazida pela Resolução CMN nº 5.215/2025, válida para títulos emitidos a partir de 23 de maio daquele ano. [VERIFICAR: confirmar número e data direto no texto da resolução antes de publicar] Liquidez antes disso depende do contrato de cada emissão, e o mercado secundário é raso.

## Como o banco define a taxa de emissão

Voltamos à pergunta de quanto a LCA custa — agora do ponto de vista da política de preços da tesouraria, não só da motivação de funding. Antes dos números: a ideia aqui não é montar uma conta, é mapear o que entra no preço. Do ponto de vista da tesouraria, a taxa oferecida pode ser decomposta assim:

$$ \text{Taxa}_{\text{LCA}} = \text{Taxa}_{\text{base}} + \text{Spread}_{\text{crédito}} + \text{Prêmio}_{\text{liquidez}} + \text{Ajuste}_{\text{prazo}} - \text{Benefício}_{\text{tributário}} $$

Não é uma fórmula operacional, muito menos uma equação para resolver — numa LCA cotada em percentual do CDI, esses componentes não se somam de forma literal. É uma forma de enxergar o que entra no preço, bloco por bloco.

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

Um banco tem uma carteira de crédito rural remunerada a CDI + 4% ao ano e emite uma LCA de dois anos a 88% do CDI — para simplificar, suponha que todo o volume dessa emissão esteja alocado nessa carteira (na prática, só 60% do captado por LCA precisa ir para crédito rural; o restante financia outras operações do banco, a outras taxas).

A leitura ingênua é olhar a diferença entre as duas taxas e chamar de margem. A leitura correta pergunta pelo que essa diferença precisa pagar: inadimplência esperada, custo de capital alocado ao crédito, descasamento de prazo entre ativo e passivo, pré-pagamento dos créditos, custo alternativo de funding e as exigências de lastro e direcionamento.

Esse é o salto entre entender a LCA como produto de investimento e entendê-la como instrumento de gestão do balanço de um banco. Dito direto: a LCA é dívida do banco, não do agro — e a isenção que parece favor é benefício fiscal, repartido entre quem empresta e quem capta. É também a fronteira que separa a LCA da CRA — outro título do agro, mas de risco completamente diferente, tema do próximo texto desta série.

Fica a pergunta para fechar: sem negócios no secundário, o que deveria pesar mais na curva de uma LCA — a LF do mesmo banco, CDBs comparáveis ou LCAs de bancos pares?

## Para continuar aprendendo

- Lei nº 11.076, de 30 de dezembro de 2004 (texto compilado) — fonte primária da definição, emissão e lastro da LCA.
- José Carlos de Souza Santos e Armênio de Souza Rangel, _Precificação e risco nos mercados de renda-fixa_ (Editora CRV, 2016) — referência para a mecânica de precificação e marcação a mercado de renda fixa usada neste texto.
- Frank J. Fabozzi, _Bond Markets, Analysis and Strategies_ — tratamento padrão de mercado internacional para análise e precificação de títulos de renda fixa, base da lógica de desconto por curva usada na seção "Quanto a LCA vale hoje".
- Luiz Cláudio Caffagni, "LCA: o título de crédito bancário para o agro" — leitura direcionada especificamente à LCA como instrumento de crédito bancário, não de securitização.

[VERIFICAR: edição do Fabozzi e referência completa do artigo do Caffagni]

---

## Notas laterais de integração — rodada 2 (pós-crítica estrutural)

Resposta a cada achado de `05-critica.md` (rodada 1). Achados de acabamento/conteúdo,
resolvidos dentro desta rodada de etapa 4, sem nova reestruturação — conforme o veredito da
própria crítica.

- **Achado 1 (severidade alta, subtítulo sem tese):** resolvido na etapa 2 (retorno
  registrado em `02-estrutura.md`) — novo subtítulo carrega a tese de fundo.
- **Achado 2 (ordem custa/rende/custa/vale):** bullets da abertura reordenados para
  custa→rende→vale (ordem de primeira aparição real). Adicionada frase de transição no início
  de "Como o banco define a taxa de emissão" ("Voltamos à pergunta de quanto a LCA custa...")
  para avisar o leitor que o texto está retomando o tema, em vez de reordenar seções — decisão
  registrada em `02-estrutura.md`, não é mudança de argumento.
- **Achado 3 (CRA sem glosa):** primeira menção de CRA, em "O que é uma LCA", ganhou glosa
  completa ("Certificado de Recebíveis do Agronegócio") e uma frase de antecipação apontando
  para a comparação mais adiante.
- **Achado 4 (CDCA, CDA, WA sem uso):** cortados. A frase da Lei 11.076 agora cita só a CRA,
  que é de fato usada depois — CDCA, CDA e WA não tinham papel argumentativo.
- **Achado 5 (FGC, FGCoop, CMN sem glosa):** os três ganharam definição funcional entre
  parênteses na primeira ocorrência.
- **Achado 6 (tese não isolada no fechamento):** adicionada frase isolada no "Fechamento" —
  "Dito direto: a LCA é dívida do banco, não do agro — e a isenção que parece favor é
  benefício fiscal, repartido entre quem empresta e quem capta." — ecoando o campo 3 da Ficha
  de Saída, cumprindo a regra 5.4 (tese isolada duas vezes: aqui e em "O que é uma LCA").
- **Achado 7 (bibliografia sem anotação):** os três itens sem razão declarada (Santos &
  Rangel, Fabozzi, Caffagni) ganharam uma cláusula cada, dizendo por que estão ali.
- **Achado 8 (movimento 4 raso):** acrescentada uma frase em "O lado de quem emite" ligando a
  gestão de ativos e passivos ao compulsório e aos índices de liquidez que os bancos reportam
  ao regulador — sem virar seção nova, só aprofundando o raciocínio institucional já presente.
- **Achado 9 (fórmula sem frase prévia):** adicionada frase de abertura em "Como o banco
  define a taxa de emissão" antes da fórmula.
- **Achado 10 (mecanismo de segregação patrimonial não nomeado):** adicionada, em "O que é
  uma LCA", a frase nomeando a ausência de patrimônio separado como o que distingue a LCA da
  CRA nesse ponto específico — antecipa e prepara a seção "LCA não é CRA".
- **Achado 11:** sem mudança — já era só registro.

Para o histórico completo de resolução dos marcadores do inventário original da etapa 0
(FGCoop, dado de 2026, MP 1.303, etc.), ver as notas laterais de `04-draft-v1.md` — continuam
válidas, esta rodada só endereça os achados novos da crítica estrutural.
