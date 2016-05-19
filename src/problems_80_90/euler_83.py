from pygraph.readwrite.dot import write
from pygraph.algorithms.minmax import shortest_path
f = open('matrix_83.txt')

mat = []

for l in f:
    mat.append(map(int, l.split(',')))

from pygraph.classes.digraph import digraph
gr = digraph()


for i in range(0, len(mat)):
    for j in range(0, len(mat)):
        r = '%d_%d' % (i,j)
        gr.add_node(r)

for i in range(0, len(mat)):
    for j in range(0, len(mat)):
        r = '%d_%d' % (i,j)
        try:
            gr.add_edge((r, "%d_%d" % (i, j+1)), mat[i][j+1])
        except:
            pass

        try:
            gr.add_edge((r, "%d_%d" % (i-1, j)), mat[i-1][j])
        except:
            pass
        try:
            gr.add_edge((r, "%d_%d" % (i+1, j)), mat[i+1][j])
        except:
            pass
        try:
            gr.add_edge((r, "%d_%d" % (i, j-1)), mat[i][j-1])
        except:
            pass
        if i in (0, 1) and j in (0, 1):
            print r, mat[i][j]
        #gr.add_edge((n, d), mat[j+1][i])

#for i in range(0, len(mat)):
    #for j in range(0, len(mat)):
        #n = '%d_%d' % (i, j)
        #if j >= 1:
            #d = '%d_%d' % (i, j-1)
            #gr.add_edge((n, d), mat[j-1][i])
        #if j < len(mat) - 1:
            #d = '%d_%d' % (i, j+1)
            #gr.add_edge((n, d), mat[j+1][i])
        #if i < len(mat) - 1:
            #d = '%d_%d' % (i+1, j)
            #gr.add_edge((n, d), mat[j][i+1])

#m = 0
#for i in range(len(mat)):
    #r = shortest_path(gr, "%d_0" % i)
    #for j in range(len(mat)):
        #if r[1]['79_%d' % j] < m or not m:
            #m = r[1]['79_%d' % j]
            #print i, m

#print m

#for i in range(0, len(mat)):
    #print r
r = shortest_path(gr, '0_0')
print r[1]['79_79'] + 4445
