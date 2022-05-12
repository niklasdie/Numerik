import math
from time import time


def newton(a, c, d, x0, y):
    xk = x0
    it = 0
    while 1:
        xkp1 = xk - ((b(a, c, d, xk) - y) / b_abl(a, c, d, xk))
        it += 1
        if xkp1 == xk:
            return xkp1, it
        xk = xkp1


def sekante(a, c, d, xm1, x0, y):
    xk = x0
    xkm1 = xm1
    it = 0
    while 1:
        b_von_xk = b(a, c, d, xk) - y
        xkp1 = xk - (((xk - xkm1) * b_von_xk) / (b_von_xk - (b(a, c, d, xkm1) - y)))
        it += 1
        if xk == xkp1:
            return xkp1, it
        xk = xkp1


def b(a, c, d, x):
    return a / (1 - (c * math.exp(-d * x)))


def b_abl(a, c, d, x):
    return - (a * c * d * math.exp(d * x)) / math.pow((c - math.exp(d * x)), 2)


a = 9.80606
c = -1.1085e25
d = 0.029

if __name__ == '__main__':
    t = time()
    n, it = newton(a, c, d, 1961, 9)
    print(f"newton = {n} mit {it} iterations in {time() - t} seconds")
    t = time()
    sek, it = sekante(a, c, d, 1961, 2000, 9)
    print(f"sekante = {sek} mit {it} iterations in {time() - t} seconds")
    print("Das Newton Verfahren braucht weniger Iterationen und weniger Zeit.")
