for i in xrange(1081000000, 2*10**9):
    s = str(i ** 2)
    if i % 1000000 == 0:
        print i, s, len(s)
    if len(s) != 19:
        continue
    if s[0] == '1' and s[2] == '2' and s[4] == '3':
        if s[6] == '4' and s[8] == '5' and s[10] == '6' and s[12] == '7' and s[14] == '8':
            print i, s
            if  s[16] == '9' and s[18] == '0':
                print i, s
                break

