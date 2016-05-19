from primeutils import *

last_divisors = None

primes = []
g = prime_gen()

p = g.next()
i = 0
while p < 10 ** 7:
    primes.append(p)
    p = g.next()
    i += 1
    if i % 1000 == 0:
        print i, p

primes.append(g.next())


print 'Done generating'
acc = 0
for i in xrange(2, 10**7):
    if i % 10000 == 0:
        print i, acc
    if not last_divisors:
        di = divisors(i, primes)
    else:
        di = last_divisors
    dii = divisors(i + 1, primes)
    last_divisors = dii
    if di == dii:
        acc += 1

print acc
