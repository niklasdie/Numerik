# Aufgabe 2
import math


def method_1(x, n):
    sum = 0
    for k in range(n + 1):
        sum += math.pow(x, k) / (math.factorial(k))
    return sum


def method_2(x, n):
    sum = 0
    for k in range(n + 1):
        sum += math.pow(x, n - k) / (math.factorial(n - k))
    return sum


nums_n = [2, 3, 5, 10, 50, 100]
nums_x = [1, 2, 4, 10, 50]


def run():
    for x in nums_x:
        for n in nums_n:
            print('for n=' + str(n) + ' and x=' + str(x))
            print('methode_1: ' + str(method_1(x, n)))
            print('methode_2: ' + str(method_2(x, n)))
            print('e^x:       ' + str(math.exp(x)))
            print()


if __name__ == '__main__':
    run()

# Methode 1 ist für große n genauer.
