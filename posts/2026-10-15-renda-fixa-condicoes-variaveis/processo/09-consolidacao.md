# Etapa 9 — Consolidação

Montagem: o orquestrador gerou `post.md` sobre `04-draft-v2.md`, aplicando:
- `06-revisao.md`: todas as "Aplicar" (A-01…A-46, T-1, T-2), exceto A-38 (substituída por K-02)
  e A-39 (redundante com a glosa de K-02); só as sugestões ★ (S-12, S-19, S-20, S-21, S-30,
  S-33 com glosa de "aporte", S-35, S-36), por decisão do autor;
- `07-verificacao.md`: K-01 versão recomendada (data + retificação), K-02, K-03, K-04, K-05,
  K-06 (oração cortada), K-07, por decisão do autor;
- glosa de "lâmina" na 1ª ocorrência (autor);
- `[VERIFICAR]` nos capítulos do Varanda Neto e na edição do Eizirik;
- tabelas → placeholders `diag-01`, `diag-02`, `graf-01`, `graf-02` com alt-text; as duas
  legendas "Cálculo próprio" que as imagens já carregam saíram do corpo.

Script de montagem com asserção por trecho (temporário, scratchpad da sessão).

Passada de coerência: agente `revisao-editorial`.

## O que conferiu

1. **Etapas 5, 6 e 7 não se contradizem.** C-05 (ponte RJ × RE + K-07), C-12 (S-19 + S-30),
   C-13 (S-35 + S-36), C-14/K-01 (sem "em setembro" residual), C-18 (S-12), C-19/K-02 (sem
   "VNA"; vírgula elíptica preservada), K-03/K-04/K-05 + A-32, K-06 (o `[VERIFICAR]` cai com o
   corte), A-30 + K-07 (sem "aceleração"), T-2 (sem DI solto no corpo). Nenhuma frase quebrada.
2. **Glosas:** ~40 termos conferidos, um caso de glosa antes do primeiro uso (edição 1). Sem
   duplicação criada pela consolidação.
3. **Aforismos protegidos:** todos preservados, sem negrito; frase de laço na versão nova.
4. **post.md × graficos.md × diagramas.md:** placeholders sem órfãos; números idênticos entre
   texto, alt, CSV/assert e imagem; rodapé do graf-02 com "PU / PU par" (coerente com K-02).
5. **Checklist de voz (§9) e antipadrões de IA:** ok, salvo T-3 (paralelismo "não é X / é Y",
   decisão do autor).
6. **Ficha de Saída:** a estrutura final entrega o campo 1; dois lados do balcão presentes;
   bibliografia com 4 itens, 2 livros, sem lei. Gate de Tufte: tabelas sem eixo, ênfase só por
   cor de célula.

## Edições feitas em post.md (pelo agente)

1. Glosa antes do primeiro uso: `três pós-fixados (a taxa acompanha um índice, o CDI ou o IPCA) e um prefixado` → `três pós-fixados (a taxa acompanha um índice) e um prefixado`.
2. T-1 meio aplicada na bibliografia: `DI + spread e IPCA + spread` → `DI + *spread* e IPCA + *spread*`; `por que os covenants existem` → `por que os *covenants* existem`; `com poucos covenants e muita` → `com poucos *covenants* e muita` (título em inglês de Smith & Warner intocado).

## Edição feita pelo orquestrador (acabamento da etapa 8, observação 1 do agente)

- graf-01: a anotação da imagem, o alt-text e o comentário de `graficos.md` diziam "O mesmo
  110% do CDI… vale… vira", contra A-36 aplicada no post. Corrigido para "Os mesmos 110% do
  CDI… valem… viram" e `figuras/graf-01.png/.svg` regenerados a partir do próprio
  `graficos.md` (sem outra mudança).

## Observações para o gate humano

1. Itálico de "spread" nas figuras (título do graf-01, cabeçalho do graf-02): cosmético, exige
   regenerar.
2. O corpo depende do `[VERIFICAR]` do Varanda Neto: "dedicam um capítulo inteiro a esse
   efeito" se apoia no cap. 19.
3. Garantia flutuante: a glosa de A-11 ("privilégio geral sobre o ativo da empresa") antecipa
   o golpe de "O nome sugere um privilégio… e por décadas foi isso". Alternativa:
   "(que dá privilégio geral sobre o ativo, nos termos da Lei das S.A.)".
4. "Quirografária" glosada duas vezes no draft do autor ("ou seja, sem garantia" e "sem
   preferência sobre os demais credores"). Registro.
5. "DI" na bibliografia sem glosa (T-2 opcional): sugestão "percentual do CDI, CDI + *spread*…".
6. "Selic em 13,75%" no texto × "meta Selic em 13,75%" na imagem do graf-01 (S-23, não ★).
7. Itens da crítica sem ação: C-03, C-10, C-11, C-15, C-16 (deck de assunto; eco com *Renda
   Fixa Não é Fixa*), C-20, T-3.
8. Frontmatter `data: 2026-10-15`: ajustar se o campo for a data de publicação (depois de 18/10).

## `[VERIFICAR]` pendentes em post.md

1. Varanda Neto, Santos e Mello: números dos capítulos 8 e 19 (afeta também "dedicam um
   capítulo inteiro").
2. Eizirik, *A Lei das S/A Comentada*: edição vigente e paginação.

Sem `[FAIXA]`.

## Reentrada pós-gate (acabamento, não consome loop)

- Glosa da flutuante: `(privilégio geral sobre o ativo da empresa)` → `(que dá privilégio geral sobre o ativo, nos termos da Lei das S.A.)` (observação 3).
- `Com a Selic (…) em 13,75