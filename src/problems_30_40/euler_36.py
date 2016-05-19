

def palindrome(i):
    return str(i) == str(i)[::-1]

s = 0

for i in range(0, 1000001):
    b = bin(i)[2:]
    if palindrome(i) and palindrome(b):
        print i
        s += i

print s
