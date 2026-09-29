# Verificação de cálculo — 2026-09-28-o-certificado-nao-muda-o-devedor

Etapa 7 (verificador técnico), 2026-09-27. Texto verificado: `posts/2026-09-28-o-certificado-nao-muda-o-devedor/processo/04-draft-v1.md`. Valores de entrada: os do próprio texto.

## Script (python3)

```python
pi=0.04; ri=0.07
def emp(T,t):
    return (((((1+pi)*(1+ri))**T-1)/(1-t)+1)**(1/T))/(1+pi)-1
def check(T,t,rt):
    iso=((1+pi)*(1+ri))**T
    trib=1+(1-t)*(((1+pi)*(1+rt))**T-1)
    return iso,trib
for T,t in [(1,.175),(2,.15),(5,.15),(10,.15)]:
    r=emp(T,t); print(T,t,"bolso %.4f%%"%(ri/(1-t)*100),"emp %.4f%%"%(r*100), check(T,t,r))
bolso=ri/.85
for T in [x/10 for x in range(50,151)]:
    pass
import math
# find crossing emp(T,.15)==bolso
prev=None
for i in range(20,2000):
    T=i/100; d=emp(T,.15)-bolso
    if prev is not None and prev>0>=d: print("cross T=",T)
    prev=d
for T in [6,7,8,9,10,11,12]: print(T,"%.4f"%(emp(T,.15)*100))
# alternative: aliquota por prazo; 1 ano = 365 dias -> 361-720 -> 17,5%
print("7/0.825",7/0.825, "7/0.85",7/0.85)
# subordination
for L in [.05,.15,.2,.3]:
    S=.2; print(L, min(L,S)/S, max(0,L-S)/(1-S))
f=1.08**3; print("1.08^3",f, 1000*f/1.095**3, 1000*f/1.12**3, 1000*round(f,4)/1.095**3, 1000*round(f,4)/1.12**3)
# du/252 = 3 exactly
print(1000*f/1.07**3/1.01**0)
```

## Saída

```
1 0.175 bolso 8.4848% emp 9.3007% (1.1128, 1.1128)
2 0.15 bolso 8.2353% emp 8.8018% (1.23832384, 1.23832384)
5 0.15 bolso 8.2353% emp 8.5196% (1.7064186339222982, 1.7064186339222989)
10 0.15 bolso 8.2353% emp 8.1795% (2.9118645541972428, 2.9118645541972406)
cross T= 9.04
6 8.4404
7 8.3674
8 8.2999
9 8.2374
10 8.1795
11 8.1257
12 8.0756
7/0.825 8.484848484848484 7/0.85 8.23529411764706
0.05 0.25 0.0
0.15 0.7499999999999999 0.0
0.2 1.0 0.0
0.3 1.0 0.12499999999999997
1.08^3 1.2597120000000002 959.4644964101828 896.6381195335276 959.4553565639663 896.6295781705537
1028.3002310939291
```

## Conferência contra o texto

| Item do texto | Texto | Recálculo | Veredito |
|---|---|---|---|
| Regra de bolso, 15% | IPCA + 8,24% | 7/0,85 = 8,2353% | bate |
| Regra de bolso, 17,5% | IPCA + 8,48% | 7/0,825 = 8,4848% | bate |
| Empate 1 ano (17,5%) | IPCA + 9,30% | 9,3007% | bate |
| Empate 2 anos (15%) | IPCA + 8,80% | 8,8018% | bate |
| Empate 5 anos (15%) | IPCA + 8,52% | 8,5196% | bate |
| Empate 10 anos (15%) | IPCA + 8,18% | 8,1795% | bate |
| Fórmula fechada do empate | — | fator isento = fator tributado líquido nos 4 prazos (a diferença fica na 15ª casa decimal) | bate |
| "por volta de nove anos" | ~9 | cruzamento em T ≈ 9,04 anos | bate |
| Alíquota 1 ano = 365 dias | 17,5% | Lei 11.033, art. 1º, III (361 a 720 dias) | bate |
| Alíquota 2 anos = 730 dias | 15% | art. 1º, IV (acima de 720 dias) | bate |
| Subordinação 5/15/20/30% | 25/75/100/100 e 0/0/0/12,5 | min(L,S)/S e max(0,L−S)/(1−S), S = 20% | bate |
| 1,08³ | ≈ 1,2597 | 1,259712 | bate |
| PU com y = 9,5% | R$ 959,46 | 959,464 (fator exato); 959,455 (com 1,2597) | bate |
| PU com y = 12% | R$ 896,64 | 896,638 (fator exato); **896,630 com 1,2597 arredondado** | bate com o fator exato; quem refizer com o 1,2597 impresso chega a 896,63 |

Nenhuma divergência bloqueante.
