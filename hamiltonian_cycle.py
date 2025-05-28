def find_hamiltonian_cycle(graph):
    n = len(graph)
    path = [0]

    def is_valid(v, pos):
        # Sprawdza, czy wierzchołek v może być dodany do ścieżki na pozycji pos
        if graph[path[pos-1]][v] == 0:
            return False
        if v in path:
            return False
        return True

    def backtrack(pos):
        if pos == n:
            # sprawdza czy ostatni wierzchołek łączy się z pierwszym (pełny cykl)
            return graph[path[pos-1]][path[0]] == 1
        for v in range(1, n):
            if is_valid(v, pos):
                path.append(v)
                if backtrack(pos + 1):
                    return True
                path.pop()
        return False

    if backtrack(1):
        path.append(path[0])  # zamknięcie cyklu
        return path
    else:
        return None
