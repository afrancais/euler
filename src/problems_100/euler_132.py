from primeutils import *
from decimal import *

#s = divisors(10**9)
s = set([8000000, 4000000, 2, 4, 5, 8, 10, 6250000, 31250, 20, 512, 31250000, 25, 32, 62500, 40, 62500000, 1280, 50, 3125, 1000000, 80000, 125000, 80, 2560, 156250, 16, 100, 125000000, 6250, 625, 125, 128, 50000000, 250000, 250000000, 160, 312500, 20000, 200, 3906250, 6400, 1250000, 12500, 40000000, 1250, 16000, 256, 640, 3125000, 15625, 100000000, 10000, 320000, 500000, 15625000, 2000000, 78125, 500000000, 8000, 25000000, 50000, 1600000, 200000000, 400, 1953125, 625000, 3200, 20000000, 40000, 1562500, 5000, 160000, 320, 7812500, 12800, 4000, 12500000, 25000, 64, 800000, 1600, 10000000, 100000, 781250, 2500, 2000, 64000, 400000, 250, 800, 5000000, 390625, 1000, 32000, 200000, 2500000, 500])


print sorted(s)[:10]

primes = set()
acc = set()
for r in sorted(s)[:20]:
    print r, len(primes)
    pr = get_prime_factors((10 ** r - 1) / 9)
    primes.update(pr)
    if len(primes)>= 40:
        break

print len(primes), sorted(primes)



###Decimal (10) ** Decimal(10 ** 9))

##print 'coucou'


##from primeutils import *
##from decimal import *


#import math

#print int(math.sqrt(10 ** 9)) + 1
#acc = []
#test = 1
#p = []
#for r in xrange(2, int(math.sqrt(10 ** 9)) + 1):
    #if is_prime(r):
        #p.append(r)

#print p


#print get_prime_factors_and_powers(10**9-1, p)


#print acc, test
#print 'coucou'

#r = 10 ** 9
#acc = 1
#while (r % 2 == 0):
    #acc *= 2
    #r //= 2
#print acc, r

#t = (10 ** acc) ** r
#t = t-1

#for p in pri:
    #print p
    #print t % p

    #print acc
            ##acc.append(r+1)
#print len(acc)
#pri =  sorted(acc)
