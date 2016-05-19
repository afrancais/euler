import itertools
import primeutils
from nways import nway

g = primeutils.prime_gen()
primes = []

print 'coucou'
for i in xrange(2, 1000):
    if primeutils.is_prime(i):
        primes.append(i)

print "prime generated"

for i in xrange(1, 100):
    p = itertools.takewhile(lambda x: x <= i, primes)
    p = [pr for pr in p]
    print p
    r = nway(i, p)
    if i % 100 == 0:
        print i, r
    if r >= 5000:
        print i, r, 'prout'
        break
