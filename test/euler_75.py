#r = 0
#for i in xrange(0, 1500000, 6):
    #acc = set()
    #for c in xrange(i/3, i/2):
        #for b in xrange(c/2, c):
            #a = i - b - c
            #if a > c:
                #continue
            #if a > b:
                #continue
            #if a ** 2 + b ** 2 == c ** 2:
                #acc.add(tuple(sorted([a, b, c])))
                #if len(acc) > 1:
                    #break
    #if len(acc) == 1:
        #r+=1
        #print i
    #if i % 10000 == 0:
        #print i, r

#print r


#r = dict()
#import math

#for a in xrange(1, 500000):
    #for b in range(a, 700000):
        #c = math.sqrt( a ** 2 + b ** 2 )
        #if a% 10 == 0and b % 10000 == 0:
            #print a, b, c
        #if a + b + c > 1500000:
            #print 'Stop at %d, %d, %.2f' % (a, b, c)
            #break
        #if c.is_integer():
            #c = int(c)
            #try:
                #r[a+b+c].add(tuple(sorted([a, b, c])))
            #except:
                #r[a+b+c] = set()
                #r[a+b+c].add(tuple(sorted([a, b, c])))


#s = []
#for k, v in r.iteritems():
    #if len(v) == 1:
        #s.append(k)

#print len(s), s
import math
import copy

seed = [(3, 13)]

r = dict()

for v in xrange(1, 1000):
    for u in xrange(v + 1, 1000):
        a = 2 * u * v
        b = u ** 2 - v ** 2
        c = int(math.sqrt(a ** 2 + b ** 2))
        if a + b + c > 1500000:
            print v, u, a, b, c, a + b + c
            break
        else:
            try:
                r[a + b + c].add(tuple(sorted([a, b, c])))
            except:
                r[a + b + c] = set()
                r[a + b + c].add(tuple(sorted([a, b, c])))

s = copy.deepcopy(r)

acc = 0
for k, v in s.iteritems():
    for t in v:
        b = 2
        a = b * sum(t)
        while a <= 1500000:
            try:
                r[a].add((b*t[0], b*t[1], b*t[2]))
            except:
                r[a] = set()
                r[a].add((b*t[0], b*t[1], b*t[2]))
            b += 1
            a = b * sum(t)


for k, v in r.iteritems():
    if len (v) == 1:
        acc+=1

print acc