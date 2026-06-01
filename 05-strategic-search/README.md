# Module 5: Strategic Search & Metaheuristics

This module is about searching when brute force is too expensive. An adversary or a combinatorial space makes the full tree impossible to expand, so the student learns to prune it, sample it, or let many simple agents explore it together.

## Field

Game theory, adversarial search, and metaheuristic optimization.

## Learning Arc

1. [Minimax](00-min-max/min-max.ipynb) searches game trees against a perfect opponent and prunes branches that cannot change the decision.
2. [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) uses random playouts when full search is too large.
3. [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) and [Genetic Algorithms](02-ant-colony/genetic-algorithms.ipynb) explore metaheuristics for hard combinatorial search spaces.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Minimax](00-min-max/min-max.ipynb) | 3/5 | 40 min | Adversarial game tree |
| [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) | 4/5 | 45 min | Sampling search tree |
| [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) and [Genetic Algorithms](02-ant-colony/genetic-algorithms.ipynb) | 4/5 | 50 min | Metaheuristic optimization |

## Why This Module Comes Next

The student now knows exact procedures and data-driven approximation. This module turns to spaces where exhaustive search fails: adversarial games and large combinatorial problems. The recurring move is to trade completeness for a disciplined estimate.

## Checkpoint

Take one hard search problem and compare three strategies on it: prune the tree (Minimax), sample it (MCTS), and let agents explore it (ant colony or a genetic algorithm). Explain how each one scales and where each one fails.
