# Minimax and Alpha-Beta Pruning

Minimax has roots in John von Neumann's work on game theory, where rational play was studied under direct opposition. In game-tree search, each move is evaluated against the best reply available to the opponent. Alpha-beta pruning keeps the same minimax value while skipping branches that cannot change the decision.

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
