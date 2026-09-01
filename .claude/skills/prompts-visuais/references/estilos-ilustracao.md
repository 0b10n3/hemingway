# Estilos de ilustração por linha editorial

SSOT do **estilo artístico** das ilustrações (`ilu-NN`). Vale só para ilustração — gráficos
(`graf-NN`) seguem `checklist-graficos.md` e não têm estilo por linha editorial.

Criado em 31/08/2026. `brand/DESIGN.md` v2.0 define paleta, tipografia, formas e
anti-padrões, mas **não define estilo de ilustração** — esta é a camada que faltava, e ela
é subordinada ao `DESIGN.md`: em qualquer conflito, o `DESIGN.md` vence.

---

## Por que dois estilos

A Substack tem duas linhas editoriais com epistemologias opostas, e o estilo precisa carregar
essa diferença antes de o leitor ler a primeira palavra:

| Linha | O que o texto faz | O que o estilo faz |
|---|---|---|
| **Spoiler** | Reconstrói uma carreira *depois* de vivida — fragmentos de memória montados em ordem que só existe em retrospecto | **Colagem**: sentido montado a partir de pedaços recortados, camadas, imperfeição analógica |
| **Notas de um Professor** | Desmonta um mecanismo para explicá-lo — corte, peça, função | **Desenho técnico esquemático**: mecanismo aberto, projeção ortogonal, linha de construção |

Vivido *versus* explicado. A colagem monta; o esquema desmonta. Se os dois usassem o mesmo
estilo, a distinção editorial existiria só no texto.

---

## Regras compartilhadas (valem para os dois estilos)

Derivadas de `brand/DESIGN.md` §4.1, §4.5 e §5 — não são opinião desta referência:

1. **Paleta fechada.** Só os tokens de `brand/tokens/skill_test.tokens.json`. Nenhum hex fora
   da lista abaixo. Nenhuma cor "nova" porque ficou bonita.
2. **Sem glow, gradiente, glassmorphism ou blob desfocado.** `DESIGN.md` §4.5 proíbe
   explicitamente. Isto revoga a regra do "elemento iluminado" que os posts de agosto/2026
   usavam (sistema anterior "O Sinal no Escuro") — **contraste agora é por cor chapada,
   densidade e escala, nunca por luz.**
3. **Lime é acento único e escasso.** Um só ponto de lime por peça, e só onde há ação ou
   conquista real. Lime-500 sobre fundo escuro; lime-700 se o fundo for claro. Nunca lime
   como cor ambiente.
4. **Sem texto renderizado na imagem.** Gerador erra tipografia e a marca tem tipografia
   própria. Quem carrega a informação verbal é o alt-text.
5. **Sem ilustração genérica de finanças** (`DESIGN.md` §4.5): moeda, cifrão, candlestick,
   cofre, aperto de mão, robô/cérebro de IA, prédio de banco, gráfico de pizza.
6. **Sem figura humana reconhecível.** Silhueta abstrata é aceitável; rosto não.
7. **Geometria reta.** Quadro, painel, bloco e moldura com canto reto (`DESIGN.md` §4.5).

### Hex autorizados

| Papel | Token | Hex |
|---|---|---|
| Âncora institucional | forest-500 | `#1B6A45` |
| Estrutura em movimento | grove-500 | `#2D9E67` |
| Estrutura clara / traço sobre escuro | grove-300 | `#78C9A4` |
| Acento único (ação/conquista) | lime-500 | `#CDF163` |
| Acento sobre fundo claro | lime-700 | `#5F7D1C` |
| Papel / fundo claro | chalk | `#F7F7F5` |
| Fundo escuro (prancha, banda) | deepForest | `#0F3D27` |
| Fundo escuro máximo contraste | ink | `#141414` |
| Secundário / traço neutro | slate | `#4A5568` |
| Hairline / linha de construção | mist | `#E2E8F0` |
| Superfície suave | mint | `#E6F4EE` |
| Verde profundo (sombra chapada) | forest-900 | `#0A3320` |

---

## Estilo A — Spoiler: colagem editorial

**Registro:** analógico, humano, montado à mão. É a linha do relato pessoal, do erro
cometido, do "não é porque eu sofri que você também precisa sofrer" — o estilo pode ser
imperfeito porque a experiência foi.

### Vocabulário

- **Papel recortado como material dominante.** Formas em papel de cor chapada, sobrepostas em
  camadas visíveis, com sombra chapada (offset sólido em forest-900, **sem blur**) marcando a
  separação entre camadas.
- **Corte reto é o padrão; rasgo é acento.** A tesoura/guilhotina domina — mantém a
  disciplina geométrica da marca. Uma borda rasgada por peça, no máximo, e só no fragmento
  que representa o ponto de ruptura da narrativa. Isso é o que separa esta colagem de
  "colagem bagunçada genérica".
- **Retícula de meio-tom (halftone)** em uma ou duas formas — ponto visível, grande o
  bastante para ler como impressão. Não é textura decorativa: é o parente direto do padrão
  `dataGrid` da marca (`DESIGN.md` §5.2), o que ancora o estilo no sistema em vez de importá-lo
  de fora.
- **Desalinho de registro tipo risograph:** uma camada de cor deslocada 2–4px da forma que
  deveria preencher. Cor chapada, sem gradiente — riso é spot color, então isso não viola
  §4.5.
- **Fragmento de papel milimetrado / pautado** como substrato de uma camada, quando o assunto
  toca formação ou estudo.

### Regras

- Fundo: chalk `#F7F7F5` (padrão) ou deepForest `#0F3D27` (quando o texto for sobre erro,
  perda ou o "mundo invertido").
- Camadas: forest-500, grove-500, mint, slate. Máximo **quatro** cores de papel por peça —
  acima disso vira ruído.
- Lime-500 aparece **uma vez só**, na forma que representa a virada, a saída, o spoiler útil.
  Se a peça não tem virada, não tem lime.
- Composição assimétrica, com uma diagonal dominante. Colagem centralizada e simétrica soa
  cartaz institucional, não relato.

### Quando o assunto é abstrato

Não force objeto literal. Colagem aceita forma geométrica pura (círculo recortado, faixa,
escada de papel) — o material é que carrega o registro, não o motivo.

### Técnicas compositivas adicionais, avaliadas contra a marca

O vocabulário acima é de **material** (papel, corte, retícula, desalinho). Colagem editorial
tem também um repertório de **composição** — como os objetos da cena se relacionam entre si —
que a taxonomia de Olga Tkachenko, ["10 Collage Approaches You're About to Use and Get
Inspired by"](https://medium.muz.li/10-collage-approaches-youre-about-to-use-and-get-inspired-by-5c45bcb1aba4)
(Muzli/Medium), cataloga bem. Três das dez abordagens já existem no sistema com nome próprio
— **pareamento de dois objetos** é a "Fusão", **substituição de partes** é a "Substituição",
e **composição de até dois objetos com uso ativo do vazio** é "O vazio carrega peso" (ambas em
`briefing-ilustracao.md`). As demais foram avaliadas uma a uma, com o mesmo critério que o
Estilo B já aplica aos seus próprios candidatos descartados:

| Abordagem | Veredito | Por quê |
|---|---|---|
| Multiplicação/fragmentação de um objeto | **Adotar, com limite** | Serve quando o argumento *é* repetição, escala ou padrão sistêmico (ex.: efeito em cascata). Fora desse caso, conflita com "Uma ideia, uma família de objetos" (`briefing-ilustracao.md`) — usar só quando a multiplicação carrega o argumento, nunca como decoração |
| Objeto reconhecível como dispositivo de escala | **Adotar** | Já compatível com "Estranhamento de objeto comum" (`briefing-ilustracao.md`) — só nomeia um uso específico da regra que já existe |
| Composição suprematista harmonizada | **Adotar, nomear** | Já permitida implicitamente em "Quando o assunto é abstrato" acima; a mudança é dar critério explícito de harmonização (poucas formas geométricas, relação de peso e eixo clara), em vez de deixar em aberto |
| Colagem com traço desenhado à mão | **Rejeitar** | Introduz variação caligráfica; conflita com a geometria reta e o traço de espessura constante que já separam este estilo do Estilo B |
| Caos deliberado, influência Dada | **Rejeitar** | Já explicitamente descartado acima — "isso é o que separa esta colagem de colagem bagunçada genérica" |

**Proveniência cultural:** mesma regra de "Referência de cultura pop" de
`briefing-ilustracao.md` — da fonte externa se extrai a abordagem compositiva, nunca um
exemplo visual específico de um artista vivo a copiar. A tabela acima já é essa extração.

---

## Estilo B — Notas de um Professor: desenho técnico esquemático

**Registro:** preciso, construído, sem ornamento. É "um professor que já foi aluno e não se
esqueceu": mostra o mecanismo aberto, com a paciência de quem lembra como é não entender.

**Por que este estilo, e não os candidatos descartados:**

| Candidato | Veredito |
|---|---|
| **Isométrico 3D** | Descartado — `DESIGN.md` §4.5 proíbe "3D render look", e isométrico corporativo é o estilo mais genérico de conteúdo tech/fintech gerado por IA |
| **Blueprint clássico** (branco sobre ciano) | Paleta descartada (ciano não existe na marca); **gramática aproveitada** — linha de construção, projeção ortogonal, cota. É a base deste estilo, repintada na paleta da marca |
| **Risograph / impressão analógica** | Descartado aqui — é o registro analógico, que pertence ao Spoiler. Usar nos dois colapsaria a distinção |
| **Construtivista / Bauhaus** | Descartado — geometria chapada é on-brand, mas é registro *expressivo*, não *explicativo*. Esta linha precisa mostrar mecanismo, não afirmar atitude |

O estilo escolhido é o que a marca já descreve para si mesma sem nomear: `DESIGN.md` posiciona
a Syntaxis como "instrumento de precisão: mais terminal financeiro, menos SaaS genérico"
(linha 10) e trata hairline como assinatura — "o grid é visível, como em terminal/planilha:
precisão desenhada, não caixas flutuantes" (§4.4.3). As três famílias de padrão da marca (§5.2)
já são vocabulário esquemático: nó-e-galho é diagrama de árvore, grade de dados é papel
milimetrado. Este estilo não importa uma estética — formaliza a que já está no sistema.

### Vocabulário

- **Projeção ortogonal.** Vista frontal, corte ou vista explodida. Sem perspectiva, sem
  ponto de fuga, sem profundidade falsa.
- **Linha de construção visível.** Hairline mist `#E2E8F0` (sobre escuro) ou slate `#4A5568`
  (sobre claro) marcando eixo, centro, alinhamento e extensão — a linha auxiliar fica na peça,
  como em prancha técnica real. É o que faz o desenho parecer construído, não desenhado.
- **Chamada com linha-guia** (*leader line*) apontando para a peça que importa — terminando
  em ponto ou seta fina, **sem rótulo de texto** (o alt-text carrega o nome).
- **Corte / vista explodida** quando o argumento for "por dentro isto é assim": camadas
  separadas por espaço regular, alinhadas no mesmo eixo.
- **Marca de cota** (linha fina com terminação em traço reto) quando o argumento envolver
  prazo, distância ou proporção — nunca com número escrito.
- **Grade de pontos** (`dataGrid` da marca) nas margens, opacidade baixa, só como respiro.

### Regras

- Fundo: deepForest `#0F3D27` (padrão — é a prancha) ou chalk `#F7F7F5` para peças claras.
- Estrutura principal: grove-300 `#78C9A4` sobre escuro; forest-500 `#1B6A45` sobre claro.
- Linha de construção e auxiliares sempre um degrau abaixo da estrutura em contraste — elas
  organizam, não competem.
- Lime-500 marca **uma** peça: o elemento que o parágrafo está explicando naquele ponto. O
  resto do mecanismo fica em verde estrutural. É o equivalente visual de apontar o dedo.
- Simetria e alinhamento rigorosos. Composição centrada é permitida aqui (ao contrário do
  Spoiler) — é prancha técnica, ordem é o assunto.
- Traço de espessura constante. Sem variação caligráfica, sem "traço à mão".

---

## Como escrever o prompt

A sintaxe específica do gerador — formato de prompt, checklist de fechamento, proporções
suportadas — mora em `references/geradores/<gerador-ativo>.md`, não aqui: esta seção do
arquivo é vocabulário e regra **agnósticos** de marca/composição (o que vale qualquer que
seja o gerador); a sintaxe de chamada é camada condicional, separada desde 31/08/2026 (ver
`pesquisa/frente-e-visuais/02-proposta.md`, item B.4). Gerador ativo hoje: **Nano Banana Pro**
— ver `references/geradores/nano-banana-pro.md`.

---

## Quando a linha editorial não está declarada

**Pare e pergunte.** Não infira o estilo a partir da voz do texto: voz e linha editorial não
são a mesma coisa, e já houve caso real disso no repositório — o post
`2026-08-25-dividir-para-nao-correr-risco` foi escrito em voz **ensaística** sobre um produto
de renda fixa, e o próprio briefing registrou que isso o tornava ambíguo entre as duas linhas
(`processo/01-briefing.md`). Escolher estilo por dedução silenciosa nesse caso teria dado a um
texto de produto a estética do relato pessoal, sem ninguém decidir isso.
