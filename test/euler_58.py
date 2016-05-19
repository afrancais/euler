import primeutils

d = dict()
d[1] = 1
i = 3

acc = 0
r = 0.0

while not r or r > 10:
    t = 0
    c1 = i ** 2
    c2 = c1 - (i - 1)
    c3 = c2 - (i - 1)
    c4 = c3 - (i - 1)

    if primeutils.is_prime(c1):
        t += 1
    if primeutils.is_prime(c2):
        t += 1
    if primeutils.is_prime(c3):
        t += 1
    if primeutils.is_prime(c4):
        t += 1

    acc += t
    n = 2 * (i - 1) + 1
    r = float(acc) / float(n) * 100.0
    print '%d: %f (%d/%d)' % (i, r, acc, n)
    i += 2


