l = []

def p(n):
    """"""
    return n * (3 * n - 1) / 2


for i in xrange(1, 10001):
    l.append(p(i))

r = None
m = 0
for i, a in enumerate(l):
    if i % 100 == 0:
        print i
    for b in l:
        if b >= a:
            break
        if a + b in l and a- b in l:
            if a-b > m:
                m = a-b
                r = (a,b)

print r, m
