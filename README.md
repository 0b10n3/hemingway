<p align="center">
  <img src="logo.png" alt="Hemingway — Personal Editor" width="280">
</p>

<h1 align="center">hemingway</h1>

<p align="center"><em>De rascunho a post publicável no Syntaxis, na sua voz, verificado tecnicamente.</em></p>

---

Este repositório **não é um projeto de código** — é um sistema editorial que roda dentro do
Claude Code. Ele lê um rascunho pré-estruturado seu (com front-matter declarando a linha
editorial), passa por um pipeline de onze etapas mais sub-etapas condicionais por linha
(briefing → estrutura → pesquisa → revisão/integração do rascunho → crítica → revisão →
verificação → visuais → consolidação → aprovação sua), e devolve um post pronto para colar
na Substack, com os gráficos, diagramas e infográficos já especificados (capa e ilustração
não fazem mais parte deste pipeline — ver nota em `.claude/skills/prompts-visuais/SKILL.md`).
O pipeline não reescreve seu rascunho do zero nem reordena sua argumentação por conta
própria — ele revisa, verifica, questiona e sugere; qualquer mudança estrutural vira
pergunta para você, nunca edição silenciosa.

Este README é o manual de uso. Para as regras internas do sistema (o que cada skill pode e
não pode fazer), veja `CLAUDE.md`. Para o histórico de como o sistema foi construído, veja
`RELATORIO.md`.

## Pré-requisitos

- [Claude Code](https://code.claude.com) instalado, versão 2.1.196+ (confira com
  `claude --version`; o sistema usa campos de frontmatter recentes de skills/subagentes).
- `git` e `git-lfs` instalados (`git lfs install` já deve ter rodado neste repo — confira com
  `git lfs env` se um `git add` de PDF ou áudio reclamar de filtro).
- `python3` (stdlib apenas — `estilo/scripts/metricas.py` não usa nenhum pacote externo).
- `pdftotext` (do pacote `poppler-utils`) se você for processar PDFs como amostra de voz.
- Acesso de push ao remoto configurado em `git remote -v` (`origin`).

**Importante — skills e subagentes recém-criados só ficam disponíveis numa sessão nova do
Claude Code.** Se você acabou de instalar ou atualizar algo em `.claude/skills/` ou
`.claude/agents/`, **feche e abra o Claude Code de novo** (`cd hemingway && claude`) antes de
tentar usá-los — na mesma sessão em que foram criados, `/nome-da-skill` ou o subagente dão
erro de "não encontrado".

## Visão geral do fluxo

```
você escreve o rascunho, com front-matter (título, slug, data, linha_editorial, status)
      ▼
_arquivo/drafts/AAAA-MM-DD_slug.md   (cru, nunca editado depois)
      │
      │  /post-substack _arquivo/drafts/AAAA-MM-DD_slug.md
      ▼
posts/AAAA-MM-DD-slug/processo/   (00 a 09 — leitura, briefing, estrutura, crítica...)
      │  linha_editorial roteia sub-etapas: Spoiler ganha revisor-quant (5a, gate
      │  bloqueante); Notas de um Professor ganha Ficha de Saída na etapa 2
      │
      │  etapa 9 consolida
      ▼
posts/AAAA-MM-DD-slug/{post.md, [graficos.md], [diagramas.md], [infograficos.md]}
      (os entregáveis — todos condicionais à peça existir)
      _revisoes/AAAA-MM-DD-slug_*.md guarda as saídas de verificação condicional
      │
      │  etapa 10 — GATE HUMANO: você aprova, pede ajuste, ou aborta
      ▼
  aprovar → /publicar slug   →   main + tag publicado/AAAA-MM-DD-slug → GitHub
```

## Passo a passo — publicar um post do zero

### 1. Escreva o rascunho

Escreva sua ideia já estruturada — com a ordem de argumento e a voz que você quiser dar ao
texto — e salve com front-matter YAML mínimo em:

```
_arquivo/drafts/AAAA-MM-DD_titulo-resumido.md
```

```yaml
---
titulo:
slug:
data: AAAA-MM-DD
linha_editorial: Spoiler | Notas de um Professor
status: rascunho
---
```

`linha_editorial` é obrigatório e roteia o pipeline para um dos dois fluxos (ver seção
"Duas linhas editoriais" abaixo). Se faltar ou vier com valor inválido, o pipeline para e
pergunta — nunca adivinha pelo assunto do texto. Esse arquivo **nunca é editado depois de
criado**. Se um dia esta pasta ganhar áudios (`_arquivo/audios/`), eles seguem a mesma regra
e vão para o Git LFS automaticamente (já configurado em `.gitattributes`).

### 2. Rode o pipeline

Dentro do Claude Code, na raiz do repo:

```
/post-substack _arquivo/drafts/AAAA-MM-DD_titulo-resumido.md
```

Isso cria a branch `post/AAAA-MM-DD-titulo-resumido` e começa a rodar as onze etapas mais as
sub-etapas condicionais da sua linha editorial. Cada etapa grava seu arquivo em
`posts/<slug>/processo/`, atualiza `estado.json` e commita sozinha — você não precisa fazer
nada até a etapa 10, mas pode acompanhar em tempo real lendo os arquivos de `processo/`
conforme eles aparecem.

| # | Etapa | O que acontece |
|---|---|---|
| 0 | Leitura do rascunho | Lê o front-matter e o corpo, monta cópia de trabalho e inventário de marcadores, sem tocar no original |
| 1 | Briefing | Lê `linha_editorial` do front-matter (não decide); define tese, gancho, analogias a preservar, encaixe no funil, e qual das duas vozes (ensaística ou explicativa) o post vai usar |
| 2 | Estrutura | Decide subtítulos, o que cada seção prova, e para cada ponto que precisa de visual escolhe por critério — gráfico (série numérica), diagrama (relação estrutural sem métrica) ou infográfico (só se nenhuma peça isolada carregar a síntese). **Linha Notas de um Professor:** preenche a Ficha de Saída de backward design antes de fechar a estrutura (`docs/BACKWARDS_DESIGN.md`) |
| 3 | Pesquisa | Um subagente busca dados, contrapontos e como o tema é tratado — sem escrever prosa |
| 4 | Revisão/integração | Revisa e completa o rascunho na sua voz — não reescreve do zero; qualquer mudança de estrutura vira pergunta a você |
| 5 | Crítica estrutural | Um subagente diagnostica o argumento (sem reescrever); se achar problema grave, o pipeline volta à etapa 2. **Linha Spoiler:** inclui validação argumentativa (salto lógico, generalização indevida, conclusão mais forte que a evidência) |
| 5a | Revisão quantitativa (**só linha Spoiler**) | Um subagente somente-leitura (`revisor-quant`) aponta fragilidade de realismo de mercado/teoria/evidência, sempre como pergunta a você. Itens `bloqueante` **param o pipeline** até você responder |
| 6 | Linha e norma | Um subagente revisa frase e norma culta, sem mexer em estrutura |
| 7 | Verificação técnica | Um subagente recalcula fórmulas e confere fontes; o que não fecha vira `[VERIFICAR: ...]`. **Linha Spoiler:** confere nome/data/caso citado. **Linha Notas:** confere os dois lados do balcão, aderência dos exemplos ao Brasil, e a regra de referências (3-4, ≥2 livros) |
| 8 | Visuais | Gera `graficos.md`/`diagramas.md` (specs + código Plotly); `infograficos.md` só no caso condicional |
| 9 | Consolidação | Junta tudo, confere coerência entre as etapas (inclusive o gate da sua linha editorial), emite os entregáveis finais |
| 10 | **Você decide** | O pipeline para e mostra o post pronto |

### Duas linhas editoriais

| | Spoiler | Notas de um Professor |
|---|---|---|
| Sobre | Carreira, relato de jornada pessoal — "não é porque eu sofri que você também precisa sofrer" | Conceito/produto/instrumento financeiro, explicado com rigor técnico e os dois lados do balcão |
| Registro | Conversa, menos formal | Aula — backward design explícito (etapa 2) |
| Verificação extra | Argumento (salto lógico, generalização) + citação/nome/data + `revisor-quant` (etapa 5a, gate bloqueante) | Fórmula recalculada + dois lados do balcão + exemplos reais no Brasil + 3-4 referências, ≥2 livros |

Definição completa em `PROJECT_DESCRIPTION.md` §Linhas Editoriais; estrutura da linha Notas
em `docs/BACKWARDS_DESIGN.md`.

### 3. O gate — sua única decisão obrigatória

Na etapa 10 você vê o post final, o que mudou desde o rascunho, e qualquer pendência
`[VERIFICAR: ...]`. Três opções:

- **Aprovar e publicar** → o sistema chama `/publicar` sozinho (ver passo 4).
- **Ajustar** → diga o que quer mudar. O pipeline volta só até onde precisa (se for algo de
  conteúdo, refaz o draft — conta como um "loop"; se for só acabamento, refaz revisão/visuais
  sem gastar loop). Você tem 3 rodadas de ajuste por padrão antes do sistema parar e te
  entregar o estado atual para decisão manual.
- **Abortar** → a branch fica salva (nada é apagado), você decide depois o que fazer com ela.

### 4. Publicar

Se você aprovou no gate, isso já roda sozinho. Se quiser rodar manualmente depois:

```
/publicar AAAA-MM-DD-titulo-resumido
```

Isso confere que os três entregáveis existem e não têm `[VERIFICAR]` pendente sem revisão,
faz merge para `main` com `--no-ff`, cria a tag `publicado/AAAA-MM-DD-titulo-resumido`, e dá
push. A branch do post **não é apagada** — ela vira material de entrada para a próxima
atualização do guia de voz.

### 5. Copie para a Substack

Abra `posts/<slug>/post.md` e `graficos.md`/`diagramas.md`/`infograficos.md` quando existirem.
Rode os blocos Python para gerar os SVGs/PNGs, substitua os placeholders
`graf-NN`/`diag-NN`/`info-NN` pelas imagens reais, e cole na Substack. Capa e ilustração não
são geradas por este pipeline — suba manualmente o que a Substack exigir.

## Retomando um post em andamento

Se você fechou o Claude Code no meio do pipeline (ou ele parou por algum motivo), retome com:

```
/post-substack AAAA-MM-DD-titulo-resumido
```

O sistema lê `estado.json`, mostra o que já foi feito, e continua da última etapa concluída
— nunca refaz trabalho sem você pedir.

## Mantendo o guia de voz vivo

O guia (`estilo/estilo-autoral.md`) foi construído a partir de 7 amostras suas + 8 de autores
admirados (ver `estilo/CHANGELOG.md` para a v1.0.0). Ele **fossiliza se nunca for atualizado**.

- **A cada ~5 posts publicados**, rode:
  ```
  /forja-de-voz atualizar <caminho-da-nova-amostra>
  ```
  Isso compara a amostra nova contra o guia atual, classifica cada diferença (evolução real,
  ruído, ou desvio a corrigir), e propõe mudanças — nunca aplica regra nova sem sua aprovação.

- **Para conferir um texto qualquer contra o guia**, sem publicar nada:
  ```
  /forja-de-voz auditar <arquivo>
  ```

- **Para comparar duas versões do guia** (por tag git):
  ```
  /forja-de-voz diff voz-v1.0.0 voz-v1.1.0
  ```

- **Assim que você tiver o primeiro post de LinkedIn** (ou qualquer gênero novo), rode
  `atualizar` mesmo com menos de 5 posts — hoje o guia não sabe distinguir "traço geral" de
  "traço específico de Substack" por falta dessa amostra.

## Estrutura do repositório

```
_arquivo/          originais imutáveis — nunca editados depois de commitados
  ├─ audios/           gravações cruas (Git LFS), se houver
  ├─ drafts/           rascunhos crus do autor, com front-matter (linha_editorial etc.)
  ├─ amostras/         textos usados para construir o guia de voz
  └─ MANIFESTO.md      origem e proveniência de cada item acima

estilo/             o guia de voz e seus derivados
  ├─ estilo-autoral.md     ← leia este primeiro para entender "como eu escrevo"
  ├─ voz.fingerprint.json  versão verificável por máquina do guia
  ├─ corpus-manifest.json  hash de cada amostra usada
  └─ scripts/metricas.py   camada quantitativa (roda com `python3`)

docs/               documentação permanente absorvida de material de apoio
  └─ BACKWARDS_DESIGN.md   backward design da linha "Notas de um Professor"

pesquisa/           auditoria e histórico do próprio sistema hemingway
_pesquisa/          Deep Research pontual (via agy) sobre metodologia editorial
_revisoes/          saídas de revisão condicional por linha (revisor-quant, cálculo numérico)

posts/<slug>/       um post publicado ou em andamento
  ├─ post.md             o texto final
  ├─ graficos.md          specs + código Plotly executável
  ├─ diagramas.md         specs + código Plotly de diagramas (nós/setas, sem série numérica)
  ├─ infograficos.md      só quando nenhuma peça isolada carrega a síntese (condicional)
  ├─ graficos/dados/      CSVs dos gráficos
  ├─ figuras/             SVG/PNG gerados
  └─ processo/             rascunho de cada etapa do pipeline

.claude/
  ├─ skills/            o que você invoca com /nome
  └─ agents/            subagentes que o pipeline chama sozinho
```

## Comandos de referência rápida

| Quero... | Comando |
|---|---|
| Começar um post novo | `/post-substack _arquivo/drafts/<arquivo>.md` |
| Retomar um post | `/post-substack <slug>` |
| Publicar um post aprovado | `/publicar <slug>` |
| Atualizar o guia de voz com amostra nova | `/forja-de-voz atualizar <arquivo>` |
| Conferir um texto contra o guia sem publicar | `/forja-de-voz auditar <arquivo>` |
| Comparar duas versões do guia | `/forja-de-voz diff <tagA> <tagB>` |
| Reescrever algo fora do pipeline, na sua voz | invoque a skill `voz-syntaxis` ou só peça — ela carrega sozinha |
| Gerar só os visuais de um post que já tem estrutura | skill `prompts-visuais` |

## Se algo der errado

- **"Unknown skill" ou "Agent type not found"** ao invocar algo que você sabe que existe →
  feche e abra o Claude Code de novo (ver aviso no topo deste README).
- **Um post trava numa etapa** → leia `posts/<slug>/estado.json` e o último arquivo escrito
  em `processo/` para entender onde parou; rode `/post-substack <slug>` de novo para retomar.
- **Dúvida sobre por que o sistema tomou uma decisão de arquitetura** → `RELATORIO.md` tem o
  raciocínio completo do bootstrap, incluindo limitações conhecidas do corpus atual.
- **Achou um texto do sistema mexendo em `_arquivo/`** → isso é bug, pare e reporte; a única
  exceção documentada é acréscimo em `_arquivo/MANIFESTO.md` (ver `CLAUDE.md`).
