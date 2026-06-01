# Quantum Key Distribution

The BB84 protocol shares a secret key over a fully public channel and detects any eavesdropper, with security resting on physics rather than on a computational hardness assumption. Alice encodes each bit in a photon's polarization using a random basis; Bob measures in a random basis; they keep the bits where their bases agree. Because an unknown quantum state cannot be measured without disturbance and cannot be copied at all, an eavesdropper who reads the photons leaves errors behind - a full interception injects an unmistakable 25% error rate. It closes the cryptography arc on a resolution: where Shor's algorithm breaks security built on hard math, BB84 builds security on laws of physics that no computer can strip away.

## Open

- [quantum-key-distribution.ipynb](quantum-key-distribution.ipynb)

## What To Watch

- Measuring a photon in the wrong basis gives a random result and destroys the original polarization, so bases must match for a bit to count.
- Sifting keeps about half the photons; the rest are discarded when Alice and Bob chose different bases.
- A full intercept-resend eavesdropper corrupts a sifted bit with probability one half times one half, leaving a 25% error rate; partial interception trades less information for less disturbance.
- The failure mode is classical, copyable bits: with no-cloning gone, Eve learns the whole key and injects no error, so the protocol's security depends entirely on the no-cloning theorem.

## Read Next

- [Bennett and Brassard, Quantum cryptography: Public key distribution and coin tossing](https://doi.org/10.1016/j.tcs.2014.05.025) - the original BB84 protocol.
- [Gisin, Ribordy, Tittel, and Zbinden, Quantum cryptography](https://doi.org/10.1103/RevModPhys.74.145) - a thorough survey.
- [Nielsen and Chuang, Quantum Computation and Quantum Information](https://doi.org/10.1017/CBO9780511976667) - the no-cloning theorem and quantum key distribution (chapter 12).
