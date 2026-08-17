# 02 — Estrutura

Fonte: `01-briefing.md`. Arco de referência:
`.claude/skills/revisao-editorial/references/tecnicas-narrativas.md`.

## Arco escolhido

Versão completa (gancho → contexto → ação crescente → clímax → resolução → fechamento) —
justificado porque o argumento tem duas camadas de evidência pessoal que se acumulam (o
produto de opções e, depois, a dinâmica de juros/dívida pública) antes de generalizar para
quem não veio da academia (o estagiário na mesa de risco), o mesmo tipo de crescendo que
justificou a versão completa no post anterior. A versão mínima (setup→conflito→resolução)
achataria a diferença entre "meu caso específico" e "isso é um padrão de carreira" — que é
o que sustenta a virada do clímax.

## Subtítulos e o que cada um prova

### 1. Abertura — "A conta batia. O produto, não."
**Arco:** gancho. **Prova:** situa o leitor na cena concreta do briefing — o autor no
mestrado, capaz de derivar de cor o modelo de precificação de opções, sem conseguir
explicar o que aquele contrato fazia de fato no mercado. Não nomeia "mundo invertido" nem
"carreira" ainda — é só a cena, a lacuna entre saber a matemática e não entender o produto.
**Visual:** `ilu-01` — ver seção de visuais abaixo.

### 2. "Bem-vindo à linha Spoiler — e ao mundo invertido, de novo"
**Arco:** contexto. **Prova:** nomeia a cena como sintoma de um padrão, faz a ponte editorial
(esta é a estreia da linha Spoiler, "spoilers" do que a pessoa vai viver na carreira) e
retoma a moldura "mundo invertido" já publicada no post anterior — agora aplicada não a qual
produto comprar primeiro, mas a qual conhecimento construir primeiro. Explica por que a
academia empurra pesquisa recente para a ponta complexa (opções, contratos avançados),
tornando esse começo invertido comum, não uma falha pessoal.

### 3. "A segunda lacuna: dinheiro no tempo"
**Arco:** ação crescente. **Prova:** camada dois do mesmo problema — mesmo com domínio
matemático de valor presente/futuro e curva de juros, faltava entendimento de dívida
pública, emissão de títulos, mercado de crédito. É a seção que prepara o leitor para o
CTA do fechamento: o "assunto mais básico" que falta é justamente o tema do curso gratuito
(valor do dinheiro no tempo), então o texto já está semeando a ponte antes de puxá-la
explicitamente.
**Visual:** `graf-01` — ver seção de visuais abaixo.
**Pilar:** narrativa + visual.

### 4. "Não é só quem veio da academia"
**Arco:** clímax. **Prova:** vira a mesa — o exemplo pessoal era só a entrada; o padrão real
é mais amplo. O estagiário que cai direto numa mesa de risco/VaR, cercado de modelos
complexos, "preso na rotina sem entender de fato a rotina que está executando" — mostra que
a ordem invertida é um risco de carreira em geral, não uma peculiaridade de quem fez
mestrado. É o momento de maior identificação do leitor: o texto deixa de ser sobre o autor e
passa a ser, potencialmente, sobre o leitor.
**Pilar:** narrativa.

### 5. "Sem orgulho, sem falsa humildade"
**Arco:** resolução. **Prova:** o autor nomeia sua própria postura diante disso — não é
vergonha nem é minimização, é reconhecer o que faltou e voltar para trás. É a virada de tom
que evita que o texto soe como confissão de fracasso: o ponto não é "eu devia ter sabido
mais cedo", é "dá para voltar e consertar a ordem". Prepara o terreno para o CTA sem soar
como propaganda encaixada à força.

### 6. Fechamento — o curso e o convite
**Arco:** fechamento. **Prova:** anuncia o curso gratuito ao vivo (setembro, YouTube, valor
do dinheiro no tempo) como a resposta concreta e prática à lacuna nomeada nas seções 3 e 5 —
não como CTA genérico de newsletter, mas como o primeiro degrau real da régua que faltou ao
autor. Fecha com convite ao cadastro e ao compartilhamento — padrão obrigatório da voz
ensaística (§4.1 do guia).

## Checklist dos três pilares (regra: cada um em pelo menos uma seção)

- **Dado** → seção 3, junto com o visual (`graf-01`): a estrutura de dependência entre
  conceitos básicos e avançados não é opinião, é a ordem lógica real de pré-requisitos em
  finanças — o "dado" aqui é estrutural, não estatístico (sem número externo no áudio; se a
  etapa 3 de pesquisa achar algo verificável sobre lacunas de formação em finanças, considerar
  incluir, senão o pilar se sustenta só na estrutura de pré-requisitos).
- **Narrativa** → seções 1, 2, 4 e 5 (a cena, o contexto editorial, a generalização para
  carreira, a resolução pessoal).
- **Visual** → `ilu-01` (seção 1) e `graf-01` (seção 3), ambos carregando informação, não
  decoração (regra 9 do guia de voz).

## Onde entram os visuais e por quê

- `ilu-01` — cena de abertura. Candidato de composição: uma estrutura (fórmula, gráfico de
  precificação, ou similar) perfeitamente construída e iluminada flutuando sobre uma base
  invertida ou ausente — o "elemento iluminado" (ver `marca-syntaxis`) é o domínio técnico
  correto, mas a base que deveria sustentá-lo está de cabeça para baixo. Função: ancorar
  visualmente a lacuna do gancho (matemática perfeita, produto incompreendido) antes mesmo da
  leitura do primeiro parágrafo completo. Prompt exato fica para a etapa 8.
- `graf-01` — diagrama de duas trilhas: a ordem "certa" de construção de conhecimento em
  finanças (base → valor do dinheiro no tempo / dinâmica de juros e crédito → topo:
  precificação de derivativos, VaR) ao lado da ordem que o autor de fato seguiu (entrada pelo
  topo, lacuna na base, preenchida só depois). Função: dar ao leitor, num só olhar, o mapa que
  a seção 3 desenvolve em texto — mesmo papel estrutural que `graf-01` cumpriu no post
  anterior (regra 9: visual que completa o raciocínio, não decora).

## O que fica de fora

- Explicação técnica de como funciona um modelo de precificação de opções, ou definição
  estendida de VaR — conteúdo de referência (voz explicativa), fora do escopo deste post; os
  termos aparecem só com gloss mínimo (regra 1 do guia).
- Estatística sobre quantos profissionais "começam pela ponta errada" — não veio no áudio,
  sem fonte; a etapa 3 pode procurar, mas o argumento não depende disso.
- Detalhe de módulos/cronograma do curso gratuito além do que o áudio já define — isso fica
  para o formulário de cadastro, não para o corpo do post (já decidido no briefing).
- Qualquer meta numérica de funil/marketing (`_arquivo/MARKETING_REVIEW.md` §10) — operação
  interna, não assunto do post.
