# Problem Set 5: Strategic Search and Metaheuristics

## Goals

Students should be able to compare exhaustive search, heuristic search, stochastic sampling, and metaheuristic optimization, and explain when each one is the right tool for a search space that is too large to enumerate.

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

## Reflection

Take one hard search problem and compare where exact search, stochastic sampling, and evolutionary search each change what is practical. Note which method you would reach for first and why.
