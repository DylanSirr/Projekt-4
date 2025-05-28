#!/usr/bin/env python3
import argparse
from creating_graphs import generate_graph, generate_non_hamiltonian_graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--hamilton", action="store_true", help="Generuj graf Hamiltonowski")
    parser.add_argument("--non-hamilton", action="store_true", help="Generuj graf nie-Hamiltonowski")

    args = parser.parse_args()

    if args.hamilton:
        n = int(input("nodes> "))
        if n <= 10:
            print("Liczba wierzchołków musi być większa niż 10")
            return
        saturation = int(input("saturation> "))
        if saturation not in (30, 70):
            print("Nasycenie musi być 30 lub 70")
            return
        edges = generate_graph(n, saturation)
        print("Graf Hamiltonowski (lista krawędzi):")
        for e in sorted(edges):
            print(e)

    elif args.non_hamilton:
        n = int(input("nodes> "))
        saturation = 50
        edges = generate_non_hamiltonian_graph(n, saturation)
        print("Graf nie-Hamiltonowski (lista krawędzi):")
        for e in sorted(edges):
            print(e)

    else:
        print("Podaj argument --hamilton lub --non-hamilton")

if __name__ == "__main__":
    main()
