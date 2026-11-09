# Exemplos reais

Tirados dos posts publicados. Cada exemplo mostra o trecho real e o item de parecer
correspondente. Eles mostram o raciocínio, não um gabarito: não copie frases daqui para
outro post.

## 1. CTA bom: o autor já fez, o parecer só completa

Post `2026-10-30-du252-contagem-de-dias` (Notas de um Professor), penúltimo parágrafo do corpo:

> Se este texto te poupou uma conta errada, encaminhe para quem está começando na mesa. E me
> conte, nos comentários, a pior pegadinha de calendário que você já encontrou.

Por que é bom: o pedido de compartilhamento nomeia quem recebe ("quem está começando na
mesa") e o benefício concreto ("te poupou uma conta errada"); a pergunta ao leitor é
específica do tema. Não há urgência nem promessa. O parecer não reescreve isso. Registra na
evidência que o CTA de conversa existe e propõe só o botão nativo que falta ali:

```json
{"id": "C4", "papel": "secundario", "tipo": "comentar", "formato": "botao_nativo",
 "ancora": "Se este texto te poupou uma conta errada",
 "destino_id": "substack:comentar",
 "motivo": "O autor já pede a pior pegadinha de calendário nos comentários; o botão logo depois transforma o pedido em clique."}
```

## 2. CTA ruim: oferta que não existe mais

Post `2026-08-17-o-mundo-invertido-das-carreiras-em-financas` (Spoiler), seção "Um Convite
para Você":

> Se você quer assistir, o cadastro é gratuito: [LINK: formulário de cadastro — curso
> Fundamentos do Valor do Dinheiro no Tempo].

Por que seria reprovado hoje:

- o curso gratuito ao vivo no YouTube saiu do roteiro (`strategy/DECISOES_2026-11.md`,
  decisão 8); o FVDT virou curso pago, `em produção`, e não é `citavel` no catálogo;
- a chamada promete data ("a partir de setembro"), e uma promessa de entrega com prazo é
  exatamente o que o funil evita (FUNIL §3.4, sem pré-venda);
- o link é placeholder, e o destino não tem URL.

O que o parecer faz num caso assim: não propõe CTA para o curso. Registra em `riscos[]` que o
texto anuncia uma oferta indisponível e propõe como `principal` o que está disponível no
estágio (Skill Check), se houver gancho no texto. Se não houver, só os botões de inscrição.

## 3. Link interno bom: a menção que o autor já faz

Post `2026-10-15-renda-fixa-condicoes-variaveis` (Notas de um Professor), abertura:

> No texto sobre o CRI e o CRA (Certificado de Recebíveis do Agronegócio), escrevi que o CRA
> de devedor único é, economicamente, uma debênture com isenção de Imposto de Renda (IR)...

O autor já aponta para o texto anterior; falta só o link. O texto do link sai da própria
âncora, descreve o destino e não acrescenta palavra ao post:

```json
{"id": "R1", "ancora": "No texto sobre o CRI e o CRA",
 "texto_link": "texto sobre o CRI e o CRA",
 "destino_id": "post:2026-09-28-o-certificado-nao-muda-o-devedor",
 "pergunta_do_leitor": "Que texto? Onde está a explicação de por que o CRA de devedor único é uma debênture?"}
```

E o caminho de volta. O post antigo termina com um exercício que já fala de debênture; é ali
que o leitor de 09-28 pergunta "e a debênture, como funciona?":

```json
{"id": "B1", "origem_id": "post:2026-09-28-o-certificado-nao-muda-o-devedor",
 "ancora_na_origem": "uma debênture da Raízen Energia",
 "texto_link": "uma debênture da Raízen Energia",
 "motivo": "Mesmo cluster (crédito privado); o 10-15 é o pilar e explica a debênture que o exercício do 09-28 pede para comparar."}
```

## 4. Contraste: link ruim

Num post sobre LCA, sugerir no fecho "Leia mais sobre renda fixa aqui" apontando para o
pilar. Três problemas: o texto é genérico ("leia mais", "aqui"); o leitor não tem, no fecho,
a pergunta que o destino responde; e a frase é nova, quando o próprio post já menciona o CDB
no corpo, onde o link caberia sem palavra extra.

## 5. Nenhuma sugestão é resposta válida

Post `2026-09-01-quando-os-modelos-se-rebelam` (Spoiler). O cluster
`modelos-e-risco-de-modelo` só tem este post. As referências do texto são externas (MIT
OpenCourseWare, Derman, MacKenzie), e o catálogo não tem nada que responda a uma pergunta do
leitor neste ponto. Forçar um link para um post de carreira ou de renda fixa só porque
existe seria ruído. No parecer:

```json
"referencias": [],
"backlinks_sugeridos": []
```

O `marketing.md` mostra "Nenhuma sugestão." nas duas seções. Os CTAs de inscrição continuam
obrigatórios.
