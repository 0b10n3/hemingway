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
