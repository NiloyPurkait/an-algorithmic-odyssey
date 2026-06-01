# PageRank

PageRank scores pages by modeling a random surfer on a directed link graph. A page receives rank from pages that link to it, weighted by their own rank.

## Open

- [pagerank.ipynb](pagerank.ipynb)

## What To Watch

- Links become transition probabilities.
- The damping factor mixes link-following with random jumps.
- Dangling pages need special handling because they have no outgoing links.
- Iteration estimates a stationary distribution over pages.

## Read Next

- [Stanford CS224W PageRank notes](https://snap.stanford.edu/class/cs224w-2018/handouts/03-pagerank.pdf) - matrix and random-surfer treatment.
- [Brin and Page, The Anatomy of a Large-Scale Hypertextual Web Search Engine](https://snap.stanford.edu/class/cs224w-readings/Brin98Anatomy.pdf) - original Google search-engine paper.
- [NetworkX PageRank documentation](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.link_analysis.pagerank_alg.pagerank.html) - implementation behavior.
