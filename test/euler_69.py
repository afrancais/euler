from primeutils import *

m = (0, 0)

for i in xrange(2, 10 ** 6 + 1):
    if i % 1000 == 0:
        print i, m
    p = phi(i)
    r = float(i)/p
    if m[1] < r:
        m = (i, r)

print m

