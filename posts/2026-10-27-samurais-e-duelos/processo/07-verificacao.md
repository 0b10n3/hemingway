# Etapa 7: Verificação técnica (agente `verificador-tecnico`)

Laudo do agente, gravado pelo pipeline principal sem alteração de conteúdo.

Post: `2026-10-27-samurais-e-duelos` · Linha: **Spoiler**. Aplica-se a verificação de citações, referências, datas e contas. Não se aplicam as verificações próprias de Notas de um Professor (cálculo em `_revisoes/`, dois lados do balcão, regra de referências).

**Texto verificado.** Corpo de `processo/04-draft-v2.md` (l. 41–223) na forma que terá depois da etapa 9:
- todas as `norma` de `06-revisao.md`;
- as 9 ★;
- "distinga ganho de perda" (l. 100 e 210);
- "livrarias do país" (l. 82);
- título em caixa de frase.

Os números de linha são os do v2.

**Acessos.** Reconferido em 2026-10-28:
- koten.net (seções 001, 105, 109, 238 e 501);
- Hurst/EJMAS;
- ja.wikipedia (宮本武蔵, 五輪書, 独行道, 五大) e en.wikipedia (*Dokkōdō*, *The Book of Five Rings*);
- MLIT (Reigandō e Ganryūjima), Yamaguchi Tourism e Tofugu;
- jamesclear.com, c2.com (Cunningham), Sosnowski e *Dawn*;
- Martins Fontes, getAbstract e Estante Virtual;
- cobertura do 2º turno.

O que não foi reaberto usa `03-pesquisa.md` (acesso em 2026-10-26) e vem marcado "(03-pesquisa)". As contas foram feitas com `python3`.

**Edição Kikuchi: sem acesso ao texto.** O Google Books devolveu captcha, a API do Google Books estava com a cota esgotada, e a web não tem trecho citado da tradução. Nenhuma passagem pôde ser conferida na redação de Kikuchi. Tudo o que é Musashi foi conferido no **original japonês** (koten.net). Só os metadados da edição estão confirmados.

**Legenda:** **OK** (confirmado) · **CORRIGIR** (impreciso, com correção mínima) · **DEF. IMPRECISA** (definição ou caracterização) · **[VERIFICAR]** (não verificável) · **FAIXA** (o valor certo é um intervalo).

---

## Resumo

| Classe | Itens |
|---|---|
| Contas | **13 conferidas, 13 certas, 0 erradas** |
| CORRIGIR | 4. (a) aposto "(o nome original do livro)", que vem da `norma` da l. 90: o título 五輪書 não é de Musashi. (b) "quase todo conselho de Musashi" (l. 86): o escopo de Hurst são as nove regras. (c) "Por volta dos 30" (l. 60): o original diz "passados os 30"; leve. (d) "três décadas… treinando, pintando…" (l. 196): omite duas campanhas militares; leve, o autor decide. |
| DEF. IMPRECISA | 2 com correção (l. 180 "de influência zen"; l. 166 "porta", opcional) e 1 só de registro (l. 136, "título pós-fixado" com "taxa constante"; não é erro grosseiro, e o autor já decidiu). |
| [VERIFICAR] | 5, todos com troca sustentada por fonte já proposta. Se a troca entrar, o [VERIFICAR] some. (e) "um dos nomes mais temidos do Japão" (l. 46). (f) "enquanto distribuía o que tinha aos discípulos" (l. 112). (g) "o duelo mais famoso da história do Japão" (l. 196). (h) redação Kikuchi das quatro regras (l. 98–104). (i) "A primeira tradução para o inglês" (l. 74), de baixa prioridade. |
| FAIXA | 0 |
| Ajustes opcionais (o texto está OK) | "lealdade, consenso…" (l. 82); preceito 12 (l. 112); ano do Greene e autoria e data do Tofugu nas Referências (preenchimento, não erro) |

---

## Contas (python3)

| Afirmação | Cálculo | Resultado | Veredito |
|---|---|---|---|
| "1,01³⁶⁵ ≈ 37,8" (l. 132) | `1.01**365` | 37,7834 | **OK** |
| "cerca de 37 vezes melhor" (l. 130) | é o número de Clear ("thirty-seven times") | 37,78, truncado | **OK**. A atribuição a Clear está correta. "37 × 37,8" fica no gate (nitpick da 5a). |
| "Dez mil dias são uns 27 anos" (l. 138) | 10000/365,25 | 27,38 | **OK** |
| "do primeiro duelo, aos 13, até… perto dos 50… quase quatro décadas" (l. 140) | 50 − 13 | 37 | **OK** |
| "três décadas" entre duelo e livro (l. 54) | 1643 − 1612 | 31 | **OK** |
| "passou as três décadas seguintes" (l. 196) | 1612 → 1643 | 31 | **OK** |
| "quase quatro séculos antes da moda" (l. 112) | 2026 − 1645; 2010 a 2014 − 1645 | 381; 365 a 369 | **OK** (abaixo de 400 em qualquer data da "moda") |
| "Uma semana antes de morrer" (l. 112) | 正保2年5月12日 → 5月19日 | 7 dias | **OK** |
| "dois anos antes de morrer" (l. 52) | Kan'ei 20 (1643), mês 10 → 13/06/1645 | 2 anos-calendário; menos de 2 anos corridos | **OK** como arredondamento. É o mesmo do MLIT ("the last two years of his life"). A conversão gregoriana exata do 10º mês de 1643 não foi verificada. |
| 29 em 1612 | contagem japonesa com nascimento em 1584: ano − 1584 + 1 | 29 | **OK** |
| 60 em 1643 | idem | 60 | **OK** |
| 13 → 1596; 50 → 1633 (não estão no texto; vale para o diag-01) | idem | 1596; 1633 | **OK**. Na etapa 8, o diag-01 usa 1596 e ~1633, não 1597 e 1634 (D15). |
| Morte (享年) | 1645 − 1584 + 1 | 62 | consistente com a ja.wikipedia ("享年62") |

---

## 1. Abertura (l. 46–70)

**1.1 "numa ilhota entre Kyushu e Honshu" (l. 46): OK.** A Yamaguchi Tourism diz 「関門海峡にポツンと浮かぶ…小島」 e 「周囲約1,6㎞の小島」 ([yamaguchi-tourism.jp](https://yamaguchi-tourism.jp/feature/ganryujima)). O MLIT descreve "this tiny, uninhabited island", em Hikoshima, Shimonoseki ([MLIT R5-00678, FY2023](https://www.mlit.go.jp/tagengo-db/R5-00678.html)). O estreito de Kanmon separa Honshu de Kyushu.

**1.2 "espadachim de 29 anos" (l. 46): OK** na convenção decidida. Hurst: "The most famous encounter, however, occurred when Musashi was 29" ([Hurst/EJMAS](https://ejmas.com/jalt/jaltart_Hurst_0101.htm)). O *Sekai Daihyakka* também dá 29 (03-pesquisa, Kotobank). A explicação da contagem vem na l. 52 e cobre o número. A data de 1612 vem de fontes tardias (武公伝 1755, 二天記 1776, D1). É a data tradicional, e o texto a usa de forma coerente. Sem ação.

**1.3 "espada de madeira talhada de um remo" (l. 46): OK**, como tradição.
- O 武公伝 diz 「武蔵は、太郎右衛門から艫を貰い削り木刀を作った」 ([ja.wikipedia 宮本武蔵](https://ja.wikipedia.org/wiki/宮本武蔵)).
- O MLIT diz "Some versions of the story state that Musashi fashioned a rough wooden sword from an oar".
- O 小倉碑文 (1654) registra só a espada de madeira (03-pesquisa).

**1.4 Kojirō, "instrutor de esgrima de um senhor feudal" (l. 46): OK.** Hurst: "a skilled fencer who was an instructor for Hosokawa Tadaoki". A tabela da ja.wikipedia diz 「細川忠興が登用した豊前の兵法師範」, a partir do 武公伝.

**1.5 "e um dos nomes mais temidos do Japão" (l. 46): [VERIFICAR].** Nenhuma fonte encontrada; a 03-pesquisa também não achou. O que as fontes sustentam:
- o 小倉碑文 o chama de 「兵術の達人」 (ja.wikipedia);
- o MLIT diz "Some believe he was the greater swordsman";
- Hurst diz "a skilled fencer".

Correção mínima, à escolha:
- (a) cortar "e um dos nomes mais temidos do Japão";
- (b) trocar por "e, para alguns, espadachim melhor que o próprio Musashi" (MLIT).

Se ficar como está: `[VERIFICAR: fonte para "um dos nomes mais temidos do Japão"]`.

**1.6 "Kojirō morreu ali, na areia" (l. 46): OK.** O texto oficial do MLIT diz "As Kojirō gasped his last breath on the sand". A versão concorrente (D2, 沼田家記, 1672) muda **quem** matou: 「蘇生した小次郎を武蔵の弟子達が皆で打ち殺した」, com os discípulos 「島に来ていて隠れていた」. **Onde** ele morreu não muda. A frase não diz quem matou, então vale nas duas versões. Sem ação.

**1.7 Reigandō, "nos arredores de Kumamoto" (l. 52): OK.**
- MLIT: no recinto do Unganzen-ji, em Nishi-ku, Kumamoto ([MLIT R2-02046, FY2020](https://www.mlit.go.jp/tagengo-db/en/R2-02046.html)).
- Tofugu: "just outside of Kumamoto".
- Apresentação do Kodansha 学術文庫 (vista só no resumo da busca; a página deu 403): 「熊本市西郊の雲巌寺にある洞窟にこもり」.

**1.8 "só se recolheu lá em 1643, aos 60 anos (na contagem japonesa, a que ele mesmo usa no livro)" (l. 52, com o ★): OK.**
- Prefácio: 「時に寛永二十年十月上旬の頃九州肥後の地巌殿山に上り…年つもりて六十」 ([koten.net 001](https://www.koten.net/gorin/gen/001/)).
- Tofugu: "a cave in Kyushu in 1643".
- Nuance que não pede ação: a ja.wikipedia registra a hipótese de que ele escreveu na residência de Kumamoto (D19). O texto segue a tradição, o que é aceitável.

**1.9 "dois anos antes de morrer" (l. 52): OK.** Ver Contas. A morte em 正保2年5月19日 = 13/06/1645 está na ja.wikipedia.

**1.10 "Foi ali que começou a escrever" (l. 52): OK.** Prefácio: 「十月十日の夜寅の一点に筆を把りて書き初るものなり」. Na ja.wikipedia: 「寛永20年（1643年）10月、『五輪書』の執筆を始める」.

**1.11 "três décadas" (l. 54): OK** (31 anos). "O duelo mais famoso da vida dele" bate com Hurst ("The most famous encounter").

**1.12 Prefácio, "mais de sessenta duelos sem perder, o primeiro aos 13" (l. 60): OK.** No koten.net 001: 「十三歳にして初て勝負を為す」 e 「六十余度まで勝負すといへども一度もその利を失はず」. A janela das vitórias é 「年十三より二十八九まで」.

**1.13 "Por volta dos 30, olhou para trás" (l. 60): CORRIGIR (leve, fidelidade).** O original diz 「三十を越えて跡をおもひ見るに」, ou seja, passados os 30. A diferença pesa porque as vitórias vão até os 28 ou 29: a reflexão vem depois de os duelos acabarem.
- Correção: "Por volta dos 30, olhou para trás" → "Passados os 30, olhou para trás".

**1.14 "talento natural, a ordem do céu ou escolas adversárias fracas" (l. 60, com a `norma` da vírgula): OK.** O original diz 「おのづから道の器用ありて天理を離れざるが故か　又は他流の兵法不足なる所にや」:
- 器用 = aptidão natural;
- 天理を離れざる = "não se afastar do princípio celeste", e "a ordem do céu" é tradução aceitável;
- 他流の兵法不足 = a estratégia das outras escolas era deficiente.

O "sorte" do rascunho (D5) já saiu. É paráfrase sem aspas e não depende da redação de Kikuchi.

**1.15 "Só perto dos 50 sentiu que tinha entendido o Caminho" (l. 60): OK.** Original: 「朝鍛夕錬して見ればおのづから兵法の道にあふこと我五十歳のころなり」. O "Só" é ênfase do autor.

## 2. Aparte "Passada a eleição" (l. 56): OK

- A CF, art. 77, na redação da [EC 16/1997](https://www.planalto.gov.br/ccivil_03/constituicao/Emendas/Emc/emc16.htm), fixa o 1º turno no primeiro domingo de outubro e o 2º no último.
- Em 2026, os domingos de outubro são 4, 11, 18 e 25 (python3). O 2º turno foi em **25/10/2026**.
- A cobertura confirma a votação nesse domingo, com o presidente do TSE prevendo o resultado para as 20h30–21h ([ABCdoABC](https://abcdoabc.com.br/eleicoes-2026-tse-preve-resultado-20h30-21h/)).
- A publicação em 27 ou 28/10 vem depois. O resultado oficial não foi conferido no portal do TSE, mas o texto não depende dele.

## 3. "Wall Street já tentou te vender este livro" (l. 72–86)

**3.1 Harris, 1974 (l. 74): OK.** Hurst: "Translated by Victor Harris and published by Overlook Press in 1974 as *A Book of Five Rings*".

**3.2 "A primeira tradução para o inglês" (l. 74): [VERIFICAR], prioridade baixa.** As duas listas cronológicas consultadas começam em Harris 1974, e nenhuma mostra tradução anterior ([Sosnowski 2007](https://ejmas.com/jalt/2007jalt/jcsart_sosnowski_0711.html); en.wikipedia). Mas nenhuma fonte primária a chama de "primeira".
- Correção sem perda: "A primeira tradução para o inglês, de Victor Harris," → "A tradução inglesa de Victor Harris". Se ficar, `[VERIFICAR: Harris 1974 como primeira tradução inglesa]`.

**3.3 "passou quase despercebida fora do circuito das artes marciais" (l. 74): OK.** Hurst: "attracted little attention outside the martial arts community".

**3.4 "No começo dos anos 80, virou leitura de executivo" (l. 74): OK.** Hurst cita o "long article (October 19, 1981)" da *Time* e a "apparent bewilderment of some US businessmen trying to come to grips with Japanese economic competition". A Bantam é de 1982 (03-pesquisa, archive.org).

**3.5 Ex-jogador de beisebol "que vivia no Japão", publicitário nova-iorquino, "meio de brincadeira", "chave para entender o sucesso japonês" (l. 80): OK.** Hurst:
- "A retired Japanese professional baseball player -- actually a Korean resident of Japan -- mentioned Gorin no sho to a New York ad man";
- "who suggested, half in jest, to some businessmen that reading Musashi's little book was the key to understanding Japanese success".

"que vivia no Japão" acomoda bem o "Korean resident of Japan".

**3.6 Faixa "Japan's Answer to the Harvard MBA" (l. 80): OK, literal.** Hurst: "they have added a new banner to the dust jacket", com o texto "Japan's Answer to the Harvard MBA: The Classic Guide to Strategy Corporate America is taking into the Boardrooms". "A editora" é a Overlook.

**3.7 A concorrente, edição de bolso, subtítulo *The Real Art of Japanese Management* (l. 80): OK.**
- Hurst: "paperback giant Bantam cashed in with a version of its own", com o subtítulo "The Real Art of Japanese Management".
- Registro de catálogo: Bantam, 1982, Nihon Services Corporation, "The real art of Japanese management" ([Deakin](https://library.deakin.edu.au/record=b1731578~S1)).
- Nuance sem ação: era uma tradução própria, não uma reedição da de Harris.

**3.8 Capa: "um executivo de sobretudo erguendo o *Wall Street Journal* como se fosse uma *katana*" (l. 80): OK, é descrição defensável.**
- Hurst: "Juxtaposed opposite a dramatic samurai figure from a woodblock print is an American executive in similar pose", e o executivo traz "a Wall Street Journal raised high in the other [hand]".
- *Dawn* (Kabir Babar, 03/11/2019): "a suited businessman in a trench coat with umbrella and briefcase confronting a samurai warrior"; o samurai carrega uma espada e o executivo ergue um jornal ([Dawn](https://www.dawn.com/news/amp/1514567)).

Se o executivo repete a pose de um samurai armado com o jornal erguido no lugar da espada, "como se fosse uma *katana*" descreve a composição com fidelidade. A comparação é do autor e está fora de aspas. "Sobretudo" se sustenta: *trench coat* na *Dawn*, "raincoat" em Hurst. A capa não foi vista em imagem.

**3.9 "não punham seus *trainees* em massa para estudar Musashi" (l. 82): OK.** Hurst: "But Japanese companies in great numbers do not put all their trainees to work mastering this text."

**3.10 "o livro mal se achava nas livrarias do país" (l. 82): OK.** Hurst: "Five Rings can be rather hard to come by in Japanese bookstores." "Mal se achava" é um grau mais forte que "rather hard to come by", o que é aceitável.

**3.11 "O modelo corporativo japonês era feito de lealdade, consenso e emprego vitalício" (l. 82): OK como síntese, com alinhamento opcional.**
- Hurst lista "loyalty, harmony, group cohesiveness, dependence, mutual support, and the like" e, em outro ponto, "lifetime employment, a seniority system, and early retirement".
- **"Consenso" não é de Hurst** ("the text does not use the word 'consensus'" nesse sentido).
- A frase vem logo depois de "O próprio Hurst derruba essa ideia", e o leitor a lê como de Hurst.
- Ajuste opcional, de uma palavra: "lealdade, consenso e emprego vitalício" → "lealdade, harmonia de grupo e emprego vitalício".

**3.12 Ressalva do *rōnin*, com o ★: "samurai sem senhor (até os últimos anos, quando aceitou o estipêndio dos Hosokawa e escreveu o livro), leal só a si mesmo" (l. 82): OK.**
- Hurst: "For all but the last years of his life, Musashi was a ronin, a masterless samurai whose only loyalty was to himself."
- Estipêndio: em 1640, Hosokawa Tadatoshi lhe dá 「7人扶持合力米18石の待遇」 e, em dezembro, 「米300石」. Ele 「家臣ではなく客分として遇された」 (ja.wikipedia).
- "Aceitou o estipêndio" é a formulação exata, porque ele foi hóspede (客分) e não vassalo. A escrita (1643–45) cai nesse período.
- O aposto opcional "senhores de Kumamoto" não entra, por ser incompatível com o ★, e por isso não foi conferido.

**3.13 "quase todo conselho de Musashi soa familiar. Benjamin Franklin, manual de escoteiro" (l. 86): CORRIGIR (escopo da atribuição, D11).**
- Hurst escreve: "While all the rest of the advice is sound enough, it is all too familiar from British and homegrown sources: Samuel Smiles, Benjamin Franklin, McGuffy's Reader, and the Boy Scout Manual."
- "The advice" são as **nove máximas** que a Bantam pôs na abertura ("The Winning Strategy"), menos a das duas espadas ("Only the enjoinder to practice the two-sword school seems a bit foreign to us").
- O texto estende a crítica a "todo conselho de Musashi". O "quase" acerta a exceção, mas o escopo sai errado.
- Citar dois dos quatro nomes é abreviação fiel.
- Correção mínima: "quase todo conselho de Musashi soa familiar" → "quase todas as nove regras de Musashi soam familiares". A l. 96 ("as nove regras que fecham o rolo") vira retomada.

## 4. "Um manual de esgrima…" (l. 88–92)

**4.1 Cinco rolos: Terra (*Chi*), Água (*Sui*), Fogo (*Ka*), Vento (*Fū*) e Vazio (*Kū*) (l. 90): OK.**
- Os rolos são 地の巻, 水の巻, 火の巻, 風の巻 e 空の巻 (ja.wikipedia 五輪書; en.wikipedia).
- As leituras *chi, sui, ka, fū, kū* são as dos cinco elementos (五大): 「地（ち）・水（すい）・火（か）・風（ふう）・空（くう）」 ([ja.wikipedia 五大](https://ja.wikipedia.org/wiki/五大)). Isso é coerente com "um para cada elemento".
- Para ciência, sem ação: os títulos dos rolos também são lidos *mizu/hi/kaze no maki*.

**4.2 "Foi escrito para ser entregue a um discípulo, não para ser vendido" (l. 90): OK.**
- Colofão do Vazio: 「正保二年五月十二日　新免武蔵」「寺尾孫之丞」 ([koten.net 501](https://www.koten.net/gorin/gen/501/)).
- Hurst: "handed down among the members of his school as a secret text. The audience for which it was intended was thus quite limited."

**4.3 `Norma` da etapa 6, "O *Gorin no Sho* (o nome original do livro)" (l. 90): CORRIGIR (factual).** O título 五輪書 não é de Musashi.
- ja.wikipedia 五輪書, seção 構成: 「武蔵自身も彼から譲り受けた弟子も、「五巻」「地水火風空之五巻」と呼んでいた」 e 「豊田正剛になって、五輪書という名が初めて見られるようになった」.
- O aposto continua necessário pela regra 1, mas não pode dizer "original".
- Correção, que substitui a da etapa 6: "O *Gorin no Sho* (o título japonês do livro) tem cinco rolos". Variante: "(o nome japonês pelo qual o livro ficou conhecido)".

## 5. Anel da Terra (l. 94–114)

**5.1 Mestre carpinteiro: madeira, medidas, ferramentas (l. 96): OK** (03-pesquisa).
- koten.net 103: 「大将は大工の統領として天下のかねを弁へ…」 e 「家を立るに木配りをする事」.
- koten.net 104: 「能きるる道具を持透々にとぐことが肝要也」.

**5.2 "nove regras que fecham o rolo" (l. 96): OK.** A seção 109 é a última do 地の巻: a navegação vai de 地の巻 九 a 水の巻 一 ([koten.net 109](https://www.koten.net/gorin/gen/109/)).

**5.3 As quatro regras (l. 98–104), conferidas no original:**

| No texto | Original (koten.net 109) | Fidelidade |
|---|---|---|
| "o Caminho está no treino" | 第二に道の鍛錬する所 | OK. Livre: literalmente, "forjar-se no Caminho". |
| "distinga ganho de perda em todas as coisas" | 第五に物毎の損徳を弁ふる事 | OK. 物毎 = em todas as coisas; 弁ふ = discernir; 損徳 = perda e ganho. |
| "preste atenção até no que parece trivial" | 第八にわづかなる事にも気を付る事 | OK. "Parece" é acréscimo leve. |
| "não faça nada que seja inútil" | 第九に役に立ぬ事をせざる事 | OK |

**Redação: [VERIFICAR] ou marca de tradução livre.** A lista vem como as regras de Musashi, uma citação de fato, sem marca de tradução, e a redação de Kikuchi não pôde ser conferida. Correção mínima, à escolha:
- (a) "Entre elas:" → "Entre elas, em tradução livre:";
- (b) manter e marcar `[VERIFICAR: redação das regras 2, 5, 8 e 9 na edição Kikuchi]`.

A regra da etapa 6 (l. 100) dizia que a redação de Kikuchi prevaleceria. Como ela não está acessível, vale (a), ou o autor confere com o livro em mãos.

**5.4 *Dokkōdō*, "Uma semana antes de morrer… 21 preceitos curtos" (l. 112): OK.**
- 21 artigos: 「21箇条」 ([ja.wikipedia 独行道](https://ja.wikipedia.org/wiki/独行道)) e "It consists of 21 precepts" ([en.wikipedia](https://en.wikipedia.org/wiki/Dokk%C5%8Dd%C5%8D)).
- Data: o colofão diz 5/12 e a morte é em 5/19, ou seja, 7 dias. A ja.wikipedia diz 「死の一週間前に書かれたとされている」 ("diz-se que"). A data do colofão é questionada (03-pesquisa §4.3), e o grau de certeza do texto é aceitável.

**5.5 "enquanto distribuía o que tinha aos discípulos" (l. 112): [VERIFICAR].**
- A única fonte é a en.wikipedia ("largely composed on the occasion of Musashi giving away his possessions in preparation for death"), **sem nota de rodapé**.
- A ja.wikipedia (独行道 e 宮本武蔵) não menciona distribuição de bens nem 形見分け, e a busca em japonês não achou fonte.
- Tem fonte o 武公伝: 「正保二年五月十二日、五輪書ヲ寺尾孫之丞勝信ニ相伝ナリ、同日ニ自誓ノ書ヲ筆ス」 (ja.wikipedia 独行道).
- Correção mínima sustentada por fonte, que mantém a imagem da entrega: "enquanto distribuía o que tinha aos discípulos," → "no mesmo dia em que entregou o livro ao discípulo,". Alternativa: cortar a oração.
- Se ficar: `[VERIFICAR: fonte primária para a distribuição de bens aos discípulos]`.

**5.6 Os três preceitos (l. 112)** (texto da ja.wikisource, 03-pesquisa):

| No texto | Nº | Original | Veredito |
|---|---|---|---|
| "não guarde objetos antigos à espera de que um dia valham alguma coisa" | 14 | 末々代物なる古き道具を所持せす | OK, próximo do literal |
| "não busque bens para garantir a velhice" | 18 | 老身に財寳所領もちゆる心なし | OK. "Garantir" é leitura, compatível com o original ("não ter o intento de reter tesouros e terras na velhice"). |
| "seja indiferente ao lugar onde mora" | 12 | 私宅におゐてのそむ心なし | OK, mas segue a lista inglesa corrente ("Be indifferent to where you live"). O literal é "não ter desejo quanto à própria casa". Opcional, e mais afinado com o minimalismo: "não tenha ambição quanto à própria casa". |

Não se sabe se a edição Kikuchi traz o *Dokkōdō* (03-pesquisa §3.2), então estas versões são necessariamente do autor. Sugestão de baixo custo: marcar "(em tradução livre)" depois dos dois-pontos. Outra saída é uma nota única nas Referências; ver §12.

**5.7 "quase quatro séculos antes da moda" (l. 112): OK.** Ver Contas.

**5.8 "a escritura de uma debênture" (l. 108, `norma`): OK.** É vocabulário corrente ("escritura de emissão") e não traz afirmação factual.

**5.9 "débito técnico: um atalho que cobra juros depois" (l. 110, `norma`): OK, a definição é compatível com a origem do termo.** Cunningham (OOPSLA 1992): "Shipping first time code is like going into debt. A little debt speeds development so long as it is paid back promptly with a rewrite." e "Every minute spent on not-quite-right code counts as interest on that debt." ([c2.com](https://c2.com/doc/oopsla92.html)). A aplicação a quem usa, e não ao artefato, é metáfora do autor. É o nitpick da 5a e fica no gate.

## 6. Anel da Água (l. 116–140)

**6.1 "A água assume a forma do recipiente e continua clara" (l. 118): OK.** Rolo da Terra, na descrição do Rolo da Água: 「水を本として心も水になる也」, 「方円のうつわものに随ひ」 e 「清き所を用ゐて一流の事を此巻に書顕す也」 ([koten.net 105](https://www.koten.net/gorin/gen/105/)).

**6.2 A frase do fecho, "hoje, vença o você de ontem; amanhã, … os menos hábeis; depois, os mais hábeis" (l. 128): OK, marcada como "tradução livre".** Original: 「今日は昨日の我に勝ちあすは下手に勝ち後は上手に勝」 ([koten.net 238](https://www.koten.net/gorin/gen/238/), 後書 do 水の巻). Por estar marcada como tradução livre, não depende de Kikuchi.

**6.3 "mil dias de treino para forjar, dez mil para polir" (l. 128): OK.** Original: 「千日の稽古を鍛とし万日の稽古を錬とす」. 鍛 é forjar; 錬 é refinar ou temperar, e "polir" é aceitável.

**6.4 "No mesmo parágrafo, pede… sem pressa… estrada de mil léguas… um passo de cada vez" (l. 128): OK.** Está na mesma seção (238): 「千里の道も一足づつ運ぶなり」, 「いそぐ心なくして」 e 「緩々と思ひ」. Reconferido. Na ordem do original, o "sem pressa" vem **antes** do "vença o eu de ontem". O texto não afirma ordem, então nada muda.

**6.5 Clear (l. 130): OK.**
- Fonte primária: "If you get one percent better each day for one year, you'll end up thirty-seven times better by the time you're done." ([jamesclear.com](https://jamesclear.com/continuous-improvement)).
- O "1% melhor por dia" entre aspas é rótulo do slogan, não citação da edição da Alta Books.
- O ★ ("uma ideia parecida com a de vencer o eu de ontem") enquadra como semelhança, o que é correto.

**6.6 1,01³⁶⁵ ≈ 37,8 (l. 132): OK** (37,7834).

**6.7 "Ela supõe uma taxa constante e positiva, todo santo dia." (l. 136): OK.** Descreve bem a conta de Clear.

**6.8 "Carreira não é título pós-fixado" (l. 136): DEF. IMPRECISA, só registro.** No sentido técnico, a taxa constante e contratada é a do prefixado levado na curva, e o pós-fixado rende a taxa do dia, que muda com o Copom (5a, atenção). No sentido coloquial ("rende todo dia"), a imagem funciona. **Não é erro factual grosseiro**, e o autor já decidiu. Sem ação.

**6.9 Gloss "marcação a mercado contra você — o preço do título, atualizado todo dia pelo valor de mercado, em queda" (l. 136, `norma`): OK, a definição é compatível.** Marcação a mercado é atualizar o preço do título pelo valor que ele teria se fosse vendido no mercado naquele dia.
- "Todo dia" vale para o Tesouro Direto (preço diário) e para o cálculo de cota de fundos, que são o contato mais comum do leitor.
- A regra ANBIMA de 2023, que estendeu a marcação a posições de clientes na distribuição, é de outro escopo ([ANBIMA, 14/12/2022](https://www.anbima.com.br/es_es/imprensa/marcacao-a-mercado-e-tema-de-novo-curso-gratuito-da-anbima.htm)). O texto normativo da ANBIMA não foi reaberto.
- "Em queda" = "contra você", correto.
- O gloss fala de preço, não de perda realizada, e bate com o graf-01 ("semestre contra que se reverte").

**6.10 "Dez mil dias são uns 27 anos" (l. 138): OK** (27,38).
- Registro sem ação, porque a decisão já é do autor (crítica 9b): "ele não promete retorno em nenhum deles" vale como "não promete taxa".
- O mesmo 後書 traz um resultado condicional: 「一身を以て数十人にも勝」, depois de entendido o princípio.

**6.11 "quase quatro décadas" (l. 140): OK** (37 anos). É calibrado como ordem de grandeza, em linha com a resposta à 5a.

## 7. Anel do Fogo (l. 142–162): OK (03-pesquisa §6; koten.net 310, 322 e 324 não reabertos)

- "a luta em si, o calor do combate": no 105, 「此巻に戦の事を書記也」 e 「火は大小となりけやけき心有によつて合戦の事を書也」 (reconferido).
- "Tomar a iniciativa" e "não deixar recuperar o ritmo" correspondem a 三ツの先, 枕をおさふる e くづれを知る. "Esmagá-lo quando ele vacila" corresponde a ひしぐ e くづれを知る (03-pesquisa).
- Impasse e recomeço "como se fosse outra luta": 四手をはなす (310), 「其儘心をすてて別の利にて勝事を知る也」, e あらたになる (324), 「物毎をあたらしくはじむる心に思ひて」. É uma condensação fiel.
- "(O próprio *Dokkōdō* manda nunca invejar ninguém.)": preceito 7, 「善惡に他をねたむ心なし」. OK.

## 8. Anel do Vento (l. 164–176)

**8.1 Espada longa e curta, força bruta, posturas (l. 166): OK.** No 401: 「大きなる太刀をとつて強き事を専らにして」, 「短き太刀を以て道を勤る」, 「太刀かず多く」 e 「太刀の構を以て」 (03-pesquisa). "Coleciona posturas" funde 太刀かず多く (muitas técnicas) e 構 (posturas), o que é aceitável.

**8.2 "uma 'porta' para iniciantes e um 'interior' para os escolhidos" (l. 166): OK no conteúdo, DEF. IMPRECISA leve no termo.**
- O par do título é 奥/表 ("interior/superfície"; Harris: "'Interior' and 'Surface'"). A entrada (口) aparece na imagem da montanha: 「猶奥へ行んと思へば又口に出るもの也」 (410).
- Entre aspas, "porta" se apresenta como termo de Musashi.
- Opcional: "porta" → "entrada" (é o 口 do próprio Musashi) ou → "superfície" (literal de 表).
- "desconfia de quem divide o ensino em níveis secretos": OK (410, 「誓紙罰文など云事を好まず」).

**8.3 *Fū* = vento e também estilo, maneira, tradição, "o jeito da casa" (l. 168): OK.**
- O próprio Musashi, no 105: 「風と云に於ては昔の風今の風其家々の風などとあれば…是風也」 (reconferido).
- en.wikipedia: "something of a pun, since the Japanese character for 'wind' can also mean 'style'".

**8.4 "a justificativa de Musashi é simples: é difícil conhecer a si mesmo sem conhecer os outros" (l. 168): OK (D7 resolvido pela redação atual).**
- A frase literal está no Rolo da Terra, **justamente no trecho que apresenta o Rolo do Vento**: 「他の事を能知らずしては自のわきまへ成がたし」 (koten.net 105, reconferido).
- Ela é, portanto, a justificativa do próprio Musashi para o rolo. O texto não diz que ela está dentro do Vento.
- A abertura do Vento repete a ideia no nível da escola: 「他流の道を知らずしては我一流の道慥に弁へがたく」 (401).

**8.5 Greene, *Maestria*, "aprendizado" (l. 172, com o ★ que tira o rótulo em negrito): OK, com fonte secundária.**
- *Mastery* (2012), cap. II, "The Ideal Apprenticeship" (03-pesquisa §7.4).
- Edição brasileira: Sextante, **2013**, ISBN 978-85-7542-981-5, tradução de Afonso Celso da Cunha Serra ([Estante Virtual](https://www.estantevirtual.com.br/livro/maestria-09J-0785-000-BK)). O resumo da [getAbstract](https://www.getabstract.com/pt/resumo/maestria/24767), que dá a edição como Sextante 2013, usa "a fase do aprendizado ideal".
- O sumário da edição não foi visto: a página da Sextante deu 404. Se 'aprendizado' entrar entre aspas simples como termo de Greene (sugestão `linha` da etapa 6), o autor confere no livro. Não vira [VERIFICAR] no texto.
- "absorve um ofício com humildade" bate com "Submit to Reality".

## 9. Anel do Vazio (l. 178–192)

**9.1 "O último rolo é o mais curto, poucas páginas" (l. 180): OK.** É uma seção só (koten.net 501).

**9.2 "de influência zen" (l. 180): DEF. IMPRECISA (leve).**
- A en.wikipedia diz "(probably) Zen-influenced". A ja.wikipedia 五輪書 não afirma a influência.
- **O próprio Musashi, no prefácio, diz que não tomou emprestado nada do budismo nem do confucionismo**: 「仏法儒道の古語をもからず軍記軍法の古きことをも用ゐず」 (koten.net 001, reconferido).
- A frase do texto põe como fato uma leitura que o autor do livro desmente.
- Correção mínima: "poucas páginas de influência zen" → "poucas páginas que muita gente lê como zen".

**9.3 Vazio × confusão (l. 184): OK.** No 501: 「物を弁へざる所を空と見る所実の空には非ず皆迷ふ心也」. A "névoa que se dissipa" é 「迷ひの雲の晴たる所」 (reconferido).

**9.4 "acumule prática dia após dia, hora após hora; afie a mente e o olhar" (l. 184): OK.** No 501: 「朝々時々におこたらず」 e 「心意二ツの心をみがき観見二ツの眼をとぎ」. É paráfrase sem aspas. O "com o espírito assentado" não foi conferido palavra a palavra, porque o koten.net não deixou transcrever a seção inteira, mas é compatível com o resumo da seção.

## 10. Fechamento "Não fica fácil" (l. 194–204)

**10.1 "começou o livro aos 60 anos, numa caverna, e o terminou doente, para um único discípulo" (l. 196): OK.**
- 60: prefácio. Caverna: tradição, com a ressalva do item 1.8.
- Doente: 「（1644年11月）武蔵は病気となり」 (ja.wikipedia).
- Entrega a Terao Magonojō em 正保2年5月12日: colofão (koten.net 501) e 武公伝.
- Nenhuma fonte consultada diz que o livro ficou inacabado.

**10.2 "Venceu o duelo mais famoso da história do Japão aos 29" (l. 196): [VERIFICAR] no superlativo.**
- O "aos 29" está OK (Hurst).
- O superlativo nacional não tem fonte:
  - Hurst fala do encontro mais famoso **de Musashi** ("The most famous encounter");
  - o MLIT, de "one of his most famous duels";
  - a Yamaguchi Tourism, de 「あまりに有名な話」;
  - a busca por 「日本一有名な決闘」 ou 「日本で最も有名な決闘」 não achou fonte.
- Correção mínima, coerente com a l. 54: "o duelo mais famoso da história do Japão" → "o duelo mais famoso da vida dele". Alternativa: "um dos duelos mais famosos do Japão".
- Se ficar: `[VERIFICAR: fonte para "o duelo mais famoso da história do Japão"]`.

**10.3 "passou as três décadas seguintes treinando, pintando, escrevendo e estudando as escolas dos outros" (l. 196): CORRIGIR (leve, omissão; D20; o autor decide).**
- Os 31 anos estão OK.
- O que a lista tem de fonte:
  - "treinando": 「朝鍛夕錬」 no prefácio;
  - "pintando": obras em tinta, como o 『枯木鳴鵙図』, que é 重要文化財 (ja.wikipedia);
  - "escrevendo".
- "Estudando as escolas dos outros" é inferência do Rolo do Vento, aceitável.
- O período inclui duas campanhas militares documentadas:
  - **Osaka (1615)**: 「徳川方の水野勝成軍に参陣し」, como 騎馬武者;
  - **Shimabara (1637–38)**: 「一揆軍の投石によって負傷したことを伝えている」, na carta a Arima Naozumi (ja.wikipedia).
- A lista do texto pinta um período contemplativo que a biografia não tem.
- Correção mínima: "treinando, pintando, escrevendo e estudando as escolas dos outros" → "treinando, indo à guerra duas vezes, pintando, escrevendo e estudando as escolas dos outros".

**10.4 "Na última semana de vida, ainda estava escrevendo regras para si mesmo" (l. 198): OK.** O 武公伝 chama o texto de 「自誓ノ書」, datado de 5/12, e a morte é em 5/19. Ver também o item 5.4.

**10.5 "o ponto exato em que Musashi parou de contar vitórias e começou a perguntar por que tinha vencido" (l. 200): OK.** Bate com o prefácio (「三十を越えて跡をおもひ見るに」) e com a correção do item 1.13.

## 11. Tabela-síntese, coluna "O que Musashi escreveu" (l. 208–214): OK

| Anel | Célula (pós-etapa 9) | Fonte |
|---|---|---|
| Terra | Conhecer as medidas e as ferramentas; distinguir ganho de perda; não fazer nada inútil | 103–104; regra 5 (物毎の損徳を弁ふる); regra 9 |
| Água | Adaptar-se como a água; vencer o eu de ontem; mil dias para forjar, dez mil para polir | 105 (方円のうつわものに随ひ); 238 |
| Fogo | Tomar a iniciativa; quando a luta trava, abandonar a abordagem e recomeçar | 三ツの先; 310; 324 |
| Vento | Criticar as escolas rivais; conhecer os outros para conhecer a si mesmo | 401–410; 105 (a justificativa do próprio rolo) |
| Vazio | Dissipar a confusão acumulando prática, dia após dia | 501 |

Se o item 1.13 ou o 9.2 mudar o corpo, a tabela não é afetada.

## 12. Referências (l. 216–223)

| Referência | Veredito |
|---|---|
| Musashi, *O Livro dos Cinco Anéis* (*Gorin no Sho*, 1645), trad. Wataru Kikuchi (Jardim dos Livros, 2020) | **OK (metadados).** Jardim dos Livros, 1ª ed., 2020, ISBN 9788584840335, 128 p.; "tradução, direta do japonês, do professor doutor Wataru Kikuchi" ([Martins Fontes](https://www.martinsfontespaulista.com.br/o-livro-dos-cinco-aneis-905742/p)). O ano "1645" serve como data de entrega; a escrita vai de 1643 a 1645, e "1643–1645" seria mais exato (opcional). **O texto de Kikuchi não foi acessado** (§5.3). |
| Musashi, *Dokkōdō* (1645) | **OK.** Data do colofão, 正保2年5月12日 (ja.wikisource, 03-pesquisa). Não há edição em português confirmada. As versões no post são do autor (§5.6). |
| Hurst, "Samurai on Wall Street: Miyamoto Musashi and the Search for Success" (*UFSI Reports*, nº 44, 1982; *InYo*, 2001) + link | **OK.** O título confere com o da página. "First published 1982, UFSI Reports #44"; *InYo: Journal of Alternative Perspectives*, janeiro de 2001. O link estava ativo em 2026-10-28. |
| Tofugu, "Miyamoto Musashi's Reigando Cave" + link | **OK. Completar:** autor **Adam Ledford**, **9 jul. 2015**. Sugestão: "Tofugu (Adam Ledford, 9 jul. 2015), [...]". O título confere. Sem ação no corpo: o Tofugu erra o nome do templo ("Reiganzen-ji" em vez de Unganzen-ji), e o post não usa esse nome. |
| James Clear, *Hábitos Atômicos* (Alta Books, 2019) | **OK.** Alta Books/Alta Life, 2019, ISBN 978-85-508-0756-0 (03-pesquisa; registro de catálogo em [BookWyrm](https://bookwyrm.de/book/29251/s/habitos-atomicos)). O tradutor não foi confirmado, e a referência não o exige. |
| Robert Greene, *Maestria* (Sextante) | **Completar o ano: 2013** (Estante Virtual; getAbstract, que dá a edição como Sextante 2013). As duas fontes são secundárias e concordam. A página da editora deu 404. |

Nota opcional nas Referências, que resolve de uma vez os §5.3 e §5.6: "As passagens de Musashi citadas no texto são traduções livres a partir do original japonês." Com ela, a marca "em tradução livre" nas regras e no *Dokkōdō* fica dispensável, e o [VERIFICAR] da redação Kikuchi cai.

---

## Correções para a etapa 9 aplicar (redação exata)

| # | Linha | De | Para | Classe |
|---|---|---|---|---|
| 1 | 90 | `O *Gorin no Sho* (o nome original do livro) tem cinco rolos` (`norma` da etapa 6) | `O *Gorin no Sho* (o título japonês do livro) tem cinco rolos` | CORRIGIR (factual) |
| 2 | 86 | `quase todo conselho de Musashi soa familiar.` | `quase todas as nove regras de Musashi soam familiares.` | CORRIGIR |
| 3 | 60 | `Por volta dos 30, olhou para trás` | `Passados os 30, olhou para trás` | CORRIGIR (leve) |
| 4 | 196 | `treinando, pintando, escrevendo e estudando as escolas dos outros` | `treinando, indo à guerra duas vezes, pintando, escrevendo e estudando as escolas dos outros` | CORRIGIR (leve; o autor decide) |
| 5 | 180 | `poucas páginas de influência zen` | `poucas páginas que muita gente lê como zen` | DEF. IMPRECISA |
| 6 | 46 | `e um dos nomes mais temidos do Japão` | cortar, ou `e, para alguns, espadachim melhor que o próprio Musashi` | resolve o [VERIFICAR] |
| 7 | 112 | `enquanto distribuía o que tinha aos discípulos,` | `no mesmo dia em que entregou o livro ao discípulo,` (ou cortar) | resolve o [VERIFICAR] |
| 8 | 196 | `o duelo mais famoso da história do Japão` | `o duelo mais famoso da vida dele` | resolve o [VERIFICAR] |
| 9 | 96 | `Entre elas:` | `Entre elas, em tradução livre:` (ou a nota única nas Referências) | resolve o [VERIFICAR] |
| 10 | 74 | `A primeira tradução para o inglês, de Victor Harris,` | `A tradução inglesa de Victor Harris` | resolve o [VERIFICAR] (baixo) |
| 11 | 222 | `Tofugu, ["Miyamoto Musashi's Reigando Cave"](…).` | `Tofugu (Adam Ledford, 9 jul. 2015), ["Miyamoto Musashi's Reigando Cave"](…).` | preenchimento |
| 12 | 223 | `Robert Greene, *Maestria* (Sextante).` | `Robert Greene, *Maestria* (Sextante, 2013).` | preenchimento |

**Opcionais (o texto está OK):**
- l. 82: "lealdade, consenso e emprego vitalício" → "lealdade, harmonia de grupo e emprego vitalício" (vocabulário de Hurst).
- l. 166: "porta" → "entrada".
- l. 112: "seja indiferente ao lugar onde mora" → "não tenha ambição quanto à própria casa" (literal do preceito 12).
- l. 112: "(em tradução livre)" nos preceitos do *Dokkōdō*, se não houver a nota única.

## `[VERIFICAR: ...]` remanescentes (só se a correção correspondente não for aplicada)

- `[VERIFICAR: fonte para "um dos nomes mais temidos do Japão"]` (l. 46)
- `[VERIFICAR: fonte primária para a distribuição de bens aos discípulos; só há a en.wikipedia, sem nota]` (l. 112)
- `[VERIFICAR: fonte para "o duelo mais famoso da história do Japão"]` (l. 196)
- `[VERIFICAR: redação das regras 2, 5, 8 e 9 na edição Kikuchi]` (l. 98–104)
- `[VERIFICAR: Harris 1974 como primeira tradução inglesa]` (l. 74)

Se as correções 6 a 10 entrarem, **não sobra nenhum [VERIFICAR]** no post.

## `[FAIXA: ...]`

Nenhum.

## Fora do escopo desta etapa

- As referências que a 5a citou de memória (Gervais & Odean, Mincer, Chetty & Szeidl, SR 11-7, LFT em março de 2020 etc.) **não estão no corpo do post**, e por isso não foram conferidas. Só precisam de verificação se alguma entrar no texto no gate.
- O "a indústria japonesa estava engolindo a americana" (l. 76) é enquadramento de época, compatível com Hurst ("bewilderment… Japanese economic competition"). A medida setorial continua como nitpick da 5a no gate.
- Etapa 8: o diag-01 usa 1596 (13), 1612 (29), ~1633 (~50) e 1643 (60). O graf-01 chega a 37,78×.

## Fontes (acesso em 2026-10-28, salvo "(03-pesquisa)", de 2026-10-26)

- *Gorin no Sho*, original japonês (koten.net): [001](https://www.koten.net/gorin/gen/001/), [105](https://www.koten.net/gorin/gen/105/), [109](https://www.koten.net/gorin/gen/109/), [238](https://www.koten.net/gorin/gen/238/), [501](https://www.koten.net/gorin/gen/501/). Também usadas, pela 03-pesquisa: 103, 104, 310, 322, 324, 401 e 410.
- [Hurst, "Samurai on Wall Street" (EJMAS/*InYo*, jan. 2001)](https://ejmas.com/jalt/jaltart_Hurst_0101.htm)
- ja.wikipedia: [宮本武蔵](https://ja.wikipedia.org/wiki/宮本武蔵) · [五輪書](https://ja.wikipedia.org/wiki/五輪書) · [独行道](https://ja.wikipedia.org/wiki/独行道) · [五大](https://ja.wikipedia.org/wiki/五大)
- en.wikipedia: [Dokkōdō](https://en.wikipedia.org/wiki/Dokk%C5%8Dd%C5%8D) · [The Book of Five Rings](https://en.wikipedia.org/wiki/The_Book_of_Five_Rings)
- ja.wikisource, [獨行道](https://ja.wikisource.org/wiki/獨行道) (03-pesquisa)
- MLIT/JTA: [Reigandō (FY2020)](https://www.mlit.go.jp/tagengo-db/en/R2-02046.html) · [Ganryūjima (FY2023)](https://www.mlit.go.jp/tagengo-db/R5-00678.html)
- [Yamaguchi Tourism, Ganryūjima](https://yamaguchi-tourism.jp/feature/ganryujima)
- [Tofugu (Adam Ledford, 09/07/2015)](https://www.tofugu.com/travel/reigando-cave/)
- [Sosnowski, *InYo*, nov. 2007](https://ejmas.com/jalt/2007jalt/jcsart_sosnowski_0711.html)
- [Dawn, Kabir Babar, 03/11/2019](https://www.dawn.com/news/amp/1514567)
- [Registro da Bantam 1982 (Deakin)](https://library.deakin.edu.au/record=b1731578~S1) · [archive.org](https://archive.org/metadata/bookoffiveringsg00miya/metadata) (03-pesquisa)
- [James Clear, "Continuous Improvement"](https://jamesclear.com/continuous-improvement)
- [Cunningham, OOPSLA 1992](https://c2.com/doc/oopsla92.html)
- [ANBIMA, 14/12/2022](https://www.anbima.com.br/es_es/imprensa/marcacao-a-mercado-e-tema-de-novo-curso-gratuito-da-anbima.htm)
- [EC 16/1997 (art. 77 da CF)](https://www.planalto.gov.br/ccivil_03/constituicao/Emendas/Emc/emc16.htm) · [ABCdoABC, 2º turno de 25/10/2026](https://abcdoabc.com.br/eleicoes-2026-tse-preve-resultado-20h30-21h/)
- Edição Kikuchi: [Martins Fontes](https://www.martinsfontespaulista.com.br/o-livro-dos-cinco-aneis-905742/p)
- Greene: [Estante Virtual](https://www.estantevirtual.com.br/livro/maestria-09J-0785-000-BK) · [getAbstract](https://www.getabstract.com/pt/resumo/maestria/24767)
- Clear BR: [BookWyrm](https://bookwyrm.de/book/29251/s/habitos-atomicos) e 03-pesquisa §5.3

**Não acessível nesta rodada:**
- texto da edição Kikuchi (Google Books com captcha e cota da API esgotada);
- página da Sextante (404);
- página do Kodansha 学術文庫 (403; usado só o trecho do resumo da busca);
- texto normativo da ANBIMA sobre marcação a mercado;
- portal de resultados do TSE.
