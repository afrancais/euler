from __future__ import division
from itertools import *

def get_all_braces(a,b,c,d, op1, op2, op3):
    try:
        yield eval('(%s %s %s %s %s %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('%s %s (%s %s %s %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('%s %s %s %s (%s %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('%s %s (%s %s (%s %s %s))' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('%s %s ((%s %s %s) %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('(%s %s %s) %s (%s %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('(%s %s %s %s %s) %s %s' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('((%s %s %s) %s %s) %s %s' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('(%s %s (%s %s %s)) %s %s' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0
    try:
        yield eval('(%s %s (%s %s %s) %s %s)' % (a, op1, b, op2, c, op3, d))
    except:
        yield 0


m = (None, 0)
for a in range (1, 7):
    for b in range(a+1, 8):
        for c in range(b+1, 9):
            for d in range(c+1, 10):

                s = set()
                for p in permutations([a,b,c,d]):
                    for o in combinations_with_replacement(['+', '-', '*', '/'], 3):
                            for oo in permutations(o):
                                for r in get_all_braces(p[0], p[1], p[2], p[3], oo[0], oo[1], oo[2]):
                                    if int(r) > 0 and (isinstance(r, int) or r.is_integer()):
                                        s.add(int(r))
                i = 1
                t = 0
                if (a,b,c,d) == (1,2,3,4):
                    print sorted(list(s))
                for j in sorted(list(s)):
                    if i != j:
                        break
                    i += 1
                    t += 1
                if (a,b,c,d) == (1,2,3,4):
                    print t
                if t > m[1]:
                    m = ((a,b,c,d), t)
                    print a, b, c, d, t, m


print sorted(list(s))
print m