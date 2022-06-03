import numpy as np


def buildMatrix(n, gamma):
    A = np.zeros(shape=(n, n), dtype=np.float32)
    for i in range(0, n):
        for j in range(0, n):
            c = 1 / (gamma * np.sqrt(2 * np.pi))
            A[i][j] = (c / n) * np.exp(-((i - j) / (np.sqrt(2) * n * gamma)))
    return A


def buildX(n):
    x = np.zeros(shape=(n), dtype=np.float32)
    for i in range(0, n):
        if i >= 45 and i <= 55:
            x[i] = 1
        elif i >= 60 and i <= 65:
            x[i] = 0.5
    return x


def build_deltaB(n):
    b = (10 ** -6) * np.random.randn(n)
    return b


# Aufgabe a
def a_solv(A, b, delta_b):
    A_pinv = np.linalg.pinv(A)
    sol = A_pinv.dot(b) + A_pinv.dot(delta_b)
    return sol


# Aufgabe b
def b_solv(A, k, b):
    for i in k:
        U, E, V_t = np.linalg.svd(A)
        alpha = 10 ** i
        print(f"alpha = {alpha}")
        for j in range(0, A.shape[0]):
            if E[0] / E[j] > 1 / alpha:
                for l in range(j, A.shape[0]):
                    E[l] = 0
                break
        E = np.linalg.pinv(np.diag(E))
        x = np.linalg.solve(np.dot(np.dot(np.matrix.transpose(V_t), E), np.matrix.transpose(U)), b)
        print(f"x = {x}\n")


k = [0, -1, -2, -3, -4, -5, -6, -7, -8]

if __name__ == '__main__':
    np.set_printoptions(precision=5, suppress=True)
    n = 100
    gamma = 0.05
    A = buildMatrix(n, gamma)
    x = buildX(n)
    print(f"x = {x}\n")
    delta_b = build_deltaB(n)
    b = np.linalg.solve(np.linalg.inv(A), x)
    print(f"b = {b}\n")
    a_solv = a_solv(A, b, delta_b)
    print(f"a_solv = {a_solv}\n")
    b_solv(A, k, b)
