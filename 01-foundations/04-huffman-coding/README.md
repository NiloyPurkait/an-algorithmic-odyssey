# Huffman Coding

Compression begins with a simple asymmetry. Frequent symbols deserve short codes. Huffman coding uses that asymmetry greedily, repeatedly merging the two least frequent trees to build an optimal prefix code for known frequencies. A data distribution becomes a binary tree.

## Open

- [huffman-coding.ipynb](huffman-coding.ipynb)

## What To Watch

- Prefix-free codes can be decoded without separators.
- The greedy merge always combines the two least frequent remaining nodes.
- Expected code length depends on the source distribution.
- Entropy gives the lower bound to compare against. Huffman codes can land above it.

## Read Next

- [Huffman, A Method for the Construction of Minimum-Redundancy Codes](https://doi.org/10.1109/JRPROC.1952.273898) - original paper.
- [Princeton Algorithms: Data Compression](https://algs4.cs.princeton.edu/55compression/) - implementation notes and examples.
- [RFC 1951: DEFLATE Compressed Data Format](https://www.rfc-editor.org/rfc/rfc1951) - real format that uses Huffman coding.
