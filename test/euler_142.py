squares = set()

for i in xrange(1, 10 ** 7):
    if i % 1000000 == 0:
        print i
    squares.add(i ** 2)