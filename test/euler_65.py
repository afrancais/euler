
from fractions import *

def gen():
    k = 0
    while True:
        yield 2
        yield 1
        while True:
            k += 1
            yield 2 * k
            yield 1
            yield 1

g = gen()
conv = []
for i in range(100):
    conv.append(g.next())

acc = 0
for i in reversed(conv):
    if acc:
        acc = i + Fraction(1/acc)
    else:
        acc = i
    print i

print acc, sum(int(l) for l in str(acc.numerator))
#for i in range(1,10):
    #r = 2
    #s = Fraction(1/2)
    #print i
    #for j in range(1, i):
        #s = g.next() + s
        #s = Fraction(1, s)
    #print i, r + s
    #if len(str((r + s).numerator)) > len(str((r + s).denominator)):
        #acc += 1
    #print '#'*30
#print acc





#
