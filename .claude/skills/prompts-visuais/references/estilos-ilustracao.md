# Estilo de ilustração

SSOT do **estilo artístico** das ilustrações (`ilu-NN`). Vale só para ilustração — gráficos
(`graf-NN`) seguem `checklist-graficos.md` e não têm estilo por linha editorial.

Criado em 31/08/2026 (atualizado em 04/09/2026 — sincronização com a v3.0). `brand/DESIGN.md`
(hoje v3.0) define paleta, tipografia, formas, anti-padrões e, desde a rodada 3, o mecanismo
de profundidade da própria camada de ilustração (§7 — collage/paper cut, subordinado a este
repositório como único consumidor). Este arquivo é a especificação executável dessa camada
para o pipeline: em qualquer conflito, o `DESIGN.md` vence.

**Revisão de 2026-09-01:** até esta data, o sistema tinha dois estilos por linha editorial
(colagem para Spoiler, desenho técnico esquemático para Notas de um Professor). A pedido do
autor, os dois foram unificados num único estilo — colagem editorial — para todo post,
qualquer que seja a linha. Ver "Por que um estilo só", abaixo, e
`pesquisa/epico-figuras-em-ilustracao/` para o histórico da decisão.

---

## Por que um estilo só

Até 2026-09-01, o sistema argumentava que Spoiler (relato vivido, retrospectivo) e Notas de
um Professor (mecanismo explicado) precisavam de técnicas de renderização inteiras diferentes
para que a distinção editorial existisse também no visual, não só no texto. Na prática, isso
custava caro: duas gramáticas de estilo para manter, e a decisão de linha editorial virava
pré-requisito bloqueante da etapa 8 (`post-substack/SKILL.md`, etapa 1: "sem esse campo, a
etapa 8 para e pergunta").

O autor decidiu simplificar: **colagem editorial é o material de todo post**, sem exceção. A
distinção entre "vivido" e "explicado" continua existindo — só que agora vive inteiramente no
texto (voz, estrutura, conteúdo) e, dentro da própria colagem, na **composição** escolhida
para cada peça (ver "Quando o argumento pede precisão mecânica", abaixo) — não mais numa
técnica de renderização à parte. Isso também resolve, de graça, o bloqueio da etapa 8 em linha
editorial ambígua ou não declarada: o estilo não depende mais dessa decisão.

O vocabulário técnico que pertencia ao antigo "Estilo B" (desenho técnico esquemático) não foi
descartado — foi absorvido como uma família de técnicas compositivas disponíveis dentro da
colagem, para quando o argumento do post for "mostrar um mecanismo por dentro" (ver a mesma
seção abaixo).

---

## Regras

Regras 1, 2, 3, 4 e 6 são derivadas de `brand/DESIGN.md` §4.1, §4.5 e §7 — não são opinião
desta referência. A regra 5 (figura humana) **não** deriva de `DESIGN.md` — é critério próprio
deste repositório, revisado em 2026-09-01 (ver `pesquisa/epico-figuras-em-ilustracao/`); a
versão anterior ("sem figura humana reconhecível, rosto não") alegava a mesma proveniência de
marca sem base real no documento — checado linha a linha, `DESIGN.md` não menciona figura
humana, rosto ou retrato em nenhum ponto.

**Revisão de 2026-09-02:** a antiga regra 5 ("sem ilustração genérica de finanças" — moeda,
cifrão, candlestick, cofre, aperto de mão, robô/cérebro de IA, prédio de banco, gráfico de
pizza) foi **removida**. Diferente da revisão acima, esta regra tinha base real em
`brand/DESIGN.md` §4.5 — a remoção é uma **divergência deliberada e documentada**, só para
ilustração editorial de post (este repositório), a pedido do autor. `brand/DESIGN.md`
continua valendo sem alteração para o resto do ecossistema Syntaxis (produto, curso,
marketing) — ver `pesquisa/epico-iconografia-financeira/` para o raciocínio completo. Moeda,
candlestick, robô e os demais itens da lista antiga passam a ser objetos de Camada 2/3
disponíveis como qualquer outro (`briefing-ilustracao.md`), sujeitos às mesmas regras de
sempre: paleta fechada, colagem editorial, sem clichê de banco de imagens (ver "Erros
recorrentes" em `briefing-ilustracao.md`) e sem reprodução literal de propriedade de terceiros
(ver "Referência de cultura pop", também em `briefing-ilustracao.md`) quando a ideia vier de
uma referência externa (ex.: um robô de ficção científica específico).

1. **Paleta fechada.** Só os tokens de `brand/tokens/syntaxis.tokens.json`. Nenhum hex fora
   da lista abaixo. Nenhuma cor "nova" porque ficou bonita.
2. **Sem glow, gradiente, glassmorphism, blob desfocado ou sombra — nenhuma exceção, nem
   "chapada sem blur".** `DESIGN.md` §4.5 proíbe glow/gradiente/glassmorphism explicitamente;
   §7.1/§7.2 (regra 4) fecha a lacuna que ainda restava — **sombra projetada é anti-padrão em
   qualquer forma, mesmo sólida e sem blur.** Isto revoga duas regras antigas em sequência: o
   "elemento iluminado" dos posts de agosto/2026 (contraste por glow verde sobre fundo escuro)
   e, mais recentemente, a "sombra chapada" que substituiu o glow mas nunca foi validada contra
   `DESIGN.md` (achado S7, `brand/REVOGACOES.md`) — **profundidade agora é só degrau de tom
   entre os hex da pilha** (ver "A escada", abaixo), nunca luz nem sombra.
3. **Lime é acento único e escasso.** Um só ponto de lime por peça, e só onde há ação ou
   conquista real (ou, em peça de mecanismo, só na peça que o parágrafo está explicando
   naquele ponto — ver "Quando o argumento pede precisão mecânica"). Lime-500 sobre fundo
   escuro; lime-700 se o fundo for claro. Nunca lime como cor ambiente.
4. **Sem texto renderizado na imagem.** Gerador erra tipografia e a marca tem tipografia
   própria. Quem carrega a informação verbal é o alt-text.
5. **Figura humana reconhecível — critério em três faixas, não proibição absoluta.** Silhueta
   abstrata sempre foi e continua aceitável. Rosto reconhecível segue o critério de
   "Figuras históricas e públicas", abaixo — a maioria dos casos (pessoa privada, decoração
   sem função editorial) continua proibida; o que muda é que figura histórica ou pública
   diretamente relevante ao argumento do texto ganhou caminho explícito.
6. **Geometria reta.** Quadro, painel, bloco e moldura com canto reto (`DESIGN.md` §4.5).

### Figuras históricas e públicas

Três faixas, do mais livre ao proibido. Todas exigem que a pessoa seja citada pelo nome no
corpo do post — nunca decoração externa ao texto — e tratamento sempre dentro do vocabulário
de colagem (ver "Como desenhar um rosto", abaixo), nunca fotorrealista.

- **Faixa 1 — figura histórica: sempre permitida, sem pergunta ao autor.** Falecida e com
  presença padrão em material didático/de referência do campo que o post trata (matemática,
  economia, finanças) — o teste é "esse rosto já aparece em livro-texto ou enciclopédia sem
  controvérsia", não uma data de corte arbitrária. Um caso limítrofe (falecimento recente,
  ainda socialmente sensível) desce para a Faixa 2 por precaução.
- **Faixa 2 — figura pública viva, discutida no papel profissional específico do texto:
  permitida, mas vira pergunta nomeada no briefing visual (etapa 8), levada ao gate humano
  (etapa 10)** — mesmo tratamento que a etapa 1 do `post-substack/SKILL.md` já dá à linha
  editorial ambígua. Condição adicional: a peça nunca pode implicar endosso da pessoa ao post,
  produto ou à Syntaxis, e o retrato se limita à capacidade profissional citada — nunca vida
  pessoal ou contexto alheio ao motivo da citação.
- **Faixa 3 — pessoa privada: nunca**, sem exceção, mesmo que nomeada no texto (ex.: um
  cliente, colega ou fonte anônima de um post de linha Spoiler).

Tratamento sempre respeitoso, nunca caricato ou satírico. O rosto é só **um** elemento da
composição — as regras de "um ponto de tensão só" e "uma ideia por peça"
(`briefing-ilustracao.md`, Passo 4) continuam valendo; a peça não vira retrato solto, precisa
estar ancorada num conceito do Passo 6, como qualquer outra `ilu-NN`.

### Hex autorizados

Tabela reorganizada nos papéis semânticos de `illustration.*` (`brand/tokens/syntaxis.tokens.json`,
§7 do `DESIGN.md`) — mesmos hexes de sempre, moldura corrigida: **pilha** é a escada de
profundidade (a "escada", abaixo — nunca inclui grove nem lime), **figura** é o que fica sobre
a pilha sem nunca empilhar, **acento** é só o lime, escasso e com teto de área.

| Papel | Token | Hex |
|---|---|---|
| Pilha escura, nível 1 (mais escuro) | `illustration.stack.dark.layer1` (ink) | `#141414` |
| Pilha escura, nível 2 | `illustration.stack.dark.layer2` (deepForest) | `#0F3D27` |
| Pilha escura, nível 3 | `illustration.stack.dark.layer3` (forest-700) | `#125233` |
| Pilha escura, nível 4 (mais claro) | `illustration.stack.dark.layer4` (forest-500) | `#1B6A45` |
| Pilha clara, nível 1 (mais escuro) | `illustration.stack.light.layer1` (mist) | `#E2E8F0` |
| Pilha clara, nível 2 | `illustration.stack.light.layer2` (mint) | `#E6F4EE` |
| Pilha clara, nível 3 (mais claro) | `illustration.stack.light.layer3` (chalk) | `#F7F7F5` |
| Figura, sobre a pilha (nunca empilha) | `illustration.figure.primary` (grove-500) | `#2D9E67` |
| Figura, traço sobre escuro | `illustration.figure.secondary` (grove-300) | `#78C9A4` |
| Acento único (ação/conquista) | `illustration.accent` (lime-500) | `#CDF163` |
| Acento sobre pilha clara | lime-700 | `#5F7D1C` |
| Secundário / traço neutro | slate | `#4A5568` |

### A escada — como escrever profundidade sem sombra

Duas camadas adjacentes da pilha diferem por **um degrau de luminância pequeno e regular**
(0,017–0,046, medido e travado em `DESIGN.md` §7.1), nunca por sombra projetada — é o que faz
a peça ler como papel empilhado sem violar a regra 2, acima.

**Lição cara, já paga uma vez — vale para todo prompt novo:** linguagem **comparativa** entre
folhas ("cada camada claramente mais clara que a anterior") faz o gerador inflar o intervalo e
sair da paleta. Use **âncora absoluta**: cite o hex de cada folha, mais um adjetivo de família
("verdes escuros e profundos, não médios nem claros"), nunca uma comparação relativa entre
folhas.

**Descreva a cena como imagem de scanner de mesa, luz idêntica em todo o quadro** — é a
alavanca mais forte contra sombra projetada. Cada folha é "uma cor perfeitamente uniforme de
borda a borda, o mesmo tom no meio e na margem". Na borda de uma abertura (onde uma camada
revela a de baixo), não há espessura de papel visível nem escurecimento de borda — "no visible
paper thickness, no wall, no bevel, no darkening at the rim" é a frase que resolve isso no
prompt.

Tetos numéricos, verificáveis, não de gosto (`illustration.*` em `syntaxis.tokens.json`):

| Regra | Valor | Token |
|---|---|---|
| Matizes de pilha por peça | 1, mais um neutro estrutural | `illustration.maxHues` |
| Cores ≥1% do quadro | entre 3 e 7 | `illustration.maxColors` |
| Fundo mínimo do quadro | 40% | `illustration.minBackground` |
| Acento (lime) do quadro | até 1%, medido 0,35% na peça de referência | `illustration.accentMaxCoverage` |
| Granulação, amplitude de luminância | abaixo de 0,028 (um degrau da escada) | `illustration.grainMaxLuminanceAmplitude` |

---

## Colagem editorial

**Registro:** analógico, humano, montado à mão — sentido montado a partir de pedaços
recortados, camadas, imperfeição analógica controlada. Vale para todo post, qualquer linha
editorial; o registro pode pender mais para o pessoal/imperfeito (Spoiler) ou mais para o
preciso/construído (Notas de um Professor) através da composição escolhida, não da técnica.

### Vocabulário

- **Papel recortado como material dominante.** Formas em papel de cor chapada, sobrepostas em
  camadas visíveis, separadas por **degrau de tom** entre os hex da pilha (ver "A escada",
  acima) — nunca sombra, nem chapada.
- **Corte reto é o padrão; rasgo é acento.** A tesoura/guilhotina domina — mantém a
  disciplina geométrica da marca. Uma borda rasgada por peça, no máximo, e só no fragmento
  que representa o ponto de ruptura da narrativa. Isso é o que separa esta colagem de
  "colagem bagunçada genérica".
- **Retícula de meio-tom (halftone)** em uma ou duas formas — ponto visível, grande o
  bastante para ler como impressão. **Construída peça a peça, não derivada de
  `pattern.reticula` da camada de sistema** — `DESIGN.md` §7.3 exige separação estrita entre
  as duas camadas desde a rodada 3 (decisão A6): a retícula de ilustração é regra própria
  desta seção, não herança do sistema.
- **Desalinho de registro tipo risograph:** uma camada de cor deslocada 2–4px da forma que
  deveria preencher. Cor chapada, sem gradiente — riso é spot color, então isso não viola
  §4.5.
- **Fragmento de papel milimetrado / pautado** como substrato de uma camada, quando o assunto
  toca formação ou estudo.
- **Como desenhar um rosto (Faixa 1/2 de "Figuras históricas e públicas", acima):** rosto como
  composição de papel recortado — formas geométricas simples (elipse, triângulo, faixa)
  compondo só os traços mínimos que tornam a pessoa reconhecível, mesma disciplina de material
  do resto da peça (corte reto padrão, degrau de tom entre camadas, retícula opcional numa
  camada, paleta fechada). Retrato-colagem editorial de revista, nunca ilustração de rosto
  realista.

### Regras

- Fundo: chalk `#F7F7F5` (padrão) ou deepForest `#0F3D27` (quando o texto for sobre erro,
  perda, "mundo invertido", ou quando a peça for de mecanismo/precisão — ver abaixo). Fundo
  ocupa no mínimo 40% do quadro (`illustration.minBackground`).
- Camadas: um matiz de pilha só, mais um neutro estrutural (`illustration.maxHues`) — ver "A
  escada", acima, para os hex exatos por nível. Figura (grove-500, ou grove-300 sobre fundo
  escuro) fica sobre a pilha, nunca é mais um degrau dela. Entre 3 e 7 cores ≥1% do quadro no
  total (`illustration.maxColors`) — acima disso vira ruído.
- Lime-500 aparece **uma vez só**, na forma que representa a virada, a saída, o spoiler útil —
  ou, em peça de mecanismo, a peça que o parágrafo está explicando naquele ponto. Se a peça
  não tem virada nem ponto de explicação, não tem lime. Teto de área: 1% do quadro, medido
  0,35% na peça de referência (`illustration.accentMaxCoverage`).
- Composição assimétrica, com uma diagonal dominante, é o padrão — colagem centralizada e
  simétrica soa cartaz institucional, não relato. **Exceção:** quando o argumento é mostrar um
  mecanismo em corte/vista explodida (ver abaixo), composição centrada e simétrica é aceitável
  — ali, ordem visual é o próprio argumento.

### Quando o assunto é abstrato

Não force objeto literal. Colagem aceita forma geométrica pura (círculo recortado, faixa,
escada de papel) — o material é que carrega o registro, não o motivo.

### Quando o argumento pede precisão mecânica

Herdado do antigo "Estilo B" (desenho técnico esquemático, retirado em 2026-09-01) — não é
outra técnica de renderização, é vocabulário de **composição** dentro da mesma colagem de
papel recortado, para quando o argumento for "por dentro isto funciona assim":

- **Vista em corte / explodida, em papel.** Camadas de papel separadas por espaço regular,
  alinhadas no mesmo eixo, cada uma um componente do mecanismo — a mesma disciplina de degrau
  de tom e corte reto do resto do vocabulário, só que a composição é ortogonal (vista
  frontal), sem perspectiva nem profundidade falsa.
- **Linha de construção como tira fina de papel** (mist `#E2E8F0` sobre escuro, slate
  `#4A5568` sobre claro) marcando eixo, centro ou alinhamento — não é hairline vetorial, é uma
  tira de papel cortada fina o bastante para ler como linha auxiliar.
- **Chamada com linha-guia**, também em papel cortado fino, apontando para a peça que importa
  — terminando em ponto ou seta recortada, **sem rótulo de texto** (o alt-text carrega o
  nome).
- **Marca de cota em papel** (tira fina com terminação em corte reto) quando o argumento
  envolver prazo, distância ou proporção — nunca com número escrito.
- **Grade de pontos**, construída peça a peça (não derivada de `pattern.reticula` do sistema —
  ver "Retícula de meio-tom", acima) como camada de fundo, opacidade baixa, só como respiro —
  pode ser retícula de meio-tom bem espaçada, mantendo o vocabulário de material.

Nessa família de composição, fundo deepForest é o mais comum (é "a prancha"), estrutura
principal em grove-300 sobre escuro ou forest-500 sobre claro, e simetria/alinhamento
rigoroso é aceitável (ver exceção de composição, acima). Isso não é um "modo alternativo" —
continua sendo papel recortado, degrau de tom, paleta fechada; só a disposição dos objetos
muda para servir o argumento de mecanismo.

### Técnicas compositivas adicionais, avaliadas contra a marca

O vocabulário acima é de **material** (papel, corte, retícula, desalinho). Colagem editorial
tem também um repertório de **composição** — como os objetos da cena se relacionam entre si —
que a taxonomia de Olga Tkachenko, ["10 Collage Approaches You're About to Use and Get
Inspired by"](https://medium.muz.li/10-collage-approaches-youre-about-to-use-and-get-inspired-by-5c45bcb1aba4)
(Muzli/Medium), cataloga bem. Três das dez abordagens já existem no sistema com nome próprio
— **pareamento de dois objetos** é a "Fusão", **substituição de partes** é a "Substituição",
e **composição de até dois objetos com uso ativo do vazio** é "O vazio carrega peso" (ambas em
`briefing-ilustracao.md`). As demais foram avaliadas uma a uma:

| Abordagem | Veredito | Por quê |
|---|---|---|
| Multiplicação/fragmentação de um objeto | **Adotar, com limite** | Serve quando o argumento *é* repetição, escala ou padrão sistêmico (ex.: efeito em cascata). Fora desse caso, conflita com "Uma ideia, uma família de objetos" (`briefing-ilustracao.md`) — usar só quando a multiplicação carrega o argumento, nunca como decoração |
| Objeto reconhecível como dispositivo de escala | **Adotar** | Já compatível com "Estranhamento de objeto comum" (`briefing-ilustracao.md`) — só nomeia um uso específico da regra que já existe |
| Composição suprematista harmonizada | **Adotar, nomear** | Já permitida implicitamente em "Quando o assunto é abstrato" acima; a mudança é dar critério explícito de harmonização (poucas formas geométricas, relação de peso e eixo clara), em vez de deixar em aberto |
| Colagem com traço desenhado à mão | **Rejeitar** | Introduz variação caligráfica; conflita com a geometria reta e o traço de espessura constante que o vocabulário de precisão mecânica exige quando ativado |
| Caos deliberado, influência Dada | **Rejeitar** | Já explicitamente descartado acima — "isso é o que separa esta colagem de colagem bagunçada genérica" |

**Proveniência cultural:** mesma regra de "Referência de cultura pop" de
`briefing-ilustracao.md` — da fonte externa se extrai a abordagem compositiva, nunca um
exemplo visual específico de um artista vivo a copiar. A tabela acima já é essa extração.

---

## Como escrever o prompt

A sintaxe específica do gerador — formato de prompt, checklist de fechamento, proporções
suportadas — mora em `references/geradores/<gerador-ativo>.md`, não aqui: esta seção do
arquivo é vocabulário e regra **agnósticos** de marca/composição (o que vale qualquer que
seja o gerador); a sintaxe de chamada é camada condicional, separada desde 31/08/2026 (ver
`pesquisa/frente-e-visuais/02-proposta.md`, item B.4). Gerador ativo hoje: **Nano Banana Pro**
— ver `references/geradores/nano-banana-pro.md`.
