import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

from scipy.sparse import spdiags, csr_matrix
import matplotlib.animation as animation


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


def Ablock(m):
    # Blockmatrix fuerr 2d-Laplace
    n = m * m

    e = np.ones(n)
    l = np.ones(n)
    l[m - 1::m] = 0.0
    r = np.ones(n)
    r[::m] = 0.0

    A = spdiags([-e, -l, 4.0 * e, -r, -e], [-m, -1, 0, 1, m], n, n, format='csr')

    return A.toarray()


def ew_exakt(m): # LÄUFT NICHT BEI MIR !!!
    # exakte Eigenwerte fuer 2d-Laplace Blockmatrix, absteigend sortiert
    ew1d = 2.0 * (1.0 - np.cos((np.arange(m) + 1.0) * np.pi / (m + 1.0)))

    ew = (np.c_[ew1d] + ew1d).flatten()
    ew.sort()

    return ew[::-1]


def plotev(xk):
    # Eigenvektoren fuer 2d-Laplace Blockmatrix graphisch darstellen
    n = len(xk)
    m = int(np.sqrt(n))

    h = np.linspace(0, 1, m)
    yy, xx = np.meshgrid(h, h)

    fig = plt.figure()
    ax = plt.subplot(projection='3d')

    surf = ax.plot_surface(xx, yy, xk.reshape(m, m), cmap=plt.cm.jet, rstride=1, cstride=1)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("Hoehe")
    plt.colorbar(surf)


def animev(xk):
    # Eigenvektoren fuer 2d-Laplace Blockmatrix animieren
    n = len(xk)
    m = int(np.sqrt(n))

    h = np.linspace(0, 1, m)
    yy, xx = np.meshgrid(h, h)
    zz = xk.reshape(m, m)

    zmax = 1.1 * abs(zz).max()

    def a(nf=100, inter=100, rep=False):
        fig = plt.figure()
        ax = plt.subplot(projection='3d')
        ax.set_axis_off()
        ax.grid(False)

        surf = ax.plot_surface(xx, yy, zz, cmap=plt.cm.jet, rstride=1, cstride=1)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("Hoehe")
        # colorbar(surf)

        ax.set_zlim(-zmax, zmax)

        def update(i, ax, fig):
            ax.cla()
            phi = i * 180.0 / np.pi / nf
            zzi = np.cos(phi) * zz
            wframe = ax.plot_surface(xx, yy, zzi, cmap=plt.cm.jet, rstride=1, cstride=1)
            ax.set_zlim(-zmax, zmax)
            ax.set_axis_off()
            ax.grid(False)
            return wframe,

        return animation.FuncAnimation(fig, update,
                                       frames=range(nf),
                                       fargs=(ax, fig), interval=inter, repeat=rep)

    return a


def sign(t):
    if t >= 0:
        return 1
    else:
        return -1


def jacobi(a, tol=1.0e-3):
    def maxElem(a):  # groesstes nicht diagonal Element
        n = len(a)
        max_elem = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i, j]) >= max_elem:
                    max_elem = abs(a[i, j])
                    k = i
                    l = j
        return max_elem, k, l

    def rotate(a, p, k, l):  # rotieren fuer a[k,l] = 0
        n = len(a)
        aDiff = a[l, l] - a[k, k]
        if abs(a[k, l]) < abs(aDiff) * 1.0e-36:
            t = a[k, l] / aDiff
        else:
            phi = aDiff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + sqrt(phi ** 2 + 1.0))
            if phi < 0.0: t = -t
        c = 1.0 / sqrt(t ** 2 + 1.0)
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp
        for i in range(k):  # fuer i < k
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(k + 1, l):  # fuer k < i < l
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])
        for i in range(l + 1, n):  # fuer i > l
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])
        for i in range(n):  # Update transformation matrix
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    n = len(a)
    maxRot = 5 * (n ** 2)
    p = np.identity(n) * 1.0
    for i in range(maxRot):
        max_elem, k, l = maxElem(a)
        if max_elem < tol:
            return np.diagonal(a), p
        rotate(a, p, k, l)
    print('Jacobi-Verfahren konvergiert nicht!')


m = 10

if __name__ == '__main__':
    np.set_printoptions(precision=3, suppress=True)
    A, b = system(m)
    A = csr_matrix.toarray(A)
    print(f"A =\n{A}\n")
    eig_w, eig_v = jacobi(A)
    eig_w = np.sort(eig_w)
    print(f"eig_v =\n{eig_v}")
    print(f"eig_w =\n{eig_w}")
    plotev(eig_v[0])
    animev(eig_v[0])()
    A, b = system(m)
    A = csr_matrix.toarray(A)
    eig_w, eig_v = np.linalg.eig(A)
    eig_w = np.sort(eig_w)
    print("\nKontrolle:")
    print(f"eig_v =\n{eig_v}")
    print(f"eig_w =\n{eig_w}")
    plotev(eig_v[0])
    animev(eig_v[0])()
