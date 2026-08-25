# Estrutura — Dividir para não correr risco

Arco completo (`tecnicas-narrativas.md`), porque o texto tem 2+ fontes/casos (Banco Master,
taxonomia CRI/LIG/LCI, dados de mercado B3/XP, artigo acadêmico Ho & Saunders) e fechamento
ensaístico (CTA + gancho, conforme `01-briefing.md`).

## 1. "O que uma LCI realmente faz" — **gancho + contexto**

- **O que prova:** planta a cena datada (liquidação do Banco Master, nov/2025, FGC
  desembolsando ~R$ 44 bi) e a pergunta que o resto do texto responde ("de quem é o risco que
  você assume ao comprar uma LCI?"). Também nomeia e descarta, de saída, a explicação ingênua
  ("versão hollywoodiana da renda fixa") que o texto vai desmontar.
- **Ato:** gancho (cena) → contexto (a pergunta que já era antiga antes do Master).

## 2. "O que é a LCI, rapidamente" — **contexto**

- **O que prova:** estabelece o vocabulário mínimo compartilhado (base legal, isenção de IR,
  FGC, carência) — o que "qualquer material de corretora conta". Existe para que a seção 3
  possa contrastar com isso sem parar para redefinir termos básicos.
- **Ato:** contexto. Fecha com transição explícita ("o interessante começa agora") que já
  demarca a virada para ação crescente.

## 3. "Por que o banco emite LCI" — **ação crescente + clímax**

- **O que prova:** o argumento central. Taxonomia CRI (securitização, sem FGC) → LIG
  (covered bond, patrimônio de afetação) → LCI (dívida comum do banco, sem segregação) mostra
  por que a resposta intuitiva está errada. Citação de Ho & Saunders (1981) sustenta o banco
  como "dealer avesso a risco" com autoridade acadêmica nomeada (regra 6 do guia). Fecha com o
  retorno ao Banco Master (agora com o porquê já estabelecido) e a resposta regulatória (CMN,
  Ativo de Referência, abr/2026) — o clímax factual que confirma a tese em tempo real.
- **Ato:** ação crescente (a taxonomia) → clímax (Master + resposta regulatória).
- **Pilar:** narrativa (é a seção que carrega o "porquê", não só o "o quê").

## 4. "Quanto a LCI movimenta no mercado" — **resolução (parte 1: escala)**

- **O que prova:** o mecanismo descrito na seção 3 não é teórico nem marginal — estoque de LCI
  quase quadruplicou (R$ 141 bi → R$ 544 bi, dez/2020-jun/2026), reage visivelmente a
  mudanças de regra (recuo após Resoluções CMN 5.118/5.119 em 2024, aceleração após MP
  1.303/2025), e foi o produto de captação bancária que mais cresceu em 2025.
- **Ato:** resolução, primeira metade — sai da teoria para o tamanho real do fenômeno.
- **Pilar:** dado. Entra aqui o **`graf-01`** (evolução do estoque de LCI, R$ bi,
  dez/2020-jun/2026, já especificado pelo autor no material bruto) — é gráfico de série
  temporal com evento regulatório marcado, informação genuína, não decoração (regra 9 do
  guia). Fica como gráfico Plotly (não ilustração): o dado é a informação, não precisa de
  metáfora visual — ver `marca-syntaxis` na etapa 8 para os tokens de cor/tipografia.

## 5. "Onde a LCI entra no seu portfólio" — **resolução (parte 2: aplicação)**

- **O que prova:** converte o entendimento estrutural em decisão prática — cálculo de
  gross-up para comparar LCI a CDB, posicionamento de risco relativo (LCI/CDB/Tesouro <
  LIG < CRI/CRA), e a implicação de diversificar entre emissores acima do teto do FGC.
- **Ato:** resolução, segunda metade — "e daí, o que eu faço com isso".

## 6. "O risco tem endereço" — **fechamento**

- **O que prova:** fecha o arco devolvendo a frase-título como quase-aforismo ("não é favor.
  é spread. o risco que sobra nunca desaparece: só muda de endereço"), generaliza o
  raciocínio para a LCA (mesma base legal, mesma lógica), e cumpre o fechamento ensaístico
  obrigatório: CTA de compartilhamento + gancho para o próximo texto (CRI).
- **Ato:** fechamento. Nenhum ajuste necessário — já está na voz certa (§4.1 do guia).

## 7. "Para continuar aprendendo" — **referências, fora do arco narrativo**

- Lista de fontes citadas ao longo do texto. Vira insumo direto para a etapa 3 (pesquisa) e a
  etapa 7 (verificação técnica) — não é seção de argumento, não entra na análise de arco.

## Três pilares — confirmação

- **Dado:** seção 4 (estoque de LCI, crescimento, participação de mercado) + números
  espalhados nas seções 1 e 3 (R$ 44 bi do FGC, teto de R$ 250 mil/R$ 1 milhão).
- **Narrativa:** seções 1 e 3 (o porquê estrutural — taxonomia CRI/LIG/LCI, dealer avesso a
  risco).
- **Visual:** `graf-01` na seção 4.

Os três representados; nenhum pilar ausente.

## O que fica de fora (deliberadamente)

- Ilustração (`ilu-NN`) adicional: o argumento é estrutural/taxonômico, não construído em
  torno de uma imagem sustentada (ver `01-briefing.md`, "não há metáfora de imagem
  sustentada"). Um gráfico de dados já cobre o pilar visual; forçar uma ilustração só para
  igualar o padrão dos dois posts anteriores seria decoração, não argumento (regra 9 do
  guia, antipadrão 7.1).
- Mecânica detalhada de CRI e LIG além do necessário para a taxonomia comparativa — o texto
  anuncia explicitamente que isso fica para o próximo post ("semana que vem a gente abre o
  CRI"); aprofundar aqui duplicaria conteúdo futuro.
- Qualquer decisão sobre o formato da isca paga de R$ 9,90 (`MARKETING_REVIEW.md` §5) — fora
  do escopo desta etapa; sinalizado em `01-briefing.md` como observação para o autor, não
  como tarefa de estrutura.
- Reconstrução forense do caso Banco Master além do que o texto já usa (data, valor pago pelo
  FGC, causa) — o post não é sobre o Master, é sobre o que o Master revela sobre a LCI.

## Pendências para pesquisa/verificação (não resolvidas nesta etapa)

- Os dois marcadores `[VALIDAR: ...]` da seção 5 (faixa de equivalência LCI 90% CDI ↔ CDB
  105%-118% CDI; ponto de virada em prazos muito longos) precisam de segunda fonte —
  encaminhar para a etapa 3 (pesquisa) e confirmar/recalcular na etapa 7 (verificação
  técnica).
- Todos os números e citações legais/regulatórias (Leis 10.931/2004, 11.033/2004 art. 3º,
  13.097/2015, 9.514/1997; Resoluções CMN 5.118/5.119, 5.215/2025, 5.295/5.296; dados B3/XP
  de estoque de LCI; Ho & Saunders 1981) ficam para verificação técnica (etapa 7) — nada aqui
  foi conferido contra fonte primária ainda.
