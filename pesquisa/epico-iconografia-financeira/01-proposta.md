# Proposta — remoção da regra 5 (iconografia financeira) e confirmação da regra de figuras

Resposta ao diagnóstico (`00-diagnostico.md`). Duas mudanças pedidas pelo autor; uma exige
edição, a outra já está satisfeita pelo sistema atual.

---

## Parte 1 — pessoas públicas e históricas: já resolvido, sem ação necessária

O pedido "usar imagens de pessoas públicas e históricas devem ser permitidas" já está coberto
pela regra de três faixas criada em `pesquisa/epico-figuras-em-ilustracao/` (2026-09-01,
`estilos-ilustracao.md`, seção "Figuras históricas e públicas"):

- **Faixa 1 (histórica, falecida)** — sempre permitida, sem pergunta ao autor.
- **Faixa 2 (pública viva, no papel profissional específico do texto)** — permitida, com
  pergunta nomeada no gate humano (mesmo mecanismo que já existe para linha editorial
  ambígua).
- **Faixa 3 (pessoa privada)** — nunca, sem exceção.

Este épico não altera essa regra. A Faixa 2 mantém o gate humano por um motivo específico —
evitar que a peça implique endosso da pessoa retratada ao post, produto ou à Syntaxis — que é
independente da questão de iconografia financeira e não foi contestado no pedido original.

## Parte 2 — iconografia financeira genérica: remover a regra 5

### O que muda

`estilos-ilustracao.md`, regra 5 ("Sem ilustração genérica de finanças") é **removida**, não
substituída. As regras seguintes são renumeradas (6→5 figura humana, 7→6 geometria reta) e o
parágrafo de proveniência no topo de "Regras" passa a listar 1, 2, 3, 4 e 6 como derivadas de
`DESIGN.md`, com um parágrafo novo de "Revisão de 2026-09-02" registrando a remoção como
divergência deliberada de `brand/DESIGN.md` §4.5, só para este repositório. (Já aplicado nesta
sessão — ver diff em `estilos-ilustracao.md`.)

Itens que deixam de ser banidos por nome: moeda, cifrão, candlestick, cofre, aperto de mão,
robô/cérebro de IA, prédio de banco, gráfico de pizza. Confirmado com o autor: a lista cai
inteira, não só os três itens citados no pedido original (robô, moeda, candlestick) — ver
`00-diagnostico.md` para o raciocínio de por que a divergência é defensável neste contexto
específico (ilustração editorial, não UI de produto).

### O que não muda

- **`brand/DESIGN.md` §4.5 continua igual.** A lista de anti-padrões "feito por IA" segue
  valendo para o resto do ecossistema Syntaxis (produto, curso, marketing). Não é um repo git
  a partir daqui, e mesmo que fosse, este épico não propõe mudar a fonte compartilhada — só
  documentar que hemingway diverge dela conscientemente para ilustração de post.
- **Referência de cultura pop continua proibida como objeto literal** (`briefing-ilustracao.md`).
  Um robô genérico passa a ser permitido; um robô identificável de uma franquia específica
  (Terminator, WALL-E, R2-D2) continua proibido por propriedade intelectual, não por marca —
  extrai-se a estrutura, descarta-se o elemento literal, como já documentado no caso real deste
  próprio corpus (`briefing-ilustracao.md`, linhas 54–61).
- **Testes de rejeição e "metáfora de dicionário" continuam valendo** (`briefing-ilustracao.md`,
  Passo 5 e "Erros recorrentes"). Um candlestick ou moeda usado como decoração solta, sem
  função de argumento na peça, ainda reprova — não mais por estar numa lista de objetos
  banidos por marca, mas pelo mesmo motivo que qualquer clichê de banco de imagens reprova.
- **Todo o resto do vocabulário de colagem editorial continua igual**: paleta fechada, sem
  glow/gradiente, lime como acento único, sem texto renderizado, geometria reta.

### Onde foi editado

1. **`.claude/skills/prompts-visuais/references/estilos-ilustracao.md`**
   - Removida a regra 5 antiga.
   - Renumeradas as regras 6→5 (figura humana) e 7→6 (geometria reta).
   - Corrigido o parágrafo de proveniência ("Regras 1, 2, 3, 4 e 6...").
   - Acrescentado o parágrafo "Revisão de 2026-09-02" registrando a remoção e apontando para
     este épico.

2. **Sem alteração em `briefing-ilustracao.md`** — o sistema de rejeição de clichê e a
   doutrina de referência de cultura pop já cobrem os casos que a regra 5 antiga também
   cobria, por outro caminho (ver "O que continua valendo" no diagnóstico).

3. **Sem alteração em `brand/DESIGN.md`** — fora do escopo deste repositório e desta tarefa;
   divergência documentada, não sincronizada.

4. **Sem alteração em `post-substack/SKILL.md`** — nenhuma etapa do pipeline dependia do texto
   específico da regra 5; a etapa 8 continua chamando `estilos-ilustracao.md` como está.

### Teste de aplicação

Um post futuro sobre opções financeiras poderia agora usar um candlestick como objeto de
Camada 2 — por exemplo, um candlestick de papel recortado cuja mecha se rasga exatamente no
ponto de virada que o parágrafo descreve, seguindo a mesma disciplina de "estranhamento de
objeto comum" (`briefing-ilustracao.md`, Passo 4) que já rege qualquer outro objeto. O que
continuaria reprovando: um candlestick genérico e decorativo, sem função de argumento — isso
reprova no teste da troca e em "metáfora de dicionário", exatamente como reprovaria qualquer
outro clichê hoje.
