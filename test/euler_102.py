

def get_equation(a, b):
    """"""
    try:
        d = float(b[1] - a[1]) / (b[0] - a[0])
    except:
        d = 999999
    r = a[1] - d * a[0]
    return d, r


#a = (-340, 495)
#b = (-153, -910)
#c = (835, -947)

a = (-175,41)
b = (-421,-714)
c = (574,-645)


acc = 0
f = open('triangles.txt')
for l in f:
    coords = l.split(',')
    a = (int(coords[0]), int(coords[1]))
    b = (int(coords[2]), int(coords[3]))
    c = (int(coords[4]), int(coords[5]))
    print a, b, c
    d1, r1 = get_equation(a, b)
    d2, r2 = get_equation(a, c)
    d3, r3 = get_equation(b, c)

    k1 = (r1 * ((d1*c[0] + r1) - c[1])) > 0
    k2 = (r2 * ((d2*b[0] + r2) - b[1])) > 0
    k3 = (r3 * ((d3*a[0] + r3) - a[1])) > 0

    if k1 and k2 and k3:
        print a, b, c
        acc += 1

print acc
