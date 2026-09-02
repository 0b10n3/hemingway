# Diagnóstico — figuras humanas em ilustração, e a utilidade da lista de clichês

Criado em 2026-09-01, a partir de um pedido direto do autor durante o gate humano do post
`2026-09-01-quando-os-modelos-se-rebelam`: por que o sistema recusou a sugestão de capa
("rebelia de máquinas humanoides como nos filmes de Terminator")? A resposta levantou duas
perguntas maiores, que o autor pediu para investigar: (1) o sistema consegue ilustrar um post
com o rosto de uma figura histórica (ex.: Gauss)? (2) a lista de "clichês proibidos" ainda faz
sentido do jeito que está, e o fluxo já sabe adaptar uma referência de cultura pop (como
Terminator) sem violar direito de terceiros?

Cada achado cita arquivo e trecho, seguindo a regra do `CLAUDE.md` ("Evidência ou silêncio").

---

## 1. A pergunta 3 (adaptar referência de cultura pop sem violar direito) já está resolvida

Antes de propor qualquer coisa nova aqui, vale registrar o que **já existe e já funcionou**:
o caso concreto que motivou a pergunta do autor — a sugestão de Terminator para a capa deste
mesmo post — é literalmente o exemplo de referência usado para documentar o método em
`.claude/skills/prompts-visuais/references/briefing-ilustracao.md`, linhas 54–61 ("Aproveitar
a estrutura... Caso real: o post `2026-09-01-quando-os-modelos-se-rebelam` recebeu a sugestão
'uma rebelia de máquinas humanoides como nos filmes de Terminator' para a capa — a referência
foi descartada..., mas a estrutura... foi levada adiante").

O método inteiro — três saídas obrigatórias (aproveitar estrutura / aproveitar literal /
descartar), seção "Proveniência" exigida no Passo 6, e a doutrina geral em "Referência de
cultura pop: evocar a estrutura, nunca reproduzir a propriedade" (linhas 201–213, citando
diretamente a regra já usada para texto em `CLAUDE.md`: "Amostras alheias são fonte de
procedimento, não de frase") — já existe e já foi aplicado com sucesso neste post específico.
Isso veio do épico anterior (`pesquisa/epico-rascunhos-e-colagem/`, commit `812f578` "exige
veredito de proveniencia e alternativa propria em ilustracao").

**Conclusão do item 1: nenhum ajuste novo é necessário aqui.** O fluxo já é capaz de pegar uma
ideia como "Terminator" e adaptá-la sem violar direitos — é exatamente o que a capa deste post
fez. O que falta não é capacidade, é o autor saber que ela existe (resolvido por esta própria
conversa, e reforçado apontando para o método já documentado).

## 2. A pergunta 1 (figura histórica/pública, tipo Gauss) esbarra numa regra que não tem base

`estilos-ilustracao.md`, "Regras compartilhadas (valem para os dois estilos)" (linha 27–29),
abre dizendo: "Derivadas de `brand/DESIGN.md` §4.1, §4.5 e §5 — não são opinião desta
referência." A regra 6, especificamente (linha 44): **"Sem figura humana reconhecível.
Silhueta abstrata é aceitável; rosto não."**

Fui conferir a fonte alegada. `brand/DESIGN.md` §4.5 ("Anti-padrões — a lista do 'feito por
IA'", linhas 250–264) lista dez itens proibidos — grid de três cards, hero centralizado
genérico, cinzas de framework, cantos arredondados, gradiente/glow/glassmorphism, emoji como
ícone, sombra como recurso principal, progressão uniforme de fonte, espaçamento uniforme, "**
Ilustração genérica de 'finanças' (moedas, cifrões, candlestick, robôs/cérebros de IA)**", e
ocorrência de Amber/Cream. Busquei o documento inteiro (`grep -in "figura humana\|rosto\|face\|
retrato"`) e não há **nenhuma** menção a figura humana, rosto ou retrato em `DESIGN.md` — nem
em §4.1 (paleta), nem em §4.5 (anti-padrões), nem em §5 (padrões geométricos).

**Achado central: a regra 6 de `estilos-ilustracao.md` não deriva de `DESIGN.md`, apesar de
estar debaixo do cabeçalho que diz que deriva.** É uma regra inventada pela camada hemingway,
razoável como precaução geral (evita o sistema gerar retrato de gente real sem critério), mas
sem o lastro que a introdução do arquivo alega, e absoluta demais: bane até o uso editorial
legítimo de uma figura histórica cujo rosto é diretamente relevante ao argumento do texto (ex.:
um post que cita Carl Friedrich Gauss ao explicar a distribuição normal, ou — caso real deste
próprio corpus — um post que já nomeia Fischer Black, Myron Scholes, Robert Merton e Peter
Kempthorne/Choongbum Lee).

**Conclusão do item 2: é seguro revisar a regra 6 sem tocar em `brand/DESIGN.md`** (o arquivo
compartilhado por todo o ecossistema Syntaxis, fora deste repositório) — porque a restrição
nunca esteve lá. O ajuste é local, dentro de `estilos-ilustracao.md`.

## 3. "Robô/cérebro de IA" (regra 5) é diferente — essa sim vem de `DESIGN.md`, e deve ficar

Ao contrário da regra 6, a regra 5 ("Sem ilustração genérica de finanças... robô/cérebro de
IA", `estilos-ilustracao.md` linha 42–43) **é** citação quase literal de `DESIGN.md` §4.5,
linha 263: "Ilustração genérica de 'finanças' (moedas, cifrões, candlestick, robôs/cérebros de
IA)". Essa é regra de marca real, compartilhada por todo o ecossistema Syntaxis (produto,
curso, marketing — não só este pipeline), e existe por um motivo de mercado documentado: robô/
cérebro-de-IA genérico é hoje o sinal visual mais rápido de "conteúdo gerado por IA sem
cuidado" — o oposto do que a marca quer comunicar (`DESIGN.md` linha 87, "IA como ferramenta,
não como enfeite").

Isso não conflita com a pergunta do autor sobre Terminator: a resposta certa nunca foi "gerar
o robô", foi "extrair a estrutura da ideia e descartar o robô literal" — que é exatamente o
que o item 1 já mostrou que o sistema faz.

**Conclusão do item 3: a lista de clichês em si (regra 5) segue útil e não deve ser
enfraquecida** — ela protege contra um problema real e documentado, e é a mesma lista que vale
para o resto do ecossistema Syntaxis, não uma opinião isolada deste repositório.

## 4. Risco real de afrouxar a regra 6 sem critério: retrato de gente comum, sátira, uso indevido de imagem

Se a regra 6 simplesmente cair ("agora pode rosto"), o sistema ganha um risco novo que hoje não
existe: gerar retrato de uma pessoa viva e comum (não pública), ou um retrato satírico/
constrangedor de uma figura pública, ou usar a semelhança de alguém para o que pareceria um
endosso não autorizado. Nenhuma dessas hipóteses é aceitável, e nenhuma delas é o que o autor
pediu (ele pediu Gauss — uma figura histórica, morta há quase dois séculos, cujo rosto é
material didático padrão em qualquer livro-texto de estatística).

O ajuste certo não é "remover a regra 6", é **trocar uma proibição absoluta por um critério
com faixas de segurança claras** — histórico/já falecido e diretamente citado no texto é o
caso mais seguro; figura pública viva, discutida no papel profissional específico que o texto
aborda, é o caso intermediário que precisa de critério explícito; pessoa privada nunca entra,
sob nenhuma hipótese. Isso é o assunto do documento de proposta (`01-proposta.md`).

## 5. Fora do escopo deste diagnóstico

`graf-NN`/`diag-NN` (código Plotly, sem geração de imagem por IA) não têm o problema descrito
aqui — não geram retrato de ninguém. O épico anterior (`epico-rascunhos-e-colagem`) já resolveu
proveniência de referência cultural e vocabulário compositivo; este diagnóstico não repete esse
trabalho, só confirma (item 1) que ele já cobre a pergunta 3 do autor.
