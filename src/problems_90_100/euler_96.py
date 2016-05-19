
l = ['003020600',
'900305001',
'001806400',
'008102900',
'700000008',
'006708200',
'002609500',
'800203009',
'005010300']


sudoku = []
for line in l:
    sudoku.append([int(i) for i in line])


for a in range(20):
    for i in range(9):
        for j in range(9):
            if sudoku[j][i] == 0:
                p = set([1,2,3,4,5,6,8,7,9])
                n = set()
                for k in range(9):
                    if sudoku[j][k]:
                        n.add(sudoku[j][k])
                    if sudoku[k][i]:
                        n.add(sudoku[k][i])
                r = p - n
                if len(r) == 1:
                    p = r.pop()
                    print a, i, j, p
                    sudoku[j][i] = p
                else:
                    print j, i, r

print sudoku