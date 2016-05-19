

from itertools import *


#def partition(k, n):
    #""""""
    #if k>n:
        #return 0
    #if k == n:
        #return 1
    #acc = 0
    #for i in range(1, n/k+1):
         #acc += partition(k, n-1)
         #acc += partition(k, n-k)
    #return acc

#print partition(2, 5)



def tilings(bs, ts):
    ways = [1]
    for s in range(1, bs + 1):
        ways.append(sum([ways[s - 1 - size] for size in ts + [1] if s  >= size ]))

    return ways[bs]

print tilings(7, [3,4,5,6,7])
