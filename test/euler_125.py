import math

from numberutils import palindrome

r = set()
ps = list()
for i in xrange(2, 10 ** 8):
    if i % 1000 == 0:
        print i
    if palindrome(i):
        ps.append(i)


for n, p in enumerate(ps):
    if n % 1000 == 0:
        print n, p
    for i in xrange(1, int(math.sqrt(p)) + 1):
        k = 0
        acc = (i + k) ** 2
        while acc < p:
            k += 1
            acc += (i + k) ** 2

        if acc == p and k:
            r.add((p, (i, k)))
            break


print r
print len(r)
