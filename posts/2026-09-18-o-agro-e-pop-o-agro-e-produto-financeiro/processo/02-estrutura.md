# Etapa 2 — Estrutura

`linha_editorial: Notas de um Professor` → Ficha de Saída obrigatória
(`docs/BACKWARDS_DESIGN.md` §2) antes de fechar a estrutura.

## Ficha de Saída

| Campo | Preenchimento |
| --- | --- |
| **1. Competência de saída** | Separar, para uma LCA, as três contas que costumam ser misturadas — quanto ela rende (break-even real por juros compostos, não a regra linear do gross-up), quanto custa ao banco emissor (decomposição da taxa) e quanto ela vale hoje (marcação a mercado) — e, a partir disso, localizar corretamente o risco de crédito do título (o banco, não o produtor rural). |
| **2. Teste de transferência** | A CRA (Certificado de Recebíveis do Agronegócio). O rascunho já traz a seção "LCA não é CRA": se o leitor termina o texto e consegue explicar por que aplicar a uma CRA a mesma lógica "o banco garante" da LCA é o erro errado — porque na CRA o risco primário é do devedor/patrimônio separado, não de um banco —, o texto funcionou como aula, não só como descrição de produto. Campo não vazio: passa na regra de corte do §2. |
| **3. Tese de fundo** | "A LCA é uma dívida do banco, não do agro — e a isenção não é generosidade, é um benefício fiscal repartido entre banco e investidor." Mesma família da tese-mãe da série (o próprio `docs/BACKWARDS_DESIGN.md` usa o par LCI→LCA como exemplo do documento). |
| **4. Erro-alvo** | Achar que a diferença de taxa entre uma LCA isenta e um CDB tributado se resolve dividindo a taxa da LCA por (1 − IR) — regra linear que superestima quanto o CDB precisa pagar, e erra mais quanto mais longo o prazo (a tabela do rascunho mostra o gap crescendo de 0,8 p.p. em 6 meses para 4,3 p.p. em 5 anos). |
| **5. Ferramenta prática** | A fórmula de break-even por juros compostos e a tabela break-even real por prazo, já no rascunho — o leitor sai sabendo refazer essa conta para qualquer par LCA×CDB com CDI e prazo diferentes. |
| **6. Âncora de autoridade** | Lei nº 11.076/2004, já citada com número na seção "O que é uma LCA" (base legal — o que é, quem emite, o que lastreia). |
| **7. Os dois lados do balcão** | Investidor PF (quanto rende, qual risco assume) × tesouraria do banco emissor (quanto custa, como decompõe a taxa, por que emite). Distribuidor: **não tratado** — nenhuma das três condições do §4.3 do `docs/BACKWARDS_DESIGN.md` se verifica neste rascunho (sem rebate, sem assimetria de dever, sem captação via canal terceiro mencionada); omitir é a escolha correta pela própria regra do documento. |
| **8. Ponte de série** | Vem do texto sobre LCI (dívida bancária lastreada em crédito imobiliário — citado no primeiro parágrafo) → aponta para a CRA (securitização real do agro, patrimônio separado, risco do devedor) — a mesma ponte que a seção "LCA não é CRA" já constrói em conteúdo, mas que falta nomear explicitamente como próximo texto da série no fechamento (ver nota 4 abaixo). |

## Verificação: a estrutura entrega a competência de saída?

Mapeamento das seções do rascunho aos oito movimentos (`docs/BACKWARDS_DESIGN.md` §3) — **sem
reordenar nada**, só confirmar encaixe:

| Seção do rascunho | Movimento(s) | Observação |
| --- | --- | --- |
| Abertura (4 parágrafos, sem título) | 0 (deck, via subtítulo) + 1 (Abertura, modo B — moldura conceitual, sem evento datado) | Ver nota 1 abaixo — não fecha em pergunta-âncora explícita. |
| "O que é uma LCA" | 2 (O Mito, no parágrafo final: "quem compra LCA não assume o risco do produtor rural") + 3 (A Anatomia: base legal, quem emite, lastro, duas relações de crédito) | Os dois movimentos vêm fundidos numa seção só — funciona, o parágrafo final já isola a tese em frase curta como o movimento 2 pede. |
| "O lado de quem emite" | 4 (O Lado de Lá — funding, isenção como benefício repartido, lastro elegível, direcionamento, ALM implícito) | — |
| "O lado de quem compra" (4 subseções) | 5 (O Ponto Cego — "por que essa conta erra", "o risco é o banco") + parte de 3 (carência/liquidez, deslocada para perto da decisão de compra, o que faz sentido editorial) | Núcleo do texto; é onde mora a Ferramenta Prática (campo 5). |
| "Como o banco define a taxa de emissão" | 4 (continuação — decomposição da taxa do ponto de vista da tesouraria) | — |
| "Quanto a LCA vale hoje" (4 subseções) | extensão da Ferramenta Prática / Ponto Cego, específica da terceira pergunta do fio condutor | Não tem encaixe 1:1 num movimento numerado — o framework de 8 movimentos foi pensado para "produto" ou "matemática financeira" isolados; este texto é híbrido dos dois (§4.2), e a extensão é esperada, não um desvio. |
| "LCA não é CRA" | 5 (O Ponto Cego, explícito — "sempre por contraste com um vizinho") | Esta seção **é** o teste de transferência do campo 2 em prosa. |
| "Fechamento: do produto ao balanço" | 8 (A Prateleira — leitura ingênua vs. correta, tradução para decisão) + parte de 9 (Síntese) | Ver nota 4 — falta nomear a ponte para o próximo texto. |
| "Para continuar aprendendo" | 10 (bibliografia anotada) | Ver nota 3 — 4 itens, dentro do limite, mas repete a Lei 11.076 já citada no corpo. |

**Conclusão:** a sequência já entrega a competência de saída declarada no campo 1 — não há
seção faltando nem seção sobrando. Nenhuma mudança de ordem de argumento é necessária. As
quatro notas abaixo são acabamento (regras transversais §5), não reestruturação — ficam
registradas aqui para a etapa 4 decidir caso a caso, sem virar pergunta ao autor (não mudam
onde uma seção entra, só como ela termina).

1. **Movimento 1 pede pergunta-âncora ao final da abertura** — hoje ela termina em afirmação
   ("Este texto responde uma de cada vez."), não em pergunta. Considerar na etapa 4.
2. **Frase-sinal (§5.3)** não aparece — nenhum marcador explícito de passagem do raso ao
   profundo ao fim da Anatomia. Opcional, usar no máximo uma vez se entrar.
3. **Bibliografia repete a Lei 11.076/2004**, já citada com número na Anatomia — a regra 5.7
   diz para evitar citar lei na bibliografia quando ela já foi citada no corpo como o ponto em
   si. Considerar remover da lista final (fica só a menção no corpo) — decisão de etapa 9.
4. **Movimento 9 incompleto**: falta nomear explicitamente a ponte para o próximo texto (CRA)
   no fechamento — o conteúdo da ponte já existe (seção "LCA não é CRA"), falta a frase
   editorial de transição. Sem CTA de compartilhamento — voz explicativa não usa (§4.2).

## O que fica de fora

Nada. As três perguntas do fio condutor do autor (quanto rende / quanto custa / quanto vale)
estão cada uma com seção própria, e o material aproveitável do "draft v2" (ver etapa 1) está
todo presente, direto ou como decisão pendente marcada.

## Onde entra graf-NN / diag-NN / info-NN

Os dois marcadores do rascunho já vieram com o tipo certo pelo critério da skill:

- **`diag-01`** (fluxo produtor/cooperativa ← banco ← investidor) — sem série numérica, é
  relação estrutural entre entidades. Critério 2: correto ser diagrama.
- **`graf-01`** (prazo × regra linear × break-even real) — série numérica real (a própria
  tabela do rascunho). Critério 1: correto ser gráfico.
- **`info-NN`** — nenhum. Nenhuma peça isolada acima falha em carregar sozinha sua parte da
  síntese; padrão do critério 3 (não ter infográfico) se aplica.

## Confirmação dos três pilares

- **Dado:** tabela de break-even, fórmulas de precificação, decomposição de taxa.
- **Visual:** `diag-01` + `graf-01`.
- **Narrativa:** em voz explicativa não há anedota (§4.2) — o fio narrativo é a continuidade
  editorial com o texto de LCI na abertura e o contraste nomeado com a CRA no fechamento
  ("O Ponto Cego", movimento 5). Pilar coberto pela estrutura argumentativa, não por cena.

Todos os três representados em pelo menos uma seção — confirmado.
