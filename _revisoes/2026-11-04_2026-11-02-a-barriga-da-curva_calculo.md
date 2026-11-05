# Verificação de cálculo — 2026-11-02-a-barriga-da-curva

Etapa 7 (verificação técnica, agente `verificador-tecnico`), 2026-11-04. Texto verificado:
`posts/2026-11-02-a-barriga-da-curva/processo/04-draft-v2.md` (corpo). Valores de entrada: os do próprio texto.
Ambiente: python3 3.14.4; `bizdays` 1.0.19 (calendário `ANBIMA.cal`), instalado em diretório isolado do
scratchpad da sessão, fora do repositório. Laudo completo: `posts/2026-11-02-a-barriga-da-curva/processo/07-verificacao.md`.

Chamada: `python3 -I -c "import sys,runpy; sys.path.insert(0,'<scratchpad>/e7/pylib'); runpy.run_path('<scratchpad>/e7/scripts/<script>.py', run_name='__main__')"`

**Resultado:** todos os números do texto conferem. Dois enunciados falham na verificação numérica (bloqueantes no
laudo): (1) "com prazo menor que um ano, a taxa linear vira uma taxa composta maior" é falso quando as réguas diferem
(1.069 de 61.651 pares de datas úteis de 2026, todos com até 39 dias corridos; overnight: 14% linear/360 → 10,29%
exponencial/252); vale com a mesma régua. (2) `DIATRABALHOTOTAL(início;fim;feriados)-1` erra o du sempre que a data
final não é dia útil (1.571 de 5.000 pares aleatórios; LTN 02/01/2026 → 01/01/2027: 248 em vez de 249);
`DIATRABALHOTOTAL(início;fim-1;feriados)` acerta em 5.000 de 5.000.

## Script 1 — `calc.py` (números do texto, busca 91/63, previsão de direção)

```python
import math
from datetime import date, timedelta
from bizdays import Calendar
cal = Calendar.load("ANBIMA")
i = 0.14; C = 1_000_000
print("== Abertura")
lin = C*i*0.5; comp = C*(1.14**(126/252)-1)
print(f"linear {lin:.2f}  composto {comp:.4f}  dif {lin-comp:.4f}")
print("== Contínuo")
print(f"ln(1.14) = {math.log(1.14):.6f}   e^0.14-1 = {math.exp(0.14)-1:.6f}")
print("== Prazo quebrado 1,5 ano")
ml = C*(1.14*1.07-1); me = C*(1.14**1.5-1)
print(f"linear {ml:.4f} exp {me:.4f} dif {ml-me:.4f}  1.14*dif_abertura(exata) {1.14*(lin-comp):.4f}  1.14*2292.17 {1.14*2292.17:.4f}  razao {(ml-me)/(lin-comp):.6f}")
print("== Fatiamento"); print(1.07**2, (1.14**0.5)**2)
print("== Barriga (R$ 1000)")
g = lambda t: 1000*(1+i*t) - 1000*1.14**t
tstar = math.log(i/math.log(1.14))/math.log(1.14)
print(f"t*={tstar:.4f} ano ({tstar*12:.2f} meses)  gap max {g(tstar):.4f}  em 0.5: {1000*(1+i*.5):.2f} x {1000*1.14**.5:.4f} (gap {g(.5):.4f}, {g(.5)/1000/1.0677*100:.3f}% do montante)")
print(f"t=1: {1000*1.14:.2f} / {1000*(1+i):.2f}; t=2: simples {1000*(1+2*i):.2f} composto {1000*1.14**2:.2f}")
print("== Bola de neve 2 anos"); J=1000*(1.14**2-1); print(f"{J:.2f} = {1000*2*i:.2f} + {J-1000*2*i:.2f}")
def virada(r):
    f=lambda t:(1+r)**t-1-2*r*t
    a,b=1.0,100.0
    for _ in range(200):
        m=(a+b)/2
        if f(m)>0: b=m
        else: a=m
    return a
for r in (0.06,0.10,0.12,0.14): print(f"virada {r:.0%}: {virada(r):.3f} anos; share jsj em 10 anos {((1+r)**10-1-r*10)/((1+r)**10-1):.3f}")
print("== Garcia")
a = 1.0166**12; d = a**(1/252)-1
f18 = (1+d)**18-1; f23=(1+d)**23-1; f21=(1+d)**21-1
print(f"1.0166^12={a:.6f}  diaria={d*100:.5f}%  fev18={f18*100:.4f}% jul23={f23*100:.4f}% dif={(f23-f18)*1e4:.2f}pb ({(f23-f18)/((f18+f23)/2)*100:.1f}% da media; {(f23-f18)/f21*100:.1f}% de 21du)  21du={f21*100:.4f}%  over*30={d*30*100:.3f}%")
def wd(y,m):
    n=0; dd=date(y,m,1)
    while dd.month==m:
        n+= dd.weekday()<5; dd+=timedelta(1)
    return n
print("dias de semana fev/98",wd(1998,2),"jul/98",wd(1998,7))
# Pascoa 1998
def easter(y):
    a=y%19;b=y//100;c=y%100;d_=b//4;e=b%4;f=(b+8)//25;g_=(b-f+1)//3;h=(19*a+b-d_-g_+15)%30;i_=c//4;k=c%4;l=(32+2*e+2*i_-h-k)%7;m=(a+11*h+22*l)//451;mo=(h+l-7*m+114)//31;da=((h+l-7*m+114)%31)+1;return date(y,mo,da)
E=easter(1998); print("Pascoa 1998",E,"carnaval",E-timedelta(48),E-timedelta(47))
print("== 365/360"); print(f"{14*365/360:.4f}%")
print("== Conversao 91dc/63du")
F = 1+i*91/360; eq=F**(252/63)-1; mot=(1+i*63/252)**4-1
print(f"F={F:.7f} eq={eq*100:.4f}% motor(63/252)={mot*100:.4f}% motor_pp={(mot-i)*100:.4f} regua_pp={(eq-mot)*100:.4f}")
Llin = i*(91/360)/(63/252)
print(f"ordem inversa: regua primeiro -> linear 252 equiv {Llin*100:.4f}%; regua_pp {(Llin-i)*100:.4f}; motor_pp {(eq-Llin)*100:.4f}")
print("== 12% cap. mensal"); print(f"{(1.01**12-1)*100:.4f}%")
print("== Busca 91 dc com 63 du (ANBIMA, [ini, ini+91) )")
hits=[]
dd=date(2024,1,1)
while dd<date(2028,12,31):
    if cal.isbizday(dd):
        fim=dd+timedelta(91)
        du = cal.bizdays(dd,fim) + (0) # bizdays exclui ini, inclui fim
        # [ini, fim) = bizdays(ini,fim) + isbiz(ini) - isbiz(fim)
        du = cal.bizdays(dd,fim) + 1 - (1 if cal.isbizday(fim) else 0)
        if du==63: hits.append((dd,fim))
    dd+=timedelta(1)
print(len(hits), [ (a.isoformat(),b.isoformat()) for a,b in hits if a.year==2026][:12])
print("== Previsão de direção: 14% linear dc/360 -> exp du/252, prazos < 1 ano, inicio em cada dia útil de 2026")
low=[]; tot=0
dd=date(2026,1,2)
while dd<=date(2026,12,30):
    if cal.isbizday(dd):
        for dc in range(1,365):
            fim=dd+timedelta(dc)
            if not cal.isbizday(fim): continue
            du=cal.bizdays(dd,fim)
            eqr=(1+i*dc/360)**(252/du)-1
            tot+=1
            if eqr<i: low.append((dd,dc,du,eqr))
    dd+=timedelta(1)
print(f"{len(low)} de {tot} pares (ini,fim dia util) dao taxa composta MENOR que 14%; maior dc nesses casos: {max(x[1] for x in low)}")
for x in low[:5]: print(x[0], x[1], x[2], f"{x[3]*100:.2f}%")
print("overnight dc=1 du=1:", f"{((1+i/360)**252-1)*100:.2f}%")
print("mesma regua (t=du/252 nos dois):", all(((1+i*t)**(1/t)-1)>i for t in [k/252 for k in range(1,252)]))
print("== DIATRABALHOTOTAL emulada")
H=set(cal.holidays)
def networkdays(s,e):  # Excel: conta s e e se uteis
    n=0; dd=s
    while dd<=e:
        n+= dd.weekday()<5 and dd not in H; dd+=timedelta(1)
    return n
def du_mkt(s,e): return cal.bizdays(s,e)+ (1 if cal.isbizday(s) else 0) - (1 if cal.isbizday(e) else 0)
import random; random.seed(1)
bad_m1=bad_inner=0; N=5000
for _ in range(N):
    s=date(2026,1,1)+timedelta(random.randint(0,700)); e=s+timedelta(random.randint(1,800))
    if networkdays(s,e)-1!=du_mkt(s,e): bad_m1+=1
    if networkdays(s,e-timedelta(1))!=du_mkt(s,e): bad_inner+=1
print(f"'-1' fora erra em {bad_m1}/{N}; 'fim-1' dentro erra em {bad_inner}/{N}")
s,e=date(2026,1,2),date(2027,1,1)
print("LTN 02/01/2026->01/01/2027: mercado",du_mkt(s,e),"NETWORKDAYS-1",networkdays(s,e)-1,"NETWORKDAYS(fim-1)",networkdays(s,e-timedelta(1)))
assert round(comp,2)==67707.83 and round(ml-me,2)==2613.08
```

Nota: o bloco "DIATRABALHOTOTAL emulada" do script 1 usava `bizdays()` como referência de [início, fim), o que está
errado quando a data inicial não é útil (a função exclui o início e inclui o fim); a contagem foi refeita por força
bruta no script 2, que é o resultado válido.

## Script 2 — `nd.py` (DIATRABALHOTOTAL por força bruta)

```python
from datetime import date, timedelta
from bizdays import Calendar
import random
cal=Calendar.load("ANBIMA"); H=set(cal.holidays)
isb=lambda d: d.weekday()<5 and d not in H
def nd(s,e): return sum(isb(s+timedelta(k)) for k in range((e-s).days+1)) if e>=s else 0
def du(s,e): return sum(isb(s+timedelta(k)) for k in range((e-s).days))   # [s,e)
random.seed(1); N=5000; a=b=c=0; c_fimutil=0; n_fimutil=0
for _ in range(N):
    s=date(2026,1,1)+timedelta(random.randint(0,700)); e=s+timedelta(random.randint(1,800))
    a+= nd(s,e)-1!=du(s,e); b+= nd(s,e-timedelta(1))!=du(s,e); c+= cal.bizdays(s,e)!=du(s,e)
    if isb(e): n_fimutil+=1; c_fimutil+= nd(s,e)-1!=du(s,e)
print(f"'-1' fora erra {a}/{N}; erra quando fim é útil: {c_fimutil}/{n_fimutil}; 'fim-1' dentro erra {b}/{N}; bizdays(s,e)!=[s,e) em {c}/{N}")
# 91/63 por força bruta
hits=[(s,s+timedelta(91)) for s in (date(2026,1,1)+timedelta(k) for k in range(365)) if isb(s) and du(s,s+timedelta(91))==63]
print(len(hits), hits[:3])
print("LTN", du(date(2026,1,2),date(2027,1,1)), nd(date(2026,1,2),date(2027,1,1))-1)
```

## Script 3 — `hits.py` (janelas de 91 dias corridos com 63 dias úteis)

```python
from datetime import date, timedelta
from bizdays import Calendar
cal=Calendar.load("ANBIMA"); H=set(cal.holidays)
isb=lambda d: d.weekday()<5 and d not in H
du=lambda s,e: sum(isb(s+timedelta(k)) for k in range((e-s).days))
for y in (2026,2027):
  hs=[(s,s+timedelta(91),isb(s+timedelta(91))) for s in (date(y,1,1)+timedelta(k) for k in range(365)) if isb(s) and du(s,s+timedelta(91))==63]
  print(y,len(hs),[(a.strftime('%d/%m'),b.strftime('%d/%m/%Y'),u) for a,b,u in hs])
from collections import Counter
print("2026: du de [s,s+91) para s util:",sorted(Counter(du(s,s+timedelta(91)) for s in (date(2026,1,1)+timedelta(k) for k in range(365)) if isb(s)).items()))
```

## Saída (scripts 1, 2 e 3, nesta ordem)

```
== Abertura
linear 70000.00  composto 67707.8252  dif 2292.1748
== Contínuo
ln(1.14) = 0.131028   e^0.14-1 = 0.150274
== Prazo quebrado 1,5 ano
linear 219800.0000 exp 217186.9207 dif 2613.0793  1.14*dif_abertura(exata) 2613.0793  1.14*2292.17 2613.0738  razao 1.140000
== Fatiamento
1.1449 1.14
== Barriga (R$ 1000)
t*=0.5055 ano (6.07 meses)  gap max 2.2924  em 0.5: 1070.00 x 1067.7078 (gap 2.2922, 0.215% do montante)
t=1: 1140.00 / 1140.00; t=2: simples 1280.00 composto 1299.60
== Bola de neve 2 anos
299.60 = 280.00 + 19.60
virada 6%: 22.395 anos; share jsj em 10 anos 0.241
virada 10%: 14.015 anos; share jsj em 10 anos 0.373
virada 12%: 11.920 anos; share jsj em 10 anos 0.430
virada 14%: 10.423 anos; share jsj em 10 anos 0.483
== Garcia
1.0166^12=1.218432  diaria=0.07843%  fev18=1.4212% jul23=1.8195% dif=39.83pb (24.6% da media; 24.0% de 21du)  21du=1.6600%  over*30=2.353%
dias de semana fev/98 20 jul/98 23
Pascoa 1998 1998-04-12 carnaval 1998-02-23 1998-02-24
== 365/360
14.1944%
== Conversao 91dc/63du
F=1.0353889 eq=14.9249% motor(63/252)=14.7523% motor_pp=0.7523 regua_pp=0.1726
ordem inversa: regua primeiro -> linear 252 equiv 14.1556%; regua_pp 0.1556; motor_pp 0.7693
== 12% cap. mensal
12.6825%
== Busca 91 dc com 63 du (ANBIMA, [ini, ini+91) )
229 [('2026-01-02', '2026-04-03'), ('2026-04-22', '2026-07-22'), ('2026-04-23', '2026-07-23'), ('2026-04-24', '2026-07-24'), ('2026-04-27', '2026-07-27'), ('2026-04-28', '2026-07-28'), ('2026-04-29', '2026-07-29'), ('2026-04-30', '2026-07-30'), ('2026-07-14', '2026-10-13'), ('2026-07-15', '2026-10-14'), ('2026-07-16', '2026-10-15'), ('2026-07-17', '2026-10-16')]
== Previsão de direção: 14% linear dc/360 -> exp du/252, prazos < 1 ano, inicio em cada dia útil de 2026
1069 de 61651 pares (ini,fim dia util) dao taxa composta MENOR que 14%; maior dc nesses casos: 39
2026-01-05 1 1 10.29%
2026-01-05 2 2 10.29%
2026-01-05 3 3 10.29%
2026-01-05 4 4 10.29%
2026-01-05 8 6 13.94%
overnight dc=1 du=1: 10.29%
mesma regua (t=du/252 nos dois): True
== DIATRABALHOTOTAL emulada
'-1' fora erra em 2157/5000; 'fim-1' dentro erra em 1600/5000
LTN 02/01/2026->01/01/2027: mercado 249 NETWORKDAYS-1 248 NETWORKDAYS(fim-1) 249
'-1' fora erra 1571/5000; erra quando fim é útil: 0/3429; 'fim-1' dentro erra 0/5000; bizdays(s,e)!=[s,e) em 1571/5000
23 [(datetime.date(2026, 1, 2), datetime.date(2026, 4, 3)), (datetime.date(2026, 4, 22), datetime.date(2026, 7, 22)), (datetime.date(2026, 4, 23), datetime.date(2026, 7, 23))]
LTN 249 248
2026 23 [('02/01', '03/04/2026', False), ('22/04', '22/07/2026', True), ('23/04', '23/07/2026', True), ('24/04', '24/07/2026', True), ('27/04', '27/07/2026', True), ('28/04', '28/07/2026', True), ('29/04', '29/07/2026', True), ('30/04', '30/07/2026', True), ('14/07', '13/10/2026', True), ('15/07', '14/10/2026', True), ('16/07', '15/10/2026', True), ('17/07', '16/10/2026', True), ('20/07', '19/10/2026', True), ('21/07', '20/10/2026', True), ('22/07', '21/10/2026', True), ('23/07', '22/10/2026', True), ('24/07', '23/10/2026', True), ('27/07', '26/10/2026', True), ('28/07', '27/10/2026', True), ('29/07', '28/10/2026', True), ('30/07', '29/10/2026', True), ('31/07', '30/10/2026', True), ('03/08', '02/11/2026', False)]
2027 81 [('10/02', '12/05/2027', True), ('11/02', '13/05/2027', True), ('12/02', '14/05/2027', True), ('15/02', '17/05/2027', True), ('16/02', '18/05/2027', True), ('17/02', '19/05/2027', True), ('18/02', '20/05/2027', True), ('19/02', '21/05/2027', True), ('22/02', '24/05/2027', True), ('23/02', '25/05/2027', True), ('24/02', '26/05/2027', True), ('25/02', '27/05/2027', False), ('29/03', '28/06/2027', True), ('30/03', '29/06/2027', True), ('31/03', '30/06/2027', True), ('01/04', '01/07/2027', True), ('02/04', '02/07/2027', True), ('05/04', '05/07/2027', True), ('06/04', '06/07/2027', True), ('07/04', '07/07/2027', True), ('08/04', '08/07/2027', True), ('09/04', '09/07/2027', True), ('12/04', '12/07/2027', True), ('13/04', '13/07/2027', True), ('14/04', '14/07/2027', True), ('15/04', '15/07/2027', True), ('16/04', '16/07/2027', True), ('19/04', '19/07/2027', True), ('20/04', '20/07/2027', True), ('14/07', '13/10/2027', True), ('15/07', '14/10/2027', True), ('16/07', '15/10/2027', True), ('19/07', '18/10/2027', True), ('20/07', '19/10/2027', True), ('21/07', '20/10/2027', True), ('22/07', '21/10/2027', True), ('23/07', '22/10/2027', True), ('26/07', '25/10/2027', True), ('27/07', '26/10/2027', True), ('28/07', '27/10/2027', True), ('29/07', '28/10/2027', True), ('30/07', '29/10/2027', True), ('02/08', '01/11/2027', True), ('03/08', '02/11/2027', False), ('13/10', '12/01/2028', True), ('14/10', '13/01/2028', True), ('15/10', '14/01/2028', True), ('18/10', '17/01/2028', True), ('19/10', '18/01/2028', True), ('20/10', '19/01/2028', True), ('21/10', '20/01/2028', True), ('22/10', '21/01/2028', True), ('25/10', '24/01/2028', True), ('26/10', '25/01/2028', True), ('27/10', '26/01/2028', True), ('28/10', '27/01/2028', True), ('29/10', '28/01/2028', True), ('01/11', '31/01/2028', True), ('01/12', '01/03/2028', True), ('02/12', '02/03/2028', True), ('03/12', '03/03/2028', True), ('06/12', '06/03/2028', True), ('07/12', '07/03/2028', True), ('08/12', '08/03/2028', True), ('09/12', '09/03/2028', True), ('10/12', '10/03/2028', True), ('13/12', '13/03/2028', True), ('14/12', '14/03/2028', True), ('15/12', '15/03/2028', True), ('16/12', '16/03/2028', True), ('17/12', '17/03/2028', True), ('20/12', '20/03/2028', True), ('21/12', '21/03/2028', True), ('22/12', '22/03/2028', True), ('23/12', '23/03/2028', True), ('24/12', '24/03/2028', True), ('27/12', '27/03/2028', True), ('28/12', '28/03/2028', True), ('29/12', '29/03/2028', True), ('30/12', '30/03/2028', True), ('31/12', '31/03/2028', True)]
2026: du de [s,s+91) para s util: [(60, 22), (61, 86), (62, 68), (63, 23), (64, 48), (65, 2)]
```
