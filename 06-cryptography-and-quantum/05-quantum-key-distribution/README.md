# Quantum Key Distribution

BB84 changes the cryptography question from hard-to-compute to hard-to-measure-without-disturbance. Alice and Bob keep only matched-basis bits, then sample the sifted key for errors caused by intercept-resend eavesdropping. Ideal quantum key distribution depends on nonorthogonal states, no-cloning, and statistical detection.

## Open

- [quantum-key-distribution.ipynb](quantum-key-distribution.ipynb)

## What To Watch

- Measuring a photon in the wrong basis gives a random result and destroys the original polarization, so bases must match for a bit to count.
- Sifting keeps about half the photons. The rest are discarded when Alice and Bob chose different bases.
- A full intercept-resend eavesdropper corrupts a sifted bit with probability one half times one half, producing an expected 25% QBER. Partial interception trades less information for less disturbance.
- The failure mode is classical, copyable bits: with no-cloning gone, Eve learns the whole key and injects no error, so the protocol's security depends entirely on the no-cloning theorem.

## Read Next

- [Bennett and Brassard, Quantum cryptography: Public key distribution and coin tossing](https://doi.org/10.1016/j.tcs.2014.05.025) - the original BB84 protocol.
- [Gisin, Ribordy, Tittel, and Zbinden, Quantum cryptography](https://doi.org/10.1103/RevModPhys.74.145) - a thorough survey.
- [Nielsen and Chuang, Quantum Computation and Quantum Information](https://doi.org/10.1017/CBO9780511976667) - the no-cloning theorem and quantum key distribution (chapter 12).
