graph = [[0, 4, 0, 5, 0],
         [0, 0, 1, 0, 6],
         [2, 0, 0, 3, 0],
         [0, 0, 1, 0, 2],
         [1, 0, 0, 4, 0]]

# graph = [[0, 1, 0, 3],
#          [1, 0, 3, 1],
#          [0, 3, 0, 1],
#          [3, 1, 1, 0]]
def get_path(P, nodes, u, v):
    if P[u][v] == v:
        nodes.append(v)
    else:
        nodes = get_path(P, nodes, u, P[u][v])
        nodes = get_path(P, nodes, P[u][v], v)
    return nodes

max_int = 99999
n = len(graph)
for i in range(n):
    for j in range(n):
        if (graph[i][j] == 0) & (i != j):
            graph[i][j] = max_int
P = [[u for u in range(n)] for v in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                P[i][j] = k
nodes = [3, ]
print(get_path(P, nodes, 3, 0))
