import math
from functools import lru_cache, reduce


def is_prime(i):
    """Define if a number is prime"""
    for j in range(2, int(math.sqrt(abs(i)) + 1)):
        if i % j == 0:
            return False
    return True


def get_prime_factors(value, stopOnFirst=False, primes=[]):
    print(value)
    """Get prime factors"""
    factors = []

    acc = value
    k = 1
    g = prime_gen()
    i = g.next()
    primes.append(i)
    while i <= acc:
        if k % 10000 == 0:
            print(acc, len(factors), k)
        if k > 1000000:
            return factors
        if acc % i == 0:
            factors.append(i)
            if stopOnFirst or len(factors) == 40:
                return factors
            while acc % i == 0:
                print(i)
                acc /= i
            print(acc)
            try:
                if acc < 10**15 and is_prime(acc):
                    primes.append(acc)
                    factors.append(acc)
                    return(factors)
            except:
                pass
        k += 1
        i = g.next()

    return factors, primes


def get_prime_factors_and_powers(value, primes):
    """Get prime factors and their powers"""
    factors = []

    temp = value
    i = 0
    k = primes[i]
    while k <= temp:
        if temp % k == 0:
            power = 0
            while temp % k == 0:
                power += 1
                temp /= k
            factors.append((k, power))
        i += 1
        k = primes[i]
    return factors


def prime_gen():
    k = 2
    while True:
        if is_prime(k):
            yield k
        k+=1


def get_raw_prime_factors_and_powers(value):
    """Get prime factors and their powers"""
    factors = []

    temp = value
    i = 0
    p = prime_gen()
    k = p.next()
    while k <= temp:
        if temp % k == 0:
            power = 0
            while temp % k == 0:
                power += 1
                temp /= k
            factors.append((k, power))
        i += 1
        k = p.next()
    return factors




class PrimeUtils:

    def __init__(self, primes):
        self.primes = primes

    def get_prime_factors_and_powers(self, value):
        """Get prime factors and their powers"""
        factors = []

        temp = value
        i = 0
        k = self.primes[i]
        while k <= temp:
            if temp % k == 0:
                power = 0
                while temp % k == 0:
                    power += 1
                    temp /= k
                factors.append((k, power))
            i += 1
            k = self.primes[i]
        return factors

    @lru_cache()
    def phi(self, n):
        """Euler phi function"""
        acc = []
        factors = self.get_prime_factors_and_powers(n)
        if n == 1:
            return 1
        for f, p in factors:
            acc.append(f - 1)
            acc.append(f ** (p - 1))
        return reduce(lambda x, y: x * y, acc)

    def is_hamming_number(self, n):
        """Get prime factors and their powers"""

        temp = n
        for prime in self.primes:
            if temp < prime:
                break
            while temp % prime == 0:
                temp /= prime
        return temp == 1


def phi(n, primes):
    """Euler phi function"""
    acc = []
    factors = get_prime_factors_and_powers(n, primes)
    if n == 1:
        return 1
    for f, p in factors:
        acc.append(f - 1)
        acc.append(f ** (p - 1))
    return reduce(lambda x, y: x * y, acc)


def divisors(n):
    """Euler phi function"""
    d = set()
    for i in range(2, n/2 + 1):
        if n % i == 0:
            d.add(i)
    return d


def is_square_divided(n):
    """"""
    for i in range(2, n/2+1):
        k = i ** 2
        if k > n:
            break
        if n % k == 0:
            return True
    return False

def get_number_of_divisors():
    factors = get_prime_factors_and_powers(n, primes)
    for f, p in factors:
        acc.append(f - 1)
        acc.append(f ** (p - 1))
    return reduce(lambda x, y: x * y, acc)

