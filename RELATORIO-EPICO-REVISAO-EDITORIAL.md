# Relatório — épico de revisão e aperfeiçoamento do pipeline

2026-11-15 a 2026-11-16. Prompt: `../../PROMPT_CLAUDE_CODE_EPICO_HEMINGWAY_2026-11.md` (raiz
`Syntaxis/`). Laudos em `pesquisa/epico-revisao-editorial/`. Branch `epico/revisao-editorial-2026-11`,
mergeada em `main` ao fim desta rodada (sem push).

## Em uma frase

O site mostrou que o pipeline escrevia contra a voz real do autor, por causa de uma regra nascida
de um erro de conversão. O épico capturou o texto publicado, mediu o que o autor desfaz e refez o
guia (v2.0.0) e as etapas para escrever na direção em que ele edita. Agora o processo volta ao
site a cada post.

## Fases

| Fase | Entrega | Laudo |
|---|---|---|
| A — corpus | 31 posts capturados (`_arquivo/publicados/`), normalizados (`estilo/corpus/publicados/`), 16 triplas rascunho → `post.md` → site com 923 edições classificadas | `00-corpus.md` |
| B — diagnóstico | 14 achados (5 altos), guia v1 contra os 31 posts, antipadrões calibrados, deriva de estilo | `01-diagnostico.md` |
| C — proposta | 15 itens em 4 ondas; 14 aprovados (P15 LanguageTool recusado) | `02-proposta.md` |
| D — implementação | 4 ondas, cada uma com gate; guia `voz-v2.0.0` | `02-proposta.md`, "Registro da Fase D" |
| E — avaliação | protocolo e script; vazamento declarado; medida limpa é prospectiva | `03-avaliacao.md` |
| F — fechamento | docs, este relatório, merge em `main` | — |

## Achados que mudaram o sistema

1. **A regra 4 era artefato.** As amostras da v1 perderam o negrito e trocaram aspas duplas por
   simples na conversão. O pipeline aplicava "nunca negrito" como norma obrigatória: 3 negritos em
   16 `post.md`, 144 no site. A regra foi revogada (GATE A e onda 1).
2. **O autor edita o texto do pipeline 3 a 4 vezes mais que o próprio**, e mais ainda o texto
   escrito nas etapas 9 e 10 (sobrevivem 89% e 80%). A consolidação passou a aplicar sem escrever.
3. **Forma é onde está o retrabalho.**
   - Parágrafo: 45 → 34 palavras.
   - Travessão: o autor corta 46%. É o único tique de IA que a calibração confirma, e não constava
     da lista de antipadrões.
   - Rótulo "Fechamento:" em H2.
4. **Pendências passavam pelo gate.** Quatro resíduos do processo estavam no ar. Agora há uma
   checagem determinística e um gate que bloqueia.
5. **A lista genérica de tiques de IA não pegava nada**, porque o pipeline já não os produz. Ela
   foi trocada por uma lista calibrada pelas edições do autor.
6. **Uma terceira voz** (ensaística em registro técnico) existia desde janeiro de 2026 e virou o
   padrão da linha Notas.

## O que existe agora

- Guia de voz v2.0.0: `estilo/estilo-autoral.md`, `voz.fingerprint.json`, `CHANGELOG.md`.
- Registro gerado das edições do autor: `estilo/preferencias-de-edicao.md`.
- Scripts, todos com teste (59 testes, todos passam):
  - `checar_post.py`: checagem mecânica;
  - `corpus_publicado.py` e `diff_edicoes.py`: colheita e triplas;
  - `diagnostico_edicoes.py`, `estilo/scripts/estratos.py` e `avaliar.py`: medida.
- Colheita pós-publicação: `/forja-de-voz colher <slug>`.
- Fontes únicas novas: `docs/AVISO_LEGAL.md` e `estilo/corpus/mapa-publicados.json`.

## Commits principais

Fase A: `2ddeea5`, `b33a857`, `51881b5`, `17cce4a`, `06765a3`. Fase B: `6c162cb`, `195cf43`,
`f2f4104`, `a399245`. Fase C: `06e7935`. Onda 1: `c53b1d9`, `6a97222`, `aeefb64` (tag
`voz-v2.0.0`), `447a41f`, `94b42de`, `6445440`, `dab3f12`. Onda 2: `82357ac`, `8f23211`, `29e8809`.
Onda 3: `3309ec2`, `b24750c`. Onda 4: `c2e5386`, `8c5aa15`, `4d111a0`, `13bc49b`. Fase E: `08ff227`,
`4ef6307`. Registros: `c167142`, `c73b250`, `347d51b`, `b940d87`.

## Pendências

**No site (correção manual do autor no Substack):**
- dois `[VERIFICAR]` publicados: *A Corda e o Arco* (taxa over) e *Frequência de Capitalização*
  (ano da edição de Maor);
- um `[LINK: …]` publicado: *O Mundo Invertido dos Investimentos*;
- jargão do pipeline publicado: *Dividir para não correr risco* ("vale checar na etapa de pesquisa
  do próximo post");
- promessa do texto sobre FIDC, cancelado: *Você está contando os dias errado*;
- erros de digitação:
  - "Ficarprocrastinando" e "conteto" (09-11);
  - "crédito rura." (09-18);
  - "O coqueiro o símbolo" (10-12);
  - "um calculo" (10-15);
  - "No munda das opções" (11-09);
- palavra "composto" partida entre parágrafos (*A Corda e o Arco*) e parágrafo só com "."
  (*Should I stay*).

**No repositório:**
- os `post.md` atuais de 10-30 (`[PREENCHER]`) e 11-09 (`[VERIFICAR]`) ainda trazem marcadores; o
  `checar_post.py` os acusa;
- `[VERIFICAR]` de 11-02 está só no site (ver acima).

**Fase E:**
- prospectiva: decisão depois de 3 posts publicados com o pipeline novo (`python3 scripts/avaliar.py
  prospectivo` depois de cada colheita);
- retrospectiva: uma sessão nova dentro do repositório, roteiro em `03-avaliacao.md` §3.B.

**Backlog fora do escopo:**
- LanguageTool (recusado no GATE C; a colheita usa só a heurística de suspeita);
- embedding de estilo (só se a Fase E ficar inconclusiva);
- `README.md` e outros docs voltam a ser revistos depois da decisão da Fase E;
- a fronteira entre registro técnico e explicativa ainda é difusa (teste cego da v2.0.0).

## Próxima colheita

No próximo post publicado: `/forja-de-voz colher <slug>`, e depois
`python3 scripts/avaliar.py prospectivo`. A revisão de regras do guia (`/forja-de-voz atualizar`)
fica para depois do terceiro post colhido, junto da decisão da Fase E.
