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


graph = []
nodes = []
node_count = 0
add_node('A')
add_node('B')
add_node('C')
add_node('D')
add_node('E')

add_edges('C', 'A', 5)
add_edges('D', 'A', 2)
add_edges('D', 'E', 5)

delete_node('D')
print_graph()