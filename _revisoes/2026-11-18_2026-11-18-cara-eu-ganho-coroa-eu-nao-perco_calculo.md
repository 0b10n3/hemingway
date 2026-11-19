# Verificação de cálculo: 2026-11-18-cara-eu-ganho-coroa-eu-nao-perco

Etapa 7 (`verificador-tecnico`), 2026-11-18. Texto verificado: corpo de
`posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco/processo/04-draft-v2.md`. Laudo:
`posts/2026-11-18-cara-eu-ganho-coroa-eu-nao-perco/processo/07-verificacao.md`.
Ambiente: Python 3.14.4, só biblioteca padrão (`decimal` com 50 dígitos, para os truncamentos não
dependerem de ponto flutuante; `datetime`, `calendar`). Script no scratchpad da sessão, fora do
repositório; cópia integral abaixo. Valores de entrada: os do próprio texto.

**Resultado.** Com os valores exatos que o texto usa (C = 1.000 × (1,10^0,5 − 1) sem arredondar),
todos os números do texto conferem: R$ 874,89; R$ 4,89; 48,808848; os três PUs de LTN; os três custos;
943,883948; TIR 14,5328%; dealer 943,680875; R$ 0,20 (0,203073); 94.368.087,53; 94.388.697,41;
20.609,88; R$ 115,18; R$ 302,60; R$ 20.307,28; 2,15 pb. Duas divergências bloqueantes:

1. **Tabela da réplica, recalculada com os números que ela mesma exibe.** A coluna "Quantidade"
   mostra 0,04880885 (C ÷ 1.000 arredondado na 8ª casa), mas os custos foram calculados com
   0,0488088482. Com 0,04880885 × os PUs exibidos, os custos dão 45,713676 / 42,702406 / 855,467870
   e o total 943,883952, contra 45,713675 / 42,702404 / 855,467869 e 943,883948 na tabela. Com 9
   casas (0,048808848) ainda falha a 3ª linha (855,467868). Com 10 casas (0,0488088482) a tabela
   inteira se reproduz.
2. **"exatamente 100.000 vezes os R$ 0,20 de diferença".** 100.000 × 0,20 = 20.000,00. O lucro de
   20.307,28 é 100.000 × 0,2030728 (a diferença sem arredondar). A identidade vale; o número
   escrito, não.

**Cadeia alternativa pela convenção do Tesouro** (fluxo A-5 = 48,80885; expoente T-14; PU da LTN
T-6; PU da NTN-F com VP de cada fluxo A-9 e PU T-6; valor financeiro T-2; regras da Tabela 3 da
*Metodologia de Cálculo* do Tesouro): PUs de LTN 936,585811 / 874,890638 / 815,656609; custos
45,713676 / 42,702406 / 855,467870; réplica 943,883952; TIR 14,5328%; dealer 943,680880; compra
94.368.088,00; vendas 94.388.697,34; líquido 20.609,34; sobra R$ 115,00 por data; VP R$ 302,12;
lucro R$ 20.307,22, contra 100.000 × 0,2030724 = R$ 20.307,24 (os R$ 0,02 são o truncamento dos
valores financeiros das três vendas). A planilha do texto (`SOMARPRODUTO` sem `TRUNCAR`) daria
943,883953 nessa cadeia, e não 943,883952.

**Datas.** 01/01/2029 cai numa segunda-feira (feriado nacional); 02/01/2029 é terça-feira.

**Caso real (crítica, item 10), ANBIMA 11/11/2026, PUs indicativos.** Réplica da NTN-F 2029 com
DF de 01/01/2027 tirado da NTN-F 2027 (último fluxo, 1.048,80885) e LTNs de 01/07/2027, 01/01/2028,
01/07/2028 e 01/01/2029: R$ 959,271765. NTN-F 2029: R$ 960,084932. Diferença: R$ 0,813167 por título
(0,0848% do preço), a NTN-F acima da réplica. Confere com `03-pesquisa.md`, item 34.

## Dados de mercado conferidos nesta etapa (acesso em 2026-11-18)

```
BCB SGS 432 (meta Selic), 01/09 a 18/11/2026: 14,00 até 16/09; 13,75 de 17/09 a 18/11
BCB Copom: 282ª, 2026-11-04, "Copom mantém a taxa Selic em 13,75% a.a."; 281ª, 2026-09-16, reduz para 13,75%
ANBIMA ETTJ prefixada (CZ-down.asp; a consulta só devolve de 10/11 em diante), vértices 126 / 252 / 378 du:
  10/11 13,7826 / 14,0821 / 14,3731
  11/11   (n/d) / 14,0442 / 14,3234   (Svensson 11/11: b1 0,1432 b2 -0,0069 b3 -0,0152 b4 0,0380 l1 1,6621 l2 0,3382)
  12/11 13,7883 / 14,1395 / 14,4730
  13/11 13,7985 / 14,1224 / 14,4288
  16/11 13,9605 / 14,3974 / 14,7502
  17/11 13,8986 / 14,2752 / 14,5920
  faixa 10 a 17/11: 126 du 13,78-13,96; 252 du 14,04-14,40; 378 du 14,32-14,75
BCB Demab, negociações no mercado secundário, arquivo NegT202610.CSV (outubro/2026), vencimento 01/01/2029:
  NTN-F 950199 BRSTNCNTF1Q6 (emissão 05/01/2018): 21 dias, 2.243 operações, 30.105.496 títulos
  NTN-F 950197 BRSTNCNTF1Y0 (emissão 01/10/2019): 19 dias, 135 operações, 349.635 títulos; sem valor par
  NTN-F 950198 BRSTNCNTF1Z7 (emissão 01/10/2019): 13 dias, 41 operações, 12.967 títulos; valor par 1.000,00
  02/10/2026, PU de lastro: LTN 01/01/2029 = 740,74570968; NTN-F 950198 = 740,74570968;
    NTN-F 950197 = 36,15494623 = 48,80885 x 740,74570968 / 1000 (conferido: 36,15494623)
  PU de lastro do 950198 igual ao da LTN 2029 nos 13 dias em que os dois negociaram;
  PU médio negociado do 950198 acima do da LTN em 11 dos 13 dias (de -29,49 a +13,33), com 1 a 10 operações por dia
```

## Script `calc.py`

Chamada: `python3 -I <scratchpad>/e7/scripts/calc.py`

```python
"""Etapa 7: recálculo de todos os números de 'Cara, eu ganho. Coroa, eu não perco.'

Duas cadeias:
  A = a do texto (C = 1000*(1,10^0,5 - 1) sem arredondar; PUs arredondados na 6ª só para exibir)
  T = convenção do Tesouro (fluxo A-5 = 48,80885; expoente T-14; LTN PU T-6;
      NTN-F: VP de cada fluxo A-9, PU T-6; valor financeiro T-2)
Decimal em tudo, para não depender de ponto flutuante nos truncamentos.
"""
from decimal import Decimal as D, getcontext, ROUND_HALF_UP, ROUND_DOWN, ROUND_CEILING
import calendar, datetime

getcontext().prec = 50
def rnd(x, n): return x.quantize(D(1).scaleb(-n), rounding=ROUND_HALF_UP)
def trc(x, n): return x.quantize(D(1).scaleb(-n), rounding=ROUND_DOWN)
def pw(b, e): return (b.ln() * e).exp()          # b^e com Decimal

DU = [D(126), D(252), D(378)]
R = [D("0.14"), D("0.143"), D("0.1455")]
N = D(100000)

print("== Abertura e prova")
print("1000 + trunc2(48,808850) =", D(1000) + trc(D("48.808850"), 2))
ltn1 = D(1000) / D("1.143")
print(f"LTN 1 ano a 14,30%: {ltn1:.10f} -> rnd6 {rnd(ltn1,6)} trc6 {trc(ltn1,6)} ; centavos {rnd(ltn1,2)} ; ganho vs 870 = {rnd(ltn1,2)-D(870)}")

def cadeia(nome, fluxo, conv):
    print(f"\n==== Cadeia {nome}: cupom por título = {fluxo}")
    CF = [fluxo, fluxo, D(1000) + fluxo]
    q = [rnd(c / 1000, 8) for c in CF] if conv else [c / 1000 for c in CF]
    pu = []
    for du, r in zip(DU, R):
        e = trc(du / 252, 14)
        x = D(1000) / pw(1 + r, e)
        pu.append(trc(x, 6) if conv else x)
    custo = [qi * pi for qi, pi in zip(q, pu)]
    for du, r, p, qi, c in zip(DU, R, pu, q, custo):
        print(f"  {du} du  {r*100}%  PU LTN {p:.9f} (rnd6 {rnd(p,6)})  q {qi:.10f}  custo {c:.9f} (rnd6 {rnd(c,6)})")
    pu_rep = sum(custo)
    print(f"  PU réplica = {pu_rep:.9f} (rnd6 {rnd(pu_rep,6)}, trc6 {trc(pu_rep,6)})")
    # mesma réplica pela fórmula de NTN-F do Tesouro com taxa spot por fluxo
    vp = [c / pw(1 + r, trc(du / 252, 14)) for c, du, r in zip(CF, DU, R)]
    alt = trc(sum(rnd(v, 9) for v in vp), 6) if conv else sum(vp)
    print(f"  (fórmula NTN-F com spot por fluxo: {alt:.9f})")

    def pu_ntnf(tir):
        vps = [c / pw(1 + tir, trc(du / 252, 14)) for c, du in zip(CF, DU)]
        return trc(sum(rnd(v, 9) for v in vps), 6) if conv else sum(vps)

    lo, hi = D("0.10"), D("0.20")
    for _ in range(200):
        mid = (lo + hi) / 2
        if pu_ntnf(mid) > pu_rep: lo = mid
        else: hi = mid
    tir = (lo + hi) / 2
    print(f"  TIR da réplica = {tir*100:.6f}% a.a.  (inclinação: abaixo dos 14,55%? {tir < D('0.1455')})")

    pu_d = pu_ntnf(D("0.1455"))
    print(f"  PU dealer a 14,55% flat = {pu_d:.9f} (rnd6 {rnd(pu_d,6)}) ; centavos {rnd(pu_d,2)}")
    dif = pu_rep - pu_d
    print(f"  diferença réplica - dealer = {dif:.9f} por título ; x100.000 = {dif*N:.4f}")

    n = [(c * N / 1000).to_integral_value(rounding=ROUND_CEILING) for c in CF]  # lotes inteiros, para cima
    assert [int(x) for x in n] == [4881, 4881, 104881]
    print(f"  lotes: {[int(x) for x in n]} (exatos {[str(c*N/1000) for c in CF]})")
    vf = (lambda x: trc(x, 2)) if conv else (lambda x: rnd(x, 2))
    compra = vf(N * pu_d)
    vendas = [vf(ni * pi) for ni, pi in zip(n, pu)]
    venda = sum(vendas)
    liq = venda - compra
    print(f"  compra {compra} ; vendas {vendas} = {venda} ; líquido {liq}")
    recebe = [vf(N * c) for c in CF] if conv else [N * c for c in CF]
    sobra = [ni * 1000 - rc for ni, rc in zip(n, recebe)]
    print(f"  deve por data {[str(ni*1000) for ni in n]} ; recebe {[str(x) for x in recebe]} ; sobra {[str(rnd(s,4)) for s in sobra]}")
    vp_sobra = sum(s * p / 1000 for s, p in zip(sobra, pu))
    lucro = liq - rnd(vp_sobra, 2)
    print(f"  VP da sobra = {vp_sobra:.6f} -> {rnd(vp_sobra,2)} ; lucro travado = {lucro} ; 100.000 x dif = {rnd(dif*N,2)}")
    print(f"  escala: lucro/compra = {lucro/compra*10000:.4f} pb ; liq/compra = {liq/compra*10000:.4f} pb")
    # planilha do texto: =SOMARPRODUTO(B2:B4/(1+C2:C4)^(D2:D4/252)), sem truncar
    plan = sum(c / pw(1 + r, du / 252) for c, du, r in zip(CF, DU, R))
    print(f"  planilha SOMARPRODUTO (sem truncar) = {plan:.9f} ; vs PU réplica: {plan - pu_rep:.2e}")
    return dict(pu_rep=pu_rep, pu_d=pu_d, liq=liq, lucro=lucro)

C = D(1000) * (pw(D("1.1"), D("0.5")) - 1)
print(f"\nC = 1000*(1,1^0,5-1) = {C:.12f} ; fator A-8 = {rnd(C/1000,8)} ; A-5 do fluxo = {rnd(C,5)} ; PU de juros T-6 = {trc(rnd(C/1000,8)*1000,6)}")
print(f"C/1000 = {C/1000:.12f}  (quantidade do texto: 0,04880885)")
A = cadeia("A (texto)", C, conv=False)
# cadeia A com as quantidades do texto (0,04880885) e C sem arredondar no fluxo
print("\n== Cadeia A' (o que a tabela do texto mistura: q = 0,04880885 e PUs sem truncar)")
qq = [D("0.04880885"), D("0.04880885"), D("1.04880885")]
pus = [D(1000) / pw(1 + r, du / 252) for du, r in zip(DU, R)]
cs = [a * b for a, b in zip(qq, pus)]
print("  custos", [str(rnd(c, 6)) for c in cs], "total", rnd(sum(cs), 6))
T = cadeia("T (Tesouro)", rnd(C, 5), conv=True)

print("\n== Datas")
for d in (datetime.date(2029, 1, 1), datetime.date(2029, 1, 2)):
    print(d, calendar.day_name[d.weekday()])
print("\n== NTN-B (exercício): fator semestral 1,06^0,5-1 =", rnd(pw(D("1.06"), D("0.5")) - 1, 8))

print("\n== Tabela recalculada com os valores exibidos (PU com 6 casas) e quantidades com 8, 9 e 10 casas")
pu6 = [D("936.585812"), D("874.890639"), D("815.656609")]
for casas in (9, 10):
    qn = [rnd(C / 1000, casas), rnd(C / 1000, casas), rnd(1 + C / 1000, casas)]
    cn = [rnd(a * b, 6) for a, b in zip(qn, pu6)]
    print(f"  {casas} casas: q {[str(x) for x in qn]} custos {[str(c) for c in cn]} soma {sum(cn)} total {rnd(sum(a*b for a,b in zip(qn,pu6)),6)}")
q8 = [D("0.04880885"), D("0.04880885"), D("1.04880885")]
print("  com 8 casas (como está):", [str(rnd(a * b, 6)) for a, b in zip(q8, pu6)], rnd(sum(a * b for a, b in zip(q8, pu6)), 6))
print("  LTN com a fórmula do texto anterior TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6):",
      [str(trc(D(1000) / pw(1 + r, trc(du / 252, 14)), 6)) for du, r in zip(DU, R)])

print("\n== BCB Demab, NegT202610, 02/10/2026: PU de lastro")
lastro = D("740.74570968")
print("  cupom 01/01/2029 implícito = 48,80885 x lastro/1000 =", rnd(D("48.80885") * lastro / 1000, 8), "(arquivo: 36,15494623)")

print("\n== Caso real (crítica, item 10): NTN-F 2029 x réplica em LTN, ANBIMA ms261111.txt, PUs indicativos de 11/11/2026")
cf = D("48.80885")
df27a = D("1030.345873") / (D(1000) + cf)      # NTN-F 2027: só resta o fluxo de 01/01/2027
dfs = [df27a, D("0.922001245"), D("0.86044003"), D("0.804327628"), D("0.748530029")]
rep = cf * sum(dfs[:4]) + (D(1000) + cf) * dfs[4]
ntnf = D("960.084932")
print(f"  DF 01/01/2027 = {df27a:.9f} ; réplica = {rep:.6f} ; NTN-F 2029 = {ntnf} ; dif = {ntnf-rep:.6f} ({(ntnf-rep)/rep*100:.4f}% do preço)")
```

## Saída

```
== Abertura e prova
1000 + trunc2(48,808850) = 1048.80
LTN 1 ano a 14,30%: 874.8906386702 -> rnd6 874.890639 trc6 874.890638 ; centavos 874.89 ; ganho vs 870 = 4.89

C = 1000*(1,1^0,5-1) = 48.808848170152 ; fator A-8 = 0.04880885 ; A-5 do fluxo = 48.80885 ; PU de juros T-6 = 48.808850
C/1000 = 0.048808848170  (quantidade do texto: 0,04880885)

==== Cadeia A (texto): cupom por título = 48.808848170151546991453513679937598475271857681500
  126 du  14.00%  PU LTN 936.585811582 (rnd6 936.585812)  q 0.0488088482  custo 45.713674676 (rnd6 45.713675)
  252 du  14.300%  PU LTN 874.890638670 (rnd6 874.890639)  q 0.0488088482  custo 42.702404348 (rnd6 42.702404)
  378 du  14.5500%  PU LTN 815.656609429 (rnd6 815.656609)  q 1.0488088482  custo 855.467869037 (rnd6 855.467869)
  PU réplica = 943.883948061 (rnd6 943.883948, trc6 943.883948)
  (fórmula NTN-F com spot por fluxo: 943.883948061)
  TIR da réplica = 14.532754% a.a.  (inclinação: abaixo dos 14,55%? True)
  PU dealer a 14,55% flat = 943.680875273 (rnd6 943.680875) ; centavos 943.68
  diferença réplica - dealer = 0.203072788 por título ; x100.000 = 20307.2788
  lotes: [4881, 4881, 104881] (exatos ['4880.88481701515469914535136799375984752718576815', '4880.88481701515469914535136799375984752718576815', '104880.88481701515469914535136799375984752718576815'])
  compra 94368087.53 ; vendas [Decimal('4571475.35'), Decimal('4270341.21'), Decimal('85546880.85')] = 94388697.41 ; líquido 20609.88
  deve por data ['4881000', '4881000', '104881000'] ; recebe [4880884.817..., 4880884.817..., 104880884.817...] ; sobra ['115.1830', '115.1830', '115.1830']
  VP da sobra = 302.601027 -> 302.60 ; lucro travado = 20307.28 ; 100.000 x dif = 20307.28
  escala: lucro/compra = 2.1519 pb ; liq/compra = 2.1840 pb
  planilha SOMARPRODUTO (sem truncar) = 943.883948061 ; vs PU réplica: -1.00e-47

== Cadeia A' (o que a tabela do texto mistura: q = 0,04880885 e PUs sem truncar)
  custos ['45.713676', '42.702406', '855.467871'] total 943.883953

==== Cadeia T (Tesouro): cupom por título = 48.80885
  126 du  14.00%  PU LTN 936.585811000 (rnd6 936.585811)  q 0.0488088500  custo 45.713676361 (rnd6 45.713676)
  252 du  14.300%  PU LTN 874.890638000 (rnd6 874.890638)  q 0.0488088500  custo 42.702405917 (rnd6 42.702406)
  378 du  14.5500%  PU LTN 815.656609000 (rnd6 815.656609)  q 1.0488088500  custo 855.467870080 (rnd6 855.467870)
  PU réplica = 943.883952358 (rnd6 943.883952, trc6 943.883952)
  (fórmula NTN-F com spot por fluxo: 943.883952000)
  TIR da réplica = 14.532754% a.a.  (inclinação: abaixo dos 14,55%? True)
  PU dealer a 14,55% flat = 943.680880000 (rnd6 943.680880) ; centavos 943.68
  diferença réplica - dealer = 0.203072358 por título ; x100.000 = 20307.2358
  lotes: [4881, 4881, 104881] (exatos ['4880.88500', '4880.88500', '104880.88500'])
  compra 94368088.00 ; vendas [Decimal('4571475.34'), Decimal('4270341.20'), Decimal('85546880.80')] = 94388697.34 ; líquido 20609.34
  deve por data ['4881000', '4881000', '104881000'] ; recebe ['4880885.00', '4880885.00', '104880885.00'] ; sobra ['115.0000', '115.0000', '115.0000']
  VP da sobra = 302.120302 -> 302.12 ; lucro travado = 20307.22 ; 100.000 x dif = 20307.24
  escala: lucro/compra = 2.1519 pb ; liq/compra = 2.1839 pb
  planilha SOMARPRODUTO (sem truncar) = 943.883952869 ; vs PU réplica: 5.11e-7

== Datas
2029-01-01 Monday
2029-01-02 Tuesday

== NTN-B (exercício): fator semestral 1,06^0,5-1 = 0.02956301

== Tabela recalculada com os valores exibidos (PU com 6 casas) e quantidades com 8, 9 e 10 casas
  9 casas: q ['0.048808848', '0.048808848', '1.048808848'] custos ['45.713675', '42.702404', '855.467868'] soma 943.883947 total 943.883947
  10 casas: q ['0.0488088482', '0.0488088482', '1.0488088482'] custos ['45.713675', '42.702404', '855.467869'] soma 943.883948 total 943.883948
  com 8 casas (como está): ['45.713676', '42.702406', '855.467870'] 943.883952
  LTN com a fórmula do texto anterior TRUNCAR(1000/(1+i)^TRUNCAR(du/252;14);6): ['936.585811', '874.890638', '815.656609']

== BCB Demab, NegT202610, 02/10/2026: PU de lastro
  cupom 01/01/2029 implícito = 48,80885 x lastro/1000 = 36.15494623 (arquivo: 36,15494623)

== Caso real (crítica, item 10): NTN-F 2029 x réplica em LTN, ANBIMA ms261111.txt, PUs indicativos de 11/11/2026
  DF 01/01/2027 = 0.982396242 ; réplica = 959.271765 ; NTN-F 2029 = 960.084932 ; dif = 0.813167 (0.0848% do preço)
```

(Na linha "recebe" da cadeia A, os 40 dígitos do `Decimal` foram abreviados com reticências; o
resto da saída está como o script imprimiu.)
