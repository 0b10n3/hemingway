# Etapa 7 — Verificação técnica (agente `verificador-tecnico`)

Post: `2026-10-12-coqueiros-e-cacaueiros` · Linha: **Spoiler**. Aplica-se a verificação de citações e referências. Não se aplicam as verificações de Notas de um Professor: cálculo em `_revisoes/`, dois lados do balcão e regra de referências.
Texto verificado: corpo de `processo/04-draft-v3.md`, da l. 17 em diante. Os números de linha abaixo são os do arquivo v3.
Acessos: 2026-10-12 e 2026-10-13. As fontes primárias em PDF foram baixadas e lidas por inteiro com `pdftotext`: Embrapa Doc. 47, *Tratado* na edição BBB, *Tratado* na edição Varnhagen de 1851, WEF Future of Jobs 2025 completo, Res. CVM 160 consolidada, Chambouleyron 2014 e Garcez/ANPUH. A aritmética foi conferida com `python3`.

**Resumo:** 2 correções factuais (⚠️), as duas com redação exata proposta: a citação "metendo" e a cronologia da vassoura-de-bruxa. Nenhum 📏. Nenhum `[VERIFICAR]` técnico novo. Os dois `[VERIFICAR]` que já estão no texto dependem só do autor. Todas as afirmações quantitativas do WEF foram confirmadas no PDF, com página.

---

## 1. Abertura e coqueiro

**1.1 "O coqueiro não existia no Brasil quando os portugueses chegaram." (l. 31)** ✅ **Confirmado.**
Embrapa Doc. 47 (2002), p. 8: "O coqueiro não existia, no Brasil, quando da sua descoberta pelos portugueses em 1500." Há também uma fonte científica independente: Gunn, Baudouin & Olsen (2011, *PLoS ONE*). Segundo eles, o coco era "unknown in the Caribbean and Atlantic basins until after European colonization". A introdução pré-colombiana vale só para a costa pacífica do Panamá.

**1.2 "Segundo a Embrapa, a primeira introdução aconteceu em 1553, na Bahia, com cocos vindos das ilhas de Cabo Verde." (l. 31)** ✅ **Confirmado na fonte declarada.**
- Embrapa Doc. 47, p. 9: "O coqueiro gigante foi introduzido pela primeira vez no Brasil em 1553, no Estado da Bahia, sendo procedente das ilhas de Cabo Verde." A Tabela 1 (p. 12) repete a informação: 1553 · Gigante · "India ou Sri Lanka" · Ilhas de Cabo Verde · Portugueses · Bahia.
- **Cabo Verde tem confirmação primária independente.** O próprio Gabriel Soares escreve, no mesmo parágrafo de 1587: "Foram os primeiros cocos à Bahia de Cabo Verde". O trecho foi conferido nas edições BBB e Varnhagen.
- **Ressalva sobre 1553.** Não há documento de época para a data. A própria Embrapa diz, em *500 perguntas — Coco*, perg. 345: "não havendo, contudo, relato histórico confirmando a entrada de coco no País nesse período". **Decisão: não vira `[VERIFICAR]`.** A frase atribui a data explicitamente ("Segundo a Embrapa"), e a fonte é a autoridade técnica do tema. A atribuição basta para um Spoiler.

**1.3 "A origem remota provável seria Índia ou o Sri Lanka." (l. 31)** ✅ **Confirmado.**
Embrapa Doc. 47, p. 9: "A origem remota desse material seria a Índia ou Sri Lanka". Gunn et al. (2011) dão confirmação genética: o material atlântico "appear[s] to be of Indian origin". "Origem remota" se refere ao material que chegou ao Brasil, não ao centro de origem da espécie. O texto usa a expressão certa.

**1.4 "O 'coco-da-baía' é imigrante." (l. 31)** ✅ **Confirmado.** O nome vulgar consta da Embrapa Doc. 47: "Nome vulgar- Coqueiro, coco-da-baía".

**1.5 "Em 1587, apenas 34 anos depois dos primeiros cocos" (l. 37)** ✅ **Aritmética confirmada:** 1587 − 1553 = 34 (`python3`). A atribuição "Segundo a Embrapa", seis linhas acima, cobre a data.

**1.6 Gabriel Soares de Sousa: "metendo um coco debaixo da terra", escreveu ele (l. 37)** ⚠️ **Impreciso: a citação entre aspas não reproduz o que o cronista escreveu.**
- **Edição Varnhagen (1851)**, *Tratado descriptivo do Brazil em 1587*, Typographia Universal de Laemmert, cap. XXXIV ("Em que se declara as arvores de Hespanha que se dão na Bahia"). Texto em grafia da época, extraído por OCR do PDF da BBM/USP: "As palmeiras que dão os cocos, se dão na Bahia melhor que na Índia, porque, **mettido** um coco debaixo da terra, a palmeira que d'elle nasce dá coco em cinco e seis annos, e na Índia não dão estas palmas fruto em vinte annos."
- **Edição moderna** (Biblioteca Básica Brasileira, Fundação Darcy Ribeiro/Ed. UnB), Parte II, cap. XXXIV, p. 160: "porque, **metido** um coco debaixo da terra, a palmeira que dele nasce dá coco em cinco e seis anos".
- **"metendo"** só aparece na transcrição indireta da Embrapa Doc. 47 (p. 8), que cita via Bondar (1955) e já traz o trecho alterado: "se dão bem na Bahia", "estas plantas, frutos". As duas edições do *Tratado* dizem "mettido"/"metido".
- **Correção exata (l. 37):**
  - de: `Bastava enterrar um coco: "metendo um coco debaixo da terra", escreveu ele, a palmeira dava frutos em cinco ou seis anos.`
  - para: `Bastava enterrar um coco: "metido um coco debaixo da terra", escreveu ele, a palmeira dava frutos em cinco ou seis anos.`
- Notas, sem ação obrigatória:
  - "cinco ou seis" está fora das aspas, então a paráfrase é legítima. O original diz "cinco e seis".
  - "Na Índia, levava vinte" parafraseia "na Índia não dão estas palmas fruto em vinte anos", ou seja, não davam fruto nem em vinte anos. A paráfrase é aceitável.

**1.7 Grafia "Sousa" (l. 37)** ✅ **Correta.** A edição moderna de referência (BBB) usa "Gabriel Soares de Sousa". A edição Varnhagen de 1851 e a Embrapa usam "Souza", que é ortografia antiga. Manter "Sousa".

**1.8 "Exagero de cronista, provavelmente." (l. 39)** ✅ **É juízo do autor e é compatível com a fonte.** A Embrapa Doc. 47 registra que, no coqueiro gigante, "o florescimento é tardio, ocorrendo normalmente entre seis e oito anos após o plantio". Os "cinco e seis" baianos estão perto do normal. O exagero provável está nos "vinte" da Índia. O texto não especifica qual dos dois números é o exagero, e por isso a frase fica de pé.

**1.9 "É do mesmo jeito que se planta coqueiro no litoral baiano até hoje: o coco cai, alguém abre um buraco…" (l. 41)** — **Confirmação do autor** (observação de viagem). Não é afirmação técnica sobre o plantio comercial e não foi verificada como tal.

**1.10 "Mais de quatro séculos depois" (l. 43)** ✅ 2026 − 1587 = 439 anos.

## 2. Cacau

**2.1 "O cacau, por sua vez, é nosso. Está na Amazônia há milhares de anos." (l. 33)** ✅ **Confirmado, com nuance que não exige mudança.**
- "Milhares de anos": Zarrillo et al. (2018), *Nature Ecology & Evolution*, doi:10.1038/s41559-018-0697-x. Há uso de *T. cacao* há cerca de 5.300 anos no sítio Santa Ana-La Florida, no sudeste do Equador, alto Amazonas.
- Presença nativa na Amazônia brasileira: Chambouleyron (2014, *Revista Complutense de Historia de América* 40), com base em documento de 1656, registra "bosques llenos de cacao" perto de Cametá, no rio Tocantins (Pará).
- Nuance: o centro de origem e de domesticação mais antigo é o alto Amazonas (noroeste da América do Sul), não o Brasil em particular. "É nosso" vale como espécie nativa da Amazônia brasileira, que é o que o texto afirma.
- **Não usar "7 mil anos"**, número do apêndice do rascunho que não tem fonte primária. O texto já não usa.

**2.2 "O cultivo no Brasil provavelmente começou no Pará, no fim do século XVII" (l. 33)** ✅ **Confirmado; o "provavelmente" está bem calibrado.**
Chambouleyron (2014) documenta o começo do cultivo nas décadas de 1670:
- ordens régias de 1675, 1677 e 1678 mandam cultivar cacau "como se hace en Indias de Castilla";
- em 1678, a Coroa reconhece que "se había plantado algún [cacao], particularmente los religiosos de la Compañía";
- o rei chama João Ornelas da Câmara de "la primera persona que dio principios a esas plantas en esa capitanía [Pará]".

Detalhe, sem ação obrigatória: segundo Serafim Leite, citado por Chambouleyron, o jesuíta Bettendorff levou sementes do Pará para o Maranhão em 1674. O começo foi no Estado do Maranhão e Pará, no último quarto do século XVII. Se o autor quiser máxima precisão: `na Amazônia portuguesa (Pará e Maranhão), no fim do século XVII`.

**2.3 "e só virou a cara da Bahia a partir do século XIX" (l. 33)** ✅ **Confirmado.**
Garcez, "Introdução ao estudo dos mecanismos de formação da propriedade no eixo Ilhéus-Itabuna — 1890-1930", *Anais do VIII Simpósio Nacional dos Professores Universitários de História* (ANPUH, 1976):
- a lavoura foi "introduzida na segunda metade do século XVIII";
- exporta regularmente "de 1834 em diante", de 27 t (1834) a 3.503 t (1890);
- "até 1890 o produto não conseguiu ultrapassar os 20% do total das exportações do Estado".

**2.4 "Na Bahia, é verdade, ele também chegou de fora: as sementes vieram do Pará, em 1746." (l. 33)** ✅ **Confirmado.**
Agência FAPESP (Peter Moon, 18/01/2017), sobre Santos et al., *PLOS ONE* (doi:10.1371/journal.pone.0145276): "Cocoa arrived in Bahia in 1746, when Louis Frédéric Warneau, a French settler living in Pará, [sent seeds]… in what is now the municipality of Canavieiras". A data é coerente com a "segunda metade do século XVIII" de Garcez.

**2.5 "No sul da Bahia, ele cresce na cabruca, à sombra da mata" (l. 55)** ✅ Pesquisa FAPESP, "The broom swept" (2006): "cabruca, in which the cacao is planted in the midst of the natural vegetation".

**2.6 "na primeira metade do século XX, o cacau dos arredores de Ilhéus fez do Brasil o segundo maior produtor do mundo" (l. 55)** ✅ **Confirmado, agora com duas fontes independentes.**
- UniDistance Suisse, projeto "Swiss Cacao Traders in Bahia, 1910-1945" (M. Schmitz; orientação de B. C. Schär): "For most of this period, Bahia was the world's second largest producer of cacao behind present-day Ghana."
- **Fonte de época, nova:** Arthur W. Knapp (1923), p. 134: "Brazil, with its Bahia and Para cacao, has now established its position as the second largest producer in the world."
- O texto não diz "durante toda a primeira metade", e por isso não cabe `[FAIXA]`.

**2.7 "Ilhéus, terra de Jorge Amado" (l. 23) e "É o mundo dos coronéis dos romances de Jorge Amado." (l. 57)** ✅ **Confirmado.**
- Simões, "Jorge Amado e Ilhéus em 'via de mão dupla'" (UESC, 2012): "Nascido em Ferradas (1912), então distrito de Itabuna, Jorge Amado, no entanto, viveu a sua infância em Ilhéus." A mesma fonte cita o próprio Amado: "o drama da economia cacaueira, a conquista da terra pelos coronéis feudais no princípio do século".
- Companhia das Letras, *Terras do sem-fim*: "guerra pela posse da terra na região cacaueira do sul da Bahia", com o "coronel Horácio da Silveira"; "Publicado em 1943".
- O recorte temporal (início do século XX) bate com o da frase anterior. "Terra de" é aceitável porque Amado cresceu em Ilhéus, embora tenha nascido em Ferradas.

**2.8 "No fim dos anos 1980, um fungo, a vassoura-de-bruxa, cortou a produção nacional em mais da metade." (l. 59)** ⚠️ **Impreciso na cronologia. A magnitude está confirmada.**
- O fungo **chega** em 1989. Fontes: Pesquisa FAPESP 2006, "Detected in the Ilhéus region in 1989"; Teixeira, Thomazella & Pereira (2015, *PLoS Pathogens*); Agência FAPESP 2017.
- A queda acontece **ao longo dos anos 1990**. Recálculo em `python3`:

| Fonte | Antes | Depois | Queda |
|---|---|---|---|
| Pesquisa FAPESP 2006 | 390 mil t (1988) | ~100 mil t (2000) | −74,4% |
| Meinhardt et al. 2008, *Mol. Plant Pathol.* 9:577–588 | 347 mil t (1988–90) | 141 mil t (1998–2000) | −59,4% |
| Agência FAPESP 2017 | 320 mil t/ano | 190 mil t (1991) | −40,6% |

  Meinhardt foi visto via registro secundário. O DOI da Wiley bloqueia acesso automatizado, e o número não foi reaberto nesta rodada.
- Em 1991, dois anos depois da chegada, a queda ainda não chegava à metade. "No fim dos anos 1980… cortou… em mais da metade" comprime uma década num instante.
- **Correção mínima exata (l. 59):**
  - de: `No fim dos anos 1980, um fungo, a vassoura-de-bruxa, cortou a produção nacional em mais da metade.`
  - para: `No fim dos anos 1980, chegou um fungo, a vassoura-de-bruxa. Ao longo da década seguinte, a produção nacional caiu mais da metade.`
- Nota de causalidade, que fica para o autor e não bloqueia: o relatório CEPLAC 2023, visto só via snippet, associa a queda também a preços baixos e crises hídricas. A formulação proposta ("caiu", em vez de "o fungo cortou") já reduz a atribuição causal única sem mudar o argumento.

## 3. Seção "A nota mede outra coisa" e passagens biográficas

**3.1 Classificação das áreas da matemática (l. 88–90, 94)** — **Convenção do autor, com ressalva explícita no próprio texto** ("Não vou polemizar as fronteiras"). Não há erro técnico a corrigir.
Nitpick para a etapa 6, não bloqueante: "da diferencial à riemanniana" sugere um intervalo, mas a geometria riemanniana é parte da geometria diferencial.

**3.2 Fatos biográficos — confirmação do autor, não `[VERIFICAR]` técnico:**
- as notas de álgebra saíram melhores que as de análise "em vários semestres" (l. 96);
- a primeira iniciação científica foi em sistemas dinâmicos (l. 94);
- foi bem avaliado pela capacidade de ensinar "em todas as equipes" (l. 116);
- o roteiro de viagem: Maraú, Itacaré, Ilhéus (l. 19, 23);
- "No meu caso, o ensino mora na barra…" (l. 152);
- "Eu levei anos…" (l. 178).

## 4. Seção "Como encontrar seus coqueiros"

**4.1 Sigla ANBIMA (l. 122)** ✅ "Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais" confere com o Relatório Anual ANBIMA 2025, seção "Quem somos".

**4.2 Mentoria ANBIMA 2025 (l. 122)** ❓ O nome oficial não foi localizado. Os candidatos levantados na etapa 3 ("Espelho", Rede D&I, eventos de terceiros) não são confirmáveis como o programa do autor. **Manter `[VERIFICAR: nome oficial do programa]`. Só o autor resolve.**

**4.3 Stone & Heen, *Obrigado pelo feedback*, três gatilhos (l. 132)** ✅ **Confirmado.**
- Edição brasileira: Portfolio-Penguin (Companhia das Letras), tradução de Renata Guerra, lançamento em 10/02/2016 segundo a página da editora.
- Rótulos da edição brasileira: "gatilhos de verdade", "gatilhos de relacionamento", "gatilhos de identidade". No original: truth, relationship e identity triggers. Os nomes foram confirmados pelo trecho da editora, visto via índice de busca porque o PDF hoje dá 404, e pelo sumário ("gatilhos de relacionamento").
- As glosas entre parênteses ("isso está errado", "quem é você para me dizer isso?", "isso não combina com quem eu acho que sou") são paráfrases do autor, coerentes com as definições do livro.
- **"Versão invertida" do gatilho de identidade:** o texto **não** a atribui ao livro. A frase começa em nova oração e na voz do autor: "Com coqueiros, acontece uma versão invertida do último". Atribuição limpa; sem ação.

## 5. Seção "Não fique esperando um coqueiro"

**5.1 Cal Newport, *So Good They Can't Ignore You* (l. 142)** ✅ **Confirmado.**
- Ficha: *So Good They Can't Ignore You: Why Skills Trump Passion in the Quest for Work You Love*, Grand Central Publishing (Hachette), 18/09/2012, ISBN 9781455509126, conforme a página da editora.
- Tese: a editora diz que o livro "debunks the long-held belief that 'follow your passion' is good advice".
- "Capital de carreira = skills raras e valiosas" e a ancoragem em prática deliberada ("stretch your abilities beyond where you're comfortable and then receive ruthless feedback") vêm de vários resumos e resenhas convergentes. O texto integral do livro não foi lido nesta rodada. A paráfrase do post é fiel ao que todas as fontes consultadas registram.
- O post cita só o título em inglês. A edição brasileira (*Bom demais para ser ignorado*, Alta Books, com ano e tradutor não confirmados) **não precisa entrar**. Se entrar, `[VERIFICAR: ano/tradutor da edição Alta Books]`.

**5.2 "Alguém teve de trazer os cocos de Cabo Verde e enterrá-los na Bahia" (l. 146)** ✅ Coerente com 1.2 (Gabriel Soares e Embrapa).

**5.3 "Duration, a estrutura de um CRA, como particionar uma tabela no Spark" (l. 144)** — Exemplos de conteúdo técnico, sem afirmação a verificar.

## 6. Seção "Três cacaueiros para plantar agora"

Todas as afirmações abaixo foram conferidas no PDF do WEF, *Future of Jobs Report 2025* (Insight Report, jan. 2025, ISBN 978-2-940631-90-2), com páginas impressas.

**6.1 "estima que 39% das skills essenciais dos trabalhadores vão mudar até 2030" (l. 158)** ✅ **Confirmado.** Fonte: p. 32, seção 3.1, "Overall, employers expect 39% of workers' core skills to change by 2030 (Figure 3.1)… down from 44% in 2023."
Nuance opcional: o número é expectativa dos empregadores ouvidos na pesquisa, não medição. "Estima" é simplificação aceitável.

**6.2 "IA e big data aparecem como as skills de crescimento mais rápido" (l. 158)** ✅ p. 37: "AI and big data top the list as the fastest-growing skills".

**6.3 "o pensamento analítico segue como a skill central mais citada: sete em cada dez empresas a consideram essencial" (l. 158)** ✅ p. 35: "analytical thinking remains the top core skill for employers, with seven out of 10 companies considering it as essential". "Segue" também confere: "As in the two previous editions of this report".

**6.4 "O relatório também observa que a IA generativa vai bem em resumir, redigir e calcular, e ainda tropeça onde é preciso julgamento com nuance." (l. 158)** ✅ **Confirmado no próprio relatório**, Box 3.1, pp. 43–44:
- "GenAI currently remains limited in performing tasks that require physical execution, **nuanced judgment** or hands-on application";
- "where it can assist in **summarizing** complex information, **drafting** text, **performing calculations**, and translation".

"Julgamento com nuance" é tradução literal de "nuanced judgment". A atribuição "o relatório" está correta, porque o box está dentro do relatório. Sem ação obrigatória. Nuance: o box é "research conducted by Indeed for this report" e se baseia numa autoavaliação do GPT-4o. Não precisa constar no post.

**6.5 "a estrutura de garantias por trás de um CRA ou de um CRI" (l. 162)** — Sem afirmação factual específica. A troca de LCI por CRI no v3 está correta como exemplo de estrutura com lastro.

**6.6 "Um modelo de linguagem resume um prospecto em segundos." (l. 162)** — Sem erro. O nitpick da 5a foi confirmado e fica como registro para o autor; não entra no post. Pela **Res. CVM 160/2022, art. 9º, I** (vigente, consolidada até a Res. CVM 226/25), ofertas "destinadas exclusivamente a investidores profissionais" dispensam prospecto. "Prospecto" está em sentido genérico; a decisão é do autor.

## 7. Referências citadas de memória pelo revisor-quant (não entram no post)

- **Deming & Noray (2020)** ✅ "Earnings Dynamics, Changing Job Skills, and STEM Careers", *QJE* 135(4): 1965–2005. O resumo sustenta o uso feito no gate 5a: "Obsolescence lowers the return to experience, flattening the age-earnings profile in faster-changing careers". O prêmio de cursos intensivos em tecnologia (ciência da computação, engenharia, negócios) cai rápido.
- **Dispensa de prospecto CVM** ✅ Res. CVM 160/2022, art. 9º, I. Ver 6.6.

## 8. Placeholders já existentes no texto

- l. 122 `[VERIFICAR: nome oficial do programa]`: autor.
- l. 180 `[VERIFICAR: link da Notas de um Professor]`: autor.

---

## Correções a aplicar na consolidação (⚠️)

| # | Linha | De | Para | Fonte |
|---|---|---|---|---|
| 1 | 37 | `"metendo um coco debaixo da terra"` | `"metido um coco debaixo da terra"` | *Tratado*, cap. XXXIV, ed. Varnhagen 1851 ("mettido") e ed. BBB p. 160 ("metido") |
| 2 | 59 | `No fim dos anos 1980, um fungo, a vassoura-de-bruxa, cortou a produção nacional em mais da metade.` | `No fim dos anos 1980, chegou um fungo, a vassoura-de-bruxa. Ao longo da década seguinte, a produção nacional caiu mais da metade.` | Pesquisa FAPESP 2006; Agência FAPESP 2017; Teixeira et al. 2015 |

## Lista consolidada de marcadores para o texto final

**`[VERIFICAR: ...]`**, ambos já presentes e ambos dependentes do autor:
1. `[VERIFICAR: nome oficial do programa]` (l. 122): nome oficial do programa de mentoria/carreira da ANBIMA em 2025.
2. `[VERIFICAR: link da Notas de um Professor]` (l. 180): URL.

Condicional: só se o autor incluir o título brasileiro do Newport, `[VERIFICAR: ano/tradutor da edição Alta Books de *Bom demais para ser ignorado*]`.

**`[FAIXA: ...]`**: nenhum.

**Confirmações do autor (biográficas, não técnicas):** notas de álgebra × análise "em vários semestres"; IC em sistemas dinâmicos; avaliações nas equipes; roteiro da viagem; frase do T; método de plantio observado no litoral (l. 41).

---

## Tabela de fontes final (links testados com HTTP 200 em 2026-10-13, salvo nota)

Substitui os links quebrados do rascunho:
- Embrapa `cpatc`: falha de SSL; substituído pelo Infoteca.
- InfoAmazonia: 403; substituída por fontes primárias.
- Trecho da Companhia das Letras: 404; substituído pela página do livro.
- Página HTML do WEF: 403 para acesso automatizado; substituída pelo PDF.
- UBC/Zarrillo: 404; substituído pelo artigo na *Nature*.

**Proposta para a tabela de fontes do post:**

| Fonte | Usada para |
|---|---|
| [Siqueira, Aragão & Tupinambá — *A introdução do coqueiro no Brasil* (Embrapa Tabuleiros Costeiros, Documentos 47, 2002)](https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/866659/1/Documentos47-1.pdf) | Ausência do coqueiro em 1500; 1553, Cabo Verde; origem remota Índia/Sri Lanka |
| [Gabriel Soares de Sousa — *Tratado descritivo do Brasil em 1587* (Biblioteca Básica Brasileira, Fundação Darcy Ribeiro/Ed. UnB), Parte II, cap. XXXIV](https://fundar.org.br/wp-content/uploads/2021/06/tratado-descritivo-do-brasil-em-1587.pdf) | Citação de 1587 ("metido um coco debaixo da terra") |
| [Agência FAPESP — "Scientists uncover the genetic history of cocoa in Brazil" (Peter Moon, 2017)](https://agencia.fapesp.br/scientists-uncover-the-genetic-history-of-cocoa-in-brazil/24635) | Sementes do Pará para a Bahia em 1746; vassoura-de-bruxa em 1989 |
| [Pesquisa FAPESP — "The broom swept" (2006)](https://revistapesquisa.fapesp.br/en/the-broom-swept/) | Cabruca; queda de 390 mil t (1988) para ~100 mil t (2000) |
| [UniDistance Suisse — Swiss Cacao Traders in Bahia, 1910–1945](https://unidistance.ch/en/history/research-project/swiss-cacao-traders-in-bahia-19101945) | Brasil segundo maior produtor na primeira metade do séc. XX |
| [Fórum Econômico Mundial — *Future of Jobs Report 2025* (PDF)](https://reports.weforum.org/docs/WEF_Future_of_Jobs_Report_2025.pdf) | 39% (p. 32); pensamento analítico, 7 em 10 (p. 35); IA e big data (p. 37); limites da IA generativa (Box 3.1, pp. 43–44) |
| [Cal Newport — *So Good They Can't Ignore You* (Grand Central Publishing, 2012)](https://www.hachettebookgroup.com/titles/cal-newport/so-good-they-cant-ignore-you/9781455509126/) | Hipótese da paixão; capital de carreira; prática deliberada |
| [Douglas Stone & Sheila Heen — *Obrigado pelo feedback* (Portfolio-Penguin, 2016)](https://www.companhiadasletras.com.br/livro/9788582850268/obrigado-pelo-feedback) | Gatilhos de verdade, relacionamento e identidade |

**Fontes de verificação, para o processo e não para o post:**

| Fonte | Uso | Link |
|---|---|---|
| *Tratado*, ed. Varnhagen (Laemmert, 1851), BBM/USP | "mettido"; grafia "Souza" | https://digital.bbm.usp.br/bitstream/bbm/4795/1/017204_COMPLETO.pdf |
| Embrapa Doc. 47, registro | Ficha | https://www.infoteca.cnptia.embrapa.br/infoteca/handle/doc/866659 |
| Embrapa, *500 perguntas — Coco*, cap. 8 | 1553 sem relato histórico | https://www.infoteca.cnptia.embrapa.br/infoteca/bitstream/doc/1106579/1/8.Recursosgeneticos.pdf |
| Gunn, Baudouin & Olsen 2011, *PLoS ONE* | Coco ausente no Atlântico pré-colonial | https://pmc.ncbi.nlm.nih.gov/articles/PMC3120816 |
| Zarrillo et al. 2018, *Nature Ecol. Evol.* | ~5.300 anos de uso de cacau, alto Amazonas | https://www.nature.com/articles/s41559-018-0697-x |
| Chambouleyron 2014, *Rev. Complutense de Hist. de América* 40 | Cultivo no Pará/Maranhão, décadas de 1670; cacau silvestre no Tocantins em 1656 | https://revistas.ucm.es/index.php/RCHA/article/download/46341/44360/78398 |
| Santos et al., *PLOS ONE* | Base genética do cacau baiano | https://doi.org/10.1371/journal.pone.0145276 |
| Garcez, Anais ANPUH (1976) | Exportações baianas de 1834 a 1890 | https://www.anpuh.org.br/uploads/anais-simposios/pdf/2018-12/1545757173_007ad1c287f376669737a323707287a0.pdf |
| Knapp (1923), p. 134 | Brasil segundo produtor (fonte de época) | https://tekniskkulturarv.dk/book/cb59e273-58ac-4ed3-a9cc-8c239dd876de?page=152 |
| Teixeira, Thomazella & Pereira 2015, *PLoS Pathogens* | Vassoura-de-bruxa em 1989; −70% | https://pmc.ncbi.nlm.nih.gov/articles/PMC4619654/ |
| Meinhardt et al. 2008, *Mol. Plant Pathol.* 9:577–588 | 347 mil → 141 mil t | Registro secundário; não reaberto nesta rodada (DOI da Wiley com 403 para acesso automatizado) |
| Simões (UESC, 2012) | Jorge Amado: Ferradas/Ilhéus; "coronéis feudais" | https://www.uesc.br/icer/artigos/jorgeamadoilheus.pdf |
| Companhia das Letras, *Terras do sem-fim* | Coronéis, região cacaueira, 1943 | https://www.companhiadasletras.com.br/livro/9788535912524/terras-do-sem-fim |
| Indeed Hiring Lab × WEF (2025) | Origem do Box 3.1 | https://hiringlab.indeed.com/2025/01/28/world-economic-forum-joint-research/ |
| ANBIMA, Relatório Anual 2025 | Nome por extenso da ANBIMA | https://www.anbima.com.br/relatorioanual/2025/quem-somos.html |
| Deming & Noray 2020, *QJE* | Gate 5a | https://ideas.repec.org/a/oup/qjecon/v135y2020i4p1965-2005..html |
| Res. CVM 160/2022, consolidada, art. 9º, I | Dispensa de prospecto (gate 5a) | https://conteudo.cvm.gov.br/export/sites/cvm/legislacao/resolucoes/anexos/100/resol160consolid.pdf |

Links da etapa 3 que hoje estão quebrados e não devem ser usados:
- `news.ubc.ca/2018/11/05/...` (404);
- `wiki.pestinfo.org/...` (conexão recusada);
- `companhiadasletras.com.br/trechos/75009.pdf` (404);
- `cpatc.embrapa.br/download/Documentos47.pdf` (SSL);
- InfoAmazonia (403).
