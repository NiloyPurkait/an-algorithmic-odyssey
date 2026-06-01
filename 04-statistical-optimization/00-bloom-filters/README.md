# Bloom Filters

A Bloom filter is a space-efficient membership structure. It can prove that an item is absent, or report that an item is probably present. This opens the probability module by making a controlled trade: less memory in exchange for a measurable chance of false positives.

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
