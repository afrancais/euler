import math

r = 0

for i in range(1, 10 ** 6):
    if i % 1000 == 0:
        print i
    acc = [i]
    j = sum(math.factorial(int(l)) for l in str(i))
    while j not in acc:
        acc.append(j)
        j = sum(math.factorial(int(l)) for l in str(j))

    if len(acc) == 60:
        print i, r
        r += 1

print r
