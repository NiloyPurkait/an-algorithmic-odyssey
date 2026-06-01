# Shor's Algorithm

Peter Shor's 1994 algorithm changed the status of factoring by linking it to quantum period finding. Classical post-processing can turn a suitable period into nontrivial factors, while the quantum subroutine supplies that period efficiently in principle. Small numbers make the threat to RSA-style assumptions traceable.

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
