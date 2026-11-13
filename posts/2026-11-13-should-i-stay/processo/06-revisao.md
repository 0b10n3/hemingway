# Etapa 6 — Revisão de linha e norma

Executor: subagente `revisor-gramatical`. Texto: corpo de `processo/04-draft-v2.md` (l. 11–137).
Conferido contra `estilo/estilo-autoral.md` (§3, §4.1, §7, §9),
`.claude/skills/voz-syntaxis/references/antipadroes.md` e `pesquisa/frente-d-antipadroes-ia-ptbr.md`;
uso da casa em `coqueiros-e-cacaueiros` e `borboletas-caos-e-carreira`. Não toca estrutura,
argumento, números nem `[VERIFICAR]`.

Classes: `norma` = erro objetivo de norma culta, regra 1 ou regra 4 (inegociável); `linha` =
clareza, ritmo ou leitura em voz alta (sugestão).

**Sem achado:** crase ("daqui a doze meses", "até a data Y", "depois de a banda deixar de
existir"); regência ("responder a ela", "de quem você realmente não gosta", "depois de eu ter
pedido"); concordância ("quem escolheu foram os parceiros"); "te" com "você" (voz, mesmo uso em
`coqueiros-e-cacaueiros`); fragmentos da voz ("Sair também.", "Oito meses contam outra.", "Custo
se administra.", "Clima entra na conta. Só não fecha a conta sozinho."); itálico de obra
(*Combat Rock*, *Freakonomics*); unidades (1,70 m, 1,85 m); frases fixadas pelo autor ("Como
matemático, eu resolvo pelo meu critério", "olhe a derivada, não o nível"); restrições do autor
(nenhum verso; sem relato pessoal).

## Decisão: rótulos dos seis sinais

Os rótulos viram H3 sem negrito e sem ponto final (`### 1. Ainda há o que aprender, e há quem
ensine`). O negrito de rótulo não é ênfase de frase, mas é o único negrito do post (regra 4); a
regra 5 resolve com subtítulo; precedente em `borboletas-caos-e-carreira` (`### 1. Julgue a
decisão, não o resultado`); o Substack inclui H3 no sumário. Classe `norma` (convenção da casa).
Itens 13, 24 e 27.

## Diff comentado

| # | Onde | Classe | Atual | Proposta | Motivo |
|---|---|---|---|---|---|
| 1 | Abertura, §1 | linha | "o The Clash lançou" | "o Clash lançou" | Artigo duplo. Opcional. |
| 2 | Abertura, §4 | norma | "sentada numa mesa de banco, asset ou corretora" | "sentada numa mesa (no mercado, a equipe de uma área, como renda fixa ou ações) de banco, de gestora ou de corretora" | Regra 1: "mesa" no jargão aparece aqui pela primeira vez e volta duas vezes. "Asset" sem glosa nem itálico → "gestora" (ou "de gestora (a *asset*, no jargão)"). |
| 3 | Ressalva | linha | "E nas situações extremas (assédio, …) não existe lista de sinais." | "E, nas situações extremas (assédio, …), não existe lista de sinais." | Vírgulas do adjunto alongado. |
| 4 | Ressalva | linha | "que é a imensa maioria dos casos" | "que é a maioria dos casos" | Crítica item 12. Opcional. |
| 5 | Clima/Capital | linha | "Cal Newport chama isso" | "Cal Newport, professor de ciência da computação e autor de livros sobre carreira, chama isso" | Única fonte sem identificação. Fato novo → etapa 7. Opcional. |
| 6 | Clima/Capital | norma | "ler uma escritura" | "ler uma escritura (o contrato que fixa as regras de um título de dívida)" | Regra 1. |
| 7 | Clima/Capital | linha | "Entre as três coisas que, para ele, desqualificam um emprego estão poucas chances…, um trabalho…, e ter de conviver com gente…" | "As três coisas que, para ele, desqualificam um emprego são poucas chances…, um trabalho… e a obrigação de conviver com gente…" | "Entre as três" sugere parte da lista; paralelismo. Ordem mantida. |
| 8 | Ficar 1 | linha | "quando [falei de Musashi](…)" | "quando [falei de Musashi](…), o espadachim japonês," | Quem não leu o post anterior. Opcional. |
| 9 | Ficar 2 | linha | "Pergunte com frieza: se eu sair" | "Pergunte-se com frieza: se eu sair" | Pergunta em 1ª pessoa. |
| 10 | Ficar 3 | norma | "As suas skills naturais" / "Toda skill nova" | "As suas *skills* naturais" / "Toda *skill* nova" | Itálico de estrangeirismo; uso da casa. |
| 11 | Ficar 3 | linha | "Existe coisa que você faz bem gastando pouca energia." | "Há coisas que você faz bem gastando pouca energia." | Singular × "os seus coqueiros". |
| 12 | Dado que incomoda | linha | "há boa evidência apontando para o outro lado" | "há boa evidência que aponta para o outro lado" | Gerúndio adjetivo. |
| 13 | Rótulos, ficar | norma | `**1. Ainda há o que aprender, e há quem ensine.**` (e 2, 3) | `### 1. Ainda há o que aprender, e há quem ensine` | Ver decisão acima. |
| 14 | Levitt §1 | linha | "Steven Levitt, o economista do *Freakonomics*," | "Steven Levitt, economista e coautor do livro *Freakonomics*," | "Livro" glosa a obra. |
| 15 | Levitt §2 | linha | "Quem recebeu da moeda a ordem de mudar mudou com mais frequência. E, seis meses depois, estava mais feliz do que quem recebeu a ordem de ficar." | "Quem tirou cara mudou com mais frequência. E, seis meses depois, estava mais feliz do que quem tirou coroa." | "Mudar mudou"; o código cara/coroa acabou de ser dado. A frase da 5a não foi tocada. |
| 16 | Levitt §3 | linha | "Vale a ressalva: eram voluntários, e a felicidade foi declarada por eles mesmos. Ainda assim, … e vale justamente" | "Duas ressalvas: eram voluntários, e a felicidade foi declarada por eles mesmos. Ainda assim, … e vale justamente" | Eco "vale… vale"; família de "vale ressaltar" (frente D). |
| 17 | Griffeth | norma | "Uma meta-análise clássica sobre rotatividade, de Griffeth, Hom e Gaertner, juntou dezenas de estudos e dezenas de milhares de pessoas para descobrir" | "Griffeth, Hom e Gaertner fizeram uma meta-análise clássica sobre rotatividade: juntaram os resultados de dezenas de estudos, com dezenas de milhares de pessoas, para descobrir" | Regra 1 com dois-pontos (regra 3). "Dezenas" → etapa 7. |
| 18 | Griffeth | linha | "O melhor preditor não foi salário nem satisfação." | "O que melhor previa a saída não foi salário nem satisfação." | Evita o jargão "preditor". |
| 19 | Correlação | norma | "A correlação é moderada, perto de 0,38." | "A correlação entre intenção e saída, numa escala em que zero é nenhuma relação e 1 é relação perfeita, é moderada: perto de 0,38." | Regra 1. Não "de 0 a 1", porque vai de −1 a 1. |
| 20 | Correlação | linha | "Se a resposta honesta é sim, isso não é humor de sexta-feira. É a melhor previsão disponível do que você vai fazer, cedo ou tarde." | "Se a resposta honesta é sim, esqueça o humor de sexta-feira: você tem em mãos a melhor previsão disponível do que vai fazer, cedo ou tarde." | Tique "Não é X. É Y.". |
| 21 | Derivada | linha | "É a taxa." | "É a taxa de crescimento." | "Taxa" sozinha lê-se como juros. A glosa curta foi aprovada pelo autor: sugestão. |
| 22 | Derivada, horizonte | linha | "No fundo, é o primeiro desqualificador de Newport escrito como taxa." | "No fundo, a regra é o primeiro desqualificador de Newport escrito como taxa." | Sujeito oculto distante. |
| 23 | Derivada, horizonte | linha | "mesmo começando um pouco mais baixo" | "mesmo que ela comece um pouco mais baixo" | Sujeito ambíguo do gerúndio. |
| 24 | Rótulo, ir 1 | norma + linha | `**1. Você pensa em sair toda semana, e já usou a voz.**` | `### 1. Você pensa em sair toda semana, e já usou a 'voz'` | H3; aspas simples do sentido técnico (opcionais). |
| 25 | Ir 1 | linha | "Pedir o projeto, pedir a mudança de mesa" | "Pedir um projeto, pedir a mudança de mesa" | "O projeto" sem referente. |
| 26 | Ir 1 | linha | "Use primeiro." | "Use a voz primeiro." | Transitivo sem objeto. |
| 27 | Rótulos, ir 2 e 3 | norma | `**2. A curva achatou, …**` / `**3. Você é um running back na piscina.**` | `### 2. A curva achatou, e ninguém acima de você sabe o que você quer aprender` / `### 3. Você é um *running back* na piscina` | H3; itálico de estrangeirismo. |
| 28 | Ir 2 | linha | "usa a ideia de *tour of duty*: cada passagem" | "usa a ideia de *tour of duty*, o 'período de serviço' dos militares: cada passagem" | Origem da imagem da "missão". |
| 29 | Ir 3 | norma | "O running back é o jogador de futebol americano" (e demais ocorrências) | "O *running back*, ou corredor, é o jogador de futebol americano" | Itálico; liga a "corredores". |
| 30 | Ir 3 | linha | "mas os números contam uma história mais interessante" | "mas os números complicam essa fama" | Clichê; eco de "contam uma história" no ficar 2. |
| 31 | Ir 3 | norma | "Um levantamento com os dez maiores corredores de cada temporada da NFL" | "Um levantamento sobre os dez melhores corredores de cada temporada da NFL, a liga profissional americana," | Sigla sem glosa; "maiores" ambíguo num parágrafo de altura. Critério do ranking → etapa 7. |
| 32 | Ir 3 | linha | "olhou para a jogada" | "examinou a jogada" | Decalque de *looked at*. |
| 33 | Ir 3 | linha | "A conclusão do autor é que" | "A conclusão do autor do levantamento é que" | "Autor" ambíguo. |
| 34 | Ir 3 | linha | "O ponto, então, não é altura. É a modalidade." | "O que decide, então, é a modalidade." | Tique. |
| 35 | Ir 3, fit | norma + linha | "A literatura chama isso de *fit* entre pessoa e ambiente" | "A psicologia do trabalho chama isso de *fit* (encaixe) entre pessoa e ambiente" | Regra 1 (*fit* sem glosa); "a literatura" é autoridade vaga. Área → etapa 7. |
| 36 | Ir 3, fit | linha | "O problema é a que nunca baixa de custo." | "O problema é a que nunca fica barata." | Retoma "nunca vai ficar barato". Opcional. |
| 37 | Procure empregado | linha | "## Enquanto decide, procure empregado" | "## Procure emprego enquanto tem um" | Sem contexto, "procure empregado" = "contrate alguém". Título do autor: sugestão. |
| 38 | Kill criteria | linha | "que hoje estuda decisão" | "que hoje estuda tomada de decisão" | Precisão. |
| 39 | Kill criteria | linha | "Ela chama de *kill criteria*:" | "Ela chama isso de *kill criteria*:" | Objeto; paralelo com Newport. |
| 40 | Kill criteria | norma | "*Se eu não estiver no estado X até a data Y, eu saio.*" | entre aspas duplas, como os dois exemplos seguintes, ou citação em bloco `>` | Regra 4: itálico de destaque. |
| 41 | Kill criteria | linha | "até o fim do próximo ciclo" | "até o fim do próximo ciclo de avaliação" | Jargão de RH. |
| 42 | Kill criteria | norma | "E protege você do contrário, que é mais comum: ficar mais um ano porque já investiu três, que é o custo afundado com crachá." | "E protege você do contrário, que é mais comum: ficar mais um ano porque já investiu três. É o custo afundado (o que já foi gasto e não volta) com crachá." | Regra 1; desfaz "que é… que é". |
| 43 | Fecho | linha | "os parceiros de banda" | "os colegas de banda" | Idiomático. Opcional. |

## Tique "Não é X. É Y."

Cerca de 18 construções de contraste. Ficam as que são tese, ressalva ou decisão do autor (o
deck; "com critério, e não com desabafo"; "não existe lista de sinais. Existe sair e buscar
ajuda"; "a pergunta que eu faria não é… É esta:"; "O melhor preditor não foi… Foi a intenção";
"Não é destino, e não diz se sair é o certo. Mas…"; "olhe a derivada, não o nível" e "É a taxa";
"deixa de ser ruído e vira sinal"; "Não porque seja um corpo ruim. Porque aquele jogo paga por
outra coisa."; "a lista não basta. Precisa de uma regra."; "Mick Jones não escolheu…"). Os itens
20 e 34 cortam duas; fica no máximo uma por parágrafo.

## Sinais para outras etapas (não corrigidos aqui)

- **S1 (regra 6, etapa 7).** Nenhuma fonte tem ano no corpo. Prováveis: Levitt 2021 (REStud),
  Griffeth, Hom e Gaertner 2000, Hirschman 1970. A etapa 7 confere antes de entrarem.
- **S2 (frase fixada pelo autor).** "As duas pesquisas não se resolvem uma pela outra": um dos
  conselhos ("fique e acumule") vem de Newport, que é livro, não pesquisa. "Os dois conselhos não
  se resolvem um pelo outro" resolveria. Fica para o autor.
- **S3.** O deck em itálico vai para `subtitulo:` no frontmatter (etapa 9).
- **S4 (etapa 7).** `[VERIFICAR: saída em 1983]` e "Em setembro de 1983" precisam bater; "cortar
  o disco" (Johns) e "fundador" (Hoffman) na fila.
- **S5.** Opiniões de voz ensaística ("quase sempre o motivo é clima", "Muita gente pula…", "o
  contrário, que é mais comum") ficam; só "a imensa maioria" ganha sugestão (item 4).
