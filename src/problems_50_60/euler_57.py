from fractions import *

acc = 0
for i in range(1,1001):
    r = 1
    s = Fraction(1/2)
    print i
    for j in range(1, i):
        s = 2 + s
        s = Fraction(1, s)
    print i, r + s
    if len(str((r + s).numerator)) > len(str((r + s).denominator)):
        acc += 1
    print '#'*30
print acc



