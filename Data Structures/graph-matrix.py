def add_node(node):
    global node_count
    if node not in nodes:
        node_count += 1
        nodes.append(node)
        for row in graph:
            row.append(0)
        new_row = []
        for i in range(node_count):
            new_row.append(0)
        graph.append(new_row)
def print_graph():
    global node_count
    print('  ', end='')
    for i in range(node_count):
        print(nodes[i], end=' ')
    print()
    for i in range(node_count):
        print(nodes[i], end=' ')
        for j in range(node_count):
            print(graph[i][j], end=' ')
        print()
def add_edges(v1, v2, w):
    if v1 == v2:
        return
    if v1 not in nodes:
        print('node', v1, 'not in list nodes')
        return
    if v2 not in nodes:
        print('node', v2, 'not in list nodes')
        return
    index_v1 = nodes.index(v1)
    index_v2 = nodes.index(v2)
    graph[index_v1][index_v2] = w
    graph[index_v2][index_v1] = w

def delete_node(v):
    global node_count
    if v in nodes:
        index = nodes.index(v)
        nodes.pop(index)
        node_count -= 1
        graph.pop(index)
        for row in graph:
            row.pop(index)
def delete_edges(v1, v2):
    if v1 == v2:
        return
    if v1 not in nodes:
        print('node', v1, 'not in list nodes')
        return
    if v2 not in nodes:
        print('node', v2, 'not in list nodes')
        return
    index_v1 = nodes.index(v1)
    index_v2 = nodes.index(v2)
    graph[index_v1][index_v2] = 0
    graph[index_v2][index_v1] = 0
def recursion_DFS(v, visited):
    if v not in visited:
        visited.add(v)
        print(v, end=' ')
        index_v = nodes.index(v)
        global node_count
        for i in range(node_count):
            if graph[index_v][i]:
                recursion_DFS(nodes[i], visited)
    # print(v)
    # index_v = nodes.index(v)
    # visited.add(v)
    # print(visited)
    # for i in range(node_count):
    #     if (graph[index_v][i] != 0) & (nodes[i] not in visited):
    #         recursion_DFS(nodes[i], visited)
def iterative_DFS(v):
    visited = set()
    stack = []
    global node_count
    stack.append(v)
    while stack:
        u = stack.pop()
        if u not in visited:
            print(u, end='->')
            visited.add(u)
            index_u = nodes.index(u)
            for i in range(node_count):
                if graph[index_u][i]:
                    stack.append(nodes[i])
def BFS(v):
    visited = set()
    queue = []
    queue.append(v)
    global node_count
    while queue:
        u = queue.pop(0)
        if u not in visited:
            print(u, end='->')
            visited.add(u)
            index_u = nodes.index(u)
            for i in range(node_count):
                if graph[index_u][i]:
                    queue.append(nodes[i])

graph = []
nodes = []
node_count = 0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')
add_node('F')

add_edges('C', 'A', 5)
add_edges('D', 'A', 2)
add_edges('D', 'E', 5)
add_edges('B', 'E', 1)
add_edges('B', 'C', 3)
add_edges('D', 'C', 6)
add_edges('F', 'A', 6)


print_graph()
recursion_DFS('A', set())
print()
iterative_DFS('A')
print()
BFS('A')