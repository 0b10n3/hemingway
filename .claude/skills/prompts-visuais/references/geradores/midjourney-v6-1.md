# Adaptador de gerador — Midjourney v6.1

> **Não-validado.** Nunca testado neste ambiente — validar com uma peça real antes de
> confiar nestes parâmetros. Esboçado a partir de
> `pesquisa/frente-e-visuais/relatorio-design-editorial-ia.md` §5.2, que por sua vez cita
> fontes de terceiros (guias de prompting, comparativos de benchmark) não verificadas por
> este sistema. Gerador ativo hoje é Nano Banana Pro (`nano-banana-pro.md`) — este arquivo só
> existe para o dia em que trocar de gerador for cogitado (ver `prompts-visuais/SKILL.md`,
> B.4 em `pesquisa/frente-e-visuais/02-proposta.md`).

## Quando cogitar este gerador

Segundo o relatório-fonte: aderência de prompt mais maleável que FLUX (preenche lacunas com
autonomia estética), especializado em atmosfera cinematográfica e interpretação de conceitos
abstratos/dramáticos — candidato a peças que priorizem atmosfera sobre precisão literal do
layout. Acesso via Discord/UI proprietária, sem API pública — relevante para decidir se cabe
num pipeline automatizado como este.

## Parâmetros

- **`--style raw`:** remove o verniz estético padrão do modelo — relevante para design
  editorial que não quer o "look" super-processado default.
- **`--stylize` / `--s` (0–1000):** valores baixos (0–200) ancoram em parâmetros fotográficos
  rigorosos; valores altos (acima de 400) induzem interpretação pictórica livre.
- **`--sref` (Style Reference):** referência de estilo via URL — transfere textura, cor e
  atmosfera de uma imagem-fonte sem herdar suas formas. É a capacidade que resolveria a
  limitação registrada em `nano-banana-pro.md` ("sem referência de estilo entre imagens") —
  se este adaptador for ativado, `--sref` é o mecanismo correto para manter múltiplas peças
  do mesmo post na mesma atmosfera exata, em vez da alternativa verbal usada hoje.

## O que NÃO herda deste sistema automaticamente

Regras agnósticas de marca (`estilos-ilustracao.md`: paleta, geometria, hex autorizados,
proibição de glow/gradiente) continuam valendo. `--sref` aponta para uma URL de imagem — se
usado, a imagem de referência precisa vir de um ativo já aprovado deste sistema (ex.: uma
capa já publicada), nunca de uma imagem externa não vinculada à marca; decisão de marca, não
de skill — se chegar a este ponto, seguir a regra de ouro de `marca-syntaxis/SKILL.md`
("se o token que você precisa não existe, pare e pergunte").
