# Exemplos reais

Tirados dos posts publicados. Eles mostram o raciocínio, não um gabarito: não copie frases daqui
para outro post. Os posts da avaliação (`evals/distribuicao/`) ficam de fora de propósito.

## 1. Note D0 boa (*Notas de um Professor*, `2026-10-30-du252-contagem-de-dias`)

```text
Uma LTN comprada a 12% ao ano, com liquidação no primeiro dia útil de 2026, vence em 1º de janeiro de 2027. Levada até lá, entrega 11,85% no período.

Ninguém errou a conta. 2026 tem 249 dias úteis, e a taxa da LTN vale para cada 252.

Qual foi a primeira conta sua que não bateu com a tela da mesa por causa do calendário?
{{URL_POST}}
```

Por que funciona:

- O gancho é a abertura do próprio post, quase literal: um enigma numérico (regra 7 do guia).
  Nenhuma frase de efeito nova.
- Uma ideia só: a taxa vale para cada 252 dias úteis, não para cada ano do calendário. A régua e o
  motor ficam para o texto.
- Todo número está no post, e a conta é do próprio texto.
- A pergunta só tem resposta para quem já trabalhou numa mesa, que é o público, e a resposta vem da
  experiência dele.
- O link vem sozinho na última linha, depois da pergunta.

## 2. Note D+2 boa (*Spoiler*, `2026-10-12-coqueiros-e-cacaueiros`): a lição em três linhas, sem link

```text
O coqueiro, símbolo do litoral baiano, chegou de fora, segundo a Embrapa. Hoje se planta quase sozinho.
Na carreira, a pergunta que importa não é de onde uma skill veio. É quanto ela custa para continuar dando fruto.
Qual skill sua já dá fruto sem pedir esforço todo dia?
```

Por que funciona:

- A segunda linha é a tese do post, literal («a pergunta que importa não é de onde uma *skill*
  veio. É quanto ela custa para continuar dando fruto»).
- Vale sozinha: quem não leu o texto entende e consegue responder. Por isso não leva link.
- O fato histórico mantém a fonte que o post dá (Embrapa). Compare com o exemplo 3.
- A metáfora central do texto aparece (regra 12), mas a pergunta sai dela para a experiência do
  leitor.
- O ângulo é outro que o da Note D0 do mesmo post, que abriria pela cena da viagem ou pelo erro do
  autor («Aí fui checar. Errei nas duas pontas.»).

## 3. Gancho ruim (real), com o motivo

A `nota_substack` que o pipeline gerou para `2026-10-12-coqueiros-e-cacaueiros` (frontmatter do
`post.md`):

```text
O coqueiro chegou à Bahia em 1553 e hoje ninguém lembra que é imigrante. Algumas skills funcionam assim.
```

Três problemas:

- **O número perdeu a fonte.** No post, 1553 vem com «Segundo a Embrapa». Na nota, a data vira
  afirmação do autor. A consolidação (`processo/09-consolidacao.md`) apontou isso, e a verificação
  registrou que não há documento de época para 1553. O validador não pega, porque 1553 está no
  post. Quem pega é você.
- **A segunda frase anuncia em vez de entregar.** «Algumas skills funcionam assim» é teaser
  (antipadrão §7.2 do guia): promete uma ideia e não diz qual.
- **Não termina com pergunta.**

Para contraste, um gancho construído (não é do autor) que o público cético descarta na primeira
linha:

```text
Você está perdendo dinheiro todo dia sem saber! 9 em cada 10 profissionais erram essa conta. Leia agora 👇
```

Urgência falsa, número inventado, exclamação, emoji e promessa. O validador reprova o número e o
emoji; o resto é com você.

## 4. Legenda de carrossel (real), boa até a última linha

Legenda do LinkedIn do carrossel de `coqueiros-e-cacaueiros`, feita na rodada 5 da marca
(`brand/SOCIAL/gerador/conteudo/coqueiros-e-cacaueiros.json`):

```text
A sua melhor nota pode estar mentindo para você.

É comum tirar a nota mais alta justamente na disciplina de que você menos gosta: o medo da recuperação faz você estudar muito mais para ela. A nota mistura afinidade e esforço, e não diz quanto veio de cada um.

No mercado, o boletim muda de nome: avaliação de desempenho, meta batida, mérito. A armadilha é a mesma, só que mais cara. E o terreno está mudando: o Fórum Econômico Mundial estima que 39% das skills essenciais dos trabalhadores vão mudar até 2030 (Future of Jobs Report 2025).

No documento: a diferença entre coqueiros (skills que entregam valor com pouca energia) e cacaueiros (as que pedem cultivo deliberado), quatro passos para encontrar os seus e três cacaueiros que valem o plantio agora no mercado financeiro.

Texto completo no link do post.
```

O que está certo: o gancho é o subtítulo do post e cabe antes do "ver mais"; o número vem com a
fonte que o post dá; o quarto parágrafo diz o que o leitor encontra no documento; não há promessa.

O que a esteira v2 muda é o fim. A legenda termina com uma pergunta, e o link vai sozinho na última
linha:

```text
(… os quatro primeiros parágrafos, sem mudança …)

O texto completo está no link abaixo. Em que disciplina você tirou a nota mais alta estudando por medo, e não por gosto?
{{URL_POST}}
```
