import math
import numpy as np


def newton(x0, y0):
    xk = [x0, y0]
    it = 0
    while 1:
        xkp1 = xk - (np.linalg.inv(J(xk[0], xk[1])).dot(f(xk[0], xk[1])))
        it += 1
        if xkp1[0] == xk[0] and xkp1[1] == xk[1]:
            print(f"xkp1 = {xkp1} = {xk} = xk ?")
            return xkp1, it
        xk = xkp1


def f(x, y):
    x_res = math.sin(x) - y
    y_res = math.exp(-y) - x
    return x_res, y_res


def J(x, y):
    j = [
        [math.cos(x), -1],
        [-1, -math.exp(-y)]
    ]
    return j


if __name__ == '__main__':
    n, it = newton(0, 0)
    print(f"newton = {n} mit {it} iterations")
