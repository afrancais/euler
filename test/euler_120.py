import primeutils
import math
from decimal import *

acc = 0
for p in xrange(3, 1001):
    if p % 10 == 0:
        print "%d / 1001" % p
    t = 0
    for k in xrange(1, p**2):
        a = (p - 1) ** k + (p + 1) ** (k)
        r = a % (p ** 2)
        if r > t:
            r = t
    acc += 0
