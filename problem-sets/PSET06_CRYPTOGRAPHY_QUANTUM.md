# Problem Set 6: Cryptography and Quantum Frontiers

## Goals

Students should be able to model classical encryption as state, build public-key cryptography from modular arithmetic, explain why its security rests on a hardness assumption, and show how quantum period finding threatens that assumption.

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

### 3. Shor's Period-Finding Bridge

For a small composite `N`, choose a base `a` with `gcd(a, N) = 1` and compute modular powers until a period appears.

Deliverables:

- modular-power table
- period r if found
- gcd factor attempt
- explanation of what the quantum subroutine accelerates

## Reflection

Trace the chain from secrecy to its weakness: explain why RSA is considered secure, then how Shor's algorithm reframes factoring as period finding. State exactly which assumption breaks and what that implies about the role of large keys and future quantum hardware.
