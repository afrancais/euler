from decimal import *

r = 1
p = 0
t = 0
u = 0

left  = 0

getcontext().prec = 10000
for i in range(2,1001):
    if i % 10 == 0:
        print i
    d = Decimal(1)/Decimal(i)
    s = str(d).split('.')[1]
    if len(s) < 90:
        continue
    while s and s[0] == '0' and len(s) > 1:
        s = s[1:]

    for j in range(0, len(s)):
        if s[j+1:].startswith(s[0:j+1]):
            if p < j+1:
                p = j+1
                r = i
                t = d
                u = s[0:j+1]
            break
        if s[j+1:].startswith(s[1:j+1]) and j > 1:
            if p < j:
                p = j
                r = i
                t = d
                u = s[1:j+1]
            break
    if j == len(s) - 1:
        left += 1


print p, r, t, u
print
print
print left
