# Bloom Filters

A Bloom filter is built for membership tests when memory is scarce. It uses multiple hash functions to mark bits, which makes false negatives impossible for inserted items but allows false positives as the bit array fills. That memory-accuracy tradeoff becomes measurable.

## Open

- [bloom-filters.ipynb](bloom-filters.ipynb)

## What To Watch

- Each inserted item sets several bit positions through hash functions.
- A zero bit proves absence.
- All checked bits set means "maybe present."
- False-positive rate depends on the bit-array size, number of hash functions, and number of inserted items.

## Read Next

- [Bloom, Space/Time Trade-offs in Hash Coding with Allowable Errors](https://doi.org/10.1145/362686.362692) - original paper.
- [Broder and Mitzenmacher, Network Applications of Bloom Filters](https://doi.org/10.1080/15427951.2004.10129096) - systems survey.
- [Redis Bloom filter documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter/) - production-oriented reference.
