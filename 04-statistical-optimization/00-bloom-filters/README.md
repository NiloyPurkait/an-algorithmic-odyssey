# Bloom Filters

Burton Bloom introduced the Bloom filter in 1970 for membership tests under tight storage limits. The structure accepts a controlled kind of uncertainty, allowing false positives while preventing false negatives for inserted items. Multiple hash functions and a bit array make the memory-accuracy tradeoff measurable.

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
