s = set()

from primeutils import *

def pascal_triangle_generator():
    r = [1]
    n = 1
    yield r
    while True:
        n += 1
        new_r = []
        for i in range(n):
            if i == 0 or i == n-1:
                new_r.append(1)
            else:
                new_r.append(r[i-1] + r[i])
        r = new_r
        yield r

g = pascal_triangle_generator()
for i in range(51):
    r = g.next()
    s.update(r)
print len(s)
print s
i = 1
acc = 0
for r in s:
    if i % 10 == 0:
        print "%d / %d" % (i, len(s))
    print i
    if not is_square_divided(r):
        acc += r
    i+=1
print acc
