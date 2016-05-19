import math

l = []

for i in range(3, 10000001):
    s = 0
    for j in str(i):
        s += math.factorial(int(j))
    if s == i:
        l.append(i)
    if i % 1000 == 0:
        print i

print l
print sum(l)
