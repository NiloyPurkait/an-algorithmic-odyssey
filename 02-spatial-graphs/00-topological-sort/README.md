# Topological Sort

Dependency ordering appears in build systems, prerequisite chains, project schedules, and compilers. Kahn's 1962 algorithm gave a clean way to repeatedly remove ready nodes from a directed acyclic graph. Topological sort exposes the difference between a constrained order and a cycle that makes any order impossible.

## Open

- [topological-sort.ipynb](topological-sort.ipynb)

## What To Watch

- In-degree counts unmet prerequisites.
- Kahn's algorithm repeatedly removes nodes whose in-degree is zero.
- A leftover node after the queue empties is evidence of a cycle.

## Read Next

- [Kahn, Topological Sorting of Large Networks](https://dl.acm.org/doi/10.1145/368996.369025) - original algorithm paper.
- [Communications of the ACM: Topological Sorting of Large Networks](https://cacm.acm.org/research/topological-sorting-of-large-networks/) - stable publication page.
- [NetworkX topological_sort documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.dag.topological_sort.html) - library behavior and exceptions.
