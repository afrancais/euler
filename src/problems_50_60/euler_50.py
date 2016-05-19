import primeutils

l = []
r = None
m = 0
acc = None

for i in xrange(2, 1000001):
    if i % 1000 == 0:
        print i
    if primeutils.is_prime(i):
        l.append(i)

print l
print 41 in l

for i in xrange(0, len(l)):
    for j in xrange(i+1, len(l)):
        s = sum(x for x in l[i:j])
        if s > 1000000:
            break
        if s in l and len(l[i:j]) > 1:
            print s, l[i:j]
            if len(l[i:j]) > m:
                m = len(l[i:j])
                r = s
                acc = l[i:j]

print r, m, acc

