# Antipadrões — voz-syntaxis

O que cortar e como consertar. A lista vem de `estilo/estilo-autoral.md` §7 (v2.0.0), que é a
fonte; aqui ficam o par real e o conserto. "Pipeline" é o `post.md` aprovado; "autor" é o que
ele publicou depois (`estilo/corpus/edicoes/`, medida em
`pesquisa/epico-revisao-editorial/01-diagnostico.md`).

## O que o autor corta no site

| Antipadrão | Conserto | Par real (pipeline → autor) |
|---|---|---|
| Travessão acima do teto (~3 por mil palavras) | Vírgula para aposto, dois-pontos para anúncio, parêntese para glosa, ponto para separar | ❌ "captar recursos — via CDB, entre outros instrumentos — para financiar operações de crédito" → ✅ "captar recursos, via CDB, entre outros instrumentos para financiar operações de crédito" (o-papel-do-cdb) |
| Travessão em subtítulo, ou continuação "— e por que…" | Ponto e frase nova, ou cortar a continuação | ❌ "Não é favor, é 'spread' — e o risco que sobra nunca desaparece, só muda de endereço." → ✅ "Não é favor, é spread. E o risco que sobra nunca desaparece, só muda de endereço." (dividir-para-nao-correr-risco) |
| Parágrafo longo (acima de ~60 palavras) | Quebrar na virada; a frase que conclui vai sozinha | ❌ "A gravação aconteceu no meio de uma crise. A banda tinha acabado de trocar de empresário…" num bloco só → ✅ "A gravação aconteceu no meio de uma crise." ¶ "A banda tinha acabado de trocar de empresário…" (should-i-stay-or-should-i-go) |
| Aspas simples de ênfase | Itálico se for estrangeirismo ou expressão destacada; nada se a palavra se sustenta sozinha | ❌ "a primeira coisa que pergunto não é 'quanto rende'" → ✅ "a primeira coisa que pergunto não é *quanto rende*" (dividir-para-nao-correr-risco) |
| Rótulo de movimento em H2 | O H2 é a frase-tese da seção, sem o nome do movimento | ❌ "## Fechamento: sem rede" → ✅ "## Sem rede" (renda-fixa-condicoes-variaveis) |
| Dado da pesquisa que não serve ao argumento | Cortar; o dado fica em `03-pesquisa.md` para o autor | ❌ "Um levantamento sobre os dez principais corredores de cada temporada da NFL…" (99 palavras) → ✅ cortado (should-i-stay-or-should-i-go) |
| Resíduo do processo | Resolver antes do gate; nunca publicar | ❌ "[VERIFICAR: link da Notas de um Professor]" → ✅ cortado (coqueiros-e-cacaueiros). Publicados por engano: "[LINK: …]" (o-mundo-invertido-dos-investimentos), "vale checar na etapa de pesquisa do próximo post" (dividir-para-nao-correr-risco) |
| Exclamação no corpo | Frase curta no lugar | O pipeline atual já não produz; o checador confere |

## Tiques de IA — vigiar, com teto

Medidos contra o texto do próprio autor (`pesquisa/epico-revisao-editorial/dados/b2-antislop.json`).
Uma ocorrência isolada é voz; em série, é cadência mecânica.

- **Antítese "não é X. É Y."** — cerca de uma por seção, nunca duas seguidas, nunca fechando todo
  bloco (regra 20). A do refrão-tese conta.
- **Travessão seguido de complemento** ("— não…", "— a…", "— o…"): o autor corta metade.
- **Teaser ou metadiscurso de anúncio:** "O interessante começa agora", "Aqui mora…", "É aí que
  entra…". Corte e entre direto no ponto.
- **Fecho-síntese de fórmula:** "Dito direto:", "Se fosse para levar uma única ideia deste texto…".
- **Tríade e frase-golpe em série:** uma por bloco no máximo.

## Não é tique — não "corrigir"

- **Glosa entre parênteses** logo após o termo: o autor mantém de 85% a 100% das que o pipeline põe.
- **Negrito em frase-tese, termo-chave e nome ou obra.** Caso real: o rascunho de
  coqueiros-e-cacaueiros tinha os passos em negrito ("**1. Siga a demanda informal.**"); o pipeline
  tirou e o autor devolveu os seis no site.
- **Pergunta retórica que empurra o argumento.** O pipeline cortou perguntas em 10 de 13 posts; o
  autor repôs parte.
- **A lista genérica de tiques de IA em pt-BR** (`pesquisa/frente-d-antipadroes-ia-ptbr.md`) é
  referência de pesquisa, não checklist: o pipeline já tem taxa zero nesses tiques, e um item dela
  ("negrito espalhado") contradiz o uso real do autor se lido ao pé da letra.
