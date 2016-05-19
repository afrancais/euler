from scipy.interpolate import lagrange, interp1d

from fractions import *

def u(n):
    return 1 - n + n ** 2 - n ** 3 + n ** 4 - n ** 5 + n ** 6 - n ** 7 + n ** 8 - n ** 9 + n ** 10


def LagrangeInterp(data, x):
    """"""
    #Number of data points
    n=len(data)
    #Number of x points
    nx = len(x)

    #Parse x, y data points
    dx = [d[0] for d in data]
    dy = [d[1] for d in data]

    #Allocate space for L(x)
    L = [0.0]*(nx)

    def b(j,xi):
        """Calculate b_j(x_xi)"""
        v = 1.0
        for k in xrange(n):
            if k != j:
                v *= Fraction((xi-dx[k]),(dx[j]-dx[k]))
        return v

    #Construct L(x)
    for i,xi in enumerate(x):
        #Construct each element of L(x)
        for j in xrange(n):
            L[i] += dy[j]*b(j,xi)

    return L


for i in range(1, 11):
    print u(i)

xs = []
ys = []
t = []
acc = 0
acc2 = 0
for i in range(1, 11):
    xs.append(i)
    ys.append(u(i))
    t.append((i, u(i)))
    l = lagrange(xs, ys)
    L = LagrangeInterp(t, range(1, i+2))
    print i, i+2, L, len(L)
    print l(i+1)
    print
    for j in range(1, 12):
        if u(j) != int(l(j)):
            r = l(j)
            break
    print j, r
    acc += r
    acc2 += round(L[i])

print acc
print acc2




#def lagrange(points, x):
    #for point in points:
#


