import math

def plays(t2i, t3i, t1i, pp):
    return round((t2i + t3i + (0.44 * t1i) + pp), 2)

def ppp(puntos, plays_val):
    return round(puntos / plays_val, 2) if plays_val != 0 else 0

def efg(tcc, t3c, tci):
    return round((tcc + (t3c * 0.5)) / tci, 3) if tci != 0 else 0

def playsP(total, plays_val):
    return round(plays_val / total, 3) if plays_val != 0 else 0

def usg(tci, pp, t1i, totales, min):
    numerador = (tci + pp + 0.44 * t1i) * 200
    denominador = ((tci - totales + pp - totales + 0.44 * (t1i - totales)) * 5 * min)
    return round(numerador / denominador, 3) if min != 0 and denominador != 0 else 0

def ts(tci, t1i, puntos):
    denom = (tci + (0.44 * t1i))
    return round(puntos / (2 * denom), 3) if denom != 0 else 0

def to(pp, plays_val):
    return round(pp / plays_val, 3) if plays_val != 0 else 0

def rtl(t1i, plays_val):
    return round(t1i / plays_val, 3) if plays_val != 0 else 0

def ppt1(t1i, t1c):
    return round(t1c / t1i, 2) if t1i != 0 else 0

def ppt2(t2i, t2c):
    return round((t2c * 2) / t2i, 2) if t2i != 0 else 0

def ppt3(t3i, t3c):
    return round((t3c * 3) / t3i, 2) if t3i != 0 else 0

def pppt3(plays_val, ppp_val, t3c):
    return round(((t3c * 3) / plays_val) / ppp_val, 3) if plays_val != 0 and ppp_val != 0 else 0

def pppt2(plays_val, ppp_val, t2c):
    return round(((t2c * 2) / plays_val) / ppp_val, 3) if plays_val != 0 and ppp_val != 0 else 0

def pppt1(plays_val, ppp_val, t1c):
    return round(((t1c * 1) / plays_val) / ppp_val, 3) if plays_val != 0 and ppp_val != 0 else 0

def f1t1p(t1i, plays_val):
    return round((t1i * 0.44) / plays_val, 3) if plays_val != 0 else 0

def f2t2p(t2i, plays_val):
    return round(t2i / plays_val, 3) if plays_val != 0 else 0

def f3t3p(t3i, plays_val):
    return round(t3i / plays_val, 3) if plays_val != 0 else 0

def f4ppp(pp, plays_val):
    return round(pp / plays_val, 3) if plays_val != 0 else 0

def posesionesA(tcc, t1p, t1i):
    return round(tcc + ((1 - math.pow(1 - t1p, 2)) * 0.44 * t1i), 2)

def posesionesA2(tcc, t1p, t1i):
    return round(tcc + ((1 - math.pow(1 - t1p / 100, 2)) * 0.44 * t1i), 2) if tcc != 0 else 0

def posesionesAporc(plays_val, posesiones):
    return round(posesiones / plays_val, 3) if plays_val != 0 else 0

def oe(tci, ro, asis, pp, tcc):
    denom = (tci - ro + asis + pp)
    return round((tcc + asis) / denom, 2) if denom != 0 else 0

def eps(puntos, oe_val):
    return round(puntos * oe_val, 2)