<p align="center">
  <img src="logo.png" alt="Hemingway — Personal Editor" width="280">
</p>

<h1 align="center">hemingway</h1>

<p align="center"><em>De transcrição de áudio a post publicável no Syntaxis, na sua voz, verificado tecnicamente.</em></p>

---

Este repositório **não é um projeto de código** — é um sistema editorial que roda dentro do
Claude Code. Ele lê uma transcrição de áudio, passa por um pipeline de onze etapas
(briefing → estrutura → pesquisa → draft → crítica → revisão → verificação → visuais →
consolidação → aprovação sua), e devolve um post pronto para colar na Substack, com as
ilustrações e os gráficos já especificados.

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
áudio (fora do repo)
      │  você transcreve (ferramenta externa)
      ▼
_arquivo/transcricoes/AAAA-MM-DD_slug.txt   (crua, nunca editada depois)
      │
      │  /post-substack _arquivo/transcricoes/AAAA-MM-DD_slug.txt
      ▼
posts/AAAA-MM-DD-slug/processo/   (00 a 08 — rascunho, crítica, revisão, verificação...)
      │
      │  etapa 9 consolida
      ▼
posts/AAAA-MM-DD-slug/{post.md, ilustracoes.md, graficos.md}   (os três entregáveis)
      │
      │  etapa 10 — GATE HUMANO: você aprova, pede ajuste, ou aborta
      ▼
  aprovar → /publicar slug   →   main + tag publicado/AAAA-MM-DD-slug → GitHub
```

## Passo a passo — publicar um post do zero

### 1. Grave e transcreva o áudio

Grave sua ideia como faria normalmente. Transcreva com a ferramenta que preferir (Whisper,
o transcritor do seu celular, o que for) e salve o texto cru — com hesitações, repetições,
tudo — em:

```
_arquivo/transcricoes/AAAA-MM-DD_titulo-resumido.txt
```

Esse arquivo **nunca é editado depois de criado**. Se um dia esta pasta ganhar áudios
(`_arquivo/audios/`), eles seguem a mesma regra e vão para o Git LFS automaticamente (já
configurado em `.gitattributes`).

### 2. Rode o pipeline

Dentro do Claude Code, na raiz do repo:

```
/post-substack _arquivo/transcricoes/AAAA-MM-DD_titulo-resumido.txt
```

Isso cria a branch `post/AAAA-MM-DD-titulo-resumido` e começa a rodar as onze etapas. Cada
etapa grava seu arquivo em `posts/<slug>/processo/`, atualiza `estado.json` e commita
sozinha — você não precisa fazer nada até a etapa 10, mas pode acompanhar em tempo real
lendo os arquivos de `processo/` conforme eles aparecem.

| # | Etapa | O que acontece |
|---|---|---|
| 0 | Ingestão | Limpa a transcrição (hesitação fora, suas palavras preservadas) sem tocar no original |
| 1 | Briefing | Define tese, gancho, analogias a preservar, encaixe no funil, e qual das duas vozes (ensaística ou explicativa) o post vai usar |
| 2 | Estrutura | Decide subtítulos, o que cada seção prova, onde entram ilustração/gráfico, e mapeia o arco narrativo |
| 3 | Pesquisa | Um subagente busca dados, contrapontos e como o tema é tratado — sem escrever prosa |
| 4 | Draft | Primeira versão do texto, na sua voz |
| 5 | Crítica estrutural | Um subagente diagnostica o argumento (sem reescrever); se achar problema grave, o pipeline volta à etapa 2 |
| 6 | Linha e norma | Um subagente revisa frase e norma culta, sem mexer em estrutura |
| 7 | Verificação técnica | Um subagente recalcula fórmulas e confere fontes; o que não fecha vira `[VERIFICAR: ...]` |
| 8 | Visuais | Gera `ilustracoes.md` (prompts de imagem) e `graficos.md` (specs + código Plotly) |
| 9 | Consolidação | Junta tudo, confere coerência entre as etapas, emite os três entregáveis finais |
| 10 | **Você decide** | O pipeline para e mostra o post pronto |

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

Abra `posts/<slug>/post.md`, `ilustracoes.md` e `graficos.md`. Gere as imagens no
`GERADOR_IMAGEM` usando os prompts prontos de `ilustracoes.md`, rode os blocos Python de
`graficos.md` para gerar os SVGs/PNGs dos gráficos, substitua os placeholders `ilu-NN`/
`graf-NN` pelas imagens reais, e cole na Substack.

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
  ├─ audios/           gravações cruas (Git LFS)
  ├─ transcricoes/     transcrições cruas
  ├─ amostras/         textos usados para construir o guia de voz
  └─ MANIFESTO.md      origem e proveniência de cada item acima

estilo/             o guia de voz e seus derivados
  ├─ estilo-autoral.md     ← leia este primeiro para entender "como eu escrevo"
  ├─ voz.fingerprint.json  versão verificável por máquina do guia
  ├─ corpus-manifest.json  hash de cada amostra usada
  └─ scripts/metricas.py   camada quantitativa (roda com `python3`)

marca/tokens.json  design tokens (cores, tipografia) — fonte única para prompts e gráficos

pesquisa/           material de apoio (estilometria, editoração, antipadrões de IA em pt-BR)

posts/<slug>/       um post publicado ou em andamento
  ├─ post.md             o texto final
  ├─ ilustracoes.md      prompts de imagem prontos
  ├─ graficos.md          specs + código Plotly executável
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
| Começar um post novo | `/post-substack _arquivo/transcricoes/<arquivo>.txt` |
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
