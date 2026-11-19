# Etapa 5: Crítica estrutural

Executor: subagente `critico-editorial`. Texto criticado: o corpo de `processo/04-draft-v1.md`, a
partir de "# Cara, eu ganho. Coroa, eu não perco.", lido junto com as notas laterais da etapa 4.
Também lidos: `01-briefing.md`, `02-estrutura.md`, `03-pesquisa.md`, `00-leitura.md` (o rascunho
original, para comparar a abertura), `docs/BACKWARDS_DESIGN.md` §3 a §6, `estilo/estilo-autoral.md`
§4, `pesquisa/frente-c-editoracao.md` e `.claude/agents/references/tecnicas-narrativas.md`.

Linha **Notas de um Professor**, tipo conceito de finanças, sem a validação argumentativa da linha
Spoiler. Não reabri as decisões do autor no rascunho: títulos, *bootstrapping*, exemplo
estilizado, Black-Scholes só como menção, movimentos 6 e 7 fora. O laudo diagnostica e não
reescreve.

## Resumo

O argumento se sustenta. A tese ("Preço não é opinião. É o custo da réplica.") está no subtítulo,
aparece isolada no Mito e volta no fecho. A abertura não começa pela metodologia: o modo B chega à
pergunta-âncora, e o texto responde a ela. A Ficha de Saída é entregue: a réplica, na tabela de "Uma
NTN-F feita de LTNs"; o preço pela Lei do Preço Único; a classificação, pelo critério do vencimento
e pelas três perguntas. O teste da NTN-B está equipado. A voz ensaística em registro técnico é estável
do começo ao fim e não se mistura com outra. Os três pilares estão presentes:
- dado: contas próprias declaradas, Shleifer e Vishny, o Nobel de 1997, a metodologia da ANBIMA;
- narrativa: a moeda, o ganha-ganha em duas camadas, o LTCM;
- visual: diag-01 e diag-02.

O achado central não está enterrado: o subtítulo o carrega, e a pergunta-critério tem parágrafo
próprio.

**Nenhum achado de severidade alta.** São 6 médios e 8 baixos. Os médios são de ligação e de lastro:
- o fio do desmembramento, o elo com menos fonte do texto, que a etapa 4 deixou no meio da abertura;
- o refrão, aplicado a uma operação que ele não descreve;
- a segunda metade do Mito, refutada sem a tese;
- o atrito de capital, anunciado e não listado;
- um dado de conjuntura.

## Respostas às observações da etapa 2 e aos alertas do briefing

**As duas metades do Mito, respondidas longe uma da outra.** A distância é de cerca de 1.500
palavras, com três H2 e cinco H3, e não exige memória do leitor. "Volte à segunda metade do mito"
repete a metade inteira, e a ordem Mito → Anatomia → Lado de Lá → Ponto Cego é a do §3. A definição
de "A aposta que não sobrevive" ("nunca dá prejuízo no futuro") ainda entrega a ferramenta antes da
refutação. O custo real está em outro lugar: a segunda metade é refutada sem a palavra da tese
(item 4).

**O desvio por Black-Scholes no meio do movimento 4.** Compensa. São cerca de 170 palavras, e elas
fazem três coisas:
- pagam a promessa explícita do Mito ("com mais matemática, a fórmula de Black-Scholes");
- trazem a prova mais visível da tese: o retorno esperado não aparece na fórmula;
- terminam na distinção entre réplica estática e réplica dinâmica, de que depende o critério do
  vencimento da seção 5.

O que sobra no desvio está no item 8.

**A abertura com cerca de 14 parágrafos curtos.** Depois da etapa 4, são 11 parágrafos e cerca de
300 palavras. Em extensão, isso equivale aos 3 a 6 parágrafos do §3, e o parágrafo curto é da voz
(§5.4). O tamanho não cansa o leitor antes da pergunta-âncora. O ponto em que ele pode desistir está
na composição, não no tamanho: os dois parágrafos do desmembramento, que a etapa 4 criou a partir de
um só (item 1).

**O refrão da moeda quatro vezes.** Ele carrega o argumento em três ocorrências: a aposta na
abertura, a definição e o fecho, que absorve o movimento 7. Vira cadência em uma, a de "A moeda
aparece" (item 3).

**A passagem dos títulos reais ao exemplo estilizado.** O texto marca cada passo: "troque 2029 por
um ano", "suponha", "hipotética", "ilustrativas". A LTN da prova (R$ 874,89) volta como o vértice de
252 du da réplica, o que ajuda o leitor. Ficam dois pontos em que o real e o estilizado se misturam
(item 7).

**"Fica para decisão posterior" (notas laterais da etapa 4).**
- *Caso real de 11/11:* a estrutura não o exige. Se entrar, o lugar é "Os limites da arbitragem de
  verdade", não "A mesma conta, todo dia" (item 10).
- *Falta de capital como atrito (TIPS × Treasury):* o exemplo não faz falta, mas a lacuna que ele
  aponta é real (item 5).
- *Daves e Ehrhardt sobre "a mesma promessa":* a frase está certa em fluxo. Se houver ressalva, ela é
  estrutural de "Os limites", não da abertura (item 9).
- *Vencimento em feriado:* não tem efeito na estrutura. A LTN e a NTN-F liquidam no mesmo dia útil,
  e "mesma data" continua valendo. Fica com a etapa 7.

**Alerta do briefing sobre a definição de arbitragem (forma 1).** O lado técnico é da etapa 7; o
lado estrutural é o item 3.

## Achados

### 1. Abertura: os parágrafos do desmembramento são o ponto de desistência (média)

**Onde:** abertura, "No Selic (o sistema do Banco Central…)" e "Desmembrados, o principal e cada
cupom…", entre o caso concreto e "Separados, o principal da NTN-F 2029 e a LTN 2029 são a mesma
promessa".

**Diagnóstico:** são os únicos dois parágrafos da abertura que não fazem a tensão avançar, e trazem
uma norma que o argumento não usa (Res. BCB 55/2020, art. 45) mais uma condição ("quando a emissão
prevê essa faculdade") que lança sobre o título do próprio caso uma dúvida que o texto nunca resolve.

**Base:** a sequência série → moeda → caso → pergunta-âncora corre sem atrito até "Agora, um caso
concreto". Dois parágrafos antes da pergunta, o leitor passa da aposta para a regulação. No rascunho
era um parágrafo só, que afirmava direto ("a NTN-F pode ser desmembrada"). A etapa 4 (nota lateral 4)
trocou esse parágrafo por dois, com a norma, a condição e o `[VERIFICAR]`. Citar o número de uma
norma no corpo é o padrão que o autor corta no site («(Resolução nº 5.295…)»,
dividir-para-nao-correr-risco).

### 2. O fio do desmembramento tem o menor lastro do texto e sustenta três pontos (média)

**Onde:**
- a abertura: os parágrafos do item 1 e "Separados…";
- "A prova cabe numa LTN": "o principal desmembrado de uma NTN-F";
- o primeiro parágrafo de "A mesma conta, todo dia": "ela existe fisicamente: é o desmembramento da
  abertura".

**Diagnóstico:** o caso concreto da abertura, o par usado na prova e o argumento de que "o mercado
leva essa decomposição a sério" dependem de um fato sem fonte oficial, e a pesquisa contraria a
inferência de "A mesma conta".

**Base:**
- Fonte (`03-pesquisa.md`, item 4): o fato só tem o Mais Retorno, com campos contraditórios. O
  Relatório do Selic de 2025 cita o desmembramento da NTN-B e não fala da NTN-F nesse ponto. O
  Comunicado 7.588 foi revogado, segundo fonte secundária.
- Inferência (item 32): Grinblatt e Longstaff (2000) concluem que, nos EUA, o *stripping* atende
  sobretudo à demanda por zeros e a assimetrias fiscais e contábeis, e acham pouca evidência de uso
  para arbitragem. É o contrário do que "leva tão a sério que existe fisicamente" deduz.
- Alcance: o exemplo estilizado do miolo (NTN-F × três LTNs) não depende do desmembramento. Só
  dependem dele a abertura, a prova e esse parágrafo.
- Ordem das etapas: se a etapa 7 não fechar o `[VERIFICAR]`, o "caso concreto" vira hipotético, e a
  abertura muda de estrutura. Como a etapa 7 roda depois da 6, a decisão precisa ir ao autor antes
  da revisão de linha, para não se polir frase de parágrafo que pode mudar.

### 3. O refrão descreve a forma 2, e as duas contas do texto são da forma 1 (média)

**Onde:** abertura ("Se der cara, você ganha. Se der coroa, você não perde nada. E não paga para
entrar."), "A aposta que não sobrevive" (o refrão logo depois das duas formas) e "A moeda aparece"
("Cara, a mesa ganha. Coroa, não perde.").

**Diagnóstico:** a imagem central do título, da abertura e da definição é a aposta que não custa
nada e ganha em algum cenário, mas as duas contas do texto são dinheiro hoje sem cenário a sortear,
e na terceira ocorrência o refrão nomeia uma operação que ele não descreve.

**Base:**
- As contas: na prova, R$ 4,89 hoje ("É a primeira forma de arbitragem"); na NTN-F, R$ 20.307,28
  travados. Nenhuma conta do texto mostra a forma 2.
- A terceira ocorrência é cadência: o parágrafo já deu o resultado. A frase que vem antes do refrão
  ("os cupons e o principal da NTN-F pagam as LTNs vendidas") chega logo depois da sobra de
  R$ 115,18 por data. A precisão é da etapa 7.
- A ligação com o briefing: é a mesma costura do alerta sobre a definição geral, que descreve mal a
  forma 1. Se a etapa 7 mexer na definição, o refrão, que vem logo depois das duas formas, precisa
  continuar fazendo sentido ali.
- As ocorrências 1, 2 e 4 carregam o argumento.

### 4. A segunda metade do Mito é refutada sem a tese (média)

**Onde:** "A taxa não manda no preço" ("As duas metades erram pelo mesmo motivo: tratam o preço
como opinião." e "Essa frase basta para tirar…") × "Nem toda convergência é arbitragem".

**Diagnóstico:** o Mito promete que as duas metades erram pelo mesmo motivo, mas a seção que refuta
a segunda nunca liga a correlação à opinião nem usa a palavra "réplica", e o texto corre o risco de
ser lido como duas aulas unidas pela palavra "arbitragem".

**Base:**
- A palavra: "réplica" não aparece em "Nem toda convergência é arbitragem" e só volta em "Os
  limites". O contraste é dado como "identidade × estatística", e o elo com a tese fica por conta do
  leitor: PETR4 não é réplica de PETR3, e apostar na volta à média é ter opinião sobre o preço.
- As promessas: a lista do Mito ("Essa frase basta para tirar…") tem o VP, a NTN-F e Black-Scholes, e
  não tem o critério. A pergunta-âncora também cobre só a primeira metade.
- O peso: é justamente a metade em que o funil e o CTA final apostam ("separar arbitragem de
  aposta").
- O contraste: a primeira metade se fecha com a tese em mãos ("A TIR sai do preço, e não o
  contrário.").

### 5. "Os limites" anuncia capital e lista só custos, e o critério do vencimento põe de lado o mecanismo de Shleifer e Vishny (média)

**Onde:**
- "Os limites da arbitragem de verdade": a abertura com Shleifer e Vishny e os três atritos;
- "Nem toda convergência é arbitragem": "O marca a mercado pode doer no meio do caminho, mas…" e, no
  LTCM, "o fundo não teve capital para esperar";
- "Antes de chamar de arbitragem": "Qualquer não: é outra coisa. Pode até ser uma boa operação, mas
  tem risco";
- a nota de Shleifer e Vishny em "Para continuar aprendendo".

**Diagnóstico:** a fonte-âncora da seção diz que a arbitragem de verdade exige capital e corre
risco, mas nenhum dos três atritos é capital ou marcação antes do vencimento, o único caso de falta
de capital (o LTCM) fica atribuído à confusão com a correlação, e a Prateleira dá a entender que três
"sim" significam uma operação sem risco.

**Base:**
- A nota bibliográfica promete o que o corpo não entrega: "pode falhar justo quando os preços mais se
  afastam do valor".
- A pergunta 3 ("quanto custa sustentar a posição até o vencimento? … a margem") cobre parte disso,
  mas como custo, não como o risco de ter de desmontar antes.
- Em "A moeda aparece", "pequena, rápida e disputada" é onde o contraponto da pesquisa pesa (item 31:
  TIPS × Treasury, réplica exata com desvio de mais de US$ 20 por US$ 100 durante meses, que só
  estreita quando entra capital).
- O exemplo não faz falta. O que falta é a ligação entre a fonte-âncora e a lista.
- A classificação arbitragem × correlação continua certa, por isso o achado não é alto.

### 6. A Selic e a reunião do Copom são conjuntura num texto sobre o mecanismo (média)

**Onde:** "Uma NTN-F feita de LTNs", "com a Selic em 13,75%, mantida pelo Copom na reunião de 4 de
novembro".

**Diagnóstico:** a oração não serve ao argumento, porque a Selic não volta no texto e o realismo das
taxas já está ancorado em "na ordem de grandeza da curva prefixada de novembro de 2026", expressão que
a prova também usa.

**Base:** é o padrão de corte do autor para dado de conjuntura em texto sobre mecanismo («a taxa
média da LCA de 12 meses caiu…», o-agro-e-pop). A oração vem do rascunho. Foi ela que trouxe o erro
de data que a etapa 4 corrigiu com a pesquisa.

### 7. Real × estilizado: dois pontos de mistura (baixa)

**Onde:**
- "Os limites da arbitragem de verdade": "Na NTN-F do exemplo, três atritos aparecem", atrito 3;
- "Uma NTN-F feita de LTNs": "Os fluxos são R$ 48,81, R$ 48,81 e R$ 1.048,81…", contra os
  "R$ 1.048,80" da abertura.

**Diagnóstico:** o texto atribui o atrito 3 ("Nem toda data tem LTN") à NTN-F do exemplo, montada
justamente supondo "três LTNs vencendo exatamente nessas datas", e o aviso "sem os truncamentos da
metodologia do Tesouro" só chega depois do fluxo de R$ 1.048,81, preso ao PU, quando a abertura já deu
R$ 1.048,80 para o mesmo último pagamento.

**Base:** o atrito 3 vale para o mercado (pesquisa, item 22), não para o exemplo. O segundo ponto
nasceu da nota lateral 3 da etapa 4, e o número final é da etapa 7.

### 8. Black-Scholes: o desvio compensa, com duas sobras (baixa)

**Onde:** "A mesma ideia, com mais matemática".

**Diagnóstico:** a quebra de ritmo se paga (ver as respostas acima), mas o detalhe de que Black não
recebeu o prêmio póstumo não tem função no argumento, e a réplica dinâmica aparece como arbitragem
pura ("Senão, alguém compra uma, vende a outra e embolsa a diferença"), sem a hipótese de modelo que o
próprio critério da seção 5, a identidade de fluxos em todo cenário, cobraria.

**Base:**
- "Daqui em diante, o texto fica na renda fixa, onde a réplica é estática" marca a diferença, mas não
  diz o que a réplica dinâmica perde. O fecho generaliza assim mesmo: "uma opção custa o que custa a
  carteira que a imita".
- Há uma ligação disponível e não usada. Merton e Scholes, premiados aqui, eram sócios do LTCM, que a
  seção 5 apresenta como o caso mais caro da confusão, e o post da série já conta isso
  (`01-briefing.md`, continuidade). A ligação reforçaria que o erro-alvo (b) é crença de gente
  competente (§6, checklist).
- A decisão "só menção" fica de pé.

### 9. Daves e Ehrhardt: "a mesma promessa" vale para o fluxo, não para os direitos (baixa)

**Onde:** abertura ("Separados, o principal da NTN-F 2029 e a LTN 2029 são a mesma promessa." e "Se
uma das duas estiver mais barata que a outra, a moeda da aposta acabou de aparecer.") e "A prova cabe
numa LTN".

**Diagnóstico:** o principal desmembrado reconstitui o título junto com os cupons e a LTN não, e a
literatura mostra pares assim negociando com diferença sistemática (pesquisa, item 32), uma diferença
que a pergunta 1 da Prateleira ("Os fluxos são idênticos, nas mesmas datas?") não pega e que nenhum
dos três atritos nomeia.

**Base:**
- "Mesmo devedor, mesmo valor, mesma data" está certo. O que vai além da literatura é a frase
  seguinte, que trata qualquer diferença como a moeda. "Os limites" corrige em termos gerais ("são o
  preço desses atritos"), por isso o achado é baixo.
- Se houver ressalva, o lugar estrutural é "Os limites", não a abertura, onde ela esvaziaria o
  gancho.
- O leitor que seguir Tuckman e Serrat ("com os títulos e os *STRIPS*") chega ao mercado em que essa
  diferença é estudada.
- Depende do item 2: se o par sair da abertura, este item cai junto.

### 10. O caso real de 11/11 não é exigido; se entrar, o lugar é "Os limites" (baixa)

**Onde:** nota lateral da etapa 4 ("pode virar uma frase em 'A mesma conta, todo dia'") e pesquisa,
item 34.

**Diagnóstico:** o texto não precisa do caso, porque o pilar do dado está atendido e o exemplo
estilizado é decisão do autor, mas, se ele entrar, pertence a "Os limites da arbitragem de verdade",
onde é o único exemplo da pesquisa com os atritos 1 e 3 num título que existe, e não a "A mesma conta",
onde mostraria um desvio antes de o texto ter os atritos que o explicam.

**Base:**
- A NTN-F 2029 sai R$ 0,81 acima da réplica, no sentido oposto ao do *dealer* do exemplo.
- Explorar o desvio exige vender a NTN-F a descoberto (atrito 1). A data de 1º/1/2027 não tem LTN, e
  a pesquisa usou no lugar o último fluxo da NTN-F 2027 (atrito 3).
- Os preços são indicativos, não executáveis.
- O número envelhece, como o autor previu ao escolher o estilizado.
- Vai ao gate depois do recálculo da etapa 7.

### 11. A pergunta "e para quem?" fica sem resposta na seção que a faz (baixa)

**Onde:** abertura de "Preço sem opinião" ("Que problema esse princípio resolve, e para quem?").

**Diagnóstico:** a seção responde "que problema" (precificar sem conhecer as preferências) e não
responde "para quem", uma resposta que o texto dá antes, em "Quem paga o ganha-ganha" (quem compra
NTN-F, quem marca a mercado, o Tesouro), e depois, com a ANBIMA de "A mesma conta".

### 12. A ponte para o *bootstrapping* promete o que este texto já mostrou (baixa)

**Onde:** fecho, "é nele que fica claro por que a TIR de uma NTN-F e a taxa *spot* do mesmo prazo
são objetos diferentes".

**Diagnóstico:** a diferença entre a TIR e a taxa *spot* do mesmo prazo já foi mostrada e explicada
aqui, com os 14,53% × 14,55% e a inclinação da curva em "Uma NTN-F feita de LTNs" e com o erro do
*dealer* na Prateleira, de modo que o gancho do próximo texto chega gasto.

**Base:** o "vértice por vértice" da mesma ponte é novidade de fato. A promessa dupla (*bootstrapping*
e trading de correlação) já tem a aprovação do autor e está registrada no briefing para o gate. Não a
reabri.

### 13. PETR3 × PETR4: a razão contestável vem antes da decisiva (baixa)

**Onde:** "Nem toda convergência é arbitragem": "Mas não pagam o mesmo fluxo: a ordinária dá direito
a voto, a preferencial dá prioridade no dividendo" e, três parágrafos depois, "Não existe data em que
as duas pontas sejam obrigadas a se encontrar".

**Diagnóstico:** o contraste abre pela diferença de fluxo, justamente a que o contraponto da pesquisa
enfraquece (acima do mínimo, as duas classes recebem o mesmo dividendo, e a PN tem *tag along*
integral; item 18), e só depois do critério chega à razão que fecha a questão: não há vencimento em
que as duas pontas se encontrem.

**Base:** a conclusão da seção continua valendo. A precisão sobre o estatuto é da etapa 7.

### 14. O Tesouro aparece só como beneficiário (baixa)

**Onde:** "Quem paga o ganha-ganha" ("o próprio Tesouro, que leiloa LTN e NTN-F toda semana…").

**Diagnóstico:** o lado de quem emite passa no checklist (§6) pela via do tipo conceito, que
responde que problema o princípio resolve e quem o criou (Black, Scholes e Merton), mas o emissor real
só aparece de passagem, e a pesquisa traz um caso do Tesouro agindo como parte interessada em preços
coerentes (item 35: cancelamento dos leilões e recompra de NTN-F na semana de 26/10/2026).

**Base:** não bloqueia. Acrescentar seria parágrafo novo, então é pergunta de gate, não de
estrutura.

---

**Veredito:** pronto para revisão de linha, sem volta à etapa 2; antes da etapa 6, levar ao autor os itens 1 e 2 (os parágrafos do desmembramento podem mudar ou sair), e tratar os itens 3 a 6, cortes e ligações pontuais, na mesma passada.
