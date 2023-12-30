def add_node(v):
    if v not in graph:
        graph[v] = []

def add_edge(v1, v2, w):
    if v1 == v2:
        return
    if v1 not in graph:
        print('node', v1, 'not in graph')
        return
    if v2 not in graph:
        print('node', v2, 'not in graph')
        return
    graph[v1].append((v2, w))
    graph[v2].append((v1, w))

def delete_node(v):
    if v not in graph:
        return
    nodes = graph[v]
    graph.pop(v)
    for node in nodes:
        for n in graph[node[0]]:
            if n[0] == v:
                graph[node[0]].remove(n)
                break

def delete_edges(v1, v2):
    if v1 not in graph:
        print('node', v1, 'not in graph')
        return
    if v2 not in graph:
        print('node', v2, 'not in graph')
        return
    for node in graph[v1]:
        if node[0] == v2:
            graph[v1].remove(node)
            break
    for node in graph[v2]:
        if node[0] == v1:
            graph[v2].remove(node)
            break
def recursion_DFS(v, visited):
    if v not in visited:
        print(v, end='->')
        visited.add(v)
        for u in graph[v]:
            recursion_DFS(u[0], visited)
def iterative_DFS(v):
    stack = []
    visited = set()
    stack.append(v)
    while stack:
        u = stack.pop()
        if u not in visited:
            print(u, end='->')
            visited.add(u)
            for node in graph[u]:
                stack.append(node[0])

graph = {}
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_edge('A', 'B', 10)
add_edge('A', 'C', 8)
add_edge('B', 'C', 12)
add_edge('D', 'C', 12)
add_edge('D', 'A', 2)
add_edge('E', 'C', 15)
print(graph)
visited = set()
recursion_DFS('E', visited)
print()
iterative_DFS('E')
