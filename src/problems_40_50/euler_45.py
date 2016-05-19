T = dict()

P = dict()

H = dict()


for i in range(2, 100000):

    t = i * (i + 1) / 2
    p = i * (3 * i - 1) / 2
    h = i * (2 * i - 1)

    T[t] = i
    P[p] = i
    H[h] = i

    if i == 285:
        print t, p, h
    if t in P and t in H and t != 40755:
        print t, i, P[t], H[t]
        break
    if p in T and p in H and p != 40755:
        print p, i, T[p], H[p]
        break
    if h in H and h in T and h != 40755:
        print p, i, T[h], P[h]
        break
