from matplotlib import pyplot as plt
import numpy as np


def pol_str(p):
    s = ""
    for i in range(len(p) - 1, -1, -1):
        if p[i] != 0:
            if p[i] != 1:
                if p[i] > 0:
                    s += "+" + str(round(p[i], 3))
                else:
                    s += str(round(p[i], 3))
            if i != 0:
                s += "x^{" + str(i) + "}"
        s += " "
    return s


# Aufgabe 2 a

def divDif(p):
    i = len(p)
    d = np.zeros(shape=(i, i), dtype=np.float32)
    for n in range(0, i):
        d[n][n] = p[n][1]
    for n in range(0, i):
        for m in range(n - 1, -1, -1):
            d[n][m] = (d[n][m + 1] - d[n - 1][m]) / (p[n][0] - p[m][0])
    return d


def interpolation(d, pk):
    n = len(d) - 1
    p = np.zeros(shape=(n + 1), dtype=np.float32)
    p[0] = d[n][0]
    for k in range(1, n + 1):
        p = shift(p)
        p = multiply(p, pk[n - k][0])
        p[0] = p[0] + d[n - k][0]
    return p


def shift(p):
    for i in range(len(p) - 1, 0, -1):
        p[i] = p[i - 1]
    p[0] = 0
    return p


def multiply(p, x):
    for i in range(0, len(p) - 1):
        p[i] = p[i] - (x * p[i + 1])
    return p


def pol_auswerten(p, x):
    y = 0
    for i in range(0, len(p)):
        y += p[i] * x ** i
    return y


# Aufgabe 2 b

def f(x):
    return 1 / (1 + x * x)


def punkte_berechnen1(m):
    p = np.zeros(shape=(m, 2), dtype=np.float32)
    for i in range(0, m):
        p[i][0] = -5 + ((10 / (m - 1)) * i)
        p[i][1] = f(p[i][0])
    return p


# Aufgabe 2 c

def punkte_berechnen2(m):
    p = np.zeros(shape=(m, 2), dtype=np.float32)
    for i in range(0, m):
        p[i][0] = -5 * np.cos(np.pi * ((2 * i + 1) / (2 * m)))
        p[i][1] = f(p[i][0])
    return p


if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    linspace = np.linspace(-10, 10, 1000)
    # Aufgabe 2 a
    print("Aufgabe 2 a:")
    print("Aus Aufgabe 1:")
    pk = [[-1, -2], [0, 4], [1, 6], [3, 22]]
    d = divDif(pk)
    print(f"d =\n{d}")
    p = interpolation(d, pk)
    print(f"p(x) = {pol_str(p)}")
    y = pol_auswerten(p, 3)
    print(f"p(3) = {y}")
    plt.plot(linspace, pol_auswerten(p, linspace))
    plt.show()

    print("\nTest:")
    p = [[0, 3], [1, 2], [3, 6]]
    d = divDif(p)
    print(f"d =\n{d}")
    p = interpolation(d, p)
    print(f"p(x) = {pol_str(p)}")
    y = pol_auswerten(p, 2)
    print(f"p(2) = {y}")
    plt.plot(linspace, pol_auswerten(p, linspace))
    plt.show()

    # Aufgabe 2 b
    linspace = np.linspace(-5, 5, 1000)
    print("\nAufgabe 2 b:")
    m = [7, 9, 11]
    for i in m:
        pk = punkte_berechnen1(i)
        d = divDif(pk)
        p = interpolation(d, pk)
        print(f"p(x) = {pol_str(p)}")
        plt.plot(linspace, pol_auswerten(p, linspace))
        plt.show()
    print("f(x)")
    plt.plot(linspace, f(linspace))
    plt.show()

    # Alle Polynome oszillieren sehr stark, besonders am Rand.
    # Aber je höher der Grad des Polynoms, desto besser ist es um x=0.
    print("Alle Polynome oszillieren sehr stark, besonders am Rand.\n"
          "Aber je höher der Grad des Polynoms, desto besser ist es um x=0.")

    # Aufgabe 2 b
    print("\nAufgabe 2 c:")
    for i in m:
        pk = punkte_berechnen2(i)
        d = divDif(pk)
        p = interpolation(d, pk)
        print(f"p(x) = {pol_str(p)}")
        plt.plot(linspace, pol_auswerten(p, linspace))
        plt.show()
    print("f(x)")
    plt.plot(linspace, f(linspace))
    plt.show()

    # Weiter oszillieren alle Polynome, der Rand ist aber viel besser.
    print("Weiter oszillieren alle Polynome, der Rand ist aber viel besser.")
