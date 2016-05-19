c = dict()
c[0] = dict()
c[0][0] = 1


def euler_15():
    for i in range(1, 41):
        c[i] = dict()
        c[i][0] = 1
        c[0][i] = 1
        print(i)
        for j in range(1, i):
            c[i][j] = c[i - 1][j - 1] + c[i - 1][j]
        c[i][i] = 1

    print(c)
