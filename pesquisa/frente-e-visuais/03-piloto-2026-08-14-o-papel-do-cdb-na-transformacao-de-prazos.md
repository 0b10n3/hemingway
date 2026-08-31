# Fase C — Piloto: cadeia nova sobre um post já publicado

Post: `2026-08-14-o-papel-do-cdb-na-transformacao-de-prazos` (Notas de um Professor), `ilu-01`.
**Nenhum entregável do post foi alterado** — `post.md`, `ilustracoes.md` e `graficos.md`
continuam exatamente como publicados. Este arquivo só registra o exercício de rodar a cadeia
nova (briefing v2 + Passo 7 + adaptador de gerador) e comparar com o que está publicado,
usando o diagnóstico da Fase A como régua.

Por que este post e não outro: a Fase A (`01-diagnostico.md`, teste 1) apontou `ilu-01` deste
post como o caso mais claro de Camada 1 não usada — o texto nomeia **"o outro lado do
balcão"** como título de seção, e o prompt publicado ignora essa imagem em favor de um
vocabulário genérico de "fio de luz atravessando um monólito".

---

## O que já existia antes deste piloto

`references/exemplos-prompts.md` já continha, desde a auditoria-2026 (Fases 1–2, antes desta
revisão), um conceito de validação para este mesmo `ilu-01` — "os dois lados do balcão" —
rodando o método `briefing-ilustracao.md` v2 até o Passo 6. **Esse conceito não é deste
piloto**, é material herdado; o que este piloto acrescenta é (a) o Passo 7, que não existia
quando aquele conceito foi escrito, e (b) o veredito formal contra os critérios da Fase A e
contra o prompt publicado, lado a lado.

## Prompt publicado (o que está em `ilustracoes.md` hoje, inalterado)

Resumo (texto completo em `posts/2026-08-14-.../ilustracoes.md`): "fio de luz volt
(`#1FE07A`) que atravessa uma estrutura escura dividida em duas metades... um emblema
discreto no centro marcando a área de ALM". Nenhum objeto do texto aparece — nem balcão, nem
depósito, nem financiamento. Paleta é do sistema aposentado (`marca/tokens.json` — obsidian/
volt), que já é esperado para um post pré-31/08 (Fase A, teste 3) e não é o achado aqui; o
achado é o vocabulário genérico.

## Cadeia nova, Passos 1–6 (herdados de `exemplos-prompts.md`, resumidos)

- **Camada 1 (autor):** "o outro lado do balcão" — título de seção; *"Para o investidor, o
  CDB é ativo... Para o banco que o emite, é o oposto — é passivo, é dívida."*
- **Camada 2 (objetos):** balcão, financiamento imobiliário (citado no texto como destino do
  dinheiro), conta corrente.
- **Camada 3 (precisão):** compulsório 21% à vista vs. 20% a prazo; FGC R$ 250 mil/R$ 1 milhão
  a cada 4 anos; "transformação de maturidade" (termo do Bacen, Relatório de Estabilidade
  Financeira, abr/2018); Lei nº 4.728/1965.
- **Frase que a peça carrega:** muitos depósitos curtos, do lado do investidor, viram um
  financiamento longo do outro lado do balcão — é o mesmo dinheiro, o balcão é a linha que
  separa os dois papéis.
- **Motor:** extensão (balcão = linha de separação entre domínios, convenção de linha de
  terreno do desenho técnico) → cruzamento (balcão × financiamento imobiliário: o que a viga
  sustenta é a casa do texto) → torção (não desenhar "transformação" com seta/engrenagem —
  desenhar a mesma extensão duas vezes, fatiada em onze unidades acima e inteira numa viga
  abaixo, porque é o mesmo dinheiro com outro prazo, não dinheiro novo).
- **Estrutura de metáfora:** fusão — balcão e estrutura são um objeto só, atravessando a
  linha.
- **Descartes:** duas barras comparando 21%/20% de compulsório rejeitadas explicitamente por
  ser gráfico com dado real, não ilustração — o critério de `diag-NN` vs. `ilu-NN` (teste de
  arquitetura da Fase A) já estava sendo aplicado aqui antes de existir como regra escrita na
  etapa 2.

## Passo 7 — Composição de cena (novo, escrito agora)

Objetos: um balcão em corte (espessura visível, não linha simples), atravessando toda a
largura da prancha na altura média — a linha que separa os dois domínios. Acima dele, onze
retângulos idênticos e curtos, em fileira — os depósitos de curto prazo. Abaixo, uma única
viga longa, comprimento equivalente à soma dos onze — o financiamento. Sobre a viga, a
elevação frontal de uma casa simples.

Disposição espacial: simetria vertical em torno do balcão — domínio de cima (retângulos
curtos, repetição) contra domínio de baixo (uma peça só, contínua), o contraste de contagem
*é* o argumento, não precisa de seta. Primeiro plano: as duas cotas de medida (uma curta, uma
longa) — são o que o olho compara primeiro, antes mesmo de reconhecer a casa. Fundo: grade de
pontos de baixíssima densidade nas margens, só respiro.

Ponto de acento: lime marca só a cota curta, acima do balcão — "a medida da liquidez que o
depositor abriu mão". Um único ponto, no lugar exato onde a Camada 3 (a precisão) entra na
cena sem virar número escrito.

Frase que a composição prova: a mesma frase do Passo 2 — o mesmo comprimento total, repartido
em onze unidades curtas de um lado, inteiro do outro lado da mesma linha.

*(Aplicar o Passo 7 depois do conceito já fechado, como fizemos aqui, mostra que ele não muda
o resultado quando o Passo 6 já foi bem feito — a "tradução material que fecha o conceito" que
`exemplos-prompts.md` já registrava é, na prática, a mesma composição descrita acima em outras
palavras. O valor do Passo 7 não é mudar este caso: é dar a quem for revisar depois um campo
nomeado para auditar essa parte do raciocínio sem precisar reconstruí-la a partir do prompt
final.)*

## Prompt final (herdado de `exemplos-prompts.md`, gerador declarado)

Ver `references/exemplos-prompts.md`, seção "`ilu-01` — os dois lados do balcão", "Prompt
(Nano Banana Pro)" — não duplicado aqui para não criar uma terceira cópia do mesmo prompt
(regra de fonte única). Já nomeia o gerador no próprio cabeçalho, cumprindo a exigência nova
de `revisao-editorial/SKILL.md` item 9.

---

## Veredito, contra os critérios da Fase A

| Critério (Fase A / `briefing-ilustracao.md`) | Prompt publicado | Prompt novo |
|---|---|---|
| Usa Camada 1 do autor (o balcão)? | Não | Sim |
| Teste da troca (serviria pra qualquer texto de "mecanismo financeiro")? | Reprova — fio genérico e monólito servem para qualquer post do gênero | Passa — balcão em corte + equivalência de comprimento é específico deste argumento |
| Teste do substantivo (objeto concreto do texto)? | Reprova — nó/fio/monólito não vêm do texto | Passa — balcão, financiamento, casa vêm das Camadas 1–2 |
| Estilo bate com a linha editorial (Notas de um Professor → desenho técnico esquemático)? | Não — usa o registro "dark minimalist/glow" do sistema antigo | Sim — projeção ortogonal, linha de construção, cota, sem perspectiva |
| Paleta no sistema de marca atual (Forest/Grove/Lime)? | Não (sistema aposentado, esperado para post pré-31/08) | Sim |
| Gerador declarado no cabeçalho? | Não (convenção não existia) | Sim |

**Conclusão do piloto:** a cadeia nova, com o Passo 7 incluído, produz um resultado
auditável e superior nos critérios que a própria Fase A usou para avaliar o sistema atual — e
o Passo 7 não trocou o conceito, só deu nome a uma parte do raciocínio que já estava
implícita no Passo 6. Isso é evidência a favor de manter o Passo 7 como está (leve, sem
arquivo próprio) em vez de expandir para uma etapa mais pesada.

## O que fica `[VERIFICAR]` ou depende de teste real — não escondido

1. **Este prompt nunca foi rodado no Nano Banana Pro de verdade.** Nem o publicado
   originalmente passou por este piloto — este documento compara texto de prompt contra
   critério escrito, não imagem gerada contra critério visual. A validação real só acontece
   quando alguém rodar o prompt e olhar o resultado.
2. **Dimensão da capa Substack (1456×816)** continua `[VERIFICAR]` — convergência de fontes
   secundárias, página oficial de suporte bloqueou fetch automático (confirmado de novo nesta
   sessão).
3. **Variantes LinkedIn (1200×627 feature, 1080×1350 feed)** nunca foram geradas nem testadas
   contra o comportamento real de recorte do LinkedIn — specs de fonte secundária.
4. **`flux-1-1-pro.md` e `midjourney-v6-1.md`** são inteiramente não-validados — parâmetros
   (`guidance_scale`, `--stylize`, `--sref` etc.) vêm do relatório de pesquisa, que por sua vez
   cita fontes terciárias. Nenhuma peça foi gerada com nenhum dos dois.
5. **O Gate de Tufte novo** (`checklist-graficos.md`) não foi testado contra nenhum `graf-NN`
   neste piloto — este post não tem gráfico ativo (só `ilu-01`). O achado real de
   `2026-08-14/graf-01` sem `rangemode="tozero"` continua sem correção, no backlog (depende de
   primeiro resolver o `marca/tokens.json` morto).
6. **A ressalva sobre a §6 do relatório** (citação fabricada) não foi investigada além do que
   já está em `02-proposta.md` — não tentei confirmar ou refutar a hipótese de alucinação com
   mais profundidade, só sinalizei o risco.

## Lembrete operacional

Skills alteradas (`prompts-visuais`, `revisao-editorial`) só carregam de verdade numa sessão
nova do Claude Code. Se for usar `/post-substack` ou a skill `prompts-visuais` isoladamente
para validar o Passo 7 ou o adaptador de gerador na prática, reinicie a sessão primeiro.
