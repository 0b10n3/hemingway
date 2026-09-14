# Backward design — linha editorial "Notas de um Professor"

**Escopo:** só a linha editorial *Notas de um Professor* do pipeline `post-substack`. Este
documento não trata de aulas expositivas, cases ou material de curso — isso pertence ao
produto irmão Syntaxis Educação (cursos Hotmart), fora deste repositório (ver nota de
proveniência no fim deste arquivo).

Absorvido de `_insumos/METHODOLOGY.md` (fundamentos, §1) e
`_insumos/ESTRUTURA_NOTAS_DE_UM_PROFESSOR.md` (macroestrutura, §2-§7) na refatoração do
pipeline v2 (2026-09-13), adaptado de material de curso para posts de Substack.

---

## 1. Fundamentos do backward design

Backward design (Wiggins & McTighe, *Understanding by Design*) inverte a ordem natural de
escrever: em vez de partir do assunto e ir cobrindo tópicos até acabar o espaço, parte-se do
que o leitor deve **conseguir fazer** ao final, define-se como isso seria demonstrado, e só
então se sequencia a explicação.

Aplicado a um post da linha Notas de um Professor:

1. **Definir a competência de saída** — o que o leitor consegue fazer depois de ler, não o
   que ele "fica sabendo". Verbo de ação + objeto, não substantivo solto.
2. **Definir a evidência** — o teste de transferência: um produto/caso vizinho que o texto
   **não** explica, mas que o leitor deve conseguir analisar sozinho ao terminar. Se esse
   campo fica vazio, o texto ainda é descrição de produto, não aula.
3. **Só então sequenciar o texto** — os movimentos da §2 abaixo.

Isto não é enfeite pedagógico: é o que separa "explicar o que a LCI é" de "ensinar alguém a
reconhecer, em qualquer título parecido, onde o risco realmente está".

Princípio complementar, também de `METHODOLOGY.md`: **carga cognitiva**. Todo termo técnico
abre na primeira ocorrência com definição funcional (não dicionarística) — ver §4.1 abaixo.
Isso não é simplificação, é sequenciamento: o termo técnico permanece no texto, o custo de
aprendê-lo é pago uma vez só.

---

## 2. Ficha de Saída (preencher antes de escrever)

O erro clássico do backward design é confundir "o que o texto vai cobrir" com "o que o leitor
vai conseguir fazer". Os campos abaixo forçam a segunda pergunta. Preencher em
`02-estrutura.md` antes de fechar a estrutura do post — é o estágio 1 e 2 do backward design.

| Campo | O que é | Exemplo (post LCI) |
| --- | --- | --- |
| **1. Competência de saída** | Verbo de Bloom + objeto. O que o leitor *consegue fazer* depois, não o que ele "conhece". | *Identificar* de quem é o risco de crédito em qualquer título bancário lastreado, distinguindo lastro de segregação patrimonial. |
| **2. Teste de transferência** | O produto/caso vizinho que o texto **não** explica, mas que o leitor deve conseguir analisar sozinho ao terminar. É a evidência de aprendizagem. | A LCA. Se o leitor não consegue refazer o raciocínio trocando "crédito imobiliário" por "crédito do agronegócio", o texto falhou. |
| **3. Tese de fundo** | Uma frase. Deve pertencer à família da tese-mãe da série. | "Não é favor, é spread — e o risco que sobra muda de endereço, não desaparece." |
| **4. Erro-alvo** | A crença falsa e *específica* que o texto demole. Precisa ser algo que gente competente de fato acredita. | Que o risco da LCI é o risco do mutuário do financiamento imobiliário. |
| **5. Ferramenta prática** | A conta, o critério ou a comparação que o leitor leva para o trabalho. | Gross-up e o ponto em que ele deixa de decidir (720 dias, piso de 15%). |
| **6. Âncora de autoridade** | A fonte primária que sustenta o bloco central: regulador nomeando o fenômeno, lei, ou paper clássico. | Ho & Saunders (1981), banco como *dealer* avesso a risco. |
| **7. Os dois lados do balcão** | Quem adquire / quem emite / (quando cabe) quem distribui. Campo obrigatório da linha editorial. | Investidor PF × tesouraria do banco. Distribuidor: não tratado. |
| **8. Ponte de série** | De qual post este texto vem e para qual ele aponta. | Vem do CDB (dívida bancária simples) → aponta para o CRI (securitização de verdade). |

**Regra de corte:** se o campo 2 estiver vazio, o texto ainda é uma descrição de produto, não
uma aula. Volte ao campo 1.

**Verificação obrigatória (etapa 2 do pipeline):** antes de fechar `02-estrutura.md`, confirme
que a estrutura de fato entrega a competência de saída declarada no campo 1 — não basta
declará-la, a sequência de seções precisa produzi-la.

---

## 3. Os oito movimentos

Blocos marcados **[núcleo]** aparecem em todo texto. Os **[opcional]** entram quando a
condição de uso se verifica. Os movimentos 4 e 5 se invertem sem prejuízo, conforme o caso.

| # | Movimento | Função | Pergunta de escrita | Status | Extensão |
| --- | --- | --- | --- | --- | --- |
| **0** | **Título + deck** | O subtítulo carrega a tese, não o assunto. | Qual frase, sozinha, já entrega a tese de fundo? | [núcleo] | 1 linha |
| **1** | **A Abertura** | Instalar a tensão. Dois modos — ver §4.1. Termina sempre na **pergunta-âncora**. | Que pergunta este texto inteiro existe para responder? | [núcleo] | 3–6 parágrafos |
| **2** | **O Mito** | Enunciar em voz alta a versão errada, e opor a tese em uma frase curta e isolada. | Qual é a versão bonitinha que o mercado conta — e qual é a frase que a substitui? | [núcleo] | 3–8 linhas |
| **3** | **A Anatomia** | O mínimo técnico com lastro: base legal, quem emite, garantias, tributação, liquidez. Fecha com **frase-sinal** (§5.3). | Quais regras mantêm este instrumento de pé? | [núcleo] | 1 seção curta |
| **4** | **O Lado de Lá** | A engenharia de quem emite. Onde vive o rigor institucional: ALM, compulsório, LCR/NSFR, spread, mitigação de risco. | Que problema de balanço, regulação ou liquidez o emissor resolve ao colocar isso na prateleira? | [núcleo] | 1–2 seções |
| **5** | **O Ponto Cego** | A distinção que separa quem entende de quem vende. **Sempre por contraste com um vizinho.** | Onde o risco (ou o conceito) está escondido, e quem o carrega no fim do dia? | [núcleo] | 1 seção densa |
| **6** | **A Materialidade** | Prova de escala: estoque, série histórica, participação de mercado, gráfico. Impede que a tese pareça curiosidade acadêmica. | O fenômeno que descrevi é grande e está crescendo? Tenho série confiável? | [opcional] | 1 seção + gráfico |
| **7** | **O Fechamento do Loop** | Voltar ao evento da abertura agora que o leitor tem ferramental — e mostrar a resposta do regulador, se houve. | O que o caso de abertura significa agora que o leitor sabe o que sabe? | [opcional] | 2–4 parágrafos |
| **8** | **A Prateleira** | Tradução para decisão. Comparação, encaixe, risco relativo contra pares, implicação prática. Bloco natural do **distribuidor**. | Sabendo como o emissor precifica isso, como a decisão muda? | [núcleo] | 1 seção |
| **9** | **A Síntese + Ponte** | Retomar a tese sem jargão, generalizar lateralmente (o produto-irmão), apontar o próximo post, convidar ao compartilhamento. | Se o leitor esquecer tudo, que frase sobra? E para onde ele vai agora? | [núcleo] | 3–6 linhas |
| **10** | **Para Continuar Aprendendo** | Bibliografia **anotada**: cada item com a razão de estar ali. | Onde está a fonte primária, e para que serve cada uma? | [núcleo] | 4–6 itens (ver regra de referências, §5.7) |

### Quando usar os opcionais

| Bloco | Use quando | Pule quando |
| --- | --- | --- |
| **6. Materialidade** | A tese depende de escala ("isso não é nicho"); existe série pública rastreável; há um ponto de inflexão a explicar (aperto regulatório, mudança tributária). | O dado não existe em série confiável; o instrumento é conceitual; o número não muda o argumento. Dado decorativo enfraquece o texto. |
| **7. Fechamento do loop** | A abertura foi por evento datado (modo A, §4.1). | A abertura foi conceitual (modo B). Nesse caso, o movimento 9 absorve a função. |

---

## 4. Variações previstas

### 4.1. Dois modos de abertura

| | **Modo A — Evento datado** | **Modo B — Moldura conceitual** |
| --- | --- | --- |
| Mecânica | Fato verificável com data e número (liquidação, mudança de regra, movimento de mercado) → pivô pessoal → pergunta-âncora. | Uma proposição contraintuitiva que reenquadra a categoria inteira → pergunta-âncora. |
| Exemplo | Banco Master, nov/2025, R$ 40,6 bi do FGC. | "Todo investimento em renda fixa bancária é, no fundo, uma negociação sobre o tempo." |
| Use quando | Existe caso recente, público e documentado que materializa o erro-alvo. | O erro-alvo é conceitual e não tem um caso limpo; ou o caso óbvio já foi usado em post anterior. |
| Custo | Obriga o movimento 7 (fechar o loop). Envelhece mais rápido. | Exige uma primeira frase muito boa. Perde ancoragem noticiosa. |

### 4.2. A estrutura por tipo de conteúdo

A linha editorial cobre quatro naturezas de tema. Os movimentos 4, 5 e 8 mudam de conteúdo —
não de função.

| Tipo de post | **4. O Lado de Lá** vira | **5. O Ponto Cego** vira | **8. A Prateleira** vira |
| --- | --- | --- | --- |
| **Produto / instrumento** | Engenharia de balanço do emissor: funding, spread, exigência regulatória. | Distinção estrutural contra o produto vizinho (LCI × CRI × LIG; CDB × CDI). | Alocação, comparação líquida, risco relativo contra pares. |
| **Conceito de finanças** | Que problema o conceito foi inventado para resolver, e por quem. | Onde a intuição comum falha e por quê. | Que decisão real muda quando o leitor passa a usar o conceito. |
| **Matemática financeira** | De onde vem a fórmula e qual hipótese ela embute. | O caso em que a aproximação quebra (ex.: gross-up linear em prazos longos). | A conta que o leitor refaz na planilha, com os parâmetros do trabalho dele. |
| **Modelagem financeira** | Quem usa o modelo, para decidir o quê, sob qual pressão institucional. | A hipótese silenciosa — o que o modelo assume e o mercado não cumpre. | Como calibrar, validar e, principalmente, quando desconfiar do output. |

### 4.3. Onde entra o distribuidor

O compromisso editorial é "quando cabe". Na prática, cabe em três situações, e o lugar é o
movimento 8 (ou uma subseção própria entre 5 e 8):

1. **Quando o distribuidor é remunerado de forma que altera o que chega à prateleira** —
   rebate, taxa de distribuição embutida na taxa, seleção de emissores por acordo comercial.
2. **Quando existe assimetria de dever** — suitability, dever de informação, quem responde
   pelo quê.
3. **Quando o produto só existe porque há canal** — captação de banco pequeno via corretora
   de terceiros é o caso mais claro.

Se nenhuma das três se verifica, omitir é correto. O que não vale é mencionar o distribuidor
de passagem, sem consequência para a decisão do leitor.

---

## 5. Regras transversais (a assinatura)

### 5.1. Cadeia de glosas
Todo termo técnico e todo acrônimo abrem na primeira ocorrência, entre parênteses, com
**definição funcional, não dicionarística**.

> alienação fiduciária (a garantia em que o imóvel fica em nome do credor até a quitação da
> dívida)

Isto é redução de carga cognitiva extrínseca, não simplificação: a glosa preserva o termo
técnico no texto e paga o custo de aprendê-lo uma vez só.

### 5.2. Um dado, uma fonte
Regra universal de marca. Todo percentual, todo estoque, toda data tem origem rastreável —
inclusive quando o número é cálculo próprio, que deve ser declarado como tal.

### 5.3. A frase-sinal
Marcador explícito da passagem do raso ao profundo, tipicamente ao fim do movimento 3:

> "Até aqui, é o que qualquer material de corretora te conta. O interessante começa agora."

Serve de contrato com o leitor. Usar uma vez por texto, nunca duas.

### 5.4. Ritmo
Parágrafos curtos, uma ideia por parágrafo. A tese aparece isolada, em linha própria, pelo
menos duas vezes: no movimento 2 e no movimento 9. Frases de virada são curtas ("O banco
quebrou.", "A LCI não é favor.").

### 5.5. Onde a leveza vive
Abertura e transições. Nunca em cima de número, de risco ou de tensão institucional. A
leveza está no *como*, nunca no *o quê*.

### 5.6. O que não fazer
- Abrir por definição ("Hoje vamos falar sobre a LCI").
- Anedota no lugar da fórmula.
- Jargão sem glosa, ou glosa sem jargão (ambos são o mesmo erro).
- Tratar o leitor como leigo total. Ele é um colega júnior competente.
- Número sem fonte. Linha vermelha.

### 5.7. Regra de referências
**3 a 4 referências no máximo**, escolhidas pela importância — não pela quantidade.
**Mínimo de 2 livros.** Leis: evitar citar como referência de bibliografia (evitar, não
proibir — só quando o dispositivo legal for o ponto em si do texto, não um livro cita-se em
"A Anatomia" com o número da norma, não na bibliografia final).

---

## 6. Checklist de publicação

- [ ] A **Ficha de Saída** (§2) está preenchida, com o campo 2 (teste de transferência)
      respondido?
- [ ] O **erro-alvo** é específico o bastante para que alguém competente pudesse acreditar
      nele?
- [ ] A **tese** aparece isolada, em frase curta, no início e no fim?
- [ ] O **movimento 4** existe de fato — o texto explica o lado de quem emite, não só o de
      quem compra? (dois lados do balcão, campo obrigatório)
- [ ] O **ponto cego** é estabelecido por contraste com um vizinho nomeado?
- [ ] Todo acrônimo foi aberto na primeira ocorrência, com definição funcional?
- [ ] Todo número tem fonte, e o cálculo próprio está declarado como próprio? Toda fórmula foi
      recalculada numericamente com os valores do próprio texto (ver etapa 7 do pipeline)?
- [ ] Exemplos (taxas, prazos, tributação, ordens de grandeza) são compatíveis com a realidade
      do mercado brasileiro na data do texto?
- [ ] Se há gráfico: manchete própria, anotação do ponto de inflexão, fonte no rodapé?
- [ ] A **ponte de série** está explícita (de onde vem, para onde vai)?
- [ ] A bibliografia tem **3 a 4 itens, no mínimo 2 livros**, cada um anotado (para que serve)?
- [ ] Nenhuma frase soaria condescendente dita a um colega de trabalho adulto?

---

## 7. Decisões em aberto (herdadas do material de origem)

1. **A quem se destina o movimento 8.** Os posts de referência terminam em "seu portfólio"
   (investidor pessoa física), enquanto o público declarado da Syntaxis é o profissional de
   mercado de capitais. Vale escolher conscientemente: (a) manter PF; (b) reescrever para a
   ótica de quem *estrutura, avalia ou recomenda*; ou (c) manter o bloco duplo como padrão.
2. **O bloco de materialidade como norma ou exceção.** Se virar padrão, exige rotina de
   coleta de série (B3, Bacen, Anbima) na etapa de pesquisa do fluxo.
3. **Profundidade matemática.** Para posts do tipo "matemática financeira" (§4.2), definir se
   a fórmula entra no corpo, em bloco destacado, ou em apêndice.

---

## Nota de proveniência e escopo

Este documento absorve `_insumos/METHODOLOGY.md` e
`_insumos/ESTRUTURA_NOTAS_DE_UM_PROFESSOR.md`. Os outros 7 arquivos que existiam em
`_insumos/` (`AUDIENCES.md`, `FEAR.md`, `FUNIL.md`, `GREED.md`, `MARKETING.md`,
`PRICE_TAG.md`, `PROJECT_DESCRIPTION.md`, `RESEARCH_GEMINI.md`, `SYNTAXIS.md` — nove no
total, dois absorvidos aqui) tratam de segmentação de público, funil de vendas e
precificação dos **cursos** Syntaxis Educação (Hotmart) — um produto irmão deste pipeline,
não o pipeline de posts do Substack. Não foram absorvidos como fonte deste sistema: o
público/estratégia comercial da newsletter já tem fonte única em
`_arquivo/MARKETING_REVIEW.md` (ver `CLAUDE.md`), e misturar as duas violaria a regra de
"uma fonte por fato". Ficam de fora deliberadamente — se um dia o pipeline de cursos for
migrado para este ecossistema de repositórios, esse material pertence lá, não aqui.
