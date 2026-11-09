# Regras de links internos

Fontes: Google Search Central, *Link best practices* (texto de link descritivo, razoavelmente
conciso e relevante para as duas pontas), e o modelo de *topic clusters* (posts de um tema
ligados entre si e a um pilar, nos dois sentidos).

## Referências (deste post para outros)

- De 0 a 4 por post. Zero é resposta válida: "nenhuma sugestão" é melhor que link forçado.
- Só itens do catálogo com `citavel: true`. Nunca o próprio post. Nunca URL fora do catálogo.
- O link entra **onde o leitor teria a pergunta que o destino responde**, e você registra essa
  pergunta em `pergunta_do_leitor`. Se não consegue formular a pergunta, o link não entra.
- Prioridade: o pilar do cluster do post, depois os membros do mesmo cluster, depois outros
  clusters. Os posts do cluster `investimentos-pessoais` são da fase anterior da newsletter
  (investidor pessoa física): use só quando o leitor precisar exatamente daquela base.
- O texto do link é, de preferência, um trecho que já está na âncora (`texto_link` contido em
  `ancora`): o post não ganha palavra nova. Só use `frase_nova` quando nenhum trecho da âncora
  descrever o destino. A frase nova entra logo depois da âncora, na voz do autor.
- Texto de link descritivo: diz o que o leitor encontra do outro lado ("o texto sobre a LCA",
  "a contagem de dias úteis"). Proibido: "clique aqui", "aqui", "leia mais", "saiba mais",
  "este link".
- Repare em menções que o próprio autor já faz a outros textos ("No texto sobre a LCA",
  "No último texto", `[LINK: ...]`, `[VERIFICAR: link ...]`). São as melhores âncoras.

## Backlinks (de posts antigos para este)

Toda sugestão de referência vem acompanhada da lista de posts antigos que deveriam apontar
de volta: ligação nos dois sentidos. Em `backlinks_sugeridos[]`:

- `origem_id`: o post antigo, do mesmo cluster ou o pilar dele.
- `ancora_na_origem`: trecho literal do post antigo (está em `posts/<slug>/post.md`) onde o
  link caberia; `null` só para posts `legado:`, que não estão no repo.
- O autor edita esses posts à mão no Substack. Eles viram lista de tarefas.

Um post novo sem cluster, ou num cluster só dele, pode ficar sem backlinks.
