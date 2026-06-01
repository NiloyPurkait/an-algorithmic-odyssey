# Module 2: Spatial Navigation & Graph Traversal

Graphs are how computers reason about connected things: maps, dependencies, networks, flows, regions, and routes. This module moves from simple directed structure to weighted paths, geometric neighborhoods, matrix-based reasoning, and capacity-constrained movement.

## Field

Network science, logistics, computational geometry, spatial data structures, and operations research.

## Learning Arc

1. [Topological Sort](00-topological-sort/topological-sort.ipynb) introduces directed acyclic graphs and dependency order.
2. [Minimum Spanning Tree](01-minimum-spanning-tree/minimum-spanning-tree.ipynb) uses greedy choices to connect everything cheaply.
3. [Dijkstra](02-dijkstra/dijkstra.ipynb) finds shortest paths from one source in a weighted graph.
4. [A*](03-a-star/a-star.ipynb) adds heuristics: a disciplined way to estimate remaining cost without losing correctness.
5. [Voronoi Diagrams and Delaunay Triangulation](04-voronoi-delaunay/voronoi-delaunay.ipynb) turns continuous coordinates into territories and natural-neighbor graphs.
6. [Floyd-Warshall](05-floyd-warshall/floyd-warshall.ipynb) shifts to all-pairs shortest paths with a dynamic programming matrix.
7. [Edmonds-Karp](06-edmonds-karp/edmonds-karp.ipynb) finishes with flow, residual graphs, bottlenecks, and cuts.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Topological Sort](00-topological-sort/topological-sort.ipynb) | 2/5 | 30 min | DAG dependency order |
| [Minimum Spanning Tree](01-minimum-spanning-tree/minimum-spanning-tree.ipynb) | 3/5 | 40 min | Greedy graph connection |
| [Dijkstra](02-dijkstra/dijkstra.ipynb) | 3/5 | 40 min | Weighted shortest path |
| [A*](03-a-star/a-star.ipynb) | 3/5 | 40 min | Heuristic graph search |
| [Voronoi and Delaunay](04-voronoi-delaunay/voronoi-delaunay.ipynb) | 3/5 | 45 min | Spatial regions and natural-neighbor graph |
| [Floyd-Warshall](05-floyd-warshall/floyd-warshall.ipynb) | 4/5 | 45 min | All-pairs distance matrix |
| [Edmonds-Karp](06-edmonds-karp/edmonds-karp.ipynb) | 4/5 | 50 min | Residual flow network |

## Why This Module Comes Next

The student now knows loops and tables. This module gives those mechanics a spatial form: nodes, edges, territories, routes, and constraints.

## Checkpoint

Design a small delivery network. Use Voronoi regions to assign each address to its nearest depot, a spanning tree to connect every stop cheaply, Dijkstra or A* to route one driver, Floyd-Warshall to compare all route pairs, and Edmonds-Karp to reason about capacity bottlenecks.
