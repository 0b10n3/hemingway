# Etapa 5 — Crítica estrutural

`linha_editorial: Notas de um Professor`. Sem validação argumentativa de carreira/tese
pessoal (essa sub-etapa é exclusiva da linha Spoiler) — os critérios aqui são a Ficha de
Saída, os oito movimentos e as regras transversais de `docs/BACKWARDS_DESIGN.md`.

## Rodada 1

### Achados

#### 1. Subtítulo não carrega a tese — só o roteiro (assunto)
- **Localização:** front-matter, `subtitulo: LCA — quanto rende, quanto custa, quanto vale`.
- **Severidade:** alta.
- **Diagnóstico:** o movimento 0 exige que o subtítulo, sozinho, entregue a tese de fundo
  (campo 3 da Ficha: "A LCA é uma dívida do banco, não do agro — e a isenção não é
  generosidade, é um benefício fiscal repartido entre banco e investidor"). O subtítulo atual
  é o roteiro das três perguntas (agenda), não a tese. A tese mais forte do texto nunca
  aparece no gancho — ela só surge fragmentada, em dois parágrafos distintos e distantes no
  meio do corpo (ver achado 6).
- **Por que importa:** é o padrão explícito de "insight enterrado" — o achado mais forte do
  post não está identificável no título/subtítulo, está no meio de parágrafos. Pede retorno
  pontual à etapa de estrutura para decidir como o campo 0 (Título + deck) vai carregar a
  tese sem perder a utilidade didática do roteiro rende/custa/vale.

#### 2. Ordem das seções não segue a ordem prometida na abertura
- **Localização:** abertura (bullets "quanto rende / quanto custa / quanto vale") vs.
  sequência real: "O lado de quem emite" (custa) → "O lado de quem compra" (rende) → "Como o
  banco define a taxa de emissão" (custa, de novo) → "Quanto a LCA vale hoje" (vale).
- **Severidade:** média.
- **Diagnóstico:** a abertura estabelece um contrato de leitura explícito na ordem
  rende→custa→vale; a entrega real é custa→rende→custa→vale, com o bloco de custo partido em
  duas seções não-adjacentes e "rende" encaixado no meio.
- **Por que importa:** quebra a expectativa que o próprio texto cria na primeira página.

#### 3. CRA — o vizinho do teste de transferência — nunca é definido por extenso no corpo
- **Localização:** primeira menção em "O que é uma LCA" e na seção "LCA não é CRA".
- **Severidade:** média.
- **Diagnóstico:** a regra 5.1 (cadeia de glosas) exige definição funcional entre parênteses
  na primeira ocorrência de todo acrônimo. CRA nunca recebe isso no texto publicado —
  "Certificado de Recebíveis do Agronegócio" só existe em `02-estrutura.md`.
- **Por que importa:** CRA é o próprio teste de transferência do campo 2 da Ficha de Saída —
  enfraquece a execução do movimento mais importante da Ficha, mesmo com a lógica de
  contraste correta.

#### 4. CDCA, CDA e WA citados sem glosa e nunca mais usados
- **Localização:** "O que é uma LCA", primeiro parágrafo.
- **Severidade:** média.
- **Diagnóstico:** três acrônimos aparecem uma única vez, sem definição funcional e sem
  retomada — viola a regra 5.6 e o princípio de carga cognitiva do §1.
- **Por que importa:** impõe leitura de três siglas desconhecidas sem ganho argumentativo.
  Candidato a corte, não a glosa.

#### 5. Outros acrônimos técnicos sem glosa: FGC, FGCoop, CMN
- **Localização:** "O risco é o banco" (FGC, FGCoop); "O lado de quem emite" (CMN).
- **Severidade:** média.
- **Diagnóstico:** mesmo padrão dos achados 3/4 — regra 5.1 aplicada de forma inconsistente.
- **Por que importa:** FGCoop, bem menos conhecido, merece a glosa mais do que FGC.

#### 6. Tese de fundo (campo 3) nunca aparece unificada e isolada — nem no início nem no fim
- **Localização:** metade em "O que é uma LCA", outra metade em "O lado de quem emite"; o
  fechamento não retoma nenhuma das duas em frase isolada.
- **Severidade:** média.
- **Diagnóstico:** a regra 5.4 exige a tese isolada em linha própria pelo menos duas vezes —
  no movimento 2 e no movimento 9. Aqui aparece fragmentada e nunca reaparece inteira no
  fechamento.
- **Por que importa:** falha explícita do checklist de publicação (§6, item 3).

#### 7. Bibliografia anotada só parcialmente
- **Localização:** "Para continuar aprendendo".
- **Severidade:** média.
- **Diagnóstico:** dos 4 itens, só a Lei 11.076 tem razão declarada.
- **Por que importa:** movimento 10 e checklist §6 exigem bibliografia anotada item a item.

#### 8. "O Lado de Lá" (movimento 4) é raso frente ao framework e frente ao peso do lado do investidor
- **Localização:** "O lado de quem emite" + "Como o banco define a taxa de emissão" (2
  seções) vs. "O lado de quem compra" + "Quanto a LCA vale hoje" (8 subseções).
- **Severidade:** média.
- **Diagnóstico:** o framework define o movimento 4 como o lugar do rigor institucional (ALM,
  compulsório, LCR/NSFR, spread). O texto toca ALM numa frase e não menciona compulsório nem
  LCR/NSFR.
- **Por que importa:** o campo 7 da Ficha pede peso comparável entre os dois lados do balcão;
  hoje o lado do investidor recebe claramente mais desenvolvimento estrutural.

#### 9. "Como o banco define a taxa de emissão" abre com fórmula antes de sentido
- **Localização:** início da seção.
- **Severidade:** baixa.
- **Diagnóstico:** a seção começa direto na fórmula, sem frase prévia dizendo o que a
  decomposição significa para o leitor.

#### 10. "Lastro não transfere risco" é repetida e contrastada, mas o mecanismo nunca é nomeado
- **Localização:** "O que é uma LCA" → "O risco é o banco" → "LCA não é CRA".
- **Severidade:** baixa.
- **Diagnóstico:** o texto nunca nomeia o mecanismo legal específico (ausência de patrimônio
  separado/regime fiduciário na LCA, presente na CRA) que explica por que o lastro não
  segrega risco.

#### 11. "O lado de quem compra" mistura a promessa do título (rendimento) com risco e liquidez
- **Localização:** subseções "O risco é o banco" e "Carência e liquidez".
- **Severidade:** baixa.
- **Diagnóstico:** já justificado editorialmente na etapa 2 (deslocamento fazia sentido para
  aproximar da decisão de compra). Registro para constar, não pede mudança.

### Checklist de publicação (§6 BACKWARDS_DESIGN), item a item

1. Ficha de Saída com campo 2 respondido? **Passa.**
2. Erro-alvo específico o bastante? **Passa** — erro linear vs. composto, demolido com tabela.
3. Tese isolada, início e fim? **Falha no fim** — achado 6.
4. Movimento 4 existe de fato, dois lados do balcão com peso comparável? **Falha
   parcialmente** — achado 8.
5. Ponto cego por contraste com vizinho nomeado? **Passa**, mas achado 3 enfraquece a execução.
6. Todo acrônimo aberto na primeira ocorrência com definição funcional? **Falha** — achados 3,
   4, 5.
7-9. Fora de escopo desta etapa (verificação quantitativa é etapa 7; visuais só etapa 8/9).
10. Ponte de série explícita? **Passa.**
11. Bibliografia 3–4 itens, mínimo 2 livros, cada anotado? **Falha em "cada anotado"** —
    achado 7.
12. Nenhuma frase condescendente? **Passa.**

### Veredito da rodada 1

O argumento geral se sustenta e o mapeamento aos oito movimentos continua correto — não há
seção sobrando nem faltando, a arquitetura de fundo não precisa ser refeita. O achado 1 é
severidade alta e pede retorno pontual à etapa 2 (campo 0 da Ficha de Saída) antes de seguir.
Os demais achados são de acabamento/conteúdo faltante, corrigíveis dentro da própria etapa 4
sem nova rodada de reestruturação. **Não está pronto para a etapa 6** até o achado 1 ser
resolvido e os achados médios endereçados.
