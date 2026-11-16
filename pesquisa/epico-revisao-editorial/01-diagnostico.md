# Fase B — Diagnóstico do pipeline

2026-11-15. Branch `epico/revisao-editorial-2026-11`. Esta fase é somente leitura: nenhuma skill,
nenhum agente e nenhuma regra do guia foi alterada.

Como reproduzir:

| Análise | Comando | Dados |
|---|---|---|
| B1 atribuição por etapa | `python3 scripts/diagnostico_edicoes.py atribuicao` | `dados/b1-atribuicao.json` |
| B2 antipadrões calibrados | `python3 scripts/diagnostico_edicoes.py antislop` | `dados/b2-antislop.json` |
| B3 deriva de estilo, B4 testes do guia | `python3 estilo/scripts/estratos.py` | `dados/b3-estratos.json` |

Tudo parte das triplas da Fase A (`00-corpus.md`). A única mudança no script da Fase A foi gravar
a posição de cada operação no `post.md` (`pos_antes`), necessária para a B1.

**Como a B1 atribui autoria.** Para cada token do `post.md` que serviu de base à publicação, a B1
reconstrói qual etapa o escreveu, seguindo a cadeia abaixo:
- **rascunho**;
- **etapa 4**, o último `04-draft-v*`;
- **etapas 6–9**, o `post.md` no commit da consolidação. Esse trecho vai para a etapa 6 ou para a 7 quando
  aparece no laudo dela, e para a 9 nos demais casos;
- **etapa 10**, o gate e o parecer.

Depois, a B1 mede quanto do texto de cada etapa sobrevive inteiro no site.

---

## Resumo: achados por severidade

| ID | Achado | Severidade | Métrica para a Fase E |
|---|---|---|---|
| D1 | A regra 4 vem de um artefato de conversão e é aplicada como norma obrigatória. O pipeline zera o negrito, e o autor o repõe | **alta** | negrito e aspas por mil palavras, `post.md` × site |
| D2 | O autor edita o texto do pipeline 3 a 4 vezes mais que o próprio texto; as etapas 9 e 10 são as piores por palavra | **alta** | similaridade e distância de edição `post.md`→site |
| D3 | Os parágrafos saem longos (45 palavras) e o autor os encurta para 34 em 13 de 13 posts com rascunho. Nenhuma etapa aponta isso | **alta** | palavras por parágrafo, % de parágrafos de uma frase |
| D4 | O travessão é o único tique de IA que a calibração confirma (3,6× o autor, sobrevive cerca de 50%). Ele não está na frente D, e a etapa 6 o defende | **alta** | travessão por mil palavras |
| D5 | `[VERIFICAR]` e `[PREENCHER]` passam pelo gate: 10 chegaram ao `post.md` aprovado, 2 foram publicados e 8 apagados sem resolução | **alta** | marcadores no `post.md` aprovado (meta: 0) |
| D6 | A lista genérica da frente D não pega nada que o pipeline escreva hoje | média | taxa da lista calibrada |
| D7 | O guia v1 está desatualizado além da regra 4: regras 7 e 9, uma terceira voz não prevista e itens de §8 | média | — (Fase D, onda 1) |
| D8 | O alt-text da etapa 8 não chega ao site: 1 legenda e 0 alt-texts em 48 imagens | média | legenda e alt-text publicados |
| D9 | Na 9a, os botões nativos aceitos não são colocados (0 de 5); CTA em texto e link chegam | média | fidelidade de CTA |
| D10 | O conteúdo que o pipeline traz da pesquisa é o mais cortado: 1.123 palavras de origem pipeline ou mista, contra 111 do rascunho | média | palavras de conteúdo do pipeline cortadas |
| D11 | O mesmo modelo escreve, critica, revisa e consolida (`model: inherit` nos 9 agentes); crítica e revisão não apontam o que o autor mais corrige | média | — (hipótese para a Fase E) |
| D12 | O pipeline tira perguntas (−31%) e todas as exclamações; o autor repõe parte das perguntas | baixa | perguntas por mil palavras |
| D13 | Título e subtítulo: o autor encurta 4 títulos e 8 subtítulos, corta o "— e por que…" e tira o rótulo "Fechamento:" dos H2 | baixa | — |
| D14 | Não existe etapa pós-publicação: o repositório e o site divergem, e a correção do FIDC não chegou ao site | baixa | — (frente "colheita" da Fase C) |

---

## Achados de severidade alta

### D1 — A regra 4 é aplicada como norma, e sua origem é um artefato

- **Origem.** As 6 amostras do guia v1 perderam o negrito e trocaram aspas duplas curvas por simples
  retas na conversão (`00-corpus.md` §5). Nos 31 posts do site, **27 usam negrito**. Os 4 que não
  usam são escolhendo-as-batalhas, objetivos-and-classes, 08-10 e 11-09.
- **Como o pipeline aplica a regra.** A legenda do `06-revisao.md` diz: "`norma`: erro objetivo, ou
  regra 1/regra 4 do guia, que são obrigatórias. Entra." Os laudos da etapa 6 citam a "regra 4" 78
  vezes e o "negrito" 69 vezes. Os picos são 23 menções a negrito em 09-01, 21 à regra 4 em 09-28 e
  17 à regra 4 em 10-30. A etapa 4, guiada por `voz-syntaxis`, já escreve sem negrito.
- **Efeito medido** (B3, média por post, nos 13 posts com rascunho de verdade):

  | | Rascunho | `post.md` | Site | Pré-pipeline |
  |---|---|---|---|---|
  | Negrito por mil palavras | 4,65 | **0,00** | 4,02 | 10,47 |
  | Aspas duplas por mil | 4,22 | 1,87 | 1,74 | 4,20 |
  | Aspas simples de ênfase por mil | 1,60 | 3,21 | 1,59 | 0,09 |
  | Itálico por mil | 3,17 | 4,74 | 5,78 | 2,09 |

- **Retrabalho.** O autor acrescentou 128 negritos.
  - 115 são novos.
  - 13 devolvem um negrito que estava no rascunho: 9 foram tirados na etapa 4 e 4 nas etapas 6–9.
  - Ele cortou 93 aspas simples.
- **Decisão.** Já foi tomada no GATE A: revogar a regra e medir.

### D2 — O texto do pipeline é o que o autor mais edita

Sobrevivência das palavras no site e taxa de edição de estilo, por etapa que escreveu o trecho (B1):

| Etapa que escreveu | Palavras na base | Sobrevivem no site | Edições por mil palavras | Sem divisão de parágrafo |
|---|---|---|---|---|
| rascunho (autor) | 27.787 | 95,7% | 9,8 | **5,5** |
| etapa 4 (draft) | 7.473 | 92,2% | 22,1 | 16,7 |
| etapa 6 (linha e norma) | 863 | 93,9% | 24,3 | 22,0 |
| etapa 7 (verificação) | 345 | 90,4% | 8,7 | 8,7 |
| etapa 9 (consolidação) | 3.169 | 89,0% | 24,6 | 19,9 |
| etapa 10 (gate e parecer) | 441 | **80,0%** | 43,1 | **36,3** |

- O autor mantém o próprio texto e edita o do pipeline numa taxa 3 a 4 vezes maior.
- As etapas 9 e 10 são as que mais geram retrabalho por palavra. São também as únicas que escrevem
  texto novo depois da crítica e da revisão, sem passar por elas.
- A etapa 7 é a exceção: o texto que a verificação corrige quase não é tocado.
- Este é o achado que a métrica principal da Fase E deve mover: a distância de edição `post.md`→site.

### D3 — Parágrafos longos que ninguém aponta

| | Rascunho | `post.md` | Site | Pré-pipeline |
|---|---|---|---|---|
| Palavras por parágrafo | 58,1 | 44,9 | **34,3** | 36,9 |
| % de parágrafos de uma frase | 34,7 | 29,9 | **43,9** | 36,4 |

- O autor encurta os parágrafos em 13 de 13 posts.
- **As 174 divisões de parágrafo da Fase A caem, em 115 casos, sobre parágrafos que vieram do próprio
  rascunho.** O parágrafo longo nasce no rascunho; o pipeline encurta um pouco e depois o autor
  divide na publicação. Mais 38 divisões caem sobre texto da etapa 4 e 15 sobre texto da etapa 9.
- Nos laudos de crítica e de revisão, "parágrafo longo" aparece 2 vezes no total.
- A etapa 6 lista "frases curtas em sequência" como voz a preservar, mas não trata a quebra de parágrafo.
  O alvo que o publicado mostra é cerca de 35 palavras por parágrafo, com perto de 45% de parágrafos de uma frase.

### D4 — O travessão é o tique que a calibração confirma

- **Taxa.** No texto escrito pelo pipeline, o travessão aparece 11,8 vezes por mil palavras. No texto
  só do autor, 3,3. É uma razão de 3,6× (B2).
- **Origem.** 63% dos travessões do `post.md` foram escritos pelo pipeline: 145 de 229.
- **Sobrevivência.** Os travessões do pipeline sobrevivem 50,5% (etapa 4), 57% (etapa 6) e 61% (etapa 9).
  Os do próprio rascunho sobrevivem 66,7%. As construções "— não", "— a" e "— o" sobrevivem de 43% a 58%.
- **Total.** No site ficam 3,89 travessões por mil palavras, menos que no rascunho (4,88).
- **O revisor defende a forma.** O laudo da etapa 6 de 10-27 diz: "Pela norma, o '—,' está correto". Os laudos
  quase não discutem o uso: são 15 menções em 16 posts.
- **A frente D não lista o travessão.** É o maior sinal real, e a referência de antipadrões não o cobre.

### D5 — Pendências passam pelo gate

- A etapa 7 marcou 146 `[VERIFICAR]` nos 16 posts. Isso é a verificação funcionando.
- **10 marcadores chegaram ao `post.md` aprovado no gate**: 9 `[VERIFICAR]` e 1 `[PREENCHER: memória do autor…]`, em 10-30.
- No site, o autor apagou 8 sem resolver. Exemplos:
  - "[VERIFICAR: atribuição a Peter Kempthorne…]";
  - "[VERIFICAR: link da Notas de um Professor]".
- **Dois estão publicados.** Um está em *A Corda e o Arco* (taxa over); o outro em *Frequência de Capitalização*
  (ano da edição de Maor).
- A regra "Zero `[VERIFICAR]` sem review humano" (`revisao-editorial`, item 3) só garante que o
  marcador fique *visível*. Nenhuma checagem impede que o post seja aprovado com ele. É o caso típico de
  regra determinística entregue a um LLM.

---

## Achados de severidade média

### D6 — A lista genérica de antipadrões não pega nada

O B2 compara 12.291 palavras escritas pelo pipeline com 51.711 só do autor: rascunhos, posts
pré-pipeline e acréscimos autorais. As taxas são por mil palavras.

| Sonda (frente D) | Pipeline | Autor | Site (era pipeline) |
|---|---|---|---|
| abertura clichê, hedging, fecho genérico, passiva analítica, analogia genérica, pergunta-muleta | **0,00** | 0,00–0,12 | 0,00–0,03 |
| conectivo formal ("além disso", "portanto"…) | 0,16 | 0,19 | 0,08 |
| adjetivo vazio ("fundamental", "essencial"…) | 0,00 | 0,46 | 0,15 |
| tríade "x, y e z" | 0,41 | 1,18 | 0,77 |
| léxico de IA ("cenário", "panorama", "moldar"…) | 0,24 | 0,14 | 0,18 |
| "não é x, é y" | 0,81 | 0,83 | 1,05 |
| **travessão** | **11,8** | 3,29 | 3,23 |
| **aspas simples de ênfase** | **3,42** | 0,77 | 1,51 |
| "ou seja / isto é" | 0,33 | 0,14 | 0,18 |
| "é justamente/exatamente" | 0,33 | 0,15 | 0,31 |

- O pipeline já suprime os tiques genéricos. Em vários deles o autor tem taxa maior, o que significa
  que a lista tem custo e nenhum retorno.
- Um item da lista ("negrito espalhado em quase todo substantivo") conflita com a prática medida do autor.
- **Excesso não basta para ser tique.** A lista de n-gramas sobre-representados, com controle de tema
  (pipeline contra os rascunhos dos mesmos posts), é dominada por glosa entre parênteses: "(Certificado de
  Depósito Bancário)", "(Letra de Crédito do Agronegócio)", "(Conselho Monetário Nacional)". Essa
  glosa sobrevive de 85% a 100% no site, porque é a regra 1 funcionando.
- **A lista calibrada** (razão ≥ 3, presença em ≥ 4 posts e menos de 70% sobrevivendo no site) tem só as
  construções com travessão ("— não", "— a", "— o") e três expressões de tema de um post só.
  - "Ou seja" e "é justamente" ficam acima do autor, mas em número pequeno e sem corte. Não entram.

### D7 — O guia v1 contra os 31 posts (B4)

| Regra (guia v1) | Veredito | Evidência |
|---|---|---|
| 1. Jargão sempre glosado na 1ª ocorrência | **confirmada, mais forte na era pipeline** | Siglas glosadas: pré-pipeline 29%, rascunho 19%, `post.md` 48%, site 52%. Glosas sobrevivem de 85% a 100% |
| 2. Exemplo depois do conceito | não testável por métrica | fica para a extração qualitativa da Fase D |
| 3. Dois-pontos como articulador | confirmada | 14,3 por mil no site, 10,9 no pré-pipeline; o autor não corta |
| **4. Nunca negrito/itálico; aspas simples** | **contradita** | D1. Revogação decidida no GATE A |
| 5. Subtítulos H2, sempre | confirmada (30 de 31) | só comece-com-o-simples (2024) não tem subtítulo |
| 6. Autoridade por estudo nomeado (autor, ano) | **condicionada à época** | Citação autor-ano em 2 de 15 posts pré-pipeline e em 10 de 16 da era pipeline. O pipeline acrescenta (0,72 → 0,97 por mil) e o autor corta parte (0,71) |
| 7. Aposto e parêntese, "frequentemente com travessão duplo" | **parcialmente contradita** | o parêntese fica (≈10 por mil, sobrevive); o travessão é o que o autor mais corta (D4) |
| 8. Instituição citada pelo nome | confirmada | 9 de 16 posts da era pipeline e 8 de 15 pré-pipeline citam CVM, BC, B3, Copom, CMN ou FGC |
| 9. Visual tratado como parte do argumento, com referência verbal | **sem suporte** | referência verbal ("gráfico abaixo", "veja o diagrama") aparece 0,00–0,03 vez por mil em todos os estratos. Os posts têm em média 3,1 imagens no site, quase sempre sem legenda (D8) |
| §4 Duas vozes (ensaística e explicativa) | **incompleta** | Desde 10-30, os briefings da linha Notas declaram "**ensaística em registro técnico**" (10-30, 11-02, 11-09), uma terceira voz não prevista. A "explicativa" aparece só em 4 posts (08-14, 09-18, 09-28, 10-15). No site, a explicativa tem 0,35 "eu" por mil, nenhum CTA e o maior uso de negrito (6,36 por mil) |
| §7.1 "Nunca tabela ou gráfico nativo" | reformular | O Substack não tem tabela; as 6 tabelas do `post.md` viraram imagem ou sumiram. É restrição da plataforma, não traço de voz |
| §8 Reticências | não promover | 0,34 por mil no pré-pipeline, 0,07 na era pipeline |
| §8 LinkedIn | sem amostra | continua aberto |

O guia v1 também não registra três traços medidos que são estáveis no publicado:
- o parágrafo curto (D3);
- a pergunta como ferramenta (2,5 por mil no site e 4,8 no pré-pipeline);
- o itálico para estrangeirismo (5,8 por mil no site, adicionado pelo autor).

### D8 — O alt-text da etapa 8 não chega ao site

- Os 16 `post.md` têm 29 marcadores `graf`/`diag` com alt-text descritivo.
- No site há 48 imagens: as figuras mais a capa e a ilustração, que hoje vêm de fora do pipeline.
- Dessas 48, **1 tem legenda e nenhuma tem alt-text.**

O texto que a etapa 8 escreve para "sustentar o post se a imagem falhar ao carregar" (`prompts-visuais`)
se perde na colagem manual. Com isso, as 28 operações de "legenda" da Fase A são perda, não reescrita.

### D9 — Parecer de marketing: o texto chega, os botões não

| Post | Itens aceitos (`estado.json`) | O que está no site |
|---|---|---|
| 11-02 | — (o parecer é anterior ao registro de aceitos) | 0 botão, 0 link interno do parecer |
| 11-09 | C1–C4, B1 | C2 (CTA em texto do Skill Check) ✓. C1, C3 e C4 (botões nativos) ✗ |
| 11-13 | C1, C4, R1, B2, B3 | R1 (link para borboletas) ✓. C1 e C4 (botões de inscrição) ✗. O autor pôs "Compartilhar" (2) e "Deixe um comentário" (2) |

Os itens que o `parecer.py aplicar` insere no texto chegam ao site (2 de 2). Os botões nativos
dependem de uma lista de inserção manual e não foram colocados como recomendado (0 de 5). O autor
coloca botões por conta própria (8 botões em 5 posts da era pipeline, quase sempre de compartilhar
ou comentar). Ou a recomendação de botão não reflete o que ele quer, ou a lista manual não funciona.
É uma pergunta para a Fase C.

### D10 — O conteúdo que vem da pesquisa é o mais cortado

A Fase A achou 35 cortes de conteúdo ou fato. **23 deles são de texto escrito pelo pipeline ou misto,
somando 1.123 palavras.** Do rascunho foram 12 cortes, com 111 palavras. Os maiores:
- 99 palavras de um levantamento da NFL (11-13);
- 60 palavras da taxa média da LCA, citando Quantum Finance e InfoMoney (09-18);
- notas de rigor;
- referências.

O pipeline traz da etapa 3 dado que o autor não quer no texto final. O agente da etapa 3 é instruído
a sustentar "cada afirmação que a estrutura promete provar", mas não a julgar se o dado cabe no texto.

### D11 — Autoviés: hipótese coerente, ainda não testada

- Os 9 agentes têm `model: inherit`. O mesmo modelo escreve (4), critica (5), revisa (6) e consolida (9).
- O que os dados mostram:
  - as três edições mais frequentes do autor (parágrafo, negrito e travessão) quase não aparecem nos laudos de
    crítica e de revisão;
  - quando aparecem, a revisão defende a forma do pipeline (D1, D4);
  - a consolidação escreve texto novo depois da revisão, e esse texto sobrevive menos (D2);
  - o `09-consolidacao.md` de 10-27 registra itens `linha` "aplicados pelo orquestrador; o gate pode reverter".
- Isso é coerente com a literatura de autoviés (Seção 4 do prompt do épico). Mas não há aqui um
  experimento que isole a variável modelo. O teste certo é o da Fase E: o juiz pareado de outra família
  contra o mesmo juiz, e a crítica com e sem exemplos reais das edições do autor.

---

## Achados de severidade baixa

- **D12 — Perguntas e exclamações.**
  - Perguntas por mil palavras: rascunho 3,29, `post.md` 2,27 (o pipeline tira em 10 de 13 posts), site 2,49. O autor repõe parte em 7 de 13.
  - Exclamações: 0,22 → 0,00 → 0,05. No pré-pipeline eram 4,8 perguntas e 0,98 exclamações.
  - É sinal fraco, mas consistente.
- **D13 — Manchetes.**
  - O autor trocou 4 títulos e 8 subtítulos, sempre encurtando.
  - Corta a continuação depois do travessão em 4 subtítulos ("… é esperado — e por que entender isso…" → "… é esperado.").
  - Tira o rótulo "Fechamento:" de H2 em 09-28, 10-15 e 11-02.
- **D14 — Repositório e site divergem depois da publicação.**
  - 09-01 foi regerado do zero um dia depois de publicado.
  - A correção do FIDC em 10-30 e 11-02 ficou só no repositório.
  - Hoje nada no processo puxa o site de volta. A colheita pós-publicação (frente 2 da Fase C) resolve as duas coisas.
- **Frase média.**
  - Sobe de 13,8 palavras (rascunho) para 17,9 (`post.md`) e fica em 17,5 no site; o pré-pipeline tem 18,4.
  - Os rascunhos têm fragmentos e marcadores que encurtam a média. Sem achado.

---

## O que está funcionando e não deve ser mexido

- **Regra 1 (glosa).** A etapa 4 sobe a glosa de siglas de 19% para 48%, e o autor mantém (52% no site).
  A glosa entre parênteses sobrevive de 85% a 100%. É o excesso que o autor quer.
- **Verificação (etapa 7).** É a etapa cujo texto o autor menos edita (8,7 edições por mil palavras), e
  ela levantou 146 pendências. O problema de D5 está no gate, não na verificação.
- **Supressão dos tiques genéricos de IA.** O pipeline tem taxa praticamente zero em todos os grupos da frente D.
- **Estrutura e argumento.** A similaridade `post.md`→site tem mediana de 0,964, e as edições de
  conteúdo são 50 de 923. O autor não reestrutura o que a crítica (5) e o gate deixaram passar.
- **Rascunho como entrada.** Nos posts com rascunho de verdade, 95,7% das palavras do autor chegam ao
  site. O pipeline não reescreve a voz dele.
- **Gate 5a (bloqueante do quant).** Nenhuma evidência de problema nos dados desta fase.

## Limites

- A atribuição B1 depende do histórico do git. Onde a consolidação não tem commit próprio, o rótulo
  vira um intervalo ("etapas 6–10"); não houve casos assim. A separação entre 6, 7 e 9 é por busca do trecho no
  laudo da etapa, então é provável, não certa.
- Nas transcrições (08-10, 08-14, 08-17), quase todo o texto é "etapa 4". Elas entram na sobrevivência e
  na B2, mas não na direção da B3.
- A contagem de primeira pessoa não pega o sujeito oculto ("Voltei de viagem"). A métrica "abre em
  primeira pessoa" foi descartada por isso.
- Nenhum achado aqui isola a variável modelo (D11). Isso é trabalho da Fase E.

## Decisões do GATE B (2026-11-15)

1. **Laudo aprovado.** Sigo para a Fase C.
2. **D9, botões da 9a.** O autor não quer botão de inscrição nos pontos que o parecer sugeriu. O
   problema é a recomendação, não a lista manual. A Fase C ajusta a 9a para propor compartilhar ou
   comentar, ou nenhum botão.
