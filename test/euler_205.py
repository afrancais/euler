import itertools
import random
from fractions import *


def random_combination_with_replacement(iterable, r):
    "Random selection from itertools.combinations_with_replacement(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in xrange(r))
    return tuple(pool[i] for i in indices)

pyramids = dict()
cubics = dict()

r = 0

ppyramids = dict()
acc = 0
for c in itertools.combinations_with_replacement([1, 2, 3, 4], 9):
    l = set()
    l.add(c)
    for s in itertools.permutations(c):
        l.add(s)
    print c, len(l)
    acc += len(l)
    try:
        pyramids[sum(c)] += len(l)
    except:
        pyramids[sum(c)] = len(l)

print acc, 4**9
print pyramids

for i in range(9, 37):
    ppyramids[i] = 0
    for j in range(i+1, 37):
        ppyramids[i] += Fraction(pyramids[i], 4**9)

ppyramids[6] = 1
ppyramids[7] = 1
ppyramids[8] = 1


acc = 0
for c in itertools.combinations_with_replacement([1, 2, 3, 4, 5, 6], 6):
    l = set()
    l.add(c)
    for s in itertools.permutations(c):
        l.add(s)
    print c, len(l)
    acc += len(l)
    try:
        cubics[sum(c)] += len(l)
    except:
        cubics[sum(c)] = len(l)

print cubics
print acc, 6**6

print ppyramids

for i in range(6, 37):
    print i, Fraction(cubics[i], (6**6)) * ppyramids[i]
    r += Fraction(cubics[i], (6**6)) * ppyramids[i]

print r
