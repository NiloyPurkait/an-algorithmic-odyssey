# Module 6: Cryptography & Quantum Frontiers

This module closes the course at the edge of what computation can protect and what it can break. Secrecy is built on problems that are easy one way and hard the other; one lesson shows how to prove a fact while revealing nothing about it, another introduces quantum search through interference, and the final lesson shows how a quantum algorithm undermines exactly the hardness that public-key cryptography depends on.

## Field

Classical cryptography, public-key cryptography, interactive and zero-knowledge proofs, number theory, quantum search, and quantum computing.

## Learning Arc

1. [Enigma](00-turing-enigma/enigma.ipynb) models classical encryption as a stateful rotor machine, and shows how operational patterns leak structure.
2. [RSA](01-rsa/rsa.ipynb) builds public-key cryptography from modular arithmetic, where security rests on factoring being hard.
3. [Zero-Knowledge Proofs](02-zero-knowledge-proofs/zero-knowledge-proofs.ipynb) shift from hiding data to proving a statement true while revealing nothing, with soundness resting on repeated random challenges rather than on a hardness assumption.
4. [Grover's Algorithm](03-grovers-algorithm/grovers-algorithm.ipynb) introduces quantum search, using superposition and interference to amplify a marked answer in about the square root of the classical number of steps.
5. [Shor's Algorithm](04-shors-algorithm/shors-algorithm.ipynb) closes the course by reducing factoring to period finding, showing how quantum hardware threatens the assumption RSA depends on.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Enigma](00-turing-enigma/enigma.ipynb) | 3/5 | 40 min | Rotor state machine |
| [RSA](01-rsa/rsa.ipynb) | 4/5 | 45 min | Modular arithmetic |
| [Zero-Knowledge Proofs](02-zero-knowledge-proofs/zero-knowledge-proofs.ipynb) | 4/5 | 45 min | Interactive proof, probabilistic soundness |
| [Grover's Algorithm](03-grovers-algorithm/grovers-algorithm.ipynb) | 4/5 | 45 min | Quantum amplitude amplification |
| [Shor's Algorithm](04-shors-algorithm/shors-algorithm.ipynb) | 5/5 | 60 min | Quantum period finding |

## Why This Module Ends the Course

It combines the whole toolkit at a single dramatic point: state machines (Enigma), modular ratio and cycle thinking (RSA), interactive proofs that convince without revealing (zero-knowledge), quantum interference that amplifies a marked answer (Grover), and representation change (Shor turning factoring into period finding). The arc ends on the tension between cryptographic hardness and quantum speedup.

## Checkpoint

Connect the chain end to end: explain why RSA is considered secure (factoring is hard), then trace how Shor's algorithm reframes factoring as period finding. State exactly which assumption breaks and what scale of quantum hardware that would require. Separately, explain how a zero-knowledge proof reaches near-certainty from repeated random challenges, and why that confidence needs no hardness assumption at all. Then explain why Grover's search needs only about the square root of the classical number of steps, and what goes wrong if it runs past the optimal number of iterations.
