from itertools import takewhile

from lib.fibonacci import fibonacci_gen


def run():
    g = fibonacci_gen()
    return sum(filter(lambda x: x % 2 == 0, takewhile(lambda x: x < 4000000, g)))
