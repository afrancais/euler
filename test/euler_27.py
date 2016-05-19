r = None
s = None

import math

def is_prime(i):
    for j in range(2, int(math.sqrt(abs(i)))):
        if i % j == 0:
            return False
    return True

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        v = None
        while not v or is_prime(v):
            v = n*n + a*n + b
            n += 1
        if not s or s < n:
            s = n
            r = (a,b)
        if a % 100 == 0 and b % 100 ==0:
            print a, b
print r,s

def divideByAll(value, m):
        for i in range(1,m):
            if value % i != 0:
                return False
        return True
