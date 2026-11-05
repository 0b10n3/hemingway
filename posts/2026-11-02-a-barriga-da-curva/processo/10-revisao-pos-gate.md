# Rodada pós-gate — versão do autor (2026-11-05)

O autor editou o texto na Substack depois da aprovação e pediu mais uma revisão, com gancho novo.
Revisão na sessão principal, sem subagentes. Diff por frase contra o `post.md` aprovado: nenhum
número, fórmula ou fonte mudou. Recalculados: abertura, prazo quebrado, conversão 91 dc/63 du,
12,68% e os números do gancho. Fontes não reconsultadas (citações inalteradas desde a etapa 7).

## Mudanças do autor mantidas

Título "A Corda e o Arco"; abertura reescrita; quebras de parágrafo; saída de FIDC, da pergunta que
fechava a abertura, da definição de "barriga" e das citações de artigo da taxa legal.

## Correções aplicadas por decisão do autor

- "barriga" sem definição (2 ocorrências): trocada.
- "arco" sem definição: nomeado no parágrafo da corda.
- graf-01: anotação "a barriga:" → "entre a corda e o arco,"; PNG e SVG regenerados.
- "ínicio"; "2026/09/07" solto no fim; interface da Substack na colagem.
- Abertura: "2026 tem 249 dias úteis"; "dias úteis"; "essa contagem".
- "Aqui podemos destacar algumas ideias" → "Aqui está a ideia".
- "O texto manda" → "A norma manda". Intertítulo em caixa de frase.

## Gancho

Decisões do autor: "motor contínuo" e aviso do adiamento do FIDC. Fatiar os mesmos 14% converge para
e^(0,14t), 15,03%, e não para 1,14^t, que é o "regime exponencial" deste post. Números: 14,49%
(m = 2), 14,93% (m = 12), limite 15,03%. Ajuste depois da decisão: "depois dele" → "depois desse
texto", porque "dele" podia remeter ao motor contínuo.

## V-1: over × 30 (resolvido por reescrita)

O autor delegou a decisão. Nova busca em 2026-11-05 (web e API de normativos do BCB):

- A convenção existe, sem data: "taxa de juros de um dia útil, multiplicada por 30 (convenção de
  mercado…)", página sem autor nem data em bertolo.pro.br, com "Ver ASSAF p. 168"; Bússola do
  Investidor diz o mesmo. Fontes secundárias. O exemplar do Assaf Neto não foi conferido.
- Nenhuma fonte diz que a Selic era cotada assim antes de 1998. Nada nos normativos do BCB.
- Garcia (1997), a única fonte de época, confirma as taxas "mensalizadas", mas usa 1,66% ao mês como
  taxa que se compõe (1,0166^12 = 21,84% a.a.). Na mesma taxa diária, × 30 daria 2,35%. É uma taxa a
  termo, então não refuta a over × 30, mas também não sustenta "saiu uma nominal".

Reescrita: a convenção fica como afirmação geral; 1998 passa a ser "cotação ao mês → efetiva ao ano"
(Garcia + Circular 2.761). Mudam a marca e quatro frases ("A virada de 1998" e fechamento). A
pedagogia nominal × efetiva fica no texto. Para voltar à versão anterior: reverter este commit.

## Pendente

Reaprovação no gate pelo autor.
