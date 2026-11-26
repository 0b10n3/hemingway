# Regras por peça (esteira v2, aprovada pelo autor em 2026-11-23)

Peças, datas e limites estão em `config/esteira.yaml`. Aqui ficam o que cada texto faz e por quê.

## Valem para todo texto

- **A voz é do autor** (`estilo/estilo-autoral.md`). Uma peça de rede social não muda isso.
  Parágrafo curto, frase curta como virada, dois-pontos como articulador, "você", sem exclamação
  (regras 1, 2 e 6). Um texto curto e sóbrio vale mais que um gancho com cara de hype. Por quê: o
  público é cético, e a voz é o ativo da marca. Uma peça que soa como social media queima as duas.
- **O gancho sai do próprio texto**, de preferência uma frase literal do post: a abertura, a tese,
  a virada. Você não escreve frase de efeito nova. Por quê: a peça promete o texto; se o gancho não
  está lá, o leitor que clica se sente enganado.
- **Uma ideia por texto, e um ângulo diferente em cada peça.** A Note D0 não repete o gancho da
  D+2 nem o da legenda. Por quê: o mesmo leitor vê as peças da semana; repetir é ruído.
- **Termina com uma pergunta que o público responde com a própria experiência** ("Qual foi a
  primeira conta sua que não bateu por causa do calendário?"). Nunca uma pergunta de sim ou não
  ("Faz sentido?") nem uma retórica que o próprio texto responde. Por quê: é regra da esteira; a
  pergunta convida quem se reconheceu no texto a falar, e é nessas respostas que o autor gasta a
  janela de retorno. Exceção: o título do Shorts.
- **O link vem sozinho na última linha, depois da pergunta.** `{{URL_POST}}` é o marcador; o
  script troca pela URL depois da publicação. Nunca escreva a URL do post à mão.
- **Nenhum número novo.** Só número que está no post, e com a fonte que o post dá a ele (se o post
  diz "segundo a Embrapa", a peça também diz). Sem emoji, sem hashtag, sem negrito.
- **Conformidade.** A Syntaxis é educação, não recomendação. Nenhuma peça sugere comprar, vender
  ou escolher um ativo ou um emissor específico. Pelo manual da ANBIMA para finfluencers, um aviso
  de "não é recomendação" não basta. Citar um emissor como caso didático, como o post faz, pode.
- **CTA só para o que o catálogo marca como disponível** (`marketing/catalogo.json`, `citavel:
  true`). O brinde de assinatura está em produção: enquanto não estiver disponível, nenhuma peça o
  menciona. Sem urgência falsa, sem promessa de resultado financeiro, de salário ou de promoção.
- **As duas linhas são independentes.** Uma peça do *Notas* não aponta para o *Spoiler*, e
  vice-versa.

## Note D0 (dia da publicação, as duas linhas)

- A primeira frase é o gancho, tirado do texto. Uma ideia só.
- Termina com a pergunta; `{{URL_POST}}` na linha seguinte.
- Até 600 caracteres (regra do projeto). Na prática, de 2 a 4 parágrafos curtos.

## Note D+2 (sem link, as duas linhas)

- Tem valor por si só: quem não leu o post entende e responde. Por isso não leva link.
- *Notas de um Professor*: um número ou uma ideia do texto, com a fonte que o post já cita.
- *Spoiler*: a lição, em até 3 linhas, contando com a pergunta.
- Até 600 caracteres (regra do projeto).

## Post no LinkedIn (*Spoiler*, D+2)

- Texto nativo, na voz do autor, contando a história ou a lição do *Spoiler*. Não é resumo do post:
  é a cena e a virada, para quem nunca vai abrir o Substack.
- As duas primeiras linhas carregam o gancho, porque o LinkedIn corta o texto em "ver mais".
- O link do post vai no próprio texto (`linkedin.link_no_post`), sozinho na última linha.
- Até 3.000 caracteres (limite da plataforma), mas mire bem menos: de 5 a 10 parágrafos curtos.

## Legendas do vídeo e do carrossel

Uma por canal, como o config manda. O gancho fica na primeira linha. Termina com a pergunta.

| Canal | O que a legenda faz | Link |
|---|---|---|
| `instagram` (carrossel) e `instagram-reels` (vídeo) | 2 a 4 frases: o gancho, o que a peça resolve, o convite (`brand/SOCIAL.md` §11) | nunca na legenda: escreva "link na bio" |
| `linkedin` (carrossel e vídeo) | 3 a 6 parágrafos curtos com o argumento e a fonte dos números (`SOCIAL.md` §11). No carrossel, diga o que o leitor encontra no documento | `{{URL_POST}}` ou a página de inscrição (`assinatura.url_inscricao`), sozinho na última linha |
| `youtube-shorts-titulo` | o gancho em até 100 caracteres, sem pergunta obrigatória | — |
| `youtube-shorts-descricao` | 1 a 3 frases sobre o vídeo e a pergunta | — |

A legenda do vídeo não repete a fala: diz do que o vídeo trata e convida para o texto. A do
carrossel não repete os slides.

O convite para assinar é um pedido simples ("O texto completo está na Syntaxis, a newsletter."), sem
oferta de brinde enquanto ele não estiver disponível.

## Roteiro do vídeo D+1 (Fatia C)

Quem escreve a **fala** é o `redator-distribuicao`, em `distribuicao/video/roteiro.md`. Quem escreve a
**direção visual** (cartões, zoom, capa) é o `diretor-visual`, em `distribuicao/video/storyboard.json`.
A montagem é do `../spielberg`, que só lê. Limites: `config/esteira.yaml` → `video`. Validador:
`scripts/storyboard.py`.

### Linguagem popular e cativante (definição operacional)

| | É | Não é |
|---|---|---|
| **Popular** | palavra do dia a dia; sigla traduzida na primeira vez ("a LTN, o título prefixado do Tesouro") ou trocada pelo nome que o público vê no app ("Tesouro Prefixado"); número traduzido para o bolso ("10 mil reais viram 13.405"); frase de até ~12 palavras, uma ideia por frase; voz ativa; "você" | gíria forçada; simplificação que fica errada; perder o rigor |
| **Cativante** | gancho nos 3 primeiros segundos com uma tensão ou pergunta concreta, tirada da frase mais forte do post; uma virada no meio; troca visual a cada poucos segundos (cena, cartão ou zoom); fecho com uma pergunta que o público responde e o convite | urgência falsa; promessa de ganho; "ninguém te conta isso"; emoji; clickbait; os anti-padrões do `AUDIENCES.md` §5 |

Teste: um estagiário entende na primeira escuta, e um gestor sênior não torce o nariz. A fala segue o
`estilo-autoral.md`, adaptado à fala: frase curta, primeira pessoa quando for opinião ou método. Nunca
invente história pessoal do autor. Antítese "não é X, é Y" no máximo uma vez (a tese).

Uma imagem que o público já conhece (uma gangorra, uma obra de preço fechado) explica melhor que o termo
técnico. O termo vem depois, uma vez, com a tradução ("o mercado chama isso de prêmio de prazo").

**Regra do número na tela:** todo número que aparece num cartão precisa ser **falado** e estar no post.
O spielberg confere contra a transcrição e reprova o render. Número que não é falado sai do cartão.

### Formato do `roteiro.md` (teleprompter)

- Uma frase por linha. `[pausa]` = meio segundo de silêncio.
- Tomadas `## T1 · <bloco> (~N s)`, cada uma com até 20 s de fala (`video.tomada_max_s`), para o autor
  repetir a tomada inteira se errar.
- Duração total dentro de `video.duracao_alvo_s`, estimada a `video.palavras_por_s`.
- Termina com o convite ("O texto completo está na Syntaxis, a newsletter.") e a pergunta.

### O `storyboard.json`

- `tomadas[].fala` copia literalmente as linhas do `roteiro.md` (sem `[pausa]`).
- Cada cena ancora em dois trechos **literais** da fala da tomada (`ancora_inicio`, `ancora_fim`).
  Nunca em segundos: os tempos saem da transcrição no spielberg.
- Cartão: `sobreposto` (caixa sobre a câmera) ou `cheio` (tela inteira); chassi do `brand/SOCIAL.md` §6.
  Texto + destaque até `video.cartao_palavras_max`. Um cartão por vez.
- `numeros[]` lista cada número do cartão com a fonte: trecho literal do post.
- `post.data_video`: `python3 scripts/storyboard.py data <slug>` (vem do kit.json). Nunca à mão.
- `estrategia`: segmento, eixo e estágio do `marketing.json`.

## Formato de `textos.md`

O `scripts/kit.py montar` cria o arquivo com um cabeçalho por texto, já com o ID e na ordem das
datas. Você escreve só o corpo, logo abaixo de cada cabeçalho:

```markdown
## N1 · note-d0 · substack-notes

Texto da Note, em parágrafos curtos.

Pergunta final?
{{URL_POST}}

## N2 · note-d2 · substack-notes

…
```

- Não mude, não apague nem acrescente cabeçalho. IDs: `N` para Note, `P` para post do LinkedIn,
  `L` para legenda.
- Nada além do texto que o autor vai colar: sem comentário, sem título, sem "Sugestão:".
- No mini-gate, reescreva só os blocos dos IDs que o autor pediu.
