# Etapa 0 — Leitura do rascunho

Fonte: `_arquivo/drafts/2026-10-27_Samurais_e_Duelos_no_Mercado_Financeiro.md` (intocado, cópia de trabalho abaixo; commitado em `main` em `53ea484`).

**Linha editorial:** Spoiler (confirmada pelo autor na etapa 0, 2026-10-26). O rascunho não
traz front-matter YAML; o corpo diz "a série Spoiler volta" e "Esta série existe por uma
ideia", mas a regra é perguntar, não inferir. Consequência: etapa 5 inclui validação
argumentativa e a etapa 5a (`revisor-quant`) roda.

**Título:** "Samurais e duelos no Mercado Financeiro" (H1 do rascunho, confirmado pelo autor
na etapa 0). O título de e-mail das notas ("O que um samurai do século 17 sabe sobre sua
carreira em finanças que o Hábitos Atômicos não te conta") fica como `assunto_email` na
etapa 9. Slug: `2026-10-27-samurais-e-duelos`.

**Natureza do rascunho:** já chega em "rodada 2". O corpo está completo: abertura sem
intertítulo, Wall Street, aviso de leitura, cinco anéis, fechamento, tabela-síntese e
referências. Depois vem um apêndice "Notas de revisão (remover antes de publicar)", escrito
como perguntas de uma rodada anterior ao autor (6 perguntas, 7 correções, SEO, 2 ideias de
gráfico), e uma última linha solta do próprio autor pedindo um exemplo sobre as eleições.
**As notas estão defasadas em relação ao corpo** em três pontos, detalhados no inventário:
o H1 não é o título de e-mail que as notas dizem estar "usado no H1"; o primeiro intertítulo
está vazio (`## `), e não com a "Nota do Substack" que as notas dizem estar ali; e os dois
`[INSERIR]` que a pergunta 3 cita não existem mais no corpo.

**Limpeza aplicada na cópia** (artefatos de exportação, não mudança de texto):
- 26 ocorrências de `&#32;` (espaço codificado em HTML, no fim ou no início de linha)
  removidas.
- Palavra partida na linha 22–24 do original ("…escolas adversárias fracas. S" / linha em
  branco / "ó perto dos 50…"): unida em "Só perto dos 50…", no mesmo parágrafo. A quebra de
  parágrafo ali pode ter sido intencional, já que o rascunho usa muitas frases isoladas; a
  etapa 6 pode reabrir isso.
- O resto da prosa está verbatim (linhas 1–199 do original), inclusive erros de digitação
  ("estagnição", "pudessemos", "semlhante") e o intertítulo vazio. Correção de norma é da
  etapa 6, decisão de intertítulo é da etapa 1/2.

**Observações de formato para etapas posteriores** (não são marcadores do autor):
- Um bloco ```latex``` (`1{,}01^{365} \approx 37{,}8`). A Substack não renderiza LaTeX; a
  etapa 2/8 decide se vira imagem de fórmula, prosa ou fica absorvido num `graf-NN`.
- Uma tabela Markdown ("Os cinco anéis numa segunda-feira", 5 linhas × 4 colunas). A
  Substack não tem tabela nativa; a etapa 2 decide (imagem, lista ou candidato a `info-NN`,
  já que é a síntese do post inteiro).
- A citação de Hurst (seção Wall Street) aparece entre aspas como fala direta, em português,
  com aspas aninhadas na faixa da capa. A etapa 7 confere se é tradução fiel de um trecho,
  ou paráfrase (e nesse caso sai das aspas).
- Corpo em prosa: ~2.360 palavras até a tabela (contagem por regex, inclui intertítulos).
  As notas estimavam ~2.600.

---

## Cópia de trabalho (corpo do post)

# Samurais e duelos no Mercado Financeiro
5 etapas para combater estagnição

Oct 26, 2026 · @0b10n3

##

Em 1612, numa ilhota entre Kyushu e Honshu, um espadachim de 28 anos desceu de um barco com uma espada de madeira talhada de um remo. Do outro lado estava Sasaki Kojirō, instrutor de esgrima de um senhor feudal e um dos nomes mais temidos do Japão. Kojirō morreu ali, na areia.

Se você já caiu num vídeo de "disciplina samurai" no YouTube, conhece a continuação: depois do duelo, Miyamoto Musashi teria se trancado numa caverna por dois anos para entender por que quase perdeu.

É uma ótima história. Só que não aconteceu assim.

A caverna existe. Chama-se Reigandō e fica nos arredores de Kumamoto. Mas Musashi só se recolheu lá em 1643, aos 60 anos, doente, dois anos antes de morrer. Foi ali que escreveu o *Livro dos Cinco Anéis*.

Entre o duelo mais famoso da vida dele e o livro, passaram-se três décadas.

*(Passada a eleição, a série Spoiler volta com um texto que eu estava devendo.)*

No prefácio, o próprio Musashi faz o resumo.

Lutou mais de sessenta duelos sem perder, o primeiro aos 13 anos. Por volta dos 30, olhou para trás e concluiu que não tinha vencido por dominar a estratégia: tinha sido talento natural, sorte, ou escolas adversárias fracas. Só perto dos 50 sentiu que tinha entendido o Caminho.

No mercado financeiro um sujeito invicto olha para a própria sequência de vitórias e conclui que talvez tenha sido o ciclo. Quantos gestores você conhece que chegaram a essa conclusão sozinhos depois de três anos bons de bolsa?

Os primeiros anos numa mesa, num banco ou numa gestora ensinam você a vencer duelos: terminar um relatório, entregar o modelo, sobreviver ao fechamento do mês.

Isso é tática.

O sistema que funciona quando o mercado não ajuda vem depois — se vier.

E o "modo automático" que aparece depois de uns bons anos de carreira, costuma nascer justamente da confusão entre uma coisa e outra.

## Wall Street já tentou te vender este livro

A primeira tradução para o inglês, de Victor Harris, saiu em 1974 e passou quase despercebida fora do circuito das artes marciais. No começo dos anos 80, virou leitura de executivo.

O que mudou não foi o livro. Foi o Japão: a indústria japonesa estava engolindo a americana, e Nova York queria saber qual era o segredo.

O historiador G. Cameron Hurst III conta como a coisa pegou.

"Um ex-jogador de beisebol que vivia no Japão comentou o livro com um publicitário nova-iorquino, que sugeriu, meio de brincadeira, que ali estava a chave do sucesso japonês. A editora pôs uma faixa na capa: *"Japan's Answer to the Harvard MBA"*. A concorrente lançou uma edição de bolso com o subtítulo *The Real Art of Japanese Management* e, na capa, um executivo de sobretudo erguendo o *Wall Street Journal* como se fosse uma katana."

O próprio Hurst derruba essa ideia. As grandes empresas japonesas não treinavam ninguém com Musashi, e o livro mal se achava nas livrarias de Tóquio. O modelo corporativo japonês era feito de lealdade, consenso e emprego vitalício. Musashi era o oposto: um *rōnin*, samurai sem senhor, sem família, apostando a vida inteira na própria espada.

Acho que é exatamente por isso que ele ainda conversa com quem trabalha em finanças. Não porque explica o Japão, mas porque descreve alguém que opera sozinho, sob risco assimétrico, num jogo em que um único erro custa tudo.

Hurst faz uma provocação que vale levar a sério: quase todo conselho de Musashi soa familiar. Benjamin Franklin, manual de escoteiro. É verdade — o conteúdo nunca foi segredo. A diferença está no que foi lixado fora. Os best-sellers de hoje ficaram com a mecânica (sistemas, hábitos, aprendizado contínuo) e tiraram o desconforto. Musashi não tira.

## Um manual de esgrima, lido como manual de carreira

O *Gorin no Sho* tem cinco rolos, um para cada elemento: Terra (*Chi*), Água (*Sui*), Fogo (*Ka*), Vento (*Fū*) e Vazio (*Kū*). Foi escrito para ser entregue a um discípulo, não para ser vendido. E boa parte dele trata do que só interessa a quem segura uma espada: empunhadura, postura, distância, ritmo.

Então, um aviso de leitura. Nos cinco anéis a seguir, separo o que Musashi escreveu do que eu aplico para a carreira.

## Anel da Terra: saiba para onde vai sua energia

No Anel da Terra, Musashi compara o estrategista a um mestre carpinteiro. Antes de levantar a casa, ele conhece a madeira, as medidas e as ferramentas. É também onde estão as nove regras que fecham o rolo. Entre elas:

o Caminho está no treino;

conheça as coisas pequenas e as grandes;

preste atenção até no que parece trivial;

não faça nada que seja inútil.

Nenhuma delas diz "acredite em você". Todas pedem que você enxergue o que de fato faz.

Faça uma revisão honesta de uma semana normal. Quantas horas exigiram cabeça de verdade — entender uma estrutura de crédito, montar um modelo do zero, ler uma escritura até o fim? Quantas foram de formatação de planilha, reunião sem pauta, aba aberta e celular na mão? Desconfio que o dia "cheio" vai ter menos horas de trabalho real do que você gostaria.

Em tempos de IA, talvez pudessemos perguntar ainda: quanto do que você entrega foi você que fez? Se o modelo, o relatório e o e-mail saíram de uma IA e você revisou, ótimo — desde que saiba refazer cada um na mão. Usar IA é competência. Não saber o que ela fez é débito técnico. Aí você não está ganhando produtividade, está terceirizando a fundação da casa.

Musashi levou essa contabilidade para além do ofício. Uma semana antes de morrer, enquanto distribuía o que tinha aos discípulos, escreveu o *Dokkōdō*, 21 preceitos curtos. Vários soam como um manual de minimalismo escrito quase quatro séculos antes da moda: não se apegue a posses de que não precisa mais; não busque bens para garantir a velhice; seja indiferente ao lugar onde mora.

Na carreira, cada degrau de padrão que você trava é um degrau a menos de liberdade para arriscar na carreira — trocar de área, aceitar um salário menor para aprender, sair de um lugar que já não ensina nada.

## Anel da Água: vencer o eu de ontem (por dez mil dias)

A água assume a forma do recipiente e continua clara.

É esse o espírito que Musashi pede no Anel da Água: postura firme, mente que não endurece, adaptação imediata ao que aparece.

Pense na pedra no meio do rio. A pedra resiste. A água contorna, acha passagem e segue.

Aceitar a realidade, aqui, não é se render a ela. É parar de brigar com o fato para gastar energia no caminho em volta dele.

Toda carreira tem pedras: a skill que você não tem, o chefe que trava, a área que encolheu, o ciclo de juros que mudou de regime. A tentação é virar pedra também — ficar parado esperando o obstáculo sair. Ser água é perguntar: dado que isso não muda agora, por onde eu passo?

É também no fecho do Anel da Água que está a frase que eu mais gosto do livro. Em tradução livre: hoje, vença o você de ontem; amanhã, vença os menos hábeis; depois, os mais hábeis. E Musashi define o ritmo: mil dias de treino para forjar, dez mil para polir.

Quem leu *Hábitos Atômicos* reconhece a ideia. James Clear a vende como o "1% melhor por dia": melhore 1% ao dia durante um ano e você termina cerca de 37 vezes melhor. Quem trabalha com renda fixa sabe o que é aquilo — juros compostos.

```latex
1{,}01^{365} \approx 37{,}8
```

Quem trabalha com finanças, já viu alguma conta semlhante.

Ela supõe uma taxa constante e positiva, todo santo dia. Carreira não é título pós-fixado. Tem dia de taxa negativa, tem semestre inteiro de marcação a mercado contra você.

Musashi não precisa dessa premissa. Dez mil dias são uns 27 anos, e ele não promete retorno em nenhum deles.

A conta, aliás, bate com a biografia: do primeiro duelo, aos 13, até sentir que entendeu a estratégia, perto dos 50, foram quase quatro décadas.

No mesmo rolo, Musashi separa dois olhares.

O *kan* enxerga a situação inteira.

O *ken* enxerga a superfície.

O primeiro é forte, o segundo é fraco. Ryan Holiday usou essa distinção em *O Obstáculo é o Caminho*.

## Anel do Fogo: o desconforto como combustível

Aqui está a parte que a autoajuda moderna não vende.

Literalmente, o Anel do Fogo é sobre a luta em si, o calor do combate. Musashi fala em tomar a iniciativa, em não deixar o adversário recuperar o ritmo, em esmagá-lo quando ele vacila. E tem uma ideia que eu acho brilhante: quando a luta trava e os dois ficam presos no mesmo impasse, a saída não é empurrar mais forte. É abandonar aquela abordagem e recomeçar, como se fosse outra luta.

Para quem tem de dois a oito anos de mercado, o adversário que importa não é o colega da mesa ao lado. É o modo automático: a mesma planilha, o mesmo relatório, o mesmo tipo de entrega, ano após ano.

E o que o Anel da Terra faz com você, se feito com honestidade, incomoda. Você descobre que passa mais tempo no Instagram do que estudando. Que o estagiário que entrou ano passado escreve Python melhor que você. Que o projeto que você adia há dois anos continua adiado. A reação natural é raiva.

O conselho padrão de desenvolvimento pessoal é ser gentil consigo mesmo. A leitura que faço do Fogo é outra: essa raiva é energia, e energia não se desperdiça. O desperdício é queimá-la em autodepreciação ou em inveja de quem está na frente. (O próprio *Dokkōdō* manda nunca invejar ninguém.)

O ponto é a mira.

Raiva de você mesmo vira paralisia.

Raiva do estado em que você está vira plano: "estudei 30 minutos esta semana" vira "na próxima, o celular fica em outro cômodo nessas duas horas". O Fogo não é sobre se punir.

É sobre não deixar o adversário — o seu padrão de sempre — recuperar o fôlego.

E se você está há dois anos empurrando a mesma porta, lembre do impasse de Musashi. Mais força na mesma abordagem raramente resolve. Às vezes a jogada é mudar de luta.

## Anel do Vento: estude as outras escolas

Literalmente, o Anel do Vento é o capítulo em que Musashi critica as escolas rivais de esgrima. Uma usa espada longa demais; outra, curta demais. Uma confia na força bruta; outra coleciona posturas. E ele desconfia de quem divide o ensino em níveis secretos, com uma "porta" para iniciantes e um "interior" para os escolhidos.

O nome guarda um trocadilho que se perde na tradução. *Fū*, vento, também quer dizer estilo, maneira, tradição — como em "o jeito da casa". O rolo do Vento é o rolo dos estilos dos outros. E a justificativa de Musashi é simples: é difícil conhecer a si mesmo sem conhecer os outros.

(A ironia: o sujeito que desconfiava de escolas de segredos foi vendido nos Estados Unidos como o segredo do Japão.)

**A leitura de carreira — interpretação, não tradução.** Leio aqui a ideia do aprendiz permanente. Robert Greene, em *Maestria*, chama de aprendizado a fase em que você absorve um ofício com humildade. Para quem quer continuar relevante, eu diria que essa fase nunca termina de verdade.

No contexto de finanças quantitativas, vejo muito o caso de quem aprende processos estocásticos e acha que fechou a matemática, a estatística e as finanças. Para de estudar. Perde a fome. O título de mestre chega antes da maestria.

O segundo risco é mais silencioso: conhecer só a escola do próprio banco. O modelo da casa, a planilha da casa, o jeito da casa de olhar risco. Funciona até o dia em que você muda de casa — ou a casa muda de mercado. Estudar como outras mesas, outras gestoras e outras áreas resolvem o mesmo problema é a forma mais barata de achar os seus pontos cegos.

## Anel do Vazio: não existe linha de chegada

O último rolo é o mais curto, poucas páginas de influência zen. É fácil ler o Vazio como iluminação: o estágio em que o esforço acaba e tudo flui.

Musashi não deixa.

Ele avisa que muita gente chama de vazio aquilo que simplesmente não entende — e isso não é vazio, é confusão. O vazio verdadeiro aparece quando essa névoa se dissipa. E o caminho até lá é descrito sem romantismo nenhum: com o espírito assentado, acumule prática dia após dia, hora após hora; afie a mente e o olhar.

O spoiler que eu tiro do Vazio é desconfortável: uma vida de melhoria contínua é difícil para sempre. Não existe a certificação, a promoção ou o mestrado depois do qual o trabalho fica leve.

Você não chega num ponto em que a disciplina fica fácil.

Você vira alguém para quem fazer coisas difíceis é o normal.

E aqui eu discordo da versão *hardcore* que circula por aí. Difícil para sempre não quer dizer sofrer à toa. Esta série existe por uma ideia: não é porque eu sofri que você também precisa sofrer. O atrito de aprender um modelo novo, de recomeçar numa área, de admitir que o eu de ontem estava errado — esse fica. O sofrimento inútil, Musashi já tinha cortado lá na Terra: não faça nada que seja inútil.

## Não Fica Fácil

Musashi escreveu o livro aos 60 anos, numa caverna, doente, para um único discípulo. Venceu o duelo mais famoso da história do Japão aos 28 e passou as três décadas seguintes treinando, pintando, escrevendo e estudando as escolas dos outros.

Na última semana de vida, ainda estava escrevendo regras para si mesmo.

Se você está no terceiro, quinto ou oitavo ano de carreira e sente que entrou no modo automático, a boa notícia é que isso não é defeito seu. É o ponto exato em que Musashi parou de contar vitórias e começou a perguntar por que tinha vencido.

A má notícia é que não fica mais fácil.

Mas, se você leu até aqui, desconfio que isso você já sabia.

## Os cinco anéis numa segunda-feira

| Anel | O que Musashi escreveu | O que eu leio para a carreira | Pergunta para esta semana |
| --- | --- | --- | --- |
| Terra (*Chi*) | Conhecer as medidas e as ferramentas, as coisas pequenas e as grandes; não fazer nada inútil | Auditoria honesta de para onde vai sua energia — inclusive o que a IA faz por você | Quantas horas desta semana exigiram cabeça de verdade? |
| Água (*Sui*) | Adaptar-se como a água; vencer o eu de ontem; mil dias para forjar, dez mil para polir | Contornar a pedra em vez de virar pedra; constância sem promessa de retorno em um ano | Qual obstáculo você está esperando sair do caminho sozinho? |
| Fogo (*Ka*) | Tomar a iniciativa; quando a luta trava, abandonar a abordagem e recomeçar | O desconforto com o próprio estado como combustível — mirado no hábito, não em você | Que impasse você está tentando resolver empurrando mais forte? |
| Vento (*Fū*) | Criticar as escolas rivais; conhecer os outros para conhecer a si mesmo | Aprendiz permanente; estudar como outras casas resolvem o mesmo problema | O que você aprendeu este mês que não é o jeito da sua casa? |
| Vazio (*Kū*) | Dissipar a confusão acumulando prática, dia após dia | Não há linha de chegada: o atrito fica, o sofrimento inútil não | Que esforço você está fazendo esperando que um dia acabe? |

## Referências

- Miyamoto Musashi, *O Livro dos Cinco Anéis* (*Gorin no Sho*, 1645). Tradução de referência usada na pauta: Thomas Cleary, *The Book of Five Rings* (Shambhala).
- Miyamoto Musashi, *Dokkōdō* (1645).
- G. Cameron Hurst III, ["Samurai on Wall Street: Miyamoto Musashi and the Search for Success"](https://ejmas.com/jalt/jaltart_Hurst_0101.htm) (1982; republicado em *InYo*, 2001).
- Tofugu, ["Miyamoto Musashi's Reigando Cave"](https://www.tofugu.com/travel/reigando-cave/).
- James Clear, *Hábitos Atômicos*.
- Robert Greene, *Maestria*.
- Ryan Holiday, *O Obstáculo é o Caminho*.

---

## Apêndice do rascunho (verbatim, não publicar)

## Notas de revisão (remover antes de publicar)

**Perguntas para você**

1. **Livro de minimalismo do áudio.** Qual era? Ancorei o argumento no *Dokkōdō* do próprio Musashi. Se for Fumio Sasaki (*Goodbye, Things*), dá para citá-lo ao lado em uma frase.
2. **Bloco de Wall Street.** É o trecho mais histórico e menos pessoal. Manter inteiro, reduzir a um parágrafo ou cortar?
3. **Relatos pessoais.** Há dois `[INSERIR]` (Terra e fechamento). Quer que eu proponha versões a partir de alguma experiência sua, ou você escreve?
4. **Edição de referência.** Citar uma tradução brasileira do livro em vez da Cleary?
5. **Vídeo.** Nenhum vídeo dos últimos 24 meses foi confirmado. O Jocko Podcast #80 é o clássico em inglês sobre o livro, mas é antigo e não foi reverificado. Incluir como "para ir além" ou deixar sem vídeo?
6. **Tamanho.** O corpo ficou com cerca de 2.600 palavras (estimativa). Se a meta do Spoiler for menor, os candidatos a corte são o bloco de Wall Street e o parágrafo do *kan*/*ken*.

**Correções em relação ao rascunho e à pesquisa**

- Caverna: o retiro em Reigandō foi em 1643, não logo após o duelo de 1612. O texto já usa isso como gancho.
- "Hoje vença o eu de ontem": a pesquisa atribui a frase ao Anel do Fogo. Ela fecha o Anel da Água — e reposicionada ali ancora o paralelo com o 1% de Clear.
- "When Musashi speaks, people listen": a pesquisa atribui à editora Overlook; Hurst atribui à *Time*. Não usei.
- Não afirmei que Clear ou Greene derivam de Musashi (a pauta diz "bestsellers que dele derivam", sem fonte). O texto diz que as ideias reaparecem em embalagem mais confortável.
- Fogo como raiva, Vento como aprendizado contínuo e Vazio como "difícil para sempre" estão marcados como leitura do autor, não tradução.
- O vídeo "Become So Disciplined People Call You Crazy" tem erros factuais (caverna após Kojirō, pai morto aos 7 e 14 horas de treino diário). Nada dele entrou como fato.
- Idade em Ganryūjima: 28 pela conta ocidental (nascido em 1584); Hurst diz 29 pela contagem japonesa. Usei 28.

**Títulos e SEO**

- E-mail (usado no H1): O que um samurai do século 17 sabe sobre sua carreira em finanças que o Hábitos Atômicos não te conta
- Busca orgânica: Livro dos Cinco Anéis aplicado à carreira: o que Musashi ensina sobre disciplina e maestria
- Nota do Substack (usado como primeiro intertítulo): Antes do 1% melhor, havia os Cinco Anéis

**Ideias de gráfico para o pipeline**

- Linha do tempo de Musashi (1584, 1597, 1612, \~1634, 1643, 1645) destacando os 30 anos entre Ganryūjima e a caverna.
- 1% ao dia composto (curva lisa até \~37,8x) contra uma trajetória com dias de "taxa negativa" — o argumento do Anel da Água em uma imagem.


Talvez valha adicionar algum exemplo relacionado as eleicoes, como perder muito tempo com politica em rede sociais .... tem arescente.

---

## Marcadores extraídos do rascunho

| # | Trecho (verbatim ou resumido) | Classificação | Resolução |
|---|---|---|---|
| 1 | Sem front-matter YAML; corpo: "*(Passada a eleição, a série Spoiler volta com um texto que eu estava devendo.)*" | Estrutural | **Resolvido (etapa 0)**: autor confirmou Spoiler. |
| 2 | H1 "# Samurais e duelos no Mercado Financeiro" × notas "E-mail (usado no H1): O que um samurai do século 17 sabe…" | Estrutural | **Resolvido (etapa 0)**: título = H1. O título de e-mail vai para `assunto_email` (etapa 9). |
| 3 | Subtítulo "5 etapas para combater estagnição" | Estrutural | Pendente (etapa 1). O corpo organiza o texto em cinco *anéis*, não em "etapas", e o vocabulário destoa do resto. Confirmar o subtítulo (o erro de digitação é da etapa 6). |
| 4 | Intertítulo vazio `## ` logo após o byline × notas "Nota do Substack (usado como primeiro intertítulo): Antes do 1% melhor, havia os Cinco Anéis" | Estrutural | Pendente (etapa 1). O corpo não tem o intertítulo que as notas dizem ter. Decidir entre preencher com a frase das notas, deixar a abertura sem intertítulo ou outra opção. |
| 5 | Notas, pergunta 1: "**Livro de minimalismo do áudio.** Qual era? … Se for Fumio Sasaki (*Goodbye, Things*), dá para citá-lo ao lado em uma frase." | Nota de conteúdo | Pendente (etapa 1, pergunta ao autor). |
| 6 | Notas, pergunta 2: "**Bloco de Wall Street.** … Manter inteiro, reduzir a um parágrafo ou cortar?" | Estrutural | Pendente (etapa 1, pergunta ao autor; a etapa 5 também opina). |
| 7 | Notas, pergunta 3: "**Relatos pessoais.** Há dois `[INSERIR]` (Terra e fechamento)." | Estrutural | Pendente (etapa 1). **Fato conferido:** não há nenhum `[INSERIR]` no corpo (grep por `[` só acha a própria nota). Ou o autor removeu os marcadores sem preencher, ou foram removidos em outra rodada. Perguntar: entra relato pessoal na Terra e/ou no fechamento, ou o texto segue sem? |
| 8 | Notas, pergunta 4: "**Edição de referência.** Citar uma tradução brasileira do livro em vez da Cleary?" | Nota de conteúdo | Pendente (etapa 1, pergunta; a etapa 3/7 confere a edição escolhida). |
| 9 | Notas, pergunta 5: "**Vídeo.** … O Jocko Podcast #80 … Incluir como 'para ir além' ou deixar sem vídeo?" | Nota de conteúdo | Pendente (etapa 1, pergunta). Hoje o corpo não tem seção "para ir além". |
| 10 | Notas, pergunta 6: "**Tamanho.** … cerca de 2.600 palavras … candidatos a corte são o bloco de Wall Street e o parágrafo do *kan*/*ken*." | Estrutural | Pendente (etapa 1). Contagem atual: ~2.360 palavras até a tabela. Ligado ao #6. O parágrafo do *kan*/*ken* termina em "Ryan Holiday usou essa distinção em *O Obstáculo é o Caminho*." sem tirar consequência dela, o que a etapa 5 deve avaliar. |
| 11 | Correções: "Caverna: o retiro em Reigandō foi em 1643, não logo após o duelo de 1612." | Nota de conteúdo | Pendente (etapa 7): confirmar 1643 e a idade ("aos 60 anos"). |
| 12 | Correções: "'Hoje vença o eu de ontem': … Ela fecha o Anel da Água." | Nota de conteúdo | Pendente (etapa 7): conferir na tradução de referência (ver #8) e conferir "mil dias para forjar, dez mil para polir". |
| 13 | Correções: "Idade em Ganryūjima: 28 pela conta ocidental (nascido em 1584); Hurst diz 29 pela contagem japonesa. Usei 28." | Nota de conteúdo | Pendente (etapa 7). |
| 14 | Correções: "'When Musashi speaks, people listen' … Não usei." / "Não afirmei que Clear ou Greene derivam de Musashi" / "O vídeo 'Become So Disciplined…' tem erros factuais … Nada dele entrou como fato." | Nota de conteúdo | Registro: decisões de rodada anterior. A etapa 3 não reintroduz nenhuma delas. |
| 15 | Correções: "Fogo como raiva, Vento como aprendizado contínuo e Vazio como 'difícil para sempre' estão marcados como leitura do autor, não tradução." | Nota de conteúdo | Registro. A etapa 5 confere se a fronteira "o que Musashi escreveu × o que eu leio" (prometida em "Um manual de esgrima…") se mantém nos cinco anéis, e não só nesses três. |
| 16 | Títulos e SEO: e-mail, "Busca orgânica: Livro dos Cinco Anéis aplicado à carreira…", "Nota do Substack: Antes do 1% melhor, havia os Cinco Anéis" | Estrutural | Parcial: e-mail resolvido no #2. `busca_organica` e `nota_substack` entram no frontmatter na etapa 9. Ver #4 para o uso da nota como intertítulo. |
| 17 | Ideia de gráfico: "Linha do tempo de Musashi (1584, 1597, 1612, \~1634, 1643, 1645) destacando os 30 anos entre Ganryūjima e a caverna." | Sugestão de visual | Pendente (etapa 2 decide pelo critério: linha do tempo sem métrica central → candidato a `diag-NN`; etapa 8 produz). As datas 1597 e ~1634 não aparecem no corpo; a etapa 7 confere as seis. |
| 18 | Ideia de gráfico: "1% ao dia composto (curva lisa até \~37,8x) contra uma trajetória com dias de 'taxa negativa'" | Sugestão de visual | Pendente (etapa 2). A curva 1,01ⁿ é conta real; a trajetória com dias negativos seria **simulada**, não série observada. A etapa 2 decide se isso cabe como `graf-NN` com a simulação rotulada como tal, ou se vira `diag-NN`. Pode absorver o bloco LaTeX. |
| 19 | Linha final, solta: "Talvez valha adicionar algum exemplo relacionado as eleicoes, como perder muito tempo com politica em rede sociais .... tem arescente." | Instrução de escrita | Pendente (etapa 4). "tem arescente" lido como "acrescente". Encaixes naturais: a auditoria de semana do Anel da Terra ("aba aberta e celular na mão"), o Instagram do Anel do Fogo e o aparte "Passada a eleição". A etapa 1 escolhe o ponto, a etapa 4 escreve com nota lateral, e o exemplo fica apartidário. |
| 20 | Aparte "*(Passada a eleição, a série Spoiler volta…)*" entre a cena da caverna e o prefácio | Nota de conteúdo | Pendente (etapa 7: o 2º turno de 2026 foi em 25/10, e a publicação em 27/10 fica depois dele; conferir). A posição do aparte no meio da abertura é com a etapa 5. |
| 21 | Referências (7 itens, 2 URLs: Hurst/EJMAS, Tofugu/Reigandō) | Nota de conteúdo | Pendente (etapa 7): abrir as duas URLs, conferir "1982; republicado em *InYo*, 2001" e Cleary/Shambhala. |
| 22 | Byline "Oct 26, 2026 · @0b10n3" × nome do arquivo `2026-10-27_…` | Nota de conteúdo | Registro: `data` no frontmatter = 2026-10-27 (nome do arquivo e slug), salvo se o autor pedir outra. |
