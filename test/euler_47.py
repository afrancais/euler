import primeutils

print primeutils.get_prime_factors(15)


for i in range(10, 10000000):
    factors = primeutils.get_prime_factors(i)
    factors1 = primeutils.get_prime_factors(i+1)
    factors2 = primeutils.get_prime_factors(i+2)
    factors3 = primeutils.get_prime_factors(i+3)

    if i % 100 == 0:
        print i
        print len(factors), len(factors1), len(factors2), len(factors3)

    if len(factors) != 4 or len(factors1) != 4 or len(factors2) != 4 or len(factors3) != 4:
        continue
    temp = set(factors)
    temp |= set(factors1)
    temp |= set(factors2)
    temp |= set(factors3)

    print i, temp, factors, factors1, factors2, set(factors + factors1 + factors2)
    if len(temp) >= 4:
        print i
        break
