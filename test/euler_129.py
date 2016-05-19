from primeutils import *

primes = []
for p in xrange(2, 100):
    if is_prime(p):
        primes.append(p)

print divisors(41)
print phi(41, primes)
print phi(7, primes)
print is_prime(41)