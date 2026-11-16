# Fase E — Avaliação antes × depois

2026-11-16. Protocolo escrito ao fim da Fase D; os resultados entram nas seções 4 e 5 conforme
as medições acontecem. Script: `scripts/avaliar.py` (com teste).

## 1. O problema do vazamento, declarado

O prompt do épico previa testar nos posts de 30/10, 02/11, 09/11 e 13/11, desde que a Fase D não
os usasse como evidência. **A Fase D usou os quatro.** Eles entraram:
- nas extrações e na agregação que sustentam o guia v2.0.0;
- nos pares reais de `voz-syntaxis/references/antipadroes.md` e `exemplos-pareados.md`;
- no registro `estilo/preferencias-de-edicao.md`.

Não existe outro corte retrospectivo limpo: todo post publicado entrou no corpus. Por isso a
avaliação tem duas partes, com pesos diferentes.

| Parte | O que mede | Limpa? | Peso na decisão |
|---|---|---|---|
| A. Prospectiva | Os próximos posts publicados, medidos pela colheita contra a linha de base dos 16 posts | sim | decide |
| B. Retrospectiva | Reexecução do pipeline novo nos 4 rascunhos de teste, contra o publicado | não | testa a mecânica (travessão, parágrafo, ênfase, marcadores), não a generalização |

## 2. Métricas

- **Principal:** quanto o autor edita. É a similaridade por palavra `post.md`→site e o número de
  edições de estilo por mil palavras, que é o custo de edição do CIPHER. Menos edição é melhor.
- Distância nas métricas de forma (parágrafo, travessão, negrito, itálico, perguntas, aspas)
  entre o `post.md` e o site.
- Construções "— não / — a / — o" por mil palavras, da lista calibrada da B2.
- Bloqueantes e avisos do `checar_post.py`.
- Sobrevivência no site do texto escrito nas etapas 9 e 10 (meta do P6: ≥ 92%). Medida pela
  B1 (`python3 scripts/diagnostico_edicoes.py atribuicao`) quando houver posts novos.
- CTA e alt-text: botões aceitos que aparecem no site; imagens com alt-text no site.
- Juiz pareado cego (seção 3.B.4) e teste cego com o autor (3.B.5).

**Linha de base** (16 posts, até 2026-11-16, de `python3 scripts/avaliar.py prospectivo`):
similaridade `post.md`→site com mediana de 0,964 (faixa de 0,847 a 0,994); edições de estilo com
mediana de 16,8 por mil palavras (faixa de 1,8 a 62,1). Outras referências: sobrevivência das
etapas 9 e 10 de 89% e 80%; 0 de 48 imagens com alt-text; 0 de 5 botões aceitos colocados;
10 marcadores no `post.md` aprovado.

## 3. Como rodar

### A. Prospectiva (a cada post publicado)

1. Publique o post normalmente.
2. `/forja-de-voz colher <slug>` (captura, tripla, preferências, checagem do publicado).
3. `python3 scripts/avaliar.py prospectivo` — compara o post novo com a linha de base.
4. Registre o resultado na seção 4. Decisão depois de **3 posts** publicados com o pipeline novo.

### B. Retrospectiva (uma vez, numa sessão nova)

As skills e os agentes editados só carregam numa sessão nova. Abra-a dentro do repositório:

```bash
cd ~/Projects/Syntaxis/pipelines/hemingway
git worktree add ../hemingway-eval -b eval/fase-e epico/revisao-editorial-2026-11
cd ../hemingway-eval && claude
```

Na sessão nova, para cada um dos 4 rascunhos (`_arquivo/drafts/` de 30/10, 02/11, 09/11, 13/11):

1. Copie o rascunho para `evals/editorial/<slug>/rascunho.md`, trocando só o `slug:` do
   frontmatter para `<slug>-eval`. Não edite o original em `_arquivo/`.
2. Rode `/post-substack evals/editorial/<slug>/rascunho.md`. As decisões do autor são
   simuladas por esta regra fixa, a mesma para os quatro:
   - tensões da etapa 1: manter o que o rascunho diz;
   - bloqueantes da 5a: "manter como está", registrado;
   - etapa 6: aceitar `norma` e as `linha` marcadas com ★;
   - 9a: o parecer não é aplicado, porque fica fora da medida de texto;
   - etapa 10: aprovar só com zero bloqueante e resolver cada marcador cortando o trecho.
3. Ao fim, mova `posts/<slug>-eval/` para `evals/editorial/<slug>/` com `git mv`.
4. `python3 scripts/avaliar.py retro <slug> evals/editorial/<slug>/post.md`.
5. **Juiz pareado cego (P9).** Para cada post, sorteie 8 pares de trechos equivalentes, antigo ×
   novo, com o mesmo trecho do rascunho. Monte duas rubricas a partir do guia v2: o §9 e
   `estilo/preferencias-de-edicao.md`. Rode o juiz nas duas ordens e conte a vitória só quando ela
   vale nas duas. Use dois juízes: um subagente Claude e `/agy:ask` (outra família de modelo).
   Para o autoviés, compare também a crítica da etapa 5 rodada pelo `critico-editorial` e via
   `/agy:ask`, contando quantos achados de cada uma coincidem com edições reais do autor naquele
   post.
6. **Teste cego com o autor.** Os mesmos pares, sem rótulo e em ordem aleatória. O autor escolhe.
   A escolha dele vale mais que a dos juízes.

## 4. Resultados — prospectiva

| Post | Similaridade post.md→site | Edições de estilo por mil | Bloqueantes no aprovado | Alt-text no site | Botões aceitos colocados |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

## 5. Resultados — retrospectiva

Pendente: depende da sessão nova (seção 3.B).

## 6. Critério de decisão

- **Fica:** a mudança cuja métrica melhora na prospectiva, nos 3 primeiros posts, sem regressão
  nos bloqueantes.
- **Reverter:** item cuja métrica não se moveu, ou piorou, em 3 posts. Isso vale em especial
  para o teto da antítese (regra 20) e para o checklist enxuto da consolidação.
- **Autoviés (P9):** trocar o modelo da crítica ou do juiz só se o modelo de outra família
  coincidir mais com as edições do autor nos 4 posts da retrospectiva **e** nos posts da
  prospectiva.
