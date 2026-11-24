# Preferências de edição do autor

Gerado por `python3 scripts/diff_edicoes.py preferencias` em 2026-11-24, a partir de 17 posts (`estilo/corpus/edicoes/`). Não editar à mão: a colheita (`/forja-de-voz colher`) regera este arquivo a cada post publicado.

É **dado medido, não regra**: o que o autor mudou entre o `post.md` aprovado e o texto que
publicou. Regra só nasce daqui pela forja (`estilo/estilo-autoral.md`). Use para escrever
(etapa 4) e revisar (etapas 6 e 9) já no rumo em que o autor vai editar. Edições de
tipografia, imagem, CTA e link ficam de fora (são do Substack ou de marketing). A coluna
"Desfaz texto do pipeline" só é medida em edição de palavra; para pontuação e ênfase, ver a
origem por etapa em `pesquisa/epico-revisao-editorial/dados/b1-atribuicao.json`.

| O que o autor faz no site | Vezes | Posts | Spoiler | Notas | Desfaz texto do pipeline |
|---|---|---|---|---|---|
| Divide parágrafo | 173 | 16 | 103 | 70 | 4 |
| Acrescenta negrito | 129 | 15 | 56 | 73 | 13 |
| Troca palavra ou trecho | 107 | 17 | 52 | 55 | 53 |
| Tira aspas simples | 93 | 7 | 19 | 74 | 0 |
| Corta trecho | 63 | 15 | 28 | 35 | 34 |
| Acrescenta itálico | 60 | 12 | 22 | 38 | 1 |
| Tira ou troca travessão | 37 | 8 | 10 | 27 | 0 |
| Muda outra pontuação | 28 | 10 | 11 | 17 | 0 |
| Reescreve subtítulo (H2) | 26 | 12 | 10 | 16 | 7 |
| Corta dado ou trecho de conteúdo que o pipeline trouxe | 23 | 10 | 7 | 16 | 10 |
| Acrescenta trecho | 23 | 8 | 12 | 11 | 0 |
| Reescreve subtítulo do post | 8 | 8 | 2 | 6 | 0 |
| Junta parágrafos | 5 | 1 | 0 | 5 | 1 |
| Reescreve título | 4 | 4 | 2 | 2 | 0 |
| Tira itálico | 3 | 3 | 1 | 2 | 1 |

## Exemplos

### Divide parágrafo
- `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`: «caso de liquidação ou intervenção no banco emissor.» ¶ «A cobertura reduz o risco para o valor»
- `2026-09-01-quando-os-modelos-se-rebelam`: «de ferramentas e modelos matemáticos fundamentais em finanças.» ¶ «Um dos meus momentos favoritos do curso é»

### Acrescenta negrito
- `2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro`: «emitido por uma instituição financeira» em «…um título de renda fixa 'emitido por uma instituição financeira', que representa uma promessa…»
- `2026-09-28-o-certificado-nao-muda-o-devedor`: «títulos» em «…do Agronegócio (CRA) são títulos de renda fixa emitidos por uma…»

### Troca palavra ou trecho
- `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`: «nomear» → «perceber», em «…segunda, que demorei mais para [[…]] , era mais básica ainda.…»
- `2026-08-25-dividir-para-nao-correr-risco`: «leu» → «viu», em «…. Na prática, o mercado [[…]] a resolução como resposta direta a…»

### Tira aspas simples
- `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`: «'» → «∅», em «…ao Consumidor Amplo) com um [[…]] spread 'prefixado. O risco…»
- `2026-08-25-dividir-para-nao-correr-risco`: «'» → «∅», em «…primeira coisa que pergunto não é [[…]] quanto rende '. É:…»

### Corta trecho
- `2026-10-12-coqueiros-e-cacaueiros`: «no programa» → «∅», em «…em 2025, a ser mentor [[…]] de carreira da ANBIMA (Associação…»
- `2026-11-13-should-i-stay`: «e a» → «∅», em «…que você considera inútil ou nocivo [[…]] obrigação de conviver com gente de…»

### Acrescenta itálico
- `2026-09-01-quando-os-modelos-se-rebelam`: «smile» em «…passou a exibir o famoso 'smile' (ou 'skew'…»

### Tira ou troca travessão
- `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`: «—» → «,», em «…de maturidade realizado pelas instituições " [[…]] o processo pelo qual um banco…»
- `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`: «—» → «,», em «…ruim) não pede matemática avançada [[…]] pede só "entender conceitos financeiros…»

### Muda outra pontuação
- `2026-08-10-o-mundo-invertido-dos-investimentos`: «[» → «∅», em «…funciona por aqui, link abaixo [[…]] LINK: post sobre Tesouro Selic…»
- `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`: «]» → «∅», em «…O Mundo Invertido dos Investimentos " [[…]] : o mundo invertido, o…»

### Reescreve subtítulo (H2)
- `2026-09-28-o-certificado-nao-muda-o-devedor`: «50» → «chão», em «…. Quando o preço vai a [[…]] Em julho de 2026, os…»
- `2026-08-10-o-mundo-invertido-dos-investimentos`: «Bem-vindo ao mundo invertido» → «∅», em «… [[…]] Imagine a cena: você compra…»

### Corta dado ou trecho de conteúdo que o pipeline trouxe
- `2026-08-25-dividir-para-nao-correr-risco`: «1º de» → «∅», em «…autorizadas pelo Banco Central. Desde [[…]] julho de 2025 (Resolução BCB…»
- `2026-10-15-renda-fixa-condicoes-variaveis`: «(art. 163, § 8º)» → «∅», em «…aos créditos que o plano abrange [[…]] . Em 2023, os agentes…»

### Acrescenta trecho
- `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`: «∅» → «como exemplo», em «…do preço de outro ativo) [[…]] para a dissertação. Eu sabia…»
- `2026-09-11-partes-dificeis-de-uma-carreira-em-financas`: «∅» → «um bom», em «…slide. Nenhum desses hábitos rende [[…]] post de LinkedIn. Todos eles…»

### Reescreve subtítulo do post
- `2026-09-28-o-certificado-nao-muda-o-devedor`: «CRI, CRA e o que a securitização realmente separa» → «Debênture disfarçada ou título do agro?»
- `2026-09-18-o-agro-e-pop-o-agro-e-produto-financeiro`: «O risco do financiamento ao agronegócio fica com o banco — não com quem compra a LCA.» → «Transformando produção agrícola em produto financeiro.»

### Junta parágrafos
- `2026-08-10-o-mundo-invertido-dos-investimentos`: «variável de verdade, com exposição ao risco bem» ¶ «maior que qualquer coisa de renda fixa.»

### Reescreve título
- `2026-08-17-o-mundo-invertido-das-carreiras-em-financas`: «O Mundo Invertido das Carreiras» → «O Mundo Invertido das Carreiras em Finanças»
- `2026-09-28-o-certificado-nao-muda-o-devedor`: «O Certificado Não Muda o Devedor» → «A anatomia e o verdadeiro risco do CRA»

### Tira itálico
- `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos`: «.» em «…Professor — primeira nota da série. O dinheiro que o banco não…»
