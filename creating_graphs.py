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

def make_even(edges, n):
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
