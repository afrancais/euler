import primeutils
import math
from decimal import *

g = primeutils.prime_gen()
k = 1

while True:
    if k % 1000 == 0:
        print k
    p = g.next()
    a = (p - 1) ** k + (p + 1) ** (k)
    r = a % (p ** 2)
    if r > 10 ** 10:
        print k, r
        break
    k += 1
