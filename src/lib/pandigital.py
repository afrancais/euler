import itertools


def is_pandigital(value, i=1, k=9):
    """Is pandigital"""
    s = str(value)
    if len(s) != k - i + 1:
        return False
    for i in range(i, k + 1):
        s = s.replace(str(i), '', 1)
    return not s


def nb_distinct(value):
    """"""
    return set(int(l) for l in str(value))


def get_all_pandigitals(i, k):
    """Return all i-k pandigitals numbers"""
    l = range(i, k + 1)
    return itertools.permutations(l)
