# Cálculo — 2026-10-15-renda-fixa-condicoes-variaveis (etapa 7)

Recálculo das contas do post pelo `verificador-tecnico`, reexecutado pelo orquestrador em 2026-10-15. Vereditos em `posts/2026-10-15-renda-fixa-condicoes-variaveis/processo/07-verificacao.md`. Todas conferem.

```python
# Etapa 7 — recalculo das contas do post 2026-10-15-renda-fixa-condicoes-variaveis
def d(c): return (1+c)**(1/252)-1
def pct_to_spread(p, c): return (1+p*d(c))**252/(1+c)-1
def spread_to_pct(s, c): return (((1+c)*(1+s))**(1/252)-1)/d(c)

texto = {0.15:(0.70,1.41,2.83), 0.1365:(0.64,1.29,2.59), 0.10:(0.48,0.96,1.92), 0.08:(0.39,0.77,1.55)}
print("1) %CDI -> CDI+s")
for c,vals in texto.items():
    calc = [pct_to_spread(p,c)*100 for p in (1.05,1.10,1.20)]
    ok = all(round(x,2)==v for x,v in zip(calc,vals))
    print(f"  CDI {c:.2%}: " + " | ".join(f"{x:.4f}" for x in calc), "texto", vals, "OK" if ok else "DIVERGE")

print("2) CDI+1,5% -> %CDI")
for c in (0.1365, 0.10):
    print(f"  CDI {c:.2%}: {spread_to_pct(0.015,c)*100:.3f}% do CDI")

print("3) Risco prefixado, 3 anos a 110%")
s_mkt = pct_to_spread(1.10, 0.1365)          # spread aditivo exigido, fixado na emissao
s_new = pct_to_spread(1.10, 0.10)            # spread efetivo do papel se CDI esperado = 10%
pu = ((1+s_new)/(1+s_mkt))**3
print(f"  s_mkt={s_mkt:.5%} s_new={s_new:.5%} PU={pu:.4%} perda={1-pu:.3%}")
# checagem pelo fator DI explicito (fluxo projetado a 110% de 10%, descontado a 10% + s_mkt)
fluxo = (1+1.10*d(0.10))**(3*252); desc = ((1+0.10)*(1+s_mkt))**3
print(f"  PU (fluxo explicito) = {fluxo/desc:.4%}")

print("4) PU CDI+1,5% bullet 5 anos, du=1260")
for sm,v in ((0.02,97.6),(0.03,92.9),(0.045,86.4),(0.06,80.5)):
    x = ((1.015)/(1+sm))**(1260/252)*100
    print(f"  CDI+{sm:.1%}: {x:.3f}%  texto {v}  {'OK' if round(x,1)==v else 'DIVERGE'}")

print("5) Duration de spread")
D = 5/1.015
print(f"  modificada = {D:.4f}")
# numerica: derivada no ponto s_mkt=1,5%
h=1e-6; f=lambda s: (1.015/(1+s))**5
print(f"  numerica  = {-(f(0.015+h)-f(0.015-h))/(2*h)/f(0.015):.4f}")
print(f"  1 p.p. -> {(1-f(0.025)):.3%} ; aprox linear {D*0.01:.3%}")

print("6) 0,10 ponto com duration 5")
print(f"  linear 5*0.001 = {5*0.001:.3%}; D_mod 4.93*0.001 = {D*0.001:.3%}; exato (1.015/1.016)^5 = {1-(1.015/1.016)**5:.3%}")

print("7) Lei 14.801")
t=0.34; j=100
liq = j*(1-t); liq2 = liq - 0.30*j*t
print(f"  R$100 -> {liq:.2f} -> {liq2:.2f}; 14% -> {14*(1-t):.2f}% -> {14*liq2/100:.4f}%")
```

Saída:

```
1) %CDI -> CDI+s
  CDI 15.00%: 0.7011 | 1.4070 | 2.8337 texto (0.7, 1.41, 2.83) OK
  CDI 13.65%: 0.6416 | 1.2874 | 2.5913 texto (0.64, 1.29, 2.59) OK
  CDI 10.00%: 0.4776 | 0.9575 | 1.9240 texto (0.48, 0.96, 1.92) OK
  CDI 8.00%: 0.3855 | 0.7724 | 1.5508 texto (0.39, 0.77, 1.55) OK
2) CDI+1,5% -> %CDI
  CDI 13.65%: 111.639% do CDI
  CDI 10.00%: 115.625% do CDI
3) Risco prefixado, 3 anos a 110%
  s_mkt=1.28739% s_new=0.95746% PU=99.0260% perda=0.974%
  PU (fluxo explicito) = 99.0260%
4) PU CDI+1,5% bullet 5 anos, du=1260
  CDI+2.0%: 97.573%  texto 97.6  OK
  CDI+3.0%: 92.927%  texto 92.9  OK
  CDI+4.5%: 86.447%  texto 86.4  OK
  CDI+6.0%: 80.501%  texto 80.5  OK
5) Duration de spread
  modificada = 4.9261
  numerica  = 4.9261
  1 p.p. -> 4.784% ; aprox linear 4.926%
6) 0,10 ponto com duration 5
  linear 5*0.001 = 0.500%; D_mod 4.93*0.001 = 0.493%; exato (1.015/1.016)^5 = 0.491%
7) Lei 14.801
  R$100 -> 66.00 -> 55.80; 14% -> 9.24% -> 7.8120%
```
