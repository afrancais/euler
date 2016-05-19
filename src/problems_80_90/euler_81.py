

import math

matrix = []
f = open('matrix.txt')
for line in f:
    matrix.append(line.strip().split(","))

best_path = dict()
for i in reversed(range(0, len(matrix))):
    best_path[i] = dict()
    for j in reversed(range(0, len(matrix))):
        if i == 79 and j > 70:
            print i, j, int(matrix[i][j])
        v = int(matrix[i][j])
        if (i + 1) in best_path and j+1 in best_path[i]:
            v += min(int(best_path[i+1][j]), int(best_path[i][j+1]))
        elif (i + 1) in best_path:
            v += int(best_path[i+1][j])
        elif (j+1) in best_path[i]:
            v += int(best_path[i][j+1])
        if i == 79 and j > 70:
            print i, j, v
        best_path[i][j] = v

print best_path[0][0]
