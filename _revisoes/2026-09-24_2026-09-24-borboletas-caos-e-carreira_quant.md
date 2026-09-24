# Revisão quantitativa — 2026-09-24-borboletas-caos-e-carreira

Etapa 5a do pipeline `/post-substack` (somente leitura, linha editorial Spoiler). Foco:
realismo de mercado e rigor teórico/empírico das afirmações sobre finanças, mercado de
trabalho e mercado financeiro. Não avalio estrutura argumentativa (já feita na etapa 5) nem
fonte/cálculo pontual (etapa 7, `verificador-tecnico`) — a etapa 3 (pesquisa) já sinalizou a
composição exata do "70%" de requalificação Febraban como candidato a `[VERIFICAR]` lá, não
repito esse ponto aqui.

| Trecho citado | Tipo de fragilidade | Severidade | Pergunta dirigida ao autor |
|---|---|---|---|
| "Tarefa rotineira. Relatório. Documento. Se você está no começo da carreira, releia essa lista com calma. É uma boa descrição do que se pede de um estagiário ou analista no primeiro ano." | evidência empírica | atenção | A Pesquisa Febraban mede automação/IA no banco como um todo (majoritariamente operações, atendimento, back office), sem quebra por função ou nível hierárquico. A ponte para "isso descreve o trabalho de estagiário/analista júnior" é uma leitura sua sobre o dado agregado, não um achado direto da pesquisa. Vale marcar explicitamente que é interpretação sua (ex.: "eu leio isso como...") em vez de apresentar como se a pesquisa já tivesse feito esse recorte? |
| Parágrafo inteiro do princípio 4, do "Ao mesmo tempo, 42% dos bancos..." até "...invista no que não se deprecia" | evidência empírica | atenção | As funções mais procuradas citadas pela própria Febraban (dev de software, engenheiro de IA, engenheiro de dados, arquiteto corporativo, engenheiro de DevOps) são papéis de especialização técnica — mais próximos de "ferramenta específica" do que de "fundamento" na dicotomia que você propõe duas frases depois. Como você concilia o dado (mercado contratando mais para papéis de ferramenta/engenharia específica) com a conclusão de que o mercado está premiando fundamentos e não ferramentas? Vale uma frase reconciliando os dois, ou prefere manter os dois lados lado a lado sem costurar essa tensão? |
| "Vender uma ação pouco antes de ela subir não torna a decisão ruim, dependendo da informação que você tinha na hora." | arcabouço teórico | atenção | O conceito de *resulting* (Duke) foi cunhado para decisões isoladas com desfecho estocástico e sem viés sistemático conhecido (pôquer). Em mesa de operações, existe um viés comportamental documentado — o *disposition effect* (Shefrin & Statman, 1985) — em que vender vencedores cedo demais é um padrão sistemático, não aleatório, e é considerado erro de processo justamente quando se repete. Um único trade isolado é compatível com a leitura que você propõe; um padrão repetido de "vender antes de subir" já não seria só "resulting" — seria evidência do próprio viés. Você quer marcar essa diferença (evento único vs. padrão repetido) no texto, ou prefere manter o exemplo isolado como está, contando com o leitor entender o contexto? |
| "Se você começasse amanhã do zero, sem nome, sem contatos, conseguiria refazer o que fez? Se a resposta for sim, não foi sorte." (filtro de Housel) | arcabouço teórico | atenção | Na prática de mercado, separar sorte de habilidade estatisticamente é difícil mesmo com dados — a literatura de avaliação de gestores (ex.: Fama & French, "Luck versus Skill in the Cross-Section of Mutual Fund Returns", 2010) mostra que é preciso track record longo para distinguir alpha de ruído, porque a razão sinal-ruído em retornos é baixa. Uma pergunta introspectiva de "eu conseguiria refazer isso?" não resolve esse problema estatístico — é uma heurística de bom senso, não um substituto para evidência. Você quer manter o filtro como heurística prática (deixando implícito que não é prova estatística), ou vale uma ressalva de uma linha sobre esse limite? |
| "O relatório Future of Jobs 2025 do Fórum Econômico Mundial indica que os empregadores esperam que 39% das habilidades essenciais dos trabalhadores mudem até 2030." | evidência empírica | nitpick | A própria pesquisa de apoio (etapa 3) registra que esse número caiu frente à edição de 2023 (44%), e o WEF descreve a disrupção como "estabilizando, ainda que em nível alto" — leitura oposta a "está tudo mudando rápido". Como o 39% está sendo usado para reforçar a urgência da IA como perturbação, vale citar essa nuance (ou é intencional manter só o número absoluto, sem a tendência)? |
| "Lá fora, o sinal é parecido." (ponte entre Febraban, específica de bancos brasileiros, e WEF Future of Jobs, cross-setorial global) | realidade de mercado | nitpick | O WEF Future of Jobs é um relatório cross-setorial (todas as indústrias, todos os países), não específico de finanças ou bancos. Ao apresentá-lo como "sinal parecido" ao dado bancário brasileiro, a intenção é dizer que a tendência é geral (e finanças não é exceção), ou você quer que o leitor entenda como corroboração direta e específica do que a Febraban mostrou para bancos? Vale uma palavra deixando explícito que é um sinal de escopo diferente (mercado de trabalho global, não financeiro especificamente)? |
| "Annie Duke, ex-campeã mundial de pôquer, deu nome a um dos erros mais comuns de quem trabalha com mercado: *resulting*." | realidade de mercado | nitpick | O trabalho de Duke em *Thinking in Bets* trata de tomada de decisão em geral (pôquer, negócios, política), não é um estudo especificamente sobre profissionais de mercado financeiro. Atribuir a ela a caracterização de "erro mais comum de quem trabalha com mercado" é uma extensão sua (razoável, já que decisões de mercado também são probabilísticas) ou você quer dar a entender que a pesquisa dela foi sobre esse público específico? |

## Resumo

- **Bloqueante:** 0
- **Atenção:** 4
- **Nitpick:** 3

Nenhum item bloqueante — nada aqui, na leitura desta revisão, compromete a credibilidade
técnica do texto a ponto de impedir a etapa 6. Os quatro itens de atenção giram em torno de um
mesmo padrão: dados agregados de mercado de trabalho/bancário (Febraban, WEF) e heurísticas de
avaliação de decisão (resulting, filtro de repetibilidade de Housel) sendo aplicados a
contextos mais específicos (carreira de entrada em finanças, mesa de operações) do que os
dados/conceitos originais cobrem — generalização razoável para um ensaio, mas que um leitor
com bagagem de mercado financeiro pode questionar. Os três nitpicks são detalhes de
enquadramento (framing seletivo de uma tendência, escopo de uma fonte, atribuição de uma
caracterização) que não mudam a conclusão do texto.

## Resposta do autor

*(em aberto — nenhum item é bloqueante, então o pipeline segue para a etapa 6; itens de
atenção e nitpick ficam visíveis para o gate humano, etapa 10, decidir se quer tratá-los.)*
