class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num = len(graph)
    def find_min(self, mts):
        min = 9999
        index = []
        for v in mts:
            for u in range(self.num):
                if (u not in mts) & (self.graph[v][u] < min) & (self.graph[v][u] > 0):
                    min = self.graph[v][u]
                    index = [v, u, self.graph[v][u]]
        return index

    def prim(self, u):
        result = []
        mts = [u]
        for i in range(self.num - 1):
            index = self.find_min(mts)
            result.append(index)
            mts.append(index[1])
        print(result)

graph = [[0, 2, 0, 1, 4, 0],
         [2, 0, 3, 3, 0, 7],
         [0, 3, 0, 5, 0, 8],
         [1, 3, 5, 0, 9, 0],
         [4, 0, 0, 9, 0, 0],
         [0, 7, 8, 0, 0, 0]]
graph = Graph(graph)
graph.prim(4)

