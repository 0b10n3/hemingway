# Etapa 6: Revisão de linha e norma

Base: corpo de `04-draft-v2.md`, de "# Cara, eu ganho. Coroa, eu não perco." até "Para continuar
aprendendo" (L33 a L291). Aviso legal fora (etapa 9). As referências de linha (L…) são do
`04-draft-v2.md`.

**Resumo:** 37 itens. **8 `norma`**, **29 `linha`** (21 com ★, que eu aplicaria). Seis
problemas factuais ou de coerência que passaram vão no fim, sem correção.

Não mexi em: estrutura e ordem das seções; números e fatos (etapa 7); o `[VERIFICAR]` da
abertura; as redações novas do autor (notas 1 a 9 do v2), salvo onde digo; negrito (regra 4),
glosas em parêntese, perguntas retóricas e os dois refrões, que são voz.

## Diff comentado

### Abertura

**¶ L51** «Separados, o principal da NTN-F 2029…»

**1.** `linha` ★
- Original: «Separados, o principal da NTN-F 2029 e a LTN 2029 são a mesma promessa.»
- Corrigido: «Separado dos cupons, o principal da NTN-F 2029 e a LTN 2029 são a mesma promessa.»
- Motivo: no plural, o particípio concorda com o sujeito composto e diz que os dois foram
  separados. Só o principal da NTN-F foi. No singular e com o complemento, ele fica preso ao
  principal.

### A taxa não manda no preço

**¶ L61** «Cada título tem a sua taxa…»

**2.** `norma`
- Original: «A NTN-F é cotada pela TIR (…), a LTN pela dela, e o preço sai de cada taxa.»
- Corrigido: «A NTN-F é cotada pela TIR (…), a LTN, pela dela, e o preço sai de cada taxa.»
- Motivo: vírgula que marca a elipse do verbo (zeugma: "a LTN [é cotada] pela dela"). Depois da
  glosa longa da TIR, sem essa vírgula, "a LTN pela dela" parece continuar a glosa. Se quiser
  mais claro ainda: "pela taxa dela".

**¶ L63** «E arbitragem, nessa versão…»

**3.** `linha`
- Original: «…é qualquer operação esperta entre dois ativos parecidos, que aposta que a diferença de preço
  entre eles vai fechar.»
- Corrigido: «…é qualquer operação esperta entre dois ativos parecidos: uma aposta de que a diferença de
  preço entre eles vai fechar.»
- Motivo: "que aposta que" encadeia dois "que". A forma corrigida é a que o próprio texto usa ao
  retomar o trecho em L214 ("qualquer aposta de que a diferença…"), e a retomada fica literal.

**¶ L65** «As duas metades erram pelo mesmo motivo…»

**4.** `linha`
- Original: «…tratam o preço como opinião. A opinião do mercado sobre os juros, sobre o título, sobre o
  futuro.»
- Corrigido: «…tratam o preço como opinião.»
- Motivo: tríade em série (§7.2). O bloco tem duas: esta e a de L69 ("a fórmula de valor
  presente, o preço justo de uma NTN-F e… Black-Scholes"). A de L69 é roteiro do texto. Esta é
  ornamento. Sem ★: está no rascunho e prepara o refrão.

### A aposta que não sobrevive

**¶ L94** «Agora suponha que alguém cote…»

**5.** `linha` ★
- Original: «Agora suponha que alguém cote o principal desmembrado de uma NTN-F, que paga os mesmos R$ 1.000
  na mesma data, a R$ 870,00.»
- Corrigido: «Agora suponha que alguém cote a R$ 870,00 o principal desmembrado de uma NTN-F, que paga os
  mesmos R$ 1.000 na mesma data.»
- Motivo: o preço fica longe do verbo, depois da relativa, e "na mesma data, a R$ 870,00" se lê
  como parte do que o título paga.

### Preço sem opinião

**¶ L129** «Da Lei do Preço Único sai, primeiro, a soma…»

**6.** `linha`
- Original: «O preço de um pacote é a soma do preço das peças.»
- Corrigido: «O preço de um pacote é a soma dos preços das peças.»
- Motivo: a soma é de vários preços. Sem ★: o singular distributivo também é aceito.

**7.** `linha`
- Original: «Se a carteira C paga exatamente o que A e B pagam juntos»
- Corrigido: «Se a carteira *C* paga exatamente o que *A* e *B* pagam juntos»
- Motivo: regra 4 (itálico em variável). No meio da frase, "A" maiúsculo pode ser lido como
  artigo. No site, o autor pôs o *e* de frequencia-de-capitalizacao em itálico pelo mesmo motivo.
  A fórmula na linha, "P(C) = P(A) + P(B)", fica como está. Sem ★: o risco de má leitura é baixo.

**¶ L139** «em que CF_t é o fluxo…»

**8.** `norma`
- Original: «em que CF_t é o fluxo pago na data t, du_t são os dias úteis até ela e r_t é a taxa
  zero-cupom (…) do vértice t (…)»
- Corrigido: «em que CFₜ é o fluxo pago na data *t*, duₜ são os dias úteis até ela e rₜ é a taxa
  zero-cupom (…) do vértice *t* (…)»
- Motivo: formatação. Em prosa, o sublinhado pode virar marcação de itálico: o par "_t é o fluxo
  pago na data t, du_" fica em itálico em conversores fora do CommonMark e ao colar no editor.
  Fora do bloco `$$`, a notação de LaTeX também não renderiza. O texto anterior da série resolveu
  isso com subscrito Unicode (TPreₙ, DUₙ, rₙ). O ₜ é do mesmo bloco de caracteres do ₙ, que o
  site já mostrou sem problema. O *t* solto vai em itálico (regra 4).

**9.** `linha` ★
- Original: a mesma frase, com «du_t são os dias úteis até ela» e dois parênteses seguidos depois de
  «taxa zero-cupom».
- Corrigido: «em que CFₜ é o fluxo pago na data *t*, duₜ é o número de dias úteis até ela e rₜ é a
  taxa zero-cupom do vértice *t* (cada prazo da curva). A taxa zero-cupom, também chamada de taxa
  *spot*, é a de um título que só paga no fim.»
- Motivo: a glosa da taxa *spot* separa "a taxa zero-cupom" de "do vértice t", e o leitor perde o
  fio numa frase que já carrega três variáveis. "É o número de dias úteis" segue o texto anterior
  ("DUₙ é o número de dias úteis") e evita o verbo no plural com sujeito que é uma variável. O
  conteúdo da glosa não muda: só sai do parêntese.

**¶ L141** «Repare de onde a fórmula veio…»

**10.** `linha`
- Original: «Repare de onde a fórmula veio. Ela não começou como matemática de valor presente. Começou com
  uma aposta que não sobrevive.»
- Corrigido: «Repare de onde a fórmula veio: de uma aposta que não sobrevive.»
- Motivo: regra 20. A seção já tem uma forma corretiva ("Em vez de perguntar…, ela pergunta…",
  L127), e esta fecha o bloco em antítese, como L184 e L246 fecham os deles. Sem ★: é antítese
  isolada e vem do rascunho. O anel com o H2 "A aposta que não sobrevive" se mantém nas duas
  versões.

**¶ L147** «Em 1973, Fischer Black e Myron Scholes…» (64 palavras)

**11.** `linha` ★
- Original: um parágrafo só.
- Corrigido: «…ajustada continuamente conforme o preço da ação se mexe.» ¶ «Se a réplica existe, a opção tem
  de custar o mesmo que ela. Senão, alguém compra uma, vende a outra e embolsa a diferença.»
- Motivo: regra 1 e §7.1 (parágrafo acima de ~60 palavras). A virada é a Lei do Preço Único
  aplicada à opção, e ela fica sozinha.

### Uma NTN-F feita de LTNs

**¶ L167** «Agora suponha três LTNs…»

**12.** `linha`
- Original: «Agora suponha três LTNs vencendo exatamente nessas datas»
- Corrigido: «Agora suponha três LTNs que vencem exatamente nessas datas»
- Motivo: a norma mais estrita condena o gerúndio com valor de adjetivo. Sem ★: na mesa, é uso
  corrente.

**13.** `linha` ★
- Original: «com a Selic em 13,75%, mantida pelo Copom»
- Corrigido: «com a Selic (a taxa básica de juros) em 13,75%, mantida pelo Copom»
- Motivo: regra 14. A linha Notas glosa a Selic assim em frequencia-de-capitalizacao,
  a-corda-e-o-arco e voce-esta-contando-os-dias-errado, e o post é de topo de funil. O "meta"
  está nos problemas que passaram (item B).

**¶ L169** «Para replicar a NTN-F, compre, em cada data…»

**14.** `linha` ★
- Original: «Para replicar a NTN-F, compre, em cada data, LTNs na quantidade fluxo ÷ 1.000:»
- Corrigido: «Para replicar a NTN-F, compre hoje, para cada data, LTNs na quantidade fluxo ÷ 1.000:»
- Motivo: "em cada data" indica quando comprar. Mas a compra é hoje, de LTNs que vencem em cada
  data. A leitura errada muda a operação.

### A moeda aparece

**¶ L188, L190, L252** *dealer*

**15.** `norma`
- Original: «Suponha um dealer (…)» (L188); «do dealer» (L190); «o erro do dealer do exemplo» (L252)
- Corrigido: «Suponha um *dealer* (…)»; «do *dealer*»; «o erro do *dealer* do exemplo»
- Motivo: itálico em estrangeirismo não aportuguesado (regra 4; Manual de Comunicação do Senado).
  O briefing dá *dealer* como já em itálico, mas não está.

**¶ L190** «A mesa compra 100.000 NTN-F do dealer…»

**16.** `linha` ★
- Original: «4.881 LTNs de 126 dias, 4.881 de 252 e 104.881 de 378.»
- Corrigido: «4.881 LTNs de 126 dias úteis, 4.881 de 252 e 104.881 de 378.»
- Motivo: a série inteira é sobre a diferença entre dias corridos e dias úteis, e aqui a elipse
  vira imprecisão. Nenhum número muda.

**17.** `linha`
- Original: «100.000 NTN-F» (L190 e na tabela, L194)
- Corrigido: «100.000 NTN-Fs»
- Motivo: plural de sigla com numeral, por consistência: o mesmo parágrafo tem "4.881 LTNs", e
  L282 tem "NTN-Fs". Sem ★: "NTN-Fs" soa pesado e o mercado costuma deixar a sigla invariável.
  O que importa é escolher uma forma só.

**¶ L198** «O arredondamento dos lotes…»

**18.** `linha` ★
- Original: «Descontada essa sobra, o lucro travado é de R$ 20.307,28»
- Corrigido: «Descontado esse custo do arredondamento, o lucro travado é de R$ 20.307,28»
- Motivo: "sobra" sugere um excedente a favor da mesa. Aqui é o que ela fica devendo a mais. O
  sinal se inverte na leitura.

### A mesma conta, todo dia

**¶ L208** «A decomposição existe até fisicamente…»

**19.** `linha` ★
- Original: «que transforma uma NTN-F em zeros negociáveis.»
- Corrigido: «que transforma uma NTN-F em zeros negociáveis (títulos que só pagam no fim).»
- Motivo: regra 14. "Zero" como substantivo é jargão e aparece aqui pela primeira vez. O texto
  definiu "taxa zero-cupom", não "zero". A glosa repete a definição de L139.

**¶ L210** «E a ANBIMA faz a conta ao contrário…»

**20.** `linha` ★
- Original: «A estrutura a termo prefixada que ela divulga é estimada…»
- Corrigido: «A estrutura a termo prefixada que ela divulga (a curva de juros, prazo a prazo) é estimada…»
- Motivo: regra 14. O texto chama o mesmo objeto de "curva prefixada" em L92 e L167. Sem a
  glosa, o leitor não liga uma coisa à outra, e a frase-tese do parágrafo ("a Lei do Preço Único
  aplicada a uma prateleira inteira") perde o apoio.

**21.** `linha`
- Original: «…pelo modelo de Svensson: os fatores de desconto que melhor explicam todos esses preços ao
  mesmo tempo.»
- Corrigido: «…pelo modelo de Svensson. O que sai dele são os fatores de desconto que melhor explicam
  todos esses preços ao mesmo tempo.»
- Motivo: logo depois de "modelo de Svensson", o dois-pontos parece definir o modelo. Mas o que
  vem depois é o resultado, a estrutura a termo. Sem ★: com a glosa do item 20, a leitura já
  melhora.

### Nem toda convergência é arbitragem

**¶ L214** «Volte à segunda metade do mito…»

**22.** `linha` ★
- Original: «Volte à segunda metade do mito:»
- Corrigido: «Volte à segunda metade da versão que circula:»
- Motivo: o texto nunca chamou de "mito" a versão de L59 a L63, então o leitor não tem a que
  ligar a palavra. "O Mito" é o nome do movimento 2 do `docs/BACKWARDS_DESIGN.md`, e o rótulo
  vazou para a prosa. "A versão que circula" é a expressão de L59 e fecha o anel.

**¶ L220, L228, L232** *trading*

**23.** `norma`
- Original: «Isso é **trading de correlação**» (L220); «No trading de correlação» (L228); «Trading de
  correlação merece» (L232)
- Corrigido: «Isso é ***trading* de correlação**»; «No *trading* de correlação»; «*Trading* de
  correlação merece»
- Motivo: estrangeirismo não aportuguesado. O corpus publicado põe *trading* em itálico (*trading
  floor*, "uma *trading*"). Em Markdown, `***trading* de correlação**` deixa o termo todo em
  negrito e só *trading* em itálico.

**¶ L220** «Isso é trading de correlação…»

**24.** `linha` ★
- Original: «…uma aposta numa relação estatística, que vale em média, até deixar de valer. A arbitragem se
  apoia numa identidade de fluxos, que vale em todo cenário.»
- Corrigido: «…uma aposta numa relação estatística, que vale em média, até deixar de valer.»
- Motivo: regra 20 e §7.2. Esta seção, sozinha, tem quatro contrastes entre arbitragem e
  correlação (L220, L222, L226 a L228, L232). L220 e L222 ficam seguidos, o que o teto proíbe. A
  frase cortada diz o mesmo que o fecho da seção ("a arbitragem vive de identidade, a correlação
  vive de estatística", L232). L222, redação nova do autor, fica. Alternativa, se o autor quiser
  L220 inteira: cortar o segundo período de L232 e fechar em "…e vai ganhar um.". Isso tira
  também o fecho-síntese "Por ora, basta a fronteira:".

**¶ L226** «Na NTN-F do exemplo, não…»

**25.** `norma`
- Original: «O marca a mercado pode doer no meio do caminho»
- Corrigido: «A marcação a mercado pode doer no meio do caminho»
- Motivo: o substantivo é "marcação a mercado", feminino. "O marca a mercado" é decalque oral de
  *mark-to-market*. O próprio texto escreve "a marcação a mercado" em L266 e usa o verbo em L115
  e L244.

### Os limites da arbitragem de verdade

**¶ L236** «Até a arbitragem de verdade tem custo…»

**26.** `linha` ★
- Original: «a arbitragem de livro não exige capital nem corre risco; a de verdade quase sempre exige os
  dois.»
- Corrigido: «a arbitragem de livro não exige capital nem corre risco; a de verdade quase sempre exige
  capital e corre risco.»
- Motivo: "exige os dois" põe "risco" como objeto de "exigir", e a elipse não fecha: risco se
  corre, não se exige.

**¶ L241 e L266** *spread*

**27.** `norma`
- Original: «**Cada ponta cruza um spread.** O spread de compra e venda é…» (L241); «o spread, a margem»
  (L266)
- Corrigido: «**Cada ponta cruza um *spread*.** O *spread* de compra e venda é…»; «o *spread*, a
  margem»
- Motivo: estrangeirismo. O Manual do Senado cita *spread* como exemplo de termo em itálico, e o
  corpus publicado o põe em itálico em todos os posts recentes.

**¶ L242** «3. Nem toda data tem LTN…»

**28.** `norma`
- Original: «a mesa recorre ao DI futuro (o contrato da B3 sobre a taxa DI), que não paga o mesmo fluxo»
- Corrigido: «a mesa recorre ao DI futuro (o contrato da B3 sobre a taxa DI, a dos empréstimos de um dia
  entre bancos), que não paga o mesmo fluxo»
- Motivo: regra 14, termo central do item. O atrito 3 depende de o leitor saber que a taxa DI é
  de banco, não do Tesouro ("referência na taxa DI, não no Tesouro"). A glosa é a mesma de
  a-corda-e-o-arco e frequencia-de-capitalizacao.

**¶ L244** «Há ainda o capital…» (74 palavras)

**29.** `linha` ★
- Original: um parágrafo só.
- Corrigido: «…sem desmontar a operação.» ¶ «Shleifer e Vishny mostram por que esse dinheiro falta na pior
  hora: quem arbitra costuma usar capital de terceiros, que sai depois da perda. A arbitragem pode
  falhar justo quando os preços mais se afastam do valor.»
- Motivo: regra 1. A quebra fica na virada: a mecânica da margem de um lado, o mecanismo de
  Shleifer e Vishny do outro. Os dois pedaços ficam perto de 37 palavras.

**¶ L246** «Por isso os desvios…»

**30.** `linha` ★
- Original: «…não são, em geral, dinheiro esquecido. Na maior parte das vezes, são o preço desses atritos.»
- Corrigido: «…não são, em geral, dinheiro esquecido. São o preço desses atritos.»
- Motivo: duas ressalvas para a mesma ideia ("em geral" e "na maior parte das vezes"). Uma basta,
  e a antítese, que é do rascunho, fica limpa.

### Antes de chamar de arbitragem

**¶ L250** «Sabendo de onde vem o preço…»

**31.** `linha` ★
- Original: «Sabendo de onde vem o preço, a decisão muda em dois lugares.»
- Corrigido: «Sabendo de onde vem o preço, você decide diferente em dois momentos.»
- Motivo: o sujeito implícito do gerúndio não é o da oração principal: a decisão não "sabe".
  Além disso, "lugares" não casa com "O primeiro é a hora de…" e "O segundo é a hora de…" (L252,
  L262).

**¶ L265** «2. O devedor é o mesmo?…»

**32.** `linha` ★
- Original: «Um CDB e uma LTN com o mesmo vencimento…»
- Corrigido: «Um CDB (Certificado de Depósito Bancário) e uma LTN com o mesmo vencimento…»
- Motivo: regra 14. O leitor da linha sabe o que é CDB, mas a pergunta é sobre o devedor, e o
  nome por extenso mostra que o devedor é o banco. É a glosa de a-corda-e-o-arco e de
  frequencia-de-capitalizacao.

### A moeda que ninguém lança duas vezes

**¶ L274** «A aposta da abertura existe…»

**33.** `linha` ★
- Original: «Cara, eu ganho; coroa, eu não perco.»
- Corrigido: «Cara, eu ganho. Coroa, eu não perco.»
- Motivo: refrão literal (§4.2: tese em refrão repetida no fecho; movimento 3 dos aspiracionais:
  repetir em vez de variar). O título e L78 usam essa forma.

**¶ L280** «Se o texto funcionou…» (88 palavras)

**34.** `linha` ★
- Original: um parágrafo só.
- Corrigido: «…A NTN-B Principal paga só o VNA, no vencimento.» ¶ «Se houvesse uma NTN-B Principal em cada
  data de cupom, quantas de cada data replicariam uma NTN-B? E por que comprar a NTN-B e vender
  essa réplica seria arbitragem, mas comprar a NTN-B e vender LTNs não é?»
- Motivo: regra 1. A quebra separa os dados do exercício das perguntas, que ficam sozinhas.

**35.** `linha` ★
- Original: «sobre o VNA (valor nominal atualizado pelo IPCA)»
- Corrigido: «sobre o VNA (valor nominal atualizado pelo IPCA, o índice oficial de inflação)»
- Motivo: regra 14. A segunda pergunta do exercício só se responde sabendo que a NTN-B paga fluxo
  corrigido pela inflação e a LTN, fluxo nominal. É a glosa do corpus ("IPCA (o índice oficial de
  inflação)").

**¶ L282** «No próximo texto, a conta vai ao contrário…» (66 palavras)

**36.** `linha` ★
- Original: um parágrafo só.
- Corrigido: «…vértice por vértice.» ¶ «É o *bootstrapping* (…), e é nele que fica claro por que a TIR de
  uma NTN-F e a taxa *spot* do mesmo prazo são objetos diferentes.»
- Motivo: regra 1. A quebra fica na virada entre anunciar o próximo texto e dar nome a ele.

### Para continuar aprendendo

**¶ L288** Tuckman e Serrat

**37.** `norma`
- Original: «*Fixed Income Securities: Tools for Today's Markets*»
- Corrigido: «*Fixed Income Securities: Tools for Today’s Markets*»
- Motivo: apóstrofo reto. No texto final, aspas e apóstrofo são sempre curvos (regra 4). É o único
  sinal reto do corpo.

## Decisões de glosa (regra 14)

| Termo | Decisão | Por quê |
|---|---|---|
| ANBIMA | sem glosa | O leitor da linha conhece. O corpus a deixa sem glosa na prosa (voce-esta-contando-os-dias-errado, renda-fixa-condicoes-variaveis), e a frase diz o que ela divulga |
| Svensson | sem glosa | É nome de modelo, e a própria frase diz o que ele entrega (ver item 21) |
| B3 | sem glosa | O texto anterior da série a glosou na mesma frase ("o manual de opções da B3, a bolsa brasileira"), e L216 fala em "bolsa brasileira" |
| taxa DI | glosa, `norma` | Item 28. "CDI" não aparece no texto |
| CDB | glosa, `linha` ★ | Item 32 |
| Copom | sem glosa | É periférico, e "mantida pelo Copom na reunião" já diz o que ele faz |
| Selic | glosa, `linha` ★ | Item 13 |
| IPCA | glosa, `linha` ★ | Item 35 |
| Tesouro Direto | não aparece | O exercício usa o nome do título ("Tesouro IPCA+ com Juros Semestrais"), que já serve de glosa |
| estrutura a termo, zeros | glosa, `linha` ★ | Itens 20 e 19 (fora da lista do briefing) |
| PU | fica | A glosa (L180) vem duas linhas depois do cabeçalho da tabela (L171). Em tabela, é aceitável |
| *long-short*, mesa, margem | sem glosa | *Long-short* só aparece no CTA, que mira quem encaminha. Mesa e margem são vocabulário do público (júnior de mesa) |

## Tiques e teto (§7.2, regra 20)

- **Travessão:** nenhum no corpo. **Exclamação:** nenhuma. **Aspas:** todas curvas, exceto o
  apóstrofo do item 37. **Aspas simples de ênfase:** nenhuma.
- **Antítese "não é X. É Y.":** sete no corpo (refrão duas vezes; L82 "Não se prova, se assume";
  L141; L184; L222; L246), cerca de 2,4 por mil palavras, contra 0,83 do autor. Por seção, só
  "Nem toda convergência é arbitragem" (com "Os limites") passa do teto, com L220 e L222 seguidos:
  item 24. "Preço sem opinião" tem duas formas corretivas (L127 e L141): item 10, sem ★. Quatro de
  doze blocos fecham em contraste (L141, L184, L232, L246), não todos.
- **Tríade:** no máximo uma por bloco, exceto em "A taxa não manda no preço" (L65 e L69): item 4.
- **Teaser ou metadiscurso:** "Agora, um caso concreto." (L47) e "O que sai dela é bem maior que a
  igualdade entre dois preços." (L119). Um de cada, isolados, dentro do teto. Sem item.
- **Fecho-síntese:** "Por ora, basta a fronteira:" (L232), um só, dentro do teto. A alternativa
  do item 24 o remove.
- **Frase-golpe:** a série curta da abertura (L41) é cena (regra 1). Sem item.
- **Parágrafos acima de ~60 palavras:** L147, L244, L280 e L282 (itens 11, 29, 34 e 36). L242
  (68) é item de lista, e com a glosa do item 28 chega a cerca de 76; em lista, a quebra não cabe
  bem, então fica com o autor. L49 (63) é quase todo o `[VERIFICAR]` e fica. L47, L61 e L230 têm
  58 ou 59 palavras: sem proposta.

## Problemas factuais e de coerência que passaram (sem correção)

**A. "exatamente 100.000 vezes os R$ 0,20 de diferença" (L198).** Com o 0,20 arredondado,
100.000 × 0,20 dá R$ 20.000. Os R$ 20.307,28 vêm da diferença sem arredondar (R$ 0,203073), e
"exatamente" só vale para ela. A etapa 7 decide como escrever o número.

**B. "com a Selic em 13,75%, mantida pelo Copom" (L167).** O Copom fixa a *meta* da Selic. A taxa
Selic efetiva costuma ficar cerca de 0,10 ponto abaixo. O corpus usa "a meta da Selic (a taxa
básica de juros)". Etapa 7.

**C. "centavo por centavo" (L226) e "os cupons e o principal da NTN-F pagam as LTNs vendidas"
(L202), contra L198.** O arredondamento dos lotes deixa a mesa devendo R$ 115,18 a mais em cada
data. A conta fecha porque os R$ 302,60 ficaram guardados hoje, mas "centavo por centavo, pelos
fluxos da NTN-F" não vale ao pé da letra. Para a etapa 7 ou o autor.

**D. "cerca de 2 pontos-base" (L204) e "2 pontos-base somem rápido" (L241).** Em L204, a base é o
valor da operação (preço). Na renda fixa, ponto-base se lê, por padrão, na taxa, e o *spread* de
compra e venda de título público é cotado em taxa. Aqui as duas leituras dão perto de 2 (TIR de
14,55% contra 14,53%; R$ 0,20 sobre R$ 943,88). Mesmo assim, a etapa 7 deve confirmar qual base o
texto usa e se L241 compara a mesma unidade (alerta do briefing).

**E. "O Tesouro não emite LTN para todo semestre" (L242).** Conferir no calendário de vencimentos
de LTN. Em parte dos anos, as datas de cupom da NTN-F (1º de janeiro e 1º de julho) têm LTN, e a
frase pode soar mais forte do que o fato. Etapa 7.

**F. Planilha (L257).** `(1+C2:C4)` supõe as taxas em formato de porcentagem (14,00% guardado como
0,14). Se a célula tiver 14,00, o PU sai errado. Uma oração na frase de L254 resolveria, mas a
fórmula é da etapa 7.

Registro, sem proposta: em L268, a regra de decisão "desde que haja capital para levar a posição
até o vencimento" repete o que a pergunta 3 (L266) já pergunta ("quanto custa sustentar a
posição até o vencimento", "o capital para atravessar a marcação a mercado"). É redação do autor
(nota 9 do v2) e fica com ele no gate.
