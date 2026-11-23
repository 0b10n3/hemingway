---
name: distribuicao
description: Regras por peça, formato de textos.md, exemplos reais e o esquema do kit.json da etapa Distribuição (esteira v2) de um post da Syntaxis. Pré-carregada pelo subagente redator-distribuicao (skill /distribuir); não use na conversa principal.
user-invocable: false
---

Material de referência dos subagentes da distribuição. Este arquivo só diz o que existe e quando
ler. As regras moram em `referencias/`; os números (peças, datas, limites), em `config/esteira.yaml`.

## A etapa em uma frase

Depois que o autor aprova o post no gate, a distribuição escreve as peças da esteira v2: Notes do
Substack, o post do LinkedIn (só *Spoiler*) e as legendas do vídeo e do carrossel. Ela nunca altera
o post. A meta é trazer assinantes para o Substack, e o público são profissionais do mercado
financeiro, céticos em relação a hype.

## Quando ler cada arquivo

| Arquivo | Ler quando |
|---|---|
| `config/esteira.yaml` | Sempre. Diz que textos cada peça tem, os limites de caracteres e a URL de inscrição |
| `referencias/regras-pecas.md` | Antes de escrever qualquer texto |
| `referencias/exemplos.md` | Sempre, antes do primeiro texto. São casos reais, bons e ruins |
| `referencias/kit.schema.json` | Não precisa. O `kit.json` é escrito só pelo `scripts/kit.py`; o esquema é o contrato com o `../uther-pendragon` |

## O que o validador reprova (`scripts/kit.py validar`)

Ele roda logo depois de você, e o kit reprovado volta para você uma vez. Antes de entregar, confira:

- cabeçalhos de `textos.md` intactos: um bloco por texto, nenhum faltando, repetido ou inventado;
- texto acima do limite do canal (`{{URL_POST}}` conta como 80 caracteres);
- texto que não termina com uma pergunta (exceto o título do Shorts); o link pode vir depois,
  sozinho na última linha;
- Note D0 e post do LinkedIn sem `{{URL_POST}}`; Note D+2 com URL; legenda do Instagram com URL;
- URL que não seja `{{URL_POST}}` nem a página de inscrição do config;
- emoji; hashtag (hoje, zero em todos os canais);
- número que não está no post nem em `../../strategy/FEAR.md` ou `GREED.md` (vírgula e ponto
  normalizados);
- menção a oferta do catálogo que não está disponível (FVDT, isca, cursos, o brinde em produção).

O validador não vê voz, gancho repetido entre peças, número citado sem a fonte que o post dá nem
recomendação de ativo. Isso é com você.
