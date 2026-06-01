# Module 6: Cryptography & Quantum Frontiers

The course closes at the edge of what computation can protect and what it can break. Secrecy begins with problems that are easy one way and hard the other. The arc then moves through proof without disclosure, quantum search by interference, quantum period finding against RSA, and key testing through measurement disturbance.

## Field

Classical cryptography, public-key cryptography, interactive and zero-knowledge proofs, number theory, quantum search, quantum key distribution, and quantum computing.

## Learning Arc

1. [Enigma](00-turing-enigma/enigma.ipynb) models classical encryption as a stateful rotor machine, and shows how operational patterns leak structure.
2. [RSA](01-rsa/rsa.ipynb) builds public-key cryptography from modular arithmetic, where security rests on factoring being hard.
3. [Zero-Knowledge Proofs](02-zero-knowledge-proofs/zero-knowledge-proofs.ipynb) shift from hiding data to proving a statement true while revealing nothing, with soundness resting on repeated random challenges rather than on a hardness assumption.
4. [Grover's Algorithm](03-grovers-algorithm/grovers-algorithm.ipynb) introduces quantum search, using superposition and interference to amplify a marked answer in about the square root of the classical number of steps.
5. [Shor's Algorithm](04-shors-algorithm/shors-algorithm.ipynb) reduces factoring to period finding, showing how quantum hardware threatens the assumption RSA depends on.
6. [Quantum Key Distribution](05-quantum-key-distribution/quantum-key-distribution.ipynb) answers that threat in a different way: ideal BB84 uses nonorthogonal quantum states, so intercept-resend eavesdropping creates errors that Alice and Bob can sample for.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Enigma](00-turing-enigma/enigma.ipynb) | 3/5 | 40 min | Rotor state machine |
| [RSA](01-rsa/rsa.ipynb) | 4/5 | 45 min | Modular arithmetic |
| [Zero-Knowledge Proofs](02-zero-knowledge-proofs/zero-knowledge-proofs.ipynb) | 4/5 | 45 min | Interactive proof, probabilistic soundness |
| [Grover's Algorithm](03-grovers-algorithm/grovers-algorithm.ipynb) | 4/5 | 45 min | Quantum amplitude amplification |
| [Shor's Algorithm](04-shors-algorithm/shors-algorithm.ipynb) | 5/5 | 60 min | Quantum period finding |
| [Quantum Key Distribution](05-quantum-key-distribution/quantum-key-distribution.ipynb) | 4/5 | 45 min | BB84, photon polarization, no-cloning |

## Why This Module Ends the Course

The endpoint pulls several earlier ideas together. Enigma is a state machine. RSA uses modular cycles. Zero-knowledge proofs rely on randomized interaction. Grover amplifies a marked answer by interference. Shor turns factoring into period finding. BB84 changes the question again by making tampering show up as measurement disturbance.

## Checkpoint

Connect the chain end to end: explain why RSA is considered secure (factoring is hard), then trace how Shor's algorithm reframes factoring as period finding. State exactly which assumption breaks and what scale of quantum hardware that would require. Separately, explain how a zero-knowledge proof reaches near-certainty from repeated random challenges, and why that confidence needs no hardness assumption at all. Then explain why Grover's search needs only about the square root of the classical number of steps, and what goes wrong if it runs past the optimal number of iterations. Finally, explain why ideal BB84 uses no-cloning and measurement disturbance rather than a hardness assumption, and what an expected 25% error rate under intercept-resend tells Alice and Bob.
