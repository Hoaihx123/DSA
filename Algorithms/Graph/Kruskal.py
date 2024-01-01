class Graph:
    def __init__(self, num):
        self.num = num
        self.graph = []
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
    def findRoot(self, u, ticks):
        cur = u
        while cur != ticks[cur]:
            cur = ticks[cur]
        return cur
    def kruskal(self):
        ticks = [u for u in range(self.num)]
        result = []
        sorted_graph = sorted(self.graph, key=lambda item: item[2])
        e = 0
        i = 0
        while e < self.num - 1:
            u, v, w = sorted_graph[i]
            i += 1
            root_u = self.findRoot(u, ticks)
            root_v = self.findRoot(v, ticks)
            if root_v != root_u:
                result.append([u, v, w])
                e += 1
                ticks[root_u] = root_v
        print(result)

g = Graph(6)
g.addEdge(0, 1, 2)
g.addEdge(0, 3, 1)
g.addEdge(0, 4, 4)
g.addEdge(1, 2, 3)
g.addEdge(1, 3, 3)
g.addEdge(1, 5, 7)
g.addEdge(2, 3, 5)
g.addEdge(2, 5, 8)
g.addEdge(3, 4, 9)
g.kruskal()