# Verificação técnica — "Dividir para não correr risco"

Laudo do agente `verificador-tecnico`, etapa 7. Veredito por item, contra fonte primária
quando disponível. Correções aplicadas diretamente em `04-draft-v1.md`.

## 1. Série de estoque de LCI (pendência bloqueante da etapa 5) — ✅ confirmada, sem correção

A série do draft (R$ 141 bi dez/2020 → R$ 373 bi jan/2024 → R$ 362 bi abr/2024, recuo pós-
Resoluções CMN 5.118/5.119 → R$ 508,8 bi fim de 2025, alta de 29% no ano → R$ 544 bi
jun/2026) **reconcilia e está correta**. A inconsistência apontada em `03-pesquisa.md` §4 (que
citava R$ 350 bi para o fim de 2024) era um erro daquela pesquisa, não do draft: o valor real
de fechamento de 2024, confirmado via fonte B3 (InfoMoney), é **R$ 392,8 bilhões** — o que já
mostra recuperação em curso antes do fim do ano. Adicionado ao draft como ponte entre
"abril de 2024" e "2025" para não deixar implícito que a retomada começou só em 2025 (achado
já sinalizado como observação em `05-critica.md`).

## 2. Faixa de gross-up (LCI 90% CDI ↔ CDB) — ✅ confirmada, `[VERIFICAR]` removido

Recalculada com Python a partir da tabela regressiva de IR vigente (22,5% até 180 dias; 20%
de 181-360; 17,5% de 361-720; 15% acima de 720 dias): 90 ÷ 0,775 ≈ 116,1% e 90 ÷ 0,85 ≈
105,9%. A faixa "106% a 116%" do draft está matematicamente correta. Marcador `[VERIFICAR]`
removido da linha.

## 3. Legislação citada — confirmada, sem correção

Lei nº 10.931/2004, Lei nº 11.033/2004 art. 3º, Lei nº 13.097/2015, Lei nº 9.514/1997,
Resolução BCB nº 471/2025 (SCFI emissoras de LCI desde 1º/7/2025), Resoluções CMN nº
5.118/5.119 (2024) e nº 5.215/2025 — número, ano e conteúdo conferidos, sem divergência.

**Uma precisão**: só a Resolução nº 5.295/2026 cria o conceito de Ativo de Referência; a
Resolução nº 5.296/2026 trata de requisitos de liquidez complementares. O draft atribuía a
criação do conceito ao "pacote" das duas indistintamente — corrigido para atribuir
especificamente à 5.295.

## 4. Ho & Saunders (1981) — confirmada, sem correção

Título, volume (16), número (4), páginas (581-600) e a leitura "banco como dealer avesso a
risco" conferem com o paper original, leitura padrão da literatura sobre margem bancária.

## 5. Vedrossi (2002) — confirmada, sem correção

Dissertação localizável, dados bibliográficos (título, instituição, ano) batem com a citação
do draft.

## 6. Banco Central do Brasil, "Covered Bond: uma opção para o Brasil?" — ❌ corrigida

A atribuição institucional "Banco Central do Brasil" estava errada. O artigo é de **Carneiro,
Júlio César Paranatinga**, publicado em *Conjuntura da Construção* (FGV/IBRE e SindusCon-SP,
set. 2010) — não é publicação do Banco Central. Referência corrigida na lista final.

## 7. Números do caso Banco Master — ❌ corrigida

A liquidação extrajudicial em novembro de 2025 está confirmada. O valor do desembolso do FGC,
porém, estava impreciso: a estimativa oficial (confirmada por Agência Brasil e pela evolução
dos pagamentos até jul/2026) é de **cerca de R$ 40,6 bilhões**, não R$ 44 bilhões. Corrigido
no draft.

## 8. Dados de mercado — composição do estoque de captação bancária — ✅ confirmada

Via B3/Bora Investir (release "cresceu 17% em 2025"): CDB R$ 2,8 tri (57,14% ≈ "cerca de 57%"
✓), LCA R$ 599,9 bi, LF R$ 976,8 bi, LCI R$ 508,8 bi (10,38% ≈ "perto de 10%" ✓). Soma dos
quatro produtos = R$ 4.885,5 bi, arredondado para R$ 4,9 tri como o draft afirma — a fonte
primária confirma o total exatamente. A conta "LCI perto de 10% do total" está certa, e o
draft já sinaliza corretamente que é aproximação própria, não dado publicado diretamente pela
B3.

## 9. Cronograma da Resolução 5.295/5.296 — ✅ confirmada

Fatores de alocação compulsória escalonados de 5% em julho de 2026 até 100% em julho de 2028,
confirmado por múltiplas fontes (LegisWeb, MercGroup). A frase do draft está correta.

## Correções aplicadas ao draft

1. R$ 44 bi → R$ 40,6 bi (desembolso do FGC no caso Master).
2. Distinção entre Resolução 5.295 (cria o Ativo de Referência) e 5.296 (requisitos de
   liquidez), antes atribuídas ao "pacote" sem diferenciação.
3. `[VERIFICAR: faixa recalculada...]` removido — faixa de gross-up 106%-116% confirmada.
4. Adicionado R$ 392,8 bi (fim de 2024) como ponte entre abr/2024 e a retomada de 2025.
5. Referência "Banco Central do Brasil, 'Covered Bond...'" corrigida para a autoria real
   (Carneiro, Júlio César Paranatinga, *Conjuntura da Construção*, FGV/IBRE, 2010).
6. Adicionada referência B3/Bora Investir + Suno para a série de estoque de LCI (a linha do
   corpo já prometia "ver referências", mas a lista não trazia essa fonte).
7. Adicionada nota sobre a Lei nº 14.430/2022 (marco legal das securitizadoras), que
   atualizou parte do regime da Lei nº 9.514/1997 — relevante para a pesquisa do próximo post
   sobre CRI, não muda nada no corpo deste texto.

## Itens que não viraram `[VERIFICAR]`

Nenhum item desta verificação precisou de novo marcador — todos os pontos levantados pela
crítica estrutural (etapa 5) e pela pesquisa (etapa 3) foram confirmados corretos, corrigidos
com valor exato de fonte primária, ou já vinham devidamente ressalvados no próprio draft (caso
do estoque de dez/2020, que segue como aproximação própria explicitamente sinalizada).
