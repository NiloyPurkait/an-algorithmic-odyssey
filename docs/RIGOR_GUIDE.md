# Rigor Guide

The course is intuition-first, but each lesson should leave students with a formal handle. Use this guide to add proof sketches, complexity arguments, and failure analysis without turning the notebooks into reference notes.

## The Four-Part Rigor Block

Every algorithm should answer:

1. **Model.** What input, state, and operations are allowed?
2. **Invariant.** What remains true after every step?
3. **Termination or convergence.** Why does the process stop, stabilize, or approach a target?
4. **Cost.** What resource grows, and how does it scale with input size?

## Proof Patterns by Module

| Module | Proof Pattern | Typical Question |
| --- | --- | --- |
| Foundations | loop invariants, induction, exchange arguments | Why does the table/tree/state machine produce the intended result? |
| Spatial Graphs | cut properties, nearest-neighbor invariants, relaxation invariants, residual reasoning | Why is this region/path/tree/flow globally valid after local decisions? |
| Natural Emergence | local rule analysis, social-agent assumptions, genotype-phenotype mapping, stability, numerical assumptions | Which patterns come from the rule, the threshold, the genome, the selection pressure, or the implementation? |
| Statistical Optimization | expectation, convergence, approximation, objective monotonicity | What is exact, what is estimated, and what is optimized? |
| Strategic and Quantum | minimax induction, sampling error, number theory, period finding | Which search spaces are tractable, heuristic, adversarial, or quantum-sensitive? |

## Complexity Standard

Use concrete parameters before using asymptotic notation:

- `n`: number of items, symbols, cells, or states
- `V`: vertices
- `E`: edges
- `S`: sites or spatial samples
- `k`: clusters, hash functions, choices, or symbols
- `d`: depth, dimension, or edit-distance limit
- `T`: iterations, generations, samples, or playouts
- `g`: genes in a genome

Then state time and space separately.

Example:

```text
For a graph with V nodes and E edges, this implementation scans all unsettled
nodes each round, so it costs O(V^2 + E). With a heap, the standard version is
O((V + E) log V).
```

## Failure-Mode Standard

Each notebook should include one assumption-breaking test:

- Dijkstra with a negative edge
- A* with an inadmissible heuristic
- Voronoi with duplicate, nearly collinear, or edge-heavy sites
- Schelling segregation with threshold, vacancy, or movement-rule changes
- Biomorphs with mutation too small, mutation too large, or recursion depth too high
- topological sort with a cycle
- Bloom filter near saturation
- gradient descent with too-large learning rate
- k-means with poor initialization
- Enigma with repeated settings
- RSA with tiny primes
- Shor with a base that gives an unusable period

Students should see both the successful case and the assumption that makes it fail.

## Grading Rigor

For written responses, reward precision over length:

- names the invariant
- uses the right input parameters
- connects the visual trace to the proof idea
- identifies an assumption
- states a counterexample or failure case
- distinguishes exact output from heuristic or estimated output
