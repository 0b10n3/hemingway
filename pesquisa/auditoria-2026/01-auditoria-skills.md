# Fase 1 — Auditoria de skills e subagentes

Metodologia: para cada item, comparei a promessa do arquivo com evidência real em
`posts/2026-08-25-dividir-para-nao-correr-risco/processo/` (post mais recente, único com
laudo completo das etapas 1-7) mais `estado.json`/`git log` para uso operacional. `claude
--version` local = 2.1.251 (README exige 2.1.196+ — atendido). Nenhuma feature de frontmatter
usada além de `disable-model-invocation`, `argument-hint`, `allowed-tools`, `skills:`,
`tools:`, `model:` — todas padrão, nada a `[VERIFICAR]` aqui.

## Veredito resumido

| Item | Veredito | Motivo em uma linha |
|---|---|---|
| `voz-syntaxis` | **manter** | Uso real (06-revisao.md) aplica regras 1/4 do guia com precisão; zero duplicação |
| `marca-syntaxis` | **manter** | Path de 5 hops resolve; alerta corretamente contra posts pré-31/08 como referência |
| `forja-de-voz` | **manter** | Dormência é esperada (3/5 posts desde o bootstrap), não achado |
| `revisao-editorial` | **manter** | Consolida sem re-revisar; nenhum artefato próprio em `processo/`, por design |
| `publicar` | **manter** | A skill em si está correta; o problema é como `post-substack` a invoca (ver abaixo) |
| `post-substack` | **ajustar** | Etapa 10 instrui invocação que o próprio flag de `publicar` recusa — bug real, já documentado em produção |
| `prompts-visuais` | **ajustar** | Resumo inline da etapa 8a descreve o método v1, não o v2 vigente em `briefing-ilustracao.md` |
| `critico-editorial` | **manter** | 05-critica.md bate item a item com o formato prometido; distingue achado de observação corretamente |
| `extrator-de-estilo` | **manter** | Sem uso observável nesta amostra (não roda por post) — spec consistente com `taxonomia-estilometrica.md` |
| `pesquisador-editorial` | **manter** | `03-pesquisa.md` citado como fonte por duas etapas posteriores; erro que introduziu foi pego pela verificação (redundância funcionando) |
| `revisor-gramatical` | **manter** | 06-revisao.md não toca estrutura/fato nenhuma vez; distingue voz de erro (fragmentação, itálico ausente) |
| `verificador-tecnico` | **manter** | Melhor evidência do lote: recalcula fórmula com Python, corrige 3 erros factuais reais, remove `[VERIFICAR]` só quando confirma |

Nenhum item **substituir** ou **aposentar** — nenhuma skill/agente morto, nenhuma
sobreposição de responsabilidade encontrada (a separação developmental/linha/técnica em
critico-editorial/revisor-gramatical/verificador-tecnico está limpa: o item 6 da crítica
estrutural foi corretamente escalado e resolvido só na verificação técnica, sem retrabalho).

---

## Achado 1 — `post-substack` etapa 10 instrui uma invocação que `publicar` recusa

**Evidência real, não hipotética:** `posts/.../estado.json.pendencias` já registra —
> "BLOQUEIO publicação: a skill publicar tem disable-model-invocation: true e recusa ser
> chamada pelo orquestrador — precisa que o autor rode /publicar diretamente"

`post-substack/SKILL.md` linha 86 diz "Aprovar → invoque a skill `publicar`". Mas
`disable-model-invocation: true` existe exatamente para impedir que o modelo dispare uma
skill por conta própria (`CLAUDE.md`: "Toda skill que escreve arquivo ou dispara pipeline
leva `disable-model-invocation: true`") — e `publicar` faz merge, tag e push, a ação de
maior risco do repositório. O flag está certo em `publicar`; o texto errado está em
`post-substack`.

**Proposta (diff, só nesta linha):**

```diff
- Aprovar → invoque a skill `publicar`.
+ Aprovar → informe o autor que a publicação requer `/publicar` manual (a skill tem
+   `disable-model-invocation: true` de propósito — merge, tag e push são ação de alto
+   risco demais para disparo automático).
```

Não requer mudar `publicar` nem `post-substack` além dessa linha — é alinhar a documentação
ao comportamento real e já confirmado, não uma mudança de comportamento.

## Achado 2 — `prompts-visuais/SKILL.md` descreve o método v1 de briefing, não o v2 vigente

Já detalhado na Fase 0: a seção "Etapa 8a" (linhas 39-43) resume "quatro testes de rejeição,
no mínimo três conceitos divergentes" — o método antigo. O arquivo que ela aponta,
`references/briefing-ilustracao.md`, foi reescrito em 31/08/2026 para o motor de três
operações (extensão/cruzamento/torção) com hierarquia de material em três camadas e
critérios positivos de beleza. Como nenhum post rodou essa etapa ainda (achado da Fase 0),
isto não quebrou nenhum post real — mas vai quebrar a primeira vez que alguém seguir só o
resumo inline em vez de abrir a referência.

**Proposta (diff):**

```diff
 ### Etapa 8a — briefing antes do prompt (obrigatório)

 **Nunca vá do texto direto ao prompt.** Rode primeiro o método de
-**`references/briefing-ilustracao.md`** e grave o resultado em
-`processo/08-briefing-visual.md`: colheita de material concreto do post → a frase que a peça
-carrega → no mínimo três conceitos divergentes (justaposição / fusão / substituição) → quatro
-testes de rejeição → escolha com os descartes anotados.
+**`references/briefing-ilustracao.md`** e grave o resultado em
+`processo/08-briefing-visual.md`: colheita de material em três camadas (a metáfora do autor
+primeiro) → a frase que a peça carrega → as três operações geradoras (extensão / cruzamento
+/ torção) → critérios positivos de beleza → testes de rejeição, incluindo o teste da
+fatalidade → escolha com os descartes anotados.
```

Alternativa mais barata a considerar: apagar o resumo inline inteiro e substituir por "ver
`references/briefing-ilustracao.md` — não resumido aqui de propósito, para não haver duas
fontes do mesmo método." Isso elimina a categoria inteira de bug (resumo desatualizado) em
vez de só corrigir a instância atual. Prefiro esta segunda opção, mas registro as duas para
sua escolha.

---

## Ponto em aberto, não decidido — paralelizar etapas 6 e 7?

Evidência real: em `05-critica.md`/`06-revisao.md`/`07-verificacao.md` do post auditado,
nenhuma das duas etapas 6/7 lê o resultado da outra — ambas partem do mesmo
`04-draft-v1.md` já corrigido pela etapa 5, uma por norma/linha, outra por fato. Rodar em
paralelo pouparia uma etapa serial. **Não estou propondo isso**: as duas escrevem no mesmo
arquivo (`04-draft-v1.md`), e paralelizar edição concorrente no mesmo arquivo é risco de
conflito sem ganho medido — não há evidência de retrabalho ou desperdício de tokens no fluxo
atual que justifique a mudança (regra "otimizar ≠ reescrever"). Registro aqui só para você
decidir se quer que eu desenvolva a ideia (ex. cada etapa grava um diff próprio, etapa 9
reconcilia) ou se prefiro deixar como está.

---

**Aguardando aprovação item a item** dos dois achados acima (post-substack linha 86;
prompts-visuais linhas 39-43, com a escolha entre correção pontual ou remoção do resumo) antes
de aplicar qualquer coisa. Nada foi alterado ainda.
