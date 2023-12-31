graph = [[0, 3, 0, 2, 0, 0, 0],
         [3, 0, 6, 0, 0, 6, 0],
         [0, 6, 0, 0, 2, 0, 2],
         [2, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 1, 0, 3, 0],
         [0, 6, 0, 0, 3, 0, 3],
         [0, 0, 2, 7, 0, 3, 0]]

def arg_min(s, count):
    n = len(count)
    min = float('inf')
    index = -1
    for i in range(n):
        if (i not in s) & (count[i] < min):
            index = i
            min = count[i]
    return index

def dijkstra(graph, v, u):
    num_nodes = len(graph)
    count = [float('inf')] * num_nodes
    ticks = [-1]*num_nodes
    count[v] = 0
    s = set()
    temp = v
    while temp != u:
        s.add(temp)
        for i in range(num_nodes):
            if (graph[temp][i] != 0) & (i not in s):
                if count[i] > count[temp]+graph[temp][i]:
                    count[i] = count[temp]+graph[temp][i]
                    ticks[i] = temp
        temp = arg_min(s, count)
    if temp == u:
        while temp != v:
            print(temp, end='->')
            temp = ticks[temp]
        print(temp)
        print('length =', count[u])
    else:
        print('no found')

dijkstra(graph, 1, 6)