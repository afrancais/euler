from primeutils import *
import itertools
import copy

#primes = list()
#sprimes = set()
#print "Generating sets"
#for i in xrange(3, 10**7):
    #if i % 100000 == 0:
        #print i
    #if primeutils.is_prime(i):
        #primes.append(i)
        #sprimes.add(i)

#print 'Done generating'
k = 0

r1 = list()
r2 = list()
r3 = list()
r4 = list()
r5 = list()

g = prime_gen()
while True:
    k += 1
    c = g.next()
    if k % 1 == 0:
        print k, c, len(r1), len(r2), len(r3), len(r4), len(r5)

    for p1, p2, p3, p4 in r4:
        if is_prime(int(str(c) + str(p1))) and is_prime(int(str(p1) + str(c))) \
            and is_prime(int(str(c) + str(p2))) and is_prime(int(str(p2) + str(c))) \
            and is_prime(int(str(c) + str(p3))) and is_prime(int(str(p3) + str(c))) \
            and is_prime(int(str(c) + str(p4))) and is_prime(int(str(p4) + str(c))):
            r5.append((p1, p2, p3, p4, c))
    if r5:
        break

    for p1, p2, p3 in r3:
        if is_prime(int(str(c) + str(p1)))  and is_prime(int(str(p1) + str(c))) \
            and is_prime(int(str(c) + str(p2)))  and is_prime(int(str(p2) + str(c))) \
            and is_prime(int(str(c) + str(p3))) and is_prime(int(str(p3) + str(c))):
            r4.append((p1, p2, p3, c))

    for p1, p2 in r2:
        if is_prime(int(str(c) + str(p1))) and is_prime(int(str(p1) + str(c))) \
            and is_prime(int(str(c) + str(p2)))  and is_prime(int(str(p2) + str(c))):
            r3.append((p1, p2, c))

    for p in r1:
        if is_prime(int(str(c) + str(p))) and is_prime(int(str(p) + str(c))):
            r2.append((p, c))

    r1.append(c)

print r5




    #ok = True
    #s = copy.deepcopy(s1)
    #s.extend(c)
    #for i in range(1,5):
        #for j in range(0, i):
            #if len(str(s[i]) + str(s[j])) > 7:
                #continue
            #if not int(str(s[i]) + str(s[j])) in primes or not int(str(s[j]) + str(s[i])) in primes:
                #k1 = primeutils.is_prime(int(str(s[j]) + str(s[i])))
                #k2 = primeutils.is_prime(int(str(s[i]) + str(s[j])))
                #if k1:
                    #primes.add(k1)
                #if k2:
                    #primes.add(k2)
                #if not k1 or not k2:
                    #ok = False
                    #break
    #if ok:
        #print s
        #break

#print r

#for i in primes:
    #if k % 1000 == 0:
        #print k, i
    #if i in s1:
        #continue
    #for c in s1:
        #if not int(str(i) + str(c)) in primes or not int(str(c) + str(i)) in primes:
            #k1 = primeutils.is_prime(int(str(i) + str(c)))
            #k2 = primeutils.is_prime(int(str(c) + str(i)))
            ##if k1:
                ###primes.add(k1)
            ##if k2:
                ###primes.add(k2)
            #if not k1 or not k2:
                #ok = False
                #break
    #if ok:
        #s1.add(i)
        #print s1
        #print sum(s1)
        #break
    #k += 1


#
