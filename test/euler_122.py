
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'memory',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))

@cache.cache('m')
def m(n):
    """"""
    if n == 1:
        return [n]
    else:
        acc = dict()
        for i in range(1, n):
            tmp = set()
            j = n - i
            if i == j:
                tmp.add(i)
                tmp.update(m(i))
            else:
                tmp.add(i)
                tmp.add(j)
                tmp.update(m(j))
                tmp.update(m(j))
            acc[i] = tmp
        r = None
        toto = 999999
        for k, v in acc.items():
            if len(v) < toto:
                r = k
                toto = len(v)
        return acc[r]

r = 0
for i in xrange(1, 16):
    print i, len(m(i)), m(i)
    r += len(m(i))
print r
