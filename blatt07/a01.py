import numpy as np
import matplotlib.pyplot as plt

from scipy.sparse import spdiags, csr_matrix


def system(m):
    n = m * m

    e = np.ones(n)
    l = np.ones(n)
    l[m - 1::m] = 0.0
    r = np.ones(n)
    r[::m] = 0.0

    A = spdiags([-e, -l, 4.0 * e, -r, -e], [-m, -1, 0, 1, m], n, n, format='csr')

    b = -e / float(n)

    return A, b


def plotxk(xk):
    n = len(xk)
    m = int(np.sqrt(n))

    h = np.linspace(0, 1, m)
    yy, xx = np.meshgrid(h, h)

    fig = plt.figure('xk, m = {0}'.format(m))
    ax = fig.gca(projection='3d')

    surf = ax.plot_surface(xx, yy, xk.reshape(m, m), cmap=plt.cm.jet, rstride=5, cstride=5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Hoehe")
    plt.colorbar(surf)


def cg_verfahren(A, b):
    n = b.shape[0]
    x = np.zeros(shape=(n), dtype=np.float32)
    r = b - A.dot(x)
    p = r
    r0 = r
    k = 1
    while k >= 0.0000001:
        alpha = r.dot(r) / p.dot(A.dot(p))
        x = x + alpha * p
        r_new = r - (alpha * A).dot(p)
        beta = r_new.dot(r_new) / r.dot(r)
        p = r_new + beta * p
        k = np.linalg.norm(r) / np.linalg.norm(r0)
        r = r_new
    return x


m = [50, 100, 200]

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    for i in m:
        A, b = system(i)
        A = csr_matrix.toarray(A)
        x = cg_verfahren(A, b)
        ref = np.linalg.solve(A, b)
        print(f"x = {x}")
        print(f"ref = {x}\n")
        plotxk(x)
