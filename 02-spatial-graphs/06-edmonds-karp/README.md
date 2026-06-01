# Edmonds-Karp Max Flow

Flow problems ask how much can move through a capacitated network. Edmonds-Karp repeatedly finds a shortest augmenting path in the residual graph, pushes the bottleneck amount, and records the reverse choices that make later correction possible. Capacity, conservation, and residual reasoning become visible together.

## Open

- [edmonds-karp.ipynb](edmonds-karp.ipynb)

## What To Watch

- Residual edges record both unused capacity and flow that can be canceled.
- An augmenting path increases flow by its bottleneck capacity.
- Breadth-first search is what gives Edmonds-Karp its polynomial bound.
- The max-flow min-cut theorem gives a certificate that no more flow is possible.

## Read Next

- [Edmonds and Karp, Theoretical Improvements in Algorithmic Efficiency for Network Flow Problems](https://doi.org/10.1145/321694.321699) - original paper.
- [MIT OCW 6.046J Network Flow lecture](https://ocw.mit.edu/courses/6-046j-design-and-analysis-of-algorithms-spring-2015/resources/lecture-13-incremental-improvement-max-flow-min-cut/) - lecture treatment.
- [NetworkX maximum_flow documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.flow.maximum_flow.html) - available algorithms and return format.
