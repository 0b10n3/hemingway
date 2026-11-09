# Verificação técnica — etapa 7

Verificação independente de `04-draft-v1.md`, usando `03-pesquisa.md` como ponto de partida
(não como verdade assumida). Todo item abaixo foi reconferido nesta etapa; onde a pesquisa da
etapa 3 já trazia fonte primária suficiente, a reconfirmação foi leve; onde não, foi refeita do
zero.

---

## 1. Definição de Value at Risk

**Texto:** "a estimativa estatística do nível de perda que uma carteira não deveria superar,
dado um horizonte de tempo e um nível de confiança."

**Veredito: ✅ Confirmado.**

Compatível com a definição padrão da literatura. Jorion (2001), a referência canônica: "VaR
measure is defined as the worst expected loss over a given horizon under normal market
conditions at a given level of confidence." Hull define de forma equivalente: "we are X percent
certain that we will not lose more than V dollars in the next N days." O texto do post captura
os três elementos exigidos por uma definição correta de VaR — estimativa estatística (não
determinística), horizonte de tempo, nível de confiança — sem a simplificação enganosa mais
comum (tratar VaR como "perda máxima possível", o que ele não é: por definição, existe uma
probabilidade residual de perda além do VaR, e é justamente essa omissão que a crítica pós-2008
do parágrafo seguinte explora). Não há erro a corrigir.

Fonte: Philippe Jorion, *Value at Risk: The New Benchmark for Managing Financial Risk*, 2001
(definição citada em múltiplas fontes secundárias consistentes, incluindo material didático
derivado do próprio Hull).

## 2. Definição de Black-Scholes

**Texto:** "o modelo clássico de precificação de opções."

**Veredito: ✅ Confirmado.**

Descrição correta e sem simplificação enganosa — é exatamente isso e nada além disso que a
frase afirma. O texto não entra em premissas do modelo (volatilidade constante, distribuição
lognormal dos retornos, ausência de custos de transação, mercado sem arbitragem), mas também não
faz nenhuma afirmação sobre essas premissas que precise ser checada; "modelo clássico de
precificação de opções" é a descrição padrão do modelo Black-Scholes-Merton em qualquer
literatura de finanças quantitativas, incluindo o próprio Hull. Nada a corrigir.

## 3. John Hull como "referência padrão de qualquer curso sério de derivativos"

**Veredito: ✅ Confirmado**, tratado como afirmação de consenso de mercado (não fórmula).

Reconfirmado nesta etapa, independente da pesquisa da etapa 3: *Options, Futures, and Other
Derivatives* é descrito de forma consistente, por editora e por cobertura de mercado, como
simultaneamente o livro-texto padrão de cursos de graduação/pós avançados em derivativos e
gestão de risco e a referência de mesa de operações ("the bible in trading rooms"). Fonte:
catálogo Pearson da obra (múltiplas edições, até a 11ª) e cobertura convergente em fontes de
mercado independentes. Afirmação de consenso amplamente sustentada — não há contraponto
relevante que a contradiga.

## 4. Citação de Jordan Peterson entre aspas duplas

**Texto:** Peterson "escreve... que erguer os ombros é aceitar 'a terrível responsabilidade da
vida'".

**Veredito: ❓ Não verificável no rigor exigido para citação literal → mantém como
`[VERIFICAR]`.**

O conteúdo está correto: a frase original em inglês — "To stand up straight with your shoulders
back is to accept the terrible responsibility of life, with eyes wide open" — está associada de
forma consistente à Regra 1 de *12 Rules for Life*, em múltiplas fontes secundárias
(Goodreads, resumos de terceiros) que convergem numa citação de página 26 da edição em inglês.
A tradução em português usada no draft, "a terrível responsabilidade da vida", também bate com
a formulação corrente da tradução brasileira ("12 Regras para a Vida", Editora Alta Books) em
fontes secundárias sobre o livro.

O problema não é o conteúdo — é o formato: o draft usa aspas duplas, que sinalizam citação
literal, não paráfrase. Citação literal pede confirmação de página/edição a partir do texto
integral (inglês ou tradução oficial), que esta verificação não teve acesso direto para
conferir palavra por palavra contra a fonte primária — só contra fontes secundárias que já
fazem a mesma mediação. Duas fontes secundárias convergentes reduzem o risco de erro, mas não
substituem a fonte primária para uma citação entre aspas.

Duas saídas possíveis para a consolidação (etapa 9), nenhuma delas literária/estilística —
decisão técnica de sourcing:
- (a) manter aspas e inserir `[VERIFICAR: página/edição exata da citação de Peterson — conferir
  contra 12 Rules for Life, p. 26 (edição em inglês) ou a tradução oficial "12 Regras para a
  Vida", Editora Alta Books]`;
- (b) remover as aspas duplas e tratar a frase como paráfrase (o que já está correto e não
  exige verificação adicional) — nesse caso o `[VERIFICAR]` desaparece.

## 5. Afirmação sobre core/lombar prevenir lesão vs. ligação mais fraca com velocidade

**Texto:** "há evidência sólida de que o 'core' forte previne lesão e sustenta a carreira do
atleta ao longo do tempo; a ligação direta com 'correr mais rápido' é mais fraca e menos
estudada."

**Veredito: ✅ Aprovado com ressalva** — não precisa de `[VERIFICAR]`, mas vale registrar o
porquê.

Reconferido o achado central da pesquisa da etapa 3 (Silva et al. 2023, PMC10588579):
confirmado via leitura direta do artigo que a meta-análise não mede velocidade de corrida como
desfecho — mede balanço (SMD 1.17, p<0.001), salto vertical (SMD 0.69, p=0.0003) e velocidade
de arremesso, não significativa (SMD 0.30, p=0.14). Isso é consistente com "ligação mais fraca e
menos estudada": a literatura de maior qualidade metodológica (meta-análise) não encontra
significância para desfechos de velocidade/potência quando isolados, enquanto a base para
prevenção de disfunção/dor lombar é mais antiga e mais robusta.

A ressalva genuína, já identificada pela pesquisa: Frontiers 2025 encontra evidência moderada
para sprint curto (10–20m) especificamente — o que, tomado isoladamente, tensiona "ligação mais
fraca" como categórico. Mas o contexto do post é corrida de fundo/meio-fundo ("quem corre quer
baixar o pace"), não sprint de arrancada — o achado de sprint curto não se aplica diretamente ao
desfecho que o texto está discutindo (pace em corrida contínua, não velocidade de saída). Dentro
desse recorte, a formulação do draft permanece defensável. Não é um consenso fechado, mas o
draft já usa linguagem hedged ("mais fraca e menos estudada", não "nenhuma ligação") compatível
com o estado real da evidência.

Fontes: Silva et al. 2023, *Core training and performance: a systematic review with
meta-analysis* — https://pmc.ncbi.nlm.nih.gov/articles/PMC10588579/; Frontiers 2025, *Exploring
the role of the core in sports performance* —
https://www.frontiersin.org/journals/sports-and-active-living/articles/10.3389/fspor.2025.1630584/full

## 6. Número "62%/42%" de PMC1865378

**Veredito: ✅ Confirmado limpo.**

Reconferida linha a linha a seção 1 (Fortalecer a Lombar é uma Droga) do draft: nenhum número,
percentual ou estatística de estudo específico aparece no texto. A afirmação permanece
inteiramente qualitativa ("há evidência sólida", "mais fraca e menos estudada"), sem citar
PMC1865378 ou qualquer número dele. Recomendação da pesquisa da etapa 3 foi seguida
corretamente — nada a corrigir.

## 7. "Crítica documentada desde a crise de 2008" sobre VaR

**Veredito: ✅ Aprovado.**

Já avaliada como bem sustentada pela pesquisa da etapa 3 (item 2b, explicitamente não candidata
a `[VERIFICAR]`) — fontes primárias nomeadas e verificáveis: Turner Review (FSA Reino Unido,
março 2009), relatório do Senior Supervisors Group/SEC (março 2008,
https://www.sec.gov/news/press/2008/report030608.pdf), FSB (outubro 2009,
https://www.fsb.org/2009/10/r_0910a/), e Robert Sollis, "Value at Risk: A Critical Overview",
*Journal of Financial Regulation and Compliance*, 2009. A única ressalva já registrada pela
pesquisa — que a crítica documentada mira a arquitetura do modelo e o uso regulatório/
institucional, não o erro de um profissional individual mal treinado especificamente — é uma
extensão pedagógica razoável do autor, não um erro factual. Concordo com o veredito da etapa 3:
não precisa de `[VERIFICAR]` na formulação qualitativa atual do draft.

## 8. Demais afirmações factuais/numéricas do draft

Varredura linha a linha do draft completo: não há outros números, fórmulas, datas ou citações
verificáveis além dos sete itens acima. "12 Rules for Life" (título correto, autoria correta —
Jordan B. Peterson), "Options, Futures, and Other Derivatives" (título correto, autoria correta
— John Hull), e "crise de 2008" (evento real, sem data ou número específico atribuído a ele além
do ano) não exigem verificação adicional além do que já foi feito acima.

---

## Lista consolidada de `[VERIFICAR]` para o texto final

1. `[VERIFICAR: página/edição exata da citação de Peterson — "a terrível responsabilidade da
   vida" — contra 12 Rules for Life, p. 26 (edição em inglês) ou a tradução oficial "12 Regras
   para a Vida" (Editora Alta Books), antes de manter entre aspas duplas como citação literal;
   alternativa: reformular sem aspas como paráfrase, o que já está correto e dispensa
   verificação]`

Nenhum item `[FAIXA: ...]` identificado nesta etapa — os dados quantitativos citados no laudo de
pesquisa (62%/42% de PMC1865378, effect sizes de Silva et al. 2023) não aparecem como números no
corpo do draft, então não há valor pontual do texto a converter em intervalo.
