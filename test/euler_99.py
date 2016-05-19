from decimal import *
result = dict()
i = 1
exps = []
f = open('base_exp.txt')
for line in f:
    r = line.strip().split(',')
    a = r[0]
    b = r[1]
    s = Decimal(a) ** Decimal(b)
    exps.append(s)
    result[s] = i
    i += 1

print exps, max(exps), result[max(exps)]
