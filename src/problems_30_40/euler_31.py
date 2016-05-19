import copy

l = [i for i in range(1,101)]
ACC = []


def binpacking(li, value):
    """"""
    if sum(x for x in li) > value:
        return None
    if sum(x for x in li) == value:
        return li
    for x in l:
        s = copy.deepcopy(li)
        if s and s[len(s) - 1] < x:
            continue
        s.append(x)
        r = binpacking(s, value)
        if r and sorted(r) not in ACC:
            ACC.append(sorted(r))
            print(len(ACC))
            if len(ACC) % 20 == 0:
                print(len(ACC[len(ACC) - 1]))

    return None

s = binpacking([], 100)
print('#', len(ACC))
