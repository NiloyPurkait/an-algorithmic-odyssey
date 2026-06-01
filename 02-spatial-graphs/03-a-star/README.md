# A* Search

A* came from late-1960s AI work by Peter Hart, Nils Nilsson, and Bertram Raphael at Stanford Research Institute, where heuristic search was tied to robot planning. The algorithm combines cost already paid with an admissible estimate of cost still ahead. An informed guess can reduce search without giving up optimality under the right conditions.

## Open

- [a-star.ipynb](a-star.ipynb)

## What To Watch

- `g(n)` is measured from the start.
- `h(n)` is a heuristic, so its assumptions matter.
- Admissible heuristics never overestimate the remaining cost.
- Consistent heuristics keep graph search from reopening settled nodes in the usual formulation.

## Read Next

- [Hart, Nilsson, and Raphael, A Formal Basis for the Heuristic Determination of Minimum Cost Paths](https://doi.org/10.1109/TSSC.1968.300136) - original A* paper.
- [Red Blob Games: Introduction to A*](https://www.redblobgames.com/pathfinding/a-star/introduction.html) - visual explanation.
- [Amit Patel's pathfinding pages](https://theory.stanford.edu/~amitp/GameProgramming/) - grid and game-design notes.
