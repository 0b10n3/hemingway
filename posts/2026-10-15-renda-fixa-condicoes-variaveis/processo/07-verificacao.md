# Etapa 7 — Verificação técnica

Executor: agente `verificador-tecnico`. Objeto: corpo de `processo/04-draft-v2.md`. Acesso a
todas as fontes em 2026-10-15. Leis conferidas no texto compilado do Planalto (6.404, 11.101,
14.195, 11.053, 12.431, 14.801, 11.033). Ponto de partida: apêndice do autor, `03-pesquisa.md`
e os itens que `05-critica.md` mandou para esta etapa (C-02c, C-05, C-14).

Código e saída das contas: `_revisoes/2026-10-15_2026-10-15-renda-fixa-condicoes-variaveis_calculo.md`
(reexecutado pelo orquestrador; mesma saída).

## Resumo

- **Contas:** as 7 do apêndice e todos os números do corpo conferem. Nenhuma divergência.
- **Base legal:** tudo confere, inclusive a nova frase de "O voto" ("garantia real,
  quirografário, subordinado" é exatamente o rol vigente do art. 163, § 1º, já que os incisos
  IV e V do art. 83 foram revogados).
- **Fatos:** **1 erro factual** (data do parecer do MP, K-01, que cobre também o C-14), **1
  definição técnica imprecisa** (VNA na fórmula do PU, K-02), **3 ajustes baixos** (K-03 FIDC,
  K-04 Americanas, K-05 STJ), **1 `[VERIFICAR]` novo** (Itaú Asset, K-06) e **1 de
  bibliografia** (capítulos do Varanda Neto), além do Eizirik.
- **C-05:** "os gatilhos perderam importância no dia do pedido" confere para a RE: art. 163,
  § 8º, estende a suspensão do art. 6º desde o pedido. Ponte opcional (K-07).
- **C-02c:** deixou de existir no v2 (a glosa sobre limitadas saiu).
- **Dois lados do balcão** e **regra de referências** (4 itens, 2 livros, sem lei): conferem.
- Nenhum `[FAIXA]`.

## 1. Contas

| # | Afirmação | Recálculo | Veredito |
|---|---|---|---|
| 1.1 | Tabela % do CDI → CDI + spread | 12 células batem | Confere |
| 1.2 | 110% = CDI + 1,29% → CDI + 0,96% | 1,2874% / 0,9575% | Confere |
| 1.3 | CDI + 1,5% ≈ 111,6% e 115,6% do CDI | 111,639% / 115,625% | Confere |
| 1.4 | 3 anos a 110% perde ~1% se CDI esperado → 10% | PU 99,026% (fluxo explícito idem) | Confere |
| 1.5 | PU 97,6 / 92,9 / 86,4 / 80,5 | 97,573 / 92,927 / 86,447 / 80,501 | Confere |
| 1.6 | Duration de spread ~5; 1 p.p. ≈ 5% | 4,926; exato −4,78% | Confere |
| 1.7 | 0,10 ponto ≈ 0,5% | 0,500% linear; 0,491% exato | Confere |
| 1.8 | Lei 14.801: 66,00 → 55,80; 9,24% → 7,81% | idem | Confere |

Fórmula simbólica do PU: a álgebra confere; o problema é o denominador (K-02).

## 2. Base legal

| # | Dispositivo | Veredito |
|---|---|---|
| 2.1–2.5 | Lei 6.404, arts. 52, 56, 57, 58 (caput, §§ 1º e 4º), 61 § 1º | Confere |
| 2.6 | art. 68 (comunhão); "uma instituição" é simplificação aceitável (art. 66, § 1º admite pessoa natural) | Confere |
| 2.7 | art. 68, § 3º, a) | Confere |
| 2.8–2.9 | art. 71 caput, §§ 5º e 8º (Lei 14.711; § 10 define "dispersa") | Confere |
| 2.10–2.11 | Lei 11.101, arts. 41 e 49 § 3º | Confere |
| 2.12–2.13 | art. 83, ordem e § 6º (inciso IX vem depois dos subordinados; "depois dela, só os acionistas" se sustenta pelo art. 58 § 4º LSA) | Confere |
| 2.14 | Extraconcursais / dinheiro novo (art. 84, I-B) | Confere |
| 2.15 | art. 163 caput: 3/5 → mais da metade (Lei 14.112) | Confere |
| 2.16 | Nova frase "espécie de crédito da Lei de Falências" | Confere |
| 2.17 | "é o devedor quem escolhe quais créditos entram" (art. 163 §§ 1º–2º; art. 161 § 1º) | Confere |
| 2.18 | C-05: art. 163, § 8º (suspensão desde o pedido na RE); GPA pediu com 46% de adesão | Confere |
| 2.19 | "a doutrina e o STJ" (Eizirik 2015 pp. 479–481; Borba & Borba 2015 p. 107; REsp 303.825/SP, 4ª T., j. 19/6/2001, via RSDE nº 22) | Confere no mérito; precedente único de turma (K-05) |
| 2.20 | Lei 14.195, arts. 45–47 ("termo de emissão" no art. 47 § 2º) | Confere |
| 2.21 | Lei 11.053, art. 5º | Confere |
| 2.22 | Lei 12.431, art. 2º, I (0% PF) | Confere |
| 2.23 | Lei 14.801, arts. 2º, 3º § 2º, 6º I e II (30% dos juros) | Confere |
| 2.24 | IN RFB 2.235/2024 (Anbima e Legisweb concordantes; DOU não aberto) | Confere |
| 2.25 | IR PF 22,5%–15% (Lei 11.033, art. 1º) | Confere |
| 2.26 | DREI, Ofício Circular SEI nº 92/2026/MEMP, 9/2/2026 (Migalhas, Baptista Luz) | Confere |
| 2.27 | Resolução CVM 179/2023 (política da Genial; XP deu 403) | Confere |

## 3. Fatos

| # | Afirmação | Veredito |
|---|---|---|
| 3.1 | Homologação em 7/10, pela juíza (Capital Aberto, 7/10) | Confere |
| 3.2–3.4 | R$ 4,57 bi quirografários; 57,49%; signatários | Confere |
| 3.5 | "a Itaú Asset, que havia coordenado a 20ª emissão" — literal na fonte (Capital Aberto, 25/5), mas coordenar oferta é papel de banco; fato relevante do GPA (8/11/2024) não nomeia; uma fonte secundária aponta o Itaú BBA | **[VERIFICAR]** (K-06) |
| 3.6 | 18ª, 19ª e CRIs, R$ 1,56 bi; petição de maio | Confere (dado de maio) |
| 3.7–3.12 | 88,4% na A; R$ 200 mi; 63–69%; 30%/2036; R$ 15 mi; 2,1→6,4 anos; CDI+1,8%→+0,5%; R$ 4,6 bi → ~R$ 2 bi | Confere |
| 3.13–3.14 | Fornecedores e funcionários fora; 46% de adesão em março | Confere |
| 3.15 | **MP "em setembro"** — o parecer contra a homologação é de **28/8/2026** (Times Brasil); retificado em 30/9 (Gironews, 1/10), passando a defender a homologação com quatro ressalvas, adotadas pela juíza (Capital Aberto, 7/10). As ressalvas não tratam da composição do grupo: o MP abandonou essa objeção. | **Corrigir** (K-01) |
| 3.16 | "Segundo a juíza, nenhuma regra foi quebrada" | Confere (paráfrase) |
| 3.17–3.19 | Chilli Beans (NeoFeed 30/9; Economic News 9/10; Gazeta Mercantil 31/8) | Confere |
| 3.20 | Americanas: vencimento antecipado **automático**, comunicado em 20/1/2023, um dia após o deferimento (InfoMoney) | Confere com imprecisão baixa (K-04) |
| 3.21 | Anbima jan–nov/2025: R$ 433 bi; R$ 150,7 bi (> R$ 135,1 bi de 2024); R$ 870,5 bi | Confere |
| 3.22 | Prazo médio 9,9 anos (Correio da Manhã citando Anbima) | Confere (secundária) |
| 3.23 | 479 DI+ × 63 % DI (Relatório Anbima 7/3/2025) | Confere |
| 3.24 | Meta Selic 13,75% desde 17/9/2026 (SGS 432); CDI 13,65% (SGS 4389) | Confere |
| 3.25 | FIDCs R$ 14,5 bi, +146,3% — "movimentaram em emissões", não "captaram" | Confere no número (K-03) |
| 3.26–3.28 | CMN 2024; Raízen; promessa do post do CRA | Confere |
| 3.29 | ANBIMA Data com Z-spread | Confere |
| 3.30–3.31 | Smith & Warner 1979; Anderson 1999 (amostra 1989–1993) | Confere |
| 3.32 | Varanda Neto, Santos e Mello (Saint Paul, 2019, ISBN 978-85-8004-149-1); caps. 8 e 19 sem sumário online | Livro confere; **capítulos [VERIFICAR]** |
| 3.33 | Eizirik, 2ª ed. 2015; existe 3ª edição da coleção | `[VERIFICAR]` já presente, manter |

## 4. Aderência ao mercado brasileiro (15/10/2026)

CDI 13,65%/Selic 13,75%; linhas de 15%, 10% e 8%; 110% do CDI e CDI + 1,5% (GPA pagava DI +
1,55% a 2,50%); spreads de 2% a 6% (Vert a DI + 3,9%); IPCA + 7%; 14% a.a. e 34% de IRPJ +
CSLL; durations de 3 a 5 anos: tudo compatível.

## Correções propostas

**K-01 (corrigir; erro factual; cobre C-14).** "O voto".
- Original: `ao recomendar, em setembro, que o plano não fosse homologado`
- Mínima: `ao recomendar, no fim de agosto, que o plano não fosse homologado`
- Recomendada (data + retificação): acrescentar ao fim do parágrafo da recomendação: `Um mês depois, o MP retificou o parecer e passou a defender a homologação, com ressalvas que a juíza adotou.`
- Escolha entre as duas versões cabe ao autor (ele cortou "O juiz homologou" antes).

**K-02 (corrigir; definição técnica).** "Pós-fixado também oscila".
- Fórmula: `\frac{PU}{VNA}` → `\frac{PU}{PU_{\text{par}}}`
- Glosa: `em que *VNA* é o valor nominal atualizado e *du* o número de dias úteis até o vencimento.` → `em que *PU* é o preço do papel, *PU par* é o valor do papel na curva (o valor nominal mais os juros acumulados desde o último pagamento) e *du* o número de dias úteis até o vencimento.`
- Base: Metodologias ANBIMA, "Debêntures remuneradas pelo DI" (VNA = VNE nas DI; PU PAR = VNE + remuneração acumulada). Resolve também C-19 e substitui a A-38 da etapa 6.

**K-03 (corrigir; baixa).** Fechamento.
- `em agosto, os FIDCs captaram R$ 14,5 bilhões` → `em agosto, as ofertas de FIDCs somaram R$ 14,5 bilhões`

**K-04 (corrigir; baixa).** "Os gatilhos".
- `os agentes fiduciários das debêntures da Americanas declararam o vencimento antecipado logo depois do deferimento da recuperação judicial.` → `os agentes fiduciários das debêntures da Americanas comunicaram o vencimento antecipado automático no dia seguinte ao deferimento da recuperação judicial.`

**K-05 (opcional; baixa).** "O voto".
- `a doutrina e o STJ entendem que a maioria da comunhão não pode cortá-lo.` → `a doutrina e o STJ, num julgado de 2001, entendem que a maioria da comunhão não pode cortá-lo.`

**K-06 (`[VERIFICAR]`).** Abertura.
- `e a Itaú Asset, que havia coordenado a 20ª emissão de debêntures da companhia.` → marcar `[VERIFICAR: quem coordenou a 20ª emissão do GPA; a fonte (Capital Aberto, 25/5/2026) atribui à Itaú Asset, mas coordenação de oferta é papel de banco, e uma fonte secundária indica o Itaú BBA]`. Saída sem perda: `e a Itaú Asset Management.`

**K-07 (opcional; C-05).** "Os gatilhos".
- Depois de `e a aceleração vira formalidade.` acrescentar: `Na extrajudicial, a lei estende a mesma suspensão, desde o pedido, aos créditos que o plano abrange (art. 163, § 8º).`

## Pendências `[VERIFICAR]` para a consolidação

1. Coordenador da 20ª emissão do GPA (K-06).
2. Eizirik: edição vigente e paginação (já no texto).
3. Varanda Neto, Santos e Mello: capítulos 8 e 19 (cai se o autor confirmar no exemplar).

## Fontes principais (acesso em 2026-10-15)

- Planalto (leis compiladas): 6.404, 11.101, 14.195, 11.053, 12.431, 14.801, 11.033.
- BCB/SGS 432, 4389, 1178.
- Anbima: Metodologias de precificação; Relatório de Precificação 7/3/2025; volumes jan–nov/2025; FIDCs agosto/2026; Z-spread; IN RFB 2.235.
- GPA: Capital Aberto (25/5, 2/7, 25/9, 7/10/2026); Times Brasil (28/8 e 7/10/2026, [parecer do MP](https://timesbrasil.com.br/empresas-e-negocios/grupo-pao-de-acucar-ministerio-publico-se-manifesta-contra-homologacao-do-plano-de-recuperacao-extrajudicial/)); [Gironews, 1/10/2026](https://gironews.com/supermercado/mp-sp-muda-posicao-e-passa-a-defender-plano-extrajudicial-do-gpa/); SuperVarejo (12/3 e 8/10/2026); fato relevante de 8/11/2024.
- Chilli Beans: NeoFeed 30/9; Economic News 9/10; Gazeta Mercantil 31/8. Americanas: InfoMoney 20/1/2023.
- DREI: Migalhas 13/2/2026; Baptista Luz 23/4/2026.
- Doutrina/STJ: RSDE nº 22. Bibliografia: RePEc (Smith & Warner; Anderson); Saint Paul; ReP USP; Migalhas (Eizirik).
- Não abertos: política da XP (403), ofício do DREI no okai.com.br (403), acórdão do REsp 303.825 no site do STJ.
