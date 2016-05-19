from primeutils import *
acc = 0
res = (99999999999,0)
seen = set()
for i in xrange(2, 10 ** 6):
    if i % 1000 == 0:
        print i, res, len(seen)
    #if i in seen:
        #continue
    c = set()
    c.add(i)
    r = sum(divisors(i)) + 1
    if r > 1000000:
        continue
    while r not in c:
        if r > 1000000:
            break
        c.add(r)
        r = sum(divisors(r)) + 1
    seen.update(c)
    if r == i:
        print i, c
        if len(c) >= res[1]:
            if len(c) == res[1]:
                res = (min(min(c), res[0]), res[1])
            else:
                res = (min(c), len(c))


print r
