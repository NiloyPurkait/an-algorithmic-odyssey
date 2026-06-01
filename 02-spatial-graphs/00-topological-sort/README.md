# Topological Sort

Topological sorting turns prerequisites into a legal order. If no such order exists, the dependency graph contains a directed cycle.

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
