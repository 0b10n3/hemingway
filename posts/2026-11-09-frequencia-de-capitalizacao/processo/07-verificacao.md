# Etapa 7 — Verificação técnica

Executor: subagente `verificador-tecnico`. Texto conferido: corpo de `processo/04-draft-v2.md`.
Fontes acessadas em 2026-11-09. Os vereditos de `03-pesquisa.md` foram reaproveitados. Registro
do cálculo: `_revisoes/2026-11-09_2026-11-09-frequencia-de-capitalizacao_calculo.md`.

**Placar:** 2 divergências numéricas bloqueantes (de arredondamento), 7 imprecisões, 2
`[VERIFICAR]`, nenhum `[FAIXA]`. O resto confere.

## Bloqueantes

**B1.** "13,10% + 13,10% = 26,21%, e e elevado a 0,2621 dá 1,2996" (Mesa de opções, item 1). Com o
expoente arredondado escrito, e^0,2621 = 1,29966, que dá 1,2997. Além disso, 13,10 + 13,10 = 26,20,
não 26,21. O valor exato é 2 × ln 1,14 = 0,262057, e e^0,262057 = 1,2996 = 1,14². → "13,103% +
13,103% = 26,21%, e e elevado a 0,26206 dá 1,2996".

**B2.** "quem vende a opção de venda recebe R$ 0,26 a menos" (Onde mora o erro). Sem arredondar, as
puts valem 4,441555 e 4,176477, e a diferença é 0,2651, que dá R$ 0,27. O 0,26 só sai da subtração
dos preços já arredondados. A call confere: 0,5184, ou R$ 0,52. → "cerca de R$ 0,27 a menos".

## Números, item a item

| # | Afirmação | Recálculo | Veredito |
|---|---|---|---|
| 1 | 1,01^12 = 1,1268 | 1,126825 | Confere |
| 2 | Bernoulli 2 / 2,25 / 2,44 / 2,61 / 2,69 / 2,7146 | 2 / 2,25 / 2,441406 / 2,613035 / 2,692597 / 2,714567 | Confere |
| 3 | Anual→semestral ganha 0,25 | 0,25 | Confere |
| 4 | Diário→horário < 4 milésimos | 0,003559 | Confere |
| 5 | Cota do binômio (3º termo em diante < 1; total < 3) | 1/k! ≤ 1/2^(k−1) para k ≥ 2 | Confere (alerta do briefing resolvido) |
| 6 | Curva do graf-01 termina em 2,718 | 2,71828 | Confere |
| 7 | (1+j/m)^m = [(1+1/n)^n]^j | identidade | Confere |
| 8 | e^0,14 = 1,1503 | 1,150274 | Confere |
| 9 | 15,03% "apareceu duas vezes no texto anterior" | `a-barriga-da-curva/post.md`, linhas 73 e 204 | Confere |
| 10 | ln 1,14 = 13,10% | 0,131028 | Confere |
| 11 | Nominais 13,542 / 13,175 / 13,106 / 13,103 | 13,5416 / 13,1746 / 13,1062 / 13,1028 | Confere |
| 12 | graf-02: 14,49 / 14,93 / 15,02 / 15,03 | 14,4900 / 14,9342 / 15,0229 (252) ou 15,0243 (365) / 15,0274 | Confere |
| 13 | R$ 9.342,03 / 887,05 / 44,72 | Batem com diária = 252 vezes. Com 365: 900,89 / 30,88 | Confere (ver I1) |
| 14 | Dobrar m corta pela metade a distância (a 14%) | razões 1,91 / 1,95 / 1,98 / 1,99 … 2,00 | Confere a 14% (ver I4) |
| 15 | 1,14^(1/252) − 1 = 0,05201% | 0,0520089% | Confere |
| 16 | 0,14/252 = 0,05556% → 15,02% | 0,0555556% → 15,0229% | Confere |
| 17 | 26,21% e 1,2996 | ver B1 | **Corrigir** |
| 18 | Dois anos: 29,96% | 29,96% | Confere |
| 19 | Termo 114,00 × 115,03 | 114,00 / 115,027 | Confere |
| 20 | Call 16,72 × 17,24, +3,1% | 16,7223 / 17,2407, +3,100% | Confere |
| 21 | Put 4,18 × 4,44, −6,0% | 4,1765 / 4,4416, −5,97% | Confere |
| 22 | Diferenças R$ 0,52 / R$ 0,26 | 0,5184 / **0,2651** | Put: **corrigir** (B2) |
| 23 | "Errar a etiqueta vale 103" pb | e^0,14 − 1,14 = 102,74 pb | Confere (na etiqueta r são 90 pb; o texto mede na efetiva) |
| 24 | Diária→contínua < 0,5 pb | 0,447 (252) / 0,309 (365) | Confere |
| 25 | 68 pb | 68,25 | Confere |
| 26 | "Da ordem de um ponto percentual" | 103 pb | Confere |
| 27 | Cartão 451,7% a.a. (set/2026), ~15,3% a.m. | **BCB SGS 22022:** 01/09/2026 = 451,71% a.a.; **SGS 25477:** 15,29% a.m. | Confere em fonte primária |
| 28 | Cartão: diária 522,6%, contínua 526,7%, > 4 pp | Diária (252) 522,57%; contínua 526,73%; 4,15 pp. Com 365: 523,85% e 2,88 pp | Confere com 252 (ver I2) |
| 29 | LTN 1 ano: 0,5 pb ≈ R$ 0,04 | R$ 0,03847 | Confere |
| 30 | TRUNCAR, caso do Tesouro (14,36%, 532 du) | 753,315323 | Confere com o documento |
| 31 | Poupança 6,17% / 5,99% | 6,1678% / 5,9850% | Confere |

## Imprecisões

- **I1.** O valor de R$ 887,05 só sai com "diária" igual a 252 vezes, e o parágrafo não diz isso. → "Da mensal para a diária (252 dias úteis), mais R$ 887,05."
- **I2.** No cartão, a conta usa 252 capitalizações. O crédito ao consumidor corre em dias corridos (CET, base 365). Com 365: 523,9% / 526,7% / quase 3 pp. → (A) 365 dias com "quase três pontos"; ou (B) manter os números e escrever "nos 252 dias úteis do ano".
- **I3.** "A distância até o teto cresce com o quadrado da taxa" fica curto: a distância ≈ e^j·j²/(2m) cresce mais rápido que o quadrado. → "cresce mais rápido que o quadrado da taxa".
- **I4.** A regra de bolso da Prateleira é apresentada como geral. A taxas de cartão, as razões entre distâncias sucessivas são 1,33 / 1,49 / 1,66 / 1,85, e só chegam perto de 2 a partir de m ≈ 50. → acrescentar "enquanto a taxa de cada subperíodo for pequena".
- **I5.** Em "Para tirar de uma curva a taxa a termo, basta subtrair", quem se subtrai são os expoentes r × T, não as taxas anuais. → "basta subtrair os expoentes (r × T) de um prazo e do outro".
- **I6.** "Bernoulli provou em 1683 que ela tem topo": em 1683 ele estudou o problema, e a prova saiu impressa em 1690 (*Acta Eruditorum*). → "Bernoulli provou que ela tem topo", sem ano.
- **I7.** O manual chama DUₙ de "número de dias de saque". "Dias úteis" é uma simplificação aceitável, e a mudança é opcional.

## Fatos, citações e normas

| Item | Fonte | Veredito |
|---|---|---|
| Bernoulli, suíço, 1683, binômio, entre 2 e 3 | MacTutor | Confere (ver I6) |
| "100% ao ano" | MacTutor: limite de (1+1/n)^n | Confere como reconstrução |
| Euler, carta de 1731 | MacTutor; Fuss (1843), carta XV, 25/11/1731 | Confere |
| B3: "conversão exponencial 252"; capitalização em dias úteis | B3, Programa de Treinamento DI | Confere |
| Manual de opções: "taxa de juro exponencial, em regime contínuo e base anual" | Manual v27, p. 11, literal | Confere |
| Eq. (1.5), Tₙ = DUₙ/252, interpolação exponencial do DI1 | Manual v27, p. 11–12 | Confere |
| BSM para "opções sobre ações, ETFs e índices" | Seção 1.1 | Confere ("Merton" é rótulo nosso) |
| Volatilidade de ilíquidos por retorno log | Manual v27, 1.2.1 | Confere |
| DI1 em efetiva anual base 252; DI ao ano base 252 | B3 | Confere |
| Poupança 0,5% a.m. + TR, Selic > 8,5%, capitalização mensal | Lei 12.703/2012; Lei 8.177/1991, art. 12 | Confere |
| LTN: truncamento na 14ª casa e na 6ª | Tesouro, Tabela 3 | Confere |
| Excel pt-BR: EFETIVA, NOMINAL, TRUNCAR, LN, EXP | Suporte Microsoft | Confere |
| Hull, "usadas extensivamente" | Não encontrada | **[VERIFICAR] mantido**. Alternativa sem depender da fonte: "trabalha em taxa contínua e mostra a conversão entre as etiquetas" |
| "um dos mais usados no mercado" | Juízo qualitativo | Risco baixo |

**Bibliografia.** Maor: a Record confirma o ISBN 978-85-01-05847-8, mas não o ano. O
**[VERIFICAR] fica**, e o ano sai da ficha catalográfica ou da Biblioteca Nacional. Hull 11ª ed.,
cap. 4, seção 4.4: confere. Assaf Neto 15ª ed. (GEN Atlas, 2022): confere (fonte de varejo).
MacTutor: confere. A regra de referências também confere: 4 itens, 3 livros e nenhuma lei.

**Linha Notas de um Professor.** As fórmulas conferem tanto na forma simbólica quanto nos
números. Os exemplos são compatíveis com o Brasil de nov/2026, com a ressalva do I2. Os dois lados
do balcão estão presentes. Observação, sem bloqueio: o texto não diz por que o credor prefere
cotar em nominal.

## `[VERIFICAR]` pendentes

1. Formulação do Hull sobre o uso "extensivo" de taxas contínuas, que segue sem fonte. Alternativa: reescrever sem atribuir.
2. O ano da edição Record do Maor (ISBN 978-85-01-05847-8; o marketplace diz 2019, o Skoob diz 2006).

## Fontes novas desta etapa

- BCB SGS, séries 22022 e 25477 (API): https://api.bcb.gov.br/dados/serie/bcdata.sgs.22022/dados/ultimos/3?formato=json · https://api.bcb.gov.br/dados/serie/bcdata.sgs.25477/dados/ultimos/3?formato=json
- B3, Manual de Apreçamento – Opções v27: https://b3.com.br/data/files/0E/32/10/AB/5FBA0A105BF9020AAC094EA8/Manual%20de%20Aprecamento%20-%20Opcoes%20v27.pdf
- Record, página do livro (ISBN, sem ano): https://www.record.com.br/en/products/e-a-historia-de-um-numero
- Martins Fontes, Assaf Neto 15ª ed. 2022: https://www.martinsfontespaulista.com.br/matematica-financeira-e-suas-aplicacoes-1004941/p
