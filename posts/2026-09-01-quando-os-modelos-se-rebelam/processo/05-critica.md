# Crítica developmental — "Quando os Modelos se Rebelam"

Executada pelo agente `critico-editorial` sobre `04-draft-v1.md`, cruzado com
`01-briefing.md` e `02-estrutura.md`.

## Achados

**1. Seção 1 — colisão de ID entre o placeholder real de `graf-01` (seção 3) e um artefato
mal formatado na seção 1.**
`02-estrutura.md` decidiu explicitamente, em "O que fica de fora", que a taxonomia
Teoria/Modelo/Intuição **não** vira peça visual — as duas tabelas nativas do rascunho cobrem
essa comparação. O draft, porém, inseriu um comentário entre colchetes rotulado
`[graf-01: comparativo Teoria x Modelo...]`, formatado como os placeholders visuais reais,
cujo próprio texto diz "não vira peça visual" — contradição de forma — e reutiliza o ID
`graf-01`, já reservado para os dados de Ibovespa/dólar da seção 3. Além disso, nenhuma das
duas tabelas nativas prometidas pela estrutura aparece de fato como tabela no draft, só como
prosa.
Severidade: **alta**.

**2. Fechamento — o parágrafo novo sobre "existem teorias, sim, em domínios fechados" reverte
sem preparo a frase categórica da seção 1 ("Em finanças, o que existe são modelos. Não
teorias.") e usa como exemplo a não-arbitragem, que a própria seção 3 já tinha descrito como
consequência derivada das premissas do modelo, não como teoria autônoma.**
O leitor sai do texto sem saber se a tese é "não existem teorias em finanças" ou "existem
teorias em domínios fechados, e não-arbitragem é uma delas" — as duas posições usam o mesmo
conceito de dois jeitos incompatíveis. Isso não resolve bem a instrução original do autor
(`[tentar reescrever... Existem teorias em financas.]`) — cria inconsistência nova em vez de
matizar a frase categórica.
Severidade: **alta**.

**3. LTCM — a ressalva sobre alavancagem como "escolha humana" mina o clímax retórico
imediatamente anterior, em vez de complementá-lo.**
A seção monta para a frase "aqui está o ponto que eu quero que fique... o erro não estava na
conta". O parágrafo seguinte qualifica essa mesma frase como possível "forma elegante de
tirar a responsabilidade" um parágrafo depois de pedir que ela "fique" com o leitor —
sobreposição de dois eixos causais despachada em sequência imediata, sem transição que
sinalize que são complementares.
Severidade: **média**.

**4. `diag-01` está posicionado antes da narrativa que ele resume**, entregando o mecanismo do
colapso do LTCM (calote russo → fuga para qualidade → spreads divergem → margem → venda
forçada) antes da prosa narrar esse mesmo ciclo — esvazia parte da tensão dramática do
clímax.
Severidade: **média**.

**5. `graf-01` é o único dos três placeholders sem bloco/legenda descritiva própria** — está
embutido numa frase de prosa, sem eixos/período especificados além do `[VERIFICAR]` de fonte,
ao contrário de `ilu-01` e `diag-01`.
Severidade: **baixa**.

**6. Seção 1 acumula quatro posições filosóficas nomeadas antes de qualquer caso financeiro
real ser narrado** — ponto de maior risco de abandono do texto, desproporcional ao papel de
"contexto".
Severidade: **média**.

**7. Abertura — dois parágrafos de contextualização de plataforma (MIT OCW) atrasam o gancho**
que `01-briefing.md` define como a citação em si, não o metadado do curso.
Severidade: **média**.

**8. A nota do target forward de 2008 é adicionada depois do dístico de fechamento de
MacKenzie**, diluindo o beat retórico e estendendo uma seção 3 já carregada.
Severidade: **média**.

## Pontos positivos

- Os três pilares (dado, narrativa, visual) representados nas seções certas.
- `ilu-01` bem posicionado, âncora visual antes da abstração.
- Imagem da alavanca e aforismo final preservados verbatim.
- Seções 5 e 6 entregam exatamente o prometido pela estrutura, sem desvio.

## Veredito

Dois achados de severidade alta atingem a tese central e a promessa estrutural da seção 1 —
por regra do pipeline (`post-substack/SKILL.md`: "se a etapa 5 devolver severidade alta...
volte à etapa 2 antes de seguir"), o texto volta para ajuste de estrutura/draft antes da
revisão de linha.

## Resolução (loop etapa 2 → 4, aplicado nesta mesma passada)

- **Item 1**: removido o artefato `[graf-01: ...]` da seção 1; as duas tabelas nativas
  (Teoria x Modelo; ponto de Derman x filosofia da ciência) reintegradas como tabelas
  markdown reais, sem ID de visual — `02-estrutura.md` atualizado para deixar explícito que
  elas são tabela nativa, nunca placeholder.
- **Item 2**: o parágrafo do Fechamento reescrito para ecoar diretamente a nuance já
  registrada na seção 1 (visão semântica de Suppes/van Fraassen/Giere — teoria também é
  família de modelos, mas finanças mora do lado em que o objeto reage ao modelo), em vez de
  introduzir não-arbitragem como exceção nova e incompatível com a seção 3.
- **Itens 3-8 (média/baixa)**: aplicados na mesma revisão do draft — reordenação de `diag-01`
  para o ponto em que o ciclo é narrado, ressalva de alavancagem integrada antes do clímax em
  vez de depois, abertura cortada direto para a citação, nota do target forward movida para
  antes do dístico de MacKenzie, `graf-01` ganhou bloco de legenda próprio.

`loops_consumidos` incrementado para 1 em `estado.json`.
