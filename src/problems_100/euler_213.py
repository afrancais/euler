from numpy import zeros


k = 5

m = zeros((k*k, k*k))

print m

for i in range(0, k*k):
    for j in range(0, k*k):
        if i == j:
            m[i][j] = 0
        else:
            if i == 0:
                if j == k-1:
                    m[i][j-1] = float(1)/2
                    m[i+1][j] = float(1)/2
                else:
                    m[i][j-1] = float(1)/3
                    m[i][j+1] = float(1)/3
                    m[i+1][j] = float(1)/3
            elif i == k-1:
                if j == 0:
                    m[i][j+1] = float(1)/2
                    m[i-1][j] = float(1)/2
                else:
                    m[i][j-1] = float(1)/3
                    m[i][j+1] = float(1)/3
                    m[i-1][j] = float(1)/3
            else:
                if j == 0:
                    m[i][j+1] = float(1)/3
                    m[i+1][j] = float(1)/3
                    m[i-1][j] = float(1)/3
                elif j == k-1:
                    m[i][j-1] = float(1)/3
                    m[i+1][j] = float(1)/3
                    m[i-1][j] = float(1)/3
                else:
                    m[i][j-1] = float(1)/4
                    m[i][j+1] = float(1)/4
                    m[i+1][j] = float(1)/4
                    m[i-1][j] = float(1)/4

print m
