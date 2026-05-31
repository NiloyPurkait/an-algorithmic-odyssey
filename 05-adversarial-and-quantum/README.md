# Module 5: Strategic Intelligence, Secrets, & Quantum Frontiers

This module studies computation under pressure: opponents, impossible search spaces, encryption, and quantum speedups. It is the end of the arc because it asks students to combine state, trees, probability, optimization, and number theory.

## Field

Game theory, metaheuristics, cryptography, and quantum computing.

## Learning Arc

1. [Minimax](00-min-max/min-max.ipynb) searches game trees against a perfect opponent.
2. [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) uses random playouts when full search is too large.
3. [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) and [Genetic Algorithms](02-ant-colony/genetic-algorithms.ipynb) explore metaheuristics for hard search spaces.
4. [Enigma](03-turing-enigma/enigma.ipynb) models classical encryption as a stateful machine.
5. [RSA](04-rsa/rsa.ipynb) builds public-key cryptography from modular arithmetic and factoring difficulty.
6. [Shor's Algorithm](05-shors-algorithm/shors-algorithm.ipynb) closes the course by showing how quantum period finding threatens the assumption RSA depends on.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Minimax](00-min-max/min-max.ipynb) | 3/5 | 40 min | Adversarial game tree |
| [Monte Carlo Tree Search](01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb) | 4/5 | 45 min | Sampling search tree |
| [Ant Colony Optimization](02-ant-colony/ant-colony.ipynb) and [Genetic Algorithms](02-ant-colony/genetic-algorithms.ipynb) | 4/5 | 50 min | Metaheuristic optimization |
| [Enigma](03-turing-enigma/enigma.ipynb) | 3/5 | 40 min | Rotor state machine |
| [RSA](04-rsa/rsa.ipynb) | 4/5 | 45 min | Modular arithmetic |
| [Shor's Algorithm](05-shors-algorithm/shors-algorithm.ipynb) | 5/5 | 60 min | Quantum period finding |

## Why This Module Ends the Course

The earlier modules supply the parts. This one combines them at the edge: strategy, secrecy, randomness, and quantum structure.

## Checkpoint

Compare limits: solve a small game position with Minimax, discuss why MCTS scales differently, then connect RSA's factoring assumption to Shor's period-finding attack. The goal is to see where classical search holds and where it breaks.
