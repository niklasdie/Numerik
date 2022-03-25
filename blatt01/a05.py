# Aufgabe 5
import numpy


# Teil a 2
def wurzel(k, x, x0):
    return y(k, x, x0)


def a(k, x, x0):
    if k > 0:
        return ((3 / (2 * k)) - 1) * ((x / x0) - 1) * a(k - 1, x, x0)
    return numpy.sqrt(x0)


def y(k, x, x0):
    if k > 0:
        return y(k - 1, x, x0) + a(k, x, x0)
    return numpy.sqrt(x0)


# Man braucht 4 bzw 9 Iterationen, um eine Abweichung kleiner als 0,005 zu haben.


# Teil b
def heron(k, x, y0):
    if k > 0:
        return (heron(k - 1, x, y0) + (x / heron(k - 1, x, y0))) / 2
    return y0


def run():
    print()
    print("run()")
    w = numpy.sqrt(2)
    b1 = 1
    b2 = 1
    for k in range(1, 100):
        w1 = wurzel(k, 2, 1)
        w2 = wurzel(k, 2, 4)
        if numpy.abs(w1 - w) < 0.005 and b1 == 1:
            print()
            print(w1)
            print(k, "versuche um Abweichung kleiner als 0.005")
            b1 = 0
        if numpy.abs(w2 - w) < 0.005 and b2 == 1:
            print()
            print(w2)
            print(k, "versuche um Abweichung kleiner als 0.005")
            b2 = 0
        if b1 == 0 and b2 == 0:
            w1 = wurzel(20, 2, 1)
            w2 = wurzel(20, 2, 4)
            print()
            print("√2:", w)
            print("w1:", w1)
            print("w2:", w2)
            print("Abweichung w1:", numpy.abs(w1 - w))
            print("Abweichung w2:", numpy.abs(w2 - w))
            break


def run2():
    print()
    print("run2()")
    w = numpy.sqrt(2)
    b1 = 1
    b2 = 1
    for k in range(1, 100):
        w1 = heron(k, 2, 1)
        w2 = heron(k, 2, 4)
        if numpy.abs(w1 - w) < 0.005 and b1 == 1:
            print()
            print(w1)
            print(k, "versuche um Abweichung kleiner als 0.005")
            b1 = 0
        if numpy.abs(w2 - w) < 0.005 and b2 == 1:
            print()
            print(w2)
            print(k, "versuche um Abweichung kleiner als 0.005")
            b2 = 0
        if b1 == 0 and b2 == 0:
            w1 = heron(20, 2, 1)
            w2 = heron(20, 2, 2)
            print()
            print("√2:", w)
            print("w1:", w1)
            print("w2:", w2)
            print("Abweichung w1:", numpy.abs(w1 - w))
            print("Abweichung w2:", numpy.abs(w2 - w))
            break


if __name__ == '__main__':
    run()
    run2()

# Nach 20 Iterationen ist das Heron-Verfahren um ein vieles genauer, wie das Verfahren aus dem ersten Aufgabenteil.
# Das Heron-Verfahren hatte schon nach 2 bzw 4 Iterationen eine kleinere Abweichung wie 0,005.
# Allerdings wird der Aufwand für hohe Iterationen sehr hoch.
