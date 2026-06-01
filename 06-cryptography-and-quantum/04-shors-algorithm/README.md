# Shor's Algorithm

Shor's algorithm reduces factoring to period finding. The quantum part estimates a period, and classical post-processing turns that period into candidate factors. The module returns to RSA's hardness assumption and shows how a different representation can change what is computationally feasible.

## Open

- [shors-algorithm.ipynb](shors-algorithm.ipynb)

## What To Watch

- The order of `a mod N` is the period being estimated.
- The quantum Fourier transform is used to extract periodic structure from amplitudes.
- Measurement gives samples, so the algorithm still needs classical arithmetic afterward.
- Toy demonstrations factor small numbers. Cryptographic-scale factoring would require fault-tolerant quantum hardware.

## Read Next

- [Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms on a Quantum Computer](https://arxiv.org/abs/quant-ph/9508027) - accessible preprint.
- [Shor, Polynomial-Time Algorithms for Prime Factorization and Discrete Logarithms](https://doi.org/10.1137/S0097539795293172) - journal version.
- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography) - standards work motivated by quantum attacks.
