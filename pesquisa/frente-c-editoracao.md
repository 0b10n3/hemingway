# Frente C — Editoração de texto: fronteiras das três camadas de edição

## 1. As três camadas clássicas

O mercado editorial (EUA/UK e, com adaptações, o mercado pt-BR) reconhece três camadas sequenciais e não sobrepostas. A tabela delimita o escopo de cada uma — essa fronteira é a base das três etapas do pipeline (crítica estrutural → revisão de linha e norma → verificação técnica).

| Camada | Nome pt-BR aproximado | O que toca | O que explicitamente NÃO toca |
|---|---|---|---|
| **Developmental editing** | Edição estrutural / substantiva | Argumento geral, estrutura, ordem das seções, se cada parte serve ao propósito do texto, lacunas lógicas, público-alvo, se algo deve ser cortado, movido ou expandido | Escolha de palavras, ritmo de frase, vírgula, ortografia — nada em nível de frase |
| **Line editing** | Edição de linha/frase | Clareza e fluidez de cada frase e parágrafo, ritmo, tom, voz, redundância, transições locais, coesão | Reestruturação do argumento geral (isso já devia ter sido resolvido); regras formais de norma culta (isso vem depois) |
| **Copy editing** | Revisão de norma/copidesque | Gramática, ortografia, pontuação, concordância, regência, consistência terminológica, formatação (siglas, itálico, numerais), aderência a manual de estilo | Não reescreve estrutura nem estilo de prosa; não questiona se um parágrafo deveria existir |

No mercado editorial em português, o equivalente mais próximo de *copy editing* é o **copidesque** (que no Brasil às vezes também absorve parte da coesão textual, um escopo um pouco mais largo que o *copyediting* anglófono) seguido da **revisão** final, mais restrita, como "pente-fino" [Re-visão de Águia; Revisão Para Quê]. A edição estrutural em pt-BR é descrita como acontecendo "no início do processo de redação, logo após a elaboração do primeiro rascunho" [Re-visão de Águia].

## 2. Por que a ordem developmental → line → copy é a única ordem correta

A lógica é de **custo irrecuperável**: cada camada só faz sentido investir depois que a camada anterior "travou" o material sobre o qual ela trabalha.

- Se você faz *copy editing* (gramática/pontuação) num parágrafo que a edição estrutural ainda vai cortar ou mover, todo o trabalho de correção gramatical é jogado fora — "esforço perdido... corrigir gramática em parágrafos posteriormente cortados por problemas estruturais" [Bernoff].
- *Copy editing* "não chega às causas-raiz dos problemas do manuscrito" — arrumar a sintaxe de uma seção mal-argumentada não a torna bem-argumentada [Bernoff].
- *Line editing* antes do *developmental* tem o mesmo problema em escala menor: polir o ritmo de uma frase que pertence a um parágrafo que será eliminado é desperdício.
- Inverter a ordem também contamina o processo cognitivo do revisor: microdecisões de gramática competem pela atenção que deveria estar em macrodecisões de estrutura, e vice-versa — por isso os frameworks profissionais tratam cada camada como uma passada isolada, não simultânea.

## 3. Erros de norma culta mais comuns em texto técnico/financeiro (não-especialistas em pt)

- **Crase**: confusão entre a preposição "a" e o artigo feminino "a" antes de substantivos femininos ("a vista" vs. "à vista"); teste padrão: substituir o termo feminino por um masculino equivalente — se virar "ao", há crase [Correio Braziliense].
- **Regência verbal/nominal**: verbos que mudam de regência conforme o sentido (ex. "assistir a" vs. "assistir" no sentido de ajudar) são a fonte mais comum de desvio, sobretudo por influência da língua oral [Mundo Escrito].
- **Vírgula em oração reduzida** (gerúndio, particípio, infinitivo): usa-se vírgula quando a reduzida equivale a uma oração adverbial ("Considerando os riscos, o fundo reduziu a exposição."); não se usa quando a reduzida tem valor adjetivo restritivo. Não há regra 100% mecânica — o consenso é de "tendências", não lei fixa [Ciberdúvidas].
- **Siglas na primeira ocorrência**: grafar por extenso seguido da sigla entre parênteses na primeira menção — "Instituto Brasileiro de Geografia e Estatística (IBGE)" — e usar só a sigla depois, em caixa alta [Meu TCC na Prática; ESPM/ABNT].
- **Itálico em estrangeirismos e jargão técnico-financeiro**: regra do Manual de Comunicação do Senado — termo já incorporado ao português (marketing, on-line, design) vai **sem** itálico; termo ainda não incorporado ou que precisa ser traduzido/explicado vai **em itálico**. O próprio manual cita *spread* e *subprime* como exemplos que levam itálico [Senado]. Por extensão, "duration" e "hedge" — jargão técnico não aportuguesado — seguem a mesma regra.

## 4. Fórmulas matemáticas/financeiras para leitor não-especialista

O Manual Editorial do Ipea traz a diretriz mais operacional encontrada: fórmulas devem ser destacadas do corpo do texto (bloco separado, não inline) quando envolvem expoentes/índices; recebem numeração em algarismos arábicos entre parênteses, alinhada à direita; símbolos e variáveis não devem iniciar frase; quando várias expressões aparecem próximas, devem ser separadas por prosa (ou ponto e vírgula) em vez de aglomeradas [Ipea]. Nenhuma fonte encontrada trata explicitamente de "quando traduzir a fórmula em prosa" para leitor leigo — esse ponto não tem diretriz editorial formal consolidada em pt-BR; a prática comum em textos de divulgação é acompanhar toda fórmula em bloco de uma frase equivalente em linguagem natural logo antes ou depois.

## Fontes

- [How a developmental edit differs from a copy edit or line edit, and why that matters — Josh Bernoff](https://bernoff.com/blog/how-a-developmental-edit-differs-from-a-copy-edit-or-line-edit-and-why-that-matters)
- [Difference Between Line Editing, Copyediting, and Developmental Editing](https://amnet-systems.com/difference-between-line-editing-copyediting-and-developmental-editing/)
- [Entenda a diferença entre copidesque, revisão técnica e preparação do texto](https://pamyla-serra.wixsite.com/re-visaodeaguia/single-post/2016/10/29/entenda-a-diferen%C3%A7a-entre-copidesque-revis%C3%A3o-t%C3%A9cnica-e-prepara%C3%A7%C3%A3o-do-texto)
- [A diferença entre preparação e revisão de textos — Revisão Para Quê](https://revisaoparaque.com/blog/diferenca-preparacao-e-revisao-de-textos/)
- [Como usar crase sem dúvidas na norma padrão da língua portuguesa — Correio Braziliense](https://www.correiobraziliense.com.br/cbradar/como-usar-crase-sem-duvidas-na-norma-padrao-da-lingua-portuguesa/)
- [Regência Verbal | Os erros mais frequentes na revisão de textos — Mundo Escrito](https://mundoescrito.com.br/erros-frequentes-regencia-verbal/)
- [Vírgula com orações/expressões de gerúndio — Ciberdúvidas da Língua Portuguesa](https://ciberduvidas.iscte-iul.pt/consultorio/perguntas/virgula-com-oracoesexpressoes-de-gerundio/21876)
- [Siglas no TCC: Regras de Uso e Primeira Menção ABNT — TCC na Prática](https://meutccnapratica.com.br/guia-abnt/siglas)
- [Siglas — Normas ABNT — ESPM](https://normas-abnt.espm.br/index.php?title=Siglas)
- [Estrangeirismo — Manual de Comunicação do Senado](https://www12.senado.leg.br/manualdecomunicacao/estilos/estrangeirismo)
- [Fórmulas — Manual Editorial do Ipea](https://www.ipea.gov.br/sites/pt-br/manualeditorial/padroes-editoriais/padroes-grafico-visuais/formulas)
- [Manual de Redação e Padronização — Poder360 (PDF)](https://extranet.poder360.com.br/wp-content/uploads/2022/08/Manual-Redacao-Poder360-jan2021-1-1.pdf)
