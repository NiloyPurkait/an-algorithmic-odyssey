# Minimax and Alpha-Beta Pruning

Minimax evaluates a game tree from the leaves upward. Alpha-beta pruning keeps the minimax answer while skipping branches that cannot change it.

## Open

- [min-max.ipynb](min-max.ipynb)

## What To Watch

- Max nodes choose the best available outcome for the agent.
- Min nodes choose the worst available outcome for the agent.
- Alpha is the best value Max can force so far.
- Beta is the best value Min can force so far.

## Read Next

- [Knuth and Moore, An Analysis of Alpha-Beta Pruning](https://doi.org/10.1016/0004-3702%2875%2990019-3) - classic pruning analysis.
- [Berkeley CS188: Adversarial Search](https://inst.eecs.berkeley.edu/~cs188/textbook/games/minimax.html) - AI-course explanation.
- [Chess Programming Wiki: Alpha-Beta](https://www.chessprogramming.org/Alpha-Beta) - game-engine implementation notes.
