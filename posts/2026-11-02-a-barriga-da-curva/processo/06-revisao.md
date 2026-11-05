# Etapa 6 — Revisão de linha e norma

Laudo do agente `revisor-gramatical`, gravado pelo pipeline principal. Base: `04-draft-v2.md`,
corpo depois do segundo `---`; "lNN" = linha nesse arquivo. **[norma]** = erro objetivo ou regra 1
do guia (glosa na primeira ocorrência), aplicar sempre · **[linha]** = clareza/ritmo, sugestão ·
**★** = propostas de linha mais importantes. Fora do escopo: números, fórmulas, fatos, ordem,
`[VERIFICAR]`, vocabulário motor/régua. Itens que encostam em fato estão em C, para a etapa 7.

**Contagem:** 62 itens (≈ 24 de norma, ≈ 38 de linha), 18 ★.

---

## A. Diff comentado, por parágrafo

### l.43 (Duas linhas é pouco…)
1. [norma — glosa] "um CDB empata" → "um CDB (Certificado de Depósito Bancário) empata" (glosa do du252).
2. [norma — glosa] "percentual do CDI" → "percentual do CDI (no mercado, o nome da taxa DI, a dos empréstimos de um dia entre bancos)". Alternativa curta: "(a taxa dos empréstimos entre bancos)".
3. [norma — itálico + glosa] "CDI mais spread" → "CDI mais *spread* (o prêmio acima do CDI que paga o risco do devedor)"; segunda ocorrência só "*spread*".
4. [norma — glosa] "o du/252 estava no expoente" → "o du/252 (dias úteis sobre 252) estava no expoente".
5. [linha] "Em todas" → "Em todas essas contas" (o antecedente é a conta, não o produto).

### l.45
6. [norma — glosa] "Antes do FIDC" → "Antes do FIDC (Fundo de Investimento em Direitos Creditórios)"; na l.218 fica "Agora, sim, o FIDC, sem mais parênteses." (ver 60).
7. ★ [linha] "de primeiro período da faculdade" → "de primeiro semestre da faculdade" (libera "período" para o sentido técnico).

### l.49
8. ★ [linha] "É o que paga o juro simples" → "É o que o juro simples paga" (evita ler "quem paga o juro").

### l.53
9. ★ [linha — tique de IA] "A diferença, R$ 2.292,17, não é arredondamento. É a distância entre dois motores." → "A diferença, R$ 2.292,17, é a distância entre dois motores." (o aforismo da l.65 passa a ser o primeiro "não é X. É Y.").

### l.55
10. [norma — modo verbal] "qualquer taxa que alguém coloca" → "qualquer taxa que alguém coloque".

### l.59
11. [linha] "chamaria de oitava maravilha" → "chama de oitava maravilha" (a dúvida é a autoria, já ressalvada).

### l.61
12. [linha] "começa a trabalhar desde o primeiro dia" → "começa a trabalhar no primeiro dia".

### l.63
13. [linha] "entre zero e um período" → "entre zero e um período da taxa".

### l.83
14. ★ [linha] "Entra a constante de Euler, e ≈ 2,71828, e uma taxa instantânea r:" → "Entram o número de Euler (e ≈ 2,71828) e uma taxa instantânea r:" (ver C2).

### l.89
15. ★ [linha — ambiguidade] "Quem aplica e elevado a 0,14 vezes t, usando o número cotado como se fosse taxa instantânea, está calculando 15,03% ao ano sem perceber." → "Usar e elevado a (0,14 × t), com o número cotado no lugar da taxa instantânea, é calcular 15,03% ao ano sem perceber." ("aplica" = investir no resto do texto; posição do t no expoente.)

### l.95
16. [linha — calque] "compõe a parte inteira… compõe tudo" → "capitaliza a parte inteira… capitaliza tudo".

### l.101
17. [linha] "carregada por mais um ano" → "capitalizada por mais um ano" ("carregada" lembra "carrego").

### l.107
18. [linha — tique] "Eis a peça que separa quem decorou as fórmulas de quem as entende." → cortar (ou "Eis a peça central.").

### l.109
19. ★ [linha] "Os dois motores passam pelos mesmos dois pontos." → "A reta do simples e a curva do composto passam pelos mesmos dois pontos."

### l.111
20. [norma — glosa; alerta do briefing] "a corda de uma curva convexa" → "…convexa (no sentido do cálculo: arqueada para cima, como o fundo de uma tigela)".
21. [norma — vírgula] "quem não fez, pode confiar" → "quem não fez pode confiar".

### l.113 (legenda graf-01)
22. [linha — regra 3] "nos dois motores: a reta… e a curva… Entre…" → "nos dois motores (a reta do juro simples e a curva do juro composto). Entre…".

### l.115
23. ★ [linha] "Esta fica na outra ponta, no prazo curto, e mora dentro de qualquer taxa, não só na curva." → "Esta fica na ponta curta e mora dentro de qualquer taxa, não só na curva de juros." (a barriga da mesa é o meio, não uma ponta; "na curva" sozinho repete o duplo sentido).
24. [norma — glosa, opcional] "a barriga da curva de juros, os vencimentos intermediários" → "…curva de juros (a taxa de cada vencimento, do mais curto ao mais longo), os vencimentos intermediários".

### l.117
25. [linha, leve] "Na prática, isso quer dizer que, com o mesmo número cotado, o motor linear…" → "Com o mesmo número cotado, então, o motor linear…". Opcional.

### l.119 (taxa legal)
26. [norma — glosa] "a Resolução CMN nº 5.171" → "a Resolução nº 5.171 do Conselho Monetário Nacional (CMN)".
27. ★ [linha — ambiguidade] "paga a taxa do mês proporcional aos dias, cerca de metade," → "paga a taxa do mês em proporção aos dias, cerca de metade dela,".
28. ★ [linha — imagem] "fica do lado de cima da corda" → "paga pela reta, que nesse trecho passa acima da curva"; "e ele passa para o lado de baixo" → "e a reta passa para baixo da curva". Etapa 7 confere a leitura.

### l.125–127
29. ★ [linha — termo] "o juro simples sobre o capital, que cresce em linha reta" → "o juro linear, isto é, o juro simples sobre o capital, que cresce em linha reta" (batiza "juro linear", usado nas l.133, 137, 212).

### l.135 (legenda graf-02)
30. [linha] "no juro total de R$ 1.000 em juros compostos a 6%…" → "no juro total de R$ 1.000 aplicados a juros compostos de 6%, 10% e 14% ao ano".

### l.137
31. [norma — regência] "na ordem de grandeza" → "da ordem de grandeza".
32. [norma — glosa] "um juro real" → "um juro real (o que sobra acima da inflação)".
33. [linha, leve] "A virada, o prazo em que…" → "O cruzamento, o prazo em que…" (o H3 "A virada de 1998" usa a palavra em outro sentido). Opcional.

### l.147–151
34. [linha] "cota juros para muitos prazos" → "cota juros em muitos prazos".
35. [linha] "não consegue valer para todos os prazos ao mesmo tempo" → "…para todos os prazos".
36. [linha] "Rendeu 14,49%" → "Rende 14,49%" (presente, como o resto do parágrafo).
37. [linha, opcional] "com um fator de" → "com um fator (o número que multiplica o capital) de".

### l.153
38. [norma — itálico + glosa] "do overnight" → "do *overnight* (o empréstimo de um dia útil para o outro)".

### l.157 (A virada de 1998)
39. [norma — verbo] "O que se mudou foi a embalagem." → "O que mudou foi a embalagem."
40. [norma — itálico, série] "A over", "Cotava-se a over" → "A *over*", "Cotava-se a *over*" (como no du252).
41. [linha — glosa de série] "a taxa do mercado de um dia" → "a taxa dos empréstimos de um dia útil".
42. [linha — regra 3] "Uma taxa assim tem nome, taxa nominal, e o número cotado não é o que se recebe." → "Uma taxa assim tem nome: taxa nominal. Nela, o número cotado não é o que se recebe."

### l.159
43. ★ [norma — glosa] + [linha — sentido] "a Circular BCB nº 2.761, de junho de 1997, trocou essa embalagem pela Selic expressa ao ano, como taxa efetiva com base em 252 dias úteis, a partir de 1998." → "a Circular nº 2.761 do Banco Central do Brasil (BCB), de junho de 1997, trocou essa embalagem: a partir de 1998, a Selic (a taxa básica de juros) passou a ser expressa ao ano, como taxa efetiva com base em 252 dias úteis."
44. [linha, opcional] glosar "taxa efetiva": "(a que de fato se recebe no prazo a que se refere)".

### l.161
45. [norma — glosa] "Quarenta pontos-base de diferença" → "Quarenta pontos-base (0,40 ponto percentual) de diferença".

### l.167
46. ★ [linha — eco] "O motor linear não morreu. Ele ficou onde resolve melhor o problema de quem cota." → "O motor linear não morreu." (a segunda frase antecipa o fecho da l.175).

### l.169
47. ★ [linha — voz alta] "No cupom cambial, a taxa de juro em dólar negociada no Brasil, os contratos futuros da B3 (DDI) e o FRC, sua operação a termo, são cotados…" → "O cupom cambial é a taxa de juro em dólar negociada no Brasil. Nele, os contratos futuros da B3 (DDI) e o FRC, a operação a termo de cupom, são cotados…".
48. [linha] "rateados de forma proporcional ao tempo" → "remunerados em proporção ao tempo".
- B3 sem glosa: o du252 também não glosou; decisão do autor.

### l.171
49. [norma — glosa, colisão] "entre dois pagamentos de cupom" → "…de cupom (os juros periódicos do título)".

### l.173
50. ★ [norma — glosa] + [linha] "O contínuo ficou com os modelos: torna os retornos aditivos… Susep (…) estima antes de converter para taxa discreta." → "O contínuo ficou com os modelos. Ele torna os retornos aditivos no tempo (o retorno de dois períodos é a soma dos dois) e deixa o cálculo diferencial trabalhar. Por isso aparece na fórmula de Black-Scholes-Merton, a de preço de opções, e na curva de juros que a Susep (Superintendência de Seguros Privados) estima antes de converter em taxa discreta, a capitalizada por períodos."
51. [norma — regência] "converter para taxa discreta" → "converter em taxa discreta".

### l.179–185 (Três perguntas)
52. ★ [norma — pontuação] + [linha — série] Três linhas soltas sem interrogação → lista numerada: "1. Qual é o motor? Linear ou composto? 2. Qual é a base? 252, 360 ou 365? 3. Que dias contam? Os úteis ou os corridos?" (formato do du252; "composto" em vez de "exponencial").
53. [linha — eco] "as quatro contas que resolvem quase tudo" → "Na planilha, as quatro contas:".

### l.187–190
54. ★ [norma — glosa] Definir os símbolos da equação: "em que i₂₅₂ é a taxa composta base 252, i₃₆₀ a linear base 360, du os dias úteis e dc os dias corridos do período".

### l.193
55. [linha] "prever o lado antes da conta" → "prever a direção antes da conta".

### l.195
56. ★ [norma — concordância/unidade] "Do quase um ponto a mais, 0,75 vêm do motor… Os 0,17 restantes vêm da régua" → "Dos quase 100 pontos-base a mais, 75 vêm do motor… Os 17 restantes vêm da régua". Etapa 7 confere.
57. [linha] "porque 91 dias corridos sobre 360 são um pouco mais que 63 úteis sobre 252" → "porque 91/360 é um pouco mais que 63/252".

### l.197
58. [linha — ambiguidade] "A régua pesa mesmo num ano inteiro." → "Mesmo num ano inteiro, a régua pesa."

### l.208
59. [linha] "traz de volta as duas perguntas que ficaram no texto anterior, calendário e pontas." → "traz de volta as duas perguntas do texto anterior que ficaram de fora das três: calendário e pontas."

### l.218
60. [norma, consequência de 6] "o FIDC (Fundo de Investimento em Direitos Creditórios), sem mais parênteses" → "o FIDC, sem mais parênteses".

### l.222–230 (bibliografia)
61. [linha — série] H2 "Para continuar aprendendo" → "Para ir além" (título do du252).
62. ★ [linha — série] Garcia → "Márcio G. P. Garcia, [*Efeitos da anualização da taxa Selic*](url) (Departamento de Economia da PUC-Rio, 30/06/1997) — …" (mesmo título e data do du252; âncora "link" sozinha é má prática). Formato de lista: etapa 9.

---

## B. O que não corrigi, porque é voz

- Fragmentos de ênfase: "Sempre." (l.61); "Seis meses de uma taxa anual. Quinze dias de uma taxa mensal." (l.117); "Na LCA…, para achar…" (l.43).
- O aforismo das l.65 e 214, isolado e repetido (§5.4).
- "Com o mesmo número cotado" três vezes (l.111, 117, 212): insistência deliberada (M6).
- "Saiu uma taxa nominal, entrou uma efetiva." e "Em 1998, trocou uma taxa nominal por uma efetiva." (decisão do autor).
- "Duas linhas é pouco": concordância correta com expressão de quantidade.
- CTA com "te" e "você": mistura de tratamento pela norma estrita, mas o du252 aprovado faz o mesmo. Uniformizar é decisão do autor.
- Aspas simples em 'bola de neve', 'juro sobre juro', 'efetiva-dia', 'taxa nominal' (regra 4).
- "Quem faz a bola de neve crescer é o tempo." (l.141).

**Molde "não é X, é Y" (v2):** l.53, 65, 161 (×2), 167, 175, 214. Com os itens 9 e 46, ficam l.65 e 214 (aforismo), l.161 (autor) e l.175 (rascunho), espaçados e com função.

**Anáfora com "Quem…":** mais de dez ocorrências (l.89, 107×2, 111×2, 115, 139×2, 141, 149, 167, 175, 220). Os itens 15, 18 e 46 tiram três.

Nenhum marcador lexical da frente D §12 ("crucial", "mergulhar", "jornada" etc.).

---

## C. Para a etapa 7 e para o autor (não corrigido)

1. Samanez: a bibliografia ainda diz "José Carlos"; `03-pesquisa.md` confirma Carlos Patricio.
2. "Constante de Euler" costuma designar γ ≈ 0,5772; e ≈ 2,71828 é o número de Euler (ou de Neper).
3. "a taxa legal, a que corrige uma dívida civil": a taxa legal é de juros (Selic − IPCA), não correção monetária. Sugestão: "a taxa de juros que incide sobre uma dívida civil quando o contrato não fixa juros".
4. Over × Selic (l.157–159): o leitor não sabe se são a mesma taxa. Uma ponte ("a Selic over") resolveria; é fato.
5. l.197: "14% ao ano na base 360 rendem 14% × 365/360" não diz o motor (a conta é linear). Sugestão: "14% ao ano linear, base 360".
6. l.208: "ANBIMA" dentro do `[VERIFICAR]`; se ficar no texto, glosa do du252.
7. Estrutural: nada novo. Itens 18 e 52 mexem numa frase e na forma de uma lista.

---

## Decisões do autor (2026-11-04)

- **Aplicar:** todos os itens [norma] — 1, 2, 3, 4, 6, 10, 20, 21, 26, 31, 32, 38, 39, 40, 43, 45,
  49, 50, 51, 52, 54, 56, 60 — e todas as ★ — 7, 8, 9, 14, 15, 19, 23, 27, 28, 29, 43, 46, 47, 50,
  52, 54, 56, 62. O item 24 (glosa opcional de "curva de juros") não entra.
- **Não aplicar:** os demais itens de linha sem ★ (5, 11–13, 16–18, 22, 25, 30, 33–37, 41, 42, 44,
  48, 53, 55, 57–59) e o item 61 ("Para ir além").
- **Série:** uniformizar o tratamento do CTA em "você" ("Se este texto ajudou você a destravar…").
- Os itens 28 e 56 dependem da conferência da etapa 7; a seção C vai para a etapa 7.
- Aplicação: etapa 9 (consolidação), como no du252.
