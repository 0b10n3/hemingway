# Etapa 9: Consolidação

**Montagem:** o orquestrador gerou `post.md` sobre `04-draft-v2.md`, aplicando as decisões do autor
(`estado.json`, "aprovacoes"):
- `06-revisao.md`: as 7 `norma` (3, 5, 6, 8, 27, 41, 43) e as 30 `linha` com ★ (2, 4, 7, 10, 11, 12,
  13, 14, 15, 16, 17, 18, 19, 21, 24, 25, 26, 28, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40, 42). As
  6 sem ★ (1, 9, 20, 22, 23, 32) ficaram de fora.
- `07-verificacao.md`: C1, C2 (texto exato), C3 na opção A (três trocas), C4 combinada com o item 8
  ("cinco papéis principais"), C5, C6 e C7 (adendo). C8 é fora do corpo (gabarito do CDB, R$ 732,30, em
  `estado.json`). V1: o autor confirmou a descrição do Securato no exemplar.
- Cada troca foi aplicada por texto exato, com conferência de ocorrência única; a ordem seguiu a de
  `06-revisao.md` ("Ordem de aplicação").
- Front-matter (título, subtítulo atual, slug, data de publicação do ClickUp 2026-11-24, linha, tags,
  `status: em-revisao`, resumo) e o aviso legal de `docs/AVISO_LEGAL.md`, depois de `* * *`.
- `scripts/checar_post.py`: sem bloqueante e sem aviso, depois de dois ajustes da montagem: o
  cabeçalho da ficha alternativa em `infograficos.md` deixou de começar por `info-01` (não é peça do
  post até o gate), e o código do `graf-01` declara `rangemode="tozero"` (o eixo já começava em zero;
  figura reexportada sem mudança visível).

**Conferência do agente `revisao-editorial`: nenhuma edição em `post.md`.**
- O diff entre o corpo de `04-draft-v2.md` e `post.md` traz as decisões, e só elas, cada uma com o
  texto do laudo. Os 6 itens sem ★ seguem com o texto do v2. O aviso legal é o de `docs/AVISO_LEGAL.md`.
- As combinações (3→4, 8+C4, 11→12, 18+19+C6, 33→34, 35+C3, 36 a 39, 40→41) fecham sem frase quebrada.
- Os números batem com `07-verificacao.md` (N1 a N46, A1 a A24; tabela 12.812, 13.081, 13.631 e
  13.405).
- Manchetes, anotações e números das figuras batem com `graficos.md` e com o texto; os dois alt-texts
  têm 124 caracteres; `infograficos.md` registra por que existe e não tem placeholder.
- Voz (§9) e antipadrões: nenhum travessão, exclamação, aspas retas ou resíduo do processo; 6
  antíteses, no máximo uma por seção (densidade no item D de `06-revisao.md`). Dois parágrafos com 60–61
  palavras (itens 9 e 23, recusados pelo autor). "Repare" aparece 4 vezes, leve.
- Fluxo Notas: passa. Ficha entregue, teste do CDB no fecho; dois lados do balcão (Tesouro, BC,
  bancos, pessoa física); bibliografia com 4 itens, 2 livros, todos anotados. Achado enterrado: sem
  alarme.

**Alarmes do agente e o que foi feito:**
1. `resumo` do front-matter dizia "caiu 3,6% em outubro de 2026" (a queda vai de 13/10 a 17/11). Era
   texto da montagem: corrigido para "perdeu 3,6% entre outubro e novembro de 2026".
2. "A queda não é o resultado da aposta." (De volta a outubro): o item 35 tirou a única menção a
   "preço" da seção, e "a queda" pode ser lida como a da taxa em 5/10. Corrigir pede uma palavra fora
   dos laudos ("A queda do preço"): **pergunta para o gate**.
3. `graficos.md`, "Onde entra" do `graf-01` descrevia a posição da v1: corrigido para a da v2.
4. A legenda do `graf-01` repetia quase igual a frase de anúncio: trocada por "Nas viradas, a taxa vira
   antes do Copom; nos sustos de 2002, 2008, 2024 e 2026, salta com a Selic parada."

**Registro de processo:** a Ficha de Saída em `02-estrutura.md` tem três campos que a v2 superou (o
gabarito de R$ 732,56, que é R$ 732,30 pela C8; a gaveta "garantia"; o *bootstrapping* logo depois da
NTN-F). O arquivo de processo fica como registro; o que vale está em `04-draft-v2.md` e em `estado.json`.
