import sys
import itertools
import primeutils
primes = set()

e = 1
stop = False
while not stop:
    n1 = 10 ** e
    n2 = 10 ** (e+1)
    print 'Iterating from %d to %d' % (n1, n2)
    for i in xrange(n1, n2):
        if i % 10**(e-1) == 0:
            print i
        if primeutils.is_prime(i):
            primes.add(str(i))

    acc = set()
    for p in primes:

        for i in range(1, len(p)):
            for k in itertools.combinations(range(len(p)), i):
                c = 0
                toto = set()
                for n in range(10):
                    r = list(p)
                    for idx in k:
                        r[idx] = str(n)
                    if p == '56003':
                        print p, ''.join(r), i, k, c
                    if ''.join(r) in primes:
                        c += 1
                        toto.add(int(''.join(r)))
                        if c >= 7:
                            print p, ''.join(r), i, k, c
                if len(toto) >= 8:
                    print p
                    stop = True
                    acc.update(toto)

    if acc:
        print sorted(acc), min(acc)
    e += 1
