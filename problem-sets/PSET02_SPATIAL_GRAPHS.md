# Problem Set 2: Spatial Graphs

## Goals

Students should be able to choose the right graph model, trace graph state, prove why local choices are safe, and detect when assumptions fail.

## Problems

### 1. Dependency Planning

Build a directed dependency graph for a project with at least eight tasks.

Deliverables:

- topological order
- visual trace of ready nodes and emitted nodes
- one added edge that creates a cycle
- explanation of why the cycle blocks scheduling

### 2. Minimum Connection Cost

Create a weighted undirected graph with at least seven nodes.

Deliverables:

- MST using Kruskal or Prim
- accepted and rejected edge trace
- total cost
- cut-property proof sketch for one accepted edge

### 3. Shortest Path Duel

Run Dijkstra and A* on the same map.

Deliverables:

- trace of settled or expanded nodes
- final path and cost
- comparison of node expansions
- explanation of what makes the A* heuristic admissible

### 4. Spatial Territories and Natural Neighbors

Create at least 12 two-dimensional sites and compute their Voronoi diagram and Delaunay triangulation.

Deliverables:

- plotted Voronoi territories
- Delaunay natural-neighbor graph
- three user points with nearest-site assignments
- one explanation of where the nearest-site model is useful and where it is too simple

### 5. Matrix All-Pairs Reasoning

Run Floyd-Warshall on a graph with at least five nodes.

Deliverables:

- one intermediate matrix snapshot
- final distance matrix
- explanation of the phase-k invariant

### 6. Flow and Bottlenecks

Design a small shipping, bandwidth, or evacuation network.

Deliverables:

- augmenting-path trace
- bottleneck capacity at each augmentation
- final max flow
- one cut whose capacity matches the max flow

## Reflection

Explain the difference between a dependency graph, a route graph, a geometric-neighbor graph, a similarity graph, and a flow network.
