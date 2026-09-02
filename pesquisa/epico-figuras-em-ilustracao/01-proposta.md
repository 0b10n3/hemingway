# Proposta — regra de figura humana em três faixas, e onde a lista de clichês já basta

Resposta ao diagnóstico (`00-diagnostico.md`). Três conclusões de lá já fecham a maior parte
do escopo: a adaptação de referência de cultura pop (pergunta 3 do autor) já está implementada
e não precisa de ajuste; a lista de clichês genéricos de finanças (regra 5) é real, vem de
`brand/DESIGN.md` §4.5 e deve continuar como está; a proibição absoluta de rosto (regra 6) não
tem base em `DESIGN.md` e é o único ponto que precisa mudar. Esta proposta é só sobre esse
ponto.

---

## O que muda

`estilos-ilustracao.md`, regra compartilhada 6, sai de proibição absoluta para **critério em
três faixas**, substituindo:

> 6. Sem figura humana reconhecível. Silhueta abstrata é aceitável; rosto não.

Por uma regra que distingue *quem* está sendo retratado e *por quê*, não só *se* há um rosto.

### Faixa 1 — Figura histórica, sempre permitida

Condições, todas obrigatórias:
- A pessoa é citada pelo nome no corpo do post (post.md, não é decoração externa) —
  material de Camada 2 em `briefing-ilustracao.md` ("objetos concretos do texto"), não Camada 1
  importada de fora.
- A pessoa é reconhecidamente histórica: falecida e com presença padrão em material didático
  ou de referência do próprio campo que o post trata (matemática, economia, finanças) — o
  teste é "esse rosto já aparece em livro-texto ou enciclopédia sem controvérsia", não uma
  data de corte arbitrária de anos. Gauss, Newton, Keynes, Fischer Black (falecido em 1995,
  já nomeado neste próprio corpus) são exemplos claros; um caso limítrofe (falecido há poucos
  anos, ainda socialmente "recente") desce para a Faixa 2 por precaução.
- Tratamento sempre dentro do estilo da linha editorial em uso — nunca fotorrealista. Ver
  "Como desenhar um rosto em cada estilo", abaixo.
- Respeitoso, não caricato, não satírico.

Nenhuma pergunta ao autor é necessária nesse caso — mesmo grau de autonomia que qualquer outro
objeto de Camada 2.

### Faixa 2 — Figura pública viva, discutida no papel profissional específico do texto

Condições, todas obrigatórias, além das da Faixa 1 (nome citado, tratamento não-fotorrealista,
respeitoso):
- A pessoa é pública especificamente na capacidade profissional que o texto discute (ex.: um
  economista citado pelo trabalho acadêmico dele) — nunca a vida pessoal, nunca um contexto
  alheio ao motivo da citação.
- A peça não pode implicar endosso — nada que sugira que a pessoa aprova o post, o produto ou
  a Syntaxis.
- **Vira pergunta nomeada no briefing visual (etapa 8), levada ao gate humano (etapa 10)** —
  mesmo tratamento que a etapa 1 já dá a linha editorial ambígua
  (`post-substack/SKILL.md`, "Etapa 1 — linha editorial é campo obrigatório"): não é
  `[VERIFICAR]` técnico, é decisão que só o autor toma, porque envolve julgamento sobre a
  pessoa retratada que a skill não pode fazer sozinha.

### Faixa 3 — Pessoa privada, nunca

Sem exceção, mesmo que nomeada no texto (ex.: um cliente, um colega, uma fonte anônima de um
post de linha Spoiler). Isso já era implícito na regra antiga; a nova regra deixa explícito
que a Faixa 3 não desaparece — só as Faixas 1 e 2 são novas.

### O que não muda

- Silhueta abstrata continua sempre aceitável, como já era.
- Regra 5 (ilustração genérica de finanças, incluindo robô/cérebro de IA) continua igual —
  não é o alvo desta proposta.
- A doutrina de "evocar a estrutura, nunca reproduzir a propriedade" para referência de cultura
  pop continua igual — já cobre o caso Terminator/robô, que é problema de propriedade
  intelectual e marca, não de retrato de pessoa real.

---

## Como desenhar um rosto em cada estilo

Sem isso, a Faixa 1/2 vira licença para quebrar a disciplina visual que o resto do sistema já
tem — um rosto "normal"/fotorrealista destoaria tanto quanto um gradiente ou um ícone de
biblioteca.

**Estilo A (Spoiler, colagem editorial):** rosto como composição de papel recortado —
formas geométricas simples (elipse, triângulo, faixa) compondo os traços mínimos que tornam a
pessoa reconhecível, mesma disciplina de material das outras peças (corte reto padrão, sombra
chapada sem blur, retícula de meio-tom opcional numa camada, paleta fechada aos tokens). Pensa
em retrato-colagem editorial de revista, não em ilustração de rosto realista.

**Estilo B (Notas de um Professor, desenho técnico esquemático):** rosto como projeção
ortogonal/contorno de linha — traço de espessura constante, sem sombreamento realista, no
mesmo espírito da "linha de construção visível" que já rege o resto do estilo. Pensa em
retrato de manual técnico ou selo postal linear, não em desenho figurativo.

Em ambos os casos, o rosto segue sendo só **um** elemento da composição — as outras regras do
Passo 4 de `briefing-ilustracao.md` (um ponto de tensão só, uma ideia por peça) continuam
valendo; a peça não vira "retrato solto", precisa estar ancorada num conceito do Passo 6, como
qualquer outra `ilu-NN`.

---

## Onde editar

1. **`.claude/skills/prompts-visuais/references/estilos-ilustracao.md`**
   - Corrigir a linha 6–8 ("Derivadas de `brand/DESIGN.md` §4.1, §4.5 e §5") para não incluir
     mais a regra 6 na alegação de proveniência de marca — deixar claro que regras 1–5 e 7 vêm
     de `DESIGN.md`, e a regra de figura humana é critério próprio deste repositório,
     justificado à parte.
   - Substituir a regra 6 pelo critério de três faixas acima, com uma subseção nova
     "Figuras históricas e públicas" (paralela à seção "Hex autorizados") detalhando as três
     faixas e a orientação de estilo por linha editorial.
   - Adicionar, em cada um dos Estilos A e B, uma nota curta de vocabulário ("Como desenhar um
     rosto neste estilo", já redigida acima) na seção de Vocabulário existente.

2. **`.claude/skills/prompts-visuais/references/briefing-ilustracao.md`**
   - Passo 1, Camada 2: acrescentar uma frase reconhecendo que uma pessoa real nomeada no
     texto é objeto de Camada 2 válido, com pointer para o critério de faixas em
     `estilos-ilustracao.md` antes de prosseguir.
   - Passo 6 (Escolha e defesa): quando o conceito envolve rosto de Faixa 2, exigir o registro
     da pergunta nomeada que vai para a etapa 10 — mesmo padrão textual já usado para a seção
     "Proveniência".

3. **Sem alteração em `brand/DESIGN.md`** — confirmado no diagnóstico que a regra antiga nunca
   dependeu dele; nenhuma mudança cross-pipeline é necessária.

4. **Sem alteração em `post-substack/SKILL.md`** — a etapa 8 já é onde a pergunta nomeada
   nasce; só o conteúdo do que pode virar pergunta muda, não o mecanismo.

---

## Teste de aplicação: o que mudaria neste post

Se esta regra já estivesse em vigor durante a etapa 8 de `2026-09-01-quando-os-modelos-se-
rebelam`, `ilu-01` (o radar da rodovia) não muda — não envolve pessoa. Mas ficaria aberta a
possibilidade de uma peça adicional com Fischer Black (Faixa 1 — falecido em 1995, citado pelo
nome na seção "Black–Scholes: o que está na bula") sem precisar de pergunta ao autor; uma peça
com Myron Scholes ou Robert Merton (ambos nomeados, e um deles ainda vivo) cairia na Faixa 2 e
exigiria a pergunta nomeada no gate humano antes de prosseguir. Nenhuma peça nova é proposta
por esta reforma — é só o exemplo de como o critério se aplicaria, para calibrar a regra
escrita.

---

## Iteração 2 (mesmo dia) — unificação dos dois estilos em um só (colagem)

Depois da revisão da regra 6, o autor pediu um passo além: que as ilustrações da linha
**Notas de um Professor** também usassem colagem editorial, em vez do "Estilo B" (desenho
técnico esquemático). Perguntado sobre o escopo — manter a distinção visual entre as linhas
dentro da mesma família de material, ou unificar por completo —, o autor escolheu **unificar
por completo**: aposentar o Estilo B, e as duas linhas passam a ter exatamente as mesmas
regras de ilustração. A distinção editorial (relato vivido vs. conceito explicado) fica só no
texto.

Implementado sem tocar `brand/DESIGN.md` (nunca foi a fonte da distinção de estilo — isso
sempre viveu só em `estilos-ilustracao.md`). O vocabulário técnico do Estilo B (projeção
ortogonal, vista explodida, linha de construção, chamada, cota, simetria) não foi descartado:
virou uma família de **composição** dentro da colagem ("Quando o argumento pede precisão
mecânica", em `estilos-ilustracao.md`) — mesmo material (papel recortado, sombra chapada,
paleta fechada), disposição diferente, para quando a peça precisar mostrar um mecanismo por
dentro. Arquivos ajustados: `estilos-ilustracao.md` (reescrito), `templates-prompt.md`
(templates mesclados), `exemplos-prompts.md` (exemplo do Estilo B marcado como histórico, não
regenerado — post já publicado, `CLAUDE.md` proíbe reescrever visual já publicado),
`prompts-visuais/SKILL.md`, `post-substack/SKILL.md` e `PROJECT_DESCRIPTION.md` (removida a
dependência de linha editorial para decidir estilo — a etapa 8 não bloqueia mais por isso).
