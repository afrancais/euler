from functools import lru_cache


from lib.prime import *
primes = []
n = 0
while True:
    g = postponed_sieve()
    if n >= 100:
        break
    primes.append(next(g))

print(primes)


@lru_cache(maxsize=128 * 128 * 128)
def nway(total, coins):
    """"""
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0
    if total % c == 0: count += 1
    for amount in range(0, total, c):
        count += nway(total - amount, coins)
    return count
# main
#print nway( 3, primes)

k = 10 ** 6
for i in range(1, 1000):
    r = nway(i, range(1, i + 1))
    print(i, r)
    if i % k == 0:
        break


