# Aufgabe 2
import numpy

def zerlegung(A):
    lu = A.copy()
    p = []
    for zeile in range(lu.shape[0]-1):
        # Diagonale != 0?
        if lu[zeile][zeile] == 0:
            for f in range(zeile, lu.shape[0]):
                if lu[f][zeile] != 0:
                    # Zeilen tauschen
                    tmp = numpy.copy(lu[zeile])
                    lu[zeile] = lu[f]
                    lu[f] = tmp
                    p.append(f + 1)
                    break
        else:
            p.append(zeile + 1)

        for y in range(zeile + 1, lu.shape[0]):
            div = int(lu[y][zeile] / lu[zeile][zeile])
            if div != 0:
                lu[y][zeile] = div
                for x in range(zeile + 1, lu.shape[1]):
                    lu[y][x] = lu[y][x] - (lu[zeile][x] * div)

    print("\nLU =\n" + str(lu))
    print("p = " + str(p))
    return lu, p


def permutation(p, b):
    c = numpy.copy(b)
    for x in range(len(p)):
        tmp = numpy.copy(c[x])
        c[x] = c[p[x] - 1]
        c[p[x] - 1] = tmp
    print("Pb = " + str(c))
    return c


def vorwaerts(LU, c):
    # LU*b=c
    b = []
    for x in range(LU.shape[0]):
        res = c[x]
        for r in range(len(b)):
            if x == r:
                res -= b[r]
            else:
                res -= (LU[x][r] * b[r])
        b.append(res)
    print("y = " + str(b))
    return b


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


# Beispiel aus Aufgabe 1
a1 = numpy.array([[0, 1, 3, 1], [1, 1, 2, 0], [4, 4, 8, 2], [2, 6, 4, 8]])
# Beispiel aus Aufgabe 2
a2 = numpy.array([[0, 0, 0, 1], [2, 1, 2, 0], [4, 4, 0, 0], [2, 3, 1, 0]])
# Beispiel aus Aufgabe 1
b1 = numpy.array([5, 1, 8, 18])
b2 = numpy.array([5, 7, 28, 22])
# Beispiel aus Aufgabe 2
b3 = numpy.array([3, 5, 4, 5])
b4 = numpy.array([4, 10, 12, 11])

if __name__ == '__main__':
    print("Matrix a1:")
    print(a1)
    LU, p = zerlegung(a1)
    print("\nb1: " + str(b3))
    c = permutation(p, b1)
    print("Löse b1 mit LU von a1:")
    rueckwaerts(LU, vorwaerts(LU, c))
    print("\nb2: " + str(b3))
    c = permutation(p, b2)
    print("Löse b2 mit LU von a1:")
    rueckwaerts(LU, vorwaerts(LU, c))
    print("\nMatrix a2:")
    print(a2)
    LU, p = zerlegung(a2)
    print("\nb3: " + str(b3))
    c = permutation(p, b3)
    print("Löse b3 mit LU von a2:")
    rueckwaerts(LU, vorwaerts(LU, c))
    print("\nb4: " + str(b3))
    c = permutation(p, b4)
    print("Löse b4 mit LU von a2:")
    rueckwaerts(LU, vorwaerts(LU, c))

    for n in [10, 20, 100]:
        print("\n\nAx=b mit Dimension n = " + str(n))
        A = numpy.empty([n, n])
        b = numpy.empty([n])
        for i in range(n):
            b[i] = 1 / ((i + 1) + 1)
            for j in range(n):
                A[i][j] = 1 / ((i + 1) + (j + 1) - 1)
        print("A =\n" + str(A))
        print("b = " + str(b))
        LU, p = zerlegung(A)
        c = permutation(p, b)
        print("Löse b mit LU von A:")
        rueckwaerts(LU, vorwaerts(LU, c))
