from mpmath import *
mp.dps = 101
r = mpf(10) ** mpf('0.5')

tmp = str(r).split('.')[1]
print len(tmp)
