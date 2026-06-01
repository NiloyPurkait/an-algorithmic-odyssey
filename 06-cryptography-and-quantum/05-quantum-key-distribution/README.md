# Quantum Key Distribution

The BB84 protocol shares a secret key over a public channel and detects intercept-resend eavesdropping statistically. Its test rests on quantum measurement rather than on a computational hardness assumption. Alice encodes each bit in a photon's polarization using a random basis. Bob measures in a random basis. They keep the bits where their bases agree. Because BB84 uses nonorthogonal states, an unknown photon cannot be copied and a wrong-basis measurement disturbs the state. A full intercept-resend attack produces an expected 25% error rate in the sifted key. After Shor breaks security built on hard math, BB84 asks whether the channel itself has been disturbed.

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
