# Etapa 9 — Consolidação

**Montagem:** o orquestrador gerou `post.md` sobre `04-draft-v2.md`, aplicando as decisões do autor:
- `06-revisao.md`: os 47 itens, inclusive o 38. O item 26 ficou de fora, porque o S1 devolveu o
  referente a "Isso desmonta".
- `07-verificacao.md`: B1, B2, I1, I3, I4, I5 e I6. O I2 entrou na versão de 365 dias. O I7 não entrou.
- S1: o parágrafo do cartão foi para o fim de "Rende todo dia", aberto pela ponte "Tudo isso vale a
  14%." no lugar de "A 14%.".
- S3: o subtítulo foi para `subtitulo:` no front-matter. Também entraram `resumo:`, `status:
  em-revisao`, as tags do post anterior, o LaTeX em `$$` e o disclaimer padrão.

**Conferência do agente `revisao-editorial`: nenhuma edição em `post.md`.**
- As decisões aplicadas são essas, e só essas.
- Os números batem com `07-verificacao.md`, com o registro de cálculo
  (`_revisoes/2026-11-09_…_calculo.md`) e com os CSVs.
- Os alt-texts batem com as figuras.
- Cada glosa aparece uma vez, na primeira ocorrência.
- Os 10 itens do checklist de voz estão ok.
- A Ficha de Saída é entregue.
- Bibliografia: 4 itens, 3 livros.
- Há 2 `[VERIFICAR]` visíveis (Hull e Maor) e nenhum `[FAIXA]`.

**Sincronização feita pelo orquestrador depois da conferência (observação 3):** o alt-text e a
legenda do graf-01 em `graficos.md` (l. 264, 267, 272) receberam a mesma redação do item 11
("capital de 1 aplicado a 100% ao ano, ao longo de um ano"; "2; 2,25; 2,44 e 2,61"). O rodapé
dentro da figura (l. 194, "Capital 1 a 100% ao ano") não mudou, porque mudá-lo obriga a regenerar
a imagem. Isso fica para o gate.

## Observações para o gate (julgamento, não aplicadas)

1. **"Tudo isso vale a 14%."** Essa ponte não estava nas aprovações. "Tudo isso" agora cobre também o
   argumento do CDI, que vale para qualquer taxa. Alternativa: "Os degraus da escada encolhem assim
   a 14%." Também dá para manter.
2. **"12 × 15,3%, ou 183,5%".** Feita à mão, a conta dá 183,6%. O valor exato é 12 × 15,29% = 183,53%.
   Alternativas: "12 × 15,29%" ou "cerca de 183,5%".
3. **Rodapé da figura do graf-01.** Diz "Capital 1 a 100% ao ano". Regenerar só se quiser a
   redação do item 11 também na imagem.
4. **Glosas de baixa prioridade.** "ln" (logaritmo natural), "opções" antes da glosa indireta,
   "fatorial" e "binômio de Newton".
5. **Itens já na pauta:** M3 (subtítulo com a tese); os dois `[VERIFICAR]` (Hull: a alternativa sem
   fonte é "trabalha em taxa contínua e mostra a conversão entre as etiquetas"); S4 (linkar "A Corda
   e o Arco" na primeira menção); por que o credor prefere cotar a nominal (etapa 7, sem bloqueio).
6. **Lie Factor declarado em `graficos.md`.** Os eixos começam um pouco abaixo da base: 0,96 no
   graf-01 e 13,9% no graf-02. No graf-02 o fator real fica perto de 0,92, o que atenua o efeito e
   não exagera. Não bloqueia. O ajuste seria começar o eixo exatamente na base ou corrigir o valor
   declarado.
