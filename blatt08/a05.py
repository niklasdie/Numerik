import math


def newton(a, c, d, x0, y):
    xk = x0
    it = 0
    while 1:
        xkp1 = xk - ((b(a, c, d, xk) - y) / b_abl(a, c, d, xk))
        it += 1
        if xkp1 == xk:
            return xkp1, it
        xk = xkp1


def f(x,y):
    x_res = math.sin(x) - y
    y_res = math.exp(-y) - x
    return x_res, y_res


if __name__ == '__main__':
