import numpy as np


def newton(x0):
    xk = x0
    it = 0
    while 1:
        xkp1 = xk - (f(xk) / f_abl(xk))
        if it != 0:
            e = np.abs(xk - xkm1)
            if e <= 10e-6:
                print(f"e = {e} <= 10e-6")
                return xkp1, it
        it += 1
        xkm1 = xk
        xk = xkp1


def f(x):
    return x + np.log(x) - 2


def f_abl(x):
    return (1 / x) + 1



if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    n, it = newton(1)
    print(f"newton = {n} mit {it} iterations")

