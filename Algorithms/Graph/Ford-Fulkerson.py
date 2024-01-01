class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.num = len(graph)
    def BFS(self, s, t, ticks):
        queue = []
        visited = [False]*self.num
        queue.append(s)
        while queue:
            u = queue.pop(0)
            if visited[u] == False:
                visited[u] = True
                for i in range(self.num):
                    if (graph[u][i] != 0) & (visited[i]==False):
                        queue.append(i)
                        ticks[i] = u
                        if i == t:
                            return True
        return False
    def FordFulkerson(self, s, t):
        ticks = [-1]*self.num
        count = 0
        while self.BFS(s, t, ticks):
            min = graph[ticks[t]][t]
            cur = ticks[t]
            while cur != s:
                if min > graph[ticks[cur]][cur]:
                    min = graph[ticks[cur]][cur]
                cur = ticks[cur]
            count += min
            cur = t
            while cur != s:
                graph[ticks[cur]][cur] -= min
                graph[cur][ticks[cur]] += min
                cur = ticks[cur]
        return count


graph = [[0, 16, 13, 0, 0, 0],
         [0, 0, 10, 12, 0, 0],
         [0, 4, 0, 0, 14, 0],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4],
         [0, 0, 0, 0, 0, 0]]
g = Graph(graph)
print(g.FordFulkerson(0, 5))
