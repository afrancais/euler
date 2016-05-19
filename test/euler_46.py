import primeutils
import numberutils

l = [2]

for i in range(3,1000001):
    if i % 100 == 0:
        print i
    if i % 2 == 1:
        if not primeutils.is_prime(i):
            print l
            found = False
            for n in l:
                k = i - n
                print k, k/2, numberutils.is_square(k/2)
                if k % 2 == 0 and numberutils.is_square(k/2):
                    found = True
                    break
            if not found:
                print i
                break
        else:
            l.append(i)
