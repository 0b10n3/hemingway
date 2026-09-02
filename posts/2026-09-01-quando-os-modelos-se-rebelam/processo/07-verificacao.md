# Verificação técnica — rodada 3 (fechamento)

Fonte: `04-draft-v1.md` (draft desta rodada). Não redescobre o que `03-pesquisa.md` já
reconfirmou contra fonte primária — só os cinco pontos pedidos para esta etapa, com veredito
de fechamento.

## 1. Título do livro de Derman — "Models. Behaving. Badly." vs "Models.Behaving.Badly."

**⚠️ Impreciso — corrigir para `Models.Behaving.Badly.` (sem espaços após os pontos).**

Confirmado contra quatro fontes de catálogo/editora, todas convergentes:

- Simon & Schuster, página oficial do editor (Free Press): "Models.Behaving.Badly." —
  [simonandschuster.com/books/Models-Behaving-Badly/Emanuel-Derman/9781439164990](https://www.simonandschuster.com/books/Models-Behaving-Badly/Emanuel-Derman/9781439164990)
- Amazon, capa do hardcover, ISBN-13 9781439164983 (Free Press, 25/10/2011): título grafado
  "Models.Behaving.Badly" na capa —
  [amazon.com/dp/1439164983](https://www.amazon.com/Models-Behaving-Badly-Confusing-Illusion-Reality-Disaster/dp/1439164983)
- Apple Books e ebooks.com, ambos "Models.Behaving.Badly." —
  [books.apple.com/us/book/models-behaving-badly/id427556312](https://books.apple.com/us/book/models-behaving-badly/id427556312),
  [ebooks.com/en-us/book/673297/models-behaving-badly/emanuel-derman](https://www.ebooks.com/en-us/book/673297/models-behaving-badly/emanuel-derman/)

Nenhuma fonte de catálogo usa espaço depois do ponto. O draft (linha 43 e linha 403,
bibliografia) tem "*Models. Behaving. Badly.*" com espaços — trocar as duas ocorrências para
"*Models.Behaving.Badly.*" sem espaços.

## 2. Citação de Kempthorne — tentativa adicional (transcrição de vídeo)

**❓ Não verificável — mantém `[VERIFICAR]`, agora com achado adicional que reforça a dúvida em
vez de resolvê-la.**

Além de reconfirmar que a página do MIT OCW da Lecture 3 segue atribuindo a aula a "Dr.
Choongbum Lee" (não Kempthorne) —
[ocw.mit.edu/.../resources/lecture-3-probability-theory/](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/lecture-3-probability-theory/),
acesso 02/09/2026 —, esta rodada foi além do que as duas rodadas anteriores fizeram: baixei a
legenda/transcrição real (não gerada automaticamente) do vídeo da Lecture 3 no YouTube
([youtube.com/watch?v=f9XFM8YLccg](https://www.youtube.com/watch?v=f9XFM8YLccg)) e busquei a
frase da moeda no texto completo (13.120 linhas de VTT). **A frase não aparece em lugar nenhum
da aula.** Não há menção a "coin", "flip", "toss", "biased" nem qualquer variante próxima ao
exemplo da moeda com 100 caras seguidas.

Fui além ainda: como a citação é sobre "retorno à média", testei as aulas de Kempthorne que
tratam de séries temporais e são o lugar temático mais plausível para esse exemplo — Lecture 6
(Regression Analysis), Lecture 8 (Time Series Analysis I), Lecture 9 (Volatility Modeling, via
transcrição oficial em PDF da versão 2024/18.642) e Lecture 12 (Time Series Analysis III).
Encontrei, na Lecture 8, Kempthorne discutindo precisamente o conceito de "mean reversion" ("a
ponto para o qual você reverte muda" — ligação temática real com a ideia do rascunho), mas sem
nenhum exemplo de moeda em lugar nenhum das quatro aulas checadas.

**Conclusão:** a citação não é rastreável a nenhuma aula específica do curso 18.S096/18.642
testada até agora (Lecture 3, 6, 8, 9, 12) — nem pela transcrição real, nem pela atribuição
oficial de instrutor. Isso é mais forte do que a pendência das rodadas anteriores (que só
apontava "instrutor errado"): agora há evidência de que a frase, tal como está no rascunho, não
está em nenhuma das aulas mais prováveis do curso. Recomendação para a consolidação: manter
`[VERIFICAR]`, mas considerar a alternativa mais segura de não atribuir a fala a "um dos
professores do curso" com implicação de fonte rastreável — ou trocar por paráfrase sem aspas
diretas, já que a citação literal não resiste a esta verificação.

## 3. Seis hipóteses de Black–Scholes / definição de VaR / 'convergence trade' — sem mudança

**✅ Confirmado — nada mudou na reescrita desta rodada, vereditos anteriores seguem valendo.**

- **Black–Scholes** (linhas 148–153 do draft): lista seis premissas — GBM sem saltos,
  volatilidade constante, taxa livre de risco constante e conhecida, ausência de custo de
  transação/imposto, rebalanceamento contínuo possível, liquidez ilimitada (venda a
  descoberto livre + divisibilidade infinita). O texto usa "entre outras coisas" — não afirma
  exaustividade — então a ausência explícita de "sem dividendos" (item que aparece em algumas
  listas didáticas, ex. Hull) não é erro, é omissão coberta pela ressalva. Consistente com o
  artigo original de Black & Scholes (1973) e com a apresentação padrão em livros-texto.
- **VaR** (linha 242): "estimativa estatística da perda máxima esperada num horizonte de
  tempo, com certa probabilidade" — é a formulação simplificada padrão (compare RiskMetrics:
  "an estimate of the maximum loss...over a given time interval...at a given confidence
  level"). Tecnicamente o VaR é um limiar de perda que só é excedido com probabilidade
  (1-confiança), não literalmente "a perda máxima" — mas essa é a simplificação universal em
  textos de divulgação e o parênteses já qualifica com "certa probabilidade". Aceitável como
  está.
- **'Convergence trade'** (linha 224): "aposta de que dois preços parecidos convergem" — gloss
  correto e proporcional ao uso no texto (exemplo on-the-run/off-the-run logo em seguida).

## 4. Alavancagem e nocional do LTCM — números reescritos nesta rodada

**⚠️ Impreciso — os números individuais batem com a fonte primária, mas a frase junta duas
datas diferentes (patrimônio de 01/01/1998 e ativos de 31/08/1998) como se fossem uma única
fotografia de "início de 1998". Corrigir a atribuição temporal, não os valores.**

Fonte primária: President's Working Group on Financial Markets, *Hedge Funds, Leverage, and
the Lessons of Long-Term Capital Management* (abril de 1999), espelho CFTC —
[cftc.gov/sites/default/files/tm/tmhedgefundreport.htm](https://www.cftc.gov/sites/default/files/tm/tmhedgefundreport.htm),
acesso 02/09/2026. Texto integral confirmado nesta rodada:

> "LTCM's balance sheet leverage was 28-to-1 at the end of 1997."
>
> "With regard to leverage, the LTCM Fund's balance sheet on August 31, 1998, included over
> $125 billion in assets. Even using the January 1, 1998, equity capital figure of $4.8
> billion, this level of assets still implies a balance-sheet leverage ratio of more than
> 25-to-1."
>
> "The notional amount of LTCM's total OTC derivatives position was $1.3 trillion at the end
> of 1997 and $1.5 trillion at the end of 1998."

Conferindo a conta: 125e9 / 4.8e9 = 26,04 — bate com ">25-to-1" (`python3` confirma).

**O que o draft (linhas 233–240) faz:** "...seguia acima de 25 para 1 no início de 1998,
quando operava com um patrimônio de cerca de US$4,8 bilhões contra mais de US$125 bilhões em
ativos..." — a frase liga "início de 1998" tanto ao patrimônio quanto aos ativos, como se
fossem medidos no mesmo momento. **Não são.** O relatório é explícito: o patrimônio de
US$4,8bi é de 1º de janeiro de 1998; os mais de US$125bi em ativos são do balanço de **31 de
agosto de 1998** — a véspera da crise russa, oito meses depois. O próprio relatório monta essa
comparação de propósito ("Even using the January 1, 1998, equity capital figure...") para
mostrar que, mesmo usando o patrimônio (maior, mais antigo) contra os ativos (mais recentes,
já na reta final antes do colapso), a alavancagem continuava acima de 25:1 — é um argumento
retórico deliberado, não uma fotografia de um único instante.

**Correção proposta** (não reescrevo o draft, isso é da consolidação): separar as datas
explicitamente, por exemplo —

"o fundo fechou 1997 já em 28 para 1. Usando o patrimônio de US$4,8 bilhões do início de 1998
contra os mais de US$125 bilhões em ativos que ainda carregava em 31 de agosto de 1998 —
véspera da crise —, a alavancagem seguia acima de 25 para 1. O nocional de derivativos de
balcão do fundo era de US$1,3 trilhões ao fim de 1997, e chegou a US$1,5 trilhões ao fim de
1998."

Os quatro valores em si (28:1, >25:1, US$4,8bi, >US$125bi, US$1,3tri, US$1,5tri) estão todos
corretos e batem exatamente com a fonte primária — não é erro de número, é erro de amarração
temporal entre dois deles.

## 5. Parágrafo do target forward — segurança factual

**✅ Confirmado como seguro.** O parágrafo (linhas 195–209) cita apenas: (a) a perda da
Aracruz de US$2,13 bilhões, com Fato Relevante de 03/11/2008 como fonte — já reconfirmado em
`03-pesquisa.md`; (b) a incorporação da Sadia pela Perdigão, dando origem à BRF — fato
institucional público, não numérico, não carece de nota; (c) o `[VERIFICAR]` explícito sobre
a métrica agregada de mercado, com a nota já correta explicando por que BIS (~US$25bi,
estimativa de perda) e BCB/CETIP (~US$37bi, exposição/delta) não são diretamente comparáveis.
O texto não afirma nenhum número único de mercado em prosa — só o `[VERIFICAR]`. Nada a
corrigir; a nota de `03-pesquisa.md` está refletida com precisão no draft.

---

## Resumo para a consolidação

| # | Item | Veredito | Ação |
|---|---|---|---|
| 1 | Título "Models.Behaving.Badly." | ⚠️ Impreciso | Remover espaços nas duas ocorrências (linha 43 e bibliografia) |
| 2 | Citação de Kempthorne | ❓ Não verificável | Manter `[VERIFICAR]`; achado novo (transcrição real não contém a frase em nenhuma das 5 aulas testadas) fortalece a dúvida |
| 3 | 6 hipóteses BS / VaR / convergence trade | ✅ Confirmado | Nenhuma mudança |
| 4 | Alavancagem/nocional LTCM | ⚠️ Impreciso | Separar data do patrimônio (01/01/1998) da data dos ativos (31/08/1998) — valores em si corretos |
| 5 | Parágrafo target forward | ✅ Confirmado seguro | Nenhuma mudança |

### `[VERIFICAR]` / `[FAIXA]` consolidados para o texto final

- `[VERIFICAR: a atribuição da citação de abertura (moeda/retorno à média) a Peter Kempthorne
  não se sustenta — a página do MIT OCW e a transcrição real do vídeo da Lecture 3
  (Probability Theory, instrutor Dr. Choongbum Lee) não contêm essa frase; testadas também as
  aulas de Kempthorne mais prováveis por tema (Lecture 6, 8, 9, 12) sem sucesso. Considerar
  remover a atribuição a um professor específico ou não usar aspas diretas.]`
- `[VERIFICAR: a faixa exata de exposição/perda do mercado brasileiro de target forward em
  2008 (BIS ~US$25bi de perda estimada; BCB/CETIP ~US$37bi de exposição/delta) mede coisas
  possivelmente diferentes entre si — não comprimir num número único sem decidir qual métrica
  citar.]`

Nenhum item novo desta rodada vira `[FAIXA: ...]` — os dois pontos quantitativos revisados
(título do livro, alavancagem/nocional do LTCM) são correções de exatidão pontual, não faixas.
