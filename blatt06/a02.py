# Aufgabe 4
import numpy as np


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
        tmp = np.copy(lu[spalte])
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
    return np.array(lu), np.array(p)


def nachiteration(A, b, x):
    r = np.zeros(shape=(b.shape[0]), dtype=np.float32)
    p = np.zeros(shape=(b.shape[0]), dtype=np.float32)
    epsilon = 0.000001
    while True:
        r = np.subtract(b, np.matmul(A, x))
        p = np.matmul(np.linalg.inv(A), r)
        x = np.add(x, p)
        if (np.linalg.norm(p)/np.linalg.norm(x)) < epsilon:
            break
    return x


def permutation(p, u):
    c = np.copy(u)
    for x in range(len(p)):
        tmp = np.copy(c[x])
        c[x] = c[p[x] - 1]
        c[p[x] - 1] = tmp
    print(f"Pu = {c}")
    return np.array(c)


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
    y = np.array(y)
    print(f"y = {y}")
    return y


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
    b = np.array(b)
    print("x = " + str(b))
    return b


def baueBeispiel1(n):
    A = np.zeros(shape=(n, n), dtype=np.float32)
    for i in range(n):
        A[i][i] = 1
        A[i][n - 1] = 1
        if i > 0:
            for j in range(i):
                A[i][j] = -1

    b = np.zeros(shape=(n), dtype=np.float32)
    b[n - 1] = 2 - n
    for i in range(0, n - 1):
        b[i] = 3 - i
    return A, b


def baueBeispiel2(n):
    A = np.zeros(shape=(n, n), dtype=np.float32)
    for i in range(n):
        for j in range(n):
            A[i][i] = 1
            if j > i:
                A[i][j] = 0
            if j < i:
                A[i][j] = i + j

    b = np.zeros(shape=(n), dtype=np.float32)
    b[0] = 1
    return A, b


A1 = np.array(
    [[0, 0, 0, 1],
     [2, 1, 2, 0],
     [4, 4, 0, 0],
     [2, 3, 1, 0]], dtype=np.float32)
b1 = np.array([3, 5, 4, 5])
# x = [0.0, 1.0, 2.0, 3.0]

n1 = [50, 70, 100]
n2 = [5, 10, 15]

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    print("LU-Zerlegung mit Pivot-Strategie:")
    print(f"A = \n{A1}")
    LU, p = zerlegung(A1)
    c = permutation(p, b1)
    rueckwaerts(LU, vorwaerts(LU, c))
    print("\nAufgabe 2a:")
    for i in n1:
        print(f"\nn={i}")
        A, b = baueBeispiel1(i)
        LU, p = zerlegung(A)
        c = permutation(p, b)
        x = rueckwaerts(LU, vorwaerts(LU, c))
        print(f"Nachiteration: x =  {nachiteration(A, b, x)}")
    print("\nAufgabe 2b:")
    for i in n2:
        print(f"\nn={i}")
        A, b = baueBeispiel1(i)
        LU, p = zerlegung(A)
        c = permutation(p, b)
        x = rueckwaerts(LU, vorwaerts(LU, c))
        print(f"Nachiteration: x = {nachiteration(A, b, x)}")
