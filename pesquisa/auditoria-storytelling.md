# Auditoria — data storytelling & dataviz nas skills do sistema editorial

2026-08-10. Rubrica filtrada (Apêndice A do prompt de auditoria) confirmada sem alterações —
o insumo de BI corporativo foi tratado como autor admirado: procedimento extraído, superfície
(vocabulário MRR/CAC/"the ask") descartada por completo. Nenhum exemplo do documento original
entra em qualquer artefato do sistema.

Artefatos auditados (todos existem — nenhuma lacuna de "skill ainda não gerada"):
`post-substack/SKILL.md`, `critico-editorial.md`, `prompts-visuais/SKILL.md`,
`revisao-editorial/SKILL.md`, `verificador-tecnico.md`. `estilo/estilo-autoral.md` foi lido
só para checagem de conflito, nunca seria editado por esta auditoria.

## Achados (Fase 2)

```json
{
  "artefato": ".claude/skills/post-substack/SKILL.md",
  "tecnica": "gancho explícito (arco em seis atos / setup-conflito-resolução)",
  "estado_atual": "etapa 1 (linha 47) pede 'tese em uma frase', analogias do áudio, encaixe no funil e a voz (§4) — não pede um gancho/abertura escolhida como campo separado",
  "lacuna": "a tese é o QUÊ do argumento; o gancho é COMO a primeira frase prende o leitor. Sem campo próprio, o gancho fica implícito e só aparece de fato na etapa 4 (draft), tarde demais para orientar a etapa 2 (estrutura)",
  "severidade": "reforço",
  "patch_proposto": 2
}
```

```json
{
  "artefato": ".claude/skills/post-substack/SKILL.md",
  "tecnica": "arco narrativo (seis atos ou setup-conflito-resolução) + três pilares (dado/narrativa/visual)",
  "estado_atual": "etapa 2 (linha 48) produz 'subtítulos; o que cada seção prova; onde entra ilu-NN/graf-NN; o que fica de fora' — uma lista de seções, cada uma com uma obrigação de prova própria",
  "lacuna": "uma lista de subtítulos que cada um 'prova algo' pode ser tecnicamente completa e ainda assim não ter arco — não há campo que force setup→conflito→resolução nem que confira se as três seções somadas têm dado, narrativa E visual, não só uma ou duas",
  "severidade": "estrutural",
  "patch_proposto": 3
}
```

```json
{
  "artefato": ".claude/agents/critico-editorial.md",
  "tecnica": "três pilares + arco narrativo + 'não abra pela metodologia' + 'não enterre o achado'",
  "estado_atual": "checklist (linhas 15-22) pergunta se a tese aparece cedo, se alguma seção não entrega o prometido, onde o leitor desistiria, o que cortar, e se a voz é consistente — nenhum critério nomeado para os três pilares, para o arco, para abertura por metodologia, ou para achado enterrado no meio do texto",
  "lacuna": "'a tese aparece cedo' é proxy parcial de gancho, mas um rascunho pode passar nesse checklist sendo só narrativa sem dado (ou dado sem sentido) — não há pergunta que force isso à tona. Também não há critério que capture explicitamente um post que abre explicando como o número foi calculado antes de dizer o que ele significa",
  "severidade": "estrutural",
  "patch_proposto": 4
}
```

```json
{
  "artefato": ".claude/skills/revisao-editorial/SKILL.md",
  "tecnica": "fórmula de manchete adaptada + 'não enterre o achado' (checagem final, não correção)",
  "estado_atual": "checklist de consolidação (linhas 17-38) cobre coerência entre etapas, aderência à voz, VERIFICAR pendente, placeholders, antipadrões de IA e frontmatter — item 6 checa só se título/subtítulo estão 'coerentes com o briefing', não se o título é uma manchete forte",
  "lacuna": "nenhum critério avalia se o título final carrega informação específica (vs. título temático genérico) nem se o achado mais forte do post ainda está enterrado no meio do texto depois de toda a revisão — e por design esta skill não pode reabrir estrutura, então o segundo item só pode ser um alarme, não uma correção",
  "severidade": "estrutural",
  "patch_proposto": 5
}
```

```json
{
  "artefato": ".claude/skills/prompts-visuais/SKILL.md",
  "tecnica": "anotação direta no gráfico + revelação progressiva (série densa) + contraste genuíno vs. forçado",
  "estado_atual": "spec de graf-NN (linhas 31-45) exige pergunta única, fonte, dados em CSV, código Plotly com tokens de marca, tipo de gráfico justificado, alt-text — sem menção a add_annotation, sem critério para quando dividir um gráfico de 3+ séries, sem guarda contra forçar um contraste antes/depois onde o conteúdo é conceitual",
  "lacuna": "a regra 'se não couber numa frase, separe em dois graf-NN' já cobre parcialmente o espírito de revelação progressiva para *propósito* empilhado, mas não cobre um gráfico de propósito único com 3+ séries visualmente carregado; anotação e guarda de contraste não têm cobertura nenhuma",
  "severidade": "reforço",
  "patch_proposto": "6+7"
}
```

```json
{
  "artefato": ".claude/agents/verificador-tecnico.md",
  "tecnica": "tratamento de incerteza (faixas e intervalos em vez de ponto único)",
  "estado_atual": "formato de saída (linhas 34-39) só distingue ✅ confirmado, ⚠️ impreciso, ❓ não verificável → [VERIFICAR: ...] — não existe categoria para 'dado confirmado, mas o valor correto é uma faixa, não um ponto'",
  "lacuna": "um número que é genuinamente uma faixa (ex. Selic variou entre X% e Y% no período) apresentado como ponto único no post é uma imprecisão factual que o agente hoje não tem vocabulário para marcar — teria que forçar em [VERIFICAR] (errado, o dado NÃO está pendente de verificação) ou deixar passar como 'confirmado' (errado, esconde a variação)",
  "severidade": "estrutural",
  "patch_proposto": 8
}
```

## Tensões registradas para a `forja-de-voz` (não resolvidas aqui)

1. **Fórmula de manchete adaptada pede número técnico no título; o corpus não confirma essa
   prática.** Os 6 títulos do corpus (`syntaxis_a_ciência_da_separação`,
   `syntaxis_eu_preciso_de_um_assessor_de_investimentos`, `syntaxis_objetivos_classes`,
   `syntaxis_o_simples_funciona`, `syntaxis_tesouro_selic`,
   `syntaxis_títulos_do_tesouro_nacional`) são todos temáticos/conceituais, um deles
   interrogativo — nenhum leva número. A técnica entra no sistema como algo **a testar**, não
   como regra obrigatória (ver patch 1 e patch 5) — se o autor testar em posts reais e gostar,
   vira candidato a regra via `/forja-de-voz atualizar`, com evidência própria.
2. **Arco em seis atos termina em "chamada para ação"; a voz explicativa (§4.2 do guia)
   nunca tem CTA.** Resolvido *dentro* dos patches (2, 3, 4) condicionando o último ato ao
   subgênero — voz ensaística fecha em CTA, voz explicativa fecha em "resolução" (descrição
   do produto) sem forçar chamada. Registrado aqui porque é o tipo de ajuste que só a
   `forja-de-voz` deveria poder tornar regra fixa do guia, não este prompt — os patches
   aplicam a técnica de storytelling num nível abaixo do guia de voz (nos artefatos do
   pipeline), sem tocar `estilo-autoral.md`.

## Nota de escopo

`critico-editorial.md` e `revisao-editorial/SKILL.md` dividem a responsabilidade de "achado
enterrado" de um jeito específico: `critico-editorial` (developmental, etapa 5) é quem PODE
reordenar/cortar, então é lá que o critério vira diagnóstico acionável, com poder de mandar o
texto de volta para a etapa 2. `revisao-editorial` (consolidação, etapa 9) já não pode reabrir
estrutura — lá o mesmo critério vira só um alarme de segurança (se ainda estiver enterrado
nesse ponto, é sinal de que a etapa 5 deixou passar, não algo para a etapa 9 corrigir sozinha).
Isso diverge levemente do mapa do Apêndice B, que sugeria checar a técnica só em
`revisao-editorial` — a divisão em duas camadas com poderes diferentes é mais fiel à própria
regra de camadas do sistema (`pesquisa/frente-c-editoracao.md`) do que colocar tudo num só
lugar.
