# Problem Set 5: Strategic Search and Metaheuristics

## Goals

Practice comparing exhaustive search, heuristic search, stochastic sampling, and metaheuristic optimization. Explain when each one fits a search space that is too large to enumerate.

## Problems

### 1. Minimax Value Backup

Create a small game tree of depth at least three.

Deliverables:

- leaf values
- backed-up internal values
- chosen root move
- induction-style proof sketch

### 2. MCTS Stability

Run Monte Carlo Tree Search with three playout budgets. Use fixed random seeds or repeat each budget enough times to compare stability.

Deliverables:

- visit counts
- win-rate estimates
- recommended move by budget
- explanation of exploration versus exploitation

### 3. Metaheuristic Comparison

Use ant colony optimization or a genetic algorithm on a small route, scheduling, or string-matching problem. Keep the scoring function fixed across runs.

Deliverables:

- parameter table
- best solution over time
- explanation of premature convergence

### 4. Artificial Selection Lineage

Run the Biomorphs artificial-selection playground for at least 10 generations.

Deliverables:

- starting genome and final genome
- visual lineage snapshots
- description of the selection criterion or scoring function used
- explanation of why mutation is random but selection is not, and how cumulative selection samples a space too large to enumerate

## Reflection

Take one hard search problem and compare where exact search, stochastic sampling, and evolutionary search each change what is practical. Name the method that fits first and explain why.
