# Adaptador de gerador — FLUX 1.1 Pro (Black Forest Labs)

> **Não-validado.** Nunca testado neste ambiente — validar com uma peça real antes de
> confiar nestes parâmetros. Esboçado a partir de
> `pesquisa/frente-e-visuais/relatorio-design-editorial-ia.md` §5.1, que por sua vez cita
> fontes de terceiros (guias de prompting, comparativos de benchmark) não verificadas por
> este sistema. Gerador ativo hoje é Nano Banana Pro (`nano-banana-pro.md`) — este arquivo só
> existe para o dia em que trocar de gerador for cogitado (ver `prompts-visuais/SKILL.md`,
> B.4 em `pesquisa/frente-e-visuais/02-proposta.md`).

## Quando cogitar este gerador

Segundo o relatório-fonte: aderência de prompt mais alta que Midjourney em benchmark
declarado (T2I-CompBench, `[VERIFICAR: número 82,4% citado pelo relatório, fonte terciária]`)
e renderização tipográfica in-image mais confiável — candidato a peças que precisem de texto
ou rótulo renderizado dentro da imagem (este sistema hoje proíbe texto embutido por regra de
marca, `estilos-ilustracao.md` regra 4 — só relevante se essa regra mudar) ou mockups/
infográficos com layout técnico preciso.

## Estrutura de prompt

Gramática fotográfica sequencial, granularidade decrescente: sujeito principal → ambiente
contextual → restrições de iluminação direcional → especificações técnicas de objetiva (ex.:
"shot with 85mm lens, f/2.8") → determinantes de atmosfera e resolução final.

## Parâmetros

- **`guidance_scale`:** faixa de equilíbrio profissional citada pelo relatório: 2,5–3,5.
- **`inference_steps`:** 40–50 para resolução máxima sem degradação de retorno.
- **Proporção nativa:** RoPE (Rotary Positional Embeddings) permite proporções personalizadas
  sem a distorção clássica de reenquadramento — inclui 4:5 e 1.91:1 nativamente, segundo o
  relatório.
- **Prompt Upsampling:** modo de API para enriquecer descrições escassas — não teria função
  aqui, já que o briefing (`briefing-ilustracao.md`) já produz descrição rica antes do prompt.

## O que NÃO herda deste sistema automaticamente

Regras agnósticas de marca (`estilos-ilustracao.md`: paleta, geometria, hex autorizados,
proibição de glow/gradiente) continuam valendo — a camada condicional aqui é só sintaxe de
chamada. Negative prompt (se o FLUX suportar) não é regra deste sistema por padrão — este
sistema usa enquadramento positivo por decisão de marca, não por limitação do Nano Banana
Pro; reavaliar se um adaptador novo justificar a mudança.
