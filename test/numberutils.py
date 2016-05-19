import math

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

cache_opts = {
    'cache.type': 'memory',
}

cache = CacheManager(**parse_cache_config_options(cache_opts))



def reverse(n):
    """Reverse a number"""
    return int(str(n)[::-1])


def palindrome(i):
    """Is the number a palindrome"""
    return str(i) == str(i)[::-1]


def is_square(i):
    """Is the sumber a square"""
    return int(math.sqrt(i)) == math.sqrt(i)

def bouncy(i):
    """Is the number bouncy"""
    last = None
    inc = True
    dec = True
    for l in str(i):
        k = int(l)
        if last is None:
            last = k
        else:
            if k < last:
                inc = False
            elif k > last:
                dec = False
            if not inc and not dec:
                return True
            last = k
    return False


@cache.cache('pgcd', expire=3600)
def pgcd(a, b):
    """ the euclidean algorithm """
    if a < b:
        return pgcd(b, a)
    if b == 0:
        return a
    else:
        return pgcd(b, (a % b))


def is_permutation(n, k):
    """"""
    return sorted(str(n)) == sorted(str(k))

