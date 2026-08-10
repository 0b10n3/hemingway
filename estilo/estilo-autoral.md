---
versao: 1.0.0
atualizado_em: 2026-08-10
commit_base: 3db8d17
corpus: { textos: 7, palavras: 25685, periodo: "não datado — ver _arquivo/MANIFESTO.md" }
confianca_global: media
---

# Guia de voz — Syntaxis

## 1. Retrato em cinco linhas

Você explica finanças como quem já foi aluno de matemática antes de ser assessor: nunca
deixa um termo técnico sem gloss, mas também nunca resiste a uma ironia sobre a própria
indústria que descreve. Sua marca registrada é abrir com uma cena pessoal ou uma pergunta
provocativa, sustentar o argumento citando um estudo acadêmico nomeado (autor, ano, revista),
e fechar pedindo para o leitor compartilhar. Mas você tem **duas vozes distintas**, não uma —
ver §4 — e a maior parte da instabilidade do seu texto vem de não escolher qual delas está
falando.

## 2. Objetivos do meu texto

| Tipo de texto | Objetivo | Fonte |
|---|---|---|
| Post de Substack | Educar e construir audiência para o funil gratuito → curso → mentoria | `_arquivo/MARKETING_REVIEW.md` §5 |
| Conteúdo de curso | Ensinar com rigor, sustentar credibilidade técnica | inferido, a confirmar |
| Marketing/aquisição | Falar às personas `#GENZ-FEAR`, `#GENZ-GREED`, `#Millennials-FEAR`, `#Millennials-GREED` | `_arquivo/MARKETING_REVIEW.md` §3.3 |

Detalhamento de público e personas: ver `_arquivo/MARKETING_REVIEW.md`. Este guia não repete
esse conteúdo — aponta para ele.

## 3. Regras (voz atual — descritivo)

Numeradas por confiança de evidência. `[cross-gênero]` = confirmado tanto em posts de
Substack quanto na dissertação (o par de gêneros mais distante do corpus — se um traço
sobrevive aos dois, é forte candidato a traço de autor, não de formato).

1. **Nunca deixa jargão sem gloss na primeira ocorrência.** No Substack, aposto entre
   parênteses logo após o termo. Na dissertação, `Definição` numerada antes de qualquer uso.
   `[cross-gênero]`
   Evidência: "O Goal Based Investing, ou investimento baseado em objetivos..." (objetivos);
   "Definição 1.1.1 (Espaço de Probabilidade)..." (dissertação); "LFT Letra Financeira do
   Tesouro), título pós-fixado..." (tesouro_selic).
   ✅ "O COE (Certificado de Operação Estruturada) costuma pagar bem ao assessor."
   ❌ "O COE costuma pagar bem ao assessor." *(sem gloss, pressupõe conhecimento)*

2. **Exemplo sempre depois do conceito, nunca antes.** `[cross-gênero]`
   Evidência: "Exemplo 1.5.1. Consideremos..." sempre após a Definição (dissertação);
   "Pedro é um engenheiro, casado..." aparece depois de definir GBI (objetivos); exemplo
   numérico do Tesouro Selic aparece após a definição do título (tesouro_selic).

3. **Dois-pontos como articulador de definição, nunca travessão triplo nem dois-pontos
   soltos sem função.** `[cross-gênero]`
   Evidência: "Agregação Estável: A composição..." (separação); "Chegamos assim a:"
   (dissertação); "A pergunta óbvia é: isso funciona?" (simples).

4. **Nunca usa negrito ou itálico de ênfase — aspas simples fazem esse trabalho.**
   Confirmado em 5 dos 6 posts de Substack como antipadrão explícito (o sexto, tesouro_selic,
   tem indícios de perda de formatação na conversão, não confirma nem contradiz).
   ✅ 'internamente homogêneo' (semelhantes entre si)
   ❌ **internamente homogêneo** (semelhantes entre si)
   Nota: itálico aparece pontualmente só para título de obra ou estrangeirismo isolado
   (ex. *Naive Set Theory*), nunca como ênfase de frase.

5. **Subtítulos H2 densos, um por movimento do argumento, sempre.**
   Confirmado em 6/6 posts de Substack e, com convenção diferente (numeração
   Capítulo.Seção), na dissertação. `[cross-gênero]`

6. **Autoridade construída citando estudo acadêmico nomeado — autor(es) e ano — nunca por
   afirmação de credencial própria.**
   Evidência: "Kinlaw, Kritzman e Turkington 2021" (separação, objetivos); "Victor DeMiguel,
   Lorenzo Garlappi e Raman Uppal. Em 2007" (simples); "Andrew Lo, renomado professor do MIT"
   (objetivos, separação).
   Confiança: forte nos posts ensaísticos (3/6); não observada nos explicativos.

7. **Aposto/parêntese explicativo logo após o termo técnico, frequentemente com travessão
   duplo.** Confirmado em 5/6 posts de Substack.
   Evidência: "que você pode assistir de graça no MIT OpenCourseWare -, apresentou..."
   (objetivos); "possuir um ETF é - na prática e na dor - o mesmo..." (separação).

8. **Cita instituição/regulador pelo nome quando o produto é regulado (CVM, Banco Central,
   B3, Copom), sem necessariamente citar o número da norma.**
   Evidência: "regulamentado pela Comissão de Valores Mobiliários CVM" (assessor);
   "Comitê de Política Monetária Copom) do Banco Central" (tesouro_selic); "A Resolução CVM
   175" (separação, este caso cita o número).

9. **Placeholder de imagem/gráfico é tratado como parte do argumento, não decoração** — os
   textos fazem referência verbal ao conteúdo visual ("A fórmula é:", "veja o gráfico
   abaixo") mesmo quando a imagem em si não está no arquivo. Ao escrever `posts/`, o
   placeholder `graf-NN`/`ilu-NN` deve ter legenda que realmente carregue informação (ver
   `CLAUDE.md` sobre os três entregáveis), porque este autor já demonstrou depender do visual
   para completar o raciocínio, não só ilustrá-lo.

## 4. Regras condicionadas ao gênero — **as duas vozes**

O achado mais importante desta extração: os 6 posts de Substack não formam um bloco
estilístico único. Eles se dividem nitidamente em dois subgêneros, e confundir um com o
outro é a causa mais provável de um texto "não soar seu".

### 4.1 Voz ensaística (`separação`, `objetivos`, `simples`, `assessor`)

- Abre com anedota pessoal ou pergunta provocativa, não com definição.
- Primeira pessoa presente (singular para memória/opinião, plural para conduzir o leitor).
- Humor e ironia leve constantes, sobretudo contra a própria indústria financeira.
- Metáfora e analogia frequentes (Ferrari/motor de uno, besta indomável, prateleira,
  coreografia), embora raramente retomadas no fechamento.
- Pergunta retórica como ferramenta de argumentação, não só de transição.
- Fecha com CTA de compartilhamento e gancho para o próximo texto.
- Admite exceção/incerteza pontualmente quando o argumento é genuinamente contestável.

### 4.2 Voz explicativa (`tesouro_selic`, `títulos_do_tesouro_nacional`)

- Abre com epígrafe de terceiro ou direto na definição — nunca com anedota própria.
- Terceira pessoa impessoal quase absoluta; primeira pessoa plural só para anunciar
  continuidade editorial ("discutimos", "abordaremos").
- Sem humor, sem ironia, sem tratamento de contra-argumento ou risco em tom alarmado.
- Praticamente nenhuma metáfora — a única figura por texto (se houver) não é retomada.
- Nunca admite incerteza; tom categórico do início ao fim.
- Sem CTA ao final; termina descrevendo o produto.

**Como decidir qual voz usar:** se o post tem tese defensável ou opinião (ex.: "você precisa
de um assessor?", "o simples funciona"), é ensaístico. Se o post é referência de produto
("o que é o Tesouro Selic"), é explicativo. Um post de referência escrito em voz ensaística
vai soar como se estivesse "vendendo" o produto; um post de tese escrito em voz explicativa
vai soar como se não tivesse opinião nenhuma — os dois são desvios perceptíveis.

### 4.3 Voz acadêmica (dissertação — não usar em Substack, mas informa registro técnico)

Terceira pessoa/primeira do plural de modéstia, nunca singular; zero metáfora; estrutura
Definição→Teorema→Demonstração→Corolário rígida; nunca fecha com síntese reflexiva, termina
no último resultado técnico. **Não é uma voz para Substack** — mas o rigor de sempre definir
antes de usar (regra 1) vem daqui, e é o traço mais valioso a preservar ao adaptar conteúdo
técnico para o público leigo.

## 5. Movimentos aspiracionais

Extraídos de Michael Lewis (3 textos), Ernest Hemingway (3 contos) e Malcolm Gladwell
(2 textos) — ver `_arquivo/MANIFESTO.md` para proveniência. São *procedimentos*, não
vocabulário. Cada um marcado com gatilho de uso.

### Michael Lewis
1. **Abre com cena datada e concreta antes da tese.** *Já parcialmente presente (voz
   ensaística abre com anedota) — reforça, não contradiz.* Gatilho: usar quando o post tiver
   um evento real e datável para ancorar (uma crise, uma mudança de norma), não só uma
   memória vaga.
2. **Travessão duplo para aside irônico do narrador.** *Já presente na voz atual.* Reforço
   direto — regra 7 ganha confiança extra por aparecer também nos admirados.
3. **Admite os limites do próprio entendimento técnico e transfere a validação para a
   credencial da fonte, em vez de fingir domínio.** Gatilho: em conteúdo que toca
   matemática financeira avançada (ex. derivativos, otimização), preferir "não vou entrar no
   mecanismo — mas quem entende, [autor X], diz que..." a uma explicação simplificada demais.

### Ernest Hemingway
4. **Confiar no leitor: omitir a explicação do porquê e deixar a justaposição de fatos
   carregar o sentido.** Gatilho: em vez de "isso é preocupante porque X", tentar "isso
   aconteceu. Depois aconteceu Y." e deixar o leitor concluir — usar com moderação, só em
   momentos de maior impacto (não substitui a regra 1, que é sobre jargão, não sobre
   argumento).
5. **Repetir a palavra-chave em vez de variar por sinônimo, para construir insistência.**
   *Já presente em grau leve (repetição de "ingênuo" em `simples`).* Gatilho: quando o
   argumento gira em torno de reabilitar um termo (como "ingênuo" ou "simples"), repetir a
   palavra-alvo em vez de driblar com sinônimos.

### Malcolm Gladwell
6. **Definir termo técnico/estatístico no instante exato em que ele aparece, em linguagem
   leiga, sem deixar pairando.** *Já é a regra 1 deste guia — coincidência forte entre voz
   atual e autor admirado.* Regra forte, não aspiracional.
7. **Estruturar o argumento como acúmulo de casos numerados (1, 2, 3...) que testam a tese,
   em vez de dedução linear sob um único subtítulo.** Gatilho: para posts ensaísticos
   longos com mais de um exemplo/fonte, considerar numerar os casos em vez de escondê-los
   sob subtítulos temáticos — ainda não testado nesta voz.
8. **Validar a intuição comum do leitor primeiro, minar caso a caso, só then declarar a tese
   invertida como aforismo curto.** Gatilho: para posts que combatem uma crença popular
   (ex. "diversificação simples supera modelo complexo"), abrir confirmando a crença ("todo
   mundo acha que...") antes de desmontá-la — `simples_funciona` já faz uma versão disso
   com Markowitz; vale generalizar.

## 6. Tensões conhecidas

- **Regra 1 (nunca deixar jargão sem explicar) vs. movimento aspiracional 4 (Hemingway:
  confiar no leitor, omitir).** A voz atual tende a fechar todo loop explicativo; Hemingway
  abre mão disso deliberadamente. Não resolvido — decisão por post: em conteúdo didático
  (voz explicativa), regra 1 vence sempre; em conteúdo ensaístico/opinativo, testar omitir
  a explicação óbvia uma vez por texto e ver se o efeito funciona.
- **Voz ensaística busca humor e ironia; voz acadêmica (dissertação) e explicativa evitam
  qualquer humor.** Não é uma tensão a resolver — é a fronteira do §4. O risco é aplicar
  humor num post explicativo "porque é a voz do autor" quando na verdade não é, para esse
  subgênero.
- **Metáfora raramente retomada no fechamento (traço atual) vs. Gladwell/Lewis que
  constroem o texto inteiro em torno de uma imagem sustentada.** Aspiracional ainda não
  testado — a hipótese é que retomar a metáfora de abertura no fechamento fortaleceria os
  posts ensaísticos sem forçar a voz.

## 7. Antipadrões

### 7.1 Meus (confirmados por evidência do corpus)
- Nunca usar negrito/itálico de ênfase (regra 4).
- Nunca apresentar tabela ou gráfico nativo — sempre placeholder de imagem (nota: parte
  disso é artefato de conversão dos arquivos fornecidos, não necessariamente escolha
  deliberada; sinalizado como incerteza em quase todas as extrações — reavaliar quando
  houver amostra com imagem/gráfico preservado).
- Na voz explicativa: nunca admitir incerteza, nunca contra-argumento, nunca humor — não são
  "erros", são a assinatura desse subgênero; o erro é usar isso na voz ensaística.

### 7.2 Tiques de texto gerado por IA em pt-BR (ver `pesquisa/frente-d-antipadroes-ia-ptbr.md`
para a lista completa de 43 pares ❌/✅ em 12 categorias)
Os mais relevantes para este autor, por já andar perto da linha:
- ❌ "É importante ressaltar que..." → ✅ cortar a frase, ir direto ao ponto (o autor já faz
  isso — só reforçando o limite).
- ❌ Fechos genéricos ("em suma, é essencial...") → ✅ o autor já fecha com CTA específico de
  newsletter ou gancho para o próximo texto — nunca com resumo genérico. Preservar.
- ❌ Tríade de adjetivos/exemplos previsível → observar ao gerar; o corpus não mostra esse
  tique, não introduzir.
- Ver `pesquisa/frente-d-antipadroes-ia-ptbr.md` para a lista completa antes de qualquer
  revisão final (etapa 6 do pipeline).

## 8. Em observação

Evidência insuficiente (uma ocorrência só, ou só num arquivo) para virar regra — candidatos a
promover quando `/forja-de-voz atualizar` rodar com mais amostras:
- Uso de reticências para sugerir continuidade/exemplos abertos (1 ocorrência clara, em
  `objetivos`).
- Analogia autobiográfica ligada à formação em matemática como ponte para conceito abstrato
  (aparece em `objetivos` e `simples` — na fronteira de virar regra; falta uma terceira
  ocorrência independente para confirmar).
- Tom irônico dirigido especificamente à "indústria financeira" como antagonista coletivo,
  nunca a uma pessoa nomeada (padrão em 3 textos ensaísticos — pode já merecer promoção na
  próxima atualização, mantido aqui por cautela nesta v1.0.0).
- Nenhuma amostra de LinkedIn foi fornecida nesta rodada — `_arquivo/amostras/proprias/linkedin/`
  está vazio. Todo traço "condicionado ao gênero Substack" pode, na verdade, ser condicionado
  a "não-LinkedIn" — não há como saber ainda.

## 9. Checklist de aderência

Dez itens verificáveis, usados no modo `auditar` de `/forja-de-voz`:

1. Todo termo técnico tem gloss ou definição na primeira ocorrência? (regra 1)
2. O exemplo aparece depois do conceito, nunca antes? (regra 2)
3. Zero negrito/itálico de ênfase no corpo do texto? (regra 4)
4. Cada seção tem subtítulo H2? (regra 5)
5. Alguma afirmação de peso é sustentada por autor+ano citado nominalmente, não por "estudos
   mostram"? (regra 6)
6. O texto está claramente numa das duas vozes (§4) e não mistura os dois tons no mesmo post?
7. Se é voz ensaística: tem CTA de compartilhamento e gancho final? Tem ao menos uma
   pergunta retórica genuína (não decorativa)?
8. Se é voz explicativa: está livre de humor, primeira pessoa singular e admissão de
   incerteza?
9. Nenhum tique de IA da lista em `pesquisa/frente-d-antipadroes-ia-ptbr.md` sobreviveu à
   revisão de linha?
10. Instituição/norma citada (se houver) está com nome correto e, quando relevante, número
    da resolução/lei?
