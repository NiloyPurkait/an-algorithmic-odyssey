# Dijkstra's Algorithm

Shortest-path search becomes reliable when edge costs are nonnegative. Dijkstra's algorithm expands certainty outward from the source, settling the nearest unfinished node and relaxing its outgoing edges. The frontier order carries the proof.

## Open

- [dijkstra.ipynb](dijkstra.ipynb)

## What To Watch

- Tentative distances can improve. Settled distances should not.
- The priority queue stores the frontier in order of current best distance.
- Negative edge weights break the greedy argument.
- With a binary heap, the common bound is `O((V + E) log V)`.

## Read Next

- [Dijkstra, A Note on Two Problems in Connexion with Graphs](https://doi.org/10.1007/BF01386390) - original 1959 paper.
- [Princeton Algorithms: Shortest Paths](https://algs4.cs.princeton.edu/44sp/) - implementation context.
- [NetworkX shortest path algorithms](https://networkx.org/documentation/stable/reference/algorithms/shortest_paths.html) - API guide for shortest-path variants.
