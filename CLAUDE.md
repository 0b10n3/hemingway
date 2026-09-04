# hemingway — sistema editorial Syntaxis

Este repositório transforma transcrições de áudio em posts publicáveis na Substack
**Syntaxis** (educação de investimentos), escritos na voz do autor, verificados
tecnicamente, com os visuais especificados. Não é um repositório de código de produto — é
um sistema de skills, subagentes e arquivos versionados que juntos formam um pipeline
editorial.

## Regras invioláveis

- **`_arquivo/` é imutável.** Nada ali é editado, renomeado, reformatado ou apagado — nunca,
  por nenhuma etapa, por nenhum subagente. Leia de `_arquivo/`; escreva em `posts/`,
  `estilo/` ou `pesquisa/`. Se uma transcrição precisa de limpeza, a versão limpa nasce em
  `posts/<slug>/processo/00-transcricao.md`; a crua permanece intocada.
  **Exceção única e explícita:** `_arquivo/MANIFESTO.md` pode receber *acréscimo* de linhas
  (preencher um "a preencher" com a proveniência de um item já catalogado, ou catalogar item
  novo) porque seu propósito é documentar o que existe em `_arquivo/`, e isso cresce junto
  com a pasta. Mesmo assim: nunca reescreva uma linha já preenchida sobre um item existente —
  só complete lacunas ou adicione linhas novas. Todo outro arquivo de `_arquivo/` é
  intocável sem exceção. (Esta exceção foi adicionada em 2026-08-10 depois que o teste de
  imutabilidade da Fase 4 pegou uma violação real — ver `RELATORIO.md`.)
- **Evidência ou silêncio.** Nenhuma afirmação sobre a voz do autor entra no guia sem pelo
  menos duas ocorrências reais, em dois textos distintos, citadas com arquivo e trecho curto.
- **Amostras alheias são fonte de procedimento, não de frase.** Dos autores admirados
  (Michael Lewis, Ernest Hemingway, Malcolm Gladwell) extraímos *movimentos*, nunca
  vocabulário ou trechos a copiar.
- **Copyright: texto de terceiros não é commitado.** `_arquivo/amostras/admiradas/**/*.md`
  está no `.gitignore` — os artigos completos de autores admirados ficam só em disco local
  (ver `_arquivo/MANIFESTO.md`). O que entra no git é a extração (JSON) e a citação.
- **Descritivo e aspiracional ficam em camadas separadas e rotuladas** em
  `estilo/estilo-autoral.md`.
- **Não invente número, fonte, fórmula ou citação.** Dado sem fonte verificável vira
  `[VERIFICAR: ...]`.
- **Toda skill que escreve arquivo ou dispara pipeline leva `disable-model-invocation: true`.**
- **Nada de sobrescrita silenciosa.** Arquivo existente em `estilo/`, `.claude/` ou `posts/`
  só muda com confirmação do autor, item a item.
- **Uma fonte por fato.** Cada informação mora em exatamente um arquivo; os demais apontam
  por caminho relativo. Sem cópia, sem symlink.
- **Git nunca destrói histórico.** Ver §Git abaixo.

## Estrutura

```
_arquivo/          originais imutáveis: áudios, transcrições, amostras, MANIFESTO.md
estilo/            guia de voz e seus derivados (estilo-autoral.md é a fonte única)
pesquisa/          resumos das frentes de pesquisa (Claude Code, estilometria, editoração, antipadrões IA)
posts/<slug>/      post.md, capa.md, ilustracoes.md, graficos.md, diagramas.md,
                   infograficos.md (entregáveis — capa.md sempre presente, os demais
                   condicionais à peça existir) + processo/ (rascunho de etapas)
.claude/skills/    skills de referência e de tarefa
.claude/agents/    subagentes de trabalho isolado (leitura pesada, pesquisa, crítica, verificação)
```

**Nota de 31/08/2026 (atualizada em 04/09/2026 — sincronização com a v3.0):** este repo não
mantém mais cópia própria de design tokens. A pasta `marca/` (que tinha `tokens.json` do
sistema "O Sinal no Escuro" v2.1) foi removida — `../../brand/DESIGN.md` (hoje v3.0,
reconstruído do zero na rodada 3) é o sucessor declarado desse sistema e passa a ser a fonte
única de identidade visual para todo o ecossistema Syntaxis, não só para este repo. Nenhum
gráfico ou ilustração já publicado foi regenerado — a correção vale só daqui para frente
(ver `.claude/skills/marca-syntaxis/SKILL.md`).

## Fonte única de cada coisa

- **Voz autoral:** `estilo/estilo-autoral.md` (legível) + `estilo/voz.fingerprint.json`
  (verificável por máquina). Toda skill que escreve texto aponta para cá — nunca duplica regra.
  **Distinção importante:** isto é a voz autoral pessoal de quem escreve o Substack, não a
  voz de marca/produto da Syntaxis — ver `../../brand/DESIGN.md` §3, que trata de tom em
  copy/curso/produto, não da prosa ensaística de um autor específico. Os dois documentos
  coexistem porque descrevem coisas diferentes; nenhum substitui o outro.
- **Marca/design tokens:** `../../brand/DESIGN.md` (regras) +
  `../../brand/tokens/syntaxis.tokens.json` (valores exatos, formato DTCG) — referenciados
  por caminho relativo, nunca copiados para dentro deste repo. Todo código Plotly em
  `graficos.md` novo lê esses arquivos em vez de repetir cor literal.
- **Público e estratégia comercial:** `_arquivo/MARKETING_REVIEW.md`.
- **Antipadrões de texto gerado por IA em pt-BR:** `pesquisa/frente-d-antipadroes-ia-ptbr.md`.

## O pipeline: `/post-substack <caminho-da-transcrição>`

Onze etapas (0-10), cada uma grava em `posts/<slug>/processo/`, atualiza `estado.json` e
**commita**. A skill retoma da última etapa concluída se invocada de novo com o mesmo slug.
Ordem: ingestão → briefing → estrutura → pesquisa → draft → crítica estrutural → revisão de
linha/norma → verificação técnica → visuais → consolidação → **gate humano**. Detalhes
completos em `.claude/skills/post-substack/SKILL.md`.

Os entregáveis (`post.md`, `capa.md`, `ilustracoes.md`/`graficos.md`/`diagramas.md` quando a
peça existir, `infograficos.md` só no caso condicional — ver `.claude/skills/prompts-visuais/SKILL.md`)
ficam na raiz de `posts/<slug>/`, separados de `processo/`.

## Git

Convenção de commit: `<tipo>(<escopo>): <o que mudou, no imperativo>`. Tipos: `feat`, `fix`,
`docs`, `chore`, `refactor`. Escopos: `voz`, `sistema`, `arquivo`, `pesquisa`, ou o slug do
post. Uma etapa do pipeline = um commit.

Branches: `main` (só conteúdo aprovado), `post/<slug>` (ciclo de um post), `voz/<versao>`
(mudança de regra do guia, via `/forja-de-voz atualizar`).

**Nunca** pré-aprove nem execute sem perguntar: `push --force`, `reset --hard`, `rebase` de
histórico já publicado, `clean -fd`, `filter-branch`, deleção de branch remota. Antes de
qualquer commit, verifique que nada de `.env`/chave/token entrou no diff.

## Ao rodar este repositório de novo

Verifique `estilo/voz.fingerprint.json` e `.claude/skills/post-substack/SKILL.md` antes de
propor recriar qualquer coisa — se já existem, o modo é auditoria/atualização, não bootstrap.
Ver protocolo completo em `.claude/skills/forja-de-voz/references/protocolo-de-atualizacao.md`.
