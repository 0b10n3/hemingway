# 07 — Verificação técnica

Executado pelo agente `verificador-tecnico`. Confere `04-draft-v1.md` contra as fontes de
`03-pesquisa.md`, mais busca direta a fontes primárias quando necessário. Não reescreve o
draft — apenas dá veredito e, quando aplicável, a correção exata a aplicar na etapa 9
(consolidação).

## 1. Números Chague/De-Losso/Giovannetti (day trade)

**✅ Confirmado**, com atribuição correta entre os dois estudos.

- **968.512 pessoas / R$ 9,9 bi de perda agregada / R$ 10.200 de perda média por pessoa** —
  confirmados contra a nota de imprensa oficial da FGV EESP sobre o estudo de 2025 (Chague &
  Giovannetti, "As pandemias de COVID-19 e de day trade no Brasil", *Revista Brasileira de
  Finanças* 23, e202515, 2025):
  https://portal.fgv.br/en/noticias/brazilians-lost-r-99-billion-day-trade-during-covid-19-pandemic-according-study-fgv-eesp
  — "968,512 people", "R$ 9.9 billion", "average gross loss was R$ 10,200 per individual".
  Cálculo de consistência: 9,9 bilhões / 968.512 pessoas = R$ 10.221,87 — bate com o R$ 10.200
  divulgado (a pequena diferença é arredondamento do valor agregado divulgado em bilhões;
  não é inconsistência).
  ```
  9.9e9 / 968512 = 10221.87
  ```
- **97% de perda entre quem persistiu 300+ dias** — confirmado contra `03-pesquisa.md` §2.1,
  que já leu o working paper na íntegra (Chague, De-Losso & Giovannetti, "Day Trading for a
  Living?", SSRN 3423101, 2020): dos 19.646 que começaram entre 2013-2015, 1.551 (7,9%)
  persistiram mais de 300 dias, e 97% desses perderam dinheiro líquido de taxas.
- **Atribuição entre os dois estudos, no draft:** o parágrafo 2 de "O equívoco que a gente vê
  todo dia" atribui corretamente os R$ 9,9 bi / R$ 10.200 / 968.512 ao estudo de 2025
  (Chague & Giovannetti, sem De-Losso) e isola o "97% após 300+ dias" num parágrafo separado,
  introduzido como "Num estudo anterior dos mesmos pesquisadores, com Rodrigo De-Losso" — não
  mistura as duas amostras numa frase só, e sinaliza que são estudos distintos (um é o de
  2020 sobre persistência, outro o de 2025 sobre o agregado pandêmico). Isso resolve
  exatamente o risco apontado no prompt. Nenhuma correção necessária.
- Nota lateral, não bloqueante: a pesquisa (03) registra "pico de participantes ativos/dia
  saltou de ~25 mil para ~108 mil"; a nota de imprensa da FGV fala em "up to 100,000 people
  engaged in day trading daily" — mas esse número **não aparece no draft**, então não gera
  pendência aqui (fica só como observação para quem for revisitar `03-pesquisa.md`).

## 2. SPIVA — percentual e edição

**❓ Não verificável / mantém `[VERIFICAR]`** — o bloqueio de acesso à fonte primária
persiste, mas a checagem adicional aumenta a confiança no dado.

- Tentei acessar diretamente `spglobal.com/spdji/en/documents/spiva/spiva-latin-america-year-end-2025.pdf`,
  a versão em português (`.../spiva-latin-america-year-end-2025-pt.pdf`), a página-artigo
  (`spglobal.com/spdji/en/spiva/article/spiva-latin-america-year-end-2025`) e uma tentativa via
  proxy de leitura (`r.jina.ai`) — **todas retornaram HTTP 403**. O bloqueio de acesso da
  S&P DJI é sistemático, não pontual.
- Consegui, porém, confirmar via busca que **existe** um documento indexado no próprio domínio
  `spglobal.com` com o nome de arquivo `spiva-latin-america-year-end-2025.pdf` (e sua versão em
  português) — isso dá confiança razoável de que a edição correta a citar é **"SPIVA Latin
  America Year-End 2025"**, não uma edição "mid-year" (que também existe como documento
  separado, o que reforça a distinção já registrada em `03-pesquisa.md` entre year-end e
  mid-year).
- O percentual **90,8% em janela de 10 anos** aparece de forma consistente em duas fontes
  jornalísticas independentes (istoedinheiro.com.br e borainvestir.b3.com.br), ambas citando a
  mesma apresentação de Christopher Anguiano (S&P DJI) no evento ETF Day RJ — a mesma dupla de
  fontes já registrada em `03-pesquisa.md`. Não encontrei uma terceira fonte independente que
  não derive dessas duas, nem consegui ler o número diretamente no PDF.
- **Veredito:** mantenho o `[VERIFICAR]` já presente no draft, mas atualizo o que ele precisa
  dizer: o percentual (90,8%) e a edição (SPIVA Latin America Year-End 2025) têm indícios
  fortes e convergentes, mas nenhum deles foi lido diretamente no documento primário — o
  bloqueio de acesso da S&P DJI (HTTP 403) persiste em todas as rotas tentadas.
  `[VERIFICAR: confirmar contra o PDF primário "SPIVA Latin America Year-End 2025" (S&P DJI)
  o percentual de 90,8% de fundos de ações ativos brasileiros perdendo do benchmark em 10
  anos — dado corroborado por duas fontes jornalísticas independentes citando a mesma
  apresentação oficial (Christopher Anguiano, ETF Day RJ), mas não lido diretamente na fonte
  primária por bloqueio de acesso repetido (HTTP 403) em múltiplas tentativas, incluindo
  proxy de leitura]`

## 3. Taleb — obra e ano

**⚠️ Impreciso — falta atribuição; correção proposta.**

- A estratégia "barbell" de concentrar a maior parte do capital em ativos ultraconservadores
  e uma fatia pequena e isolada em apostas de risco extremo é formalizada por Nassim Taleb em
  **_Antifragile: Things That Gain from Disorder_ (2012)** — confirmado por múltiplas fontes
  secundárias consistentes entre si (thepowermoves.com, grahammann.net, quantifiedstrategies
  via Substack) descrevendo o "barbell strategy" como conceito central do livro de 2012,
  associado à tese de antifragilidade. Não encontrei o texto integral do livro para citar
  página exata (mesma limitação já registrada em `03-pesquisa.md` — "não achei trecho textual
  com página exata").
- *The Black Swan* (2007) trata de assimetria e cisnes negros, mas a estratégia de alocação
  "barbell" nomeada e formalizada como tal é de *Antifragile* (2012) — não recomendo citar os
  dois livros como fontes equivalentes do "barbell"; se o autor quiser precisão máxima, a
  atribuição correta é só a *Antifragile*.
- O draft não cita nenhum percentual específico (ex. 90/10) para a alocação — o que é
  tecnicamente seguro, já que esse número circula em resumos de mercado sobre o livro, não
  como citação textual única e verificável (mesma ressalva de `03-pesquisa.md` §5.1). Manter
  assim, sem adicionar percentual.
- **Correção proposta para a etapa 9:** trocar "o autor Nassim Taleb, por exemplo, prefere
  concentrar..." por "o autor Nassim Taleb, por exemplo — em *Antifragile* (2012) —, prefere
  concentrar...". Isso resolve o item 13 de `06-revisao.md` (regra 6, atribuição obra+ano) com
  confiança razoável, mas não altíssima (fonte é secundária, não o texto do livro em si).

## 4. Gloss técnico

**✅ Confirmado**, com uma observação de janela temporal (não é erro, é vigência a monitorar).

- **CDB** — "você empresta dinheiro a um banco e recebe de volta com juros": correto como
  definição de leigo (título de renda fixa emitido por banco, captação via dívida do
  investidor para a instituição).
- **LCI/LCA** — "o mesmo princípio, com isenção de Imposto de Renda para pessoa física":
  confirmado vigente em 2026. A MP 1.303/2025, que propunha tributar esses papéis a partir de
  2026, **caducou em 08/10/2025** sem votação — LCI e LCA seguem isentas de IR para pessoa
  física. Fontes: cobertura de borainvestir.b3.com.br e adrianofreire.com.br sobre o desfecho
  da MP 1.303. Vale registrar que esse é um tema que pode voltar à pauta legislativa — a
  isenção não é uma garantia permanente, é o status vigente na data de checagem (10/08/2026).
- **Tesouro Selic** — "título público pós-fixado, o mais líquido e conservador da família":
  correto e consistente com a caracterização oficial do Tesouro Direto (título indexado à
  Selic, resgate diário, menor volatilidade de preço entre os títulos públicos federais).
- **ETF** — "fundo negociado em bolsa que replica um índice": correto como definição
  majoritária (a maior parte dos ETFs listados no Brasil e no mundo são passivos/indexados);
  simplificação aceitável para gloss de uma frase — existem ETFs ativos, mas isso foge do
  escopo de uma definição curta para leigo.
- **Day trade** — "comprar e vender o mesmo ativo no mesmo dia, tentando lucrar [com] a
  oscilação de preço": correto.
- **Swing trade** — "a mesma lógica do day trade, só que ma[n]t[ém] a posição por alguns dias
  em vez de fechar tudo no mesmo pregão": correto.
- **Derivativos** — "contratos cujo valor deriva do preço de outro ativo": correto,
  definição-padrão.
- **Opções** (gloss acrescentado pela revisão de linha, item 4 de `06-revisao.md`) — "contratos
  que dão o direito, mas não a obrigação, de comprar ou vender um ativo por um preço
  combinado": correto, é a definição-padrão de opção (call/put).
- **SPIVA** — "S&P Indices Versus Active, que a S&P Dow Jones Indices publica todo semestre
  comparando fundos ativos a seus índices de referência": confirmado. A série SPIVA é
  publicada em edições Mid-Year e Year-End (semestrais) tanto para os EUA quanto para a
  América Latina — confirmado pela existência de ambos os documentos indexados no domínio da
  S&P DJI (`spiva-latin-america-mid-year-2025.pdf` e `spiva-latin-america-year-end-2025.pdf`).

## 5. Outros números/afirmações factuais não listados no prompt

### 5.1 "Pace sub-3... um ritmo que só um punhado de atletas profissionais no mundo sustenta"

**⚠️ Impreciso — a analogia exagera a raridade do dado.**

- Um "pace sub-3" (terminar a maratona em menos de 3 horas) é, de fato, um feito de elite —
  mas não é exclusividade de "um punhado de atletas profissionais no mundo". Levantamentos
  agregados de maratonas de participação em massa (dados citados por sub3-marathon.com e
  runnersconnect.net) mostram que aproximadamente **2% a 4,5% dos maratonistas amadores**
  terminam abaixo de 3 horas (com diferença por gênero: ~4% dos homens, ~1% das mulheres) —
  ou seja, milhares de corredores não-profissionais no mundo conseguem esse tempo todos os
  anos. É "território de elite amadora", não algo restrito a atletas profissionais.
  Maratonistas profissionais de fato correm muito mais rápido que isso — as elites mundiais
  fecham a prova entre 2h03 e 2h10, quase uma hora mais rápido que o "sub-3" usado como
  referência no texto.
- **Correção proposta:** ajustar a frase para não dizer "só um punhado de atletas
  profissionais no mundo sustenta" — por exemplo, "um ritmo que só uma fração muito pequena
  dos corredores amadores do planeta consegue sustentar" (mais preciso e ainda serve à
  analogia: o iniciante nem está perto disso). Isso não muda a força da imagem — o argumento
  do post não depende de o pace sub-3 ser exclusivo de profissionais, só de ser muito difícil
  — mas, como está, a frase é factualmente exagerada.
- Fontes usadas: https://www.sub3-marathon.com/how-rare-is-sub-3-a-back-of-the-envelope-estimate/
  e resumo agregando runnersconnect.net/rundreamachieve.com (dados de 2025 sobre maratonas de
  massa). Não é fonte acadêmica única, mas o padrão (2-4,5%) é consistente entre as fontes.

### 5.2 Distâncias de maratona/meia maratona (42 km / 21 km)

**✅ Confirmado como aproximação aceitável.** A distância oficial de maratona é 42,195 km e
de meia maratona 21,0975 km — o arredondamento para "42 quilômetros" e "21 quilômetros" é uso
coloquial padrão em português e não constitui erro técnico digno de nota.

### 5.3 Demais afirmações do texto

Não encontrei outros números ou claims factuais no draft além dos já cobertos acima e pelos
itens 1-4. A seção "Quem são os quenianos do mercado financeiro" e o fechamento são
argumentativos/narrativos, sem claim numérico adicional a verificar.

## Consolidado — `[VERIFICAR]` e `[FAIXA]` para o texto final

- `[VERIFICAR: confirmar contra o PDF primário "SPIVA Latin America Year-End 2025" (S&P DJI)
  o percentual de 90,8% de fundos de ações ativos brasileiros perdendo do benchmark em 10
  anos — dado corroborado por duas fontes jornalísticas independentes citando a mesma
  apresentação oficial (Christopher Anguiano, ETF Day RJ), mas não lido diretamente na fonte
  primária por bloqueio de acesso repetido (HTTP 403) em múltiplas tentativas, incluindo
  proxy de leitura]`

Nenhum item se qualifica como `[FAIXA: ...]` — os dados numéricos centrais (968.512 / R$ 9,9
bi / R$ 10.200 / 97%) são valores pontuais corretamente reportados como tal pelos próprios
estudos-fonte, não faixas mal representadas como ponto único.

## Itens que exigem ação na etapa 9 (consolidação), fora do escopo desta verificação

1. Adicionar atribuição de obra/ano a Taleb: "*Antifragile* (2012)" — ver item 3 acima.
2. Ajustar a frase do pace "sub-3" na abertura para não overstate a raridade — ver item 5.1
   acima (sugestão de redação incluída, mas a decisão final de fraseado é da etapa de
   consolidação/autor, não desta verificação).
