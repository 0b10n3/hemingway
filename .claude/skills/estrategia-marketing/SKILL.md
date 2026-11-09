---
name: estrategia-marketing
description: Rubrica, regras de CTA e de links internos e exemplos do parecer de marketing de um post da Syntaxis. Pré-carregada pelo subagente estrategista-marketing (etapa 9a do post-substack); não use na conversa principal.
user-invocable: false
---

Material de referência do subagente `estrategista-marketing`. Este arquivo só diz o que
existe e quando ler. As regras moram nos arquivos de `referencias/`.

## O que é o parecer

Três partes, todas sugestões que o autor aceita ou recusa item por item no gate (etapa 10):

1. **Alinhamento à estratégia:** diagnóstico (segmento, eixo, estágio, cluster) e a rubrica.
2. **CTAs:** onde, qual chamada, por quê.
3. **Referências internas:** links deste post para outros conteúdos do catálogo e
   backlinks: posts antigos que devem passar a apontar para este.

O parecer nunca reescreve o post. O texto sugerido (CTA, frase com link) é curto, opcional
e na voz de `estilo/estilo-autoral.md`.

## Quando ler cada arquivo

| Arquivo | Ler quando |
|---|---|
| `referencias/rubrica.md` | Antes de preencher `alinhamento[]`. Uma linha por critério |
| `referencias/regras-cta.md` | Antes de propor qualquer CTA |
| `referencias/regras-links.md` | Antes de propor referências e backlinks |
| `referencias/esquema.json` | Antes de escrever `marketing.json`. É o formato exato que o validador cobra |
| `referencias/exemplos.md` | Sempre. São casos reais dos posts publicados, bons e ruins |

## O que o validador reprova (scripts/parecer.py)

Ele roda logo depois de você, e o parecer reprovado volta para você uma vez. Antes de
entregar, confira:

- `ancora` copiada literalmente do post e única nele (procure com Grep antes de usar);
- todo `trecho` do diagnóstico, da rubrica e dos riscos copiado literalmente;
- `destino_id` existente em `marketing/catalogo.json` com `citavel: true`, e nunca o próprio post;
- no máximo 1 CTA `principal`, 2 `secundario` e 4 referências; inscrição no primeiro quarto e no fim;
- texto de link descritivo, nunca "clique aqui", "aqui", "leia mais", "saiba mais", "este link";
- nenhum emoji; nenhum número em texto sugerido que não esteja no post ou em
  `../../strategy/FEAR.md`, `GREED.md` ou `PRICE_TAG.md`.
