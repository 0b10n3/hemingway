# Verificação técnica — O Papel do CDB na Transformação de Prazos

*Laudo do agente `verificador-tecnico`, etapa 7 do pipeline, sobre `processo/04-draft-v1.md`.
Parte do trabalho retoma `03-pesquisa.md` (seis `[VERIFICAR]` já levantados); parte resolve
os dois flags técnicos deixados por `06-revisao.md` (itens 8 e 11). Cada item abaixo recebe
veredito e, quando há correção, o texto exato a aplicar na consolidação (etapa 9). Acesso a
todas as fontes: 2026-08-14.*

## 1. Flag da revisão, item 8 — definição de CDI (fricção conceitual "taxa" vs. "título")

**Veredito: ⚠️ Impreciso — corrigido.**

Fonte primária: B3, "Metodologia de Apuração da Taxa DI"
(https://www.b3.com.br/pt_br/market-data-e-indices/indices/indices-de-segmentos-e-setoriais/di/metodologia-de-apuracao-da-taxa/,
acesso 2026-08-14) — a B3 trata "Depósitos Interfinanceiros" (o instrumento/título) e "Taxa
DI" (a taxa calculada a partir das operações com esse instrumento) como coisas
categoricamente diferentes; a página nunca chama o CDI, em si, de "taxa".

O revisor está certo: a frase do draft define CDI primeiro como taxa ("é uma taxa de
referência") e, na sequência, como título ("título emitido e negociado exclusivamente entre
bancos") — as duas definições colidem, e o parágrafo seguinte já reserva "taxa DI" para o
índice calculado pela B3. A definição correta é: **CDI é o título** (o instrumento de
depósito interfinanceiro); **taxa DI é a taxa** calculada a partir das operações com esse
título. O draft tem os dois conceitos certos, só trocados de lugar na primeira frase.

**Correção exata proposta** — em "CDB não é CDI" (§5), trocar:

> "O CDI (Certificado de Depósito Interbancário) não é um produto de investimento — é uma
> taxa de referência: título emitido e negociado exclusivamente entre bancos, com prazo de um
> dia útil, para equilibrar o caixa diário entre eles, já que o Banco Central não permite que
> uma instituição feche o dia com saldo negativo."

por:

> "O CDI (Certificado de Depósito Interbancário) não é um produto de investimento — é um
> título emitido e negociado exclusivamente entre bancos, com prazo de um dia útil, para
> equilibrar o caixa diário entre eles, já que o Banco Central não permite que uma instituição
> feche o dia com saldo negativo."

(Basta remover "é uma taxa de referência:" — o resto da frase já descreve corretamente o
título. O parágrafo seguinte, que define "taxa DI" como a taxa calculada pela B3 a partir
dessas operações, não precisa de nenhuma alteração; ele já está certo e passa a ficar
consistente com a frase corrigida.)

## 2. Flag da revisão, item 11 — NSFR não é "a mesma norma" do Relatório de Estabilidade Financeira

**Veredito: ⚠️ Impreciso — corrigido.**

Confirmado por leitura direta dos dois documentos: a seção anterior (§3, "O outro lado do
balcão") cita o **Relatório de Estabilidade Financeira de abril de 2018** do Bacen (um
relatório institucional, seção 2.6, p. 62-63) como fonte da expressão "transformação de
maturidade". A seção "Por que o banco precisa emitir CDB" (§6) cita a **Resolução CMN nº
4.616, de 30 de novembro de 2017** (lida integralmente:
https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50474/Res_4616_v1_O.pdf) como a
norma que institui o limite mínimo do NSFR. São dois documentos de natureza diferente — um
relatório analítico e uma resolução normativa — publicados em datas diferentes (a Resolução é
de novembro de 2017; o Relatório, de abril de 2018, é posterior e comenta a resolução já
existente). O revisor está certo: não são "a mesma norma".

**Correção exata proposta** — em "Por que o banco precisa emitir CDB" (§6), trocar:

> "...e o NSFR (Net Stable Funding Ratio, instituído pela Resolução CMN nº 4.616/2017), que
> mede o financiamento estável de longo prazo — a mesma norma citada na seção anterior sobre
> transformação de maturidade."

por:

> "...e o NSFR (Net Stable Funding Ratio, instituído pela Resolução CMN nº 4.616/2017), que
> mede o financiamento estável de longo prazo — o indicador cujo objetivo declarado é
> exatamente mitigar excessos no processo de transformação de maturidade descrito na seção
> anterior."

(Preserva a ligação de sentido entre as duas seções — que é real e vale a pena manter — sem
afirmar que é "a mesma norma" quando na verdade é a mesma ideia regulatória descrita em dois
documentos diferentes.)

## 3. Compulsório: 21% recursos à vista, 20% recursos a prazo

**Veredito: ✅ Confirmado, com fonte lida diretamente (não só a citação repassada por
`03-pesquisa.md`).**

Baixei e li o PDF na íntegra: Banco Central do Brasil, Deban/Diban, "Recolhimento
Compulsório – Quadro Resumo", **atualizado em 24.7.2026**
(https://www.bcb.gov.br/content/estabilidadefinanceira/aliquotascompulsorios/Resumo_aliquotas_compulsorios.pdf).
Texto exato da tabela:
- **Recursos à Vista: alíquota 21%** — base normativa Resoluções BCB 189/2022, 227/2022,
  426/2024, 486/2025, 551/2026.
- **Recursos a Prazo: alíquota 20%** — base normativa Resoluções BCB 145/2021, 426/2024,
  551/2026; a rubrica contábil correspondente é explicitamente "4.1.5.10.00.00-3 DEPÓSITOS A
  PRAZO", que é onde o CDB entra no cálculo.

Documento atualizado há três semanas da data de publicação do post (2026-08-14) — vigência
atual confirmada. Busquei especificamente por alterações de alíquota entre a atualização do
documento e hoje (Resolução BCB 551/2026, de março/2026, e Resolução BCB 584/2026, de
7/8/2026): nenhuma altera a alíquota-base de 21%/20%; 551/2026 trata só de mecanismo de
dedução (antecipação ao FGC), 584/2026 é sobre prevenção a fraude, sem relação com
compulsório. Citação do draft está correta e é a afirmação mais solidamente verificada de
todo o post — fonte primária, lida na íntegra, atual.

## 4. FGC: R$ 250 mil por CPF/CNPJ por conglomerado, teto de R$ 1 milhão a cada 4 anos

**Veredito: ✅ Confirmado, fonte primária.**

Central de Atendimento FGC, "04. Qual o valor máximo garantido pelo FGC?"
(https://atendimento.fgc.org.br/hc/pt-br/articles/15806127807259, conteúdo recuperado via
busca — acesso direto retornou 403, mas o texto indexado é consistente, palavra por palavra,
com a segunda fonte primária abaixo) e FGC, FAQ em inglês (https://fgc.org.br/en/faq, acesso
2026-08-14, já citado em `03-pesquisa.md`): confirmam, em 2026, exatamente os dois valores do
draft — **R$ 250.000,00 por CPF ou CNPJ, por instituição associada ou conglomerado
financeiro**, e **teto de R$ 1 milhão a cada período de 4 anos**, contado da data da primeira
intervenção/liquidação. A reforma do CMN de abril de 2026 (cobertura noticiada por Agência
Brasil e Seu Dinheiro em `03-pesquisa.md`) mexeu em regras de captação e contribuição ao FGC,
não nesses dois valores de cobertura — confirmado que permanecem inalterados.

O item `[VERIFICAR: número exato da(s) Resolução(ões) CMN que instituíram o teto de R$ 1
milhão/4 anos]`, de `03-pesquisa.md`, não se aplica: o draft não cita número de resolução para
este ponto, só os valores — que estão confirmados por fonte primária. Nada a fazer.

## 5. Definição de CDB — Lei nº 4.728/1965 e CVM

**Veredito: ⚠️ Impreciso — nuance factual real, mas que espelha a própria fonte primária
oficial; sugestão de ajuste opcional, não obrigatório.**

A definição textual citada no draft ("título de crédito nominativo, transferível e de livre
negociação, representativo de promessa de pagamento do valor depositado junto ao emissor,
acrescido da remuneração combinada no momento da aplicação") confere, quase palavra por
palavra, com o Portal do Investidor
(https://www.gov.br/investidor/pt-br/investir/tipos-de-investimentos/titulos-bancarios/certificado-de-deposito-bancario-cdb,
acesso 2026-08-14) — confirmado por `03-pesquisa.md` e re-conferido aqui.

Achado adicional, não coberto pela pesquisa anterior: **o art. 30 da Lei nº 4.728/1965 — o
dispositivo que historicamente autorizava bancos a emitir CDB para depósitos com prazo
superior a 18 meses — foi expressamente revogado pelo art. 61, inciso I, da Lei nº 13.986, de
7 de abril de 2020** (a "Lei do Agro"). Texto lido diretamente na versão oficial do Congresso
(câmara.leg.br/legin, texto compilado da Lei 13.986/2020): "Art. 61. Ficam revogados: I - o
art. 30 da Lei nº 4.728, de 14 de julho de 1965". Desde então, a emissão de CDB é
regulamentada diretamente por resolução do CMN (Resolução CMN nº 4.812/2020, com alterações
posteriores), sob a competência genérica do CMN/Bacen prevista na Lei nº 4.595/1964 — não mais
sob o art. 30 especificamente.

Dito isso: a própria página oficial do Portal do Investidor (gov.br/investidor — iniciativa
que reúne CVM, Bacen e outros reguladores), consultada em 2026-08-14, **continua atribuindo a
instituição do CDB à Lei nº 4.728/1965**, sem menção à revogação de 2020. Ou seja, o draft
reproduz fielmente a própria simplificação que o regulador usa em material educacional oficial
— não é um erro inventado pelo texto, é a mesma simplificação da fonte primária citada.

**Recomendação:** manter como está é defensável (a fonte primária citada usa a mesma
formulação); se a consolidação preferir precisão máxima, a frase pode ganhar uma ressalva
opcional — algo como "com base histórica na Lei nº 4.728/1965 (art. 30, revogado em 2020;
hoje a emissão é regulamentada por resolução do CMN)" — mas isso é uma decisão editorial de
nível de detalhe, não uma obrigação de correção, já que o texto atual não afirma nada que a
fonte primária oficial não afirme também.

## 6. LCR — Resolução CMN nº 4.401/2015

**Veredito: ✅ Confirmado, fonte primária lida na íntegra.**

Baixei e li o texto consolidado: "RESOLUÇÃO Nº 4.401, DE 27 DE FEVEREIRO DE 2015 — Dispõe
sobre os limites mínimos do indicador Liquidez de Curto Prazo (LCR) e as condições para sua
observância" (https://normativos.bcb.gov.br/Lists/Normativos/Attachments/48574/Res_4401_v2_P.pdf,
versão consolidada). Em vigor desde 1º de outubro de 2015. O art. 3º (público-alvo) e o art.
4º (dispensa) foram alterados/revogados pela Resolução nº 4.616/2017 a partir de 1º/10/2018 —
mas a resolução em si **não foi revogada**, continua vigente, hoje aplicável às instituições
do Segmento 1 (S1). Número e ano da resolução citados no draft estão corretos.

## 7. NSFR — Resolução CMN nº 4.616/2017

**Veredito: ✅ Confirmado, fonte primária lida na íntegra.**

Texto lido integralmente: "RESOLUÇÃO Nº 4.616, DE 30 DE NOVEMBRO DE 2017 — Dispõe sobre o
limite mínimo do indicador Liquidez de Longo Prazo (NSFR) e as condições para seu cumprimento"
(https://normativos.bcb.gov.br/Lists/Normativos/Attachments/50474/Res_4616_v1_O.pdf).
Confirma: NSFR = razão entre ASF (Recursos Estáveis Disponíveis) e RSF (Recursos Estáveis
Requeridos); limite mínimo de 1 (cem por cento); aplicável a instituições do Segmento 1 (S1);
em vigor desde 1º de outubro de 2018. Arquivo é "versão 1, original" (v1_O) — sem indicação de
alteração ou revogação posterior. Número e ano corretos; resolução vigente.

## 8. `[VERIFICAR]` de `03-pesquisa.md`: percentual exato de ASF para depósito de varejo no NSFR

**Veredito: ✅ Resolvido com fonte primária — o `[VERIFICAR]` pode sair do texto, mas o valor
correto é uma faixa, não um número único.**

`03-pesquisa.md` não tinha conseguido ler a Circular BC nº 3.869/2017 diretamente (bloqueios
de acesso) e deixou o percentual como `[VERIFICAR]`, apoiado só em fontes secundárias (Dattos,
LegisWeb). Consegui uma fonte primária direta que **cita e aplica** os artigos da Circular:
Banco Central do Brasil, *Demonstrativo do Indicador de Liquidez de Longo Prazo (NSFR) —
Instruções de Preenchimento* (documento "DLP 2170"), lido na íntegra via
https://www.bcb.gov.br/content/estabilidadefinanceira/dlp-2170/DLP_2170_instrucoes_brasil_v201907.pdf
(62 páginas, texto extraído e conferido linha a linha). O documento tabula o fator de
ponderação (ASF) para "Captações de Varejo - Pessoas Físicas" cobertas por seguro-depósito
(FGC/FGCoop), incluindo explicitamente depósitos a prazo (onde o CDB se enquadra):

| Fator de ponderação (ASF) | Prazo efetivo de vencimento residual | Base normativa |
|---|---|---|
| 90% | captação considerada "menos estável" | Circular 3.869/2017, Art. 5º, inc. II |
| 95% | captação considerada "estável", < 1 ano | Circular 3.869/2017, Art. 5º, inc. I |
| 100% | qualquer captação de varejo, ≥ 1 ano | Circular 3.869/2017, Art. 4º, inc. II |

Ou seja: não existe um único "percentual exato" — o fator varia de **90% a 100%** conforme o
prazo da captação e a classificação de estabilidade (que depende de cobertura pelo FGC e
características da relação com o cliente, nos termos da Circular BC nº 3.749/2015, arts. 11-13,
referenciada pela própria Circular 3.869/2017).

**Correção exata proposta** — em "Por que o banco precisa emitir CDB" (§6), trocar:

> "...recebendo um fator de financiamento maior no cálculo do índice [VERIFICAR: percentual
> exato de ASF atribuído a depósito de varejo no NSFR, Circular BC nº 3.869/2017] — porque..."

por:

> "...recebendo um fator de financiamento entre 90% e 100% no cálculo do índice, conforme o
> prazo e a estabilidade da captação (Circular BC nº 3.869/2017, arts. 4º e 5º) — porque..."

`[FAIXA: percentual exato de ASF para depósito de varejo no NSFR → 90% a 100%, conforme prazo
e estabilidade da captação (Circular BC nº 3.869/2017, arts. 4º e 5º)]`

## 9. Exemplos numéricos — CDB pós-fixado (90/100/110% do CDI) e CDB prefixado (11% a.a.)

**Veredito: ✅ Confirmado — ambos claramente rotulados como ilustrativos, não como dado de
mercado atual.**

- "CDB não é CDI" (§5): "é comum, embora não universal, que o CDB pós-fixado seja atrelado a
  um percentual do CDI (90%, 100%, 110%, por exemplo)" — draft já seguiu a recomendação de
  `03-pesquisa.md` (item 4 do resumo de VERIFICAR) de remover a alegação de proporção de
  mercado ("a maior parte dos CDBs...") e manter só a descrição qualitativa com números como
  exemplo de faixa comum de mercado, não como estatística. Não há afirmação de percentual de
  mercado a verificar; a legenda do gráfico associado ("Gráfico: crescimento de capital de um
  CDB pós-fixado em diferentes percentuais do CDI (90%, 100%, 110%)...") também trata os três
  valores como cenários ilustrativos de comparação, não como dado histórico. Nada a corrigir.
- "Onde o CDB entra na sua carteira" (§7): "um CDB prefixado — a uma taxa combinada no
  momento da aplicação, como exemplo hipotético, 11% ao ano — trava a rentabilidade" — a
  expressão "como exemplo hipotético" já está no texto, explicitamente rotulando o número.
  Consistente com a nota de `03-pesquisa.md` (seção 6): taxas de CDB variam diariamente com
  Selic/CDI, então o número não deve ser lido como taxa de mercado atual — e o texto já evita
  essa leitura. Nada a corrigir (a revisão de linha, item 13, já sugeriu só reordenar a frase,
  sem mudar o conteúdo numérico).

## Resumo — itens que devem entrar como `[VERIFICAR: ...]` ou `[FAIXA: ...]` no texto final

Apenas um item sobrevive como pendência de precisão numérica; todos os demais dos seis
`[VERIFICAR]` originais de `03-pesquisa.md` **não se aplicam ao texto atual do draft**, porque
o draft já não faz as afirmações que motivavam aqueles VERIFICAR (proporção de CDB pós-fixado
em CDI, número da resolução do teto FGC, caso Banco Master, exemplo de funding gap de banco
nomeado, frase categórica sobre impossibilidade de uso do saldo em conta corrente — nenhum
desses está no draft na forma que exigiria a verificação).

1. `[FAIXA: percentual exato de ASF para depósito de varejo no NSFR → 90% a 100%, conforme
   prazo e estabilidade da captação (Circular BC nº 3.869/2017, arts. 4º e 5º; fonte: Bacen,
   *DLP 2170 — Instruções de Preenchimento*,
   https://www.bcb.gov.br/content/estabilidadefinanceira/dlp-2170/DLP_2170_instrucoes_brasil_v201907.pdf)]`

Nenhum `[VERIFICAR: ...]` novo precisa ser adicionado — os dois flags técnicos da revisão
(itens 8 e 11) foram resolvidos com correção de texto (não com placeholder), e o achado sobre
a revogação do art. 30 da Lei 4.728/1965 (item 5 acima) é uma nuance opcional de precisão, não
uma pendência de verificação: a informação está confirmada, só cabe decidir o nível de detalhe
desejado no texto final.

## Fontes primárias lidas na íntegra nesta etapa (novas, além das já listadas em `03-pesquisa.md`)

- Bacen, Deban/Diban, *Recolhimento Compulsório – Quadro Resumo*, atualizado 24.7.2026 — PDF
  baixado e lido por completo (2 páginas de tabela).
- Bacen, *Resolução CMN nº 4.401, de 27 de fevereiro de 2015* (texto consolidado, v2) — LCR.
- Bacen, *Resolução CMN nº 4.616, de 30 de novembro de 2017* (texto original, v1) — NSFR.
- Bacen, *Demonstrativo do Indicador de Liquidez de Longo Prazo (NSFR) — Instruções de
  Preenchimento* (DLP 2170), 62 páginas, lido por completo — fatores de ponderação ASF por
  tipo de captação de varejo.
- Câmara dos Deputados (legin), texto oficial da *Lei nº 13.986, de 7 de abril de 2020* — art.
  61, inciso I, revogação do art. 30 da Lei nº 4.728/1965.
- FGC, Central de Atendimento, "Qual o valor máximo garantido pelo FGC?" (triangulado com
  fgc.org.br/en/faq, já citado em `03-pesquisa.md`).
- B3, "Metodologia de Apuração da Taxa DI" (já citado em `03-pesquisa.md`, reconferido aqui
  para resolver a fricção conceitual do item 8 da revisão).

*Aplicação na consolidação (etapa 9), junto com `05-critica.md` e `06-revisao.md`, conforme
`CLAUDE.md`.*
