from fractions import *

acc = set()

for i in range(2, 12001):
    if i % 100 == 0:
        print i
    for j in range(1, i):
        acc.add(Fraction(j, i))

acc = sorted(list(acc))
i = acc.index(Fraction(1,3))
j = acc.index(Fraction(1,2))
print i, j, j-i

