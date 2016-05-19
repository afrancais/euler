s = 0
m = 0

sols = dict()

for p in range(0, 1000):
    temp = 0
    sols[p] = []
    for a in range(1, p):
        b = float(p * p - 2 * a * p) / float(2 * (p - a ))
        if a < b and b.is_integer():
            temp += 1
            sols[p].append((a, b, p-a-b))
    if temp > m:
        s = p
        m = temp
        print p, sols[p]

print p, m
