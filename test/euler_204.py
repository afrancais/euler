
from primeutils import *

primes = []
for i in xrange(2,100):
    if is_prime(i):
        primes.append(i)

print primes

p = PrimeUtils(primes)
acc = 0
for i in xrange(1, 10 ** 9 + 1):
    if i % 100000 == 0:
        print i, acc
    if p.is_hamming_number(i):
        acc += 1

print acc

