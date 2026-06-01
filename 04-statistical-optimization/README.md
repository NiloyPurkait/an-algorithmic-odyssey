# Module 4: Statistical Sampling & Optimization

When exact answers are too slow, too large, or too rigid, computers lean on probability, vectors, matrices, and optimization. This module connects algorithmic thinking to data science.

## Field

Artificial intelligence, quantitative modeling, linear algebra, and signal processing.

## Learning Arc

1. [Bloom Filters](00-bloom-filters/bloom-filters.ipynb) introduces the trade between memory and certainty.
2. [Markov Chains](01-markov-chains/markov-chains.ipynb) models systems that move by probability.
3. [PageRank](02-pagerank/pagerank.ipynb) uses random walks to find stable importance in a network.
4. [k-means](03-kmeans-cluster/kmeans-cluster.ipynb) groups data by distance in vector space.
5. [Gradient Descent](04-gradient-descent/gradient-descent.ipynb) follows error downhill to fit a model.
6. [Moore-Penrose Pseudoinverse](05-penrose-linear-algebra/pseudoinverse.ipynb) and [Penrose Graphical Notation](05-penrose-linear-algebra/graph-notation.ipynb) show how linear algebra handles imperfect systems and tensor structure.
7. [Fast Fourier Transform](06-fast-fourier-transform/fft.ipynb) decomposes signals into frequencies.
8. [Perlin Noise](07-perlin-noise/perlin-noise.ipynb) runs that idea in reverse, synthesizing a coherent signal by layering frequencies as octaves.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Bloom Filters](00-bloom-filters/bloom-filters.ipynb) | 2/5 | 35 min | Probabilistic hash array |
| [Markov Chains](01-markov-chains/markov-chains.ipynb) | 3/5 | 35 min | Transition probabilities |
| [PageRank](02-pagerank/pagerank.ipynb) | 3/5 | 40 min | Random surfer graph |
| [k-means](03-kmeans-cluster/kmeans-cluster.ipynb) | 3/5 | 40 min | Vector-space clusters |
| [Gradient Descent](04-gradient-descent/gradient-descent.ipynb) | 3/5 | 40 min | Loss surface |
| [Linear Algebra Pair](05-penrose-linear-algebra/pseudoinverse.ipynb) | 4/5 | 50 min | SVD and tensor diagrams |
| [Fast Fourier Transform](06-fast-fourier-transform/fft.ipynb) | 4/5 | 45 min | Frequency transform |
| [Perlin Noise](07-perlin-noise/perlin-noise.ipynb) | 3/5 | 40 min | Procedural signal synthesis |

## Why This Module Comes Here

Students have seen exact structure. Now they learn the tools used when structure becomes noisy, high-dimensional, or too large to inspect directly.

## Checkpoint

Analyze a small dataset or network: use PageRank to score importance, k-means to group items, and gradient descent or the pseudoinverse to fit a simple model. State which parts are exact and which are approximate.
