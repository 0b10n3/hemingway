# Protocolo de atualização — modo `atualizar`

O guia de voz fossiliza se nunca for revisto contra texto novo. Rode este modo a cada ~5
posts publicados, ou quando o autor trouxer amostras de um gênero ainda não coberto
(ex. o primeiro texto de LinkedIn).

## Passo a passo

1. **Branch dedicada.** `git checkout -b voz/<próxima-versão>` a partir de `main`. A mudança
   de guia é revisada separadamente porque altera o comportamento de toda skill que escreve
   texto — merge só depois da Fase 4 (validação) passar de novo.

2. **Deduplicação por hash.** Compare cada arquivo do caminho informado contra
   `estilo/corpus-manifest.json` (campo `sha256`). Se já processado, pare e avise — não
   reprocessa amostra antiga sem motivo.

3. **Extração pontual.** Dispare `extrator-de-estilo` só para os arquivos novos (não o
   corpus inteiro — isso é o que torna a atualização incremental barata). Salve em
   `estilo/extracoes/proprias/` ou `admiradas/` conforme o caso.

4. **Métricas recalculadas.** Rode `python3 estilo/scripts/metricas.py` de novo — ele
   processa `_arquivo/amostras/proprias/**` inteiro (idempotente, é barato porque é regex
   puro, sem chamada de modelo).

5. **Delta.** Compare o resultado agregado novo contra `estilo/voz.fingerprint.json`
   vigente, eixo por eixo. Para cada traço que mudou de status (surgiu, sumiu, mudou de
   frequência), classifique:

   | Classificação | Critério | O que fazer |
   |---|---|---|
   | Evolução deliberada | ≥3 ocorrências em ≥2 textos, concentrado nos textos mais recentes | Propor como regra nova ou revisão de regra existente |
   | Ruído amostral | Abaixo do limiar, ou plenamente explicável pelo gênero do texto novo | Ignorar, ou no máximo anotar em "Em observação" |
   | Desvio a corrigir | Contraria regra que o autor já confirmou querer manter (§3/§4 do guia) | Sinalizar ao autor como desvio, não como evolução — não promover sozinho |

6. **Proposta, não execução silenciosa.** Adicionar item novo em "Em observação" (§8) pode
   ser automático. **Alterar ou remover regra existente em §3/§4 nunca é automático** —
   apresente a evidência (arquivo + trecho) e espere confirmação, item por item.

7. **Versionamento semântico do guia.**
   - `patch` (1.0.0 → 1.0.1): só itens novos em "Em observação".
   - `minor` (1.0.0 → 1.1.0): regra nova promovida a §3/§4.
   - `major` (1.0.0 → 2.0.0): regra existente revogada ou alterada de forma incompatível.

8. **Registro e fechamento.** Escreva a entrada correspondente em `estilo/CHANGELOG.md`
   (antes/depois, com justificativa), commit, `git tag voz-vX.Y.Z`, e só faça merge de
   `voz/<versão>` para `main` depois de rodar a Fase 4 (validação) de novo — uma mudança de
   guia pode quebrar uma skill que dependia do texto exato de uma regra antiga.

## Sinal para rodar antes do previsto

- O autor colar um texto que soa "certo" mas viola uma regra do guia repetidamente — é sinal
  de que a regra pode estar desatualizada, não de que o texto está errado.
- Um gênero novo aparecer em `_arquivo/amostras/proprias/` (ex. primeiro post de LinkedIn) —
  vale rodar mesmo com menos de 5 posts novos, porque preenche uma lacuna estrutural do
  corpus (ver §8 do guia v1.0.0: "todo traço condicionado a Substack pode na verdade ser
  condicionado a não-LinkedIn — não há como saber ainda").
