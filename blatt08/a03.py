import math

import numpy as np


def newton(x0):
    xk = x0
    it = 0
    for i in range(4):
        xkp1 = xk - (f(xk) / f_abl(xk))
        it += 1
        xk = xkp1
    return xkp1, it


def newton_mod1(x0):
    xk = x0
    it = 0
    for i in range(4):
        xkp1 = xk - 3 * (f(xk) / f_abl(xk))
        it += 1
        xk = xkp1
    return xkp1, it


def newton_mod2(x0):
    xk = x0
    it = 0
    for i in range(4):
        xkp1 = xk - ((f(xk) * f_abl(xk)) / (math.pow(f_abl(xk), 2) - f(xk) * f_abl_abl(xk)))
        if xkp1 == 0:
            break
        it += 1
        xk = xkp1
    return xkp1, it


def f(x):
    return math.atan(x) - x


def f_abl(x):
    return (1 / ((x * x) + 1)) - 1


def f_abl_abl(x):
    return -((2 * x) / (math.pow(1 + x * x, 2)))


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    n, it = newton(1)
    print(f"newton = {n} mit {it} iterations")
    n, it = newton_mod1(1)
    print(f"newton_mod1 = {n} mit {it} iterations")
    n, it = newton_mod2(1)
    print(f"newton_mod2 = {n} mit {it} iterations")
