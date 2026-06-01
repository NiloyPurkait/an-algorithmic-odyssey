# Floyd-Warshall

Floyd-Warshall computes all-pairs shortest paths by allowing one more possible intermediate vertex at each phase. It brings dynamic programming back from strings to networks, turning "use earlier answers" into a map between every pair of places.

## Open

- [floyd-warshall.ipynb](floyd-warshall.ipynb)

## What To Watch

- `dist[i][j]` means the best known path from `i` to `j`.
- Phase `k` tests whether paths improve by passing through vertex `k`.
- The recurrence is `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`.
- The `O(V^3)` runtime is often acceptable for small dense graphs.

## Read Next

- [Floyd, Algorithm 97: Shortest Path](https://doi.org/10.1145/367766.368168) - shortest-path formulation.
- [Warshall, A Theorem on Boolean Matrices](https://doi.org/10.1145/321105.321107) - transitive-closure formulation.
- [CP-Algorithms: Floyd-Warshall](https://cp-algorithms.com/graph/all-pair-shortest-path-floyd-warshall.html) - implementation notes and negative-cycle discussion.
