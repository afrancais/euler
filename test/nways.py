from primeutils import *
primes = []
for i in xrange(2, 100):
    if is_prime(i):
        primes.append(i)

print primes

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'memory',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

@cache.cache('nway')
def nway( total, coins):
    """"""
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0
    if total % c == 0: count += 1
    for amount in xrange(0, total, c):
        count += nway(total - amount, coins)
    return count
# main
#print nway( 3, primes)

k = 10 ** 6
for i in xrange(1, 1000):
    r = nway(i, range(1, i+1))
    print i, r
    if i % k == 0:
        break


