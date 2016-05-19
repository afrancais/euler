from primeutils import *

primes = list()

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'memory',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

for i in xrange(2, 5 * 10 ** 7):
    if i % 100000 == 0:
        print i
    if is_prime(i):
        primes.append(i)
        if i > 4 * 10 ** 7:
            break


@cache.cache('phi_chain')
def phi_chain(n):
    """"""
    p = PrimeUtils(primes)
    if n == 1:
        return [n]
    return [n] + phi_chain(p.phi(n))

acc = 0
for k, p in enumerate(primes):
    if p > 4 * 10 ** 7:
        break
    if k % 10000 == 0:
        print k, acc
    l = len(phi_chain(p))
    if l == 25:
        acc += p

print acc
