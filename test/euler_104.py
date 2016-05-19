import fibonacci
import pandigital

fibo = fibonacci.fibonacci_last_digits()
k = 2
#while True:
    #r = fibo.next()
    #k += 1

    #if len(str(r)) < 9:
        #continue
    #s = str(r)
    #if k % 100 == 0:
        #print k
    #if pandigital.is_pandigital(s[0:9]):
        #print k, s[0:9]
        #if pandigital.is_pandigital(s[-9:]):
            #print r
            #print
            #print s[0:9]
            #print s[-9:]
            #print
            #print k
            #break


while True:
    r = fibo.next()[-9:]
    k += 1
    if k == 541:
        print r
        print 'trololo'
        print 'lala', pandigital.is_pandigital(r)
    if len(str(r)) < 9:
        continue
    s = str(r)
    if k % 1000 == 0:
        print k
    if pandigital.is_pandigital(s):
        f = str(fibonacci.fibonacci(k))
        print k, s, f[0:9]
        if pandigital.is_pandigital(f[0:9]):
            print r
            print
            print f[0:9]
            print f[-9:]
            print
            print k
            break

#for i in range(3,2760):
    #r = fibo.next()
    #r1 = fibo1.next()
    #if i == 2749:
        #print i, r, r1, str(fibonacci.get_fibonacci(i)).replace('.','')[0:9]

#
