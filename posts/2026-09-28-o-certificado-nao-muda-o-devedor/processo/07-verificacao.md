# Etapa 7 — Verificação técnica

Feita pelo agente `verificador-tecnico` sobre `04-draft-v1.md` (linhas citadas são dele),
acessos em 2026-09-27. Registro de cálculo (script, saída, tabela de conferência):
`_revisoes/2026-09-27_2026-09-28-o-certificado-nao-muda-o-devedor_calculo.md`.

**Resumo:** nenhuma divergência de cálculo e nenhum erro factual bloqueante.

- **M-4:** a Raízen S.A. (fiadora) está entre as requerentes. O `[VERIFICAR]` cai e o
  argumento fica mais forte.
- **M-3:** o regime fiduciário foi instituído na 73ª emissão.
- **M-2:** "Até a isenção foi preservada" generaliza. A isenção sobrevive só em parte da
  dívida nova.
- Há 11 substituições de redação. A mais sensível é a paráfrase do Migalhas.

Rótulos: **[OK]** confirmado · **[AJUSTAR]** · **[ERRADO]** · **[VERIFICAR]** não fechou.

## 1. Fórmulas e números (recalculados em python3)

| # | Afirmação | Veredito | Recálculo |
|---|---|---|---|
| 1.1 | 7%/0,85 ≈ IPCA + 8,24% | [OK] | 8,2353% |
| 1.2 | Fórmula fechada do empate | [OK] | Fatores iguais até a 15ª casa |
| 1.3 | Tabela do empate | [OK] | 8,4848/9,3007; 8,2353/8,8018; 8,2353/8,5196; 8,2353/8,1795 |
| 1.4 | Os erros "se anulam" por volta de nove anos | [OK] | Cruzamento em T ≈ 9,04; 11a = 8,13; 12a = 8,08 |
| 1.5 | Os dois erros puxam para lados opostos | [OK] | Coerente com a tabela |
| 1.6 | 1 ano → 17,5%; 2 anos → 15% | [OK] | Lei 11.033, art. 1º, III-IV (dias corridos) |
| 1.7-1.8 | Subordinação e max(0, L−S)/(1−S) | [OK] | — |
| 1.9 | 1,08³ ≈ 1,2597; PU a 9,5% ≈ R$ 959,46 | [OK] | 959,464 |
| 1.10 | PU a 12% ≈ R$ 896,64 | [AJUSTAR], cosmético | Exato: 896,638. Com o 1,2597 impresso, a conta dá 896,63. Escrever `1.000 × 1,08³ / 1,12³` nas duas contas |
| 1.11 | PU com du/252 | [OK] | 756/252 = 3 |
| 1.12 | Aderência dos exemplos ao mercado | [OK] | NTN-B em 25/09/2026: 7,21%-7,63%; a 73ª emissão saiu a IPCA + 6,00%/6,25%; IPCA de 4% está dentro da tolerância da meta |

Nota: no exemplo, "NTN-B + spread" aplica taxa tributada a papel isento. É a convenção de
mercado, com o benefício fiscal embutido no spread. Opcional: meia frase ligando ao empate.

## 2. Fatos Raízen

| # | Afirmação | Veredito | Fonte / redação |
|---|---|---|---|
| 2.1 | RE em 11/03/2026, ~R$ 65,1 bi | [OK] | Cosan 6-K, 11/03/2026 |
| 2.2 | "dívida financeira sem garantia" | [AJUSTAR] | → "sem garantia real". As debêntures são quirografárias, com fiança |
| 2.3 | Pacote com debêntures, bonds e CRAs | [OK] | Money Times, 12/03/2026 |
| 2.4 | "entre 60% e 90% dos CRAs da companhia estavam com pessoas físicas" | [AJUSTAR], leve | A faixa varia por emissão (InvestNews, 11/03/2026). → "a fatia com pessoas físicas ia de 60% a 90%, conforme a emissão" |
| 2.5 | Lastro com fiança da Raízen S.A. | [OK] | Termo da 73ª emissão; lâmina ("Concentrado") |
| 2.6 | **M-4: a fiadora é requerente?** | [OK], sim | FAQ Opea (22/09/2026) lista Raízen S.A., Raízen Energia S.A. e outras. **Redação para a l. 118:** "A fiança, por sua vez, era da Raízen S.A., que estava entre as requerentes da mesma recuperação extrajudicial. A garantidora pedia para reestruturar a própria dívida." |
| 2.7 | 73ª emissão: out/2023, 3 séries, R$ 1 bi, Pentágono, subscrição pela securitizadora | [OK] | Termo de 20/09/2023 (via Daycoval); emissão em 15/10/2023 |
| 2.8 | **M-3: regime fiduciário / "O patrimônio separado ficou onde a lei manda"** | [OK] | Termo, cl. 3.1.1 e 18.3 ("foi instituído o Regime Fiduciário"). Nenhum indício de desvio na Opea/Raízen |
| 2.9 | Assembleia vincula ausentes e dissidentes | [OK] | Termo, cl. 14.19 e 14.17 |
| 2.10 | "convocada pela securitizadora" | [AJUSTAR], leve | → "convocada pela securitizadora ou pelo agente fiduciário" (termo; RCVM 60) |
| 2.11 | ~50% do PU em jul/2026 | [OK] | Seu Dinheiro, 13/07/2026: "negociam próximos a 50% do preço unitário" |
| 2.12 | Homologação em 30/07/2026, vinculando não aderentes | [OK] | Migalhas; FAQ Opea |
| 2.13 | "uma das opções... preservam a isenção" | [OK] | Opção A: 55% em dívida nova, com os títulos da Raízen Energia como novos CRA isentos; os da Raízen Combustíveis como debêntures sem isenção; 45% em Units |
| 2.14 | **M-2: "Até a isenção foi preservada."** | [AJUSTAR] | Só em parte da dívida nova. Não vale para os 45% em ações, para as debêntures da Combustíveis nem para a Opção C (dinheiro). O enquadramento foi automático por valor (Opção A acima de R$ 13 mil por emissão; Opção C até esse valor, 75% limitado a R$ 9.750). Proposta ao autor (aforisma protegido): "Até parte da isenção sobreviveu. O que nenhuma estrutura tinha como preservar era o devedor." |
| 2.15 | Todo o estoque lastreado em debêntures da Raízen Energia | [OK] | FAQ Opea (10 séries) |

## 3. Normas

| # | Afirmação | Veredito | Nota |
|---|---|---|---|
| 3.1-3.2 | Lei 9.514/1997; Lei 11.076/2004 | [OK] | — |
| 3.3 | Lei 14.430, 03/08/2022, vigência na publicação | [OK] | Art. 39. O [VERIFICAR] da etapa 3 cai |
| 3.4 | Regime fiduciário como faculdade | [OK] | Art. 25 |
| 3.5 | Agente fiduciário em emissões públicas | [OK] | Art. 26, III |
| 3.6 | Art. 27 e § 4º | [OK] | Paráfrase fiel |
| 3.7 | Isenção PF: Lei 11.033, art. 3º, II e IV, vigente | [OK] | Planalto; MP 1.303 com vigência encerrada |
| 3.8 | Alienação fiduciária fora da recuperação, "em regra" | [OK] | Art. 49, § 3º (ressalva de bens de capital essenciais); art. 161, § 1º (Lei 14.112/2020) |
| 3.9 | CMN 5.118 e regra dos 2/3 | [OK] | "Receita consolidada"; alcança devedor, codevedor e garantidor |
| 3.10 | Setores: saúde, varejo, locação de veículos | [OK], secundária | Machado Meyer; InfoMoney (Zamp, Rede D'Or, Dasa) |
| 3.11 | "Reaproximar da finalidade" | [OK], secundária | Mayer Brown; Agência Brasil (nota da Fazenda). O texto original do gov.br não foi lido |
| 3.12 | 5.121 "ajustou a redação" | [AJUSTAR], leve | → "esclareceu e flexibilizou pontos da regra" |
| 3.13 | 5.212: qualquer PJ, aberta ou fechada | [OK] | DOU de 26/05/2025 |
| 3.14 | FGC "por instituição" | [AJUSTAR], leve | → "por instituição ou conglomerado" |
| 3.15 | CVM regula a securitizadora; CMN define o lastro | [OK] | — |

## 4. Afirmações conceituais

| # | Afirmação | Veredito | Nota |
|---|---|---|---|
| 4.1 | "subordinação quase não aparece" em devedor único | [OK], qualitativo | A 73ª emissão não tem série subordinada. Opcional: "raramente aparece" |
| 4.2-4.3 | Alienação fiduciária; assembleia | [OK] | — |
| 4.4 | NTN-B de duration parecida + spread | [OK] | Convenção Anbima |
| 4.5 | Anbima: taxas indicativas de CRI/CRA; curvas de crédito por rating | [OK] | Metodologia nov/2023; página de curvas de crédito |
| 4.6 | IR sobre o ganho nominal | [OK] | — |
| 4.7 | Na LCA, o investidor não vota | [OK] | — |
| 4.8 | Dois lados do balcão | [OK] | — |

## 5. Bibliografia e atribuições

| # | Item | Veredito | Nota |
|---|---|---|---|
| 5.1 | Gorton & Souleles | [OK] | NBER w11190. Contraponto do bail-out disponível (B-2) |
| 5.2 | Caminha e a "desintermediação" | [OK], secundária | Tese de Hélio Mendes (FD-USP) confirma a atribuição |
| 5.3 | Cerqueira | [OK] | — |
| 5.4 | Ribeiro Júnior | [AJUSTAR], leve | Título completo: *Securitização de Recebíveis: Elementos Constitutivos no Direito Brasileiro* |
| 5.5 | Fabozzi & Kothari | [OK] | — |
| 5.6 | Regra de referências | [OK] | 4 itens, 3 livros |
| 5.7 | **"É uma camada a mais de mediação." (l. 167)** | [AJUSTAR], **sensível** | A fonte (Farley Menezes, Migalhas, 14/04/2026) diz literalmente "camada adicional de mediação", na mesma função argumentativa. Saídas: (a) reescrever: "Entre você e a mesa de negociação há mais um intermediário. Não mais uma proteção."; (b) atribuir: "o que o advogado Farley Menezes chamou de posição 'juridicamente mediada'". A l. 19 é aceitável sozinha |

## Lista consolidada para a etapa 9

**[VERIFICAR] pendente:** nenhum. **[FAIXA]:** nenhum.

1. l. 15: "sem garantia" → "sem garantia real".
2. l. 15: a faixa de 60% a 90% passa a ser "conforme a emissão".
3. l. 118: fiança + [VERIFICAR] → redação do item 2.6.
4. l. 163: "pela securitizadora ou pelo agente fiduciário".
5. l. 167: reescrever ou atribuir (5.7). Pergunta ao autor, porque é aforisma protegido.
6. l. 183: 5.121 "esclareceu e flexibilizou pontos da regra".
7. l. 268/272: escrever 1,08³ nas duas contas de PU.
8. l. 308: "Até parte da isenção sobreviveu." Pergunta ao autor (M-2).
9. Tabela, linha FGC: "por instituição ou conglomerado".
10. Bibliografia: título completo de Ribeiro Júnior.
11. l. 79: espaço duplo.

**Fontes principais:** termo da 73ª emissão (Daycoval PDF); FAQ Opea; Cosan 6-K de
11/03/2026; lâmina da oferta; Planalto (Leis 14.430, 11.033, 11.101); Mayer Brown e Machado
Meyer (CMN 5.118); Agência Brasil (fev/2024); Cescon Barrieu e IRIB (5.212); FGC; Anbima
(curvas de crédito); NBER w11190; Migalhas (Farley Menezes; homologação); InvestNews
(11/03/2026); Seu Dinheiro (13/07/2026; NTN-B set/2026); tese de Hélio Mendes (USP);
InfoMoney (02/02/2024). As URLs estão em `03-pesquisa.md` e no registro de cálculo.
