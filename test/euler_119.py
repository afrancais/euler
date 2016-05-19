l = []

for i in range(2, 100):
    for j in range(2, 100):
        k = i ** j
        if sum(int(l) for l in str(k)) == i:
            print i, j, k
            l.append(k)


print len(l)
print sorted(l)[29]