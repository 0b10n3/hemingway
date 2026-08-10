---
name: forja-de-voz
description: Constrói, atualiza e audita o guia de voz autoral (estilo/estilo-autoral.md) a partir do corpus em _arquivo/amostras/. Use quando o autor pedir para "atualizar minha voz", "auditar este texto contra meu estilo", "comparar versões do guia", ou quando novas amostras forem adicionadas ao arquivo.
disable-model-invocation: true
argument-hint: [bootstrap|atualizar|auditar|diff] [caminho ou tag]
allowed-tools: Read Write Edit Glob Grep Bash(python3 *) Bash(git add *) Bash(git commit *) Bash(git checkout -b *) Bash(git tag *) Bash(git diff *) Bash(git log *)
---

Skill de tarefa — só roda quando invocada explicitamente via `/forja-de-voz <modo> [alvo]`.
Nunca dispare sozinha: mudar o guia de voz afeta toda skill que escreve texto no repositório
(ver `CLAUDE.md` §"Nada de sobrescrita silenciosa").

## Modo `bootstrap`

Constrói o guia do zero. **Recusa-se a rodar se `estilo/voz.fingerprint.json` já existir**,
salvo confirmação explícita do autor de que é para sobrescrever. Se confirmado:

1. Rode `estilo/scripts/metricas.py` sobre `_arquivo/amostras/proprias/**` → `estilo/metricas.json`.
2. Para cada arquivo em `_arquivo/amostras/proprias/**` e `_arquivo/amostras/admiradas/**`,
   dispare o subagente `extrator-de-estilo` (um por arquivo, no máximo 4 em paralelo) — ver
   `references/taxonomia-estilometrica.md` para o esquema de saída esperado. Salve cada
   retorno em `estilo/extracoes/proprias/<slug>.json` ou `estilo/extracoes/admiradas/<slug>.json`.
3. Agregue por eixo, aplicando o limiar de evidência (≥2 ocorrências, ≥2 arquivos distintos
   para virar regra; ver `references/taxonomia-estilometrica.md`).
4. Mescle a camada aspiracional conforme o protocolo do Apêndice C do meta-prompt original
   (regra forte se presente em ambos; regra preservada se só minha; movimento aspiracional
   com gatilho se só do admirado e compatível; descartado com explicação se incompatível).
5. Emita `estilo/estilo-autoral.md`, `estilo/voz.fingerprint.json`,
   `estilo/corpus-manifest.json` (hash SHA-256 + palavras + gênero de cada amostra própria;
   amostras admiradas sem hash, ver nota de copyright no manifesto), `estilo/CHANGELOG.md`
   começando em v1.0.0.
6. Faça o teste cego do §7.7: dois posts do autor, pergunte se um redator só com o guia
   produziria algo reconhecível. Aponte os três pontos mais frágeis.
7. **Mostre o guia ao autor e espere aprovação antes de commitar.** Só depois do "ok":
   commit `feat(voz): guia de estilo autoral v1.0.0`, tag `voz-v1.0.0`, push com `--tags`.

## Modo `atualizar <caminho-da-nova-amostra>`

O modo que mantém o guia vivo — rode a cada ~5 posts novos publicados. Ver protocolo
completo em `references/protocolo-de-atualizacao.md`. Resumo:

1. Abra a branch `voz/<próxima-versão>`.
2. Compare o arquivo novo contra `estilo/corpus-manifest.json` por hash — se já processado,
   pare e avise.
3. Dispare `extrator-de-estilo` só para o(s) arquivo(s) novo(s).
4. Recalcule `estilo/metricas.json` sobre o corpus ampliado.
5. Gere o delta contra `estilo/voz.fingerprint.json` vigente.
6. Classifique cada divergência: **evolução deliberada** (≥3 ocorrências em ≥2 textos, e nos
   mais recentes), **ruído amostral** (abaixo do limiar ou explicável por gênero), **desvio a
   corrigir** (contraria regra que o autor confirmou querer manter).
7. Proponha as edições uma a uma, com evidência. Adicionar item em "Em observação" (§8 do
   guia) pode ser automático; alterar ou remover regra existente (§3-§4), nunca — sempre
   pergunte.
8. Incremente a versão (patch = observação nova; minor = regra nova; major = regra
   revogada), escreva o delta no `CHANGELOG.md`, commite, tag `voz-vX.Y.Z`.

## Modo `auditar <arquivo>`

Pontua um texto contra o checklist §9 de `estilo/estilo-autoral.md` e contra
`estilo/voz.fingerprint.json`. Devolve relatório de desvio por eixo, com trechos marcados, e
**propõe correções sem aplicá-las** — quem decide se aplica é quem invocou a skill.

## Modo `diff [tagA] [tagB]`

`git diff tagA tagB -- estilo/estilo-autoral.md estilo/voz.fingerprint.json` e explique o que
mudou e por quê, cruzando com as entradas correspondentes do `CHANGELOG.md`.

## Referências

- `references/taxonomia-estilometrica.md` — os nove eixos e o esquema JSON completo que o
  subagente `extrator-de-estilo` devolve. Leia antes de disparar qualquer extração.
- `references/protocolo-de-atualizacao.md` — o passo a passo detalhado do modo `atualizar`,
  incluindo como classificar evolução vs. ruído vs. desvio.
- `estilo/scripts/metricas.py` — script da camada quantitativa (Python puro, stdlib). Roda
  com `python3 estilo/scripts/metricas.py` a partir da raiz do repo.
