# Etapa 9: Consolidação

**Montagem:** o orquestrador gerou `post.md` sobre `04-draft-v2.md`, aplicando as decisões do autor
(`estado.json`, "aprovacoes"):
- `06-revisao.md`: as 8 `norma` (2, 8, 15, 23, 25, 27, 28, 37) e as 21 `linha` com ★ (1, 5, 9, 11,
  13, 14, 16, 18, 19, 20, 22, 24, 26, 29, 30, 31, 32, 33, 34, 35, 36). As 8 sem ★ (3, 4, 6, 7, 10,
  12, 17, 21) ficaram de fora.
- `07-verificacao.md`: C1 a C12, sem a C1-alt. A C5 entrou no alt-text curto do diag-02 e na
  legenda de `diagramas.md`. A C12 tirou o `[VERIFICAR]` da abertura.
- Onde as duas etapas tocam a mesma frase, as correções foram combinadas: 6.18 com C2, 6.25 com C6,
  6.34 com C11. A 6.16 é a própria C10.
- Alt-texts: os curtos de `diagramas.md` (123 e 119 caracteres). As legendas longas ficam lá.
- Front-matter (título, subtítulo, slug, data, linha, tags, `status: em-revisao`, resumo) e o aviso
  legal de `docs/AVISO_LEGAL.md`, depois de `* * *`.

**Conferência do agente `revisao-editorial`: nenhuma edição em `post.md` nem em `diagramas.md`.**
- O diff entre `04-draft-v2.md` e `post.md` traz essas decisões, e só elas, cada uma com o texto do
  laudo. Fora delas, só a montagem (front-matter, `* * *` e aviso). Os 8 itens sem ★ seguem com o
  texto do v2.
- Os números batem com `07-verificacao.md` e com o registro de cálculo
  (`_revisoes/2026-11-18_…_calculo.md`): 874,89; 4,89; 48,808848; as três linhas da tabela, com as
  quantidades de 10 casas; 943,88; 14,53%; 943,68; 94.368.087,53; 94.388.697,41; 20.609,88; 115,18;
  302,60; 20.307,28; 0,2031 (0,2030728); cerca de 2 pontos-base (2,15).
- `post.md`, `diagramas.md` e as figuras estão coerentes. O diag-01 mostra os fluxos, as
  quantidades com 4 casas (as exatas no rodapé) e os custos 45,71 + 42,70 + 855,47 = 943,88. O
  diag-02 mostra os cinco valores de hoje, os brutos de cada data, os 115,18 e o saldo 0,00. Tudo
  confere com o texto e com o laudo. PNG e SVG têm as mesmas manchetes e os mesmos números. Os
  alt-texts dos placeholders são os de `diagramas.md`, abaixo de 125 caracteres.
- Coerência entre etapas: as combinações fecham sem frase quebrada.
  - A "reserva separada na montagem" da C6 tem referente na C4, dois blocos antes.
  - O refrão depois das duas formas continua fazendo sentido com a definição da C3.
  - "Separado dos cupons" (6.1) continua certo sem o `[VERIFICAR]`.
  - A pergunta 1 de "Antes de chamar de arbitragem" continua de acordo com a C9.
- Checklist de voz (§9): os 11 itens estão ok.
  - Itálico em todos os estrangeirismos (*dealer*, *trading*, *spread*, *spot*, *bootstrapping*,
    *long-short*, *STRIPS*).
  - Aspas e apóstrofos curvos.
  - Abre na moeda e no par LTN × NTN-F 2029, e fecha na moeda.
  - Antíteses dentro do teto depois do item 24.
- Antipadrões: nenhum travessão, exclamação, aspas simples de ênfase, rótulo de movimento em H2 ou
  resíduo do processo.
- Notas de um Professor:
  - A Ficha de Saída (`02-estrutura.md`) é entregue: montar, precificar e classificar. O teste de
    transferência da NTN-B fecha o texto, com o enunciado da C11.
  - Dois lados do balcão: quem cota errado e paga, a mesa que arbitra, quem compra NTN-F e marca a
    mercado, e o Tesouro. O Tesouro aparece leve, e isso já está no gate (crítica 14).
  - Bibliografia: 4 itens, 2 livros.
  - As duas divergências do registro de cálculo (C1 e C2) têm correção aplicada.
- `[VERIFICAR]`: nenhum. `[FAIXA]`: nenhum.
- `python3 scripts/checar_post.py`: ok, sem bloqueante e sem aviso.

## Observações para o gate (julgamento, não aplicadas)

1. **"exatamente 100.000 vezes a diferença de preço, que, sem arredondar, é de R$ 0,2031 por
   título."** É o texto da C2, como foi aceito. Mas 0,2031 já está arredondado (o valor é
   0,2030728), e 100.000 × 0,2031 dá R$ 20.310,00, não R$ 20.307,28. Quem refizer a conta cai no
   mesmo tropeço que a C2 corrigiu. Alternativas: "que, sem arredondar, é de R$ 0,2030728 por
   título" ou "que é de cerca de R$ 0,2031 por título".
2. **Planilha (`06-revisao.md`, item F).** `(1+C2:C4)` supõe a taxa guardada como porcentagem
   (14,00% = 0,14). A etapa 7 conferiu a fórmula, mas não tratou do formato da célula. Uma oração
   na frase que apresenta as células resolve, mas pede redação.
3. **Manchete do diag-02: "Ganha hoje, não perde depois".** Ecoa o refrão na seção de onde o autor
   o tirou (crítica 3). Ao contrário do refrão, ela descreve bem a forma 1 (dinheiro hoje, saldo
   zero em cada data), então não repete o defeito. Pode ficar. Trocar exige regenerar a figura.
4. **Parágrafos no limite.** Com as glosas aceitas, "E a ANBIMA faz a conta ao contrário" chegou a
   63 palavras (item 20) e "Agora, um caso concreto" chegou a 60 (C8). O atrito 3 da lista, com a
   glosa do item 28, tem cerca de 76. A etapa 6 deixou esse caso com o autor, por ser item de
   lista. O checador não avisa.
5. **Tags.** `[Notas de um Professor, Renda Fixa, Arbitragem, Precificação]` traz duas tags novas
   em relação ao post anterior (`Matemática Financeira`). Confirmar.
6. **Itens já na pauta:**
   - as críticas baixas 8b e 9 a 14;
   - o registro da etapa 6 sobre a regra de decisão de "Antes de chamar de arbitragem", que repete
     a pergunta 3 (redação do autor, nota 9 do v2);
   - o contexto da etapa 7: o PU de lastro do BCB igual ao da LTN, o caso real de 11/11 e a frase
     de Cochrane sobre *risk arbitrage*;
   - regenerar `marketing/catalogo.json` antes da 9a.
