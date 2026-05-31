# Module 4: Statistical Sampling & Modern Data Science

When exact answers are too slow, too large, or too rigid, computers lean on probability, vectors, matrices, and optimization. This module connects algorithmic thinking to modern data science.

## Field

Artificial intelligence, quantitative modeling, linear algebra, and signal processing.

## Learning Arc

1. [Bloom Filters](00-bloom-filters/bloom-filters.ipynb) introduces the trade between memory and certainty.
2. [Markov Chains](01-markov-chains/markov-chains.ipynb) models systems that move by probability.
3. [PageRank](02-pagerank/pagerank.ipynb) uses random walks to find stable importance in a network.
4. [K-Means](03-kmeans-cluster/kmeans-cluster.ipynb) groups data by distance in vector space.
5. [Gradient Descent](04-gradient-descent/gradient-descent.ipynb) follows error downhill to fit a model.
6. [Moore-Penrose Pseudoinverse](05-penrose-linear-algebra/pseudoinverse.ipynb) and [Penrose Graphical Notation](05-penrose-linear-algebra/graph-notation.ipynb) show how linear algebra handles imperfect systems and tensor structure.
7. [Fast Fourier Transform](06-fast-fourier-transform/fft.ipynb) decomposes signals into frequencies.

## Lesson Guide

| Lesson | Difficulty | Time | Main Model |
| --- | --- | --- | --- |
| [Bloom Filters](00-bloom-filters/bloom-filters.ipynb) | 2/5 | 35 min | Probabilistic hash array |
| [Markov Chains](01-markov-chains/markov-chains.ipynb) | 3/5 | 35 min | Transition probabilities |
| [PageRank](02-pagerank/pagerank.ipynb) | 3/5 | 40 min | Random surfer graph |
| [K-Means](03-kmeans-cluster/kmeans-cluster.ipynb) | 3/5 | 40 min | Vector-space clusters |
| [Gradient Descent](04-gradient-descent/gradient-descent.ipynb) | 3/5 | 40 min | Loss landscape |
| [Linear Algebra Pair](05-penrose-linear-algebra/pseudoinverse.ipynb) | 4/5 | 50 min | SVD and tensor diagrams |
| [Fast Fourier Transform](06-fast-fourier-transform/fft.ipynb) | 4/5 | 45 min | Frequency transform |

## Why This Module Comes Here

Students have seen exact structure. Now they learn the tools used when structure becomes noisy, high-dimensional, or too large to inspect directly.

## Checkpoint

Analyze a small dataset or network: use PageRank to score importance, K-Means to group items, and Gradient Descent or the pseudoinverse to fit a simple model. State which parts are exact and which are approximate.
