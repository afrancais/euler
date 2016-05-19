# -*- coding: UTF-8 -*-
from primeutils import *
from itertools import *
primes = []

k = 0
g = prime_gen()

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(imap(lambda x: True, takewhile(pred, iterable)))
    #return sum(imap(pred, iterable))

acc = 0
N = 10 ** 8

while True:
    k += 1
    p = g.next()
    if p > N/2:
        break
    if k % 1000 == 0:
        print k, p

    primes.append(p)
    acc += quantify(primes, lambda x: p*x <= N)

print acc
