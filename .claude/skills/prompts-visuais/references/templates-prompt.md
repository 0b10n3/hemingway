# Templates de prompt por estilo de ilustração

Esqueleto preenchível, não regra nova. A tabela de hex autorizados, o vocabulário de cada
estilo e o checklist de validação moram em `estilos-ilustracao.md` — este arquivo não repete
nenhum dos dois, só acelera a primeira frase de um prompt e reduz a chance de sair vago demais
e obrigar reprocessamento no gerador.

Use depois de `briefing-ilustracao.md` (etapa 8a) já ter dado o conceito, a operação
(extensão/cruzamento/torção) e a estrutura de metáfora (justaposição/fusão/substituição) —
nunca antes.

## Template — Colagem editorial (todo post, qualquer linha editorial)

```
[Sujeito/objeto único, recortado em papel de cor chapada] + [camadas visíveis separadas por
degrau de tom entre os hex da pilha — luz uniforme de scanner de mesa, sem sombra projetada,
cada folha uma cor perfeitamente uniforme de borda a borda] + [retícula de meio-tom ou
desalinho de registro tipo risograph, se o conceito pedir] + [fundo: chalk ou deepForest —
ver estilos-ilustracao.md] + [entre 3 e 7 cores ≥1% do quadro; lime-500 uma vez só, até 1%
do quadro, se e só se há virada/saída/ponto de explicação no conceito] + [composição
assimétrica, diagonal dominante — ou centrada/simétrica, se o argumento for mostrar
mecanismo, ver bloco de precisão mecânica abaixo] + [proporção]
```

### Extensão — quando o argumento pede precisão mecânica

Some ao template acima, no lugar da composição assimétrica padrão, quando a peça precisar
mostrar um mecanismo por dentro (herdado do antigo "Estilo B", ver `estilos-ilustracao.md`,
"Quando o argumento pede precisão mecânica" — continua sendo papel recortado com degrau de
tom, não outra técnica):

```
[Peça/mecanismo único, em corte ou vista explodida, camadas de papel alinhadas no mesmo eixo,
projeção ortogonal — sem perspectiva] + [linha de construção como tira fina de papel
recortado, marcando eixo/centro/extensão] + [chamada com linha-guia em papel fino até a peça
que importa, sem rótulo de texto] + [marca de cota em papel, se o argumento envolver prazo/
distância/proporção] + [fundo: deepForest ou chalk] + [lime-500 marca só a peça que o
parágrafo está explicando; resto em verde estrutural] + [composição centrada e simétrica] +
[proporção]
```

## Lembrete de formato (não repetido de `estilos-ilustracao.md`, só citado)

Todo hex citado por nome de token; nenhum "glow"/"glowing"/"luminous"/"bloom"/"gradient"/
"shadow"/"drop shadow" — regras agnósticas de marca, valem para qualquer gerador. A sintaxe específica do gerador ativo
(cena narrada vs. lista de palavras-chave, se há ou não negative prompt, checklist de
fechamento) mora em `references/geradores/<gerador-ativo>.md` — hoje,
`references/geradores/nano-banana-pro.md`.
