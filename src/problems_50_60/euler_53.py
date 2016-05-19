from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'memory',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))


@cache.cache('cnp', expire=3600)
def Cnp(n, p):
    """ Created: 2005.11.05 - Updated:
        Calcul du Cnp - ne pas renseigne l et res lors de l'appel """
    if p == 1:
        return n
    if n == 1:
        return 0
    r = Cnp(n-1, p-1) + Cnp(n-1, p)
    return r


cpt = 0
for i in range(1,101):
    print i
    for j in range(1, i+1):
        if Cnp(i,j) >= 1000000:
            print i, j
            cpt +=1

print cpt

