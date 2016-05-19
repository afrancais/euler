
import pandigital

results = set()

for i in xrange(1, 10000000001):
    if i % 1000 == 0:
        print i, results
    for j in xrange(1, 1000000001):
        r = i * j
        if len(str(i) + str(j) + str(r)) > 9:
            break
        if j % 100 == 0:
            print '#', i, j, r

        if pandigital.is_pandigital(str(i) + str(j) + str(r)):
            print i, j, r
            results.add(r)

print r

