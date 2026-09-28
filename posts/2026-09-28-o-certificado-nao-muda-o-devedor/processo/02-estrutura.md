# Etapa 2 — Estrutura

A estrutura é a do rascunho do autor, que já segue os movimentos de `docs/BACKWARDS_DESIGN.md`
§3 quase um a um. Esta etapa mapeia, verifica a competência de saída e decide os visuais. Não
reordena nada. As únicas mudanças são as que o próprio autor pediu (item 6 do inventário:
ponte para debêntures).

## Ficha de Saída

| Campo | Preenchimento |
| --- | --- |
| **1. Competência de saída** | *Localizar* o risco de crédito de qualquer CRI ou CRA, separando três camadas: quem é o devedor (um ou muitos), o que a estrutura põe entre o investidor e esse devedor (garantia real, coobrigação, subordinação ou nada) e quanto o título vale hoje (PU descontado pela NTN-B + spread do devedor). Como consequência, *comparar* corretamente um CRA isento com a debênture tributada do mesmo devedor. |
| **2. Teste de transferência** | **A debênture do mesmo devedor.** O texto explica o CRA corporativo como "uma debênture daquela empresa, com isenção e mais intermediários", mas não explica a debênture em si. Se o leitor termina o texto e consegue dizer, diante de uma debênture da Raízen e de um CRA lastreado nela, o que é igual (o devedor, o risco de crédito), o que muda (IR, camadas de mediação, assembleia, eventuais garantias da estrutura) e como compará-los (o empate da seção "A conta que todo mundo faz"), o texto funcionou como aula. Substitui o FIDC do rascunho, por decisão do autor (linha 354 do original: "Próximo texto sobre debentures, em geral"). |
| **3. Tese de fundo** | "Securitizar muda o endereço do risco. Não muda o tamanho dele." É da família da tese-mãe da série ("o risco que sobra muda de endereço, não desaparece", exemplo da LCI no §2 do `BACKWARDS_DESIGN.md`). É a formulação mais literal dela até agora. |
| **4. Erro-alvo** | Achar que o patrimônio separado (ou o nome "agronegócio"/"recebíveis") dilui ou isola o risco do investidor, quando num CRA de devedor único o lastro é a promessa de pagamento de uma empresa só. Gente competente acredita nisso: o caso Raízen mostrou entre 60% e 90% dos CRAs com pessoa física. |
| **5. Ferramenta prática** | Três: (a) as quatro perguntas antes da taxa (quem deve, o que está no lastro, o que fica no meio, quem representa); (b) a fórmula do empate CRA isento × debênture tributada em IPCA+, que corrige a regra de bolso; (c) o PU de um CRI/CRA em IPCA+ descontado por NTN-B + spread. |
| **6. Âncora de autoridade** | Lei nº 14.430/2022, art. 27 (efeitos do patrimônio separado), citada com número na Anatomia. É o dispositivo que o texto inteiro qualifica. Apoio: Gorton & Souleles (2007) para a função do veículo e Cerqueira (tese FD-USP, 2022) para a distinção dos "dois CRAs". |
| **7. Os dois lados do balcão** | Investidor PF (quanto rende, que risco assume, como vota) × **devedor** como emissor econômico (incorporadora, usina, trading), com a securitizadora como veículo. Novidade frente à LCA: há um terceiro lado, os **estruturadores e distribuidores**, que ficam com parte da isenção ("repartida entre mais mãos"). A condição 1 do §4.3 se verifica (a remuneração da estrutura altera o que chega à prateleira), mas o rascunho trata disso em uma frase. Registrado como observação, não como lacuna: o texto nomeia o fato e o liga à resposta do CMN (Res. 5.118), e isso tem consequência para a decisão do leitor. |
| **8. Ponte de série** | Vem da LCA (citada na primeira linha: "prometi que o próximo seria sobre o CRA") → aponta para **debêntures em geral** (decisão do autor). O parágrafo final do rascunho aponta para FIDC e a etapa 4 reescreve. A ponte já está construída em conteúdo: "Economicamente, o CRA corporativo é uma debênture daquela empresa" e a seção "Qual curva usar" já usam a debênture como vizinha. |

## Verificação: a estrutura entrega a competência de saída?

| Seção do rascunho | Movimento(s) | Observação |
| --- | --- | --- |
| Título + deck ("CRI, CRA e o que a securitização realmente separa") | 0 | O deck anuncia a tese pela metade ("o que separa"), sem entregá-la. É aceitável: o título já é a tese ("O Certificado Não Muda o Devedor"). |
| Abertura (continuidade + Raízen + três perguntas) | 1 (modo A, evento datado) + 2 (O Mito: "O nome sugere lavoura..."; tese isolada em negrito) | Fecha com as três perguntas + aforisma, que funcionam como pergunta-âncora. Modo A obriga o movimento 7, que existe ("De volta à Raízen"). |
| "O que são os Certificados de Recebíveis?" + "O patrimônio separado" | 3 (A Anatomia: base legal, emissor, regulador, IR, FGC, caminho em 5 passos, três relações de crédito, art. 27) | Termina na frase-sinal do §5.3: "Até aqui, é o que o prospecto conta na primeira página. O que importa está nas outras duzentas." Usada uma vez só. ✓ |
| "Dois CRAs com o mesmo nome" + "O que fica entre você e o devedor" + "Você vota" | 5 (O Ponto Cego, por contraste com vizinhos nomeados: CRA de carteira × CRA corporativo; LCA × CRA na assembleia) | O núcleo do erro-alvo. Aqui mora a ferramenta 5b (subordinação) em versão estrutural. |
| "O lado de quem emite" | 4 (O Lado de Lá: por que o devedor usa o veículo, divisão da isenção, resposta do CMN) | Movimentos 4 e 5 invertidos, o que o §3 permite. |
| "O lado de quem compra" (conta, risco, liquidez) | 8 (A Prateleira) | Ferramentas 5a e 5b. |
| "Quanto vale hoje" (3 subseções) | 8 (continuação) + extensão de matemática financeira (§4.2) | Ferramenta 5c. Híbrido produto + matemática, como no texto da LCA. |
| "De volta à Raízen" | 7 (Fechamento do Loop, com o desfecho judicial) | ✓ |
| "Fechamento: da sigla ao devedor" | 9 (Síntese + Ponte: tese isolada de novo, generalização lateral) | A ponte atual aponta para FIDC. A etapa 4 troca para debênture (campo 8). |
| "Para continuar aprendendo" | 10 | 4 itens, 3 livros + 1 tese, cada um anotado. Dentro da regra §5.7. ✓ Sem lei na bibliografia. ✓ |

**Conclusão:** a sequência produz a competência do campo 1. As três camadas (devedor →
estrutura → preço) aparecem nessa ordem, e as quatro perguntas de "O risco é o devedor" são a
competência em forma de checklist. A tese aparece isolada no início e no fim (§5.4). ✓

## Notas para as etapas seguintes

1. **Ilustração com a emissão real da Raízen (item 3 do inventário).** O ponto de inserção é
   entre as "três relações de crédito" e "O patrimônio separado", onde o autor deixou o
   marcador. A etapa 3 levanta uma série de CRA da Raízen (securitizadora, agente fiduciário,
   devedor do lastro, instrumento do lastro, garantias). A etapa 4 escreve um parágrafo curto
   que percorre os passos 1-5 com esses nomes.
2. **Ponte e teste de transferência (item 6).** O parágrafo final troca FIDC por debênture. A
   frase "Se o texto funcionou, você consegue dar o próximo passo sozinho" continua, agora
   apontando para a debênture do mesmo devedor.
3. **Gross-up: coerência com o texto da LCA.** A tabela do empate declara "cálculo próprio".
   A etapa 7 recalcula as quatro linhas e a afirmação "só por volta de nove anos os dois erros
   se anulam".
4. **Datas futuras em relação à escrita.** O texto cita fatos de mar-jul/2026 (RE da Raízen,
   homologação em 30/07/2026, preço a 50%). Todos têm fonte na tabela 2.2 do autor. A etapa 7
   confere.

## O que fica de fora

- **FIDC**, que vira no máximo menção lateral. Não é o próximo texto.
- **Fiagro, LIG, CPR como investimento direto**: vizinhos que o texto não precisa para a
  competência de saída.
- **Distribuidor como bloco próprio**: ver campo 7. Fica na frase do rascunho.
- **Mercado secundário em profundidade**: "Liquidez" já cumpre a função em um parágrafo.

## Onde entra graf-NN / diag-NN / info-NN

Restrição do autor (marcador 4): **a Substack não renderiza tabela markdown.** Tabela vira
peça-imagem. Isso vale para as três tabelas do rascunho, não só para a que tem o marcador.
Critério aplicado a cada ponto:

| Peça | Onde | Tipo | Por quê (e por que os outros perderam) |
| --- | --- | --- | --- |
| **diag-01** | "Na LCA havia duas relações de crédito. Aqui há três" (depois do caminho em 5 passos) | Diagrama de fluxo | Relação estrutural entre entidades (devedor → cedente → securitizadora/patrimônio separado → investidor, com agente fiduciário ao lado), sem métrica central → diag (critério 2). graf perde: não há série. info perde: uma peça só carrega a ideia. É o par direto do diag-01 do texto da LCA (duas relações lá, três aqui), e isso reforça a série. Se a etapa 3 fechar os dados da Raízen, os rótulos usam os nomes reais da emissão (item 3 do inventário); se não, usa rótulos genéricos. |
| **diag-02** | Tabela LCI/LCA × CRI/CRA (marcador explícito do autor) | Tabela-imagem | Comparação estrutural de 7 atributos entre dois produtos, sem série numérica → diag (critério 2), renderizada como tabela. graf perde: não há métrica. info perde: é uma comparação só, não uma síntese de várias peças. |
| **graf-01** | Tabela de subordinação (4 cenários de perda) | Tabela-imagem com números | Série numérica real (perda da carteira → perda da subordinada/sênior), gerada pela fórmula do texto → graf (critério 1). Mantém o formato de tabela para preservar o conteúdo do autor. Transformar em curva seria mudança de conteúdo, não de formato. |
| **graf-02** | Tabela do empate (4 prazos) | Tabela-imagem com números | Série numérica (prazo → taxa de empate), cálculo próprio → graf (critério 1). Mesmo raciocínio do graf-01. |
| — info-NN | — | Não se aplica | Nenhuma síntese exige mais de uma peça. Padrão: não tem. |

Formato: tabelas-imagem em Plotly (`go.Table`) com tokens de `../../brand/`, exportadas em
PNG/SVG. A etapa 8 confirma se `prompts-visuais` aceita `go.Table` como `graf`/`diag`. Se não
aceitar, leva ao gate como pendência de formato, não de conteúdo.

## Confirmação dos três pilares

- **Dado**: caso Raízen com números (R$ 65,1 bi, 60-90% PF, PU a 50%), tabela de empate,
  exemplo de PU.
- **Narrativa**: arco Raízen abertura → anatomia → ponto cego → prateleira → volta à Raízen.
- **Visual**: diag-01, diag-02, graf-01, graf-02.
