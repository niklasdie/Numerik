# Aufgabe 4
import numpy


def zerlegung(A):
    lu = A.copy()
    p = []
    for spalte in range(lu.shape[0] - 1):
        max_element = abs(lu[spalte][spalte])
        max_element_pos = spalte
        for zeile in range(spalte, lu.shape[0]):
            if (max_element < abs(lu[zeile][spalte])):
                max_element = abs(lu[zeile][spalte])
                max_element_pos = zeile

        # Zeilen tauschen
        tmp = numpy.copy(lu[spalte])
        lu[spalte] = lu[max_element_pos]
        lu[max_element_pos] = tmp
        p.append(max_element_pos + 1)

        for y in range(spalte + 1, lu.shape[0]):
            div = float(lu[y][spalte] / lu[spalte][spalte])
            if div != 0:
                lu[y][spalte] = div
                for x in range(spalte + 1, lu.shape[0]):
                    lu[y][x] = lu[y][x] - lu[spalte][x] * div
            else:
                lu[y][spalte] = 0

    print(f"LU =\n{lu}")
    print(f"p = {p}")
    return numpy.array(lu), numpy.array(p)


def permutation(p, u):
    c = numpy.copy(u)
    for x in range(len(p)):
        tmp = numpy.copy(c[x])
        c[x] = c[p[x] - 1]
        c[p[x] - 1] = tmp
    print(f"Pu = {c}")
    return numpy.array(c)


def vorwaerts(LU, b):
    # L*y=b
    y = []
    for x in range(LU.shape[0]):
        res = b[x]
        for r in range(len(y)):
            if x == r:
                res -= y[r]
            else:
                res -= (LU[x][r] * y[r])
        y.append(res)
    print(f"y = {y}")
    return numpy.array(y)


def rueckwaerts(LU, y):
    # LU*b=y
    b = []
    for x in range(LU.shape[0] - 1, -1, -1):
        res = y[x]
        if len(b) == 0:
            res /= LU[x][x]
        else:
            for r in range(0, len(b)):
                res -= (LU[x][LU.shape[1] - r - 1] * b[len(b) - r - 1])
            res /= LU[x][x]
        b.insert(0, res)
    print("x = " + str(b))
    return b


def baueBeispiel(n, beta):
    A = numpy.zeros(shape=(n,n), dtype=numpy.float32)
    # A = numpy.array([[] * n] * n, dtype=numpy.float32)
    for i in range(n):
        A[i][i] = 1
        if i > 0:
            A[i][i - 1] = -beta
    A[0][n-1] = beta
    A[n - 1][n - 1] = 0

    b = numpy.zeros(shape=(n), dtype=numpy.float32)
    b[0] = 1 + beta
    for i in range(1, n-1):
        b[i] = 1 - beta
    b[n-1] = -beta
    return A, b


A1 = numpy.array(
    [[0, 0, 0, 1],
     [2, 1, 2, 0],
     [4, 4, 0, 0],
     [2, 3, 1, 0]], dtype=numpy.float32)
b1 = numpy.array([3, 5, 4, 5])
# x = [0.0, 1.0, 2.0, 3.0]

beta = 10
n = [10, 20, 100]

if __name__ == '__main__':
    numpy.set_printoptions(precision=3, suppress=True)
    print("LU-Zerlegung mit Pivot-Strategie:")
    print(f"A = \n{A1}")
    LU, p = zerlegung(A1)
    c = permutation(p, b1)
    rueckwaerts(LU, vorwaerts(LU, c))
    for i in n:
        print(f"\nn={i}")
        A, b = baueBeispiel(i, beta)
        LU, p = zerlegung(A)
        c = permutation(p, b)
        rueckwaerts(LU, vorwaerts(LU, c))
