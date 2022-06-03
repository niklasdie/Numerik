import numpy as np
import scipy.integrate as integrate


# Aufgabe 1

def f(x):
    return 1 / (1 + x * x)


def a_1(a, b):
    exact = integrate.quad(f, a, b)[0]
    print(f"exact = {exact}\n")
    return exact


def b_1(m, a, b, f):
    l = (b - a) / m
    tmp = 0
    for i in range(0, m + 1):
        if i == 0 or m == i:
            tmp += f(a + i * l)
        else:
            tmp += 2 * f(a + i * l)
    trapez = (l / 2) * tmp
    print(f"trapez = {trapez}")
    return trapez


def c_1(m, a, b):
    m *= 2
    l = (b - a) / m
    temp = 0
    for i in range(0, m):
        k = 1
        if i % 2 != 0 and (i != 0 and 1 != m - 1):
            k = 4
        else:
            k = 2
        temp += k * f(a + i * l)
    simpson = (l / 3) * temp
    print(f"simpson = {simpson}")
    return simpson


def d_1(a, b):
    gauss = (8 / 9) * f(0) + (5 / 9) * f(np.sqrt(3 / 5)) + f(1)
    print(f"gauss = {gauss}")
    return gauss


def umrechnen(a, b, x, beta):
    x = ((b - a) / 2) * x + ((b + a) / 2)
    beta = 0  # TODO


def skalar(f, g, a, b):
    return integrate.quad(f * g, a, b)[0]


# Aufgabe 2

def g(x):
    return np.sin(np.pi * x**2)


def divDif(p):
    i = len(p)
    d = np.zeros(shape=(i, i), dtype=np.float32)
    for n in range(0, i):
        d[n][n] = p[n][1]
    for n in range(0, i):
        for m in range(n - 1, -1, -1):
            d[n][m] = (d[n][m + 1] - d[n - 1][m]) / (p[n][0] - p[m][0])
    return d


def a_2(a, b, f, ordnung):
    T = np.zeros(shape=(len(ordnung)), dtype=np.float32)
    l = np.zeros(shape=(len(ordnung)), dtype=np.float32)
    for m in range(0, len(ordnung)):
        T[m] = b_1(2 ** m + 1, a, b, f)
        l[m] = 2 ** m
    l = l[::-1]
    p = np.c_[l, T]
    sol = np.diag(divDif(p))
    for i in range(0, len(sol)):
        print(f"Bei Ordnung {ordnung[i]} ist die Näherung {sol[i]}")
    return sol


def b_2(a, b, f, ordnung):
    T = np.zeros(shape=(len(ordnung)), dtype=np.float32)
    l = np.zeros(shape=(len(ordnung)), dtype=np.float32)
    for m in range(0, len(ordnung)):
        T[m] = b_1(2 ** m + 1, a, b, f)
        l[m] = 2 ** m
    l = l[::-1]
    p = np.c_[l, T]
    sol = np.diag(divDif(p))
    for i in range(0, len(sol)):
        print(f"Bei Ordnung {ordnung[i]} ist die Näherung {sol[i]}")
    return sol


if __name__ == '__main__':
    np.set_printoptions(precision=5, suppress=True)
    print("\nAufgabe 1:\n")
    a = 0
    b = 1
    exact = a_1(a, b)
    trapez = b_1(8, a, b, f)
    print(f"abs. Fehler summierte Trapez-Regel: {np.abs(exact - trapez)}\n")
    simpson = c_1(4, a, b)
    print(f"abs. Fehler summierte Simpson-Regel: {np.abs(exact - simpson)}\n")
    # gauss = d_1()
    # print(f"abs. Fehler Gauß-Verfahren: {np.abs(exact - gauss)}\n")

    print("\nAufgabe 2:\n")
    a = -1
    ordnung = [2, 4, 6, 8, 10, 12, 14, 16]
    print("a)")
    sol = a_2(a, b, g, ordnung)
    exact = integrate.quad(g, a, b)[0]
    print(f"abs. Fehler Romberg: {np.abs(exact - sol[len(sol)-1])}\n")

    print("\nb)")
    sol = b_2(a, b, g, ordnung)
    print(f"abs. Fehler Romberg: {np.abs(exact - sol[len(sol) - 1])}\n")
