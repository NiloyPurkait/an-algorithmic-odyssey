# RSA

RSA is a public-key cryptosystem based on modular exponentiation and the difficulty of factoring large composite numbers. Secrecy shifts from hidden machine settings to mathematical asymmetry, where one direction is easy to compute and hard to reverse without extra information.

## Open

- [rsa.ipynb](rsa.ipynb)

## What To Watch

- The public modulus has the form `n = pq`.
- Public and private exponents are linked through modular inverses.
- Toy RSA demonstrates the algebra but omits production padding and side-channel defenses.
- Factoring `n` reveals the private key material in the textbook construction.

## Read Next

- [Rivest, Shamir, and Adleman, A Method for Obtaining Digital Signatures and Public-Key Cryptosystems](https://doi.org/10.1145/359340.359342) - original RSA paper.
- [RFC 8017: PKCS #1 RSA Cryptography Specifications](https://www.rfc-editor.org/rfc/rfc8017) - RSA standard used in practice.
- [NIST FIPS 186-5: Digital Signature Standard](https://csrc.nist.gov/pubs/fips/186-5/final) - federal digital-signature standard.
