# Crítica estrutural — O Papel do CDB na Transformação de Prazos

*Laudo do agente `critico-editorial`, etapa 5 do pipeline. Diagnóstico, não reescrita.*

## Resumo no topo — severidade alta encontrada

O draft tem **um problema de severidade alta na própria seção-gancho** (contradição entre o
que o subtítulo promete e o que o parágrafo entrega) e **um problema de severidade média-alta
na tese** (uma das três pernas do argumento — "como é remunerado" — é afirmada no fechamento,
mas nunca demonstrada no corpo). Ver itens 1 e 3 abaixo. O restante do draft é sólido:
estrutura, dados, pilares e voz explicativa estão majoritariamente bem executados.

## Laudo item a item

### 1. Gancho (seção 1) — título contradiz o próprio parágrafo de abertura
**Localização:** H2 "O dinheiro que você não pode usar, e o banco também não" + primeira
frase do corpo.
**Diagnóstico:** o subtítulo promete que "você" (o titular) não pode usar o dinheiro. A
primeira frase do corpo diz o oposto: "o titular pode sacar a qualquer momento" — quem não
pode usar livremente é só o banco. O subtítulo e o corpo do parágrafo fazem afirmações
opostas sobre o mesmo sujeito ("você"). Um leitor atento para no primeiro parágrafo
justamente por essa incoerência — é a pior posição possível para um erro desse tipo, porque é
a primeira frase do post inteiro.
**Severidade:** alta.

### 2. Gancho — frase categórica que a pesquisa recomendou explicitamente evitar
**Localização:** primeira frase da seção 1 ("...e o banco não pode livremente aplicar esse
saldo em outra operação").
**Diagnóstico:** `03-pesquisa.md` (item VERIFICAR 1) já sinalizou este ponto exato e
recomendou não usar a formulação categórica "o banco não pode usar" sem qualificação, e sim
"o banco pode usar uma fração menor, sob regras diferentes". O draft mantém a formulação
categórica na primeira leitura, e só a qualifica duas frases depois com os números reais (21%
vs. 20%). Tecnicamente o dado que vem a seguir resolve a imprecisão, mas a primeira impressão
do leitor — e a citação isolada da frase, se algum leitor a compartilhar — carrega o overclaim
que a própria pesquisa pediu para evitar.
**Severidade:** média (mitigada pela correção dois períodos depois, mas ainda no parágrafo de
abertura do post inteiro).

### 3. Tese — a perna "como é remunerado" é afirmada, não demonstrada
**Localização:** fechamento da seção 6, comparado ao corpo das seções 3-5.
**Diagnóstico:** a tese do briefing tem três pernas explícitas: por que o CDB existe, como é
remunerado, por que é regulado de perto. As seções 3 (ALM) e 5 (compulsório/LCR/NSFR)
demonstram com mecanismo as pernas "existência" e "regulação" — inclusive com uma citação
primária forte do Bacen ("transformação de maturidade"). A perna "remuneração" nunca é
conectada explicitamente à transformação de prazos em nenhuma seção intermediária: a seção 4
explica CDI/indexador como mecânica de remuneração, mas não amarra isso ao argumento de
ALM/funding; a seção 3 menciona "spread bancário" de passagem, sem desenvolver. O resultado é
que a frase final ("essa função... é o que explica por que existe, como é remunerado e por que
é tão de perto regulado") afirma algo que o corpo do texto não constrói para a parte da
remuneração.
**Severidade:** média-alta — não exige necessariamente voltar à etapa 2 (a lacuna cabe como
parágrafo adicional dentro de uma seção já existente, provavelmente 3 ou 5), mas o pipeline
principal deve decidir se resolve isso ainda na etapa 4 (redraft) ou se volta à estrutura.

### 4. Metáfora "do outro lado do balcão" é retomada, contra a regra da voz explicativa
**Localização:** título da seção 3 ("O outro lado do balcão...") e penúltima frase da seção 6
("a mesma transformação de prazo que, do outro lado do balcão, permite ao banco...").
**Diagnóstico:** `estilo-autoral.md` §4.2 é explícito: na voz explicativa, "a única figura por
texto (se houver) não é retomada." O draft usa a mesma imagem duas vezes, em seções
diferentes.
**Severidade:** média.

### 5. Fechamento da seção 6 — salto de registro figurativo no clímax do argumento
**Localização:** últimas duas frases da seção 6 ("...não é um produto entre outros na
prateleira da renda fixa. É a peça pela qual o sistema bancário converte...").
**Diagnóstico:** o texto é rigorosamente literal do início ao fim (compulsório, FGC, ALM, CDI,
LCR/NSFR) — a única concessão figurativa prevista era "do outro lado do balcão". Nas duas
frases finais aparecem, além da retomada do "balcão", duas imagens novas nunca usadas antes
("prateleira", "peça"). É o ponto do texto onde a voz mais se aproxima do registro ensaístico
(figura de linguagem acumulada para fechar com impacto), destoando do resto do post, que é
categórico e plano. Isso não é reescrita de frase — é um padrão estrutural (acúmulo de figuras
justamente no parágrafo de resolução) que vale a pena a etapa de redraft resolver.
**Severidade:** média.

### 6. Achado mais forte do post (citação primária do Bacen) está enterrado na seção 3
**Localização:** meio do terceiro parágrafo da seção 3 ("O Banco Central usa... transformação
de maturidade...").
**Diagnóstico:** `03-pesquisa.md` já identificou esta citação como "achado mais forte, fonte
primária" — é a evidência mais forte de todo o post porque mostra que "transformação de
prazos" não é enquadramento do autor, é linguagem oficial do Bacen. No draft, ela aparece como
a terceira frase de um parágrafo no meio do texto, sem destaque de subtítulo ou posição de
abertura de seção. Não chega a ser "insight enterrado" no sentido crítico de contradizer a
estrutura planejada — a sequência gancho→contexto→clímax foi deliberada na etapa 2 — mas dado
o peso probatório da citação, vale considerar dar a ela mais protagonismo (por exemplo, abrindo
a seção 3 com ela, em vez de chegar só no terceiro parágrafo).
**Severidade:** média (não é motivo isolado para forçar retorno à etapa 2, mas é uma
oportunidade de reordenação dentro da seção 3 que fortalece a tese sem alterar o arco geral).

### 7. "Todo mês" na abertura — periodicidade não sustentada por `03-pesquisa.md`
**Localização:** primeira frase da seção 1 ("Todo mês, uma parte do dinheiro...").
**Diagnóstico:** nenhuma fonte em `03-pesquisa.md` menciona periodicidade mensal para o
cálculo/apuração do compulsório — é um detalhe que parece ter sido inserido no draft sem
lastro na pesquisa. Pode ser impreciso (o cálculo de exigibilidade do compulsório no Brasil
tipicamente segue períodos quinzenais, não mensais). Isto é mais adequado à verificação
técnica (etapa 7) do que a este laudo, mas registro aqui porque nasce na abertura do texto.
**Severidade:** baixa — sinalizar para etapa 7 confirmar ou remover a referência temporal.

### 8. Ressalva do FGC — bem calibrada (confirmação positiva)
**Localização:** final da seção 2 ("A cobertura reduz o risco... mas não elimina fricção
prática...").
**Diagnóstico:** a ressalva pedida por `03-pesquisa.md` (Banco Master como contraponto
genuíno, sem precisar nomear o caso) está bem executada: qualifica sem alarmismo ("leva
tempo", "valor acima do teto não é recuperado") e evita a armadilha de soar como "CDB com FGC
é livre de risco". Não nomear o Master é decisão editorial válida dado que é caso sob litígio.
Nenhum ajuste necessário aqui.
**Severidade:** nenhuma (observação positiva).

### 9. Voz explicativa — aderência geral
**Diagnóstico:** terceira pessoa quase absoluta, sem humor, sem CTA de fechamento, sem
primeira pessoa — todos presentes corretamente. A admissão de incerteza do áudio sobre
proporção de CDBs atrelados ao CDI foi corretamente convertida em afirmação qualitativa ("é
comum, embora não universal") na seção 4, seguindo exatamente a recomendação de
`03-pesquisa.md`. Os únicos resíduos de registro não-explicativo são os itens 4 e 5 acima
(acúmulo de figuras de linguagem).
**Severidade:** média (soma dos itens 4 e 5, já contabilizados acima; não há item novo aqui).

### 10. Três pilares (dado, narrativa, visual)
**Diagnóstico:** presentes e equilibrados. Dado: compulsório (21%/20%), FGC (R$250 mil/R$1 mi
a cada 4 anos), LCR/NSFR com números de resolução. Narrativa: a jornada
depositante→CDB→banco→crédito via ALM, nas seções 1, 3 e 5. Visual: `ilu-01` e `graf-01`
posicionados como fechamento informacional de seção, não decoração. Nenhuma seção é só
narrativa sem dado, nem só dado sem sentido.
**Severidade:** nenhuma.

### 11. Abertura por cálculo vs. abertura por significado
**Diagnóstico:** nenhuma seção abre explicando metodologia/cálculo antes do achado — a regra 1
do guia (glosa no primeiro uso) é seguida consistentemente (compulsório é definido antes do
número; ALM é definido antes do detalhe; LCR/NSFR definidos antes das resoluções).
**Severidade:** nenhuma.

## Veredito

O texto **não está pronto para revisão de linha**. Precisa de mais uma passagem pela etapa de
draft (no mínimo) para resolver o item 1 (contradição título/corpo do gancho, severidade alta)
e o item 3 (perna "remuneração" da tese não demonstrada, severidade média-alta) antes de
seguir para revisão de linha/norma. Os itens 4-6 (metáforas retomadas, salto de registro no
fechamento, reposicionamento da citação do Bacen) podem ser resolvidos na mesma passagem de
redraft, sem necessidade de reabrir a etapa 2 de estrutura — a ordem e a seleção de seções
seguem sustentáveis.

## Decisão do pipeline principal

Severidade alta encontrada, mas localizada na execução do draft (contradição de frase, perna
de tese não desenvolvida), não na seleção/ordem de seções — o próprio laudo (itens 9-11)
confirma estrutura, pilares e sequência sustentáveis. Decisão: revisar `04-draft-v1.md`
(etapa 4) incorporando os itens 1, 3, 4, 5 e 6, sem reabrir a etapa 2. Isso não consome loop
de revisão (`loops_consumidos` é contado a partir de reentradas pós-gate-humano, etapa 10) —
é still a primeira passagem do pipeline.
