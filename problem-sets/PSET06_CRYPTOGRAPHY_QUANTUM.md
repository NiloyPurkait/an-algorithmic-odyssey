# Problem Set 6: Cryptography and Quantum Frontiers

## Goals

Students should be able to model classical encryption as state, build public-key cryptography from modular arithmetic and explain why its security rests on a hardness assumption, prove a statement without revealing it and bound a cheating prover's success, search an unstructured space with a quantum square-root speedup, and show how quantum period finding threatens the hardness assumption.

## Problems

### 1. Enigma as State

Encrypt a short repeated-character message with Enigma.

Deliverables:

- rotor state trace
- ciphertext
- explanation of why the same plaintext letter can map to different ciphertext letters

### 2. RSA and the Factoring Assumption

Generate a tiny RSA keypair and encrypt a number message `m` with `0 <= m < n`.

Deliverables:

- p, q, n, public exponent, private exponent
- repeated-squaring trace for encryption or decryption
- explanation of why tiny RSA is insecure

### 3. Zero-Knowledge Soundness

Simulate the Ali Baba cave (or the graph 3-coloring protocol) for an honest prover and a cheating prover across a range of round counts `k`.

Deliverables:

- acceptance rate for the honest prover (completeness) and the cheating prover (soundness) versus `k`
- the measured cheat rate compared with the bound `(1/2)^k` for the cave, or `(1 - 1/|E|)^k` for the coloring graph
- the smallest `k` that pushes the cheat below one in a million
- a predictable-challenge run showing the cheat now passes every round, and one sentence on why independent randomness is what makes the proof sound

### 4. Grover Amplitude Amplification

Simulate Grover's algorithm on an 8-state system with one marked answer, recording the target probability after each iteration.

Deliverables:

- probability of the marked state after 0, 1, and 2 iterations
- the optimal iteration count from `(pi/4)*sqrt(N)` and the success probability it reaches
- an over-rotation run showing the probability fall past the optimal iteration, with one sentence on why more iterations hurt
- the classical-versus-Grover query counts for `N = 10^6`

### 5. Shor's Period-Finding Bridge

For a small composite `N`, choose a base `a` with `gcd(a, N) = 1` and compute modular powers until a period appears.

Deliverables:

- modular-power table
- period r if found
- gcd factor attempt
- explanation of what the quantum subroutine accelerates

## Reflection

Trace the chain from secrecy to its weakness: explain why RSA is considered secure, then how Shor's algorithm reframes factoring as period finding. Contrast that with Grover, whose square-root speedup only weakens unstructured search and must stop at its optimal iteration count. State exactly which assumption breaks and what that implies about the role of large keys and future quantum hardware.
