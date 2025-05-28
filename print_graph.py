def print_graph(edges, n):
    adjacency_list = {i: [] for i in range(n)}
    for a, b in edges:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    for vertex in range(n):
        neighbors = ', '.join(map(str, sorted(adjacency_list[vertex])))
        print(f"{vertex}: {neighbors}")
