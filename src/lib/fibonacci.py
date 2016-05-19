from decimal import *


def fibonacci_gen():
    """"""
    yield 1
    n1 = 1
    n2 = 1
    while True:
        n = n1 + n2
        n1 = n2
        n2 = n
        yield n


def fibonacci_last_digits(digits=10):
    """"""
    n1 = 1
    n2 = 1
    while True:
        n = int(n1) + int(n2)
        n1 = n2
        n2 = str(n)[-digits:]
        yield str(n)[-digits:]


def get_fibonacci(n):
    """"""
    fi = Decimal(1.61803398874989)
    return round(fi ** Decimal(n) / Decimal(5).sqrt())


def fibo2(n):
    """Renvoie F_{n-1}, F_n"""
    if n == 0:
        return 1, 0  # F_{-1}, F_0
    else:
        f_k_1, f_k = fibo2(n // 2)
        f2_k = f_k**2
        if n % 2 == 0:
            return f2_k + f_k_1**2, f_k * f_k_1 * 2 + f2_k
        else:
            return f_k * f_k_1 * 2 + f2_k, (f_k + f_k_1)**2 + f2_k


def fibonacci(n):
    """Renvoie F_n"""
    return fibo2(n)[1]
