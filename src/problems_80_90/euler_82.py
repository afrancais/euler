from pygraph.readwrite.dot import write
from pygraph.algorithms.minmax import shortest_path
f = open('matrix_82.txt')

mat = []

for l in f:
    mat.append(map(int, l.split(',')))

from pygraph.classes.digraph import digraph
gr = digraph()

o = "O"
d = "D"
gr.add_nodes([o, d])
for i in range(0, len(mat)):
    for j in range(0, len(mat)):
        r = '%d_%d' % (i,j)
        gr.add_node(r)

for i in range(0, len(mat)):
    for j in range(0, len(mat)):
        r = '%d_%d' % (i,j)
        if j == 0:
            gr.add_edge((o, r), mat[i][j])
        if j == len(mat) -1:
            gr.add_edge((r, d), 0)
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
        if i in (0, 1) and j in (0, 1):
            print r, mat[i][j]

r = shortest_path(gr, o)
print r[1][d]
