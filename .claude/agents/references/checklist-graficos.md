# Checklist de craft visual — graf-NN

Três critérios adicionais ao spec básico de `graf-NN` (ver `SKILL.md`), extraídos e
filtrados de uma skill de referência de data storytelling corporativo — procedimento
adotado, vocabulário de BI descartado. Origem: `pesquisa/auditoria-storytelling.md`.

## Anotação direta, não só legenda

Todo `graf-NN` com um ponto de interesse específico (um pico, uma virada, o número que a
pergunta do gráfico responde) leva anotação Plotly (`add_annotation`) apontando diretamente
para ele, além da legenda — não em vez dela. Uma legenda genérica obriga o leitor a caçar o
ponto; a anotação entrega o achado.

## Revelação progressiva, quando a série está carregada

Se um `graf-NN` de propósito único (responde a uma pergunta só, já passou no critério da
`SKILL.md`) ainda tem 3 ou mais séries/categorias visualmente competindo, considere dividir
em 2-3 gráficos sequenciais (`graf-NN`, `graf-NN+1`...) que revelam uma camada por vez, em
vez de um único gráfico poluído. Critério é visual (quantas linhas/cores brigando pela
atenção), não temático — não confundir com a regra já existente de separar propósitos
diferentes.

## Contraste genuíno, nunca forçado

Contraste antes/depois só quando há de fato dois estados comparáveis no mesmo eixo (ex.:
preço de um título antes/depois de um choque de juros). Não force um "antes/depois" onde o
conteúdo é conceitual e não tem dois estados reais — um gráfico conceitual mal-encaixado num
molde de contraste é pior que nenhum contraste.

## Gate de Tufte (integridade da forma, não do craft de leitura)

Os três critérios acima (anotação, revelação progressiva, contraste genuíno) tratam de como o
gráfico se lê. Estes tratam de se o gráfico mente:

- **Eixo Y começa em zero para gráfico de barras.** Exceção exige justificativa escrita no
  spec (ex.: série já é uma variação percentual pequena onde zero não é o ponto de
  comparação relevante). Para linha/série temporal, avalie caso a caso: se a amplitude real
  entre as séries é pequena frente ao valor absoluto, o eixo sem zero exagera visualmente a
  diferença mesmo sendo linha, não barra — declare `rangemode="tozero"` como padrão, e
  justifique por escrito a exceção.
- **Lie Factor declarado quando há ênfase visual** (tamanho, cor, área carregando o
  argumento) — fórmula: (variação visual do efeito) ÷ (variação real do efeito nos dados).
  Alvo 0,95–1,05. Fora dessa faixa, redesenhe o encoding.
- **Sem 3D, sombra, textura ou moldura.** Grid mínimo, opacidade baixa.
- **Rótulos adjacentes ao dado**, não só legenda distante — já coberto pela regra de anotação
  acima, citado aqui só para lembrar que os dois testes se reforçam.
- **Dimensão visual ≤ dimensão dos dados** — nunca escalar raio de círculo (área) para dado
  unidimensional; nunca altura de barra 3D fingindo profundidade que não é dado.
- **Small multiples quando ≥3 séries competem visualmente** — mesmo critério que já existe
  em "Revelação progressiva" acima (não duplicar; esta seção só lembra que small multiples é
  a ferramenta formal de Tufte para o mesmo problema que a revelação progressiva já ataca).
