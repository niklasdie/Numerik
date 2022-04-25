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


def vorwaerts(Q, b):
    # Q*y=b
    y = []
    for x in range(Q.shape[0]):
        res = b[x]
        for r in range(len(y)):
            if x == r:
                res -= y[r]
            else:
                res -= (Q[x][r] * y[r])
        y.append(res)
    print(f"y = {y}")
    return np.array(y)


def rueckwaerts(R, y):
    # R*b=y
    b = []
    for x in range(R.shape[0] - 1, -1, -1):
        res = y[x]
        if len(b) == 0:
            res /= R[x][x]
        else:
            for r in range(0, len(b)):
                res -= (R[x][R.shape[1] - r - 1] * b[len(b) - r - 1])
            res /= R[x][x]
        b.insert(0, res)
    print("x = " + str(b))
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
        Q, R = qr_decomposition(A)
        print(f"Q = \n{Q}")
        print(f"R = \n{R}")
        y = np.linalg.solve(Q, b)
        print(f"y = {y}")
        x = np.linalg.solve(R, y)
        print(f"x = {x}")
