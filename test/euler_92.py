
acc = 0
for i in xrange(1, 10000000):
    if i % 1000 == 0:
        print i, acc
    k = sum(int(l) ** 2 for l in str(i))
    while k != 89 and k != 1:
        k = sum(int(l) ** 2 for l in str(k))
    if k == 89:
        acc += 1

