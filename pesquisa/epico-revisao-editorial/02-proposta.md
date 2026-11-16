# Fase C — Proposta e backlog

2026-11-15. Cada item nasce de um achado de `01-diagnostico.md` (D1–D14) e diz que métrica da Fase
E deve mover. Os itens estão agrupados em quatro ondas, na ordem em que dependem uns dos outros, e
são aprovados um a um no GATE C. As mudanças em regra do guia (P1) têm uma segunda aprovação, regra
por regra, durante a Fase D, como manda o protocolo da forja.

**Riscos.**
- Baixo: documentação ou script novo isolado.
- Médio: muda o comportamento de um agente ou skill.
- Item a item: estilo ou posts.

**Princípio.** Prefiro apagar a acrescentar, e prefiro script a instrução para o modelo. Nenhum item
cria etapa nova no pipeline. P10 é um modo novo de skill existente, e P4 é um script chamado por
etapas que já existem.

## Ordem por impacto ÷ esforço

| # | Item | Achados | Impacto | Esforço |
|---|---|---|---|---|
| 1 | P3 revisor da etapa 6 sem a regra 4, com foco em parágrafo e travessão | D1, D3, D4 | alto | baixo |
| 2 | P4 + P5 checagem determinística e gate sem pendência | D5 | alto | baixo-médio |
| 3 | P1 guia v2.0.0 | D1, D3, D4, D7 | alto | alto |
| 4 | P2 antipadrões e exemplos recalibrados | D4, D6 | médio-alto | baixo |
| 5 | P6 consolidação e gate sem prosa nova fora do filtro | D2 | médio-alto | baixo |
| 6 | P12 botões da 9a | D9 | médio | baixo |
| 7 | P10 colheita pós-publicação | D14, D5 | alto (contínuo) | médio |
| 8 | P7 registro de preferências de edição | D2, D11 | médio | médio |
| 9 | P8 crítica e pesquisa com critério de pertinência | D10, D11 | médio | baixo |
| 10 | P11 alt-text e legenda para colar | D8 | médio (acessibilidade) | baixo |
| 11 | P13 aviso legal como fonte única | Fase A | baixo | baixo |
| 12 | P14 cortes em checklist e referências | D6, D13 | baixo | baixo |
| 13 | P9 experimento de autoviés | D11 | incerto | médio |
| 14 | P15 LanguageTool local | Fase A §6 | baixo-médio | médio (dependência) |

---

## Onda 1 — Voz (a origem do maior retrabalho)

### P1 — Guia de voz v2.0.0, a partir dos 31 posts e das edições

- **Achados:** D1, D3, D4, D7. Decisão do GATE A sobre a regra 4.
- **Mudança.** Seguir `forja-de-voz/references/protocolo-de-atualizacao.md` na branch `voz/2.0.0`, com três ajustes:
  - **Corpus.** Os 31 publicados entram, com peso por época: os 16 da era pipeline são a voz atual e os
    15 anteriores são a linha de base. `metricas.py` passa a ler também `estilo/corpus/publicados/`.
  - **Extração.** O `extrator-de-estilo` roda nos 25 posts publicados que ainda não têm extração. As 6
    amostras antigas não são reprocessadas: a extração delas é substituída pela do texto do site, porque
    a amostra perdeu formatação, e isso fica registrado.
  - **Evidência.** Reversão ou acréscimo autoral que se repete em 3 ou mais posts conta como "evolução
    deliberada". Contradição com regra vigente vira pergunta.
- **Arquivos:** `estilo/estilo-autoral.md`, `voz.fingerprint.json`, `corpus-manifest.json`, `metricas.json`,
  `CHANGELOG.md`, `extracoes/proprias/*.json`, `estilo/scripts/metricas.py`.
- **Propostas de regra.** Cada uma será aprovada separadamente na Fase D:

| Regra (v1) | Proposta (v2) | Evidência |
|---|---|---|
| 4. Nunca negrito/itálico; aspas simples | **Revogada.** Nova regra de ênfase: negrito em nome e obra na primeira menção, definição-chave e frase-tese (≈4 por mil palavras); itálico em estrangeirismo e título de obra; aspas duplas curvas para citação e termo; aspas simples só dentro de aspas duplas | D1; GATE A |
| 7. Aposto "frequentemente com travessão duplo" | Glosa e aposto entre parênteses logo após o termo. Travessão com parcimônia (≈4 por mil palavras), nunca em título ou subtítulo | D4 |
| 9. Visual com referência verbal | **Revogada no guia.** Legenda e alt-text são regra do pipeline (`prompts-visuais`), não traço de voz | D7, D8 |
| §7.1 "Nunca tabela ou gráfico nativo" | Sai do guia. É restrição da plataforma e vai para `prompts-visuais` (tabela vira figura) | D7 |
| — | **Nova: parágrafo curto.** Média de cerca de 35 palavras, perto de 45% de parágrafos de uma frase; frase isolada como ênfase | D3 |
| — | **Nova: pergunta como ferramenta.** O pipeline não corta pergunta retórica que empurra o argumento | D12 |
| 6. Autoridade por estudo nomeado | Mantida, condicionada: forte na era pipeline (10 de 16 posts). O pipeline não acumula citação que o argumento não pede | D7 |
| §4. Duas vozes | Terceira voz candidata: **ensaística em registro técnico** (linha Notas, desde 10-30). Entra só se a extração da Fase D sustentar com ≥ 2 posts | D7 |
| §8 | Reticências saem da observação (em queda). "Ironia contra a indústria" e "analogia com a matemática" são testadas na extração | D7 |
| `confianca_global` | Reavaliar: o corpus passa de 7 para 31 textos, cerca de 60 mil palavras, acima do piso de `taxonomia-estilometrica.md` | — |

- **Risco:** item a item (estilo). É major, porque revoga regra.
- **Métrica (Fase E):** todas as de forma: negrito, aspas, travessão, parágrafo e perguntas por mil palavras no `post.md`, contra o publicado.
- **Dependência:** nenhuma.

### P2 — Antipadrões e exemplos recalibrados pelo autor

- **Achados:** D4, D6.
- **Mudança:**
  - `voz-syntaxis/references/antipadroes.md` é reescrito a partir de `dados/b2-antislop.json`:
    - **O que cortar:** travessão acima do orçamento e construções "— não / — a / — o"; aspas simples de
      ênfase (troca por itálico ou aspas duplas).
    - **O que não é tique e não deve ser "corrigido":** glosa entre parênteses, negrito em nome e
      definição, pergunta retórica com função.
  - A frente D (`pesquisa/frente-d-antipadroes-ia-ptbr.md`) fica como referência de pesquisa. Nenhuma etapa
    a lê inteira por padrão: o pipeline já tem taxa zero nesses tiques.
  - `voz-syntaxis/references/exemplos-pareados.md`:
    - o par da regra 4 é invertido;
    - entram 6 pares reais pipeline → autor, tirados das triplas: parágrafo, travessão, negrito,
      subtítulo, aspas e corte de dado.
- **Antes → depois (exemplo):** a linha "Negrito ou itálico de ênfase | Confirmado em 5/6 posts de Substack
  como ausência total…" vira "Negrito em nome, obra, definição e frase-tese é voz (27 de 31 posts); negrito
  espalhado em todo substantivo não é".
- **Risco:** médio.
- **Métrica:** travessão e aspas simples por mil palavras no `post.md`; operações de pontuação e de aspas no site.

### P3 — Revisor da etapa 6: sem a regra 4, com foco em parágrafo e travessão

- **Achados:** D1, D3, D4, D12.
- **Mudança em `.claude/agents/revisor-gramatical.md`:**
  - **Sai:** "Ausência sistemática de negrito/itálico de ênfase — voz, não lacuna a preencher."
  - **Entra** (depende de P1):
    - o negrito e o itálico do autor se preservam;
    - itálico em estrangeirismo é `norma` (Manual do Senado, já citado em `frente-c`).
  - **Classificação.** `norma` fica restrita a norma culta e à regra 1 (glosa). Escolha de estilo nunca é `norma`.
  - **Focos novos de `linha`:**
    - parágrafo acima de cerca de 60 palavras: propor quebra;
    - travessão acima do orçamento ou em subtítulo: propor vírgula, dois-pontos ou ponto;
    - pergunta retórica com função argumentativa: não sai.
- **Risco:** médio.
- **Métrica:** palavras por parágrafo e travessão por mil no `post.md`; divisões de parágrafo e cortes de
  travessão feitos pelo autor no site (174 e 37 hoje).

## Onda 2 — Gate e checagens determinísticas

### P4 — `scripts/checar_post.py`, com teste

- **Achados:** D5, D3, D4, D13.
- **Mudança.** Script stdlib que lê um `post.md`, ou o `.md` publicado, e devolve:
  - **Bloqueante:**
    - `[VERIFICAR`, `[FAIXA` ou `[PREENCHER` no texto;
    - placeholder órfão entre `post.md` e `graficos.md`/`diagramas.md`/`infograficos.md`, nos dois sentidos;
    - frontmatter mínimo ausente (titulo, subtitulo, data, linha_editorial, status).
  - **Aviso** (não bloqueia):
    - travessão acima do orçamento;
    - parágrafo médio acima de 40 palavras, ou algum parágrafo acima de 90;
    - H2 com rótulo de movimento ("Fechamento:", "Movimento N");
    - aspas simples de ênfase;
    - código Plotly sem `rangemode="tozero"`, sem exceção justificada no spec.
- **Risco:** baixo (script novo).
- **Métrica:** marcadores no `post.md` aprovado (10 hoje; meta 0).

### P5 — Etapas 9 e 10: o gate não aprova com pendência

- **Achado:** D5.
- **Mudança em `post-substack/SKILL.md`:**
  - A etapa 9 roda `checar_post.py` depois do `revisao-editorial`.
  - Na etapa 10, "Aprovar" só aparece com zero bloqueante. Cada marcador vira uma pergunta nomeada:
    resolver, cortar o trecho ou reescrever sem o dado.
  - **Antes:** "Se algum `[VERIFICAR]` ou `[FAIXA]` ficou pendente, liste cada um e pergunte se o autor
    publica assim mesmo."
  - **Depois:** "Nenhum `[VERIFICAR]`, `[FAIXA]` ou `[PREENCHER]` chega a um post aprovado: cada um vira
    pergunta nomeada antes do `AskUserQuestion` de aprovação."
- **Mudança em `revisao-editorial.md`:** os itens 3, 4, 6, 9 e 11 do checklist passam a ser "rodar
  `checar_post.py` e tratar a saída". O LLM deixa de reler mecanicamente o que o script confere.
- **Risco:** médio.
- **Métrica:** marcadores no `post.md` aprovado e no site (meta 0).

### P6 — Consolidação e gate não escrevem prosa nova fora do filtro

- **Achado:** D2. O texto da etapa 9 sobrevive 89% e o da etapa 10, 80%.
- **Mudança em `post-substack/SKILL.md` e `revisao-editorial.md`:**
  - A etapa 9 aplica só `norma`, mais as `linha` que o autor marcou como aceitas.
  - **Sai** a prática registrada em 10-27: "Aplicadas pelo orquestrador; o gate pode reverter".
  - A redação nova da etapa 10 (itens A/X do parecer, ajustes do gate) passa pelas referências de
    `voz-syntaxis` e por `checar_post.py` antes de ser mostrada.
- **Risco:** médio.
- **Métrica:** sobrevivência no site das palavras escritas nas etapas 9 e 10 (89% e 80%; meta ≥ 92%).

### P14 — Cortes em checklist e referências

- **Achados:** D6, D13.
- **Mudança:**
  - **(a)** `revisao-editorial` item 7 (fórmula de manchete) sai, assim como a seção correspondente de
    `tecnicas-narrativas.md`. O autor encurta títulos (4 de 16) e nenhum adotou a fórmula.
  - **(b)** `revisao-editorial` item 5 deixa de ler a frente D inteira e lê só `antipadroes.md` (P2).
  - **(c)** `docs/BACKWARDS_DESIGN.md` §3 ganha uma linha: o nome do movimento ("O Fechamento do Loop") é
    instrução de forma e não vira rótulo de H2.
- **Risco:** baixo.
- **Métrica:** H2 com rótulo de movimento (3 posts hoje; meta 0).

## Onda 3 — Conteúdo, crítica e preferências

### P7 — Registro de preferências de edição (estilo CIPHER)

- **Achados:** D2, D11.
- **Mudança:**
  - Um modo novo, `python3 scripts/diff_edicoes.py preferencias`, gera `estilo/preferencias-de-edicao.md`
    a partir de `estilo/corpus/edicoes/`. O registro diz o que o autor desfaz e o que acrescenta, por
    classe, por voz e por linha, com contagem e 2 exemplos de cada.
  - As etapas 4, 6 e 9 leem o registro antes de escrever ou revisar.
  - O registro é dado medido, não regra. Regra só nasce dele via forja (P1, P10).
- **Risco:** médio.
- **Métrica:** distância de edição `post.md`→site; reversões que se repetiriam.

### P8 — Crítica e pesquisa com critério de pertinência

- **Achados:** D10, D11.
- **Mudança:**
  - **`pesquisador-editorial`:** cada dado sai marcado `entra no texto` ou `contexto para o autor`. A etapa
    4 integra só os `entra`; o resto fica em `03-pesquisa.md`.
  - **`critico-editorial`:** ganha uma pergunta nova: "Que dado ou trecho trazido pela pesquisa não serve
    ao argumento?". Recebe 3 exemplos reais de corte do autor, entre eles o levantamento da NFL (11-13) e
    a taxa da LCA (09-18).
- **Risco:** médio.
- **Métrica:** palavras de conteúdo de origem pipeline cortadas pelo autor (1.123 hoje).

### P9 — Experimento de autoviés (não muda o pipeline agora)

- **Achado:** D11.
- **Mudança.** Na Fase E, a etapa 5 (crítica) e o juiz pareado rodam também com um modelo de outra
  família, via `agy`. Mede-se quanto da crítica coincide com as edições reais do autor e quanto do juiz
  concorda com a escolha do autor. A decisão de trocar modelo fica para depois da Fase E.
- **Risco:** baixo.
- **Custo:** chamadas ao `agy` em 4 posts.
- **Métrica:** coincidência entre crítica e edições do autor; concordância do juiz com o autor.

### P15 — LanguageTool local (opcional, dependência)

- **Achado:** Fase A §6. São 7 erros de digitação no site, todos introduzidos depois do pipeline, na
  edição no Substack.
- **Mudança.** LanguageTool em Docker (LGPL, roda local, nada sai da máquina), usado:
  - pela colheita (P10) sobre o texto publicado;
  - opcionalmente, como aviso no `checar_post.py`.
- **Alternativa stdlib.** A heurística de palavra rara no corpus achou 3 dos 7 erros, com 4 falsos positivos.
- **Risco:** baixo.
- **Dependência:** Docker e a imagem do LanguageTool. Pede sua aprovação.
- **Métrica:** erros de digitação apontados no publicado.

## Onda 4 — Colheita, visuais, marketing

### P10 — `/forja-de-voz colher <slug|todos>`: colheita pós-publicação

- **Achados:** D14, D5. Pedido central do épico: manter a voz viva a partir do publicado.
- **Mudança.** Um modo novo em `forja-de-voz/SKILL.md`:
  1. `corpus_publicado.py` capturar e normalizar;
  2. `diff_edicoes.py <slug>`;
  3. `checar_post.py` sobre o publicado (marcador no ar e, com P15, erro de digitação);
  4. propõe `url_publicada` se faltar;
  5. atualiza o registro de preferências (P7);
  6. sugere item para "Em observação" quando um padrão atinge 3 ou mais ocorrências em 2 ou mais posts.

  O modo nunca altera §3 ou §4 sem aprovação. A etapa 10 do `post-substack` termina com uma linha:
  "depois de publicar, rode `/forja-de-voz colher <slug>`".
- **Risco:** médio.
- **Métrica:** posts da era pipeline com captura e tripla em dia (16 de 16 hoje, mas feito à mão).

### P11 — Alt-text e legenda para colar

- **Achado:** D8. O site tem 0 alt-text em 48 imagens.
- **Mudança:**
  - **`prompts-visuais`:** alt-text com até 125 caracteres e legenda de uma linha.
  - **Etapa 10:** a lista de inserção manual mostra, por figura, "alt-text para colar" e "legenda para
    colar", no mesmo formato dos botões.
  - A acessibilidade continua obrigatória. O que muda é a entrega.
- **Risco:** baixo.
- **Métrica:** imagens com alt-text e com legenda no site.

### P12 — Botões da 9a: compartilhar e comentar, sem inscrição obrigatória

- **Achado:** D9. Decisão do GATE B.
- **Mudança:**
  - **`regras-cta.md`:** o papel `inscricao` deixa de ser obrigatório ("2: um no primeiro quarto e outro no
    fim" sai). O botão sugerido por padrão vira `compartilhar` no primeiro quarto, onde o autor já o põe
    (11-13), e `comentar` no fim, quando há gancho. Inscrição só se o autor pedir.
  - **`scripts/parecer.py`:** saem as linhas 124–127 (erro por falta de inscrição no primeiro quarto e no
    fim). `scripts/test_parecer.py` acompanha a mudança.
  - **`referencias/exemplos.md`:** o caso "só os botões de inscrição" é atualizado.
- **Risco:** médio (validador).
- **Métrica:** botões aceitos que aparecem no site (0 de 5 hoje).

### P13 — Aviso legal como fonte única

- **Achado:** Fase A, natureza `aviso-legal`. O aviso está em 7 dos 13 posts publicados desde 09-01,
  sem padrão por linha: 09-01, 09-11, 10-15, 10-27, 10-30, 11-02 e 11-09. Falta em 09-18, 09-24, 09-28, 10-12 e 11-13.
- **Mudança:**
  - O texto, copiado do site, vai para `docs/AVISO_LEGAL.md`.
  - A etapa 9 acrescenta o aviso ao fim de todo `post.md`, ou só nos posts que o autor indicar.
  - O `checar_post.py` avisa se ele faltar.
- **Risco:** baixo.
- **Métrica:** posts com aviso legal.

---

## Não fazer

| Considerado | Por que não |
|---|---|
| Fine-tuning, Antislop Sampler ou FTPO | Pedem controle de sampling ou pesos. O pipeline roda no Claude Code; o equivalente possível é a lista calibrada (P2) e a checagem (P4) |
| Embedding de estilo (StyleDistance, LUAR) como métrica | É dependência pesada para um sinal auxiliar, e o STEB conclui que nenhum embedding vence em tudo. As métricas de forma (B3) e a distância de edição já medem o que importa. Reabrir se a Fase E ficar inconclusiva |
| NILC-Metrix | Dá 200 métricas de complexidade, mas o problema medido é de forma (parágrafo, ênfase, travessão), coberto pelo `estratos.py` |
| Reescrever a frente D | Ela continua válida como pesquisa. O erro era usá-la como checklist padrão (P2, P14) |
| Mexer na etapa 7 | É a etapa mais respeitada pelo autor (D2). O problema das pendências está no gate (P5) |
| Paralelizar as etapas 6 e 7 | Continua sem evidência de ganho (backlog da auditoria de 2026) |
| Etapa nova de "estilo" ou agente novo de revisão | O retrabalho vem de regra errada (P1, P3) e de texto novo sem filtro (P6), não de falta de etapa |
| Regerar posts publicados | `CLAUDE.md`: posts publicados não são reescritos |
| Trocar o modelo dos agentes agora | Fica para depois do experimento P9 |

## Decisões do GATE C (2026-11-15)

| Item | Decisão |
|---|---|
| P1, P2, P3, P4, P5, P6, P14 (ondas 1 e 2) | aprovados |
| P7, P8, P9 (onda 3) | aprovados |
| P15 LanguageTool | **recusado**. Sem dependência nova; a colheita usa a heurística stdlib e marca o resultado como suspeita |
| P10, P11, P12, P13 (onda 4) | aprovados |
| P13, escopo | o aviso legal entra **em todos os posts**, nas duas linhas |

As regras do P1 passam por uma segunda aprovação, uma a uma, no GATE da onda 1.

## Registro da Fase D

### Onda 1 — voz (concluída em 2026-11-16)

| Item | Commits | Decisão |
|---|---|---|
| P1 guia v2.0.0 | `c53b1d9`, `6a97222`, `aeefb64`; tag `voz-v2.0.0`; merge `447a41f` | aprovado regra por regra: quatro revogações e reformulações, todas as regras novas, antítese como voz com teto, linha de base com recorte, confiança alta para forma |
| P2 referências de voz | ver `git log -- .claude/skills/voz-syntaxis` | aprovado no fim da onda |
| P3 revisor da etapa 6 | ver `git log -- .claude/agents/revisor-gramatical.md` | aprovado no fim da onda |
| Varredura de referências | `fix(sistema): referências ao guia v2` | consequência do P1 |

Desvios registrados:
- Os extratores rodaram como agentes gerais seguindo `extrator-de-estilo.md` (os agentes do
  hemingway não carregam numa sessão aberta na raiz). Cada um gravou o próprio JSON, para não
  trazer 31 extrações para o contexto principal. Uma evidência parafraseada foi trocada pelo
  trecho literal.
- A branch `voz/2.0.0` saiu da branch do épico (precisa do corpus) e voltou para ela; o merge em
  `main` fica para a Fase F, com a sua autorização.

### Onda 2 — gate e checagens (concluída em 2026-11-16)

| Item | Entrega | Decisão |
|---|---|---|
| P4 | `scripts/checar_post.py` + `scripts/test_checar_post.py` (12 testes) | aprovado no fim da onda |
| P5 + P6 | `post-substack/SKILL.md` (etapas 9 e 10), `revisao-editorial.md` (checklist de 11 para 6) | aprovado no fim da onda |
| P14 | `tecnicas-narrativas.md` sem a fórmula de manchete; `docs/BACKWARDS_DESIGN.md` §3 | aprovado no fim da onda |

Ajuste feito durante a onda: saiu o aviso de "aspas retas" do checador. O Substack converte as
aspas ao colar (291 trocas tipográficas na Fase A), então o aviso só fazia ruído.
Contra o site, o checador acha os quatro resíduos publicados: dois `[VERIFICAR]`, um `[LINK` e o
jargão de 08-25.

### Onda 3 — conteúdo, crítica e preferências (concluída em 2026-11-16)

| Item | Entrega | Decisão |
|---|---|---|
| P7 | `diff_edicoes.py preferencias` → `estilo/preferencias-de-edicao.md` (15 tipos de edição); teste; `voz-syntaxis` manda as etapas 4, 6 e 9 lerem | aprovado no fim da onda |
| P8 | `pesquisador-editorial.md` (etiqueta de pertinência), `critico-editorial.md` (pergunta + 3 cortes reais), etapa 4 do `post-substack` | aprovado no fim da onda |
| P9 | sem mudança no pipeline; desenhado para a Fase E (crítica e juiz também com modelo de outra família, via `agy`) | aprovado no GATE C |

### Onda 4 — colheita, visuais, marketing (concluída em 2026-11-16)

| Item | Entrega | Decisão |
|---|---|---|
| P10 | modo `colher` em `forja-de-voz/SKILL.md`; lembrete no fim da etapa 10; ensaio de ponta a ponta sem alterar dados | aprovado no fim da onda |
| P11 | `checar_post.py` (alt-text ≤ 125 e lista para colar; parágrafo sem palavra); `prompts-visuais.md` | aprovado no fim da onda |
| P12 | `parecer.py` sem inscrição obrigatória; `regras-cta.md`, `exemplos.md`, `estrategia-marketing/SKILL.md`; teste trocado | aprovado no fim da onda |
| P13 | `docs/AVISO_LEGAL.md` (versão de 10-27 a 11-09; a anterior está registrada no arquivo); etapa 9; aviso no checador | aprovado no fim da onda |

A Fase D está concluída. Todos os testes passam (58).
