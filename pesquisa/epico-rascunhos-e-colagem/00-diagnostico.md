# Diagnóstico — rascunhos como entrada e fluxo de capa/ilustração

Criado em 2026-09-01, a partir de um pedido direto do autor: o pipeline trata hoje o arquivo
de entrada como **transcrição de áudio** (etapa 0: "cópia limpa, hesitação removida"), mas
pelo menos um caso real já é um **rascunho escrito**, com instruções e sugestões embutidas
para o próprio processo. O mesmo pedido cobre revisão do fluxo de capa/ilustração (validar
sugestão do autor, dar espaço a ideia própria do executor, ler o rascunho em busca de
sugestões soltas) e o uso do estilo de colagem com revisão de marca. Gráficos e diagramas
ficam fora — o autor pediu explicitamente para não mexer aí.

Cada achado abaixo cita arquivo e trecho, seguindo a regra do `CLAUDE.md`
("Evidência ou silêncio").

---

## 1. O caso real: `2026-09-01-quando-os-modelos-se-rebelam` já é um rascunho, não uma transcrição

`_arquivo/transcricoes/2026-09-01_Quando_os_modelos_se_rebelam.md` abre com:

```
[LINHA EDITORIAL: Spoiler]
[CAPA: Como ideia para criativo de capa, podemos utilizar algo como uma rebelia de máquinas
humanoides como nos filmes de Terminator]
```

E no corpo, dois pontos de instrução ao processo, não de conteúdo a preservar:

- Seção 3: `[escrever um breve prágrafo sobre o que é o modelo e pq ele é tao famoso.]`
- Fechamento: `[tentar reescrever o parágrafo acima. Existem teorias em financas. ]`

Nenhum desses quatro marcadores é fala transcrita de uma gravação. São notas de um autor
escrevendo um rascunho e deixando instruções para quem (ou o quê) vai desenvolvê-lo — mais
próximo de comentário de editor em manuscrito do que de "hesitação a remover".

**O pipeline lidou bem com isso — mas por julgamento no momento, não por regra escrita.**
Evidência: `posts/2026-09-01-quando-os-modelos-se-rebelam/processo/01-briefing.md` linhas
80–93 tem uma seção inteira, "Pendências que a etapa 4 precisa resolver", narrando a decisão
de tratar os colchetes como instrução e não como texto — mas essa seção existe porque o
executor decidiu criá-la, não porque `post-substack/SKILL.md` pede isso. Nada na etapa 0
("Ingestão... cópia limpa, hesitação removida, palavras do autor preservadas" —
`post-substack/SKILL.md` linha 46) distingue "palavra do autor a preservar" de "instrução do
autor ao processo" — as duas convivem no mesmo arquivo cru e, sem essa distinção escrita,
uma sessão futura sob pressão de contexto poderia perfeitamente tratar `[escrever um breve
parágrafo...]` como texto a limpar e preservar, em vez de ordem de serviço a executar e
descartar.

## 2. A tensão de linha editorial foi registrada, mas nunca virou pergunta

`01-briefing.md` (linhas 63–78) identifica que o **assunto** do post (modelagem financeira,
sem relato de carreira) se encaixaria melhor em "Notas de um Professor", mas o autor já havia
declarado `[LINHA EDITORIAL: Spoiler]` no arquivo de origem. A skill manda "registre a
ambiguidade e leve ao gate humano" (`post-substack/SKILL.md` linha 75) — o que aconteceu foi
registro em prosa dentro do briefing, carregado como item de `pendencias` em `estado.json` até
a etapa 10, junto com dois `[VERIFICAR]` de fonte primária sem relação nenhuma com a decisão
de linha editorial. A aprovação em `estado.json` ("aprovado para publicação... tensão sobre
linha editorial... registrada mas não resolvida — autor optou por manter Spoiler") sugere que
ninguém perguntou "Spoiler ou Notas de um Professor?" como decisão binária no gate — a tensão
foi carregada, diluída numa lista, e resolvida por omissão a favor do que já estava escrito.
Isso importa porque a linha editorial **determina o estilo artístico da capa e das
ilustrações** (`post-substack/SKILL.md` linha 78) — uma decisão de linha tomada por inércia
decide, em cascata, o estilo visual inteiro do post sem que o autor tenha, de fato, escolhido.

## 3. O fluxo de capa já faz o que o autor está pedindo — mas como exceção, não como regra

`posts/2026-09-01-quando-os-modelos-se-rebelam/capa.md`, seção "Proveniência" (linhas 18–25),
é exatamente o comportamento que o autor descreveu no pedido: pega a sugestão do rascunho
("uma rebelia de máquinas humanoides como nos filmes de Terminator"), avalia (descarta a
referência por ser propriedade de terceiros e incompatível com o estilo de colagem), extrai a
**estrutura** da ideia (uma ferramenta que não decide nada, e é essa obediência cega que
produz o desastre) e a leva adiante como um conceito novo e coerente com a marca.

Isso é uma execução exemplar do princípio já existente em
`.claude/skills/prompts-visuais/references/briefing-ilustracao.md` ("A metáfora do autor é a
semente. Seu trabalho é levá-la adiante, não substituí-la", linha 14) — mas **nada no método
exige esse tratamento especificamente para uma sugestão de peça visual pronta**. O Passo 1
("Colher o material, em três camadas") trata "a imaginação do autor" como uma categoria ampla
— analogias, metáforas, referências de cultura pop, título — sem separar "ideia de imagem já
pronta e explícita, sugerida por fora do corpo do texto" como um caso com contrato próprio:
avaliar, decidir (aproveitar estrutura / aproveitar literal / descartar) e **registrar a
proveniência por escrito**. O que existe em `capa.md` é uma seção "Proveniência" que a própria
skill não define nem exige em lugar nenhum — se não tivesse havido essa iniciativa pontual, a
sugestão do autor poderia ter sido silenciosamente ignorada ou copiada ao pé da letra
(reproduzindo Terminator, o que violaria a regra de propriedade intelectual de
`briefing-ilustracao.md` linha 180).

## 4. Nada obriga o executor a gerar alternativa própria quando o autor já sugeriu algo

O Passo 3 de `briefing-ilustracao.md` (as três operações — extensão, cruzamento, torção) é
generativo por natureza, mas se aplica a **qualquer** semente, sugerida ou não. Não há
distinção entre "o autor não deu ideia nenhuma, gere conceitos do zero" e "o autor deu uma
ideia pronta, gere pelo menos uma alternativa independente para comparar antes de decidir". Na
prática, o caso real (`capa.md`) só produziu **um** conceito final (a alavanca) — não há
registro de um segundo conceito descartado especificamente em contraste com a sugestão do
autor, ao contrário do padrão que `08-briefing-visual.md` já aplica para escolha entre
conceitos concorrentes em geral. Ou seja: mesmo no melhor caso já observado, o sistema não
force brainstorming paralelo quando existe uma sugestão de partida — o risco natural é ancorar
demais na primeira ideia (do autor ou do próprio executor) sem comparação real.

## 5. Sugestões de visual soltas no meio do texto não têm rota de captura

O único padrão hoje reconhecido é o marcador dedicado `[CAPA: ...]` no topo do arquivo. Não há
instrução em nenhuma etapa (0, 1, 2 ou 8) para varrer o rascunho inteiro atrás de sugestões de
ilustração que apareçam soltas no corpo — por exemplo, um comentário entre parênteses no meio
de um parágrafo, ou uma frase do tipo "isso dava uma imagem boa de tal coisa", sem marcador
formal. Neste caso real não havia esse tipo de sugestão solta (só a de capa, já marcada), mas
nada garante que o próximo rascunho mantenha esse hábito de marcar tudo no topo — e nada no
processo hoje pede, explicitamente, essa varredura.

## 6. O estilo de colagem já existe e é rigoroso — mas o vocabulário é só material, não compositivo

`.claude/skills/prompts-visuais/references/estilos-ilustracao.md`, "Estilo A — Spoiler:
colagem editorial" (linhas 66–106), já define um sistema fechado e bem fundamentado: papel
recortado como material dominante, corte reto vs. rasgo como acento raro, retícula de
meio-tom, desalinho tipo risograph, paleta de no máximo quatro papéis, lime como acento único.
Isso é vocabulário de **material e textura**. O que falta é vocabulário de **composição** —
como os objetos da cena se relacionam entre si — e é justamente aí que a referência que o
autor apontou (Olga Tkachenko, "10 Collage Approaches", Muzli/Medium) ajuda: ela cataloga
abordagens compositivas (pareamento de dois objetos, substituição de partes, composição
suprematista harmonizada, caos deliberado de inspiração Dada, multiplicação/fragmentação de
objetos, mistura com desenho à mão, composição de dois objetos com uso ativo do vazio), não
técnicas de material.

Cruzando essa lista com o que já existe no repositório:

| Abordagem (Tkachenko) | Já coberta hoje? | Onde |
|---|---|---|
| Pareamento de dois objetos formando uma imagem única | Sim — é a "Fusão" | `briefing-ilustracao.md` linha 152, tabela de estrutura de metáfora |
| Substituição de partes / combinação inesperada | Sim — é a "Substituição" | idem, linha 154 |
| Composição de até 2 objetos com uso ativo do vazio | Sim — "O vazio carrega peso" | `briefing-ilustracao.md` linha 120 |
| Caos controlado, influência Dada | **Não — e deve continuar rejeitada** | `estilos-ilustracao.md` linha 80: "isso é o que separa esta colagem de colagem bagunçada genérica" |
| Composição suprematista harmonizada | Parcial | `estilos-ilustracao.md` linha 102, "Quando o assunto é abstrato" aceita forma geométrica pura, mas não nomeia o movimento nem dá critério de "harmonização" |
| Multiplicação / fragmentação de um objeto | **Não coberta** | sem entrada equivalente hoje |
| Objeto reconhecível como dispositivo de escala | **Não coberta** | sem entrada equivalente hoje |
| Colagem complementada com traço à mão | Parcial | `estilos-ilustracao.md` linha 88 permite fragmento de papel milimetrado como substrato, mas não traço desenhado |

Ou seja: três das dez abordagens já estão embutidas no sistema (com nome próprio, inclusive
mais preciso que o artigo genérico), uma deve continuar explicitamente fora por conflito com a
identidade de marca (a disciplina geométrica é regra de `DESIGN.md`, não gosto), e as demais
são material real para enriquecer o vocabulário — mas nenhuma delas deveria entrar sem o mesmo
filtro que `estilos-ilustracao.md` já aplica a outros candidatos (ver "Estilo B", a tabela de
candidatos descartados nas linhas 114–121: cada abordagem nova precisa do mesmo veredito
explícito, a favor ou contra).

## 7. Não existe checagem mecânica do pixel entregue — só do texto do prompt

`.claude/skills/revisao-editorial/SKILL.md`, item 10 (linhas 60–69): a checagem de paleta é um
`grep` por hex de 6 dígitos **no texto** de `capa.md`, `ilustracoes.md` e `infograficos.md`,
comparado contra `brand/tokens/skill_test.tokens.json`. Isso confirma que o *prompt* só cita
cores autorizadas. Não confirma que a *imagem gerada* pelo Nano Banana Pro de fato saiu com
essas cores — geradores de imagem são conhecidos por não aderir 100% ao hex pedido no prompt
(drift de cor é um problema documentado na indústria; ver pesquisa externa em
`01-proposta.md`). O próprio item 10 já reconhece o análogo para `graficos.md`/`diagramas.md`
("a isenção pressupõe que o código roda com sucesso") — ali existe pelo menos a possibilidade
de rodar o código e checar de verdade. Para `ilu-NN`/`capa`, não existe hoje nenhuma etapa,
mecânica ou humana, que abra o PNG final e confira a paleta de fato usada antes do gate
humano aprovar.

No caso real (`2026-09-01`), isso ainda não mordeu porque a capa e a `ilu-01` "seguem como
prompt, não geradas" (`estado.json`, campo `aprovacoes`) — mas o gate humano já aprovou o post
sem essa peça existir, o que significa que a checagem de cor real, quando a imagem for
finalmente gerada, vai acontecer (se acontecer) fora do pipeline documentado, não dentro dele.

## 8. Fora do escopo deste diagnóstico

`graficos.md` e `diagramas.md` não entram — o autor pediu explicitamente para manter como
está, e o diagnóstico do item 7 já explica por que eles não têm o mesmo problema (o código lê
`tokens.json` em runtime, a cor é determinística, não gerada por um modelo de imagem).
