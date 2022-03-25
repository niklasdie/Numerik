# Aufgabe 3
import math
from time import time

import numpy as np

nums_n = [1, 2, 5, 10, 100, 1000, 100000]


def rechteck_summe(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(n):
        sum += f(a + i * h)
    return h * sum


def trapezregel(f, a, b, n):
    h = (b - a) / n
    sum = 0
    for i in range(1, n):
        sum += f(a + i * h)
    sum *= 2
    sum += f(a) + f(b)
    return (h / 2) * sum


def f1(x):
    return 1 / (x * x)


def f2(x):
    return np.log(x)


def run():
    print('∫ 1/x² dx from 1/10 to 10:')
    for n in nums_n:
        print('für n=' + str(n))
        print(rechteck_summe(f1, 0.1, 10, n))
        print(trapezregel(f1, 0.1, 10, n))
        print()

    print()
    print('∫ ln(x) dx from 1 to 2:')
    for n in nums_n:
        print('für n=' + str(n))
        print(rechteck_summe(f2, 1, 2, n))
        print(trapezregel(f2, 1, 2, n))
        print()


# if __name__ == '__main__':
#     run()


# Für f1 ist die Rechtecksumme genauer, man braucht aber generell ein großes n (n=10⁵).
# Für f2 ist die Trapezregel genauer und das schon für recht kleines n=10 (gerundet auf 3. Nachkommastelle).


# Aufgabe 4


def vektor2(f, a, b, n):
    h = (b - a) / n
    v = np.array([a + i * h for i in range(1, n)])
    v2 = f(v)
    s = np.sum(v2) * 2 + f(a) + f(b)
    return h / 2 * s


def vektor(f, a, b, n):
    h = (b - a) / n
    vektor1 = []
    for i in range(1, n):
        vektor1.append(a + i * h)
    for x in range(len(vektor1)):
        vektor1.insert(x, f(vektor1.pop(x)))
    summe = sum(vektor1)
    summe *= 2
    summe += f(a) + f(b)
    return (h / 2) * summe


def run2():
    print('∫ 1/x² dx from 1/10 to 10:')
    t = time()
    for n in nums_n:
        print('für n =', n)
        t = time()
        print("rechteck_summe:", rechteck_summe(f1, 0.1, 10, n))
        print("time for rechtecksumme:", time() - t)
        t = time()
        print("traprezregel", trapezregel(f1, 0.1, 10, n))
        print("time for trapezregel:", time() - t)
        t = time()
        print("v1", vektor(f1, 0.1, 10, n))
        print("time for vektor v1:", time() - t)
        t = time()
        print("v2", vektor2(f1, 0.1, 10, n))
        print("time for vektor v2:", time() - t)
        print()

    print()
    print('∫ ln(x) dx from 1 to 2:')
    for n in nums_n:
        print('für n =', n)
        t = time()
        print("summ", rechteck_summe(f2, 1, 2, n))
        print("time for rechtecksumme:", time() - t)
        t = time()
        print("trapez", trapezregel(f2, 1, 2, n))
        print("time for trapezregel:", time() - t)
        t = time()
        print("v1", vektor(f2, 1, 2, n))
        print("time for vektor v1:", time() - t)
        t = time()
        print("v2", vektor2(f2, 1, 2, n))
        print("time for vektor v2:", time() - t)
        t = time()
        print()


if __name__ == '__main__':
    run2()

# Man muss darauf achten, das man die numpy Vektoren nimmt, sonst ist die Vektorart nicht schneller.
