# RSA

RSA is a classic public-key cryptosystem where different keys handle encryption and decryption. Modular exponentiation makes the main operations efficient, while reversing the system requires information tied to factoring a large composite number. Small examples keep the arithmetic traceable.

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
