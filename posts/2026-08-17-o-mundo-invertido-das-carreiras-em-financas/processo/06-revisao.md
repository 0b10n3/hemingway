# 06 — Revisão de linha e norma culta

Revisão sobre `processo/04-draft-v1.md`. Contexto: `estilo/estilo-autoral.md` §3 (regras 1-9) e
§4.1 (voz ensaística), `pesquisa/frente-d-antipadroes-ia-ptbr.md`,
`.claude/skills/voz-syntaxis/references/antipadroes.md`, e o achado de baixa severidade
registrado em `processo/05-critica.md` ("Reverificação pós-revisão") sobre o duplo sentido de
"produto". Executada pelo agente `revisor-gramatical`.

Nenhum problema estrutural novo foi encontrado — a estrutura de `02-estrutura.md`/`05-critica.md`
foi respeitada e não é reaberta aqui. Checklist de tiques de IA foi conferido inteiro: nenhuma
ocorrência de abertura clichê, hedging genérico, tríade previsível, fecho vago, negrito/itálico
de ênfase ou pergunta retórica decorativa. O texto está limpo nesse quesito.

## Seção 1 — "A conta batia. O produto, não." (parágrafo 2)

**Original:** "Foi a parte mais difícil da dissertação inteira — não a matemática, que eu
dominava, mas entender o produto."

**Corrigido:** "Foi a parte mais difícil da dissertação inteira — não a matemática, que eu
dominava, mas o instrumento em si."

**Motivo (`linha`):** dois problemas resolvidos com uma só troca. (1) Paralelismo sintático:
"não [substantivo: a matemática] ... mas [oração: entender o produto]" mistura registro nominal
e verbal no mesmo par "não X, mas Y"; trocar para "o instrumento em si" restaura o paralelismo
nominal. (2) Desambiguação apontada em `05-critica.md`: "produto" aqui significa o instrumento
financeiro (as opções da dissertação); duas seções depois, "produto" volta a significar produto
de investimento/régua de risco. "Instrumento" já é usado na frase seguinte do mesmo parágrafo
("aquele instrumento eu só fui entender de verdade"), então a troca reforça insistência lexical
(o autor já repete palavra-chave deliberadamente — movimento Hemingway #5) sem tocar no
argumento nem no título da seção (jogo de palavras estrutural com "conta"/"produto").

## Seção 2 — "Bem-vindo à linha Spoiler" e fechamento

**Original:** "o mundo invertido, o Upside Down de *Stranger Things*"
**Corrigido:** "o mundo invertido, o *Upside Down* de *Stranger Things*"

**Original (fechamento do post):** "Menos Upside Down, mais alicerce."
**Corrigido:** "Menos *Upside Down*, mais alicerce."

**Motivo (`norma`):** regra 4 do guia permite itálico para estrangeirismo isolado (não para
ênfase). "Upside Down" é nome próprio em inglês, não naturalizado em português, tratado no
mesmo nível que *Stranger Things* na mesma frase — inconsistente deixá-lo sem itálico ao lado do
título que já recebe o tratamento correto.

## Seção 3 — "A segunda lacuna: dinheiro no tempo"

**Original:** "o pré-requisito listado pela GFMI, provedora de treinamento profissional de
risco, para o curso dela sobre VaR"

**Sinalização (`norma`, regra 1):** GFMI aparece sem a expansão da sigla na primeira ocorrência
— só a descrição funcional. O guia estabelece o padrão de expandir a sigla, não só descrevê-la
funcionalmente. Não há fonte confirmada nesta etapa para o nome completo por trás de "GFMI" —
fica `[VERIFICAR: nome completo da sigla GFMI]` para a etapa 7 (verificação técnica).

**Original:** "O currículo do CFA (a certificação mais reconhecida do mercado de investimentos)"

**Sinalização (`norma`, regra 1, severidade mais baixa):** mesmo padrão — só gloss funcional,
sem expandir "Chartered Financial Analyst". Menos crítico que GFMI (CFA é sigla amplamente
reconhecida mesmo fora do texto), mas para consistência com a regra 1: "CFA (Chartered
Financial Analyst, a certificação mais reconhecida do mercado de investimentos)" —
`[VERIFICAR]` na etapa 7 antes de aplicar.

**Original:** "provedora de treinamento profissional de risco"
**Corrigido (opcional):** "provedora de treinamento profissional em risco"
**Motivo (`linha`):** "treinamento ... de risco" pode ser lido, numa primeira passada, como
"treinamento arriscado" em vez de "treinamento na área de risco". "Em risco" fecha essa leitura
errada. Baixa prioridade.

## Seção 4 — "Não é só quem veio da academia"

**Original:** "um estágio, direto numa mesa que cuida do risco de VaR de um banco, cercado de
modelos complexos"

**Corrigido:** "um estágio, direto numa mesa que cuida do VaR de um banco, cercado de modelos
complexos"

**Motivo (`linha`):** redundância. VaR (Value at Risk, já glossado na seção 3: "a métrica que
estima quanto uma carteira pode perder num cenário ruim") já é, por definição, uma métrica de
risco — "risco de VaR" soa como "o risco do risco". Cortar "risco de" resolve sem alterar o
sentido nem a estrutura da frase.

**Observação opcional, não bloqueante (`linha`):** "quantos estagiários caem exatamente nessa
cadeira" ecoa "sentar na cadeira" da seção 3 (repetição de palavra-chave coerente com a voz do
autor, não é erro). Mas "cair... nessa cadeira" fica perto da expressão idiomática "cair de
cadeira" (= ser óbvio), de sentido oposto ao pretendido. O contexto deixa claro que não é o
idiotismo, então não é correção obrigatória — só fica sinalizado para o autor decidir se quer
manter (reforça o eco) ou trocar (ex.: "caem exatamente nesse buraco").

## Seção "O convite"

**Original:** "Compreender de fato o que ela significa é outra história, e é justamente essa a
ferramenta mais usada em todo o mercado financeiro."

**Corrigido:** "Compreender de fato o que ela significa é outra história — e é justamente o
valor do dinheiro no tempo a ferramenta mais usada em todo o mercado financeiro."

**Motivo (`norma` — concordância/coesão referencial):** o pronome "essa" (feminino) não tem
antecedente feminino coerente com o sentido pretendido. As candidatas femininas mais próximas
são "a fórmula" e "a conta" (mencionadas na frase anterior), mas o que se quer dizer é que "o
valor do dinheiro no tempo" (substantivo masculino, tópico do parágrafo, mencionado três frases
antes) é a ferramenta mais usada do mercado. A discordância de gênero somada à distância do
referente pretendido cria ambiguidade real. Nomear o referente resolve sem mudar o argumento.

## Observação de baixa prioridade, não bloqueante — Seção 1, parágrafo 1

**Trecho:** "eu tinha bastante curiosidade por processos estocásticos (a matemática que descreve
fenômenos que evoluem no tempo com uma boa dose de aleatoriedade — o preço de uma ação, por
exemplo) aplicados ao mercado."

A concordância resolve a referência corretamente ("aplicados", masculino plural, só pode remeter
a "processos estocásticos"), então não é erro. Mas o parêntese longo entre o substantivo e seu
particípio pode exigir uma segunda leitura. Sinalizado como possível ajuste de ritmo (mover
"aplicados ao mercado" para logo após "processos estocásticos"), sem ser correção obrigatória —
é decisão de ritmo, não de norma.

## Resumo

Onze itens ao todo: 4 `norma` (2 itálico de estrangeirismo em "Upside Down", 1 concordância de
gênero/coesão referencial na seção final, 1 par de siglas sem expansão completa — GFMI e CFA,
sinalizados para verificação técnica) e 7 `linha` (paralelismo + desambiguação de "produto" na
seção 1, redundância "risco de VaR" na seção 4, mais três observações opcionais de baixa
prioridade não bloqueantes). Nenhum tique de IA da lista em `pesquisa/frente-d-antipadroes-ia-ptbr.md`
sobreviveu à revisão — nenhuma ocorrência encontrada. Nenhuma estrutura foi reaberta; todos os
achados de `05-critica.md` seguem resolvidos, e o achado de baixa severidade sobre "produto" tem
aqui uma correção pontual (seção 1, sem reescrever frase).

Itens `[VERIFICAR]` para a etapa 7: nome completo da sigla GFMI; expansão de CFA (Chartered
Financial Analyst).
