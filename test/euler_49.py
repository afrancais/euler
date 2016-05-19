import primeutils
import itertools

for i in xrange(1000, 10000):
    if primeutils.is_prime(i):
        cpt = 0
        l = [i]
        for a in itertools.permutations(str(i)):
            j = int("".join(l for l in a))
            if j == i:
                continue
            if j > 1000 and primeutils.is_prime(j) and not j in l:
                if len(l) == 2:
                    delta = l[1] - l[0]
                    if j - l[1] == delta:
                        l.append(j)
                else:
                    l.append(j)
                if len(l) == 3:
                    print l
                    break
