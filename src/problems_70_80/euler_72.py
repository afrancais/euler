from primeutils import *


from fractions import gcd

count = 0

primes = list()

for i in xrange(2, 2 * 10 ** 6):
    if i % 10000 == 0:
        print i
    if is_prime(i):
        primes.append(i)
#for n in xrange(2,10 ** 6):
    #if n % 1000 == 0:
        #print n, count
    #get_prime_factors(n)
    ##for i in xrange(1, n):
        ##if i > 1 and n % i == 0:
            ##continue
        ##if i % 2 == 0 and n % 2 == 0:
            ##continue
        ##if i % 3 == 0 and n % 3 == 0:
            ##continue
        ##if gcd(i, n) == 1:
            ##count += 1

print 'OK, computing'

acc = 0
for i in xrange(2, 10 **6 + 1):
    if i % 1000 == 0:
        print i, acc
    acc += phi(i, primes)

print acc
