# Etapa 5 — Crítica estrutural

Executor: subagente `critico-editorial`. Texto criticado: corpo de `processo/04-draft-v1.md`.
Linha **Notas de um Professor**, tipo matemática financeira (`docs/BACKWARDS_DESIGN.md` §4.2),
sem validação argumentativa de Spoiler. As respostas do autor às tensões do briefing (título,
aprofundamento, profundidade, linha pessoal) não foram reabertas. O laudo diagnostica e não
reescreve.

## Resumo

O argumento se sustenta. A tese ("O contínuo não compete com o composto. É o limite dele.")
aparece isolada no movimento 2 e no 9. A identidade (1 + i)^t = e^{rt} chega no lugar certo e
prova o que a seção promete. Os três pilares estão presentes: dado (escada de Bernoulli, R$
9.342 / 887 / 45, Black-Scholes), narrativa (Bernoulli até Euler, continuidade de série) e visual
(graf-01, graf-02). A voz ensaística em registro técnico é estável.

**Nenhum achado de severidade alta.** Os problemas são de entrega incompleta: uma promessa do
gancho sem lugar de entrega, uma hipótese anunciada e não usada, uma competência mostrada numa
taxa só, o lado de quem paga ausente nas opções e um parágrafo final que sai do assunto. São 8
achados médios e 10 baixos.

## Respostas aos cinco pontos de atenção

**(1) O movimento 4 em duas partes, com o 5 no meio.** O leitor sente a volta, e ela funciona. A
pergunta que abre "Por que a mesa de opções fala contínuo" retoma explicitamente o clímax de
"Mesma curva, outra etiqueta". A ordem 4a → 5a → 4b → 5b sustenta o argumento: o fecho de "Onde
mora o erro" (menos de 0,5 pb contra 103 pb) depende do número que "Rende todo dia" estabeleceu
antes. O custo está em B1.

**(2) Competência de saída e teste de transferência.** Entrega em parte. "Converter" e
"traduzir DI → modelo" são entregues por inteiro. "Avaliar se a frequência pesa para a taxa e o
prazo em jogo" é mostrada só a 14% e um ano (M6). O teste da poupança está equipado, mas é uma
transferência curta, que exercita só a conversão (B5).

**(3) Sobreposição com "A Corda e o Arco".** Três das quatro sobreposições fazem remissão
explícita: r = ln(1,14), o erro dos 15,03% e a *over* como nominal. Sobram a pergunta-âncora, que
o fecho anterior já tinha respondido (M1), e as conveniências 1 e 2, que repetem sem remissão a
frase anterior (B4).

**(4) Súmula 541.** Vale como sugestão ao gate, com lugar definido. Serve à tese-mãe ("é
cláusula") e ao lado de quem paga, não à tese do limite (B6).

**(5) Dois lados do balcão.** Bastam para o checklist (§6). Não bastam para o ponto cego: no caso
em que o erro custa 103 pb, o texto não diz quem paga (M7).

## Achados

### M1. A pergunta-âncora já foi respondida pela série (média)
**Onde:** abertura, "Mas sobe até onde? … o rendimento cresce sem limite?". O fecho de "A Corda e
o Arco" já respondeu ("Com doze, 14,93% (…) o rendimento nunca passa dos 15,03%"). Para o leitor
da série, a pergunta que move o texto não tem incógnita. O que ele não sabe é por que o teto é
e^j e que a frequência pesa menos que a etiqueta, e a pergunta-âncora não aponta para nenhum dos
dois.

### M2. A primeira promessa do gancho não tem lugar de entrega (média)
**Onde:** fim da abertura ("o du/252 (…) é só um caso particular") e Fechamento ("explicado de
ponta a ponta"). A segunda promessa (manual da B3) ganha H2 própria. A primeira fica dispersa em
três lugares ("Mesma curva", a lista das cinco taxas, o parágrafo do DI) e nunca é fechada como
resposta. O Fechamento declara "de ponta a ponta" em cima dessa promessa incompleta.

### M3. A segunda metade da tese não aparece no título, no deck nem no gancho (média)
**Onde:** H1, subtítulo provisório e abertura. A parte mais útil da tese ("a diferença que pesa
no bolso vem de ler a etiqueta errada") só se paga em "Onde mora o erro". O deck descreve o
assunto, e o movimento 0 pede a tese. Não é alta porque os dois aforismos estão isolados e o deck
já vai ao gate.

### M4. A taxonomia da série muda sem mapa explícito (média)
**Onde:** "Dois motores rivais" ("dois dos três motores são o mesmo"), "De onde vem o e" ("É o
motor contínuo."), "Mesma curva" ("uma curva do motor contínuo"). Eram três motores e passam a
ser dois (linear e exponencial) com três etiquetas, mas isso nunca é dito, e "motor contínuo"
continua sendo usado como coisa à parte. O "aviso de vocabulário" resolve "exponencial", não
"motor". Trocar as ocorrências é tarefa da etapa 6. O que falta é o mapa.

### M5. A "hipótese escondida" é anunciada e não é usada (média)
**Onde:** "De onde vem o e", a partir de "Há outro caminho até a mesma fórmula, e ele mostra a
hipótese escondida". O texto enuncia a hipótese ("nenhum centavo fica parado (…) tudo é
reinvestido à mesma taxa") e segue sem tirar consequência dela. O texto anterior já dizia que "o
composto supõe que ele é reinvestido à mesma taxa". A ponte que serviria à tese: é a mesma
hipótese em granularidade diferente, logo é o mesmo motor. Ligar ou cortar antes da etapa 6.

### M6. A competência "avaliar" é mostrada numa taxa e num prazo só (média)
**Onde:** "Rende todo dia" e o bloco de decisão da Prateleira. A Ficha pede "para a taxa e o
prazo em jogo", mas tudo está a 14% e em um ano. A ressalva "a taxas da ordem do DI" aponta para um
contraexemplo que o leitor não vê. A regra de bolso não diz que a distância cresce com o quadrado
da taxa (`03-pesquisa.md`, contraponto 2). A pesquisa já tem o vizinho: o rotativo do cartão,
451,7% a.a. em set/2026.

### M7. O lado de quem paga some no caso mais caro (média)
**Onde:** "Onde mora o erro" ("De um lado do balcão, a tesouraria (…) Do outro, a mesa"). Os
"lados" aqui são uma passagem interna da instituição. O texto não diz quem carrega os 103 pb (quem
compra a call cara, quem vende a put barata, o que isso significa na marcação). Nos outros casos
o lado de quem paga existe (o tomador, o investidor). Lembrete: não há caso real documentado de
"DI usado direto como r", e o texto não deve afirmar que o erro é comum.

### M8. O parágrafo da LTN sai do assunto no fim da Prateleira (média)
**Onde:** de "No mercado, até a precisão é cláusula" até o bloco `PU da LTN`. Traz tema novo
(truncamento), sigla nova e código novo no ponto de consolidar, e prepara uma comparação que não
faz ("compare essa distância com a precisão de que você precisa"). Saídas: ligar à competência
"avaliar" (M6) ou cortar. Disputa a função "é cláusula" com a Súmula 541 (B6), e cabe um dos dois.

### B1. O custo da volta do movimento 4 (baixa)
A metade "mais preciso" do mito espera cerca de 800 palavras para ser refutada, e a refutação
("A escolha é de conveniência, não de precisão") fica colada a uma atribuição ao Hull com
`[VERIFICAR]`. A refutação já acontece em "Mesma curva" ("Não é uma aproximação. É uma
identidade."), mas sem ligação ao mito. Para a etapa 6: "Na seção anterior", em "Onde mora o
erro", aponta para dois blocos atrás.

### B2. A frase-sinal vem depois do trecho mais técnico (baixa)
O aviso de passagem do raso para o profundo chega logo depois da expansão binomial, o trecho mais
difícil até ali. A decisão de manter o binômio é do autor. Fica o registro sobre a posição da
frase-sinal.

### B3. O aviso de vocabulário cita o manual antes de apresentá-lo (baixa)
A prova mais forte ("exponencial" nos dois sentidos na mesma página do manual) mora na seção da
mesa. Funciona onde está.

### B4. Sobreposição sem remissão nas conveniências 1 e 2 (baixa)
Elas ampliam a frase de "A Corda e o Arco" ("torna os retornos aditivos no tempo (…) e deixa o
cálculo diferencial trabalhar") sem remeter a ela. O graf-02 repetir os números do fecho anterior
é esperado. Lateral: o texto anterior cita a "desigualdade de Bernoulli", do mesmo Jacob. Pode ser
ponte ou ruído, decisão do gate.

### B5. O teste de transferência é curto (baixa)
Tem a mesma forma da conta da abertura e exercita só "converter". Fica como observação.

### B6. Súmula 541: onde cabe (baixa; opcional, gate)
Na Prateleira, junto de "Se uma das taxas é nominal e a outra efetiva". Responde no plano jurídico
"qual dos dois números você de fato paga?" e conversa com o teste de transferência do texto
anterior. Não cabe na abertura. Se entrar, substitui a LTN no papel de "é cláusula" (M8). Vai no
corpo, com número, e não na bibliografia (§5.7).

### B7. Itens com autoridade frágil ou fora do argumento central (baixa)
O Hull: se o `[VERIFICAR]` cair, a frase de conclusão fica de pé sozinha. A conveniência 3 trata
de volatilidade, não da etiqueta, e tem atribuição ressalvada. A conveniência 1 introduz "taxa a
termo", que não volta. São candidatos a enxugar.

### B8. A regra de bolso aparece duas vezes (baixa)
Repetir como ferramenta é legítimo. O alcance (vale para m grande) é assunto da etapa 7.

### B9. O título da seção afirma mais do que ela mostra (baixa)
"Rende todo dia não é render mais": a seção mostra que rende pouco a mais na nominal e que, na
efetiva, isso já está no preço. Os 14% trocam de etiqueta três vezes na seção com uma só
sinalização.

### B10. O distribuidor aparece de passagem (baixa)
Tem consequência ("a frequência já foi paga"), então passa no §4.3.

## Veredito

Pronto para revisão de linha, sem volta à etapa 2. Antes da etapa 6, levar ao autor M5 (o
parágrafo da hipótese) e M8 com B6 (LTN ou Súmula 541), para não revisar frase de parágrafo que
pode sair. M2, M4, M6 e M7 são acréscimos pontuais de ligação.
