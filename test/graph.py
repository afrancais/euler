

class Graph:
    """"""

    def __init__(self, oriented=True):
        """"""
        self.oriented = oriented
        self.nodes = set()
        self.edges = dict()
        self.adjacencies = dict()

    def add_edge(self, p1, p2, weight = 1):
        """"""
        if p1 not in self.nodes:
            self.nodes.add(p1)
        if p2 not in self.nodes:
            self.nodes.add(p2)

        try:
            self.adjacencies[p1]
        except:
            self.adjacencies[p1] = []

        if p2 in self.adjacencies[p1]:
            raise Exception("%s is already in %s neightborhood" % (p2, p1))

        try:
            self.adjacencies[p1].append(p2)
        except KeyError:
            self.adjacencies[p1] = [p2]

        self.edges[(p1, p2)] = weight

        if not self.oriented:
            self.add_edge(p2, p1, weight)

    def get_adjacencies_matrix(self):
        """"""
        m = dict()
        print m

    def shortest_path(self, start, end):
        D = {}  # dictionary of final distances
        P = {}  # dictionary of predecessors
        Q = priorityDictionary()   # est.dist. of non-final vert.
        Q[start] = 0

        for v in Q:
            D[v] = Q[v]
        if v == end: break
            for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v
        return (D,P)




g = Graph()
g.add_edge((0,0), (1,1), 1)

print g.adjacencies
print g.edges
