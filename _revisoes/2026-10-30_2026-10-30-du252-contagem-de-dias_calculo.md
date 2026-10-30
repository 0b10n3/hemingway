# Verificação de cálculo — 2026-10-30-du252-contagem-de-dias

Etapa 7 (verificação técnica, agente `verificador-tecnico`), 2026-10-30. Texto verificado:
`posts/2026-10-30-du252-contagem-de-dias/processo/04-draft-v2.md`. Valores de entrada: os do próprio texto.
Ambiente: python3 3.14.4, numpy 2.5.2, pandas 3.0.5, `bizdays` 1.0.19 (instalado em diretório isolado do
scratchpad da sessão, fora do repositório). Laudo completo: `posts/2026-10-30-du252-contagem-de-dias/processo/07-verificacao.md`.

Chamada:

```
python3 -I -c "import sys,runpy; sys.path.insert(0,'<scratchpad>/pylib'); sys.path.append('~/.local/lib/python3.14/site-packages'); runpy.run_path('<scratchpad>/scripts/verificacao.py', run_name='__main__')"
```

Dado externo usado na seção 10: `PrecoTaxaTesouroDireto.csv` (Tesouro Transparente), baixado em 30/10/2026.

**Resultado:** todas as contas e saídas de código do texto conferem, exceto uma: na tabela do CDB, a diferença da linha
DC/360 linear é **R$ 218,18** (102.033,33 − 101.815,15), não R$ 218,19 (bloqueante O-1, corrigido na etapa 9).

## Blocos de código do texto

Blocos 1, 4 e 5 como no texto (o 1 com `print`); 2 e 3 com `print`, porque o texto os mostra como REPL.

```python
# b1.py
import numpy as np

print(np.busday_count("2026-10-01", "2026-12-01"))
# 43 — contou 12/10, 02/11 e 20/11 como dias úteis
```

```python
# b2.py
from bizdays import Calendar

cal = Calendar.load("ANBIMA")

print(cal.bizdays("2026-01-02", "2027-01-01")                 )# 248
print(cal.bizdays("2026-01-02", cal.following("2027-01-01"))  )# 249
```

```python
# b3.py
from bizdays import Calendar
print(repr(Calendar.load("B3").enddate      ))# datetime.date(2026, 12, 31)
print(repr(Calendar.load("ANBIMA").enddate  ))# datetime.date(2099, 12, 25)
```

```python
# b4.py
from bizdays import Calendar

cal = Calendar.load("ANBIMA")

aplicacao  = "2026-10-01"
vencimento = cal.following("2026-12-01")  # garante que a ponta final é dia útil

du = cal.bizdays(aplicacao, vencimento)   # conta (aplicação, vencimento]: com as duas pontas em dia útil, dá o du da convenção
fator = (1 + 0.12) ** (du / 252)

print(du, round(100_000 * fator, 2))
# 40 101815.15
```

```python
# b5.py
import pandas as pd
from pandas.tseries.offsets import CustomBusinessDay

# Feriados bancários nacionais de 2026 (Resolução CMN 4.880/2020 + Lei 14.759/2023)
feriados_2026 = [
    "2026-01-01", "2026-02-16", "2026-02-17", "2026-04-03",
    "2026-04-21", "2026-05-01", "2026-06-04", "2026-09-07",
    "2026-10-12", "2026-11-02", "2026-11-15", "2026-11-20",
    "2026-12-25",
]

dia_util_br = CustomBusinessDay(holidays=feriados_2026)
dias = pd.date_range("2026-10-01", "2026-12-01", freq=dia_util_br, inclusive="left")

print(len(dias))
# 40
```

## Script de verificação

```python
# Etapa 7 — verificacao numerica, post 2026-10-30-du252-contagem-de-dias
# python3 3.14.4 | numpy 2.5.2 | pandas 3.0.5 | bizdays 1.0.19
import datetime as dt, math, csv, runpy
from decimal import Decimal as D, getcontext
import numpy as np, pandas as pd
from bizdays import Calendar
getcontext().prec = 40
def pw(x, e): return (x.ln() * e).exp()          # x**e em Decimal
SCR = "<scratchpad>"

print("=== 1. Os cinco blocos de codigo do texto, como estao (blocos 2 e 3 com print, pois o texto os mostra como REPL)")
for b in ("b1", "b2", "b3", "b4", "b5"):
    print(f"--- {b}"); runpy.run_path(f"{SCR}/scripts/{b}.py", run_name="__main__")
print("repr no REPL do bloco 1:", repr(np.busday_count("2026-10-01", "2026-12-01")))
anb, b3 = Calendar.load("ANBIMA"), Calendar.load("B3"); hol = list(anb.holidays)
print("tipo de cal.bizdays:", type(anb.bizdays("2026-01-02", "2027-01-01")).__name__)

print("\n=== 2. pandas.bdate_range sem e com feriados")
fer = ["2026-01-01","2026-02-16","2026-02-17","2026-04-03","2026-04-21","2026-05-01","2026-06-04",
       "2026-09-07","2026-10-12","2026-11-02","2026-11-15","2026-11-20","2026-12-25"]
print("sem holidays, inclusive='left':", len(pd.bdate_range("2026-10-01", "2026-12-01", inclusive="left")))
try: pd.bdate_range("2026-10-01", "2026-12-01", holidays=fer, inclusive="left")
except ValueError as e: print("com holidays e freq padrao 'B': ValueError:", e)
print("com holidays e freq='C':", len(pd.bdate_range("2026-10-01", "2026-12-01", freq="C", holidays=fer, inclusive="left")))
print("numpy.busday_count com holidays:", np.busday_count("2026-10-01", "2026-12-01", holidays=fer))
print("lista feriados_2026 do texto == ANBIMA.cal 2026:", sorted(fer) == sorted(str(d) for d in hol if d.year == 2026))

print("\n=== 3. bizdays: pontas, following, validade")
print("bizdays('2013-01-02','2013-01-05') =", anb.bizdays("2013-01-02", "2013-01-05"), "(05/01/2013 = sabado: (ini,fim] -> 2; [ini,fim) -> 3)")
print("following('2027-01-01') =", anb.following("2027-01-01"))
try: b3.bizdays("2026-12-01", "2027-01-05")
except Exception as e: print("B3 depois de 2026-12-31:", type(e).__name__, "-", e)
print("convencao [liq, venc): [02/01/2026, 01/01/2027) =", int(np.busday_count("2026-01-02", "2027-01-01", holidays=hol)),
      "| [02/01/2026, 04/01/2027) =", int(np.busday_count("2026-01-02", "2027-01-04", holidays=hol)))
for d in ["2026-01-02","2026-10-01","2026-10-12","2026-11-02","2026-11-15","2026-11-19","2026-11-20","2026-12-01","2026-12-24","2026-12-31","2027-01-01","2027-01-04"]:
    print(d, dt.date.fromisoformat(d).strftime("%A"), end=" | ")
print("\ndias corridos 01/10 -> 01/12/2026:", (dt.date(2026,12,1) - dt.date(2026,10,1)).days)
sextas = [dt.date(2026,11,d) for d in range(1,31) if dt.date(2026,11,d).weekday() == 4]; print("terceira sexta de nov/2026:", sextas[2])

print("\n=== 4. LTN e rendimento por numero de DU")
for du in (248, 249, 250, 251, 252, 253, 254):
    print(du, "DU -> 1,12^(du/252) - 1 =", f"{(pw(D('1.12'), D(du)/252) - 1) * 100:.4f}%")

print("\n=== 5. Tabela do CDB (R$ 100.000, 12%, 01/10 -> 01/12/2026, 40 DU, 61 DC)")
V = D(100000)
rows = [("DU/252 composto", pw(D("1.12"), D(40)/252)), ("DC/365 composto", pw(D("1.12"), D(61)/365)),
        ("DC/360 composto", pw(D("1.12"), D(61)/360)), ("DC/360 linear  ", 1 + D("0.12") * D(61)/360)]
F0 = rows[0][1]; R0 = (V * F0).quantize(D("0.01"))
for n, f in rows:
    R = (V * f).quantize(D("0.01"))
    print(f"{n}: fator(8) {f.quantize(D('0.00000001'))} | resgate {R} | dif. entre resgates arredondados {R - R0} | dif. exata {V*f - V*F0:.4f}")
print("juros do contratado:", R0 - V)

print("\n=== 6. Taxas equivalentes (mesmo fator do contratado)")
print("DC/365 composto:", f"{(pw(F0, D(365)/61) - 1) * 100:.4f}%")
print("DC/360 composto:", f"{(pw(F0, D(360)/61) - 1) * 100:.4f}%")
print("DC/360 linear  :", f"{(F0 - 1) * D(360)/61 * 100:.4f}%")

print("\n=== 7. Armadilha 1 (43 DU) e escala R$ 100 mi")
R43 = (V * pw(D("1.12"), D(43)/252)).quantize(D("0.01")); print("resgate com 43 DU:", R43, "| acima do contratado:", R43 - R0)
for n, f in rows[1:]: print(f"R$ 100 mi, {n}: {(V*f - V*F0) * 1000:,.2f}")

print("\n=== 8. Dezembro de 2026")
print("ANBIMA:", int(np.busday_count("2026-12-01", "2027-01-01", holidays=hol)), "DU | B3:", int(np.busday_count("2026-12-01", "2027-01-01", holidays=list(b3.holidays))), "pregoes")
print("2 DU a 12% sobre R$ 100 mil:", f"{V * (pw(D('1.12'), D(2)/252) - 1):.4f}", "| sobre R$ 100 mi:", f"{V * 1000 * (pw(D('1.12'), D(2)/252) - 1):,.2f}")

print("\n=== 9. Serie 2001-2030 (ANBIMA.cal, [1/jan, 1/jan seguinte))")
du = {y: int(np.busday_count(f"{y}-01-01", f"{y+1}-01-01", holidays=hol)) for y in range(2001, 2031)}
print(du)
print("anos com 252:", [y for y, v in du.items() if v == 252], "| abaixo:", sum(v < 252 for v in du.values()), "| acima:", sum(v > 252 for v in du.values()), "| faixa:", min(du.values()), "-", max(du.values()))
m = D(sum(du.values())) / 30; print("media:", m)
print("1,12^(251/252) - 1 =", f"{(pw(D('1.12'), D(251)/252) - 1) * 100:.4f}%")
print("media geometrica dos 30 rendimentos anuais:", f"{(pw(pw(D('1.12'), D(sum(du.values()))/252), D(1)/30) - 1) * 100:.4f}%")
print("media aritmetica dos 30 rendimentos anuais:", f"{sum(pw(D('1.12'), D(v)/252) - 1 for v in du.values()) / 30 * 100:.4f}%")
fut = {y: int(np.busday_count(f"{y}-01-01", f"{y+1}-01-01", holidays=hol)) for y in range(2024, 2099)}
print("regime com 20/11, 2024-2098: anos com 252 =", sum(v == 252 for v in fut.values()), "de", len(fut), "| media", round(sum(fut.values())/len(fut), 2))

print("\n=== 10. Tesouro Direto, LTN 01/01/2027 (PrecoTaxaTesouroDireto.csv, Tesouro Transparente, baixado em 30/10/2026)")
for r in csv.reader(open(f"{SCR}/dl/td/td.csv", encoding="latin-1"), delimiter=";"):
    if r[0] == "Tesouro Prefixado" and r[1] == "01/01/2027" and r[2] in ("02/01/2026", "01/10/2026"):
        txc, txv = float(r[3].replace(",", ".")), float(r[4].replace(",", ".")); puc, pub = float(r[5].replace(",", ".")), float(r[7].replace(",", "."))
        base = "-".join(reversed(r[2].split("/"))); n0 = int(np.busday_count(base, "2027-01-01", holidays=hol))
        print(f"{r[2]}: taxa compra {txc}% PU compra (D+1) {puc} -> du implicito {252*math.log(1000/puc)/math.log(1+txc/100):.2f} | "
              f"taxa venda {txv}% PU base (D0) {pub} -> du implicito {252*math.log(1000/pub)/math.log(1+txv/100):.2f} | du [base, venc) = {n0}")
print("LTN 12% liquidada em D+1 (05/01/2026):", int(np.busday_count("2026-01-05", "2027-01-01", holidays=hol)), "DU ->", f"{(1.12**(248/252)-1)*100:.2f}%")
```

## Saída

```
=== 1. Os cinco blocos de codigo do texto, como estao (blocos 2 e 3 com print, pois o texto os mostra como REPL)
--- b1
43
--- b2
248
249
--- b3
datetime.date(2026, 12, 31)
datetime.date(2099, 12, 25)
--- b4
40 101815.15
--- b5
40
repr no REPL do bloco 1: np.int64(43)
tipo de cal.bizdays: int

=== 2. pandas.bdate_range sem e com feriados
sem holidays, inclusive='left': 43
com holidays e freq padrao 'B': ValueError: a custom frequency string is required when holidays or weekmask are passed, got frequency B
com holidays e freq='C': 40
numpy.busday_count com holidays: 40
lista feriados_2026 do texto == ANBIMA.cal 2026: True

=== 3. bizdays: pontas, following, validade
bizdays('2013-01-02','2013-01-05') = 2 (05/01/2013 = sabado: (ini,fim] -> 2; [ini,fim) -> 3)
following('2027-01-01') = 2027-01-04
B3 depois de 2026-12-31: DateOutOfRange - Given date out of calendar range
convencao [liq, venc): [02/01/2026, 01/01/2027) = 249 | [02/01/2026, 04/01/2027) = 249
2026-01-02 Friday | 2026-10-01 Thursday | 2026-10-12 Monday | 2026-11-02 Monday | 2026-11-15 Sunday | 2026-11-19 Thursday | 2026-11-20 Friday | 2026-12-01 Tuesday | 2026-12-24 Thursday | 2026-12-31 Thursday | 2027-01-01 Friday | 2027-01-04 Monday | 
dias corridos 01/10 -> 01/12/2026: 61
terceira sexta de nov/2026: 2026-11-20

=== 4. LTN e rendimento por numero de DU
248 DU -> 1,12^(du/252) - 1 = 11.7987%
249 DU -> 1,12^(du/252) - 1 = 11.8490%
250 DU -> 1,12^(du/252) - 1 = 11.8993%
251 DU -> 1,12^(du/252) - 1 = 11.9496%
252 DU -> 1,12^(du/252) - 1 = 12.0000%
253 DU -> 1,12^(du/252) - 1 = 12.0504%
254 DU -> 1,12^(du/252) - 1 = 12.1008%

=== 5. Tabela do CDB (R$ 100.000, 12%, 01/10 -> 01/12/2026, 40 DU, 61 DC)
DU/252 composto: fator(8) 1.01815145 | resgate 101815.15 | dif. entre resgates arredondados 0.00 | dif. exata 0.0000
DC/365 composto: fator(8) 1.01912036 | resgate 101912.04 | dif. entre resgates arredondados 96.89 | dif. exata 96.8908
DC/360 composto: fator(8) 1.01938848 | resgate 101938.85 | dif. entre resgates arredondados 123.70 | dif. exata 123.7027
DC/360 linear  : fator(8) 1.02033333 | resgate 102033.33 | dif. entre resgates arredondados 218.18 | dif. exata 218.1882
juros do contratado: 1815.15

=== 6. Taxas equivalentes (mesmo fator do contratado)
DC/365 composto: 11.3644%
DC/360 composto: 11.2003%
DC/360 linear  : 10.7123%

=== 7. Armadilha 1 (43 DU) e escala R$ 100 mi
resgate com 43 DU: 101952.60 | acima do contratado: 137.45
R$ 100 mi, DC/365 composto: 96,890.83
R$ 100 mi, DC/360 composto: 123,702.69
R$ 100 mi, DC/360 linear  : 218,188.23

=== 8. Dezembro de 2026
ANBIMA: 22 DU | B3: 20 pregoes
2 DU a 12% sobre R$ 100 mil: 89.9839 | sobre R$ 100 mi: 89,983.86

=== 9. Serie 2001-2030 (ANBIMA.cal, [1/jan, 1/jan seguinte))
{2001: 250, 2002: 253, 2003: 253, 2004: 252, 2005: 251, 2006: 249, 2007: 250, 2008: 254, 2009: 250, 2010: 251, 2011: 251, 2012: 251, 2013: 253, 2014: 253, 2015: 250, 2016: 251, 2017: 249, 2018: 250, 2019: 253, 2020: 251, 2021: 251, 2022: 251, 2023: 249, 2024: 253, 2025: 252, 2026: 249, 2027: 251, 2028: 248, 2029: 249, 2030: 252}
anos com 252: [2004, 2025, 2030] | abaixo: 20 | acima: 7 | faixa: 248 - 254
media: 251
1,12^(251/252) - 1 = 11.9496%
media geometrica dos 30 rendimentos anuais: 11.9496%
media aritmetica dos 30 rendimentos anuais: 11.9497%
regime com 20/11, 2024-2098: anos com 252 = 20 de 75 | media 250.55

=== 10. Tesouro Direto, LTN 01/01/2027 (PrecoTaxaTesouroDireto.csv, Tesouro Transparente, baixado em 30/10/2026)
01/10/2026: taxa compra 13.33% PU compra (D+1) 970.16 -> du implicito 61.01 | taxa venda 13.45% PU base (D0) 969.42 -> du implicito 62.02 | du [base, venc) = 62
02/01/2026: taxa compra 13.65% PU compra (D+1) 881.68 -> du implicito 248.01 | taxa venda 13.77% PU base (D0) 880.31 -> du implicito 249.02 | du [base, venc) = 249
LTN 12% liquidada em D+1 (05/01/2026): 248 DU -> 11.80%
```

Leitura da seção 10: os PUs oficiais implicam du = [liquidação, vencimento), com liquidação em D+1 para a compra e em D0
para o PU base; a fração de 0,01 a 0,02 vem do truncamento ANBIMA/Tesouro. Numa varredura das 207 datas de 2026, o du
implícito do PU de compra é sempre du − 1.
