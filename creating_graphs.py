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