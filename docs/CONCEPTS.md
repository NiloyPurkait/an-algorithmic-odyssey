# Concept Index

Use this as a cross-reference. Many notebooks teach different surfaces of the same idea.

## Greedy Choice

A greedy algorithm makes the best local move available, then commits to it.

- [Gale-Shapley](../01-foundations/03-gale-shapley/gale-shapley.ipynb): stable proposals converge through repeated local choices.
- [Huffman Coding](../01-foundations/04-huffman-coding/huffman-coding.ipynb): merge the two least frequent trees first.
- [Minimum Spanning Tree](../02-spatial-graphs/01-minimum-spanning-tree/minimum-spanning-tree.ipynb): keep the cheapest edge that does not create a cycle.
- [Dijkstra](../02-spatial-graphs/02-dijkstra/dijkstra.ipynb): settle the nearest unfinished node.

## Dynamic Programming

Dynamic programming stores smaller answers so larger answers can reuse them.

- [Levenshtein Distance](../01-foundations/02-levenshtein-distance/levenshtein-distance.ipynb): prefix-to-prefix string edits.
- [Floyd-Warshall](../02-spatial-graphs/05-floyd-warshall/floyd-warshall.ipynb): all-pairs shortest paths through intermediate nodes.

## Graph Thinking

Graphs model connected systems: routes, dependencies, links, capacities, and influence.

- [Topological Sort](../02-spatial-graphs/00-topological-sort/topological-sort.ipynb)
- [Minimum Spanning Tree](../02-spatial-graphs/01-minimum-spanning-tree/minimum-spanning-tree.ipynb)
- [Dijkstra](../02-spatial-graphs/02-dijkstra/dijkstra.ipynb)
- [A*](../02-spatial-graphs/03-a-star/a-star.ipynb)
- [Voronoi and Delaunay](../02-spatial-graphs/04-voronoi-delaunay/voronoi-delaunay.ipynb): turn coordinate geometry into a natural-neighbor graph.
- [Edmonds-Karp](../02-spatial-graphs/06-edmonds-karp/edmonds-karp.ipynb)
- [PageRank](../04-statistical-optimization/02-pagerank/pagerank.ipynb)

## Matrix Thinking

Matrices make relationships visible as tables of numbers.

- [Levenshtein Distance](../01-foundations/02-levenshtein-distance/levenshtein-distance.ipynb): edit costs across prefixes.
- [Floyd-Warshall](../02-spatial-graphs/05-floyd-warshall/floyd-warshall.ipynb): path costs across every pair of nodes.
- [Game of Life](../03-natural-emergence/00-game-of-life/game-of-life.ipynb): cell states across a grid.
- [PageRank](../04-statistical-optimization/02-pagerank/pagerank.ipynb): probability flowing through a network.
- [Moore-Penrose Pseudoinverse](../04-statistical-optimization/05-penrose-linear-algebra/pseudoinverse.ipynb): best-fit solutions in linear systems.

## Spatial Partitioning

Spatial partitioning turns a continuous plane into discrete regions, neighbors, and queries.

- [Voronoi and Delaunay](../02-spatial-graphs/04-voronoi-delaunay/voronoi-delaunay.ipynb): closest-site territories and natural-neighbor triangles.
- [A*](../02-spatial-graphs/03-a-star/a-star.ipynb): grid coordinates become a searchable route space.
- [k-means](../04-statistical-optimization/03-kmeans-cluster/kmeans-cluster.ipynb): points inherit cluster regions from nearest centers.
- [Perlin Noise](../03-natural-emergence/05-perlin-noise/perlin-noise.ipynb): coordinates sample smooth procedural fields.

## Local Rules and Emergence

Simple local interactions can produce global structure that is hard to predict from one rule alone.

- [Game of Life](../03-natural-emergence/00-game-of-life/game-of-life.ipynb): synchronous neighbor rules create stable, oscillating, and moving patterns.
- [Schelling's Model of Segregation](../03-natural-emergence/01-schelling-segregation/schelling-segregation.ipynb): mild local preferences can amplify into global clustering.
- [Boids](../03-natural-emergence/02-boids/boids.ipynb): separation, alignment, and cohesion create flocking from autonomous vector agents.
- [Dawkins' Biomorphs](../03-natural-emergence/03-biomorphs/biomorphs.ipynb): mutation plus artificial selection walks through a space of recursive forms.
- [Turing Patterns](../03-natural-emergence/04-turing-patterns/turing-patterns.ipynb): reaction and diffusion create spots, bands, and waves.
- [Perlin Noise](../03-natural-emergence/05-perlin-noise/perlin-noise.ipynb): local gradient structure creates smooth procedural terrain.
- [Penrose Tiling](../03-natural-emergence/06-penrose-tiling/tiling.ipynb): recursive substitution creates non-repeating order.

## Social Emergence

Social simulations can reveal how individual rules and institutional constraints create group-level patterns.

- [Schelling's Model of Segregation](../03-natural-emergence/01-schelling-segregation/schelling-segregation.ipynb): micro-level satisfaction rules produce macro-level spatial clustering.
- [Game of Life](../03-natural-emergence/00-game-of-life/game-of-life.ipynb): local neighbor rules create larger grid dynamics.
- [Boids](../03-natural-emergence/02-boids/boids.ipynb): agent-level rules create collective motion.

## Evolutionary Search

Evolutionary systems generate variation and preserve selected structure over repeated generations.

- [Dawkins' Biomorphs](../03-natural-emergence/03-biomorphs/biomorphs.ipynb): artificial selection chooses among small integer-gene mutations.
- [Genetic Algorithms](../05-adversarial-and-quantum/02-ant-colony/genetic-algorithms.ipynb): selection, crossover, and mutation optimize candidate solutions.
- [Ant Colony Optimization](../05-adversarial-and-quantum/02-ant-colony/ant-colony.ipynb): successful paths reinforce future search behavior.

## State Machines

A state machine changes behavior based on its current state and input.

- [Antikythera Mechanism](../01-foundations/01-antikythera-mechanism/antikythera-mechanism.ipynb): crank position determines every connected dial.
- [Universal Turing Machine](../01-foundations/05-turing-universal-machine/universal-turing-machine.ipynb)
- [Markov Chains](../04-statistical-optimization/01-markov-chains/markov-chains.ipynb)
- [Enigma](../05-adversarial-and-quantum/03-turing-enigma/enigma.ipynb)

## Ratio and Cycle Thinking

Some algorithms encode structure as ratios, modular positions, or repeating cycles.

- [Antikythera Mechanism](../01-foundations/01-antikythera-mechanism/antikythera-mechanism.ipynb): gear ratios approximate lunar and solar cycles.
- [Markov Chains](../04-statistical-optimization/01-markov-chains/markov-chains.ipynb): probability mass cycles through states.
- [Fast Fourier Transform](../04-statistical-optimization/06-fast-fourier-transform/fft.ipynb): signals become periodic frequency components.
- [RSA](../05-adversarial-and-quantum/04-rsa/rsa.ipynb): modular exponentiation cycles through residues.
- [Shor's Algorithm](../05-adversarial-and-quantum/05-shors-algorithm/shors-algorithm.ipynb): factoring becomes period finding.

## Randomness and Sampling

Randomness can reduce memory, model uncertainty, or search spaces too large to exhaust.

- [Bloom Filters](../04-statistical-optimization/00-bloom-filters/bloom-filters.ipynb)
- [Markov Chains](../04-statistical-optimization/01-markov-chains/markov-chains.ipynb)
- [Perlin Noise](../03-natural-emergence/05-perlin-noise/perlin-noise.ipynb)
- [Monte Carlo Tree Search](../05-adversarial-and-quantum/01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb)
- [Ant Colony Optimization](../05-adversarial-and-quantum/02-ant-colony/ant-colony.ipynb)
- [Genetic Algorithms](../05-adversarial-and-quantum/02-ant-colony/genetic-algorithms.ipynb)

## Optimization

Optimization searches for better choices under a cost, score, or constraint.

- [k-means](../04-statistical-optimization/03-kmeans-cluster/kmeans-cluster.ipynb): improve cluster centers.
- [Gradient Descent](../04-statistical-optimization/04-gradient-descent/gradient-descent.ipynb): reduce loss by following a slope.
- [Ant Colony Optimization](../05-adversarial-and-quantum/02-ant-colony/ant-colony.ipynb): reinforce useful paths.
- [Genetic Algorithms](../05-adversarial-and-quantum/02-ant-colony/genetic-algorithms.ipynb): evolve better candidates.

## Trees

Trees appear as compression structures, search spaces, and recursive decompositions.

- [Huffman Coding](../01-foundations/04-huffman-coding/huffman-coding.ipynb)
- [Minimax](../05-adversarial-and-quantum/00-min-max/min-max.ipynb)
- [Monte Carlo Tree Search](../05-adversarial-and-quantum/01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb)
- [Penrose Tiling](../03-natural-emergence/06-penrose-tiling/tiling.ipynb)

## Signals and Structure

Some algorithms reveal hidden structure by changing representation.

- [Fast Fourier Transform](../04-statistical-optimization/06-fast-fourier-transform/fft.ipynb): time samples become frequencies.
- [Penrose Graphical Notation](../04-statistical-optimization/05-penrose-linear-algebra/graph-notation.ipynb): tensor operations become diagrams.
- [Shor's Algorithm](../05-adversarial-and-quantum/05-shors-algorithm/shors-algorithm.ipynb): factoring becomes period finding.
