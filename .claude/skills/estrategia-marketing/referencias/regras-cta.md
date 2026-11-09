# Regras de CTA

Os limites abaixo (1 principal, até 2 secundários) são **regra deste projeto**, aprovada pelo
autor em 2026-11-09, não dado de mercado. Mudar exige mudar também `LIMITES` em
`scripts/parecer.py`.

## Papéis

| papel | Quantos | O que é |
|---|---|---|
| `inscricao` | 2: um no primeiro quarto e outro no fim | Botão nativo de inscrição do Substack (`substack:inscrever`). O guia de lançamento do Substack recomenda um botão no primeiro quarto do post, e a central de ajuda recomenda botão em todo post |
| `principal` | 0 ou 1 | O próximo passo coerente com o estágio do funil. Hoje, em geral, o Skill Check (`oferta:skill-check`) ou o post-pilar do cluster |
| `secundario` | 0 a 2 | Compartilhar, comentar, responder ao e-mail. Só onde o texto já cria o gancho (uma pergunta ao leitor, um "se isso te poupou uma conta") |

## Formato

- `botao_nativo`: botões do Substack (inscrever, compartilhar, comentar). Não viram texto no
  `post.md`; o autor insere à mão no editor, e o `marketing.md` lista o parágrafo.
- `texto`: uma ou duas frases em prosa, que o autor pode colar. Se o destino tem URL, marque
  em `texto_link` o trecho que vira link (descritivo, nunca "clique aqui").

## Onde e o quê

- A âncora é o trecho literal depois do qual o CTA entra. O CTA entra como parágrafo novo,
  depois do parágrafo que contém a âncora. Escolha uma âncora curta e única.
- *Spoiler* tende a convidar à conversa (comentário, resposta ao e-mail). *Notas de um
  Professor* tende ao próximo passo técnico (Skill Check, post-pilar). É ponto de partida, não
  regra fixa.
- Voz explicativa (`estilo/estilo-autoral.md` §4.2) não fecha com CTA em prosa. Nela, o CTA
  em texto só entra se o autor aceitar no gate: prefira os botões nativos, que não são prosa.
  Se o post já tem um CTA do autor, não proponha outro igual. Aponte o existente na
  evidência e proponha só o que falta.
- Antes de propor "comentar", lembre que nem todo post aceita comentário de leitor gratuito.
  Registre isso em `riscos[]` quando o CTA principal depender de comentário.

## Proibido

- CTA para oferta que não seja `citavel: true` no catálogo (isca, FVDT e cursos futuros estão
  em produção ou congelados). Menção editorial sem link só a pedido do autor, e não pelo parecer.
- Contagem regressiva, escassez artificial, "últimas vagas", "só hoje" (MARKETING §11).
- Promessa de resultado financeiro, de salário ou de promoção (FUNIL §1).
- Emoji, exclamação de vendedor, imperativo em sequência ("Inscreva-se já! Compartilhe!").
- Número que não esteja no post ou em FEAR.md, GREED.md ou PRICE_TAG.md.

## Texto sugerido na voz do autor

Português do Brasil, "você", frases curtas, sem negrito. Na voz ensaística, o fecho do autor
pede compartilhamento de forma específica ("mande esse texto pra alguém que está prestes a
comprar o primeiro par de tênis"), nunca genérica ("compartilhe com seus amigos"). Se não
couber nada na voz, não sugira.
