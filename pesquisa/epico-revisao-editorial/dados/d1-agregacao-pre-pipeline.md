# D1 — Agregação estilométrica dos 15 posts pré-pipeline

Fonte única dos traços: `d1-extracoes-pre-pipeline.md`.
Guia testado: `../../../estilo/estilo-autoral.md` v1.0.0.

Como ler:
- Toda evidência «…» é cópia literal do digest, seguida do slug.
- "nº" conta posts distintos.
- Os códigos de post estão na tabela A.
- Vozes: ENS = ensaística; ENS-T = ensaística em registro técnico; EXP = explicativa.
- Limite comum: cada post tem menos de 5.000 palavras. Os extratores dizem que as frequências são frágeis.
- A seção está vazia ("-") nos 15 cabeçalhos. Não dá para condicionar à linha editorial.

## A. Voz por post

Critério uniforme, aplicado na ordem:
1. Estrutura de ensaio (gancho, tese em refrão, fecho que retoma o gancho) e corpo técnico dominante → ENS-T.
2. Tese ou opinião, com 1ª pessoa ou anedota e com figura própria → ENS.
3. Sem tese em disputa, tom impessoal ou didático → EXP.

Desempates: quando há opinião em 1ª pessoa, a figura própria decide entre ENS e EXP (EAB tem; RES não).
Técnico pontual num corpo narrativo fica em ENS (SIM).

| Cód. | Slug | Data | Voz | Justificativa |
|---|---|---|---|---|
| CDS | conectando-dinheiro-e-sonhos | 2024-09-06 | EXP | Didático-motivacional, sem anedota nem humor: «O dinheiro, quando gerido de forma inteligente, é uma ferramenta poderosa para transformar sonhos em realidade.» |
| EAB | escolhendo-as-batalhas | 2024-09-12 | ENS (limítrofe) | Opinião em 1ª pessoa e metáfora militar retomada no fim. Sem anedota, sem humor: «Entretanto, acredito que bons objetivos possuem algumas características essenciais.» |
| UOC | um-objetivo-para-comecar | 2024-09-20 | EXP | Sequência didática. A 1ª pessoa só recomenda: «Existem muitos recursos sobre como lidar com dívidas, mas hoje vou recomendar dois que considero essenciais.» |
| RES | reservas-de-emergencia | 2024-09-30 | EXP (limítrofe) | Uma pergunta prática por subtítulo. Opina em 1ª pessoa, mas sem figura nem anedota: «## Qual o Tamanho da Reserva?» |
| CCS | comece-com-o-simples | 2024-10-10 | EXP (limítrofe) | Abertura de série por retrospecto, tom prudente, sem humor: «Nos últimos artigos, discutimos a importância de desenvolver seus investimentos de forma a alcançar seus objetivos de vida.» |
| TIT | titulos-do-tesouro-nacional | 2024-10-16 | EXP | Catálogo impessoal, um H2 por produto: «O **Tesouro IPCA+** é um título híbrido» |
| ASS | eu-preciso-de-um-assessor-de-investimentos | 2024-10-20 | ENS | Tese em disputa, 1ª pessoa e ironia: «Sempre que escuto esses relatos, me pergunto se essas pessoas realmente precisam seguir as orientações do assessor.» |
| PRE | tesouro-prefixado-o-guia-completo | 2024-10-24 | EXP | Esqueleto fixo de guia de produto: «## Vantagens e Riscos» |
| SEL | tesouro-selic | 2024-11-01 | EXP | Verbete em 3ª pessoa: «O investidor pode resgatar o Tesouro Selic a qualquer dia útil sem perda de capital» |
| ETF | etf-o-que-e | 2025-07-08 | EXP | Guia/FAQ sem 1ª pessoa do singular: «## O que é um ETF (Exchange Traded Fund)? A Definição Direta» |
| SIM | o-simples-funciona | 2026-01-06 | ENS | Tese provocativa, humor até no trecho técnico. A fórmula é pontual: «um motor de uno (*sem escada*).» |
| IVY | o-portfolio-da-ivy-league | 2026-01-14 | ENS-T | Gancho autobiográfico, corpo de pesos e mapeamento item a item, fecho retoma "tropical" e a fundação: «precisam de um ajuste fino tropical» |
| OBJ | objetivos-and-classes | 2026-01-26 | EXP (limítrofe) | Tem 1ª pessoa, anedota e humor. Mas não tem tese em disputa nem fecho que retome o gancho. A Conclusão repete o corpo: «A classificação de instrumentos financeiros é útil e relevante. Nos permite compreender, comparar e entender resultados» |
| SEP | a-ciencia-da-separacao | 2026-02-08 | ENS-T | Anedota na abertura, fio aparência × essência até o fim, sete critérios aplicados item a item: «Isso viola o critério de homogeneidade interna» |
| GBI | goal-based-investing | 2026-03-02 | ENS-T | Cena datada, genealogia autor + data com glosa, fecho retoma a cena: «Assim como as paisagens mudam ao cruzar a divisa de um estado, a hiperpersonalização garante» |

Contagem: ENS 3 (EAB, ASS, SIM). ENS-T 3 (SEP, GBI, IVY). EXP 9.
Limítrofes: EAB, RES, CCS, OBJ.
Divergências com a v1: OBJ (v1: ensaística) vai para EXP. SEP (v1: ensaística) vai para ENS-T.

## B. Traços recorrentes (≥ 2 posts)

Ordem: eixos estruturais primeiro, léxico por último. "Voz" diz se o traço depende da voz ou da época.

### B1. Sintaxe

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Frase curta de ênfase ou virada ao lado de períodos longos | 8 | SEP, ETF, ASS, GBI, IVY, SIM, OBJ, RES | «Você coloca 100 reais em cada uma. Fim.» (o-simples-funciona) | Época: 5/5 em 2026; em 2024 só ASS e RES |
| Inverso: comprimento uniforme, sem frase curta de ênfase | 7 | CCS, CDS, EAB, UOC, PRE, SEL, TIT | «Colocar as finanças em ordem é uma prioridade que vem antes de viagens, compras e até mesmo de poupar para a aposentadoria.» (um-objetivo-para-comecar) | Todos de 2024; 6 EXP + EAB |
| Subordinada, adjunto ou conector anteposto + vírgula abrindo a frase | 15 | todos | «Quando eu ainda era um estudante bolsista no início da graduação em matemática na UFES, participei de um projeto» (o-portfolio-da-ivy-league) | Não. Universal, pouco discriminante |
| Condicional "Se..., ..." como motor de exemplo ou de regra | 6 | SEP, CDS, EAB, IVY, PRE, UOC | «Se você deseja se aposentar cedo, por exemplo, faz sentido colocar esforço e dinheiro» (escolhendo-as-batalhas) | Não |
| Contraste corretivo "não X, mas Y" / "X, não Y" | 7 | SEP, CDS, ETF, GBI, IVY, SIM, OBJ | «trata-se de gestão ativa, não de uma classe de ativos» (a-ciencia-da-separacao) | Época: 6 de 7 em 2025–26; em CDS só no fecho. Marcado como tique em 6 (ver E) |
| Gerúndio de consequência no fim do período | 10 | SEP, CCS, ETF, ASS, GBI, OBJ, RES, PRE, SEL, TIT | «Ele funciona como uma aplicação de longo prazo, com rentabilidade indexada ao IPCA, garantindo proteção contra a inflação.» (titulos-do-tesouro-nacional) | Não. Concentrado em trechos expositivos, listas e conclusões (SEP, ASS, GBI, RES). OBJ pela linha antipadrão |
| Frase iniciada por "Mas" ou "E" | 8 | SEP, EAB, ETF, ASS, IVY, SIM, OBJ, RES | «E, acima de tudo, é caro.» (o-simples-funciona) | Presente em todos ENS/ENS-T; não registrado em CCS, CDS, UOC, PRE, SEL, TIT |
| Enumeração ternária (tríade) | 8 | CCS, ETF, ASS, IVY, SIM, OBJ, SEL, TIT | «diversificação, transparência e, principalmente, custos baixos» (etf-o-que-e) | Não. SEL pela linha antipadrão |
| Fragmento nominal expressivo, sem verbo | 5 | EAB, GBI, IVY, SIM, RES | «Sem emoção, sem tentar adivinhar o fundo. Apenas matemática aplicada à sobrevivência.» (o-portfolio-da-ivy-league) | Forte em GBI, IVY, SIM (2026); EAB e RES têm de 1 a 3 |
| Oração dependente solta depois do ponto (deslize) | 2 | SEP, TIT | «Sendo classificados como produtos de renda variável.» (a-ciencia-da-separacao) | Não |
| Anáfora e paralelismo em série | 4 | CDS, IVY, SIM, OBJ | «Sem cálculo estocástico. Sem descontar fluxos de caixa futuros. Sem tentar adivinhar se o CEO da Apple vai ter uma indigestão amanhã.» (o-simples-funciona) | Não |
| Inciso entre vírgulas separando sujeito e verbo | 3 | CCS, EAB, ASS | «Este é, talvez, o ponto mais crítico.» (eu-preciso-de-um-assessor-de-investimentos) | 2024 |
| Pares de adjetivos coordenados | 3 | EAB, UOC, PRE | «conhecido por suas estratégias simples e eficientes» (um-objetivo-para-comecar) | 2024. PRE pela linha antipadrão |
| Demonstrativo anafórico abrindo a frase ("Esse/Essa" + nome) | 3 | CCS, PRE, TIT | «Essa previsibilidade o torna atrativo para quem busca segurança» (tesouro-prefixado-o-guia-completo) | EXP, 2024 |
| Frase definitória "X é Y" na abertura da seção | 3 | ETF, SEL, TIT | «O Tesouro Selic é um título público pós-fixado oferecido pelo programa do Tesouro Direto, em parceria com a B3.» (tesouro-selic) | EXP |
| Clivada "É/Foi ... que/quem" | 2 | GBI, IVY | «Foi Mebane Faber quem decidiu abrir as cortinas.» (o-portfolio-da-ivy-league) | ENS-T, 2026 |
| Deslizes de concordância ou regência publicados | 3 | SEP, EAB, RES | «fazem com que possuir um ETF é» (a-ciencia-da-separacao) | Não é estilo. GBI e SIM listam erros só na incerteza |

### B2. Pontuação

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Dois-pontos como articulador (anuncia definição, revelação, lista) | 13 | todos menos EAB, TIT | «O papel dos investimentos é simples: ajudar você a alcançar seus objetivos mais rápido!» (conectando-dinheiro-e-sonhos) | Não. EAB e TIT não têm dois-pontos na prosa |
| Parágrafos curtos; parágrafo de uma frase como ponte, gancho ou punchline | 13 | todos menos SEL, TIT | «Hoje vamos nos aprofundar nessas ideias.» (a-ciencia-da-separacao) | Não. SEL: sem parágrafo de uma linha |
| Travessão (—, – ou hífen com espaços) para inciso na prosa | 6 | SEP, GBI, IVY, SIM, OBJ, TIT | «— um dos poucos lugares com ar-condicionado onde eu podia me refugiar naqueles tempos —,» (objetivos-and-classes) | Época: 5/5 em 2026; TIT tem um par. Os outros 9 só têm travessão na epígrafe, ou nenhum |
| Hífen com espaços e travessão no mesmo post | 2 | SEP, GBI | «algumas pessoas - por mais estranho que possa parecer - compram tanto bilhetes de loteria» (goal-based-investing) | ENS-T, 2026 |
| Parênteses frequentes (≥ 5) como inserção principal | 7 | SEP, ETF, IVY, OBJ, RES, SEL, UOC | «(como o Ibovespa ou IMA (um índice de títulos públicos))» (a-ciencia-da-separacao) | Não. CCS e EAB têm um parêntese só |
| Aspas duplas para termo em menção, ironia ou rótulo | 12 | SEP, CDS, EAB, ETF, ASS, GBI, IVY, SIM, OBJ, RES, TIT, UOC | «não tenta "vencer" o mercado» (etf-o-que-e) | Não. Curvas nos 5 de 2026; retas em CDS, EAB, ETF, TIT, UOC. Aspas simples só em GBI, alternando com duplas |
| Ponto e vírgula ausente ou raro na prosa | 12 | CCS, EAB, ETF, SIM, RES, SEL, TIT (nunca); SEP, ASS, IVY (1–3); OBJ, PRE (só em lista) | «O gestor não opera no vazio; ele segue» (a-ciencia-da-separacao) | Não |
| Exclamação rara (1–4 no corpo) | 8 | SEP, CDS, EAB, GBI, OBJ, RES, PRE, UOC | «Parabéns!» (reservas-de-emergencia) | Não. Nenhuma no corpo: CCS, ETF, ASS, IVY, SIM, SEL, TIT |
| Itens de lista com ponto e vírgula e ponto final no último | 3 | OBJ, PRE, SEL | «- 22,5% para investimentos até 180 dias;» (tesouro-selic) | Não |
| Reticências | 4 | IVY, SIM, OBJ, RES | «E os fundos de investimento? Ativos alternativos… Por que elas são relevantes?» (objetivos-and-classes) | Funções diferentes: lista aberta (OBJ), citação simulada (RES), teaser "Continua …" (IVY, SIM) |
| Vírgula entre sujeito e verbo | 2 | SEP, IVY | «O ensino e a pesquisa, não podem parar.» (o-portfolio-da-ivy-league) | 2026; pode ser deslize |
| Barra entre dois termos equivalentes | 2 | ASS, RES | «nosso perfil/tolerância ao risco» (eu-preciso-de-um-assessor-de-investimentos) | 2024 |

### B3. Arquitetura

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Abre com imagem e epígrafe de terceiro em pullquote | 9 | CCS, CDS, EAB, ASS, RES, PRE, SEL, TIT, UOC | «[[PULLQUOTE: "Risco vem de não saber o que você está fazendo." — Warren Buffett]]» (comece-com-o-simples) | Época: 9/9 de 2024, 0 depois. Atravessa vozes |
| Abre com cena, anedota ou tese provocativa antes do conceito | 5 | SEP, ASS, GBI, IVY, SIM | «No feriado de Carnaval viajei para a cidade de Três Lagoas no Mato Grosso do Sul para o casamento de um amigo.» (goal-based-investing) | Sim: 5 de 6 ENS/ENS-T (EAB não) |
| Abre retomando o post anterior da série | 5 | SEP, CCS, EAB, RES, SEL | «No post anterior, falamos sobre a importância de definir objetivos claros e alcançáveis.» (escolhendo-as-batalhas) | Não |
| Metatexto de roteiro ("Hoje vamos...", "Nosso plano é") | 11 | SEP, CCS, EAB, ETF, ASS, GBI, OBJ, RES, PRE, SEL, UOC | «Para isso, faremos uma breve pausa nos textos focados exclusivamente em objetivos de investimentos» (comece-com-o-simples) | Não |
| Conceito antes do exemplo | 12 | SEP (dentro de cada critério), CCS, CDS, EAB, ETF, GBI, OBJ, RES, PRE, SEL, TIT, UOC | «Suponha que você invista R$ 1.000,00 no Tesouro Selic e a taxa Selic esteja em 13% ao ano.» (tesouro-selic) | Ver linha seguinte |
| Exemplo antes do conceito (no texto ou na seção) | 4 | SEP, ASS, IVY, SIM | «Você tem 1.000 reais? Tem 10 ações disponíveis? Você coloca 100 reais em cada uma. Fim.» (o-simples-funciona) | Sim: só ENS/ENS-T |
| Subtítulos densos (um a cada ~100–230 palavras) | 12 | CCS, CDS, EAB, ETF, ASS, IVY, SIM, RES, PRE, SEL, TIT, UOC | «## Objetivos Alinhados com Seus Valores» (escolhendo-as-batalhas) | Época: esparsos (~300+ palavras) em SEP, GBI, OBJ, todos de 2026 |
| Esqueleto de guia/FAQ (o que é → como funciona → vantagens/riscos → para quem → custos → conclusão) | 3 | ETF, PRE, SEL | «## Como funciona a remuneração do Tesouro Selic?» (tesouro-selic) | EXP. TIT (catálogo) e RES (pergunta por subtítulo) são vizinhos |
| Seção final com rótulo literal "Conclusão" | 13 | todos menos SEP, CCS | «### Conclusão» (etf-o-que-e) | Não. Recapitulativa e marcada como tique em 11 (ver E). SIM, IVY e GBI usam a Conclusão para ressalva ou retomada |
| Fecho retoma a figura ou a palavra-tema da abertura | 8 | SEP, CDS, EAB, GBI, IVY, SIM, RES, UOC | «Assim como as paisagens mudam ao cruzar a divisa de um estado, a hiperpersonalização garante» (goal-based-investing) | Imagem desenvolvida só em ENS-T e SIM (2026); só palavra-tema em 2024. Não retomam: CCS, ASS, PRE, SEL, OBJ, TIT |
| Promessa de continuação (gancho de série no fecho ou adiamento no corpo) | 10 | SEP, CCS, CDS, EAB, GBI, IVY, SIM, OBJ, PRE, TIT | «Na próxima vez, vamos falar sobre a estratégia Ivy 5 de Meb Faber, outra tentativa de colocar ordem no caos.» (o-simples-funciona) | Não |
| Frase-síntese curta ou máxima fechando seção ou parágrafo | 7 | SEP, ETF, ASS, IVY, PRE, TIT, UOC | «O problema com a semelhança é que, muitas vezes, nem tudo é o que parece.» (a-ciencia-da-separacao) | Não |
| Seção abre ou fecha com pergunta | 4 | SEP, ASS, SIM, OBJ | «O que seria a tal gestão de riscos?» (eu-preciso-de-um-assessor-de-investimentos) | ENS/ENS-T + OBJ |
| Lista de itens ou critérios examinada caso a caso | 3 | SEP, EAB, ASS | «Com a ressalva de todos os pontos anteriores, este é um aspecto onde um assessor ou consultor financeiro pode ser extremamente útil.» (eu-preciso-de-um-assessor-de-investimentos) | Sim: ENS/ENS-T |
| Anedota da formação em matemática como ponte para o conceito | 4 | SEP, IVY, SIM, OBJ | «Quando eu estava na graduação em Matemática na **UFES (Universidade Federal do Espírito Santo)**, um professor me recomendou uma leitura.» (o-simples-funciona) | Época: 4/5 de 2026, 0 antes |

### B4. Formatação

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Subtítulos em Title Case | 13 | todos menos GBI, TIT | «**O Que São Investimentos?**» (comece-com-o-simples) | Não. Marcado como decalque em ETF e SEL |
| Rótulo de item + dois-pontos (lista ou parágrafo-lista), quase sempre em negrito | 8 | SEP, ETF, ASS, IVY, RES, SEL, UOC, PRE (sem negrito) | «**Investível:** Os componentes subjacentes da classe de ativos devem ser diretamente investíveis.» (a-ciencia-da-separacao) | Não. Em ASS é a lista atribuída ao ChatGPT |
| Negrito no corpo para conceito, frase-tese ou ênfase | 8 | SEP (raro), ETF, GBI, IVY, SIM, SEL, TIT, UOC | «Esse título **protege o investidor contra a inflação**» (titulos-do-tesouro-nacional) | Não. Nunca na prosa: CCS, EAB, ASS, OBJ, RES, PRE |
| Itálico para estrangeirismo ou título de obra, inconsistente | 6 | SEP, ETF, GBI, IVY, SIM, PRE | «Se você entrar no *trading floor* da BlackRock» (o-simples-funciona) | Época: 2025–26 (PRE só obra). Sem itálico: CCS, CDS, EAB, ASS, OBJ, RES, TIT |
| Só H2 como nível de subtítulo | 8 | SEP, CDS, EAB, GBI, OBJ, RES, TIT, UOC | «## Critérios de Kritzman» (a-ciencia-da-separacao) | Não. H3 em ASS, IVY, SIM, ETF, PRE; H4 em SEL; CCS usa parágrafo em negrito |
| Imagens sem legenda | 15 | todos (GBI legenda em parte) | «![](img-01)» (o-portfolio-da-ivy-league) | Não. Conteúdo das imagens desconhecido em todos |
| Separador "* * *" isolando bloco de CTA ou nota | 8 | SEP, CDS, EAB, ETF, IVY, SIM, OBJ, UOC | «* * *» (escolhendo-as-batalhas) | Não |
| Link inline ancorado em palavra | 3 | SIM, OBJ, UOC | «[Confira o canal do Primo Pobre](https://www.youtube.com/c/PrimoPobre)» (um-objetivo-para-comecar) | Não. Sem link no corpo: SEP, CDS, ETF, ASS, GBI, IVY, RES, PRE, SEL |

### B5. Figuras

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Imagem-motivo retomada ao longo do texto | 8 | SEP, CDS, EAB, ETF, GBI, IVY, SIM, UOC | «É ***“Rocket Science”*** financeira. É sexy.» (o-simples-funciona) | Não. Mais extensa em ENS-T e SIM |
| Metáforas pontuais de domínios variados (medicina, guerra, máquina, jogo, animal) | 7 | SEP, ETF, ASS, GBI, IVY, SIM, TIT | «como se o mercado fosse uma besta indomável» (o-simples-funciona) | Não |
| Metáforas lexicalizadas de caminho, construção ou jornada | 6 | CCS, CDS, ETF, OBJ, RES, UOC | «iniciar essa jornada de forma prática e confiável» (um-objetivo-para-comecar) | Sim: 6/6 EXP |
| Registro literal: sem figura própria, só clichê ou expressão feita | 5 | CCS, CDS, RES, PRE, SEL | «O Tesouro Selic é semelhante à LFT (Letra Financeira do Tesouro), título pós-fixado também atrelado à Selic.» (tesouro-selic) | Sim: EXP. TIT tem uma figura só |
| Referência de cultura pop, brasilidade ou atualidade como gancho ou ironia | 5 | SEP, GBI, IVY, SIM, OBJ | «## Daniel. Bernoulli, não o Vorcaro.» (goal-based-investing) | Época: 5/5 de 2026, 0 antes. Banco Master em SEP e OBJ |
| Personificação da estratégia como "agnóstica" no fecho | 2 | IVY, SIM | «O 1/N é agnóstico. Ele não se importa com seus sentimentos» (o-simples-funciona) | 2026. Frase quase igual em IVY |
| "Cesta" como analogia para fundo | 2 | SEP, ETF | «Pense neles como uma “cesta” que agrupa diversos ativos» (a-ciencia-da-separacao) | Não |
| Produto novo explicado por comparação com produto conhecido | 3 | ETF, SEL, TIT | «comece a receber um pagamento mensal por um período determinado, semelhante a uma aposentadoria privada» (titulos-do-tesouro-nacional) | EXP |

### B6. Postura

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| "Nós" inclusivo ou editorial conduzindo a exposição | 15 | todos | «analisar como podemos criar planos concretos para alcançá-los» (comece-com-o-simples) | Não. Em SEL e TIT só na abertura ou no fecho |
| Autoridade implícita: nenhuma credencial própria declarada | 14 | todos menos CCS | «É nessa discussão que o trabalho de Kinlaw, Kritzman e Turkington (2021) nos auxilia» (a-ciencia-da-separacao) | Não. CCS declara a trajetória profissional |
| "Eu" só na anedota ou memória; depois passa a "nós" | 5 | SEP, GBI, IVY, SIM, OBJ | «eu e meu amigo Oscar Londono» (a-ciencia-da-separacao) | Época: 5/5 de 2026 |
| "Eu" para opinião, intenção e metadiscurso | 3 | EAB, ASS, RES | «Acho essencial dizer que muitas situações tidas como emergências poderiam (podem!) ser mitigadas com o uso de seguros.» (reservas-de-emergencia) | 2024. Em UOC, PRE e CCS o "eu" só recomenda ou escolhe |
| Sem "eu" | 3 | ETF, SEL, TIT | «Uma análise rigorosa exige atenção aos detalhes:» (etf-o-que-e) | EXP |
| Humor ou ironia leve | 6 | SEP, ASS, GBI, IVY, SIM, OBJ | «(você foi honesto?)» (eu-preciso-de-um-assessor-de-investimentos) | Sim: 5 de 6 ENS/ENS-T; 1 de 9 EXP (OBJ). RES: um lampejo |
| Antagonista coletivo (mercado, indústria, prática convencional), sem nomear quem critica | 7 | SEP, ETF, ASS, IVY, SIM, OBJ, RES | «O mercado financeiro tem um fetiche por complexidade.» (o-simples-funciona) | Não. Ironia explícita só em SEP, ASS, SIM, RES |
| Admite limite, exceção ou incerteza da própria tese | 7 | SEP, EAB, ASS, GBI, IVY, SIM, RES | «Obviamente, se você se enquadra em um segmento de alta renda, a situação pode ser bem diferente.» (eu-preciso-de-um-assessor-de-investimentos) | Sim: 6/6 ENS/ENS-T; em EXP só RES |
| Modalização frequente ("pode", "acredito", "talvez") | 6 | CCS, CDS, EAB, ASS, RES, UOC | «Este é, talvez, o ponto mais crítico.» (eu-preciso-de-um-assessor-de-investimentos) | Época: todos de 2024 |
| Tom categórico, sem dúvida no conteúdo | 7 | SEP, ETF, IVY, OBJ, PRE, SEL, TIT | «proporcionando sempre um retorno positivo, mesmo que a taxa caia» (titulos-do-tesouro-nacional) | Verbetes de 2024 e posts de 2025–26 |
| Tom encorajador ou lisonjeiro com o leitor | 4 | CDS, ETF, RES, UOC | «Alguns desses objetivos podem até parecer sonhos, mas acredite: todos são possíveis.» (conectando-dinheiro-e-sonhos) | EXP |
| Tom favorável ao produto, sem risco nem ressalva de perfil | 2 | SEL, TIT | «O Tesouro Selic é uma das alternativas mais seguras e acessíveis do Tesouro Direto» (tesouro-selic) | EXP |

### B7. Leitor

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| "Você" direto e frequente | 10 | CDS, EAB, ETF, ASS, GBI, IVY, SIM, OBJ, RES, UOC | «Você precisa começar a se questionar sobre o nível de exposição que você precisa em seu portfólio.» (eu-preciso-de-um-assessor-de-investimentos) | Não |
| "O investidor" em 3ª pessoa no lugar de "você" | 5 | SEP, CCS, PRE, SEL, TIT | «permitindo que o investidor saiba exatamente quanto receberá no vencimento do título» (titulos-do-tesouro-nacional) | Quase só EXP; SEP é exceção |
| Pergunta no corpo (retórica ou dirigida ao leitor) | 10 | SEP, CDS, EAB, ETF, ASS, GBI, IVY, SIM, OBJ, RES | «você é mais arrojado ou conservador quando o objetivo é construir o patrimônio que garantirá os estudos de seus filhos?» (eu-preciso-de-um-assessor-de-investimentos) | 6/6 ENS/ENS-T. Sem pergunta no corpo: CCS, PRE, SEL, TIT, UOC (todos EXP) |
| Pergunta curta respondida logo em seguida | 5 | EAB, GBI, IVY, SIM, RES | «O resultado? Na prática, a estratégia “ingênua” do 1/N empatava ou ganhava do modelo do Prêmio Nobel.» (o-simples-funciona) | Não |
| Subtítulo em forma de pergunta | 8 | SEP, CCS, CDS, ETF, ASS, RES, PRE, SEL | «## Qual o Tamanho da Reserva?» (reservas-de-emergencia) | Época: 7 de 8 em 2024–25 |
| Cenário hipotético em 2ª pessoa ("Imagine", "Suponha", "Se você...") | 7 | CDS, EAB, SIM, RES, PRE, SEL, UOC | «Imagine que você guardou dinheiro para comprar um novo notebook.» (um-objetivo-para-comecar) | Não. O notebook também aparece em CDS |
| Imperativo raro (≤ 4) ou ausente | 14 | todos menos CDS | «Lembre-se de que seus investimentos devem estar alinhados aos seus objetivos de vida.» (eu-preciso-de-um-assessor-de-investimentos) | Não. "Lembre-se" no fecho em CDS, EAB, ASS, SIM. GBI e OBJ evitam imperativo |
| Botão de compartilhar do Substack | 7 | SEP, EAB, GBI, IVY, SIM, OBJ, UOC | «Obrigado por ler o Syntaxis! Compartilhar este post ajuda a ampliar o alcance de ideias que merecem circular.» (objetivos-and-classes) | Época: 5/5 de 2026. Os 7 extratores dizem que o texto pode ser padrão. Sem CTA: CCS, ASS, RES, PRE, SEL, TIT |
| Confere se o leitor entendeu ("entendeu o ponto") | 2 | EAB, ASS | «mas acredito que você entendeu o ponto» (escolhendo-as-batalhas) | ENS, 2024 |
| Recomenda fonte externa acessível (curso, vídeo, canal) | 3 | GBI, OBJ, UOC | «que você pode assistir de graça no MIT [OpenCourseWare]» (objetivos-and-classes) | Não |
| Segmenta o leitor por perfil ou situação | 4 | OBJ, PRE, TIT, UOC | «Para os mais curiosos, basta pesquisar por exemplo sobre “classes de equivalência”» (objetivos-and-classes) | EXP |

### B8. Técnico

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Sem fórmula; mecanismo e cálculo em prosa | 13 | todos menos SIM, UOC | «Se o ativo está acima da média dos últimos 10 meses, você mantém. Se caiu abaixo, você vende e vai para o caixa.» (o-portfolio-da-ivy-league) | Não |
| Fórmula única em display, variáveis por extenso em português | 2 | SIM, UOC | «$$ Ativo = Passivo + Patrimônio \ Líquido $$» (um-objetivo-para-comecar) | Não (ENS e EXP) |
| Nenhum número no texto | 6 | SEP, CCS, EAB, ASS, TIT, UOC | «Esses produtos, embora ofereçam retornos mais modestos, proporcionam uma base sólida e menos arriscada» (comece-com-o-simples) | Não |
| Resultado numérico sem mostrar a conta | 3 | CDS, PRE, SEL | «Levaria 30 meses para alcançar o valor total.» (conectando-dinheiro-e-sonhos) | EXP. O extrator de CDS achou contas que não fecham |
| Formato numérico brasileiro (R$ com centavos, vírgula decimal, ponto de milhar) | 6 | CDS, ETF, SIM, OBJ, PRE, SEL | «valor nominal de R$ 1.000,00 no vencimento» (tesouro-prefixado-o-guia-completo) | Não |
| Dado, taxa ou regra sem fonte nem data | 8 | CDS, ETF, IVY, OBJ, RES, PRE, SEL, TIT | «No Brasil, em tempos normais, o tempo médio de recolocação costuma ficar entre 6 a 12 meses.» (reservas-de-emergencia) | Não. SIM cita Bloomberg 2017 como "hoje" |
| Estudo ou obra acadêmica nomeada no corpo, sem bibliografia nem link | 6 | SEP, CCS, GBI, IVY, SIM, OBJ | «três acadêmicos: Victor DeMiguel, Lorenzo Garlappi e Raman Uppal. Em 2007» (o-simples-funciona) | Época: 5/5 de 2026; em 2024 só CCS (sem ano). Com ano: SEP, GBI, SIM, OBJ |
| Regra regulada ou tributária sem norma nem órgão | 6 | ETF, GBI, IVY, RES, PRE, SEL | «no Brasil, a regulamentação exige que esses proventos sejam **reinvestidos** no próprio fundo» (etf-o-que-e) | Não |
| Regulador ou instituição nomeada | 5 | SEP, ASS, PRE, SEL, TIT | «O serviço de assessoria financeira é regulamentado pela Comissão de Valores Mobiliários (CVM)» (eu-preciso-de-um-assessor-de-investimentos) | Não. Número da norma só em SEP (CVM 175) |
| Tabela vira lista ou imagem | 4 | ETF, IVY, PRE, SEL | «- 20% para aplicações de 181 a 360 dias;» (tesouro-prefixado-o-guia-completo) | Não |
| Tickers e índices brasileiros como exemplo | 4 | SEP, ETF, IVY, OBJ | «(ex: BOVA11 para o Ibovespa, IVVB11 para o S&P 500)» (etf-o-que-e) | Não |

### B9. Léxico

| Traço | nº | Posts | Evidência | Voz/época |
|---|---|---|---|---|
| Glosa do termo central na primeira menção (parêntese, aposto, "ou seja") | 13 | todos menos CDS, EAB | «“internamente homogêneo” (semelhantes entre si) e “externamente heterogêneo” (diferentes dos outros)» (a-ciencia-da-separacao) | Não |
| Jargão periférico pressuposto, sem glosa | 13 | todos menos EAB, UOC | «O recolhimento é de responsabilidade do investidor via DARF.» (etf-o-que-e) | Não. Em ASS, IVY e ETF contraria o leitor declarado |
| Registro misto: formal com coloquialismo encaixado ("te", "o sujeito", "a tal") | 9 | SEP, EAB, ASS, GBI, IVY, SIM, OBJ, RES, UOC | «Como explicar o sujeito que protege o patrimônio da família com um seguro de vida» (goal-based-investing) | Sim: 6/6 ENS/ENS-T. Só formal: CCS, ETF, PRE, SEL, TIT (todos EXP) |
| Anglicismo em par: português primeiro, original entre parênteses | 5 | SEP, ETF, GBI, IVY, SIM | «Já o conceito de Contabilidade Mental (*Mental Accounting*), desenvolvido por Richard Thaler» (goal-based-investing) | Época: 2025–26 |
| Anglicismo aceito sem glosa nem itálico | 8 | CCS, CDS, EAB, ASS, IVY, SIM, OBJ, PRE | «sem simplesmente enviar calls de operações com ações ou derivativos pela mesa da corretora?» (eu-preciso-de-um-assessor-de-investimentos) | Não. Nenhum anglicismo: RES, SEL, TIT, UOC (EXP, 2024) |
| Repete a palavra-tema em vez de variar | 8 | CCS, EAB, IVY, SIM, OBJ, RES, SEL, UOC | «mais apto a lidar com as emergências, mas não necessariamente pronto para arcar com toda e qualquer emergência.» (reservas-de-emergencia) | Não. CDS alterna sinônimos |
| Adjetivação avaliativa genérica e intensificadores ("ideal", "fundamental", "excelente") | 9 | ETF, ASS, GBI, OBJ, RES, PRE, SEL, TIT, UOC | «O Tesouro Selic é ideal para investidores que buscam segurança, liquidez e um retorno atrelado à taxa de juros básica» (tesouro-selic) | Mais denso em EXP. CCS e CDS têm clichês avaliativos |
| Maiúscula inicial em nome de conceito comum | 4 | SEP, GBI, IVY, UOC | «Faber sugere o uso de uma Média Móvel Simples de 10 meses.» (o-portfolio-da-ivy-league) | Não |
| "Agnóstico" no sentido de "indiferente" | 3 | IVY, SIM, OBJ | «um portfólio global mais coerente com a persona do investidor e menos agnóstico aos seus objetivos e desejos» (objetivos-and-classes) | 2026 |
| Campo "objetivos de vida" amarrando produto a propósito (tema) | 5 | SEP, CCS, CDS, EAB, ASS | «como relacionar um ativo aos objetivos reais de uma pessoa» (a-ciencia-da-separacao) | Tema, não estilo |

## C. Teste das regras do guia v1

Base de ENS/ENS-T: 6 posts (EAB, ASS, SIM, SEP, GBI, IVY). Base de EXP: 9 posts.

### C1. Regras do §3

| Regra | Status | nº | Evidência |
|---|---|---|---|
| 1. Nunca deixa jargão sem gloss | Contradita como "nunca" | Termo central glosado em 13; jargão periférico sem glosa em 13 | «O recolhimento é de responsabilidade do investidor via DARF.» (etf-o-que-e) |
| 2. Exemplo sempre depois do conceito | Condicionada | Conceito antes em 12; exemplo antes em 4 (SEP, ASS, IVY, SIM), todos ENS/ENS-T. Três deles estão no corpus da v1 | «Você tem 1.000 reais? Tem 10 ações disponíveis? Você coloca 100 reais em cada uma. Fim.» (o-simples-funciona) |
| 3. Dois-pontos como articulador | Confirmada | 13; EAB e TIT sem dois-pontos na prosa. "Travessão triplo": sem evidência | «entendi o conceito básico de uma fundação: uma estrutura feita para durar.» (o-portfolio-da-ivy-league) |
| 4. Sem negrito/itálico de ênfase; aspas simples no lugar | Contradita | Negrito no corpo em 8; itálico em 6. Aspas de destaque são duplas em 12; simples só em GBI | «uma estratégia conhecida como **gestão passiva**» (etf-o-que-e) |
| 5. Subtítulos H2 densos, sempre | Contradita em parte | Densos em 12, esparsos em 3 (SEP, GBI, OBJ, de 2026). Só H2 em 8; H3, H4 ou negrito em 7 | «### Quando o Nobel Falha» (o-simples-funciona) |
| 6. Estudo nomeado (autor + ano); nunca credencial | Condicionada | Estudo nomeado em 6, com ano em 4. Ausente em ASS e EAB (ENS). Sem credencial em 14; CCS declara trajetória | «trabalhando em algumas das principais instituições financeiras do país e estudando intensivamente o tema, percebi que» (comece-com-o-simples) |
| 7. Aposto/parêntese logo após o termo, com travessão duplo | Parêntese confirmado; travessão condicionado à época | Glosa em parêntese em 13. Travessão na prosa em 6 (5/5 de 2026, um par em TIT). ASS e SEL, do corpus v1, não têm | «Na maioria das corretoras — por uma conveniência técnica que ignora a lógica financeira — os ETFs» (a-ciencia-da-separacao) |
| 8. Regulador pelo nome quando o produto é regulado | Condicionada | Regulador nomeado em 5; número da norma em 1 (SEP). Regra regulada sem órgão nem norma em 6 | «no Brasil, a regulamentação exige que esses proventos sejam **reinvestidos** no próprio fundo» (etf-o-que-e) |
| 9. Placeholder de imagem como parte do argumento, com referência verbal | Sem evidência | Nenhuma linha registra referência verbal à imagem. Imagens sem legenda em 15. A imagem carrega conteúdo em ETF, IVY e OBJ; é "respiro" em SIM | «## ETF vs. Fundo Ativo vs. Ações: Onde Alocar seu Capital?» (etf-o-que-e) |

### C2. §4.1 Voz ensaística

| Item | Status | nº | Evidência |
|---|---|---|---|
| Lista da v1 (separação, objetivos, simples, assessor) | Condicionada | OBJ não cumpre o critério (vai a EXP); SEP vai a ENS-T | — |
| Abre com anedota ou pergunta provocativa | Confirmada | 5/6; EAB abre com epígrafe e ponte de série | «Tudo começa com a fundação — e não, não estamos falando dos impérios galácticos de Isaac Asimov.» (o-portfolio-da-ivy-league) |
| 1ª pessoa presente | Confirmada, não exclusiva | 6/6; também em OBJ, RES, UOC, PRE, CCS | «Sempre que escuto esses relatos, me pergunto se essas pessoas realmente precisam seguir as orientações do assessor.» (eu-preciso-de-um-assessor-de-investimentos) |
| Humor e ironia constantes | Condicionada | 5/6; EAB sem humor. "Frequente" só em SIM e ASS | «um motor de uno (*sem escada*).» (o-simples-funciona) |
| Metáfora frequente, raramente retomada no fecho | Metade contradita | Figura em 6/6; fecho retoma em 5/6 (ASS não) | «precisam de um ajuste fino tropical» (o-portfolio-da-ivy-league) |
| Pergunta retórica argumentativa | Confirmada | 6/6; também em CDS, ETF, OBJ, RES | «Mas e se a “Rocket Science” for apenas uma cortina de fumaça?» (o-simples-funciona) |
| Fecha com CTA de compartilhar e gancho | Condicionada à época | Botão em 5/6 (ASS sem CTA); gancho no fecho em 4/6 (SEP, GBI, IVY, SIM). Texto do botão tido como padrão | «Obrigado por ler o SYNTAXIS! Compartilhar este post ajuda a ampliar o alcance de ideias que merecem circular.» (o-simples-funciona) |
| Admite exceção ou incerteza | Confirmada | 6/6 | «Obviamente, se você se enquadra em um segmento de alta renda, a situação pode ser bem diferente.» (eu-preciso-de-um-assessor-de-investimentos) |

### C3. §4.2 Voz explicativa

| Item | Status | nº | Evidência |
|---|---|---|---|
| Abre com epígrafe ou definição, nunca com anedota | Confirmada | 9/9 sem anedota de abertura; epígrafe em 7. Mas a epígrafe é traço de 2024: EAB e ASS (ENS) também têm | «[[PULLQUOTE: **“O que você faz hoje pode melhorar todos os seus amanhãs.”**» (titulos-do-tesouro-nacional) |
| 3ª pessoa impessoal quase absoluta | Condicionada | Vale para PRE, SEL, TIT. "Você" direto em CDS, ETF, OBJ, RES, UOC | «O investidor pode resgatar o Tesouro Selic a qualquer dia útil sem perda de capital» (tesouro-selic) |
| Sem humor, ironia ou contra-argumento | Confirmada para humor | 8/9 sem humor; OBJ é exceção. RES relativiza o consenso | «como no caso da renda fixa — como um CDB do Banco Master? —» (objetivos-and-classes) |
| Praticamente nenhuma metáfora | Condicionada | Literal em 5 (CCS, CDS, RES, PRE, SEL) e TIT com uma figura. Figura própria em ETF, OBJ e UOC (analogia pessoa-empresa) | «Pense nele como uma cesta de ativos.» (etf-o-que-e) |
| Nunca admite incerteza; tom categórico | Condicionada | Categórico em 6 (ETF, OBJ, PRE, SEL, TIT, UOC). CCS e CDS modalizam muito; RES admite não saber | «Esse número, embora não tenha identificado sua origem, parece ser ancorado no prazo médio de recolocação de um profissional.» (reservas-de-emergencia) |
| Sem CTA; termina descrevendo o produto | Condicionada | Sem CTA em 5 (CCS, RES, PRE, SEL, TIT). CTA em CDS (enquete, consultoria), ETF (ferramenta implícita), OBJ e UOC (botão) | «[[ENQUETE]]» (conectando-dinheiro-e-sonhos) |

### C4. §5 Movimentos aspiracionais (aparecem nos posts?)

| Mov. | Status | nº | Evidência |
|---|---|---|---|
| 1. Cena datada antes da tese | Presente | 2 (GBI, SIM), ambos 2026 | «No feriado de Carnaval viajei para a cidade de Três Lagoas no Mato Grosso do Sul para o casamento de um amigo.» (goal-based-investing) |
| 2. Travessão duplo para aside irônico | Presente | 5 (SEP, GBI, IVY, SIM, OBJ), todos 2026; nenhum em 2024 | «E aí está o ponto curioso — e um pouco irônico: existe uma estratégia» (o-simples-funciona) |
| 3. Admite limite técnico e delega à fonte | Sem evidência do movimento completo | Partes soltas: delega o método à fonte (IVY, SEP); admite não saber a origem de uma regra (RES) | «Faber propôs que o investidor comum poderia replicar os retornos dos *Endowments*» (o-portfolio-da-ivy-league) |
| 4. Omitir o porquê; justaposição | Presente | 2 (ASS: fecho irônico que puxa a conclusão sem dizê-la; EAB: confia que o leitor entendeu) | «Num primeiro momento, ele pode gerar uma ótima remuneração ao assessor e à corretora.» (eu-preciso-de-um-assessor-de-investimentos) |
| 5. Repetir a palavra-chave | Presente | 8. Fio deliberado em SIM ("ingênuo"), UOC ("controle"), OBJ ("fluxo"). CDS faz o oposto | «ter suas finanças pessoais sob controle.» (um-objetivo-para-comecar) |
| 6. Definir o termo no instante | Condicionada (= regra 1) | Central glosado em 13; periférico sem glosa em 13 | «Um ETF é um fundo de investimento negociado na Bolsa de Valores como se fosse uma ação.» (etf-o-que-e) |
| 7. Casos em série que testam a tese | Presente (a v1 diz "não testado") | 3 (ASS: lista de 5 itens examinada um a um; SEP: critério por critério; EAB: três critérios paralelos) | «Decidi iniciar este post de uma maneira menos convencional. Perguntei ao ChatGPT, na versão 4,» (eu-preciso-de-um-assessor-de-investimentos) |
| 8. Validar a intuição, minar, fechar em aforismo | Presente | 4 (SIM, ASS, RES, SEP) | «Markowitz não é um qualquer.» (o-simples-funciona) |

### C5. §6 Tensões

| Tensão | Status | Evidência |
|---|---|---|
| Regra 1 × mov. 4 (omitir) | Condicionada. A regra 1 já não é absoluta: 13 posts deixam jargão periférico sem glosa. O mov. 4 aparece em ASS e EAB | «Sem cálculo estocástico. Sem descontar fluxos de caixa futuros.» (o-simples-funciona) |
| Humor ensaístico × explicativa sem humor | Confirmada: humor em 5/6 ENS/ENS-T e em 1/9 EXP | «com seu desejo de comprar um iate» (o-portfolio-da-ivy-league) |
| Metáfora não retomada × imagem sustentada | Contradita. O fecho retoma figura ou palavra-tema em 8. Imagem sustentada do começo ao fim em SEP, GBI, IVY, SIM (2026) | «Podia até parecer, mas não.» (a-ciencia-da-separacao) |

### C6. §8 Em observação

| Item | Status | nº | Evidência |
|---|---|---|---|
| Reticências para continuidade ou exemplos abertos | Condicionada; não promover | 4 posts, mas lista aberta só em OBJ. Nos outros: citação simulada (RES), teaser "Continua …" (IVY, SIM) | «E os fundos de investimento? Ativos alternativos… Por que elas são relevantes?» (objetivos-and-classes) |
| Analogia autobiográfica da formação em matemática | Confirmada; promover | 4 (SEP, IVY, SIM, OBJ), todos 2026 | «Desde meus primeiros dias no curso de matemática, algo ficou muito claro: matemáticos amam classificar e quantificar.» (objetivos-and-classes) |
| Ironia contra a indústria como antagonista coletivo, nunca pessoa nomeada | Confirmada com ressalva | Antagonista sem nome em 7; ironia explícita em 4 (SEP, ASS, SIM, RES). Ressalva: casos de fraude nomeados como ironia (SEP, OBJ) e trocadilho com nome de pessoa (GBI) | «O mercado financeiro adora nomes complicados para esconder verdades simples.» (a-ciencia-da-separacao) |
| LinkedIn | Sem evidência | O digest só tem Substack | — |

Extra (§7.2, fora do pedido):
- "O corpus não mostra tríade": contradito. Tríade em 8 posts (B1).
- "Nunca fecha com resumo genérico": contradito. Conclusão recapitulativa marcada como tique em 11 (E).

## D. Linha do tempo

Períodos: 2024 (set–nov) = 9 posts. 2025 = 1 post (ETF). 2026 (jan–mar) = 5 posts.
Vozes: 2024 = ENS 2 (EAB, ASS), EXP 7. 2025 = EXP 1. 2026 = ENS 1 (SIM), ENS-T 3, EXP 1 (OBJ).

| Traço | 2024 (9) | 2025 (1) | 2026 (5) |
|---|---|---|---|
| **Somem depois de 2024** | | | |
| Epígrafe em pullquote na abertura | 9 | 0 | 0 |
| Comprimento uniforme, sem frase curta de ênfase | 7 | 0 (ETF: variação moderada) | 0 |
| Modalização frequente | 6 (CCS, CDS, EAB, ASS, RES, UOC) | 0 | 0 |
| "Eu" de opinião e metadiscurso | 3 (EAB, ASS, RES) | 0 | 0 |
| Nenhum anglicismo | 4 (RES, SEL, TIT, UOC) | 0 | 0 |
| Subtítulo em forma de pergunta | 6 | 1 | 1 (SEP) |
| Aspas retas no corpo | 5 (CDS, EAB, TIT, UOC; RES em parte) | 1 | 0 (todas curvas) |
| **Surgem em 2025–26** | | | |
| Travessão na prosa | 1 (TIT, um par) | 0 | 5 |
| Frase curta de ênfase | 2 (ASS, RES) | 1 | 5 |
| "Não X, mas Y" | 1 (CDS, só no fecho) | 1 | 5 |
| Anglicismo em par português/original | 0 | 1 | 4 (SEP, GBI, IVY, SIM) |
| Itálico para estrangeirismo ou obra | 1 (PRE, só obra) | 1 | 4 (OBJ não) |
| Estudo acadêmico nomeado | 1 (CCS, sem ano) | 0 | 5 |
| "Eu" de memória ou anedota | 0 | 0 | 5 |
| Anedota da formação em matemática | 0 | 0 | 4 |
| Referência pop ou de atualidade | 0 | 0 | 5 |
| Fecho retoma imagem desenvolvida | 0 (só palavra-tema: CDS, EAB, RES, UOC) | 0 | 4 (SEP, GBI, IVY, SIM) |
| Botão de compartilhar | 2 (EAB, UOC) | 0 | 5 |
| Subtítulos esparsos (~300+ palavras) | 0 | 0 | 3 (SEP, GBI, OBJ) |
| **Persistem** | | | |
| Seção "Conclusão" | 8 (CCS não) | 1 | 4 (SEP não) |
| Gerúndio de consequência | 6 (CCS, ASS, RES, PRE, SEL, TIT) | 1 | 3 (SEP, GBI, OBJ) |
| Rótulo + dois-pontos em lista | 5 (ASS, RES, SEL, UOC, PRE) | 1 | 2 (SEP, IVY) |

Também persistem em todos os períodos: glosa do termo central com jargão periférico sem glosa, dois-pontos articulador, parágrafos curtos, Title Case, promessa de continuação, autoridade implícita, imagens sem legenda.

Leitura:
- 2024 tem dois registros: verbete de produto (PRE, SEL, TIT) e texto de conselho em 1ª pessoa, modalizado, com epígrafe.
- ETF (2025) é um guia isolado de formato SEO. É o post com mais tiques marcados (ver E).
- 2026 consolida a voz ensaística, quase toda em registro técnico.
- Travessão e "não X, mas Y" surgem juntos em 2026. O extrator de SEP liga os tiques às passagens com travessão longo; os de SIM e IVY dizem que os traços são compatíveis com escrita humana.

## E. Tiques que os extratores marcaram como possível texto gerado por IA

Fonte: linhas `antipadrao (b)` e `incerteza` de cada post.

| Post | Voz | Tiques marcados | Onde | Leitura do extrator | Uso como base "só do autor" |
|---|---|---|---|---|---|
| SIM | ENS | Nenhum tique claro. Próximos: tríades, "A conclusão deles foi impactante.", texto do CTA | Pontual | "compatível com escrita humana" | Base limpa |
| IVY | ENS-T | "não é apenas X; é Y" (4x), "elegante em sua simplicidade", fragmento de efeito, tríades, CTA | Espalhado | "não é indício de geração" | Base limpa |
| CCS | EXP | "Vale ressaltar que", clichês avaliativos, metatexto de anúncio, tríades, decalques do inglês | Espalhado | "hábito do autor, não contaminação" | Base, com cautela no léxico |
| CDS | EXP | Conclusão que só recapitula, lugares-comuns, "não é apenas X, mas Y", fecho exortativo, "Na verdade," | Fecho e Conclusão | "tiques são do autor" (não do pipeline) | Base sem a Conclusão |
| EAB | ENS | Binômios abstratos, "Isso ajudará a garantir que", recapitulação genérica | Só na Conclusão, que muda de registro | Não permite concluir se houve ferramenta externa | Base sem a Conclusão |
| ASS | ENS | Fecho com "Em resumo", "é fundamental que", "é crucial"; cadência gerada nas definições; lista do ChatGPT | Conclusão, dois parágrafos definicionais e a lista (declarada pelo autor) | Não permite dizer se houve IA além da lista declarada | Base sem lista, definições e Conclusão |
| GBI | ENS-T | "não X, mas Y" (~6x), clichês, gerúndio em cadeia, clivadas, fecho ornamental | Seções Thaler, Hiperpersonalização e Conclusão; o resto é coloquial e tem erros | Não permite dizer se esses trechos tiveram outra origem ou edição | Base só com cena e trecho histórico |
| SEP | ENS-T | Gerúndio encadeado, "não X; Y", aforismo genérico, texto do CTA | Passagens expositivas sobre ETF e CVM, com travessão longo; a anedota usa hífen e tem deslizes | Não permite atribuir autoria; registra coincidência. Blocos de critérios e CVM parecem paráfrase da fonte | Base com a anedota e a aplicação; cautela nos blocos parafraseados |
| OBJ | EXP | Definição do GBI genérica, com paralelismo e gerúndio; Conclusão recicla o corpo; texto do botão | Parágrafo de definição do GBI e Conclusão | A mudança de registro não basta para atribuir origem | Base sem definição do GBI e Conclusão |
| RES | EXP | Listas de 5 itens com rótulo e gerúndio final, fatores genéricos, Conclusão-resumo | Listas, parágrafo dos fatores de recolocação e Conclusão; a prosa em volta tem 1ª pessoa e deslizes | Podem ser do autor ou de assistência externa; não permite decidir | Base só com a prosa em volta |
| UOC | EXP | Pares de adjetivos, clichê de jornada, elogio genérico, "Em termos simples,", listicle, Conclusão genérica | Segunda metade (listas) e Conclusão | Reconhecimento de padrão, não prova de autoria | Base com a primeira metade |
| PRE | EXP | "Vale destacar que", gerúndio em cadeia, "Em resumo", pares sinonímicos, esqueleto-modelo, "Fique atento!" | Texto inteiro | Neutro; o formato de guia pode ditar os traços | Só para traços de formato |
| TIT | EXP | Gerúndio em cadeia ("garantindo" 5x, "ajudando" 5x), "papel fundamental", tríade no fecho, "Além disso" | Texto inteiro | Não permite concluir nada sobre a origem | Só para traços de formato |
| SEL | EXP | Tríades, gerúndio avaliativo, Conclusão genérica, superlativo promocional, "Hoje, vamos explorar", Title Case | Texto inteiro | Não dá para saber se é a voz do autor | Fora da base |
| ETF | EXP | Abertura genérica, antíteses em série, tríades realçadas, "Vamos dissecar", intensificadores, listas com rótulo, Title Case, Conclusão | Texto inteiro | Densidade de tiques e template SEO; não permite saber se é voz do autor ou ferramenta | Fora da base |

Contagem:
- Tiques marcados em 14 dos 15 posts. SIM é o único sem tique claro.
- Dúvida explícita de origem em 6: EAB, ETF, ASS, GBI, RES, SEL. ASS declara o uso do ChatGPT numa lista.
- Extrator atribui ao autor, ou lê como coincidência, em 3: CCS, CDS, IVY.
- Neutros em 5: SEP, OBJ, PRE, TIT, UOC.

Tiques mais marcados (nº de posts):
- Conclusão recapitulativa ou genérica: 11 (CDS, EAB, ETF, ASS, GBI, OBJ, RES, PRE, SEL, TIT, UOC).
- Clichê, adjetivação genérica ou superlativo: 10 (CCS, CDS, SEP, ETF, ASS, GBI, PRE, SEL, TIT, UOC).
- Gerúndio de consequência: 8 (SEP, ASS, GBI, OBJ, RES, PRE, SEL, TIT).
- "Não X, mas Y": 6 (SEP, CDS, ETF, GBI, IVY, OBJ).
- Tríade: 6 (CCS, ETF, IVY, SIM, SEL, TIT).
- Lista com rótulo em negrito e dois-pontos: 4 (ETF, ASS, RES, UOC).
- Texto do CTA ("Vamos levar esse conhecimento mais longe?"): 4 (SEP, IVY, SIM, OBJ).

Implicações para a linha de base:
- A premissa "escrito só pelo autor" é falsa para ASS: o próprio texto declara o uso do ChatGPT.
- A seção "Conclusão" é o principal lugar dos tiques. Não deve informar o guia.
- Linha de base sem recorte: SIM e IVY. Com cautela no léxico: CCS.
- Linha de base com recorte de trechos: CDS, EAB, ASS, GBI, SEP, OBJ, RES, UOC.
- Fora da base: ETF e SEL. PRE e TIT servem só para formato.
- Gerúndio de consequência, "não X, mas Y" e tríade aparecem nos dois tipos de post: nos que os extratores atribuem ao autor e nos marcados. Não devem virar regra de voz sem novo teste.
