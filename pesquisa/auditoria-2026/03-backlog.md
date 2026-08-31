# Fase 3 — Backlog (itens abertos das Fases 0-2, não é proposta de diff)

Nada aqui foi decidido ainda — é o inventário do que a auditoria encontrou e não fechou.
Cada item aponta pra onde foi discutido, com o motivo de continuar aberto.

## 1. Dimensão oficial de capa da Substack — `[VERIFICAR]`

**Onde:** `02-processo-visual.md` §2.1. **Por que aberto:** `support.substack.com` bloqueou
fetch automático (403) nesta sessão; fontes secundárias divergem (1200×630 a 1456×1048,
proporção citada como 14:10, 3:2 ou 16:9 dependendo da fonte). **Convenção em uso enquanto
isso:** 16:9, ≥2400×1350px — cobre com folga qualquer mínimo citado, aprovada pelo autor em
29/08. **Para fechar:** tentar o fetch de novo com outro user agent, ou pedir para o autor
colar o texto da página oficial.

## 2. Paralelizar etapas 6 (linha/norma) e 7 (verificação técnica) — não decidido

**Onde:** `01-auditoria-skills.md`, "Ponto em aberto". **Evidência:** as duas etapas partem
do mesmo `04-draft-v1.md` já corrigido pela etapa 5 e nenhuma lê o resultado da outra — rodar
em paralelo pouparia uma etapa serial. **Por que não foi proposto como diff:** as duas
escrevem no mesmo arquivo; paralelizar edição concorrente é risco de conflito sem ganho
medido (regra "otimizar ≠ reescrever" — nenhuma evidência de retrabalho ou desperdício de
tokens no fluxo atual). **Se algum dia justificar revisitar:** desenho possível é cada etapa
gravar um diff próprio e a etapa 9 reconciliar — não desenvolvido, só registrado.

## 3. Sistema visual novo ainda não rodou ponta a ponta num post real

**Onde:** `00-contexto.md`, achado 1. **Situação:** os 3 posts publicados são anteriores ao
motor de briefing v2 e às categorias `capa`/`diag`/`info` da Fase 2 — o mais recente
(2026-08-25) ainda referencia `marca/tokens.json` removido e tem blocos `Negative prompt`
que o Nano Banana Pro não suporta. Consistente com a regra de não reescrever entregáveis
publicados, mas confirma que nada da Fase 2 foi validado em produção, só em teoria. **Para
fechar:** primeiro post novo que passar pela etapa 8 é o teste real — conferir se `capa.md`
sai obrigatório, se o critério da etapa 2 escolhe o tipo certo de visual, e se
`revisao-editorial` de fato pega uma paleta fora do token se alguém errar um hex.

## 4. Graphviz — reabrir só se algum diagrama precisar de layout de grafo automático

**Onde:** `02-processo-visual.md`, "Avaliação adicional de Graphviz". **Decisão atual:**
Plotly, pela fidelidade de marca já comprovada em `graf-NN`, não por peso (Graphviz é leve,
174 KB — a rejeição inicial por peso estava errada e foi corrigida). **Não instalado nesta
máquina** e sem `sudo` para instalar; se reabrir, `apt install graphviz` vira linha nova em
`README.md`. **Gatilho para reabrir:** diagrama com >8-10 nós que precise de layout
automático — nenhum caso citado neste pipeline chega perto disso hoje.

## 5. Smoke test dos skills de referência (item 3 da Fase 3)

**Onde:** esta sessão (nova, após reinício — pré-condição para o teste, ver `RELATORIO.md`
"Subagentes custom criados nesta sessão não ficam invocáveis..."). **O que testar:** disparo
de `voz-syntaxis` e `marca-syntaxis` por descrição (sem `/`, frase natural) e por invocação
direta, confirmando que carregam sem erro "Unknown skill". Resultado registrado na sessão em
questão, não neste arquivo — promover para cá só se o teste encontrar algo a corrigir.
