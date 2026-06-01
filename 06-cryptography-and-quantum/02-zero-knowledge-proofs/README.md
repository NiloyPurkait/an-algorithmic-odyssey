# Zero-Knowledge Proofs

Zero-knowledge proofs emerged in the 1980s through work by Shafi Goldwasser, Silvio Micali, and Charles Rackoff. They answered a subtle cryptographic question. Can a claim be verified without handing over the secret that makes it true? Random challenges and repeated interaction make cheating unlikely while leaving no reusable witness in the protocol shown here.

## Open

- [zero-knowledge-proofs.ipynb](zero-knowledge-proofs.ipynb)

## What To Watch

- Completeness, soundness, and zero-knowledge are the three properties every proof must satisfy.
- In the Ali Baba cave a cheating Prover survives a single random challenge with probability one half, so soundness error falls as `(1/2)^k` over `k` rounds - 20 rounds clears one in a million.
- Soundness rests on the challenge being unpredictable: a fixed or guessable challenge lets a cheat pass every round and proves nothing.
- The graph 3-coloring protocol proves an NP-complete statement. A fresh color permutation each round keeps the revealed edge zero-knowledge.

## Read Next

- [Goldwasser, Micali, and Rackoff, The Knowledge Complexity of Interactive Proof Systems](https://doi.org/10.1137/0218012) - the foundational paper.
- [Quisquater et al., How to Explain Zero-Knowledge Protocols to Your Children](https://link.springer.com/chapter/10.1007/0-387-34805-0_60) - the Ali Baba cave.
- [Goldreich, Micali, and Wigderson, Proofs that Yield Nothing But Their Validity](https://doi.org/10.1145/116825.116852) - zero-knowledge for all of NP via graph coloring.
- [Zcash: What are zk-SNARKs?](https://z.cash/learn/what-are-zk-snarks/) - non-interactive, succinct proofs in practice.
