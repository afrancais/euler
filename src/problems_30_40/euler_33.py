
from decimal import *


for i in range(10,100):
    for j in range(10,100):
        r = Decimal(i) / Decimal(j)
        if r < 1:
            l1 = i % 10
            l2 = i / 10
            if l1 != 0:
                if str(l1) in str(j):
                    n = l2
                    m = str(j).replace(str(l1),'')
                    if m:
                        m= int(m)
                        if m != 0:
                            q = Decimal(n) / Decimal(m)
                            if r == q:
                                print i, j
            if l2 != 0:
                if str(l2) in str(j):
                    n = l1
                    m = str(j).replace(str(l1),'')
                    if m:
                        m= int(m)
                        if m != 0:
                            q = Decimal(n) / Decimal(m)
                            if r == q:
                                print i, j
