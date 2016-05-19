import math
from decimal import *
getcontext().prec = 250
from fractions import *

m = (0, 0, 0)

for n in xrange(1, 1000+1):#[19, 28, 29, 17]:
    l = []
    ll = list()
    if math.sqrt(n).is_integer():
        continue
    a = Decimal(n).sqrt()
    while True:
        l.append(math.floor(a))
        ll.append(a.quantize(Decimal('0.0000000000000000000000001')))
        a = 1 / (a - Decimal(math.floor(a)))
        if a.quantize(Decimal('0.0000000000000000000000001')) in ll:
            break

    a = None
    print n, l
    if len(l) % 2 == 0:
        l = l + l[1:]
    for i in reversed(l[:-1]):
        if not a:
            a = int(i)
        else:
            a = int(i) + Fraction(1, a)


    print n, a
    if a.numerator > m[1]:
        m = (n, a.numerator, a)
        #print m

print m