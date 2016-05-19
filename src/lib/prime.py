# -*- coding: utf-8 -*-

"""
 :Authors: Dolead R&D Team <rd@dolead.com>
 :Date: 19/05/16
"""
from itertools import count


def postponed_sieve():
    yield 2
    yield 3
    yield 5
    yield 7
    sieve = {}
    ps = postponed_sieve()
    p = next(ps) and next(ps)
    q = p * p
    for c in count(9, 2):
        if c in sieve:
            s = sieve.pop(c)
        elif c < q:
            yield c
            continue
        else:   # (c==q):
            s = count(q + 2 * p, 2 * p)
            p = next(ps)
            q = p * p
        for m in s:
            if m not in sieve:
                break
        sieve[m] = s


def prime_factors(n, primes=None):
    primes = primes or postponed_sieve()
    m = n
    f = []
    for p in primes:
        if p > m:
            break
        if m % p == 0:
            f.append(p)
            while m % p == 0:
                m /= p
            print(p, m)
    return f