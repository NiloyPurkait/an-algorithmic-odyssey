# Dawkins' Biomorphs

Biomorphs are recursive line drawings controlled by a small genome. Mutation creates nearby variants and the learner selects one, so cumulative selection searches a space of forms far too large to enumerate. It is the gentlest of this module's metaheuristics: the same mutate-and-select engine as genetic algorithms, with a human standing in for the fitness function.

## Open

- [biomorphs.ipynb](biomorphs.ipynb)

## What To Watch

- Genotype means the stored parameters.
- Phenotype means the drawing produced by those parameters.
- Mutation explores nearby forms; selection decides which branch of the search continues.
- The exercise demonstrates cumulative selection in a toy design space, not biological development in full.

## Read Next

- [The Blind Watchmaker, publisher page](https://www.penguinrandomhouse.com/books/38604/the-blind-watchmaker-by-richard-dawkins/) - book where Dawkins used biomorphs to explain cumulative selection.
- [LMU Biomorphs notes](https://cs.lmu.edu/~ray/notes/biomorphs/) - compact programming-oriented explanation.
- [Sims, Artificial Evolution for Computer Graphics](https://doi.org/10.1145/122718.122752) - influential evolutionary-art paper.
