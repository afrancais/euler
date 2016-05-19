from pandigital import *
from primeutils import *


g = prime_gen()
k = 1
p = g.next()


s = {
    1: list(),
    2: list(),
    3: list(),
    4: list(),
    5: list(),
    6: list(),
    7: list(),
    8: list(),
    9: list()
}

while p < 987654322:
    if k % 1000 == 0:
        print k, p, len(s[9])
    k += 1
    p = str(p)
    m = len(p)
    for j in range(1, 10-m):
        for l in s[j]:
            t =''.join(l) + p
            if len(nb_distinct(t)) == len(t):
                s[len(''.join(l) + p)].append(t)
    if len(nb_distinct(p)) == len(p):
        s[len(p)].append((p))

    p = g.next()
print len(s[9])

