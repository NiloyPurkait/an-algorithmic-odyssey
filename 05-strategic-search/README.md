# Module 5: Strategic Search & Metaheuristics

This module is about searching when brute force is too expensive. An adversary or a combinatorial space makes the full tree impossible to expand, so the student learns to prune it, sample it, or let many simple agents explore it together.

## Field

Game theory, adversarial search, metaheuristic optimization, and evolutionary computation.

## Learning Arc

1. [Minimax](00-min-max/min-max.ipynb) searches game trees against a perfect opponent and prunes branches that cannot change the decision.
2. [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) uses random playouts when full search is too large.
3. [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) lets many simple agents reinforce good routes through a hard combinatorial space.
4. [Genetic Algorithms](03-genetic-algorithms/genetic-algorithms.ipynb) evolve a population of candidate solutions through selection, crossover, and mutation.
5. [Dawkins' Biomorphs](04-biomorphs/biomorphs.ipynb) applies the same mutate-and-select engine to a space of visual forms, with a human as the fitness function.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Minimax](00-min-max/min-max.ipynb) | 3/5 | 40 min | Adversarial game tree |
| [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) | 4/5 | 45 min | Sampling search tree |
| [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) | 4/5 | 40 min | Pheromone-reinforced search |
| [Genetic Algorithms](03-genetic-algorithms/genetic-algorithms.ipynb) | 4/5 | 45 min | Population, selection, crossover, mutation |
| [Dawkins' Biomorphs](04-biomorphs/biomorphs.ipynb) | 3/5 | 45 min | Genome, mutation, and selection |

## Why This Module Comes Next

The student now knows exact procedures and data-driven approximation. This module turns to spaces where exhaustive search fails: adversarial games and large combinatorial problems. The recurring move is to trade completeness for a disciplined estimate.

## Checkpoint

Take one hard search problem and compare three strategies on it: prune the tree (Minimax), sample it (MCTS), and let agents explore it (ant colony or a genetic algorithm). Explain how each one scales and where each one fails.
