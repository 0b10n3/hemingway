# Diagnóstico — a proibição de iconografia financeira genérica, revisitada

Criado em 2026-09-02, a partir de um pedido direto do autor: a regra 5 de
`estilos-ilustracao.md` ("sem ilustração genérica de finanças" — moeda, cifrão, candlestick,
cofre, aperto de mão, robô/cérebro de IA, prédio de banco, gráfico de pizza) está bloqueando
peças que não deveriam ser bloqueadas. Pedido explícito: robô, moeda e candlestick devem
voltar a ser permitidos, e a regra de marca para criação de imagens deve ficar bem menos
restritiva em geral.

Cada achado cita arquivo e trecho, seguindo a regra do `CLAUDE.md` ("Evidência ou silêncio").

---

## 1. Esta regra já foi revisada uma vez, há um dia, e mantida de propósito

`pesquisa/epico-figuras-em-ilustracao/00-diagnostico.md` (item 3) e
`pesquisa/epico-figuras-em-ilustracao/01-proposta.md` ("O que não muda") já examinaram
especificamente esta regra, no mesmo ciclo de revisão que criou o critério de três faixas para
figura humana. A conclusão de ontem foi explícita: **a regra 5 é real (deriva de
`DESIGN.md` §4.5, linha 263, quase citação literal), protege contra um problema de mercado
documentado, e não deveria ser enfraquecida.** O motivo citado:
"robô/cérebro-de-IA genérico é hoje o sinal visual mais rápido de 'conteúdo gerado por IA sem
cuidado' — o oposto do que a marca quer comunicar" (`DESIGN.md`, linha 87, "IA como
ferramenta, não como enfeite").

Isso não invalida o pedido de hoje — o autor tem autoridade para revisar a própria decisão de
ontem — mas significa que a mudança pedida agora **reverte uma conclusão evidenciada
recentemente**, não corrige um erro de proveniência (que era o caso da regra de figura
humana). Vale registrar essa diferença por escrito, para quem ler este épico depois.

## 2. A regra 5 tem base real em `brand/DESIGN.md` — ao contrário da antiga regra 6

`estilos-ilustracao.md`, linha 62–66 (antes desta revisão): "**Sem ilustração genérica de
finanças** (`DESIGN.md` §4.5): moeda, cifrão, candlestick, cofre, aperto de mão, robô/cérebro
de IA, prédio de banco, gráfico de pizza." Conferido contra a fonte:
`brand/DESIGN.md` §4.5 ("Anti-padrões — a lista do 'feito por IA'"), linha 263: "**Ilustração
genérica de 'finanças'** (moedas, cifrões, candlestick, robôs/cérebros de IA)." A lista do
`DESIGN.md` cobre 4 dos 8 itens citados em `estilos-ilustracao.md` explicitamente pelo nome;
cofre, aperto de mão, prédio de banco e gráfico de pizza são extrapolação desta camada
(hemingway), não citação direta.

`brand/DESIGN.md` vive fora deste repositório (`../../brand/`, referenciado por caminho
relativo, nunca copiado — `CLAUDE.md`, "Fonte única de cada coisa"). Não é um repositório git
a partir daqui (`git status` em `../../brand` retorna "not a git repository"), então nenhuma
mudança ali é commitável nesta tarefa de qualquer forma. Mas o ponto não é técnico — é de
propriedade: `DESIGN.md` é "fonte única de identidade visual para todo o ecossistema Syntaxis,
não só para este repo" (`CLAUDE.md`, nota de 31/08/2026). Mudar a regra aqui, sem tocar
`DESIGN.md`, cria uma **divergência real** entre o que hemingway permite e o que o resto do
ecossistema (produto, curso, marketing) trata como anti-padrão.

## 3. A divergência é defensável para este repositório especificamente

O motivo original da regra em `DESIGN.md` é sobre **produto/UI** ("Proibições verificáveis em
revisão de PR", §4.5, cabeçalho) — grid de três cards, hero centralizado, cinzas de framework,
emoji como ícone: uma lista de sinais de "feito às pressas com um gerador, sem cuidado de
design" num contexto de interface. Ilustração editorial de post de Substack é um contexto
diferente: a peça já passa por um método de composição inteiro
(`briefing-ilustracao.md` — colheita de material em três camadas, três operações sobre a
metáfora, testes de rejeição contra clichê de banco de imagens) que a maioria das peças de UI
genéricas nunca passa. Um candlestick usado como argumento visual específico de um post sobre
opções, desenhado dentro do vocabulário de colagem editorial (papel recortado, sombra chapada,
paleta fechada), não é o mesmo problema que um candlestick decorativo solto num hero de
landing page.

Isso é o mesmo raciocínio que já justificou a regra 6 (agora 5) de figura humana como critério
próprio do repositório — a diferença é que ali a proveniência de marca nunca existiu, e aqui
ela existe e está sendo conscientemente deixada de lado para este uso específico.

## 4. O que continua valendo, mesmo sem a proibição por nome de objeto

Remover a regra 5 não remove o resto do sistema de rejeição de clichê:

- `briefing-ilustracao.md`, "Erros recorrentes": "**Metáfora de dicionário.** Escada solta,
  ponte, quebra-cabeça, ampulheta, iceberg, labirinto, engrenagem, alvo com flecha. Se podia
  ter vindo de banco de imagens, veio." — um candlestick ou moeda tratado como clichê solto
  (sem função de argumento, só decoração) ainda reprova aqui, por um motivo diferente do banimento por marca.
- `briefing-ilustracao.md`, Passo 5 ("Testes de rejeição"): teste da troca, teste do
  substantivo, teste da fatalidade — todos continuam se aplicando a qualquer objeto, incluindo
  os que eram banidos por nome antes.
- A doutrina de "Referência de cultura pop: evocar a estrutura, nunca reproduzir a
  propriedade" (`briefing-ilustracao.md`) continua intacta — um robô específico de ficção
  científica (Terminator, WALL-E) continua proibido como objeto literal por motivo de
  propriedade intelectual, independente da regra de marca. Só a categoria genérica "robô" deixa
  de ser banida por si só.

**Conclusão:** a mudança pedida é segura de implementar como regra local, documentada como
divergência deliberada de `DESIGN.md` §4.5, sem enfraquecer o resto do sistema de crítica de
conceito. Ver `01-proposta.md` para o texto exato da mudança.
