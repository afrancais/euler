
acc = 0

for i in range(1,100):
    for j in range(1, 100):
         r = j ** i
         if len(str(r)) == i:
             print i, r
             acc += 1

print acc
