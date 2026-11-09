# Caso 01 — A Corda e o Arco (2026-11-02-a-barriga-da-curva)

- **Data:** 2026-11-09 · rodada 1 do `estrategista-marketing`
- **Parecer avaliado:** `../../posts/2026-11-02-a-barriga-da-curva/marketing.json` (commit 654d9ad)
- **Situação do post:** já publicado; parecer rodado como se estivesse no gate. Nada aplicado.
- **Quem julgou:** Claude, por delegação explícita do autor ("avalie e siga com o seu melhor
  julgamento"). Não é veredito do autor; ele pode revisar qualquer linha abaixo.

## Validação mecânica

`scripts/parecer.py validar` aprovou na primeira tentativa. Âncoras literais e únicas, só ids
citáveis do catálogo, limites de CTA respeitados.

## Vereditos

| ID | Veredito | Motivo |
|---|---|---|
| A1–A9 | procede | Diagnóstico coerente com o post e com FUNIL/AUDIENCES. A4 (objeção mestra "respondida de forma implícita") é o mais generoso dos nove. |
| C1 | aceito | Inscrição no primeiro quarto, como manda `regras-cta.md`; entra logo depois do gancho dos R$ 2.292,17, antes da explicação. |
| C2 | **recusado** | O texto ("medir onde você está em outras habilidades da mesa") descreve o Skill Check sem fonte: nenhum arquivo de `strategy/` nem o catálogo diz o que o teste avalia. O próprio agente apontou isso em X2. |
| C3 | aceito | Botão logo depois do pedido de encaminhamento que o autor já escreveu. |
| C4 | aceito | Segundo botão de inscrição, no anúncio do próximo texto. Depende de X1: se a frase do FIDC mudar, a âncora muda. |
| R1 | aceito | Melhor item do parecer: liga "No último texto…" ao DU/252 e resolve a ressalva do A6. |
| R2 | aceito | O post da LCA traz a conta de empate LCA × CDB. |
| R3 | aceito | Condições Variáveis tem a seção "Percentual do CDI não é CDI mais *spread*". |
| B1 | aceito | "Qual o regime? Composto ou linear?" existe no checklist do DU/252 (l. 253). |
| X1 | procede | Conferido: o DU/252 prometeu o FIDC como próximo texto, e este adia de novo. |
| X2 | procede | Risco real, e o agente o pegou sozinho. |

**Resultado:** 9 de 10 itens acionáveis aceitos; 2 de 2 riscos procedem; 0 âncoras inválidas;
0 itens fora do catálogo.

## O que o caso ensina

1. **Falha:** o agente escreveu um CTA descrevendo um produto que o catálogo não descreve. Ele
   sinalizou o risco (X2), mas o certo seria não afirmar o conteúdo do produto no texto
   sugerido. **Correção de dado, pendente do autor:** registrar em `marketing/ofertas.yaml` o
   que o Skill Check avalia. Sem isso, todo CTA para ele vai repetir o problema.
2. **Acerto a manter:** os três links internos reaproveitam menções que o autor já faz, sem
   acrescentar palavra ao post (o padrão do exemplo 3 de `exemplos.md`).
3. **Acerto a manter:** o agente cruzou este post com outro do catálogo (X1) e achou uma
   inconsistência editorial que nenhuma etapa anterior viu.

## Desdobramentos (2026-11-09)

- **X1:** o autor cancelou o texto sobre FIDC. A promessa saiu dos três posts que a faziam
  (Condições Variáveis, DU/252 e este). Por isso o X1 saiu do `marketing.json` e o C4 passou para
  a frase anterior do mesmo parágrafo. A versão avaliada acima é a do commit 654d9ad.
- **C2/X2:** `marketing/ofertas.yaml` passou a ter o `resumo` do Skill Check (fonte:
  `apps/skill_test/docs/metodologia.md`). O agente ganhou a regra de descrever oferta só pelo
  `resumo` do catálogo. O teste dessa regra fica para o próximo caso que propuser CTA para
  o Skill Check.
