# Etapa 2 — Estrutura

Linha Spoiler — sem Ficha de Saída de backward design (isso é exclusivo de Notas de um
Professor, ver `docs/BACKWARDS_DESIGN.md`).

## Seções e o que cada uma prova

| # | Subtítulo | O que prova | Ato do arco |
|---|---|---|---|
| 1 | Fortalecer a Lombar é uma Droga | Instala a analogia física: treino chato ≠ treino vistoso, mas é o que sustenta o resultado a longo prazo | Setup |
| 2 | O Objetivo Escolhe o Fardo | Transpõe a analogia para carreira: o difícil certo depende do objetivo, não é genérico; introduz o caso concreto (base quant vs. modelo pronto) | Setup → conflito |
| 3 | Evitar o difícil frequentemente torna tudo mais difícil | Framework de decisão (Dor A vs. Dor B) — ferramenta prática, não só narrativa | Conflito |
| 4 | Dificuldades com significado | A cadeia de Peterson (responsabilidade → dificuldade → competência → contribuição → significado), com exemplos concretos de estudo | Conflito → resolução |
| 5 | Nem toda dificuldade vale a pena | Contrapeso: nem todo sofrimento é produtivo; fecha a tese ("não é porque eu sofri...") e abre CTA + ponte para o próximo post | Resolução |

## Três pilares

- **Dado:** fraco de propósito nesta linha (Spoiler é relato, não dado duro) — a única
  afirmação quantificável é a crítica ao VaR mal implementado ligada à crise de 2008
  (checar na etapa 7/verificação, linha Spoiler cobre isso via checagem de citação/caso, não
  por ser Notas de um Professor).
- **Narrativa:** pilar dominante — analogia física sustentada do início ao fim, vivência
  pessoal do autor (base quant).
- **Visual:** ver abaixo.

## Visual — critério, não gosto

1. Série numérica real a comparar? Não há — nenhum dado quantitativo em série no texto.
   Descarta `graf-NN`.
2. Relação estrutural entre entidades sem métrica central? **Sim** — a cadeia de Peterson
   (responsabilidade → dificuldade → competência → contribuição → significado, seção 4) é
   exatamente isso: cinco nós em sequência causal, sem número por trás. → **`diag-01`**.
3. Info-NN? Não se aplica — uma peça isolada (`diag-01`) já carrega a síntese sozinha; não há
   dado disperso que precise de leitura conjunta.
4. Metáfora/analogia sem peça visual dedicada? A analogia central (lombar/core) tinha, no
   rascunho original, uma sugestão de ilustração (`ilu-01`, registrada como tensão na etapa
   1) — este pipeline não produz mais essa peça; fica em prosa.

**Decisão:** um único visual, `diag-01`, para a cadeia de Peterson.

## Revisão (retorno da etapa 5 — severidade alta)

A crítica estrutural (`05-critica.md`) encontrou dois achados de severidade alta:

1. **Seção 5 subdesenvolvida** — o contrapeso "nem toda dificuldade vale a pena" tinha duas
   frases sem apoio, exatamente onde a pesquisa (etapa 3) reuniu material aproveitável
   (crítica de Credé ao "grit", viés de sobrevivência, "culpar a vítima"). **Correção
   estrutural:** a Seção 5 ganha um parágrafo extra incorporando esse material — não é ajuste
   de frase, é conteúdo novo que faltava na seção.
2. **Registro determinístico em série** (seções 1, 2 e 4 — "garante", "consequência
   mecânica", "a maioria não percebe") sem hedge suficiente ao longo do corpo, só recuando
   tarde no fechamento. **Correção estrutural:** cada uma dessas três afirmações passa a
   trazer o hedge no próprio parágrafo onde aparece (não só no fechamento) — decisão de
   estrutura, não de palavra isolada, porque afeta o registro do texto inteiro, não um ponto.

Voltando para a etapa 4 com essas duas correções — não é reescrita do zero, é redistribuição
de ênfase e adição de conteúdo já pesquisado e não usado.
