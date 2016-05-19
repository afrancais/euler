#Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
#Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
#Pentagonal	 	P5,n=n(3n1)/2	 	1, 5, 12, 22, 35, ...
#Hexagonal	 	P6,n=n(2n1)	 	1, 6, 15, 28, 45, ...
#Heptagonal	 	P7,n=n(5n3)/2	 	1, 7, 18, 34, 55, ...
#Octagonal	 	P8,n=n(3n2)	 	1, 8, 21, 40, 65, ...

def t(n):
    return n * (n + 1) / 2

def s(n):
    return n ** 2

def p(n):
    return n * (3 * n - 1) / 2

def hx(n):
    return n * (2 * n - 1)

def hp(n):
    return n * (5 * n - 3) / 2

def o(n):
    return n * (3 * n - 2)


def get_successors(k, r):
    results = []
    for l in k:
        if len(str(l)) != 4: continue
        if l / 100 != r: continue
        r = l % 100
        results.append((l, r))
    return results


st = dict()
ss = dict()
sp = dict()
shx = dict()
shp = dict()
so = dict()


for i in xrange(1,150):
    if i % 10 == 0:
        print i, t(i), s(i), p(i), hx(i), hp(i), o(i)

    st[t(i)] = i
    ss[s(i)] = i
    sp[p(i)] = i
    shx[hx(i)] = i
    shp[hp(i)] = i
    so[o(i)] = i

import itertools
#for perm in itertools.permutations(st,ss,sp,shx,shp,so)
    #for a in perm[0]:
        #r = a % 100
        #if len(str(r)) != 2: continue
        #if len(str(a)) != 4: continue
        #l = get_successors(sp, r)
        #for succ, r in l:
            #ll = get_successors(ss, r)
            #for su, r2 in ll:
                #if r2 == a / 100:
                    #print a, succ, su


for perm in itertools.permutations([st,ss,sp,shx,shp,so]):
    for a in perm[0]:
        r1 = a % 100
        if len(str(r1)) != 2: continue
        if len(str(a)) != 4: continue
        for b in perm[1]:
            if len(str(b)) != 4: continue
            if b / 100 != r1: continue
            r2 = b % 100
            if len(str(r2)) != 2: continue
            for c in perm[2]:
                if len(str(c)) != 4: continue
                if c / 100 != r2: continue
                r3 = c % 100
                if len(str(r3)) != 2: continue
                for d in perm[3]:
                    if len(str(d)) != 4: continue
                    if d / 100 != r3: continue
                    r4 = d % 100
                    if len(str(r4)) != 2: continue
                    for e in perm[4]:
                        if len(str(e)) != 4: continue
                        if e / 100 != r4: continue
                        r5 = e % 100
                        if len(str(r5)) != 2: continue
                        for f in perm[5]:
                            if len(str(f)) != 4: continue
                            if f / 100 != r5: continue
                            if f % 100 != a / 100: continue
                            l = sorted([a,b,c,d,e,f])
                            if l[0] in st and l[1] in ss and l[2] in sp and l[3] in shx and l[4] in shp and l[5] in so:
                                print "##"
                            print a, b, c, d, e, f
                            print a%100, b/100
                            print perm[0][a], perm[1][b], perm[2][c], perm[3][d], perm[4][e], perm[5][f]
                            print sum([a, b, c, d, e, f])
        #if k in ss and k in sp:
        #print k, st[k], ss[k], sp[k], shx[k], shp[k], so[k]
        #if k in shx and k in shp and k in so:
            #print 'youhou'

