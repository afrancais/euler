import math
from decimal import *

getcontext().prec = 40

def area_triangle(a, b, c):
    return ((a + b - c) * (a - b + c) * (b - a + c) *(a + b + c)).sqrt() / 4




acc = 0
for i in xrange(1, ((10 ** 9) / 3) + 1):
    if i % 10000 == 0:
        print '%d / %d' % (i, ((10 ** 9) / 3)), acc

    a = b = i
    c = i + 1
    t = area_triangle(Decimal(a), Decimal(b), Decimal(c))
    if not t - t.to_integral():
        print (a, b, c), a + b + c
        acc += a + b + c

print acc
