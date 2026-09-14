# Laudo — revisão quantitativa (etapa 5a, linha Spoiler)

**Post:** `2026-09-11-partes-dificeis-de-uma-carreira-em-financas-teste-pipeline-v2`
**Documento revisado:** `processo/04-draft-v2.md`
**Documento de apoio:** `processo/03-pesquisa.md`

| Trecho citado | Tipo de fragilidade | Severidade | Pergunta dirigida ao autor |
|---|---|---|---|
| "um modelo de 'Value at Risk' implementado por alguém que não entende a premissa de normalidade por trás dele tende a subestimar sistematicamente a chance de superar exatamente esse nível de perda [...] 'saber implementar' sem entender o que sustenta o cálculo é construir em cima de areia, mesmo que o código rode sem erro" | arcabouço teórico / realidade de mercado | atenção | O caso mais citado de VaR quebrando por causa da premissa de normalidade — o LTCM (1998) — não foi construído por alguém que "não entendia a premissa": Myron Scholes e Robert Merton, coautores do próprio arcabouço teórico de precificação de opções, estavam entre os sócios do fundo. A literatura atribui esse tipo de falha mais a alavancagem, ruptura de correlações sob estresse e incentivos institucionais do que a um gap de conhecimento individual. Você quer manter a moldura de "quem não entende a premissa" sabendo que ela não descreve o episódio histórico mais famoso da própria crítica que está citando, ou prefere qualificar essa ligação (por exemplo, deixando claro que é um risco atual/pessoal de quem implementa hoje, não uma explicação do que aconteceu em 1998/2008)? |
| "tende a subestimar sistematicamente a chance de superar exatamente esse nível de perda" | arcabouço teórico | nitpick | A crítica acadêmica mais central ao VaR não é só que a *frequência* de violação do limite é subestimada — é que o VaR não diz nada sobre a *magnitude* da perda quando o limite é ultrapassado (não é uma medida coerente de risco). O texto foca só na frequência. Foi simplificação deliberada para o público leigo, ou vale mencionar também essa segunda dimensão, já que é o motivo formal pelo qual os reguladores trocaram VaR por Expected Shortfall? |
| "já era o centro do embate entre Nassim Taleb e a defesa acadêmica do modelo" | realidade de mercado | nitpick | A pesquisa (etapa 3) localiza esse embate como debate nominal — Taleb contra Philippe Jorion, 1997 — não uma disputa contra "a academia" como bloco. Generalizar foi escolha de fluidez, ou prefere nomear Jorion explicitamente para não implicar consenso acadêmico monolítico que não existia? |
| "pesquisadores já mostraram que os testes de 'grit' essencialmente medem um traço de personalidade antigo e conhecido (disciplina, no sentido comum), não algo novo" | evidência empírica | atenção | A meta-análise de Credé conclui que os itens de grit se sobrepõem fortemente a Conscienciosidade (Big Five) — mais amplo que "disciplina no sentido comum": inclui organização, senso de dever, busca de realização. Rotular como "disciplina" simplifica o construto de um jeito que pode subestimar o achado. Manter a simplificação por fluidez, ou nomear Conscienciosidade explicitamente? |
| "[Um modelo de VaR / Black-Scholes] é divertido. É pop. Aparece bem no portfólio, aparece bem numa conversa de happy hour." | realidade de mercado | nitpick | Com tutoriais prontos e geração assistida por IA amplamente disponíveis hoje, um VaR ingênuo ou um pricer de Black-Scholes virou projeto de portfólio comoditizado, não necessariamente diferencial em 2026. Leitura pessoal válida, ou essa parte do argumento pode estar um pouco desatualizada frente à saturação atual? |

## Resumo

- **Bloqueante:** 0
- **Atenção:** 2
- **Nitpick:** 3

Nenhum achado invalida o argumento central da seção. As duas fragilidades de "atenção" dizem
respeito a como o texto usa episódios históricos reais (LTCM/2008, meta-análise de Credé)
como munição retórica de um jeito ligeiramente mais simples do que a evidência sustenta. Cabe
ao autor decidir se isso pede hedge adicional ou se o registro essayístico já absorve a
simplificação.
