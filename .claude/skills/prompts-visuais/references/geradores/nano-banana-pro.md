# Adaptador de gerador — Nano Banana Pro (Google, Gemini)

Gerador ativo hoje (ver `prompts-visuais/SKILL.md`). Sintaxe e restrições específicas deste
motor — o vocabulário de estilo, a paleta e as regras de marca continuam em
`estilos-ilustracao.md`; este arquivo só cobre a camada condicional de "como escrever para
este gerador em particular".

Extraído de `estilos-ilustracao.md` em 31/08/2026 (revisão do processo texto→visuais, Fase C)
para separar regra agnóstica de regra de gerador — ver
`pesquisa/frente-e-visuais/02-proposta.md`, item B.4. Conteúdo inalterado na extração.

## Como escrever o prompt

Fonte: [guia oficial de prompting do Nano Banana](https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-nano-banana)
(Google Cloud). Três achados que mudam o formato antigo:

1. **Prompt é cena narrada, não lista de palavra-chave.** O guia é explícito: *"A simple list
   of keywords won't cut it; you need to describe the scene narratively."*
2. **Enquadramento positivo.** Descreva o que deve existir, não o que não deve. "Fundo
   deepForest chapado" funciona; "sem gradiente" não.
3. **Negative prompt não é suportado** pelo Nano Banana Pro — o guia não oferece o recurso e
   recomenda enquadramento positivo no lugar. Por isso o bloco `### Negative prompt` saiu do
   formato de `ilustracoes.md`: escrever um era teatro, o gerador nunca leu.

### Estrutura

Template do guia oficial, adaptado:

```
[Sujeito] + [Ação/estado] + [Contexto] + [Composição] + [Estilo e materialidade] + [Paleta com hex] + [Proporção]
```

### Checklist antes de fechar um prompt

- [ ] O conceito veio de `briefing-ilustracao.md` (etapa 8a), com os três conceitos
      divergentes gerados e os quatro testes de rejeição aplicados? **Estilo é a última
      decisão — se você chegou aqui sem briefing, volte.**
- [ ] A composição escolhida (pessoal/assimétrica ou precisão mecânica/centrada) bate com o
      que o conceito pede — não com a linha editorial, que não determina mais estilo desde
      2026-09-01 (`estilos-ilustracao.md`, "Por que um estilo só")?
- [ ] Todo hex citado existe na tabela de hex autorizados (`estilos-ilustracao.md`)?
- [ ] A palavra "glow", "glowing", "luminous", "bloom" ou "gradient" **não** aparece?
- [ ] Lime aparece em exatamente um elemento (ou em nenhum, se não há virada/foco)?
- [ ] O prompt descreve cena narrada, sem cauda de palavras-chave soltas?
- [ ] Toda restrição está em forma positiva?
- [ ] Nenhum texto, número ou rótulo é pedido dentro da imagem?
- [ ] A proporção é uma das suportadas (1:1, 3:2, 2:3, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9)
      e a resolução é 1K, 2K ou 4K?

### Proporção padrão

- Ilustração inline de post: **3:2**, 2K.
- Peça de abertura vertical: **4:5**, 2K.
- Faixa larga: **16:9**, 2K.

### Limitação conhecida: sem referência de estilo entre imagens

Diferente do `--sref` do Midjourney (ver `midjourney-v6-1.md`), o Nano Banana Pro não tem
mecanismo de referência de estilo via URL para amarrar múltiplas peças do mesmo post à mesma
atmosfera exata. Alternativa registrada, sem fingir paridade: repetir os mesmos termos de
material/luz/paleta em cada prompt do post (mesma linguagem descritiva, não só mesma tabela
de hex) — funciona para consistência de família, não para identidade pixel a pixel entre
peças.
