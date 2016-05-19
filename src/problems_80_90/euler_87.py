from primeutils import *
from itertools import *

primes = []

s = set()

for i in xrange(2, 8000):
    if is_prime(i):
        primes.append(i)

print len(primes)

k = 1

for c in combinations_with_replacement(primes, 3):
    for p in permutations(c):
        if k % 10000 == 0:
            print k, p, len(s)
        k += 1
        r = p[0] ** 2 + p[1] ** 3 + p[2] ** 4
        if r > 50000000:
            continue
        s.add(r)



print len(s)