# Etapa 2 — Estrutura

A estrutura é a do rascunho do autor, que já chega com a Ficha de Saída preenchida e os
movimentos de `docs/BACKWARDS_DESIGN.md` §3 declarados ("Movimentos usados: 0, 1 (Modo A,
GPA), 2, 3, 4 (com materialidade curta), 5, 7, 8, 9, 10"). Esta etapa adota a Ficha, confere
se a sequência entrega a competência de saída e decide os visuais. Não reordena nada. As
únicas mudanças são as que o autor pediu na etapa 0 (ponte de série e data da abertura).

## Ficha de Saída

Adotada do rascunho. Só o campo 8 muda, pela decisão do autor na etapa 0.

| Campo | Preenchimento |
| --- | --- |
| **1. Competência de saída** | *Localizar*, na escritura de qualquer debênture, a posição do investidor na fila (espécie e tipo de garantia), os gatilhos que o protegem (covenants, vencimento antecipado) e quem decide uma renegociação (quórum da escritura e da lei). *Converter* % do CDI em CDI + spread e *estimar* quanto o PU cai quando o spread do devedor abre. (Autor, verbatim.) |
| **2. Teste de transferência** | Nota comercial (Lei nº 14.195/2021). Se o leitor não consegue refazer as perguntas trocando escritura por termo de emissão e S.A. por limitada, o texto falhou. (Autor, verbatim.) Para a etapa 7: conferir que as três perguntas de fato se transferem (a nota comercial tem termo de emissão, agente fiduciário e assembleia de titulares, mas não tem as quatro espécies do art. 58 da Lei das S.A.; a pergunta "onde estou na fila" muda de fonte, do nome da espécie para as garantias do termo). |
| **3. Tese de fundo** | "Na debênture, não há rede. Há contrato." Família da tese-mãe: o risco que sobra muda de endereço; aqui ele está no endereço de origem, sem FGC e sem patrimônio separado no meio. (Autor.) |
| **4. Erro-alvo** | Que "renda fixa" quer dizer condições fixas: que o debenturista tem um direito individual que só muda com a assinatura dele, e que a espécie escrita no nome diz como ele será tratado numa crise. (Autor.) Gente competente acredita nisso: os debenturistas da 18ª e 19ª emissões do GPA contestaram justamente por não terem assinado. |
| **5. Ferramenta prática** | Conversão % do CDI ↔ CDI+; sensibilidade do PU ao spread pela metodologia Anbima; roteiro de cinco perguntas para a escritura; taxa da prateleira × taxa indicativa. (Autor.) |
| **6. Âncora de autoridade** | Lei nº 6.404/1976, arts. 52 a 74; Lei nº 11.101/2005, arts. 41, 49, 83 e 163; Smith & Warner (1979); Varanda Neto, Santos e Mello (2019), caps. 8 e 19. (Autor; art. 83 acrescentado porque a tabela de espécies depende dele.) |
| **7. Os dois lados do balcão** | Emissor (por que debênture; quem fica com o subsídio: Lei nº 12.431 × Lei nº 14.801) × investidor e analista. Distribuidor entra pelas condições 1 e 3 do §4.3: o spread de prateleira altera o que chega ao investidor; e os veículos da XP são o canal sem o qual a PF não acessa a opção A do GPA. (Autor.) |
| **8. Ponte de série** | Vem do CRI/CRA, que terminou prometendo a debênture ("A debênture é o tema do próximo texto desta série", `posts/2026-09-28-o-certificado-nao-muda-o-devedor/post.md:290`) e chamou o CRA corporativo de "economicamente, uma debênture". Este texto cumpre a promessa → aponta para o **FIDC**, anunciado como próximo, sem o verbo "prometi" (autor, etapa 0). A nota comercial fica como teste de transferência, não como próximo texto. |

## Verificação: a estrutura entrega a competência de saída?

| Seção do rascunho | Movimento(s) | Observação |
| --- | --- | --- |
| Título + deck ("Renda Fixa, Condições Variáveis" / "Debêntures, escritura e quem decide quando a empresa não paga") | 0 | O título carrega o erro-alvo invertido; o deck anuncia o assunto e a pergunta, não a tese. Aceitável (precedente do CRA). A etapa 5 pode opinar; não é mudança desta etapa. |
| Abertura (GPA, 7/10) + ponte com o CRA + três perguntas | 1 (modo A) | Termina nas três perguntas (quem deve, o que o contrato garante e quem pode mudá-lo, quanto vale), que são a pergunta-âncora. Modo A obriga o movimento 7, que existe. ✓ |
| "A versão que se conta… A primeira parte é verdade. A segunda, não." + rede/contrato | 2 (O Mito) | Mito enunciado e tese isolada em linha própria. ✓ |
| "O que é uma debênture" | 3 (A Anatomia) | Base legal (arts. 52, 56–58, 61, 68), emissor (inclui limitadas, DREI 2026), espécies, remuneração, IR, tabela LCA × CRA × debênture. Fecha com a frase-sinal do §5.3: "Até aqui, é o que qualquer material de oferta conta. O que decide o seu resultado está na escritura, e quase ninguém lê a escritura." Usada uma vez. ✓ |
| "O lado de quem emite" + "Quem fica com a isenção" | 4 (O Lado de Lá) + 6 curto (materialidade em prosa: R$ 433 bi em 2025, incentivadas em 2026) | Explica por que a empresa emite e quem fica com o subsídio (Lei nº 12.431 × nº 14.801), com conta própria declarada. ✓ |
| "O que fica entre você e a empresa" (fila, gatilhos, voto) | 5 (O Ponto Cego) | Por contraste com vizinhos nomeados: LCA (FGC), CRA (patrimônio separado), e a espécie da Lei das S.A. contra a fila da Lei nº 11.101. Entrega os três primeiros objetos do campo 1 (fila, gatilhos, quórum). ✓ |
| "Quanto rende e quanto vale" (4 subseções) | 8 (A Prateleira) + extensão de matemática financeira (§4.2) | Entrega "converter" e "estimar" do campo 1. Distribuidor pela condição 1 do §4.3 ("A taxa da prateleira"). As cinco perguntas são a competência em forma de checklist. Bloco profissional (montar a fila) atende a decisão (c) do §7.1, já tomada pelo autor. ✓ |
| "De volta ao GPA" | 7 (Fechamento do Loop) | Relê o caso com as ferramentas; laço com a frase do juiz. Distribuidor pela condição 3 (canal da XP). ✓ |
| "Fechamento: sem rede" | 9 (Síntese + Ponte) | Tese isolada pela terceira vez, generalização lateral (LCI → CRA → debênture), teste de transferência explícito (nota comercial) e ponte. A ponte é corrigida na etapa 4 (campo 8). |
| "Para continuar aprendendo" | 10 | Seis itens, um livro, duas leis. Fora da regra §5.7. Tensão registrada no briefing para o gate; a etapa 4 não mexe. |

**Conclusão:** a sequência produz a competência do campo 1, na ordem fila → gatilhos → voto →
preço, e a seção "De volta ao GPA" aplica as cinco ferramentas ao caso de abertura. A tese
aparece isolada no início e no fim (§5.4). ✓

## Notas para as etapas seguintes

1. **Ponte (etapa 4).** Trocar "No texto do CRA, prometi o FIDC. Ele vem no próximo, e o
   momento ajuda" por uma formulação que anuncie o FIDC sem dizer que foi prometido. Na
   abertura, o parágrafo "No texto sobre CRI e CRA, escrevi que…" pode ganhar a promessa
   cumprida, se couber sem alongar. Mudança mínima.
2. **Data (etapa 4).** "Na quarta-feira, 7 de outubro" → "Em 7 de outubro".
3. **Fórmulas (etapa 4/9).** Os dois blocos ```latex``` viram `$$ … $$`, como no post do CRA
   (precedente: `posts/2026-09-28-o-certificado-nao-muda-o-devedor/post.md:132`).
4. **Tabelas.** A Substack não renderiza tabela Markdown (precedente do CRA). As quatro
   tabelas do corpo viram peça-imagem (ver abaixo). O texto ao redor já faz referência verbal
   a elas ("Lado a lado com os produtos…", "A tabela mostra…"), como pede a regra 9 do guia.
5. **Verificação (etapa 7).** Recalcular as sete contas do apêndice do autor; conferir as 22
   linhas da tabela de fontes; abrir o original do Neofeed (Chilli Beans); ticket de R$ 15 mi
   no plano homologado; prenome de Anderson; CDI efetivo; teste de transferência da nota
   comercial (campo 2).

## O que fica de fora

Os cortes do autor, mantidos: Casas Bahia; anexos ("derivativos e renda fixa", Manual do
Emissor); série anual de emissões com gráfico. Também fora: debênture conversível em
profundidade (fica na linha do GPA), rating, oferta pública × restrita (Resolução CVM nº 160).

## Onde entra graf-NN / diag-NN / info-NN

Mesma restrição do post do CRA: a Substack não renderiza tabela Markdown, então tabela vira
peça-imagem. Critério aplicado a cada ponto:

| Peça | Onde | Tipo | Por quê (e por que os outros perderam) |
| --- | --- | --- | --- |
| **diag-01** | "Lado a lado com os produtos dos textos anteriores" (LCA × CRA de devedor único × debênture, 5 atributos) | Tabela-imagem | Comparação estrutural entre três produtos, sem métrica → diag (critério 2). graf perde: não há série. info perde: é uma comparação só. Continua a série: o diag-02 do CRA comparava LCI/LCA × CRI/CRA. |
| **diag-02** | Tabela "Espécie ou garantia × o que o nome sugere × recuperação judicial × falência" | Tabela-imagem | Relação estrutural (espécie → classe → posição na fila), sem métrica → diag (critério 2). graf perde: sem série. info perde: uma peça carrega a ideia. É a peça central do ponto cego. |
| **graf-01** | Tabela "% do CDI → CDI + spread" (4 níveis de CDI × 3 percentuais) | Tabela-imagem com números | Série numérica real (cálculo próprio pela fórmula do texto) → graf (critério 1). O autor cogitou um gráfico de linha (spread × nível do CDI) e preferiu a tabela; a escolha dele fica. Transformar em curva seria mudança de conteúdo. |
| **graf-02** | Tabela "Spread exigido → PU em % do valor na curva" (4 linhas) | Tabela-imagem com números | Série numérica (spread → PU), cálculo próprio → graf (critério 1). Mesmo raciocínio. |
| — info-NN | — | Não se aplica | Nenhuma síntese exige mais de uma peça. Padrão: não tem. |
| — materialidade | "O lado de quem emite" | Sem peça | O autor não abriu série primária consolidada e declarou materialidade curta, em prosa. Dado decorativo enfraquece o texto (§3, tabela de opcionais). Fica em prosa. |

Formato: tabelas-imagem em Plotly (`go.Table`) com tokens de `../../brand/`, como no post do
CRA.

## Confirmação dos três pilares

- **Dado:** caso GPA (R$ 4,57 bi, 57,49%, R$ 1,56 bi, 88,4% na opção A, recuperação de 63% a
  69%), Chilli Beans, volumes Anbima, contas de conversão e de PU.
- **Narrativa:** arco GPA abertura → anatomia → emissor → ponto cego → prateleira → volta ao
  GPA, com o laço da frase do juiz.
- **Visual:** diag-01, diag-02, graf-01, graf-02.
