import numberutils

nb = 0

for i in xrange(1, 100000000):
    if numberutils.bouncy(i):
        nb += 1
    if i % 1000 == 0:
        print i, nb, float(nb)/i

    if nb and float(nb) / i >= 0.99:
        print i, nb, float(nb)/i
        break
