import itertools

s = 0
l = []
for pan in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    if int("".join(str(i) for i in pan[1:4])) % 2 == 0 and \
        int("".join(str(i) for i in pan[2:5])) % 3 == 0 and \
        int("".join(str(i) for i in pan[3:6])) % 5 == 0 and \
        int("".join(str(i) for i in pan[4:7])) % 7 == 0 and \
        int("".join(str(i) for i in pan[5:8])) % 11 == 0 and \
        int("".join(str(i) for i in pan[6:9])) % 13 == 0 and \
        int("".join(str(i) for i in pan[7:])) % 17 == 0:

            s += int("".join(str(i) for i in pan))
            l .append(int("".join(str(i) for i in pan)))

    if int("".join(str(i) for i in pan)) == 1406357289:
        print pan
        print int("".join(str(i) for i in pan[1:4])) % 2 == 0
        print int("".join(str(i) for i in pan[2:5])) % 3 == 0
        print int("".join(str(i) for i in pan[3:6])) % 5 == 0
        print int("".join(str(i) for i in pan[4:7])) % 7 == 0
        print int("".join(str(i) for i in pan[5:8])) % 11 == 0
        print int("".join(str(i) for i in pan[6:9])) % 13 == 0
        print int("".join(str(i) for i in pan[7:])) % 17 == 0

print 'coucou'
print s, l
