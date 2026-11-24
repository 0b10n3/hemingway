# Infográficos — "A Peça Mais Simples"

## Alternativa ao `graf-01`: info-01 (Copom × taxa prefixada, com os episódios)

*Enquanto o autor não escolhe no gate, este cabeçalho não começa por `info-01`, para o
`scripts/checar_post.py` não cobrar placeholder. Se o `info-01` for o escolhido, o cabeçalho volta a
ser `## info-01 — …` e o placeholder `info-01` entra no `post.md` no lugar do `graf-01`.*

**Status:** alternativa, não decidida. O autor pediu na nota do rascunho "incluir um infográfico"
(marcador M2); pelo critério da etapa 2 a peça é o `graf-01` (tensão T2 em
`processo/02-estrutura.md`). Em 2026-11-23 o autor pediu as duas versões: o gráfico, em
`graficos.md`, e o prompt para gerar este infográfico no Claude web. No gate, entra uma das duas no
lugar do placeholder; não as duas.

**Por que pode valer como infográfico:** o gráfico sozinho mostra o padrão, mas o "porquê" de cada
episódio (eleição, Lehman, rebaixamento, corte e alta antecipados, pacote fiscal) só cabe em texto
ao lado. A versão em infográfico lê a série e os sete cartões juntos, e acrescenta a faixa "Como
ler" (expectativa + prêmio de prazo), que no post fica em prosa na seção "A aposta escondida na
taxa".

**Produção:** fora do padrão Plotly desta pasta, por decisão do autor. O infográfico é gerado no
Claude web (canvas) com o prompt de `graficos/info-01-prompt-claude-web.md`, que traz os dados, os
textos, os tokens e as regras. O autor exporta o PNG e o salva em `figuras/info-01.png`.

**Hierarquia de leitura:**
1. Manchete: "A taxa prefixada anda antes do Copom e salta sem ele", e a linha de apoio, que faz o
   papel da legenda das séries.
2. O gráfico de 2002 a 2026 (meta Selic em degrau; taxa prefixada de 1 ano), com sete episódios
   numerados.
3. Os sete cartões, na mesma numeração: out/2002, out/2008, set/2015, out/2016, mar/2021, dez/2024,
   out/2026, cada um com etiqueta de tipo (salta sem o Copom, anda antes do Copom, anda antes e
   salta).
4. A faixa "Como ler a taxa prefixada".
5. O rodapé com a fonte.

**Dados e fonte:** os mesmos do `graf-01` (`graficos.md`, bloco "Dados"): Banco Central, SGS 432 e
SGS 7806; Tesouro Nacional, Tesouro Transparente; cálculo próprio para a interpolação de 1 ano. O
prompt usa as versões enxutas `graficos/dados/graf-01-semanal.csv` (1.299 semanas, com o dia exato de
cada episódio) e `graficos/dados/graf-01-meta-selic.csv` (140 mudanças da meta). Os números dos
cartões saem da série diária e de `processo/03-pesquisa.md`, item 5 (datas do Copom; S&P em
9/9/2015, Agência Brasil; pacote fiscal em 27/11/2024). A faixa "Como ler" se apoia no boxe do
Banco Central (Relatório de Inflação, dez/2022), item 6 do mesmo laudo. A etapa 7 confere os
números dos cartões se esta versão for a escolhida.

**Tokens** (de `../../brand/tokens/syntaxis.tokens.json`, valores copiados no prompt porque o Claude
web não lê o repositório): `color.neutral.chalk` #F7F7F5, `color.neutral.ink` #141414,
`color.neutral.slate` #4A5568, `color.neutral.mist` #E2E8F0, `color.neutral.mint` #E6F4EE,
`color.neutral.white` #FFFFFF, `color.grove.500` #2D9E67, `color.forest.500` #1B6A45;
`typography.fontFamily` display (Montserrat), body (Source Sans 3), data (IBM Plex Mono). Sem `lime`.
Cantos retos, nenhuma sombra (`brand/DESIGN.md` §10 e §11).

**Alt-text (para o placeholder `info-01`, se escolhido; 121 caracteres):**

> Linha da taxa prefixada de 1 ano e cartões de sete episódios, de 2002 a 2026: a taxa anda antes do Copom e salta sem ele.

**Conferência depois de gerar:** comparar o PNG com `figuras/graf-01.png` (a forma da linha tem de
ser a mesma, com a lacuna de 2023 e o pico de 2002 perto de 33%); conferir que os sete números dos
cartões e os textos são os do prompt; nenhum travessão, nenhuma cor fora da lista.
