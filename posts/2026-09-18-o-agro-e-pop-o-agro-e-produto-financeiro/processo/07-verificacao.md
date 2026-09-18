# Etapa 7 — Verificação técnica

Post: `posts/2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro/`
Base: `processo/04-draft-v2.md` (conteúdo do post, excluída a seção de registro de
processo no fim) + leads de `processo/03-pesquisa.md`.

Cálculos de apoio rodados com `python3`, sem aproximação de cabeça. Buscas priorizaram
fonte primária (Bacen/CMN, Lei em texto compilado, periódico original) sobre agregador.

---

## 1. Gross-up linear (90% do CDI, IR 15%)

**✅ Confirmado.** `90 / 0,85 = 1,058823... = 105,88%`. Bate com o texto ("≈ 105,88% do CDI").

## 2. Tabela de break-even (CDI 14% a.a., LCA a 90% do CDI)

**✅ Confirmado — os cinco pares (regra linear / break-even real) batem exatamente com o
texto**, recalculados com $d = (1+0,14)^{1/252} - 1$ e a fórmula de break-even dada no
rascunho:

| Prazo | n (d.u.) | IR | Regra linear (texto) | Break-even (texto) |
|---|---|---|---|---|
| 6 meses | 126 | 20% | 112,5% | 111,7% |
| 1 ano | 252 | 17,5% | 109,1% | 107,8% |
| 2 anos | 504 | 15% | 105,9% | 103,9% |
| 3 anos | 756 | 15% | 105,9% | 103,0% |
| 5 anos | 1260 | 15% | 105,9% | 101,6% |

Nenhuma divergência.

## 3. Marcação a mercado (PU = VF/(1+y)^(du/252))

**✅ Confirmado.** Com VF=1.100, du=252: `1100/1,12 = 982,14`; `1100/1,14 = 964,91`. Bate
exatamente com o texto.

## 4. IR regressivo — limites de prazo (180/360/720 dias)

**✅ Confirmado.** Lei nº 11.033, de 21 de dezembro de 2004, art. 1º: até 180 dias 22,5%;
181–360 dias 20%; 361–720 dias 17,5%; acima de 720 dias 15%. O mapeamento do rascunho
(20%/17,5%/15%/15%/15% para 6 meses/1/2/3/5 anos) é consistente com a conversão usual de
dias úteis para dias corridos. Sem erro a corrigir.

## 5. Lei nº 11.076/2004 — criação da LCA

**✅ Confirmado.** Texto compilado:
`planalto.gov.br/CCIVIL_03/_Ato2004-2006/2004/Lei/L11076compilado.htm`. Institui CDA, WA,
CDCA, LCA e CRA.

## 6. Direcionamento de 60% em crédito rural (Resolução CMN nº 5.216/2025)

**✅ Confirmado**, via `Voto 60/2025–BCB` e `Voto 23/2025–CMN` (base técnica da resolução):
"proponho elevar o nível de direcionamento da LCA de 50% [...] para 60% [...] a partir de
1º de julho de 2025." Fonte: `normativos.bcb.gov.br/Votos/CMN/202523/Voto_do_CMN_23_2025.pdf`
(acesso 2026-09-18). Confirma os dois números do texto: 50%→60%, vigência 01/07/2025. Sai do
`[VERIFICAR]`.

## 7. Resolução CMN nº 5.315/2026 — Proagro e/ou socioambiental?

**⚠️ Correção de atribuição necessária.** A Resolução CMN nº 5.315, de 25/06/2026 (PDF oficial
do Bacen, acesso 2026-09-18), trata só de Proagro (comprovação de perdas, alíquotas do
adicional) — **não** de restrição socioambiental nem de LCA. Isso pertence à **Resolução CMN
nº 5.314/2026** (mesmo pacote, mesma data, vigência 01/07/2026), confirmada por três fontes
secundárias convergentes (Portal do Cooperativismo Financeiro, PSAA, Mundo Coop). O rascunho
atribuía os dois assuntos à 5.315 sozinha — corrigido no texto. A conclusão de fundo (nenhuma
das duas mexe no percentual de 60%) continua correta.

## 8. Prazo mínimo de LCA reduzido de 9 para 6 meses

**⚠️ Correção de data.** Resolução CMN nº 5.215, **de 22 de maio de 2025** (não 23), publicada
no DOU em **26/05/2025**, com vigência a partir da publicação. Fontes: IRIB e LegisWeb (acesso
2026-09-18). O número da resolução estava certo; a data, não. Corrigido no texto.

## 9. Teto do FGC

**✅ Confirmado.** R$ 250 mil por CPF/CNPJ por instituição, teto global de R$ 1 milhão a cada
quatro anos. Múltiplas fontes convergentes, mais o artigo de Caffagni (2021, ver item 14, já
citava os mesmos valores com fonte fgc.org.br — não mudou entre 2021 e 2026).

## 10. Teto global do FGCoop

**❓ Mantém `[VERIFICAR]`.** Norma primária do CMN/Bacen específica do FGCoop não localizada.
Fontes secundárias convergentes (Cresol, Sicredi, Sicoob, Unicred, XP, André Bona,
Investidor10) indicam que **não existe** teto global agregado equivalente ao do FGC — só o
limite individual de R$ 250 mil por instituição. Como é dado negativo (ausência de regra) sem
fonte primária, mantém-se `[VERIFICAR]` em vez de virar afirmação no corpo do texto.

## 11. Estoque de LCA em queda de ~4% no 1º semestre de 2026

**✅ Confirmado.** Bora Investir/B3, 27/07/2026: estoque de LCA em R$ 563 bilhões ao final de
junho de 2026, ante R$ 586 bilhões em junho de 2025 — queda de 4% na comparação anual. O
"+13%" do título da mesma matéria refere-se ao agregado de captação bancária, não à LCA
isolada — os dois números coexistem sem contradição. Sai do `[VERIFICAR]`.

## 12. Taxa média da LCA de 12 meses: 90,05% → 88,24% do CDI

**✅ Reconfirmado.** InfoMoney/Quantum Finance, 11/06/2026. Já estava confirmado pela etapa 3.

## 13. LCR e NSFR — siglas e definições

**⚠️ Correção de nomenclatura.** LCR confirmado como está ("Liquidez de Curto Prazo",
Circular BCB nº 3.749/2015). NSFR: o Bacen usa **"Índice de Liquidez de Longo Prazo (ILE)"**,
não "Financiamento Estável Líquido" (tradução literal não usada pelo regulador brasileiro) —
horizonte de um ano está correto. Fontes: documentos técnicos do Bacen sobre estabilidade
financeira (acesso 2026-09-18). Corrigido no texto.

## 14. Referências bibliográficas — Fabozzi e Caffagni

**Caffagni — ✅ localizado.** CAFFAGNI, Luiz Cláudio. "LCA: o título de crédito bancário para o
agro". *Agroanalysis* (FGV), out. 2021, p. 26–28.
`periodicos.fgv.br/agroanalysis/article/view/87891/82664` (acesso 2026-09-18). Sai do
`[VERIFICAR]` — referência atualizada com edição e páginas.

**Fabozzi — mantém `[VERIFICAR]`, mas por decisão editorial, não por falta de fonte.**
*Bond Markets, Analysis, and Strategies* tem duas edições correntes (10ª, 2021; 11ª, 2026),
ambas Frank J. Fabozzi e Francesco A. Fabozzi (coautoria, ausente na referência do rascunho).
Falta o autor escolher a edição — não é mais uma busca pendente.

---

## Lista consolidada de `[VERIFICAR]` remanescentes no texto final

```
[VERIFICAR: teto global agregado do FGCoop — fontes secundárias convergentes indicam que não
existe teto global equivalente ao R$ 1 milhão/4 anos do FGC, mas a norma primária do CMN/Bacen
que rege o FGCoop não foi localizada diretamente]

[VERIFICAR: edição de Bond Markets, Analysis, and Strategies a citar — 10ª ed. (Fabozzi &
Fabozzi, MIT Press, 2021) ou 11ª ed. (mesmos autores, MIT Press, 2026); referência também
precisa incluir Francesco A. Fabozzi como coautor]
```

Nenhum `[FAIXA]` nesta rodada — os itens corrigidos (7, 8, 13) foram de atribuição normativa e
nomenclatura, não de intervalo de valores.

## Itens que saem do `[VERIFICAR]` do rascunho (confirmados ou corrigidos nesta etapa)

- Item 6 (direcionamento 60%): confirmado, remover `[VERIFICAR]`.
- Item 7 (Res. 5.315/2026): corrigida a atribuição (5.314 trata de socioambiental/LCA, 5.315
  só de Proagro) — remover `[VERIFICAR]`, manter a correção no texto.
- Item 8 (prazo mínimo, Res. 5.215/2025): corrigida a data (22/05, não 23/05; vigência
  26/05/2025) — remover `[VERIFICAR]`.
- Item 14, Caffagni: referência completa — remover `[VERIFICAR]` relativo a ele.
