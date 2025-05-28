from collections import defaultdict

def build_adjacency_list(edges, n):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def find_euler_cycle(edges, n):
    graph = build_adjacency_list(edges, n)
    stack = [0]
    path = []

    while stack:
        v = stack[-1]
        if graph[v]:
            u = graph[v].pop()
            graph[u].remove(v)
            stack.append(u)
        else:
            path.append(stack.pop())

    if len(path) == len(edges) + 1:
        return path[::-1]
    else:
        return None
