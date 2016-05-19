import primeutils

def rad(n):
    r = 1
    primes = primeutils.get_prime_factors_and_powers(n)
    for p,f in primes:
        r *= p
    return r

l = list()

for i in xrange(1, 100001):
    if i % 1000 == 0:
        print i
    l.append((i, rad(i)))

print len(l)
print sorted(l, key=lambda x: x[1])[9998:10005]
