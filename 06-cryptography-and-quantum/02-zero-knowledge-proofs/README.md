# Zero-Knowledge Proofs

A zero-knowledge proof lets a Prover convince a skeptical Verifier that a statement is true while revealing nothing beyond that truth: not the password, not the witness, and, in the interactive setting shown here, not a reusable certificate for someone else. The guarantee comes from interaction and randomness: the Verifier issues an unpredictable challenge each round, and a Prover who lacks the secret cannot prepare for every challenge at once. It adds proof to the cryptography story: knowledge can be demonstrated without being handed over.

## Open

- [zero-knowledge-proofs.ipynb](zero-knowledge-proofs.ipynb)

## What To Watch

- Completeness, soundness, and zero-knowledge are the three properties every proof must satisfy.
- In the Ali Baba cave a cheating Prover survives a single random challenge with probability one half, so soundness error falls as `(1/2)^k` over `k` rounds - 20 rounds clears one in a million.
- Soundness rests on the challenge being unpredictable: a fixed or guessable challenge lets a cheat pass every round and proves nothing.
- The graph 3-coloring protocol proves an NP-complete statement; a fresh color permutation each round is what keeps the revealed edge zero-knowledge.

## Read Next

- [Goldwasser, Micali, and Rackoff, The Knowledge Complexity of Interactive Proof Systems](https://doi.org/10.1137/0218012) - the foundational paper.
- [Quisquater et al., How to Explain Zero-Knowledge Protocols to Your Children](https://link.springer.com/chapter/10.1007/0-387-34805-0_60) - the Ali Baba cave.
- [Goldreich, Micali, and Wigderson, Proofs that Yield Nothing But Their Validity](https://doi.org/10.1145/116825.116852) - zero-knowledge for all of NP via graph coloring.
- [Zcash: What are zk-SNARKs?](https://z.cash/learn/what-are-zk-snarks/) - non-interactive, succinct proofs in practice.
