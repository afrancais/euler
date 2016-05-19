import math
from decimal import *
getcontext().prec = 250

#a = Decimal(7).sqrt()

#r = math.sqrt(a) - math.floor(math.sqrt(a))
#print r

#l = []
#ll = set()
#for i in range(1, 50):
    #l.append(math.floor(a))
    #ll.add(a.quantize(Decimal('0.000000000000000000000001')))
    #a = 1 / (a - Decimal(math.floor(a)))
    #if a.quantize(Decimal('0.000000000000000000000001')) in ll:
        #break

#l = l[1:]
#print ll
#print l
#l.append(6)
#regex = re.compile(r'(.+ .+)( \1)+')
#match = regex.search(' '.join(str(int(k)) for k in l))

acc = 0
m = 0
for n in xrange(2, 10001):
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
            idx = ll.index(a.quantize(Decimal('0.0000000000000000000000001')))
            break

    r = l[idx:]
    if len(r) > m:
        m = len(r)
    if len(r) % 2 == 1:
        acc += 1
    if n % 100 == 0:
        print n, acc, m


print acc, r