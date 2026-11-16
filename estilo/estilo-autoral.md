---
versao: 2.0.0
atualizado_em: 2026-11-16
commit_base: a399245
corpus: { textos: 32, palavras_publicadas: 55400, posts: 31, periodo: "2024-09-06 a 2026-11-15 — ver estilo/corpus-manifest.json" }
confianca_global: alta
confianca_nota: "alta para forma (parágrafo, pontuação, ênfase, arquitetura), medida no texto publicado e nas edições do autor; média para léxico e postura, porque a era pipeline mistura autor e sistema e 14 dos 15 posts anteriores têm tiques de IA marcados (ver §10)"
---

# Guia de voz — Syntaxis

## 1. Retrato em cinco linhas

Você explica finanças como quem já foi aluno de matemática antes de ser do mercado: glosa o
termo que importa no instante em que ele aparece, ancora tudo em fonte, lei ou conta, e não
resiste a uma ironia seca sobre a indústria que descreve. O texto abre numa cena ou num caso
concreto, planta uma tese curta, discorda de crenças (nunca de pessoas) e fecha voltando à
imagem do começo. A forma é a assinatura mais estável: parágrafo curto, frase curta como
virada, dois-pontos como articulador, glosa entre parênteses, negrito só no que importa. Você
tem três vozes (§4), e a escolha da voz vem antes da primeira frase.

## 2. Objetivos do meu texto

| Tipo de texto | Objetivo | Fonte |
|---|---|---|
| Post de Substack | Educar e construir audiência para o funil vigente | `../../strategy/FUNIL.md` |
| Conteúdo de curso | Ensinar com rigor, sustentar credibilidade técnica | inferido, a confirmar |
| Marketing/aquisição | Falar às personas `#GENZ-FEAR`, `#GENZ-GREED`, `#Millennials-FEAR`, `#Millennials-GREED` | `../../strategy/AUDIENCES.md` §3 |

Detalhamento de público e personas: `../../strategy/AUDIENCES.md` e `../../strategy/MARKETING.md`.

## 3. Regras (voz atual — descritivo)

Valem para as três vozes, salvo indicação. Cada regra traz evidência de pelo menos dois posts
publicados (`estilo/corpus/publicados/<slug>.md`) e, quando há, a medida no texto publicado da
era pipeline (16 posts, `pesquisa/epico-revisao-editorial/dados/b3-estratos.json`). "Edição do
autor" quer dizer o que ele mudou entre o `post.md` final e o site (`estilo/corpus/edicoes/`).

### Forma

1. **Parágrafo curto; frase curta isolada como virada.** Média de cerca de 35 palavras por
   parágrafo e perto de 45% de parágrafos de uma frase (site: 34,3 e 43,9%). A frase curta fecha um
   período longo e muitas vezes ocupa o parágrafo sozinha. Edição do autor: divide parágrafos em
   16 de 16 posts (174 divisões; 115 em parágrafos do próprio rascunho).
   Evidência: «Parece uma blindagem completa. Não é.» (a-anatomia-e-o-verdadeiro-risco-do); «Ficar
   custou caro. Sair também.» (should-i-stay-or-should-i-go); «Kojirō morreu ali, na areia.»
   (samurais-e-duelos-no-mercado-financeiro).

2. **Dois-pontos é o articulador principal** — anuncia definição, resposta, revelação ou lista
   (16 de 16 posts; site: 14,3 por mil palavras). `[cross-gênero]`
   Evidência: «O lastro era outro: debêntures emitidas pelas próprias empresas do grupo.»
   (a-anatomia-e-o-verdadeiro-risco-do); «O que define o caos é outra coisa: a sensibilidade às
   condições iniciais.» (borboletas-caos-e-carreira).

3. **Glosa e inciso vão entre parênteses; aposto, entre vírgulas; travessão é raro.** O parêntese é
   o veículo da glosa em 16 de 16 posts. O travessão some da prosa em 8 de 16, inclusive nos quatro
   últimos; no site fica em 3,9 por mil palavras. Teto prático: cerca de 3 por mil, nunca em título
   ou subtítulo. Edição do autor: corta 46% dos travessões do `post.md` (236 → 127).
   Evidência: «convexa (no sentido do cálculo: arqueada para cima, como o fundo de uma tigela)»
   (a-corda-e-o-arco); «Os atalhos (decorar fórmulas, dominar uma ferramenta específica, apertar
   botão) são exatamente o que a IA vai comoditizar.» (borboletas-caos-e-carreira).

4. **Ênfase com função, e só com função.**
   - **Negrito** na frase-tese (9 posts), no termo-chave na primeira definição (7) e em nome
     próprio ou obra na primeira menção. Sem cota: a média no site é 4 por mil palavras, mas varia
     de zero (frequencia-de-capitalizacao) a ~8 por mil (coqueiros-e-cacaueiros). Nunca negrito
     espalhado em todo substantivo. Presente em 27 dos 31 posts do site.
   - **Itálico** em estrangeirismo, variável e título de obra (16 de 16). Ênfase de palavra única
     em itálico, rara.
   - **Aspas curvas.** Simples para termo mencionado ou tomado com distância; duplas para citação,
     fala e expressão de mercado entre aspas. Nunca aspas retas no texto final.
   Edição do autor: acrescenta 128 negritos e 60 itálicos e corta 93 aspas simples de ênfase.
   Evidência: «**Raiva de você mesmo vira paralisia.**» (samurais-e-duelos-no-mercado-financeiro);
   «Essa é a **convenção de capitalização**: linear ou composta.»
   (voce-esta-contando-os-dias-errado); «qual fonte de captação — o *funding* — saía mais barata»
   (a-anatomia-e-o-verdadeiro-risco-do); «era uma taxa ‘efetiva-dia’, acumulada de forma composta»
   (a-corda-e-o-arco); «A B3 chama a convenção de 252 dias úteis de “conversão exponencial 252”»
   (frequencia-de-capitalizacao).

5. **Subtítulo H2 por movimento do argumento, como frase-tese ou figura, nunca rótulo.** Um a cada
   ~190–440 palavras (16 de 16). O nome de um movimento da estrutura ("Fechamento", "Movimento 7")
   não vira título. Edição do autor: tira "Fechamento:" de H2 em 3 posts e encurta subtítulos.
   `[cross-gênero]`
   Evidência: «## Render todo dia não é render mais» (frequencia-de-capitalizacao); «## Se tudo é
   caos, para que escolher?» (borboletas-caos-e-carreira).

6. **Nenhuma exclamação no corpo do texto** (16 de 16 posts da era pipeline; site: 0,05 por mil).
   A intensidade vem da frase curta, não do ponto.
   Evidência: «Quero muito saber qual foi.» (coqueiros-e-cacaueiros); «Promessa é dívida.»
   (a-anatomia-e-o-verdadeiro-risco-do).

### Arquitetura

7. **Abre numa cena ou num caso concreto antes de qualquer conceito** — caso real datado, cena
   pessoal, ou enigma numérico (14 de 16; ausente só na voz explicativa). Datado quando houver data.
   Evidência: «Em 1612, numa pequena ilha entre Kyushu e Honshu, um espadachim de 29 anos desceu de
   um barco» (samurais-e-duelos-no-mercado-financeiro); «Novembro de 2025. O Banco Central decreta
   a liquidação extrajudicial do Banco Master.» (dividir-para-nao-correr-risco).

8. **No corpo, o conceito vem antes do exemplo** (10 de 16). Exceção: na voz ensaística o caso pode
   vir antes da ideia (3 posts). `[cross-gênero]`
   Evidência: «A taxa efetiva, i, é o que de fato rendeu no fim do ano:» (frequencia-de-capitalizacao);
   contraexemplo ensaístico: «Agora traga isso para a sua carreira.» (coqueiros-e-cacaueiros).

9. **Expõe a versão corrente, concede a parte válida e a corrige** — discorda de crenças e leituras,
   nunca de pessoas (16 de 16).
   Evidência: «A versão que se conta sobre debênture é simples.» (renda-fixa-condicoes-variaveis);
   «É uma ótima história. Só que não aconteceu assim.» (samurais-e-duelos-no-mercado-financeiro);
   «Para ele, se você consegue aumentar, não é sorte, é trabalho. No rigor, ele tem razão.»
   (borboletas-caos-e-carreira).

10. **Fecha em anel: volta à cena, ao caso ou à conta da abertura** (15 de 16; também em 8 dos 15
    posts anteriores).
    Evidência: «Com o que vimos até aqui, dá para reler o caso.» (renda-fixa-condicoes-variaveis);
    «Mick Jones não escolheu a data da própria saída.» (should-i-stay-or-should-i-go).

11. **Costura de série: retoma o texto anterior ou a promessa feita, e anuncia o próximo** (14 de 16).
    Evidência: «No fim do último texto, deixei uma conta para você.» (frequencia-de-capitalizacao);
    «No último Spoiler, falei sobre os difíceis.» (borboletas-caos-e-carreira).

### Figura, postura e leitor

12. **Uma metáfora central, muitas vezes nomeada, estendida do título ao fecho** (14 de 16); o
    rótulo declarado vira vocabulário da série (motor, régua, etiqueta, coqueiros, os difíceis).
    Evidência: «Chamamos essa contagem de régua.» (a-corda-e-o-arco); «Daqui em diante, vou chamar de
    ‘coqueiros’ as *skills* que entregam valor relevante com pouco ou nenhum gasto de energia.»
    (coqueiros-e-cacaueiros); «A B3 não trocou de motor. Trocou de etiqueta.»
    (frequencia-de-capitalizacao).

13. **Autoridade por fonte nomeada — estudo (autor, ano), lei pelo número, regulador pelo nome —,
    nunca por credencial própria** (15 de 16). A norma vai pelo número quando o dispositivo é o
    ponto (9 posts). `[cross-gênero]`
    Evidência: «Thomas Ho e Anthony Saunders, num artigo de 1981 no Journal of Financial and
    Quantitative Analysis» (dividir-para-nao-correr-risco); «Pelo art. 52 da Lei nº 6.404/1976, a
    Lei das S.A., ela dá ao titular um direito de crédito» (renda-fixa-condicoes-variaveis).

14. **Termo técnico glosado na primeira ocorrência, em parêntese, com definição funcional curta**
    (16 de 16; siglas glosadas no site: 52%). O jargão que o leitor daquele texto já domina pode
    ficar sem glosa (6 posts de carreira). `[cross-gênero]`
    Evidência: «CVM (Comissão de Valores Mobiliários)» (a-anatomia-e-o-verdadeiro-risco-do); «numa
    mesa de banco, de gestora ou de corretora (no mercado, ‘mesa’ é a equipe de uma área, como renda
    fixa ou ações)» (should-i-stay-or-should-i-go).

15. **Imperativo que conduz o raciocínio, não que vende** — "Repare", "Pense", "Volte", "Imagine"
    (14 de 16).
    Evidência: «Repare no detalhe: 252 é uma convenção, não uma contagem.»
    (voce-esta-contando-os-dias-errado); «Agora quebre a premissa.» (quando-os-modelos-se-rebelam).

16. **Admite limite.** Na voz ensaística, com hedge pessoal; nas outras, com limite factual ("em
    tese", "cerca de", "pelo menos") (15 de 16).
    Evidência: «Por quê? Sinceramente, não sei até hoje.» (borboletas-caos-e-carreira); «A espécie
    define, em tese, o seu lugar na fila se a empresa quebrar. Em tese, porque»
    (renda-fixa-condicoes-variaveis).

17. **Humor seco, ocasional, nas três vozes** — no máximo uma vez por bloco, sem piada marcada
    (14 de 16).
    Evidência: «Promessa é dívida. E, neste texto, a palavra *dívida* vai aparecer bastante.»
    (a-anatomia-e-o-verdadeiro-risco-do); «Foi buscar um café.» (borboletas-caos-e-carreira).

18. **Registro culto com coloquialismo e ditado encaixados; "te" convive com "você"** (15 de 16).
    Evidência: «Juro simples é coisa de livro escolar e de agiota de bairro.» (a-corda-e-o-arco);
    «Até aqui, é o que qualquer material de corretora te conta.» (dividir-para-nao-correr-risco).

19. **Dado com data e fonte; números no padrão brasileiro** (14 de 16).
    Evidência: «O estoque de LCI saiu de R$ 141 bilhões ao final de 2020 para R$ 544 bilhões em junho
    de 2026» (dividir-para-nao-correr-risco); «Num CDB prefixado à mesma taxa, o rendimento é de
    R$ 67.707,83.» (a-corda-e-o-arco).

20. **Antítese corretiva em duas frases ("não é X. É Y.") carrega a tese e as viradas — com teto.**
    Está nos 16 posts da era pipeline e nos rascunhos do autor na mesma taxa (0,83 por mil contra
    0,81 do pipeline); o autor não a corta. Os extratores a marcam como possível tique de IA quando
    vem em série. Teto: cerca de uma por seção, nunca duas seguidas, nunca como fecho automático de
    todo bloco (decisão do autor, 2026-11-16).
    Evidência: «Securitizar muda o endereço do risco. Não muda o tamanho dele.»
    (a-anatomia-e-o-verdadeiro-risco-do); «Capitalização não é lei da natureza. É cláusula.»
    (a-corda-e-o-arco).

## 4. As três vozes

A linha editorial (Spoiler, Notas de um Professor) e a voz são eixos separados. Na prática, desde
outubro de 2026, Spoiler usa a ensaística e Notas usa a ensaística em registro técnico; a
explicativa não aparece desde 20/09/2026.

### 4.1 Ensaística (8 dos 16 posts da era pipeline; o-simples-funciona e eu-preciso-de-um-assessor antes)

- Abre em cena pessoal ou histórica; primeira pessoa do singular confessional ou opinativa.
- Tom de mentor para quem começa; antecipa o que o leitor já viveu («Você provavelmente já
  desconfiava disso.», o-mundo-invertido-dos-investimentos).
- Vocabulário de finanças como metáfora de carreira e vida («Ela muda a taxa de câmbio: a mesma hora
  de estudo rende mais onde você tem facilidade.», coqueiros-e-cacaueiros).
- Analogia autobiográfica da formação em matemática como ponte (borboletas, coqueiros, o mundo
  invertido das carreiras, should; antes: a ciência da separação, ivy league, o simples funciona).
- Seção de ressalva que antecipa a leitura errada da própria tese («Este texto tem um risco, e
  prefiro nomeá-lo», coqueiros-e-cacaueiros).
- Fonte citada pelo nome no corpo, sem referência formal; matemática verbalizada, sem notação.
- Fecho: pedido de resposta pessoal ou CTA de compartilhamento condicionado ao efeito do texto,
  nunca genérico («Se você reconheceu seu próprio primeiro ano de investidor em algum parágrafo aí
  de cima, mande esse texto pra alguém», o-mundo-invertido-dos-investimentos).
- Pergunta retórica como ferramenta em parte dos posts (frequente em borboletas, samurais, should);
  nunca como abertura automática de seção.

### 4.2 Ensaística em registro técnico (6 dos 16; a ciência da separação, goal-based-investing e ivy league já em jan–mar/2026)

Estrutura de ensaio com corpo de aula. É a voz padrão da linha Notas de um Professor.
- Gancho por caso real datado ou enigma numérico.
- **Tese em refrão de duas frases**, plantada na abertura e repetida no fecho (literal em anatomia,
  corda, frequência, renda fixa).
- Glosa sistemática; fórmula display anunciada por dois-pontos e glosada depois ("onde", "em que")
  («O montante cresce em progressão geométrica:», a-corda-e-o-arco); conta resolvida até o número
  final.
- Quadro de perguntas: roteiro no começo e/ou checklist no fim («Antes de olhar a taxa, quatro
  perguntas:», a-anatomia-e-o-verdadeiro-risco-do).
- Primeira pessoa só para costurar a série; "você" didático.
- Fecho técnico: «Se o texto funcionou, você consegue … sozinho» + exercício + "Para continuar
  aprendendo", com referências comentadas pela função da obra (a-corda-e-o-arco,
  frequencia-de-capitalizacao).
- Estrutura de aula detalhada em `docs/BACKWARDS_DESIGN.md` (Ficha de Saída, movimentos).

### 4.3 Explicativa (em desuso desde set/2026: o-papel-do-cdb e o-agro-e-pop; 9 posts de 2024–2025)

- Referência de produto ou conceito sem tese em disputa; abre com tese aforística ou definição,
  nunca com anedota.
- Terceira pessoa; primeira pessoa só para continuidade da série.
- Categórica no conteúdo, mas admite limite factual («nem o regulador nem o investidor têm hoje uma
  forma simples de medir a proporção exata.», o-agro-e-pop-o-agro-e-produto-financeiro).
- Sem CTA em prosa.

### 4.4 Acadêmica (dissertação — não usar em Substack)

Terceira pessoa ou plural de modéstia; Definição → Teorema → Demonstração; zero metáfora. Daqui vem o
rigor de definir antes de usar (regra 14).

**Como decidir a voz.** Tese defendida com memória ou opinião pessoal → ensaística. Conceito ou
produto ensinado com tese em refrão e conta → ensaística em registro técnico. Verbete de produto sem
tese → explicativa (hoje rara). Escolha antes da primeira frase e registre no briefing.

## 5. Movimentos aspiracionais

Extraídos de Michael Lewis, Ernest Hemingway e Malcolm Gladwell (`_arquivo/MANIFESTO.md`).
Procedimento, nunca vocabulário. Desde a v2.0.0, a cena datada antes da tese (Lewis, antigo
movimento 1) e "validar a intuição, miná-la, fechar em aforismo" (Gladwell, antigo 8) são traços
medidos da voz (regras 7 e 9) e saíram desta camada. O aside irônico com travessão (antigo 2) saiu:
contraria a direção medida da regra 3; o aparte irônico do autor vai em parêntese.

1. **Admitir o limite do próprio entendimento técnico e transferir a validação à fonte** (Lewis).
   Sem evidência nos 31 posts. Gatilho: matemática financeira avançada que o texto não vai provar.
2. **Confiar no leitor: omitir o porquê e deixar a justaposição falar** (Hemingway). Sem evidência
   na era pipeline. Gatilho: um momento de maior impacto por post ensaístico; nunca no lugar da
   regra 14.
3. **Repetir a palavra-chave em vez de variar** (Hemingway). Presente em 3 posts. Gatilho: quando o
   argumento reabilita um termo.
4. **Casos numerados que testam a tese** (Gladwell). Hoje a numeração aparece como passos ou sinais
   prescritivos (5 posts), não como casos que testam. Gatilho: post ensaístico longo com mais de uma
   fonte.

## 6. Tensões conhecidas

- **Antítese corretiva: voz ou tique?** Ver regra 20. O autor a escreve no rascunho e a mantém no
  site; em série, ela vira cadência mecânica. O teto resolve na prática; a medida (Fase E) decide se
  ele está certo.
- **Era pipeline mistura autor e sistema.** Os 16 posts recentes passaram por edição do pipeline;
  as regras de forma se apoiam no que o autor fez na publicação (edições), que é sinal só dele.
- **Regra 14 × movimento 2 (omitir).** Resolvida a favor da regra 14 nas três vozes; o movimento 2
  fica para um momento por post ensaístico.

## 7. Antipadrões

### 7.1 Confirmados pela edição do autor (ele corta ou troca no site)

- Travessão acima do teto, em subtítulo ou como continuação de subtítulo ("— e por que…").
- Parágrafo longo (acima de ~60 palavras) sem quebra.
- Aspas simples de ênfase onde cabe itálico (estrangeirismo) ou nada.
- Rótulo de movimento em H2 ("Fechamento: …").
- Dado trazido pela pesquisa que não serve ao argumento (o autor cortou 1.123 palavras assim).
- Resíduo do processo no texto: `[VERIFICAR]`, `[FAIXA]`, `[PREENCHER]`, `[LINK: …]`, menção a
  "etapa" do pipeline.
- Seção final "Conclusão" que só recapitula (frequente nos posts de 2024, ausente desde 2026).
- Exclamação no corpo.

### 7.2 Tiques de IA calibrados (medidos contra o texto do autor)

O pipeline já não produz os tiques genéricos da lista em `pesquisa/frente-d-antipadroes-ia-ptbr.md`
(taxa ~0 em todos os grupos; ver `pesquisa/epico-revisao-editorial/01-diagnostico.md` D6). Vigiar:
- **Cortados pelo autor:** travessão denso; construções "— não …", "— a …", "— o …" (sobrevivem 43–58%).
- **Marcados pelos extratores, com teto:** antítese "não é X. É Y." em série; teaser ou metadiscurso
  de anúncio ("O interessante começa agora", "Aqui mora…", "É aí que entra…"); fecho-síntese de
  fórmula ("Dito direto:", "Se fosse para levar uma única ideia…"); tríade em série; frase-golpe em
  série.
- **Não é tique (não "corrigir"):** glosa entre parênteses (o autor mantém 85–100%); negrito em
  nome, definição e frase-tese; pergunta retórica com função.

## 8. Em observação

Evidência insuficiente para regra; candidatos para a próxima colheita (`/forja-de-voz colher`):
- Pergunta retórica: frequente em 6 posts, evitada ou convertida em afirmação em 7. A frequência
  depende do post.
- Ironia contra a indústria e o material de venda como antagonista coletivo, nunca pessoa nomeada:
  6 posts da era pipeline e 7 anteriores. Candidata forte a regra na próxima versão.
- Citação em bloco para destacar frase do próprio autor (5 posts).
- Imagem antes do primeiro parágrafo (5 posts).
- Figura anunciada por frase com dois-pontos ("Lado a lado com os produtos dos textos anteriores:"),
  sem legenda (6 posts, só nas vozes técnica e explicativa). O placeholder com legenda e alt-text é
  regra do pipeline (`.claude/agents/prompts-visuais.md`), não da voz.
- LinkedIn: nenhuma amostra. Todo traço "de Substack" pode ser, na verdade, "de não-LinkedIn".

## 9. Checklist de aderência

Usado no modo `auditar` de `/forja-de-voz`. Os itens marcados (m) são mecânicos e conferidos por
script (`scripts/checar_post.py`, onda 2 do épico).

1. A voz foi escolhida (§4) e o texto não mistura as três?
2. (m) Parágrafo médio perto de 35 palavras, sem parágrafo acima de ~90? (regra 1)
3. (m) Travessão abaixo de ~3 por mil palavras e nenhum em título ou subtítulo? (regra 3)
4. Negrito, quando houver, só em frase-tese, termo-chave e nome/obra (sem cota); itálico em
   estrangeirismo; aspas curvas com função? (regra 4)
5. (m) H2 como frase-tese, sem rótulo de movimento? (regra 5)
6. (m) Nenhuma exclamação no corpo? (regra 6)
7. Abre em cena ou caso, e fecha voltando a ele? (regras 7 e 10)
8. Todo termo técnico central glosado na primeira ocorrência, em parêntese? (regra 14)
9. Afirmação de peso sustentada por fonte nomeada, lei pelo número ou conta? (regra 13)
10. Antítese "não é X. É Y." dentro do teto, e nenhum tique da §7.2 em série? (regra 20)
11. (m) Nenhum resíduo do processo (`[VERIFICAR]`, `[FAIXA]`, `[PREENCHER]`, `[LINK:`, "etapa" do
    pipeline)? (§7.1)

## 10. Corpus e método (v2.0.0)

- **Corpus.** 31 posts publicados, capturados do site (`_arquivo/publicados/`, normalizados em
  `estilo/corpus/publicados/`), mais a dissertação. Os 16 da era pipeline (ago–nov/2026) descrevem a
  voz atual; os 15 anteriores (2024–mar/2026) são linha de base. As 6 amostras de Substack da v1 saíram
  do agregado: a conversão apagou o negrito e trocou aspas duplas por simples
  (`pesquisa/epico-revisao-editorial/00-corpus.md` §5).
- **Edições do autor** entre o `post.md` final e o site (`estilo/corpus/edicoes/`) contam como
  evidência de primeira classe: reversão ou acréscimo que se repete em 3 ou mais posts é evolução
  deliberada.
- **Linha de base pré-pipeline.** 14 dos 15 posts anteriores têm tiques de IA marcados pelos
  extratores, sobretudo na seção "Conclusão"; eu-preciso-de-um-assessor declara o uso do ChatGPT numa
  lista. Sem recorte, só o-simples-funciona e o-portfolio-da-ivy-league; etf-o-que-e e tesouro-selic
  ficam fora da base; os demais entram sem a Conclusão e sem os trechos marcados
  (`pesquisa/epico-revisao-editorial/dados/d1-agregacao-pre-pipeline.md` §E).
- **Medidas.** `estilo/scripts/metricas.py`, `estilo/scripts/estratos.py`; extrações qualitativas em
  `estilo/extracoes/proprias/publicados/`, agregadas em `pesquisa/epico-revisao-editorial/dados/`.
