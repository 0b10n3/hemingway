# O Papel do CDB na Transformação de Prazos

*Notas de um Professor — primeira nota da série.*

## O dinheiro que você não pode usar, e o banco também não

Todo mês, uma parte do dinheiro parado numa conta corrente comum permanece, teoricamente,
disponível o tempo todo: o titular pode sacar a qualquer momento, e o banco não pode
livremente aplicar esse saldo em outra operação. Não por acordo comercial, mas por regra do
Banco Central: hoje, o compulsório sobre recursos à vista — a parcela que o banco é obrigado
a reter numa conta no próprio Banco Central, sem poder emprestar — é de 21%, contra 20% para
recursos captados a prazo, como o CDB (Certificado de Depósito Bancário). A diferença parece
pequena. Ela não é: é o primeiro sinal de que o CDB não é só um produto de investimento com
nome estranho, é um contrato que libera uma fração maior do dinheiro do investidor para o
banco usar — porque o investidor abriu mão, ele também, de parte da disponibilidade imediata.

## O que é, de fato, um CDB

O CDB é um título de renda fixa emitido exclusivamente por bancos e outras instituições
financeiras, representativo de um depósito a prazo: ao comprá-lo, o investidor empresta
dinheiro ao banco e recebe, em troca, a promessa de receber de volta o valor aplicado,
acrescido de juros, numa data futura (ou a qualquer momento, nas modalidades com liquidez
diária). É a definição da Comissão de Valores Mobiliários, com base na Lei nº 4.728/1965: um
título de crédito nominativo, transferível e de livre negociação, representativo de promessa
de pagamento do valor depositado junto ao emissor, acrescido da remuneração combinada no
momento da aplicação.

A remuneração pode ser prefixada (uma taxa fixa definida na contratação), pós-fixada (mais
comumente atrelada ao CDI, o Certificado de Depósito Interbancário — ver seção seguinte) ou
híbrida, combinando um índice de inflação como o IPCA com um spread prefixado.

O risco de crédito do CDB é baixo, mas não inexistente: o capital aplicado conta com a
cobertura do Fundo Garantidor de Créditos (FGC), até R$ 250 mil por CPF ou CNPJ, por
instituição ou conglomerado financeiro, com um teto global de R$ 1 milhão a cada período de
quatro anos, em caso de liquidação ou intervenção no banco emissor. A cobertura reduz o risco
para o valor garantido, mas não elimina fricção prática: um processo de liquidação leva
tempo até o ressarcimento ser concluído, e qualquer valor acima do teto simplesmente não é
recuperado.

## O outro lado do balcão: o CDB como passivo do banco

Para o investidor, o CDB é ativo: instrumento de acumulação de capital e gestão de liquidez.
Para o banco que o emite, é o oposto — é passivo, é dívida. E é aí que mora a função real do
produto no sistema financeiro.

A área responsável por administrar esse passivo dentro do banco chama-se ALM (Asset and
Liability Management, ou Gestão de Ativos e Passivos): sua missão é captar recursos — via
CDB, entre outros instrumentos — para financiar operações de crédito, que são os ativos do
banco. O ALM gerencia o risco de taxa de juros e o risco de liquidez, garantindo que o banco
capte a um custo menor do que empresta (a diferença é o spread bancário) e que os prazos de
captação e de crédito estejam equilibrados o suficiente para nunca faltar dinheiro em caixa.

O Banco Central usa, para descrever esse mecanismo, um termo técnico direto: transformação de
maturidade. No Relatório de Estabilidade Financeira de abril de 2018, o Bacen explica que
parte da regulação bancária existe justamente para "mitigar excessos no processo de
transformação de maturidade realizado pelas instituições" — ou seja, no processo pelo qual um
banco pega dinheiro captado a prazos curtos (como um CDB de liquidez diária) e o transforma em
crédito concedido a prazos longos (um financiamento imobiliário, por exemplo). É esse processo
que dá ao CDB seu papel: não é só onde o investidor guarda dinheiro, é o mecanismo pelo qual
o sistema bancário converte poupança de curto prazo em crédito de longo prazo.

![Ilustração: fluxo do dinheiro do depositante ao tomador de crédito — depósito em CDB entra como passivo do banco e sai como ativo de crédito, com a área de ALM administrando o descasamento de prazos no meio](ilu-01)

## CDB não é CDI

É comum confundir os dois termos, mas eles cumprem funções diferentes. O CDB é o produto: um
título vendido pelo banco ao público em geral, pessoa física ou jurídica, para captar recursos
e expandir sua carteira de crédito. O CDI (Certificado de Depósito Interbancário) não é um
produto de investimento — é uma taxa de referência: título emitido e negociado exclusivamente
entre bancos, com prazo de um dia útil, para equilibrar o caixa diário entre eles, já que o
Banco Central não permite que uma instituição feche o dia com saldo negativo.

A taxa que baliza o mercado, chamada de taxa DI, é calculada e divulgada pela B3: é a média
ponderada das taxas de operações de CDI de um dia entre bancos de conglomerados diferentes,
registradas na própria B3. Um CDB pós-fixado usa essa taxa como indexador do seu rendimento
diário — é comum, embora não universal, que o CDB pós-fixado seja atrelado a um percentual do
CDI (90%, 100%, 110%, por exemplo). É essa ligação — CDB remunerado com base na taxa DI, que
por sua vez reflete o custo do dinheiro entre bancos — que costuma gerar a confusão entre os
dois termos.

![Gráfico: crescimento de capital de um CDB pós-fixado em diferentes percentuais do CDI (90%, 100%, 110%) ao longo de um horizonte de investimento](graf-01)

## Por que o banco precisa emitir CDB: a regra que o Bacen impõe

A decisão de um banco de emitir CDBs não é só comercial — é uma necessidade imposta pela
regulação do Banco Central, em pelo menos três frentes.

A primeira é o próprio compulsório mencionado na abertura: o Bacen exige que os bancos
recolham uma parcela de tudo o que captam. Quando um banco expande sua carteira de crédito,
precisa repor caixa e respeitar limites de alavancagem — e uma das formas de repor é emitir
CDB.

A segunda é a exigência de colchões de liquidez sob as normas de Basileia III, adotadas no
Brasil pelo Conselho Monetário Nacional e regulamentadas pelo Bacen: o LCR (Liquidity Coverage
Ratio, instituído pela Resolução CMN nº 4.401/2015), que mede a capacidade do banco de resistir
a um estresse de liquidez de curto prazo, e o NSFR (Net Stable Funding Ratio, instituído pela
Resolução CMN nº 4.616/2017), que mede o financiamento estável de longo prazo — a mesma norma
citada na seção anterior sobre transformação de maturidade.

A terceira é a qualidade do funding captado. No cálculo do NSFR, cada fonte de recursos do
banco recebe um peso conforme sua estabilidade estatística. O dinheiro de pessoas físicas
captado via CDB é tratado como funding mais estável — recebendo um fator de financiamento
maior no cálculo do índice [VERIFICAR: percentual exato de ASF atribuído a depósito de varejo
no NSFR, Circular BC nº 3.869/2017] — porque o varejo pulverizado é, estatisticamente, muito
menos propenso a sacar tudo de uma vez do que um investidor institucional concentrado. Emitir
CDB para o público, portanto, não é só captar dinheiro: é melhorar a saúde regulatória do
banco.

## Onde o CDB entra na sua carteira

A mesma característica que explica a existência do CDB do lado do banco — a transformação de
um compromisso de prazo em outro — é o que define seu uso do lado do investidor, de forma
diferente conforme o prazo e o indexador escolhidos.

Para reserva de emergência, o CDB pós-fixado com liquidez diária, rendendo próximo de 100% do
CDI, garante resgate imediato sem risco de perda de capital por oscilação de mercado — é o
uso mais próximo de um depósito à vista remunerado.

Para um objetivo com prazo definido, como a compra de um imóvel em dois anos, um CDB
prefixado — a uma taxa combinada no momento da aplicação, como exemplo hipotético, 11% ao
ano — trava a rentabilidade: o investidor sabe exatamente o valor nominal que vai resgatar,
independentemente do que aconteça com a Selic no meio do caminho.

Para proteção patrimonial de médio e longo prazo, entre três e sete anos, um CDB atrelado à
inflação (IPCA mais um spread prefixado) garante ganho real: protege o poder de compra do
capital, independentemente do cenário macroeconômico.

Em qualquer um dos três casos, o que o investidor está negociando com o banco é o mesmo: abrir
mão de disponibilidade imediata em troca de remuneração — a mesma transformação de prazo que,
do outro lado do balcão, permite ao banco financiar o crédito de longo prazo. O CDB não é um
produto entre outros na prateleira da renda fixa. É a peça pela qual o sistema bancário
converte poupança de curto prazo em crédito de longo prazo — e essa função, não a
rentabilidade que ele paga, é o que explica por que existe, como é remunerado e por que é tão
de perto regulado.
