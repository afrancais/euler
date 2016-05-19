import itertools

from fractions import *

acc = 0
l = range(1, 16)
for k in range(8, 16):
    for c in itertools.combinations(l, k):
        p = 1
        for i in l:
            if i in c:
                p *= Fraction(1, (i+1))
            else:
                p *= Fraction(i, (i+1))
        print p
        acc += p

print acc
n = acc.numerator
d = acc.denominator

t = n

r = 0
while t < d:
    t += n
    r += 1

print r, t

