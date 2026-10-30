# Etapa 5 — Crítica estrutural

Laudo do agente `critico-editorial` sobre `processo/04-draft-v1.md`, gravado pelo pipeline
principal. Linha Notas de um Professor: sem validação argumentativa de Spoiler e sem etapa 5a.
Números de linha são os de `04-draft-v1.md` (o corpo começa na l. 35). Decisões do autor não
reabertas (título, "quase nunca", [PREENCHER], bibliografia em 4, ponte FIDC, Armadilha 3);
quando uma delas tem consequência estrutural, a consequência aparece marcada como tal.

## Respostas diretas

**Há item de severidade alta?** Não. O texto não volta à etapa 2.
- A tese aparece cedo e isolada (l. 53), volta no meio (l. 140) e no fim (l. 265).
- Cada seção entrega o que o intertítulo promete.
- O achado central ("252 é uma convenção", "o ano é que muda de tamanho") está no gancho e no
  deck, não enterrado.
- O texto não abre pela metodologia: l. 41 dá o resultado, l. 43 o que significa, l. 45 a
  causa.

**A estrutura entrega a competência de saída?** Sim, com ressalva. Das quatro peças da Ficha,
duas (régua e motor) são ensinadas como moldura conceitual; as outras duas (calendário e
pontas) entram como problema de automação, e as pontas só por uma peculiaridade de biblioteca
(M-2, M-4). O teste de transferência (CDB a 100% do CDI) tem as peças no texto: a diária de um
dia útil (l. 91–93), a acumulação de mais de uma Taxa DI entre sessões (l. 159), o calendário
ANBIMA para juros (l. 165).

**Os cinco pontos que a etapa 2 deixou:**
1. Frase-sinal ausente: B-1. A função existe na l. 89, falta o contrato explícito. Não bloqueia.
2. Régua/motor × relógio: M-3. Na l. 87 a imagem soma ("relógio" = o juro correndo, sentido
   próprio). Em "Outros relógios" (l. 253–261) dispersa: vira sinônimo de régua e depois de
   regra de rolagem.
3. Pontas só no código: M-4. Confirmado, e é o principal ponto de abandono.
4. Loop da abertura fechado no meio: B-2. A l. 109 é o lugar certo (modo B dispensa o
   movimento 7). O fecho não precisa retomar a LTN.
5. Ponte e CTA: B-3. Decisão tomada; consequências baixas.

## Diagnóstico

### Severidade média

**M-1. Título × gancho**
- **Onde:** l. 35 contra l. 43–45, com o [PREENCHER] da l. 49.
- **Diagnóstico:** o título diz que o leitor conta dias úteis errado e perde dinheiro; as duas
  frases logo depois do primeiro número dizem que ninguém errou e ninguém ficou com a
  diferença. O caso do gancho é de contagem *certa* dentro da convenção. O primeiro custo em
  reais só aparece na l. 131; o primeiro dia útil literalmente mal contado, na l. 161
  (calendário B3) e nas l. 172–181 (numpy). A virada "o erro é a leitura do leitor, não a
  conta" fica implícita em "Se essa frase soou estranha" (l. 47).
- Consequência da decisão de título, não reabertura: a promessa do assunto do e-mail não tem
  eco na primeira tela. Pelo que a l. 49 pede, a memória pessoal é o único ponto da abertura
  capaz de carregar essa promessa; a avaliação da abertura depende do que o autor escrever ali.
- **Pergunta ao autor:** o gancho fica e a memória faz a ponte, ou a abertura precisa marcar a
  virada?
- **Severidade:** média.

**M-2. A moldura cresce de duas para quatro perguntas sem avisar**
- **Onde:** l. 55–58 ("duas perguntas"), l. 267–272 ("quatro perguntas"), l. 265 (aforismo).
- **Diagnóstico:** a moldura ensinada tem duas peças (contagem e capitalização); o checklist
  final tem quatro. O texto nunca diz que a moldura cresceu, nem como calendário e pontas se
  ligam à pergunta 1 ("quanto tempo passou"). O calendário entra na l. 146 como "dúvida de quem
  vai automatizar"; as pontas, na l. 85, como aparte. Pela definição da l. 64 (régua =
  contagem), o aforismo da l. 265 cobre só a pergunta 1; o título fala das perguntas 3 e 4.
  Ficam três centros com rótulos diferentes: título (contar dias úteis), moldura (régua e
  motor), fecho (quatro perguntas e um aforismo só sobre a régua).
- **Risco:** o leitor guarda a moldura de duas peças e trata calendário e pontas como detalhe
  de código, que é o erro-alvo na versão código (Ficha, campo 4).
- **Severidade:** média.

**M-3. "Outros relógios"**
- **Onde:** l. 253–261.
- **Diagnóstico:** "relógio" tem três sentidos: na l. 87, o juro correndo; nas l. 257–259,
  convenção de contagem (o que as l. 64–68 chamaram de régua; os "dois relógios no mesmo
  prédio" são duas réguas com dois motores); na l. 261, o "terceiro relógio" é ambíguo
  (terceiro depois de DU e DC, ou depois de régua e motor?). A seção promete ir "além do
  DU/252" (l. 255), mas metade da nota sobre rolagem ("Na renda fixa, ela vai para o dia útil
  seguinte") é o `following` já ensinado como remédio (l. 198, l. 219), apresentado como novo.
  Só a metade sobre as opções da B3 é de fato lateral. É a última seção antes da síntese, que
  volta a falar em "régua" (l. 265).
- **Severidade:** média. Corte parcial ou reordenação; o argumento se sustenta.

**M-4. As pontas só se ensinam pelo comportamento de uma biblioteca**
- **Onde:** l. 85 (introduz e adia "para o código"), l. 185–198 (Armadilha 3), l. 251 (pandas),
  l. 272 (pergunta 4).
- **Diagnóstico:** a convenção das pontas (liquidação inclusive, vencimento exclusive, e o
  vencimento em feriado) só é desenvolvida pelo fato de a `bizdays` contar (início, fim]. O
  conceito não depende de Python (a pesquisa §9 registra duas regras com respaldo próprio:
  Código Civil e convenção financeira), mas o texto só o ensina como armadilha de ferramenta.
  A pergunta 4 e a competência da Ficha (campo 1, "tratamento das pontas") dependem desse
  trecho.
- **Agravante:** as l. 185–196 são o parágrafo mais denso do texto (quatro datas, duas regras de
  contagem, uma inversão), na seção que o público não programador do briefing (Bianca, Pedro)
  mais tende a pular. É o principal ponto de abandono. Quem para na l. 168 também perde o
  checklist final, que vem depois de duas seções fáceis de pular.
- **Pergunta ao autor (reordenação):** onde mora o conceito das pontas?
- **Severidade:** média.

**M-5. A l. 77 fecha o que a l. 75 abriu e tira o motivo da pergunta 1**
- **Onde:** l. 77, contra l. 75, l. 269 e a tabela das l. 124–129.
- **Diagnóstico:** a l. 75 diz que o mercado monta combinações conforme o produto; a l. 77 põe
  a renda fixa brasileira inteira, CDB e debêntures incluídos, em DU/252 composto. Para o
  leitor brasileiro, isso tira o motivo doméstico da pergunta 1 e faz as linhas "erradas" da
  tabela do CDB parecerem hipotéticas. A pesquisa (§2; §10 contraponto 1; divergência 6) achou
  CDB registrado na B3 em DC/365, DC/360 composto e meses × 21: a pergunta 1 vale também
  dentro do Brasil, e as linhas da tabela viram alternativas reais. Correção do fato: etapa 7.
- **Severidade:** média.

**M-6. "ANBIMA ou B3?": a diferença que já não vale vem antes da que vale**
- **Onde:** l. 153–157.
- **Diagnóstico:** das "duas diferenças" anunciadas, a primeira (feriados de São Paulo até 2021)
  não tem efeito hoje (o próprio parágrafo termina dizendo que o 20/11 "hoje fecha os dois
  calendários"), mas vem antes da única ainda válida (fim de ano, l. 157) e da prova (dezembro
  de 2026, l. 161, onde entra o diag-01). É o parágrafo mais denso da seção (três datas, uma
  lei, duas mudanças de regime) e não diz para quem isso importa (série histórica, recálculo
  de juros anteriores a 2022). Segundo ponto de abandono.
- **Pergunta ao autor:** manter, descer ou justificar?
- **Severidade:** média.

**M-7. O deck promete uma frequência que o corpo não mostra**
- **Onde:** l. 37 ("quase nunca") contra a tabela das l. 101–107.
- **Diagnóstico:** a única evidência de frequência no corpo é 1 ano em 5, e o ano com 252 é
  2025, o anterior à publicação, na segunda linha da tabela. O que sustenta o "quase nunca" (3
  em 30 anos, 2001–2030) está na pesquisa §0, não no texto. A alavanca é a janela do graf-01,
  que a etapa 2 deixou como opção: com 5 anos, o deck fica sem sustentação visível; com a série
  longa, fica sustentado.
- **Severidade:** média. Depende de decisão já em aberto, não de reescrita.

### Severidade baixa

**B-1. Frase-sinal** (l. 85, l. 89). A l. 85 é promessa, não passagem. A passagem do raso ao
profundo existe na l. 89, no ponto previsto, sem o contrato explícito do §5.3. A l. 133 ("a
parte que eu acho mais bonita") é um segundo ponto de virada; uma frase-sinal explícita não
deveria concorrer com esses dois. Não bloqueia.

**B-2. Loop da LTN** (l. 109, l. 185). Fechar na l. 109 é o lugar certo. O fecho retoma o loop
do leitor (l. 274 responde ao "soou óbvia", l. 278 ao "júnior que senta do seu lado", ambos da
l. 47), e isso basta. Observação: a LTN volta na l. 185 como caso das pontas sem ser marcada
como a mesma do começo; o leitor pode perder que o gancho já continha a armadilha. Sem ação
obrigatória.

**B-3. Ponte de série** (l. 276, l. 259). Decisão tomada; três consequências: (i) o checklist
§6 pede "de onde vem, para onde vai", e o "de onde vem" fica só na palavra "parêntese", sem o
motivo (a série usou DU/252 sem explicá-lo, Ficha campo 8); (ii) o leitor só descobre na
penúltima linha que o texto é um parêntese dentro de uma série; (iii) "Isso merece uma nota só
para ele" (l. 259) continua como segunda promessa, sem prazo, ao lado do FIDC. O campo 8 da
Ficha em `02-estrutura.md` ainda diz "em aberto".

**B-4. Armadilha 2** (l. 183). Remissão sem código e sem conteúdo novo ("Já vimos o custo
acima") dentro da seção de código; infla a contagem de armadilhas. Cortar ou fundir é opção
estrutural do autor.

**B-5. O mito enunciado não é o erro do gancho** (l. 60). A versão enunciada ("No Brasil é 252
composto, lá fora é 360 linear" como uma coisa só) é a confusão régua × motor. O erro-alvo que
o gancho e o deck instalam ("12% ao ano rende 12% em um ano") nunca é dito em voz alta como
crença, só presumido em "Ninguém errou a conta". Liga-se a M-2.

**B-6. Achados da pesquisa que afetam o argumento e não foram usados.** (a) Materialidade
(l. 131, l. 161): a escala vem de multiplicar por 1.000, duas vezes; mostra tamanho, não que o
erro acontece. A pesquisa (§10) não achou caso público de erro, mas achou impacto financeiro
documentado de mudança de calendário (20/11: CE 006/2024-VPC, CE 013/2024-VPC, OC
207/2023-PRE). (b) Movimento 4 (l. 99–109): o texto trata o desvio em relação a 252 como
oscilação; a pesquisa (§10, item 1) mostra viés (média de 251 DU em 2001–2030, cerca de 250,5
no regime atual), que é exatamente "a hipótese que a fórmula embute" do §4.2. Opcionais;
números para a etapa 7; o autor decide.

**B-7. Falta visual no ponto mais difícil** (l. 185–196). Os três pilares estão presentes
(graf-01, graf-02, diag-01), mas o conceito mais difícil (as pontas com vencimento em feriado)
é o único sem peça visual, e o critério 2 se aplicaria. Decisão das etapas 2 e 8; só
registrado.

### O que está bem

- Abre pelo resultado e pelo sentido, não pela metodologia (l. 41–45).
- Tese isolada três vezes (l. 53, l. 140, l. 265); insight central no gancho e no deck.
- Cada intertítulo entrega o que promete; as três partes do deck estão cobertas (l. 87–95,
  l. 99–109, l. 168–251), com a ressalva de M-7.
- Voz ensaística consistente: primeira pessoa de opinião e memória (l. 89, 133, 170, 200),
  plural que conduz (l. 113, 181, 183), CTA de compartilhamento. O tom impessoal da Anatomia e
  do calendário é o registro técnico declarado, não mistura de vozes.
- O arco do CDB fecha bem: tabela de custo → taxas equivalentes (l. 133–140) → o mesmo
  `40 101815.15` saindo do código (l. 225). Dado, narrativa e prova executável na mesma linha.
- Os dois leitores da l. 47 voltam no fecho (l. 274, l. 278).
- Nenhuma seção precisa sair inteira; os cortes possíveis são parciais (M-3, M-6, B-4).

## Checklist §6 (BACKWARDS_DESIGN)

| Item | Status | Nota |
|---|---|---|
| Ficha preenchida, campo 2 respondido | Sim | CDB a 100% do CDI; peças no texto (l. 91–93, 159, 165) |
| Erro-alvo específico | Sim | Ressalva B-5 |
| Tese isolada no início e no fim | Sim | l. 53 e l. 265, também l. 140 |
| Movimento 4 existe | Sim | DI de um dia útil e Circular 2.761. Ressalva B-6(b) |
| Ponto cego por contraste com vizinho nomeado | Sim | DC/365, DC/360, linear (l. 124–140); calendário B3 (l. 144–166) |
| Acrônimos glosados | Pendente, etapa 6 | LTN (l. 41), Selic, DI, CDB, DI1, VF, marcação, pregão, PyPI, Treasuries, DDI/FRC, cupom cambial, Actual/Actual |
| Números com fonte, cálculo próprio declarado, fórmulas recalculadas | Pendente, etapa 7 | Taxas equivalentes, R$ 137, R$ 90 e escala de R$ 100 mi são cálculo próprio sem rótulo no corpo |
| Exemplos compatíveis com o mercado | Pendente, etapa 7 | Ver M-5 |
| Gráfico com manchete, anotação e fonte | Pendente, etapa 8 | graf-01 (janela, M-7), graf-02, diag-01 |
| Ponte de série explícita | Parcial | Para onde vai: sim. De onde vem: só "parêntese" (B-3) |
| Bibliografia 3–4, mínimo 2 livros, anotada | Sim | Hull, Tosi, ANBIMA, Garcia |
| Nada condescendente | Sim | A ironia da l. 47 recai sobre o professor, não sobre o leitor |

**Três pilares:** presentes, com a ressalva B-7.

## Parágrafos que a etapa 6 deve deixar para depois

Dependem de decisão estrutural do autor: l. 41–49 (M-1); l. 55–60 (M-2, B-5); l. 77 (M-5,
também etapa 7); l. 85 e l. 185–198 (M-4); l. 153–157 (M-6); l. 183 (B-4); l. 253–261 (M-3).

## Contagem por severidade

- **Alta:** 0
- **Média:** 7 (M-1 a M-7)
- **Baixa:** 7 (B-1 a B-7)

Nenhum item alto: nada força retorno à etapa 2.

**Veredito:** pronto para a revisão de linha (etapa 6), sem volta à estrutura. M-1, M-2, M-3,
M-4 e M-6 vão ao autor, de preferência antes de a etapa 6 tocar os parágrafos listados. M-5
acompanha a etapa 7; M-7 acompanha a decisão da janela do graf-01 (etapa 8 ou gate).
