
from decimal import *

cubes = dict()

for i in xrange(1, 100000):
    if i % 100 == 0:
        print i
    r = i ** 3
    k = tuple(sorted(l for l in str(r)))
    try:
        cubes[k].append(i)
    except:
        cubes[k] = [i]

results = []
for k, v in cubes.iteritems():
    if len(v) == 5:
        results.extend(v)

print results, min(results), min(results) ** 3










#max_acc = 0
#t = 0

#for i in cubes:
    #tmp = str(i)
    #acc = 0
    #s = set()
    #for t in
    #for p in itertools.permutations(tmp):
        #k = int(''.join(str(l) for l in p))
        #if len(str(k)) != len(tmp):
            #continue
        #if k == p:
            #continue
        #c = Decimal(k) ** Decimal(1.0 / 3)
        #if c in cubes:
            #if p in s:
                #continue
            #s.add(p)
            #acc += 1

        #if acc == 5:
            #print i, s
            #break

    #if max_acc < acc:
        #max_acc = acc
    #if acc == 5:
        #print i, s
        #break
    #t += 1
