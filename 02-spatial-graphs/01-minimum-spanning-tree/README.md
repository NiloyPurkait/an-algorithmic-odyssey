# Minimum Spanning Tree

A minimum spanning tree connects every vertex with no cycles and minimum total edge weight. Kruskal's algorithm builds it by scanning edges from cheapest to most expensive.

## Open

- [minimum-spanning-tree.ipynb](minimum-spanning-tree.ipynb)

## What To Watch

- A spanning tree on `V` vertices has exactly `V - 1` edges.
- Union-find answers the only question Kruskal needs: would this edge create a cycle?
- The cut property explains why a locally cheap safe edge can be globally safe.

## Read Next

- [Kruskal, On the Shortest Spanning Subtree of a Graph](https://doi.org/10.1090/S0002-9939-1956-0078686-7) - original paper.
- [Princeton Algorithms: Minimum Spanning Trees](https://algs4.cs.princeton.edu/43mst/) - visual and implementation notes.
- [NetworkX minimum_spanning_tree documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html) - reference implementation behavior.
