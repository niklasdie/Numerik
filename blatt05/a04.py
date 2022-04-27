from time import time
import numpy as np


def householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    tau = 2 / (v.T @ v)

    return v, tau


def qr_decomposition(A: np.ndarray):
    m, n = A.shape
    R = A.copy()
    Q = np.identity(m)

    for j in range(0, n):
        v, tau = householder(R[j:, j, np.newaxis])
        H = np.identity(m)
        H[j:, j:] -= tau * (v @ v.T)
        R = H @ R
        Q = H @ Q

    return Q[:n].T, np.triu(R[:n])


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

    # print(f"LU =\n{lu}") # not printing for cleaner output
    # print(f"p = {p}") # not printing for cleaner output
    return np.array(lu), np.array(p)


def permutation(p, u):
    c = np.copy(u)
    for x in range(len(p)):
        tmp = np.copy(c[x])
        c[x] = c[p[x] - 1]
        c[p[x] - 1] = tmp
    # print(f"Pu = {c}") # not printing for cleaner output
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
    # print(f"y = {y}") # not printing for cleaner output
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
    # print("x = " + str(b)) # not printing for cleaner output
    return b


def baueBeispiel(n):
    A = np.zeros(shape=(n, n), dtype=np.float32)
    for i in range(n):
        A[i][i] = 1
        A[i][n - 1] = 1
        if (i > 0):
            for j in range(i):
                A[i][j] = -1

    b = np.zeros(shape=(n), dtype=np.float32)
    b[n - 1] = 2 - n
    for i in range(0, n - 1):
        b[i] = 3 - i
    return A, b


A1 = np.array(
    [[0, 0, 0, 1],
     [2, 1, 2, 0],
     [4, 4, 0, 0],
     [2, 3, 1, 0]], dtype=np.float32)
b1 = np.array([3, 5, 4, 5])

n = [10, 50, 100]

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    print("Householder:")
    print(f"A = \n{A1}")
    Q, R = qr_decomposition(A1)
    print(f"Q = \n{Q}")
    print(f"R = \n{R}")
    y = np.linalg.solve(Q, b1)
    print(f"y = {y}")
    x = np.linalg.solve(R, y)
    print(f"x = {x}")

    for i in n:
        print(f"\nn={i}")
        A, b = baueBeispiel(i)
        print(f"A = \n{A}")
        t = time()
        Q, R = qr_decomposition(A)
        hh = time() - t
        print(f"Q = \n{Q}")
        print(f"R = \n{R}")
        print(f"time for Householder: {hh}s")
        t = time()
        y = np.linalg.solve(Q, b)
        x = np.linalg.solve(R, y)
        shh = time() - t
        print(f"y = {y}")
        print(f"QR: x = {x}")
        print(f"time for solving Householder: {shh}s")
        t = time()
        LU, p = zerlegung(A)
        lu = time() - t
        print(f"time for LU: {lu}s")
        t = time()
        c = permutation(p, b)
        x = rueckwaerts(LU, vorwaerts(LU, c))
        print(f"LU: x = {x}")
        slu = time() - t
        print(f"time for solving LU: {slu}s")
        print(f"time difference Householder to LU: {hh - lu}s")
        print(f"time difference solving Householder to LU: {shh - slu}s")
