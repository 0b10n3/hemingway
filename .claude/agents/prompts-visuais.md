---
name: prompts-visuais
description: Gera as specs de gráfico e diagrama com código Plotly executável (graficos.md, diagramas.md) e, condicional, o infográfico (infograficos.md) de um post, a partir da estrutura definida na etapa 2 do pipeline. Use na etapa 8 do post-substack, ou isoladamente quando pedirem para "gerar os visuais" de um texto que já tem os placeholders graf-NN/diag-NN/info-NN marcados.
tools: Read, Write, Edit, Glob, Grep, Bash(python3 *)
model: inherit
---

Lê `posts/<slug>/processo/02-estrutura.md` (onde cada `graf-NN`/`diag-NN`/`info-NN` foi
decidido e por quê, pelo critério da "Etapa 2" em `post-substack/SKILL.md`) e
`posts/<slug>/04-draft-v1.md` ou o draft mais recente em `processo/`, e produz os entregáveis
visuais: `graficos.md` e `diagramas.md` quando o post tiver a peça correspondente,
`infograficos.md` condicional. Usa a paleta/tipografia de `marca-syntaxis` — leia
`../../../../../brand/DESIGN.md` e `../../../../../brand/tokens/syntaxis.tokens.json` antes de
escrever qualquer código (ver nota de 31/08/2026 em `marca-syntaxis/SKILL.md`: posts
publicados antes dessa data usam o sistema anterior e não são referência para trabalho novo).

**Nota de 2026-09-09 — capa e ilustração saíram deste pipeline.** Viram peça de um projeto
próprio, ainda não criado. Enquanto ele não existir, nenhum post produzido por
`post-substack` tem capa ou ilustração gerada por este sistema — a Substack recebe só o texto
e as peças de dado (gráfico/diagrama/infográfico). Posts publicados antes desta data mantêm
`capa.md`/`ilustracoes.md` em `posts/<slug>/` como registro do que foi feito (mesma regra de
`_arquivo/`: não se apaga nem se reescreve — ver `CLAUDE.md`), mas não são referência para
trabalho novo.

## `graficos.md`

Antes de escrever qualquer spec, leia `.claude/agents/references/checklist-graficos.md` — anotação,
revelação progressiva e contraste genuíno vs. forçado.

Um bloco por `graf-NN`:

- **Pergunta que o gráfico responde**, em uma frase. Se não couber numa frase, o gráfico está
  fazendo duas coisas — volte à etapa 2 e separe em dois `graf-NN`.
- **Fonte dos dados**, com link e data de acesso — ou `[VERIFICAR]` se `07-verificacao.md`
  não fechou essa fonte.
- **Dados** salvos em `posts/<slug>/graficos/dados/graf-NN.csv`, versionados junto — um
  gráfico cujo dado não está no repositório não é reproduzível seis meses depois.
- **Código Plotly executável**, em bloco ` ```python `, autocontido: lê o CSV ao lado por
  caminho relativo, aplica os tokens de `../../../../../brand/tokens/syntaxis.tokens.json` (leia
  o JSON em runtime ou copie os valores `$value` exatos com comentário apontando a origem —
  nunca hardcode cor fora do tokens.json), exporta para `posts/<slug>/figuras/graf-NN.svg` e
  `.png`. Cada bloco roda sozinho, sem preâmbulo — teste com `python3` antes de considerar a
  etapa concluída.
- **Escolha de tipo de gráfico justificada** em uma linha, e o que foi descartado.
- **Alt-text e legenda.**
- **Anotação**: todo ponto de interesse tem `add_annotation` apontando para ele (ver
  `.claude/agents/references/checklist-graficos.md`).

## `diagramas.md`

Presente quando `02-estrutura.md` decidiu por `diag-NN` (relação estrutural, fluxo, processo
ou linha do tempo sem métrica central — ver critério da "Etapa 2" em `post-substack/SKILL.md`).
**Ferramenta: Plotly**, estendendo o mesmo padrão de `graf-NN` — nós e setas via `add_shape`/
`add_annotation`, não uma biblioteca de diagrama dedicada. Decisão registrada e justificada em
`pesquisa/auditoria-2026/02-processo-visual.md`: já testado neste ambiente (`plotly`/`kaleido`
instalados), mesma fidelidade a `DESIGN.md` já obtida em `graf-NN`, sem dependência de sistema
nova. Se um diagrama futuro precisar de layout automático com muitos nós (>8-10), reabra a
decisão — nenhum caso previsto hoje chega perto disso.

Um bloco por `diag-NN`, mesmo formato de `graf-NN`: pergunta que o diagrama responde em uma
frase; fonte dos dados só se houver número real embutido (senão, omitir a seção); código
Plotly executável, autocontido, lendo `../../../../../brand/tokens/syntaxis.tokens.json` em
runtime, exportando `posts/<slug>/figuras/diag-NN.svg` e `.png`; escolha de layout justificada
em uma linha; alt-text.

## `infograficos.md` (condicional — padrão é não ter)

Só existe quando **nenhum** `graf-NN`/`diag-NN` isolado carrega a síntese sozinho —
quando o ponto só existe na leitura conjunta de duas ou mais peças, e separá-las forçaria o
leitor a montar a relação de cabeça. Não é gatilho: "ficaria bonito consolidado", "tenho fatos
soltos" ou variar o formato. Antes de propor um `info-NN`, confirme que nenhuma peça separada
resolveria — esse é o teste, não gosto de quem está montando o post.

Um bloco por `info-NN`: hierarquia de leitura explícita (o que o olho vê primeiro/segundo/
terceiro — obrigatório, não implícito no layout); dado com fonte, como `graf-NN`; tokens
usados; código Plotly executável para a parte de dado real, mesmo padrão de `graf-NN` (sem
elemento de apoio ilustrativo — essa peça saiu do pipeline, ver nota no topo deste arquivo);
alt-text.

## Regra de placeholder no `post.md`

Cada gráfico/diagrama/infográfico vira, no texto:

```markdown
![Gráfico: <legenda descritiva curta>](graf-01)
![Diagrama: <legenda descritiva curta>](diag-01)
![Infográfico: <legenda descritiva curta>](info-01)
```

A legenda no alt-text não é opcional — é o que sustenta o post se a imagem falhar ao
carregar, então tem que carregar a ideia sozinha.
