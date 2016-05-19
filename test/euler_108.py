
from __future__ import division
from fractions import *


m = 0
r = 0
for n in xrange(100000, 10000000):
    if n % 1000 == 0:
        print n
    acc = set()
    for i in xrange(n+1, 10000000):
        if i in acc:
            continue
        j = n * i / (i - n)
        if j < i:
            break
        if j.is_integer():
            acc.add(j)

    if len(acc) > m:
        print n, len(acc)
        m = len(acc)
        r = n
        if m > 1000:
            break

print m, r
