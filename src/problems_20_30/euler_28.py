d = dict()
d[1] = 1
i = 3
while i <= 1001:
    d[i] = d[i - 2] + 4*i*i  - (i-1) - 2*(i-1) - 3*(i-1)
    i +=2

print d

