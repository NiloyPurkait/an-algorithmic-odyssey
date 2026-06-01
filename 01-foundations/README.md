# Module 1: Foundational Mechanics & Deterministic Logic

Computers become less mysterious when their rules are visible. This module builds the baseline vocabulary: objects, arrays, loops, complexity, deterministic state, simple dynamic programming, greedy choice, trees, recursion, and formal machines.

## Field

Classical computer science and discrete mathematics.

## Learning Arc

1. [Algorithmic Thinking](00-begin-odyssey/algorithmic-thinking.ipynb) and [Sorting](00-begin-odyssey/sorting.ipynb) establish the language of state, cost, data, and comparison.
2. [Antikythera Mechanism](01-antikythera-mechanism/antikythera-mechanism.ipynb) asks what counts as a computer by modeling computation in bronze gears.
3. [Levenshtein Distance](02-levenshtein-distance/levenshtein-distance.ipynb) introduces dynamic programming through a small, visual string matrix.
4. [Gale-Shapley](03-gale-shapley/gale-shapley.ipynb) shows stable convergence using plain logic and repeated proposals.
5. [Huffman Coding](04-huffman-coding/huffman-coding.ipynb) introduces greedy compression and the first major tree structure.
6. [Universal Turing Machine](05-turing-universal-machine/universal-turing-machine.ipynb) asks what a program is at its most mechanical level.
7. [Penrose Tiling](06-penrose-tiling/tiling.ipynb) ends with recursion made visible: a deterministic substitution rule whose tile count grows exponentially with depth.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Algorithmic Thinking](00-begin-odyssey/algorithmic-thinking.ipynb) and [Sorting](00-begin-odyssey/sorting.ipynb) | 1/5 | 45 min | State, cost growth, and ordered arrays |
| [Antikythera Mechanism](01-antikythera-mechanism/antikythera-mechanism.ipynb) | 2/5 | 40 min | Analog state, gear ratios, cycles |
| [Levenshtein Distance](02-levenshtein-distance/levenshtein-distance.ipynb) | 2/5 | 35 min | String dynamic programming matrix |
| [Gale-Shapley](03-gale-shapley/gale-shapley.ipynb) | 2/5 | 30 min | Stable matching loop |
| [Huffman Coding](04-huffman-coding/huffman-coding.ipynb) | 3/5 | 40 min | Greedy binary tree |
| [Universal Turing Machine](05-turing-universal-machine/universal-turing-machine.ipynb) | 3/5 | 45 min | Tape and state machine |
| [Penrose Tiling](06-penrose-tiling/tiling.ipynb) | 3/5 | 40 min | Recursive substitution |

## Why This Module Comes First

These lessons are predictable on purpose. Students learn to trust state, trace loops, read tables, reason about cost, and see computation as a physical or abstract rule system before the course opens into networks, probability, and adversarial systems.

## Checkpoint

Build a tiny spelling helper: use Levenshtein distance to rank candidate corrections, then explain how Huffman coding would compress the same word list. For the historical-computation extension, explain how the Antikythera gear ratio `254/19 - 1 = 235/19` turns physical motion into a lunar-phase computation. The point is to connect gears, tables, trees, tapes, and cost.
