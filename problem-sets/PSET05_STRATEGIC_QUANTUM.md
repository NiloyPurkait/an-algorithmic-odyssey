# Problem Set 5: Strategic Intelligence and Quantum Frontiers

## Goals

Students should be able to compare exhaustive search, heuristic search, stochastic sampling, cryptographic hardness, and quantum period finding.

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

### 4. Enigma as State

Encrypt a short repeated-character message with Enigma.

Deliverables:

- rotor state trace
- ciphertext
- explanation of why the same plaintext letter can map to different ciphertext letters

### 5. RSA and the Factoring Assumption

Generate a tiny RSA keypair and encrypt a number message `m` with `0 <= m < n`.

Deliverables:

- p, q, n, public exponent, private exponent
- repeated-squaring trace for encryption or decryption
- explanation of why tiny RSA is insecure

### 6. Shor's Period-Finding Bridge

For a small composite `N`, choose a base `a` with `gcd(a, N) = 1` and compute modular powers until a period appears.

Deliverables:

- modular-power table
- period r if found
- gcd factor attempt
- explanation of what the quantum subroutine accelerates

## Reflection

Compare where exact search, random sampling, evolutionary search, and quantum period finding each change what is practical.
