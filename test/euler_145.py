
acc = 0

for i in xrange(1, 10**9):

    if i % 1000 == 0:
        print i, acc
    s = str(i)
    r = int(s[::-1])
    if len(s) != len(str(r)):
        continue
    k = i + r
    reversible = True
    for l in str(k):
        if int(l) % 2 == 1:
            continue
        reversible = False

    if reversible:
        acc += 1

print acc
