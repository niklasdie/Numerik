# Aufgabe 1
import math


def pq_formel(p, q):
    return -p + math.sqrt(p * p + q)


def alternativ(p, q):
    return -q / (-p - math.sqrt(p * p + q))


nums = [2, 4, 6, 7, 8]


def run():
    for x in nums:
        print('p=10^' + str(x) + ' , p=1: ')
        print(pq_formel(math.pow(10, x), 1))
        print(alternativ(math.pow(10, x), 1))
        print()


if __name__ == '__main__':
    run()

# Die Alternative ist für große p genauer.
