# Estrutura

Arco completo (setup → conflito → resolução), cinco seções H2, mantendo os subtítulos do
rascunho de origem — já densos e um por movimento do argumento, batendo com a regra 5 do guia
de voz sem precisar de ajuste.

## 1. Fortalecer a Lombar é uma Droga — **setup**
Prova: estabelece a cena pessoal (gancho) e planta a metáfora estrutural inteira (treino chato
vs. treino pop) com uma evidência da literatura de ciência do esporte. É o setup — ainda não
fala de finanças.
Pilar coberto: **narrativa** (cena pessoal) + **dado** (evidência sobre 'core' e prevenção de
lesão, qualitativa mas atribuída à literatura).

## 2. O Objetivo Escolhe o Fardo — **setup → conflito**
Prova: faz a ponte Peterson → carreira em finanças; introduz a distinção concreta entre o
'difícil pop' (trade system, VaR, Black-Scholes) e o 'difícil chato' (Teoria da Probabilidade,
Hull) que sustenta a tese. É a virada do setup para o conflito real do texto.
Pilar coberto: **dado** (crítica documentada desde 2008 sobre VaR mal implementado).

## 3. Evitar o difícil frequentemente torna tudo mais difícil — **conflito**
Prova: generaliza o mecanismo (Dor A vs. Dor B) com quatro exemplos paralelos. É o corpo do
conflito — mostra que evitar não elimina a dificuldade, só adia e aumenta.
Sem pilar novo — reforça narrativa/dado já plantados; a força da seção é o paralelismo retórico
em si (já visualmente organizado no texto como citação em bloco).

## 4. Dificuldades com significado — **resolução (parte 1)**
Prova: dá o mecanismo causal completo de Peterson (responsabilidade → dificuldade →
competência → contribuição → significado) e torna a tese concreta em hábitos pequenos e
verificáveis de estudo.
Pilar coberto: **visual** — ver decisão de visual abaixo (diag-01).

## 5. Nem toda dificuldade vale a pena — **resolução (parte 2) + fechamento**
Prova: fecha o argumento com a ressalva que evita o estrawman ("sempre escolha o mais difícil"
não é o princípio) e devolve a decisão para o leitor, com CTA.
Sem pilar novo — fechamento.

## Três pilares — confirmação

- **Narrativa:** seção 1 (cena do treino) e a mesma linha pessoal sustentada até a seção 2
  (escolha da base quant).
- **Dado:** seção 1 (evidência de ciência do esporte) e seção 2 (crise de 2008 / VaR mal
  implementado).
- **Visual:** seção 4, `diag-01` (ver abaixo).

Todos os três representados em pelo menos uma seção — nenhum pilar ausente.

## Decisão de visual

**Um só visual: `diag-01`, seção 4 (Dificuldades com significado).**

Critério aplicado, na ordem do `SKILL.md`:

1. Há série numérica real a comparar/mostrar trajetória? **Não.** A evidência de ciência do
   esporte (seção 1) e a crítica ao VaR (seção 2) são qualitativas/documentais, sem número a
   plotar — não há `graf-NN` neste post. Decisão deliberada de ausência, não omissão.
2. Há relação estrutural entre entidades ou fluxo sem métrica central? **Sim** — a cadeia
   causal de Peterson (responsabilidade → dificuldade → competência → contribuição →
   significado) é exatamente o caso descrito no critério: "duas linhas, dois blocos" resolvidos
   em forma geométrica, sem métrica real por trás. Vira `diag-01`: fluxo linear de cinco nós.
3. Infográfico? Não se aplica — uma peça isolada (`diag-01`) já carrega a síntese da seção mais
   densa; nenhuma seção depende de composição de múltiplas peças. Padrão mantido: sem
   `info-NN`.
4. Metáfora do autor (lombar) que pediria ilustração? Sim, é a espinha dorsal do texto — mas
   ilustração não é mais peça deste pipeline (nota de 2026-09-09). Já registrado como tensão na
   etapa 1 para o gate humano; a metáfora fica só em prosa.

## Loop 1 — reentrada pedida pelo gate humano (2026-09-11)

O gate humano da rodada 1 aprovou a estrutura de 5 seções, mas pediu três adições de conteúdo
e um título/subtítulo novos (ver `estado.json`, `motivo_retorno`). Duas das três adições
aprofundam seções já existentes, sem mudar o arco; a terceira é tese nova, sem lugar nas 5
seções da rodada 1 — por isso a reentrada é na etapa 2, não direto na etapa 4.

**Seção 2 (O Objetivo Escolhe o Fardo) — aprofundamento, sem mudar o que a seção prova.**
Acrescenta o argumento "se você não escolhe conscientemente, seu chefe escolhe por você"
(consequência concreta de não escolher o próprio difícil) — já é o que a seção argumenta em
tese ("se você não escolhe os difíceis da sua jornada, alguém... escolhe por você"); o pedido
do autor é tornar isso concreto com a figura do chefe, incluindo a ressalva de que nem todo
chefe é um problema. Continua setup→conflito, mesmo pilar (dado: crítica ao VaR).

**Seção 4 (Dificuldades com significado) — aprofundamento, sem mudar o que a seção prova.**
Acrescenta "a disciplina não pode depender de ânimo, depende de significado" com exemplos
concretos de teoria da medida/probabilidade avançada (Fubini, Radon-Nikodym, Decomposição de
Lebesgue, convergência de medidas de probabilidade) — mesmo ponto já presente ("entender a
demonstração antes de decorar a fórmula"), só com nomes próprios em vez de genérico. Continua
resolução (parte 1), mesmo pilar (visual: `diag-01`).

**Nova seção 5 (entre a atual 4 e a atual 5) — tese nova, não estava na rodada 1.**
"O difícil chato fica mais valioso justamente porque a IA generativa faz o fácil." Prova: dá a
razão de urgência — por que esse investimento em base "chata" importa *agora*, especificamente
num mundo em que ferramentas de IA comoditizam a parte "pop"/de superfície do trabalho quant
(rodar um modelo, montar um `trade system` básico). É resolução (parte 2): fortalece a tese
antes do fechamento, não é setup nem conflito novo.

Pilar coberto: **dado** — mas é um dado de natureza diferente dos outros dois (evidência
empírica de ciência do esporte, crítica documentada pós-2008): aqui é argumento
econômico/prospectivo sobre valor de habilidade num mercado de trabalho em mudança, mais frágil
por natureza (é sobre o futuro, não sobre o passado). **Registrado para a etapa 7:** verificar
se a afirmação precisa de hedge (`[VERIFICAR]` ou linguagem qualificada) em vez de tom
categórico — é o tipo de claim mais fácil de exagerar sem perceber.

**Visual:** nenhuma peça nova. Critério da etapa 2 (rodada 1) não muda: sem série numérica
(sem `graf-NN`), sem fluxo/relação estrutural nova que `diag-01` já não cubra (a nova seção é
argumentativa, não processual). `diag-01` segue sendo o único visual do post — a legenda não
precisa mudar, porque a nova seção não altera a cadeia de Peterson que `diag-01` já representa.

**Título/subtítulo:** ditados pelo autor no gate humano —
"O Díficil sobre as Dificuldades em uma Carreira em Finanças" / "As partes difíceis que
ninguém posta no instagram". Substituem os da rodada 1 (que eram tentativa da consolidação,
não pedido do autor). Ajuste de norma culta (acentuação de "Difícil", maiúscula em
"Instagram") fica para a etapa 6 desta rodada — não decidido aqui.

**Arco final: 6 seções** — setup (1) → setup/conflito (2, aprofundada) → conflito (3) →
resolução parte 1 (4, aprofundada) → resolução parte 2, nova (5) → resolução/fechamento (6, era
a 5 da rodada 1).

## Loop 1, revisão 2 — crítica encontrou severidade alta, seção de IA reintegrada

`05-critica-loop1.md` (agente `critico-editorial`) achou severidade alta: a seção nova sobre
IA trocava o eixo do argumento (de "significado", a mecânica de Peterson, para "valor de
mercado"), não era recolhida pelo fechamento, e sua frase final ("o que fica mais difícil de
automatizar") competia como critério rival com a frase-tese da seção seguinte ("escolha aquilo
que é significativo..."). Com 6 seções, isso também produzia três beats de resolução seguidos
antes do fechamento real.

**Decisão:** não cortar o conteúdo (o pedido do autor era claro) — subordinar o argumento de
IA ao critério de significado em vez de propor um critério concorrente. Dois ajustes:

1. **A seção deixa de ser um H2 próprio.** Vira um parágrafo mais curto, movido para dentro da
   seção de fechamento ("Nem toda dificuldade vale a pena"), logo no início — antes da
   ressalva "sempre escolha o mais difícil não é isso". Isso resolve o achado 5 (elimina o
   terceiro beat de resolução) e evita competir com o pico da seção 4 (achado 3, parte
   "posição").
2. **A conclusão do parágrafo passa a apontar para significado, não para automação.** Em vez
   de "o difícil que vale a pena é o que fica mais difícil de automatizar" (critério novo),
   a frase final vira algo como "não é coincidência que o difícil com significado seja também
   o mais difícil de automatizar — mas é consequência de escolher certo, não o motivo para
   escolher". Isso resolve o achado 3 (parte "critério concorrente") — a IA vira evidência a
   favor do critério já estabelecido, não um critério novo.

Hedge (achado 4) também ajustado nesta reescrita: cortar "pelo menos não ainda" (concede que o
argumento expira) e "não é uma previsão confortável de se admitir" (reforça em vez de
qualificar); generalizações sem hedge ("para qualquer pessoa", "cada vez mais") suavizadas.

**Arco final revisado: 5 seções**, igual à rodada 1 — a seção de IA não conta mais como seção
própria, volta a ser 5 subtítulos H2, só que a seção de fechamento agora tem um parágrafo a
mais no início.

## O que fica de fora

- A cadeia "Dor A vs. Dor B" (seção 3) não vira diagrama: já está organizada como paralelismo
  retórico direto no texto (blockquote com quatro pares), e transformar isso em peça visual
  duplicaria, sem acrescentar, o que a prosa já faz sozinha.
- Números específicos de VaR/Black-Scholes não aparecem no texto (é relato, não tutorial
  técnico) — não há o que verificar numericamente além da atribuição "crítica documentada desde
  a crise de 2008", que vai para a etapa 7 como item a verificar.
