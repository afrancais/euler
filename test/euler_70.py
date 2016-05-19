import numberutils
from primeutils import is_prime, phi

primes = list()

m = (0, 0, 0)
for i in xrange(2, 10 ** 7 + 1):
    if is_prime(i):
        primes.append(i)


for i in xrange(8 * 10 ** 6, 10 ** 7 + 1):
    if i % 10000 == 0:
        print i, m
    p = phi(i, primes)
    if numberutils.is_permutation(i, p):
        r = float(i)/p
        if m[1] > r or not m[1]:
            m = (i, r, p)

print m
