import random

def generate_hamiltonian_cycle(n):
    verts = list(range(n))
    random.shuffle(verts)
    edges = set()
    for i in range(n):
        a = verts[i]
        b = verts[(i+1) % n]
        edges.add(tuple(sorted((a,b))))
    return edges

def make_even_degrees(edges, n):
    deg = [0]*n
    for a,b in edges:
        deg[a] += 1
        deg[b] += 1

    odd = [i for i, d in enumerate(deg) if d % 2 == 1]

    while len(odd) >= 3:
        a,b,c = odd[:3]
        edges.add(tuple(sorted((a,b))))
        edges.add(tuple(sorted((b,c))))
        edges.add(tuple(sorted((c,a))))
        odd = odd[3:]

def generate_graph(n, saturation):
    max_edges = n * (n - 1) // 2
    target_edges = int((saturation / 100) * max_edges)

    if target_edges < n:
        raise ValueError("Podane nasycenie jest za małe, aby graf był spójny")

    edges = generate_hamiltonian_cycle(n)

    while len(edges) < target_edges:
        a,b = random.sample(range(n), 2)
        edges.add(tuple(sorted((a,b))))

    make_even_degrees(edges, n)
    return edges

def generate_non_hamiltonian_graph(n, saturation=50):
    max_edges = n * (n - 1) // 2
    target_edges = int((saturation / 100) * max_edges)
    edges = set()

    while len(edges) < target_edges:
        a,b = random.sample(range(n), 2)
        edges.add(tuple(sorted((a,b))))

    edges = {e for e in edges if 0 not in e}
    return edges
