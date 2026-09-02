# Pesquisa — Quando os Modelos se Rebelam (rodada 4)

Produzido pelo agente `pesquisador-editorial`. Organizado pelos quatro itens do brief; cada um
indica que seção de `02-estrutura.md` alimenta. Nenhum número aqui é veredito fechado — isso é
trabalho da etapa 7 (verificação técnica). Regra do repositório: "evidência ou silêncio"
(`CLAUDE.md`) — nenhum item foi forçado onde não havia achado de valor.

---

## Item 1 — Contraponto ao par Derman/Lakatos (seção 1)

**O contraponto genuíno já está bem coberto no próprio rascunho.** A seção 1 já cita a visão
semântica das teorias (Suppes, van Fraassen, Giere) como discordância real de Derman, e a
seção 5 já distingue ajuste "saudável" de "degenerado" pelo critério lakatosiano correto: se o
ajuste gera previsões novas, não é evasão, é ciência normal. Isso já é, na prática, a defesa
contra a leitura de que "cinturão protetor = má-fé".

Confirmação de que a visão semântica é posição filosófica real, não invenção do autor:
Stanford Encyclopedia of Philosophy, "The Structure of Scientific Theories"
([plato.stanford.edu/entries/structure-scientific-theories](https://plato.stanford.edu/entries/structure-scientific-theories/)).

Material extra, opcional, não essencial: a resenha de M.A.H. Dempster sobre *Models. Behaving.
Badly.* (Derman) em *Quantitative Finance*, vol. 12, n. 4 (2012), pp. 509-511, DOI
[10.1080/14697688.2012.662596](https://www.tandfonline.com/doi/full/10.1080/14697688.2012.662596),
levanta o ponto do flogisto — a física também teve "teorias" que depois viraram aproximação
histórica descartada, sugerindo que a fronteira teoria/modelo é grau, não categoria, mesmo
dentro da física. **Não lido na íntegra** (paywall) — conteúdo vem de resumo de busca, não
citar como fato fechado sem confirmar o texto original. Outra resenha, de Martin Fridson, CFA,
em *Financial Analysts Journal*, vol. 6, n. 1 (2011),
[DOI 10.2469/br.v6.n1.13](https://rpc.cfainstitute.org/research/financial-analysts-journal/2011/models-behaving-badly)
(lida integralmente), aponta uma inconsistência interna do livro de Derman: ele diz que "o
mercado às vezes está errado sobre o valor", mas também que "não há nada de absoluto sobre o
valor de um ativo" — nota de rodapé possível, não pilar.

**Veredito:** não força seção nova. O material extra só entra se a etapa 4 quiser uma frase a
mais; não é obrigatório.

---

## Item 2 — A nota brasileira do target forward de 2008 (seção 3) — achado principal desta rodada

Três fontes distintas, cada uma medindo algo diferente — e a origem provável do número
"US$ 35 bilhões" do rascunho, que não é nenhuma das duas do BIS:

**A. BIS Quarterly Review, junho de 2009.** Alejandro Jara, Ramon Moreno, Camilo E. Tovar,
"The global crisis and Latin America: financial impact and policy responses", Box 1, p. 55 —
PDF lido diretamente:
[bis.org/publ/qtrpdf/r_qt0906f.pdf](https://www.bis.org/publ/qtrpdf/r_qt0906f.pdf). Citação
textual: *"In Mexico, derivatives losses reached $4 billion in the fourth quarter of 2008,
while in Brazil, where official figures have not been released yet, losses are expected to be
as high as $25 billion."* Métrica: **perda** (não exposição, não nocional); os próprios
autores marcam como estimativa não-oficial.

**B. BIS Papers No 54.** Mário Mesquita e Mário Torós, "Brazil and the 2008 panic", dezembro de
2010 — PDF: [bis.org/publ/bppdf/bispap54.pdf](https://www.bis.org/publ/bppdf/bispap54.pdf).
**Não lido diretamente** (PDF sem texto extraível pela ferramenta usada) — dado vem de resumo
de busca sobre o mesmo documento, precisa confirmação antes de citar como fato fechado. Segundo
o resumo: exposição de clientes registrada na CETIP chegava a "close to $37 billion (delta)"
no fim de setembro de 2008. Métrica: **exposição delta**, não perda realizada — dado
administrativo de câmara de compensação, citado por autor ligado ao Banco Central (Mesquita
foi diretor do BCB), em publicação do BIS.

**C. Origem provável do "US$ 35 bilhões" do rascunho.** Fernando Nogueira da Costa (professor
titular, FEE-Unicamp), "Anatomia da Crise da Aracruz em 2008", blog *Cidadania & Cultura*,
21/12/2012 — lido integralmente:
[fernandonogueiracosta.wordpress.com/2012/12/21/anatomia-da-crise-da-aracruz-em-2008](https://fernandonogueiracosta.wordpress.com/2012/12/21/anatomia-da-crise-da-aracruz-em-2008/).
Citação quase verbatim ao rascunho do autor: *"Estima-se que o montante total dessas operações
tenha alcançado US$ 35 bilhões."* **Isto não é fonte primária** — é blog, sem nenhuma
atribuição de origem para o número. O mesmo texto também registra que o mesmo tipo de contrato
tóxico foi vendido em larga escala fora do Brasil (Índia, México, Coreia do Sul) — o que deixa
ambíguo se "US$ 35 bi" seria estatística fechada do Brasil, como o rascunho assume.

**Recomendação para a etapa 7, em ordem de preferência:**
1. Trocar por "~US$ 37 bilhões (exposição delta registrada na CETIP, fim de setembro de 2008)",
   citando Mesquita & Torós/BIS Papers No 54 — exige antes confirmar a leitura do PDF (item B
   ainda não verificado por leitura direta).
2. Trocar por "estima-se que as perdas tenham chegado a US$ 25 bilhões", citando o BIS
   Quarterly Review de junho de 2009 (fonte lida diretamente, sólida) — mas muda o sentido da
   frase (perda ≠ volume de operações), exige reescrita, não só troca de número.
3. Marcar `[VERIFICAR]` e deixar para o autor — nenhuma fonte confiável sustenta exatamente
   "US$ 35 bi" como volume/exposição do Brasil especificamente.

**Aracruz e Sadia, checados de passagem — resultado bom, com um alerta:**
- Aracruz, US$ 2,13 bi: bem sustentado — Bloomberg, "Aracruz Fails to Settle $2.13 Billion
  Derivative Loss", 12/12/2008
  ([bloomberg.com/news/articles/2008-12-12/aracruz-banks-fail-to-agree-213-billion-derivatives-loss](https://www.bloomberg.com/news/articles/2008-12-12/aracruz-banks-fail-to-agree-213-billion-derivatives-loss));
  e *International Journal of Auditing Technology*, vol. 3, n. 3 (2017), pp. 217-230,
  [DOI 10.1504/IJAUDIT.2017.086756](https://www.inderscienceonline.com/doi/10.1504/IJAUDIT.2017.086756).
  É a perda total comunicada ao desmontar as posições em 03/11/2008 — bate com o rascunho.
  **Alerta:** o artigo da RACEF, já citado nas "Fontes e leituras" do próprio rascunho, usa
  "R$ 2,5 bilhões" para a Aracruz — não é conversão direta de US$ 2,13 bi no câmbio de
  novembro/2008 (daria ~US$ 1,0-1,1 bi). Provavelmente mede um corte temporal diferente
  (posição de setembro, não o desmonte de novembro) — a etapa 7 deveria checar se as duas
  fontes já citadas no rascunho não estão medindo momentos diferentes sem dizer isso.
- Sadia, R$ 2,55 bi: bem sustentado — mesmo blog do item C confirma, com detalhe adicional:
  despesa financeira total de R$ 3,892 bi no ano, da qual R$ 2,55 bi vieram de perdas com os
  contratos ("sell target forward"), sendo R$ 705 milhões com impacto de caixa.

---

## Item 3 — Caso adicional pós-2015 (opcional, para seção 3 ou nota extra)

**Candidato forte: LME nickel, março de 2022.** Preço subiu de US$ 27.080/t para
US$ 101.365/t em três dias (mais de 270% em 72 horas), forçando a LME a suspender o mercado e
cancelar cerca de 9.000 negociações. Causa raiz: os modelos de margem da bolsa pressupunham
liquidez e continuidade de preço suficientes para chamadas de margem incrementais — quando o
preço saltou sem histórico, o sistema de margem teria exigido US$ 19,75 bilhões de 28
bancos/corretoras num único dia, mais de dez vezes o recorde diário anterior. É a mesma
hipótese de continuidade (Black–Scholes) e a mesma hipótese de liquidez (LTCM) quebrando ao
mesmo tempo, na estrutura de margem de uma bolsa de metais. Fonte: Oliver Wyman, *Independent
Review of Events in the Nickel Market in March 2022 — Final Report*, encomendado pela própria
LME, janeiro de 2023 — PDF não lido diretamente (dado de resumo de busca, confirmar antes de
citar número exato):
[lme.com/.../Independent-Review-of-Events-in-the-Nickel-Market-in-March-2022...pdf](https://www.lme.com/-/media/Files/Trading/New-initiatives/Nickel-independent-review/Independent-Review-of-Events-in-the-Nickel-Market-in-March-2022---Final-Report.pdf).
Complementar: Bloomberg, "LME Halts Nickel Trading After Unprecedented 250% Spike",
08/03/2022. **Ressalva editorial:** a LME cancelou negociações retroativamente — intervenção
sem paralelo nos outros casos do post; se usado, nomear essa diferença.

**Candidato descartado: Archegos, março de 2021.** Superficialmente atraente (perdas > US$ 10
bi entre bancos), mas a própria investigação interna do Credit Suisse (Special Committee,
conduzido por Paul, Weiss) concluiu que a falha "not due to flaws in risk management
frameworks, risk reporting or systems" — foi governança e cultura (ignorar alertas que o
modelo já dava), não modelo calibrado num regime que deixou de valer. Não se encaixa na tese
deste post especificamente.

**Recomendação:** o nickel da LME é candidato editorial válido para uma menção curta, se a
etapa 4 quiser; não é obrigatório, o post já tem quatro casos fortes (moeda de Kempthorne,
radar, Black–Scholes/18-05, LTCM) mais o London Whale.

---

## Item 4 — Financial Modelers' Manifesto (2009): checagem de fidelidade

Texto original lido diretamente: Emanuel Derman & Paul Wilmott, *The Financial Modelers'
Manifesto*, 7 de janeiro de 2009 — PDF:
[emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf](https://emanuelderman.com/wp-content/uploads/2009/01/fmm.pdf).
A seção final, "The Modelers' Hippocratic Oath", tem exatamente cinco compromissos, e a
paráfrase do rascunho bate em sentido e ordem com todos os cinco, sem distorção. Único ponto
menor: os cinco compromissos vêm tecnicamente do "Modelers' Hippocratic Oath", uma subseção do
manifesto — não do manifesto inteiro (que tem prefácio e corpo argumentativo antes do
juramento). Simplificação editorial razoável, não erro; a etapa 7 pode ajustar o nome exato se
quiser precisão cirúrgica.

**Veredito: confirmado, sem correção necessária.**
