---
name: revisao-editorial
description: Passada final de coerência sobre um post já com crítica estrutural, revisão de linha e verificação técnica aplicadas — confere se as três etapas não se contradisseram e se os entregáveis (post.md, capa.md, ilustracoes.md, graficos.md, diagramas.md, infograficos.md quando existir) estão consistentes entre si. Use na etapa 9 do pipeline post-substack, ou isoladamente quando pedirem para "dar uma revisão final" num texto já pronto.
disable-model-invocation: true
argument-hint: [caminho-do-slug-em-posts/]
allowed-tools: Read Edit Glob Grep
---

Esta skill roda **depois** das etapas 5 (crítica estrutural), 6 (linha/norma) e 7
(verificação técnica) — ela não refaz o trabalho delas, confere se o resultado combinado
ainda faz sentido como um todo. Editoração em camadas existe justamente para não misturar
essas responsabilidades (ver `pesquisa/frente-c-editoracao.md`); esta skill é o único ponto
que olha as três juntas.

## Checklist de consolidação

1. **Coerência entre etapas.** A crítica estrutural (`05-critica.md`) pediu corte ou
   reordenação que a revisão de linha (`06-revisao.md`) não aplicou? A verificação técnica
   (`07-verificacao.md`) mudou um número que quebra uma frase da revisão de linha? Resolva
   divergências lendo os três arquivos de `processo/` antes de tocar em `post.md`.

2. **Checklist de aderência à voz** (§9 de `estilo/estilo-autoral.md`, via skill
   `voz-syntaxis`) — os dez itens, um a um.

3. **Zero `[VERIFICAR]` ou `[FAIXA]` sem review humano.** Se `07-verificacao.md` deixou algum
   item aberto (`[VERIFICAR: ...]`) ou marcou um número como intervalo mal representado como
   ponto único (`[FAIXA: ...]`), ambos devem aparecer no `post.md` visíveis — nunca
   silenciosamente resolvidos a favor de uma suposição ou do valor único original.

4. **Placeholders consistentes entre os entregáveis.** Todo `ilu-NN`/`graf-NN`/`diag-NN`/
   `info-NN` citado em `post.md` tem bloco correspondente em `ilustracoes.md`/`graficos.md`/
   `diagramas.md`/`infograficos.md`, e vice-versa — nenhum placeholder órfão em nenhuma
   direção.

5. **Antipadrões de IA.** Passe `references` de `voz-syntaxis` (`antipadroes.md`) e, se
   houver tempo, a lista completa em `pesquisa/frente-d-antipadroes-ia-ptbr.md` sobre o texto
   final — a revisão de linha (etapa 6) já deve ter pego a maioria, esta é a rede de segurança.

6. **Frontmatter do `post.md`** — título, subtítulo, data, tags, status — está preenchido e
   coerente com o briefing (`01-briefing.md`)?

7. **Manchete** (opcional — ver `references/tecnicas-narrativas.md`, "fórmula de manchete"):
   o título testa a fórmula conceito+quebra-de-intuição+prática? Não é bloqueante — é
   técnica a testar, não regra do guia de voz. Se aplicar bem, ótimo; se o título temático
   atual já funciona, não force.

8. **Achado enterrado — alarme, não correção.** Se o insight mais forte do post ainda
   estiver no meio de um parágrafo neste ponto do pipeline, esta skill não reestrutura (não
   é seu escopo, ver acima). Sinalize explicitamente no resumo da etapa 10 que a etapa 5
   (crítica estrutural) deixou passar isso — é informação para o gate humano decidir se vale
   reabrir a etapa 2, não uma correção silenciosa aqui.

9. **Inventário visual completo.** Todo post tem `capa.md`. Todo `ilu-NN`/`graf-NN`/`diag-NN`/
   `info-NN` referenciado em `post.md` tem bloco no arquivo certo (ver item 4). `infograficos.md`
   só existe se o critério de gatilho de `prompts-visuais/SKILL.md` de fato se aplicou — se
   existir sem justificativa registrada, sinalize. Todo prompt de imagem em `capa.md`/
   `ilustracoes.md` declara no cabeçalho para qual gerador foi escrito (ver
   `prompts-visuais/SKILL.md`, "Gerador ativo hoje") — se faltar, sinalize.

10. **Paleta fora dos tokens — checagem mecânica.** `Grep` por `#[0-9A-Fa-f]{6}` em `capa.md`,
    `ilustracoes.md` e `infograficos.md` (arquivos baseados em prompt — `graficos.md` e
    `diagramas.md` já são estruturalmente seguros, o código lê `tokens.json` em runtime, não
    precisa desta checagem). Compare cada hex encontrado contra os valores `$value` de
    `../../brand/tokens/skill_test.tokens.json` (leia o arquivo). Hex fora da lista vira
    pendência para o gate humano — não corrija sozinho qual token o autor quis dizer.
    **A isenção de `graficos.md`/`diagramas.md` pressupõe que o código roda com sucesso — esta
    etapa não executa o bloco Python, só lê o texto.** Quem confirma que o import de fato
    resolve é o autor, ao rodar o código antes de aprovar a figura no gate humano; se o
    caminho do token estiver quebrado, o erro aparece ali, não aqui.

11. **Gate de Tufte — checagem mecânica.** Para cada bloco de código em `graficos.md`/
    `diagramas.md`: `rangemode="tozero"` presente (ou exceção justificada por escrito no
    spec)? Nenhuma menção a `3d`, sombra (`shadow` fora de `shadow.syntaxis*`), textura ou
    moldura no código? Se o spec já traz "Lie Factor" declarado, confira a conta; se a peça
    tem ênfase visual e não declara, sinalize para o gate humano — não calcule por conta
    própria sem o dado bruto. Critério completo em
    `.claude/skills/prompts-visuais/references/checklist-graficos.md`, seção "Gate de Tufte".

## Saída

Aplica as correções diretamente nos entregáveis (`post.md`, `capa.md`, `ilustracoes.md`,
`graficos.md`, `diagramas.md`, `infograficos.md` quando existirem) e devolve um resumo curto
do que mudou desde a etapa 7, para o gate humano (etapa 10) mostrar ao autor.
