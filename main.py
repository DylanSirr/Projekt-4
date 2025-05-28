#!/usr/bin/env python3
import sys
from creating_graphs import generate_graph, generate_non_hamiltonian_graph
from print_graph import print_graph
from euler_cycle import find_euler_cycle
from hamiltonian_cycle import find_hamiltonian_cycle

def edges_to_adjacency_matrix(edges, n):
    graph = [[0]*n for _ in range(n)]
    for a, b in edges:
        graph[a][b] = 1
        graph[b][a] = 1
    return graph

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ("--hamilton", "--non-hamilton"):
        print("Użycie: ./main.py --hamilton lub ./main.py --non-hamilton")
        return

    mode = sys.argv[1]

    n = int(input("nodes> "))
    if mode == "--hamilton":
        saturation = int(input("saturation> "))
        edges = generate_graph(n, saturation)
    else:
        edges = generate_non_hamiltonian_graph(n)

    print("\n--- Graf ---")
    print_graph(edges, n)

    print("\n--- Cykl Eulera ---")
    euler = find_euler_cycle(edges, n)
    if euler:
        print(" -> ".join(map(str, euler)))
    else:
        print("Brak cyklu Eulera.")

    print("\n--- Cykl Hamiltona ---")
    graph_matrix = edges_to_adjacency_matrix(edges, n)
    hamilton = find_hamiltonian_cycle(graph_matrix)
    if hamilton:
        print(" -> ".join(map(str, hamilton)))
    else:
        print("Brak cyklu Hamiltona.")

if __name__ == "__main__":
    main()
