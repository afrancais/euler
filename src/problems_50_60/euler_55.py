import numberutils


r = 0
for i in range(1, 10001):
    j = numberutils.reverse(i)
    n = i + j
    acc = 0
    while not numberutils.palindrome(n):
        n = n + numberutils.reverse(n)
        acc += 1
        if acc > 51:
            print i
            r += 1
            break
    if i % 100 == 0:
        print i

print r
