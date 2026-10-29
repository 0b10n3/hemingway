# Etapa 2 — Estrutura

`linha_editorial: Spoiler`, portanto sem Ficha de Saída de backward design, que é exclusiva de
"Notas de um Professor" (`docs/BACKWARDS_DESIGN.md` §2). Esta etapa documenta e confirma a
estrutura que o rascunho já traz. O pipeline não reordena argumento por conta própria. As
decisões do autor na etapa 1 (manter Wall Street inteiro, sem relato pessoal, só o
*Dokkōdō*) não mudam a ordem das seções.

## Subtítulos e o que cada seção prova

| Seção | O que prova |
|---|---|
| Abertura (hoje `## ` vazio — ver "Intertítulo da abertura" abaixo): Ganryūjima 1612, mito da caverna, Reigandō 1643, aparte da série, prefácio de Musashi, invicto × ciclo, tática × sistema | Monta a intuição comum (o vídeo de "disciplina samurai": vitória → retiro imediato → maestria) e a derruba com data verificável: três décadas entre o duelo e o livro. O prefácio dá a segunda prova: o próprio invicto atribui as vitórias a talento, sorte e adversários fracos. A ponte para finanças vem por "talvez tenha sido o ciclo". Fecha com a tese ("Isso é tática…" / "modo automático… nasce justamente da confusão entre uma coisa e outra"). |
| "Wall Street já tentou te vender este livro" | Prova que a leitura "Musashi = segredo do sucesso" é um produto de marketing dos anos 80 (Harris 1974, faixa da capa, Hurst 1982) e que o modelo corporativo japonês era o oposto de Musashi. Ganha dois argumentos para o resto do texto. (1) Por que Musashi serve para finanças: rōnin, risco assimétrico, um erro custa tudo. (2) A provocação de Hurst: o conteúdo nunca foi segredo, os best-sellers tiraram o desconforto. O ponto (2) arma o Fogo. |
| "Um manual de esgrima, lido como manual de carreira" | Não prova, contrata: apresenta os cinco rolos e declara o método de leitura (separar o que Musashi escreveu do que o autor aplica). É a seção mais curta e funciona como dobradiça entre contexto e argumento. |
| "Anel da Terra: saiba para onde vai sua energia" | Prova que o primeiro passo é contábil, não motivacional (as nove regras pedem que você enxergue o que faz). Desdobra em três auditorias: horas de trabalho real (onde entra o exemplo das eleições, instrução do autor), o que a IA faz por você (débito técnico) e padrão de vida como perda de liberdade (*Dokkōdō*). |
| "Anel da Água: vencer o eu de ontem (por dez mil dias)" | Prova que constância sem promessa de retorno (dez mil dias) é mais honesta que o "1% ao dia" de Clear, porque carreira não é título pós-fixado. É a seção com mais dado e com a analogia mais "de casa" (juros compostos, marcação a mercado). Contém também a pedra no rio e o *kan*/*ken*. |
| "Anel do Fogo: o desconforto como combustível" | Prova a tese contra a autoajuda (cumpre a provocação de Hurst): a raiva que a auditoria da Terra produz é combustível se mirada no estado, não na pessoa. O impasse ("mudar de luta") é a segunda prova. Define o adversário do texto: o modo automático. |
| "Anel do Vento: estude as outras escolas" | Prova que o aprendiz permanente é uma exigência, não uma virtude opcional, por dois riscos: o "título de mestre antes da maestria" (processos estocásticos) e conhecer só "a escola do próprio banco". |
| "Anel do Vazio: não existe linha de chegada" | Entrega o spoiler da série: é difícil para sempre. Separa atrito (fica) de sofrimento inútil (sai), fechando o laço com a última regra da Terra ("não faça nada que seja inútil"). |
| "Não Fica Fácil" | Volta à cena de abertura (caverna, 60 anos, discípulo único, *Dokkōdō* na última semana) e devolve o modo automático ao leitor como o ponto em que Musashi "parou de contar vitórias". Fecho seco, sem CTA (alerta do briefing). |
| "Os cinco anéis numa segunda-feira" | Síntese aplicável: as cinco leituras em tabela com pergunta para a semana. Reproduz em colunas a fronteira prometida ("o que Musashi escreveu" × "o que eu leio"). |
| "Referências" | — |

## Arco narrativo (versão completa: post longo, 6+ fontes)

- **Gancho:** Ganryūjima e o mito da caverna desmontado.
- **Contexto:** o prefácio (invicto que desconfia), a ponte tática × sistema, Wall Street e o
  contrato de leitura.
- **Ação crescente:** Terra (auditoria) → Água (constância sem promessa) → Fogo (o
  desconforto que a autoajuda tira). A tensão sobe de "enxergue" para "aguente" e depois para
  "use a raiva".
- **Clímax:** Vazio ("não existe linha de chegada"), o spoiler propriamente dito. O Vento fica
  entre Fogo e Vazio como alívio de tensão e ampliação (dos outros para si). Essa ordem é a
  do próprio livro, que o rascunho segue; não é escolha do pipeline.
- **Resolução:** o fim do Vazio (atrito × sofrimento inútil, a discordância da versão
  *hardcore*).
- **Fechamento:** "Não Fica Fácil" + tabela. Em voz ensaística o fechamento esperado é CTA
  (`.claude/agents/references/tecnicas-narrativas.md`), mas o rascunho fecha seco. Fica para
  a etapa 5 e, se for o caso, para o gate. O pipeline não insere CTA.

## Confirmação dos três pilares

- **Dado:** 1584, 1597 (primeiro duelo aos 13), 1612 (Ganryūjima, 28 anos), ~1634 ("perto
  dos 50"), 1643 (Reigandō), 1645 (*Gorin no Sho*, *Dokkōdō*, morte); "mais de sessenta
  duelos"; Harris 1974; Hurst 1982; "nove regras"; "21 preceitos"; 1,01³⁶⁵ ≈ 37,8; dez mil
  dias ≈ 27 anos. Aparece na abertura, em Wall Street, na Água e no fechamento.
- **Narrativa:** a biografia de Musashi como fio, o episódio de Wall Street e as cinco
  leituras de carreira. Modo dominante, coerente com Spoiler.
- **Visual:** `diag-01`, `graf-01` e `diag-02` (abaixo), na abertura, na Água e na síntese.

Os três pilares aparecem cada um em pelo menos uma seção. Confirmado.

## Visuais: onde e por quê

A Substack não renderiza tabela Markdown nem LaTeX (precedentes: posts do CRA e da
debênture). A tabela vira peça-imagem e a fórmula vira texto ou anotação de gráfico.

| Peça | Onde | Tipo | Por quê (e por que os outros perderam) |
| --- | --- | --- | --- |
| **diag-01** | Abertura, logo depois de "Só perto dos 50 sentiu que tinha entendido o Caminho." e antes de "No mercado financeiro um sujeito invicto…" | Linha do tempo | Sugestão do autor (notas: "Linha do tempo de Musashi… destacando os 30 anos entre Ganryūjima e a caverna"). Datas sem métrica central → diag (critério 2, "linha do tempo sem métrica central"). graf perde: a única grandeza é o tempo, e não há série a comparar. info perde: uma peça só carrega a ideia. Marcos: 1584 nascimento, 1597 primeiro duelo (13), 1612 Ganryūjima (28), ~1634 "entendeu o Caminho" (~50), 1643 Reigandō, 1645 livro + *Dokkōdō* + morte, com o intervalo 1612→1643 em destaque. Fica nesse ponto porque o leitor acaba de receber as três idades do prefácio (13, 30, 50) e vê as três sobre a mesma linha que mostra o vão de três décadas. Todas as seis datas, inclusive 1597 e ~1634, que não aparecem no corpo, passam pela etapa 7 antes da etapa 8. A convenção de idade é uma só na peça inteira (ver alerta 1 abaixo). |
| **graf-01** | Água, logo depois de "Tem dia de taxa negativa, tem semestre inteiro de marcação a mercado contra você." e antes de "Musashi não precisa dessa premissa." | Gráfico de linha | Sugestão do autor (notas: "1% ao dia composto… contra uma trajetória com dias de 'taxa negativa'"). Há série numérica com métrica real (multiplicador acumulado, dia a dia, pela conta do próprio texto) → graf (critério 1). A ressalva do critério 2 ("duas linhas sem métrica real por trás → diagrama") não se aplica: a métrica é real. O que é hipotético é o cenário da segunda linha. **Restrição para a etapa 8:** a segunda trajetória é cenário declarado, não dado observado. Precisa ser determinística ou com semente fixa, ter os parâmetros escritos na legenda e não sugerir que representa carreira real de alguém. A forma do cenário (dias negativos esparsos, um "semestre de marcação contra" ou mesma média aritmética com oscilação) é decisão da etapa 8, desde que caiba na frase do autor e não acrescente argumento novo. graf-01 absorve a anotação "≈ 37,8×" no fim da curva lisa. info perde: uma peça basta. |
| **diag-02** | "Os cinco anéis numa segunda-feira" (substitui a tabela Markdown) | Tabela-imagem | Comparação estrutural (5 anéis × 4 colunas de texto), sem métrica → diag (critério 2), mesmo tratamento das tabelas sem número do post da debênture. graf perde: não há número. info perde: a tabela já é a síntese em uma peça só, e o critério de gatilho do infográfico ("nenhuma peça isolada carrega a síntese sozinha") falha justamente porque esta carrega. Texto das células = o do autor, sem edição nesta etapa. |
| — info-NN | — | Não se aplica | Nenhuma síntese exige mais de uma peça. Padrão: não tem. |

**Bloco LaTeX (`1{,}01^{365} \approx 37{,}8`).** Vira linha de texto simples na etapa 4
("1,01³⁶⁵ ≈ 37,8", centralizada, com sobrescrito Unicode), sem imagem de fórmula. O graf-01
repete o número como anotação, e a linha de texto continua lá para quem lê o e-mail sem
carregar imagem.

### Considerados e descartados

- **Diagrama dos cinco rolos** (Terra → Água → Fogo → Vento → Vazio como sequência). Seria
  diag pelo critério 2, mas duplicaria o diag-02 e reforçaria a leitura "5 etapas" que o
  próprio texto evita (ver "Tensão — subtítulo"). Não entra.
- **Pedra × água no rio** (Água). É a metáfora do autor e carregaria o argumento, mas é o caso
  4 do critério (ilustração), fora do pipeline desde 2026-09-09. Fica em prosa.
- **Gráfico de "horas de trabalho real" da auditoria da Terra.** Não há série. Seria número
  inventado. Não entra.

## Intertítulo da abertura (marcador #4) — sugestão ao autor, não decisão

O `## ` vazio logo depois do byline é artefato de exportação ou sobra de uma rodada em que o
primeiro intertítulo era a "Nota do Substack" ("Antes do 1% melhor, havia os Cinco Anéis").
Essa frase fala do Anel da Água e não da cena de 1612, que é o que a abertura de fato contém.
O post anterior da série (`2026-10-12-coqueiros-e-cacaueiros`) abre sem intertítulo.
**Sugestão:** remover o `## ` vazio (abertura sem intertítulo, como no coqueiros) e manter a
frase só como `nota_substack` no frontmatter (etapa 9). A etapa 4 aplica e anota. Se o autor
preferir um intertítulo, isso vira ajuste de gate (etapa 9, não consome loop).

## Tensão nova registrada nesta etapa — "Tensão — ponte de série"

O post `2026-10-12-coqueiros-e-cacaueiros` publicou: "Sei que prometi na semana passada
começar uma série sobre _O livro dos cinco anéis_, de Miyamoto Musashi. Ela vai acontecer."
(`posts/2026-10-12-coqueiros-e-cacaueiros/post.md:16`). Este rascunho cobre os cinco anéis
num texto só, e o aparte diz "a série Spoiler volta com um texto que eu estava devendo". A
promessa publicada era de *série*. Pergunta para o gate: (A) este texto é a série inteira
num post só, e o aparte basta como está; ou (B) este é o primeiro de uma série, e o aparte ou
o fecho precisam dizer isso, com o que vem depois. O pipeline segue com o texto como está.
Não renumera nada nem promete próximo texto.

## O que fica de fora

- **Reordenação de argumento:** nenhuma. A sequência segue a do próprio *Gorin no Sho* e
  entrega o arco.
- **Decisões da rodada anterior** (notas do rascunho): citação "When Musashi speaks…", a
  afirmação de que Clear/Greene derivam de Musashi e qualquer fato do vídeo "Become So
  Disciplined…" ficam fora.
- **Relato pessoal e livro moderno de minimalismo:** fora, por decisão do autor (etapa 1).

## Pontos para a crítica estrutural (etapa 5) olhar — não são decisões desta etapa

1. **Aparte da série no meio do gancho.** "*(Passada a eleição…)*" fica entre a cena da
   caverna e o prefácio. É o mesmo padrão que a crítica do coqueiros apontou ("o parágrafo da
   série sobre Musashi interrompe o gancho"), e lá o autor decidiu manter.
2. **Fronteira "o que Musashi escreveu × o que eu leio".** Só o Vento tem rótulo explícito
   ("**A leitura de carreira — interpretação, não tradução.**"). Nos outros anéis a passagem é
   por frase ("A leitura que faço do Fogo é outra", "O spoiler que eu tiro do Vazio"), e na
   Terra e na Água ela é menos visível (ex.: "Nenhuma delas diz 'acredite em você'" já é
   leitura). Conferir se o contrato da seção "Um manual de esgrima…" é cumprido nos cinco.
3. **Parágrafo do *kan*/*ken*.** Termina citando Holiday sem tirar consequência para a
   carreira. Candidato a corte apontado pelo próprio autor nas notas.
4. **Fecho sem CTA nem gancho de série** (ligado à "Tensão — ponte de série").
5. **Subtítulo "5 etapas…"** contra cinco leituras que não são sequenciais ("Tensão —
   subtítulo", briefing).
6. **Validação argumentativa (Spoiler):** a tese "modo automático = confusão entre tática e
   sistema" é sustentada pelos cinco anéis ou só pela abertura e pelo fechamento?

## Alertas para a verificação técnica (etapa 7)

1. **Convenção de idade inconsistente.** O texto usa a contagem ocidental em Ganryūjima ("28",
   nascido em 1584, nota do autor) e "aos 60 anos" no retiro de 1643 e no fechamento ("escreveu
   o livro aos 60 anos"). Pela conta ocidental, 1643 − 1584 = 59. O prefácio do *Gorin no
   Sho* diz "sessenta anos" pela contagem japonesa. Ou se usa uma convenção só, ou o "60" vem
   atribuído ao próprio Musashi. Vale também para o diag-01.
2. "Mil dias para forjar, dez mil para polir" e "hoje, vença o você de ontem" no fecho do
   Anel da Água, conferidos na edição de referência (pendente pós-etapa 3).
3. "Para um único discípulo" (Terao Magonojō?), "uma semana antes de morrer" (*Dokkōdō*), "21
   preceitos", "nove regras", "mais de sessenta duelos, o primeiro aos 13".
4. Clear: "cerca de 37 vezes melhor" e 1,01³⁶⁵ = 37,78.
