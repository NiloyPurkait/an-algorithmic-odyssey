# Problem Set 4: Statistical Optimization

## Goals

Practice reasoning about uncertainty, approximation, vector spaces, convergence, and objective functions.

## Problems

### 1. Bloom Filter Tradeoff

Insert the same set of items into Bloom filters with three memory sizes.

Deliverables:

- false-positive rate table
- bit-saturation plot
- explanation of why false negatives do not occur in an insert-only Bloom filter with the same hash functions

### 2. Markov Chain Long Run

Create a Markov chain with at least four states.

Deliverables:

- transition matrix
- probability-vector animation or table over time
- long-run distribution, or an explanation of why the chain does not settle
- one modified transition and observed effect

### 3. PageRank Perturbation

Run PageRank on a small directed graph with damping, then add one node or link.

Deliverables:

- before/after rankings
- explanation of damping
- identification of the largest rank movement

### 4. k-means Initialization Study

Run k-means on the same points from three initializations.

Deliverables:

- visual trace for one run
- final objective values
- explanation of local minima

### 5. Fitting by Descent and Linear Algebra

Fit a simple line or curve using gradient descent and either least squares or the Moore-Penrose pseudoinverse.

Deliverables:

- fitted parameters
- loss over time
- comparison of exact, estimated, and optimized parts

### 6. Frequency Decomposition

Build a sampled signal from at least two sine waves and run the FFT.

Deliverables:

- time-domain plot
- frequency-domain plot
- identification of peaks
- aliasing example or warning

### 7. Procedural Signal Synthesis

Generate Perlin noise with one octave and with several octaves.

Deliverables:

- single-octave and multi-octave output images or one-dimensional plots
- description of how persistence and frequency change the result
- one sentence connecting octave layering to the frequency view from the FFT problem

## Reflection

Name one answer in this module that is exact, one that is estimated, and one that is optimized.
