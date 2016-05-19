#s = 0
#for i in range(1,4):
    #for j in range(1,3):
        #print i, j, 3*2 / (i * j)
        #s += 3*2 / (i * j)

#print s



a = 100
b = 80
m = 100000000000000000000
r = None


def count_rec(a, b):
    acc = 0
    for i in xrange(1, a+1):
        for j in xrange(1, b+1):
            k = (i, j)
            acc += (b - k[1] + 1)*(a - k[0] + 1)
    return acc


for a in xrange(1, 10000):
    print a, r, m
    for b in xrange(1, a+1):
        k = count_rec(b, a)
        if abs(k - 2000000) < m:
            m = abs(k - 2000000)
            r = (a, b)
        if k > 2000000:
            print a, b
            break

print m, r, r[0] * r[1]
print count_rec(3, 2)
print count_rec(2, 3)
