import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

i = 1

while True:
    d = 2 * i
    t = 3 * i
    q = 4 * i
    c = 5 * i
    s = 6 * i


    if i % 100 ==0:
        print i, d, t, q, c, s

    if not compare(list(str(i)), list(str(d))):
        i += 1
        continue
    if not compare(list(str(i)), list(str(t))):
        i += 1
        continue
    if not compare(list(str(i)), list(str(q))):
        i += 1
        continue
    if not compare(list(str(i)), list(str(c))):
        i += 1
        continue
    if not compare(list(str(i)), list(str(s))):
        i += 1
        continue
    print i, d, t, q, c, s

    break

print 'resultat:', i

