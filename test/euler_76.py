#import copy

#l = [i for i in reversed(range(1,101))]
#ACC = []

#print l

#def binpacking(li, value):
    #""""""
    #if sum(x for x in li) > value:
        #return None
    #if sum(x for x in li) == value:
        #return li
    #for x in l:
        #s = copy.deepcopy(li)
        #if s and s[len(s)-1] > x:
            #continue
        #s.append(x)
        #r = binpacking(s, value)
        #if r and sorted(r) not in ACC:
            #ACC.append(sorted(r))
            #if len(ACC) % 1000 == 0:
                #print
                #print len(ACC)
                #print len(ACC[len(ACC)-1])
                #print ACC[len(ACC)-1]
                #print
    #return None

#s = binpacking([], 100)
#print '#', len(ACC)
#

from mctools import Cached

@Cached
def nway(total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0
    if total % c == 0: count += 1
    for amount in xrange( 0, total, c):
        count += nway(total - amount, coins)
    return count
# main
N = 100
print nway(N, tuple(range(1, N))) # 265 ms
