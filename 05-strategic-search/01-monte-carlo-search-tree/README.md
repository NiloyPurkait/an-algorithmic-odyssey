# Monte Carlo Tree Search

Monte Carlo Tree Search became prominent in the 2000s, especially through computer Go, where exhaustive search was impractical. Instead of expanding the whole tree, it samples play-outs and uses statistics to decide where to search next. The method turns limited computation into a balance between exploration and exploitation.

## Open

- [monte-carlo-search-tree.ipynb](monte-carlo-search-tree.ipynb)

## What To Watch

- Selection chooses a path through the current tree.
- Expansion adds a new child state.
- Simulation estimates value by rollout.
- Backpropagation updates visit counts and rewards.
- UCT balances high-value moves against underexplored moves.

## Read Next

- [Browne et al., A Survey of Monte Carlo Tree Search Methods](https://doi.org/10.1109/TCIAIG.2012.2186810) - standard survey.
- [Kocsis and Szepesvari, Bandit Based Monte-Carlo Planning](https://aima.cs.berkeley.edu/~russell/classes/cs294/s11/readings/Kocsis%2BSzepesvari%3A2006.pdf) - UCT source paper.
- [Silver et al., Mastering the game of Go with deep neural networks and tree search](https://doi.org/10.1038/nature16961) - AlphaGo paper.
