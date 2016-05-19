from pygraph.classes.graph import graph
from pygraph.algorithms.minmax import *
g = graph()

mat = []

f = open('network.txt')
for l in f:
    mat.append(l.replace('\n', '').split(','))

#mat = [['-', 16, 12, 21,'-','-','-'],
#[16,'-','-',17,20,'-','-'],
#[12,'-','-',28,'-',31,'-'],
#[21,17,28,'-',18,19,23],
#['-',20,'-',18,'-','-',11],
#['-','-',31,19,'-','-',27],
#['-','-','-',23,11,27,'-']]

print mat
m = 0

for i in range(len(mat)):
    g.add_node(i)

for i in range(len(mat)):
    for j in range(i):
        if mat[i][j] == '-':
            continue
        g.add_edge((i,j), wt=int(mat[i][j]))
        m += int(mat[i][j])

print g
acc = 0
r = minimal_spanning_tree(g)

for k, v in r.items():
    if v is None:
        continue
    acc += g.edge_weight((k, v))

print m, acc, m - acc
