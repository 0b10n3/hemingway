# Taxonomia estilométrica — os nove eixos

Usada pelo subagente `extrator-de-estilo` (`.claude/agents/extrator-de-estilo.md`) e pela
agregação manual em `forja-de-voz`. Ver `pesquisa/frente-b-estilometria.md` para a
justificativa de pesquisa por trás desta taxonomia e dos limiares abaixo.

## Os nove eixos

1. **lexico** — campos semânticos recorrentes; termos técnicos explicados vs. pressupostos;
   formalidade; anglicismos aceitos/rejeitados; palavras-assinatura; palavras evitadas.
2. **sintaxe** — comprimento e variação de frase; coordenação vs. subordinação; posição da
   oração principal; aposto, parêntese, travessão; frase curta como ênfase.
3. **pontuacao** — inventário por eixo; onde cai a quebra de parágrafo; dois-pontos como
   articulador; listas vs. prosa corrida.
4. **arquitetura** — como abre (cena, dado, pergunta, tese, objeção); como sustenta; como
   fecha; densidade e função dos subtítulos; onde entra o exemplo em relação ao conceito.
5. **figuras** — analogias e metáforas, domínio de origem; grau de extensão; retomada ao fim.
6. **postura** — distância do leitor; primeira pessoa; autoridade declarada ou implícita;
   como admite incerteza; humor; tratamento da discordância.
7. **leitor** — conhecimento prévio pressuposto; introdução do desconhecido; pergunta
   retórica; imperativo; chamada para ação.
8. **tecnico** — notação; apresentação de fórmula (inline/display/glosa); tabela vs.
   gráfico; citação de norma/regulação; tratamento de dado desatualizado.
9. **formatacao** — negrito, itálico, código; destaque e citação em bloco; comprimento
   típico de bloco; título e subtítulo.

## Esquema de saída do extrator-de-estilo

```json
{
  "arquivo": "caminho/relativo/ao/repo",
  "genero": "substack | dissertacao | linkedin | admirada:<autor-slug>",
  "palavras": 0,
  "eixos": {
    "lexico": [ { "traco": "...", "frequencia": "sempre|frequente|ocasional|evita|nunca", "ocorrencias": 0, "evidencias": ["trecho ≤25 palavras"], "contraexemplo": "opcional" } ],
    "sintaxe": [], "pontuacao": [], "arquitetura": [],
    "figuras": [], "postura": [], "leitor": [], "tecnico": [], "formatacao": []
  },
  "antipadroes_observados": [],
  "incerteza": "o que este arquivo não permite concluir"
}
```

## Limiares de evidência (agregação)

- **Regra do guia:** ≥2 ocorrências, em ≥2 arquivos distintos do mesmo gênero (ou entre
  gêneros — ver abaixo).
- **`[cross-gênero]`:** traço presente tanto em amostras de gêneros muito distintos (ex.
  Substack e dissertação) quanto no mesmo eixo — confiança mais alta, porque sobrevive à
  maior variação de formato do corpus.
- **Condicionado ao gênero:** traço com ≥2 ocorrências mas só dentro de um único gênero/
  subgênero — vira regra da seção "Regras condicionadas ao gênero" (§4 do guia), não regra
  geral.
- **Em observação:** uma ocorrência só, ou evidência espalhada mas abaixo do limiar — entra
  no §8 do guia, nunca no §3/§4.
- **Piso de confiabilidade do corpus:** pesquisa recomenda ~5.000 palavras por amostra
  individual para confiança alta, e um corpus total de ~8 textos / ~10.000 palavras próprias
  como piso de estabilidade. Abaixo disso, `confianca_global` no frontmatter do guia deve
  ser `media` ou `baixa`, nunca `alta`.
- **Preferir traço estrutural a traço de conteúdo** ao decidir se algo é "voz" ou só
  "assunto do texto" — pontuação, sintaxe e estrutura de argumento generalizam melhor entre
  textos de temas diferentes do que vocabulário específico de um produto financeiro.

## Amostra admirada — regra adicional

Para `genero: admirada:*`, todo `traco` deve ser um **movimento de procedimento**
("abre com cena datada antes da tese"), nunca vocabulário-assinatura do autor admirado.
`evidencias` continua obrigatório (trecho ≤25 palavras), mas serve só para ancorar o
movimento observado — nunca para ser reaproveitado como texto no guia final ou em qualquer
post.
