# 05 — Crítica estrutural

Executada pelo agente `critico-editorial`, sobre `01-briefing.md`, `02-estrutura.md`,
`03-pesquisa.md` e `04-draft-v1.md`.

## Achados

**1. Título/subtítulo do draft contradiz o próprio briefing e a proposta editorial da seção 2**
- **Localização:** frontmatter (`título: O Mundo Invertido das Carreiras (em Investimentos)`).
- **Diagnóstico:** o briefing é explícito — este é o post de estreia da linha Spoiler
  (carreira), que retoma a moldura "mundo invertido" mas aplicada a *conhecimento*, não a
  *produto de investimento*. O slug do post é `...carreiras-em-financas`. Ainda assim, o
  título do draft usa "(em Investimentos)", que é exatamente o enquadramento do post anterior
  que a seção 2 está tentando diferenciar ("Da última vez foi sobre qual produto você compra
  primeiro. Dessa vez é sobre qual conhecimento você constrói primeiro"). Um leitor recorrente
  vendo o título antes de abrir o texto recebe o sinal errado sobre o que está prestes a ler —
  o próprio movimento editorial que a seção 2 tenta fazer ("Bem-vindo à linha Spoiler") é
  sabotado pelo título.
- **Severidade:** alta.

**2. O insight mais forte do post está disperso em três formulações diferentes, nenhuma no
gancho/título**
- **Localização:** fim da seção 3 ("o gargalo raramente é a matemática. É o alicerce."), fim
  da seção 4 ("quantas pessoas na sua mesa, agora, sabem rodar o modelo e não sabem explicar
  por que ele existe?"), fim da seção 5 ("O problema nunca foi ter começado pela ponta
  difícil. Foi ter ficado lá, achando que aquilo bastava.").
- **Diagnóstico:** são três candidatas fortes à formulação mais afiada da tese do briefing, e
  nenhuma delas aparece no título, subtítulo ou gancho de abertura — todas estão enterradas no
  fim de parágrafos, em seções distintas e distantes umas das outras. O subtítulo atual não
  carrega a tese de ordem-vs-complexidade que é o argumento real do texto. Por regra do skill
  de técnicas narrativas, achado enterrado é severidade alta e exige voltar à etapa 2 para
  decidir qual formulação ancora subtítulo/título — não basta mover uma frase, é decisão de
  estrutura.
- **Severidade:** alta.

**3. A virada da seção 4 (estagiário de mesa de VaR) é afirmação solta, não ganha pelo texto**
- **Localização:** seção 4, "Não é só quem veio da academia", parágrafo do estagiário.
- **Diagnóstico:** este é o clímax do arco. Mas `03-pesquisa.md` registra explicitamente que
  não foi encontrado estudo, survey ou correspondência exata para esse padrão — só material
  adjacente e anedótico. O draft, no entanto, apresenta a cena do estagiário como fato
  genérico e universal, sem nenhuma âncora em primeira pessoa — diferente da seção 1, que
  ganha credibilidade por ser vivência direta e nomeada do autor. O momento de maior peso
  argumentativo do texto é sustentado por asserção, não por narrativa nem por dado.
- **Severidade:** alta.

**4. Seção 3 concentra três citações institucionais em um parágrafo com registro explicativo,
risco de mistura de voz**
- **Localização:** seção 3, parágrafo "Isso não é impressão minha. Pega o livro-texto...
  Hull... CFA... GFMI...".
- **Diagnóstico:** o parágrafo empilha Hull, CFA e GFMI em sequência rápida, com nomes de
  capítulos e módulos — registro mais próximo da voz explicativa do que da voz ensaística
  declarada no briefing. As frases de abertura e fechamento amarram o parágrafo de volta à
  primeira pessoa, o que evita que o problema seja grave, mas é o ponto do texto onde a
  temperatura ensaística mais cai.
- **Severidade:** média.

**5. Pilar visual da seção 1 (`ilu-01`) não está de fato inserido no draft**
- **Localização:** seção 1 (abertura).
- **Diagnóstico:** `02-estrutura.md` define `ilu-01` como visual da abertura. No draft,
  apenas `graf-01` aparece como placeholder de imagem (seção 3); a seção 1 não tem nenhuma
  marcação de imagem. Pode ser convenção do pipeline reservar isso para a etapa 9 (visuais) —
  mas vale confirmar, porque o checklist de pilares em `02-estrutura.md` já lista os dois
  visuais como parte da prova estrutural, e neste estágio só um está presente.
- **Severidade:** média.

**6. "Não foi só comigo" (seção 2) promete uma generalização que a seção 4 não entrega com
peso equivalente**
- **Localização:** seção 2, frase "Não é falha pessoal, e não foi só comigo."
- **Diagnóstico:** essa frase cria expectativa de prova que só a seção 4 deveria cumprir — e a
  seção 4 entrega apenas asserção (item 3). Decorre diretamente do item 3; resolvido o item 3,
  este se resolve junto.
- **Severidade:** baixa.

**7. A tese do briefing nunca aparece como frase única — está reconstituída por fragmentos em
três seções**
- **Localização:** seções 3, 4 e 5, como listado no item 2.
- **Diagnóstico:** para a voz ensaística isso pode ser intencional (argumento construído por
  acúmulo) — mas, combinado ao item 2, o efeito líquido é que o leitor só recompõe a tese
  completa se ler o texto inteiro até a seção 5.
- **Severidade:** baixa.

## O que funciona (para registro, não é problema)

- O arco em cinco/seis movimentos está bem montado: a cena pessoal (seção 1) e a segunda
  camada pessoal (seção 3) se acumulam antes da generalização (seção 4), como o plano previa.
- O fechamento (CTA do curso) está genuinamente integrado — retoma "valor do dinheiro no
  tempo" da seção 3, não é emenda comercial solta.
- O pilar dado da seção 3 é real e bem verificado (Hull, CFA, GFMI convergem na mesma ordem de
  pré-requisitos) — não é dado inventado nem estatística forçada.
- Nenhuma citação inventada; a pesquisa reportou honestamente onde não achou evidência (seção
  4), e o draft não forçou dado onde não havia — coerente com a regra "evidência ou silêncio",
  só que a ausência de dado na seção 4 se torna problema porque é exatamente a seção que
  carrega o clímax do argumento (item 3).

## Veredito

Três itens de severidade alta (título contraditório, insight mais forte enterrado, virada da
seção 4 não sustentada) — o texto volta à etapa 2 (estrutura) antes de seguir para revisão de
linha, conforme a regra do pipeline.
