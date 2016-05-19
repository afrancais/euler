
a = 3
s = 3

for k in xrange(4):
    r = s ** a
    s = r % 10 ** 9
    print k, s, r

print s
print 3 ** (3 ** 27)



