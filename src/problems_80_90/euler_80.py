from decimal import *
import math
getcontext().prec = 105

s = 0
for i in xrange(1, 101):
    r = Decimal(i).sqrt()
    if float(r).is_integer():
        continue
    tmp = str(r).split('.')
    print len(tmp[1]), tmp[1]

    s += sum(int(l) for l in tmp[1][:99]) + int(tmp[0])
    #if int(tmp[99]) >= 5:
        #s += 1

print s
