import math

triangle = []
f = open('triangle.txt')
for line in f:
    triangle.append(line.strip().split(" "))


best_path = dict()

for i in reversed(range(0, len(triangle))):
    best_path[i] = dict()
    for j in range(0, i + 1):
        v = int(triangle[i][j])
        if (i + 1) in best_path:
            v += max(int(best_path[i+1][j]), int(best_path[i+1][j+1]))
        best_path[i][j] = v


print(best_path[0][0])
