# Spatial Prisoner's Dilemma

The Prisoner's Dilemma came out of Cold War-era game theory work by Merrill Flood and Melvin Dresher, with Albert Tucker giving the story its familiar name. Robert Axelrod's later tournaments made Tit-for-Tat prominent as a simple strategy for repeated play. Placing strategies on a grid adds space to the dilemma, so local neighborhoods can protect cooperation from local extinction.

## Open

- [spatial-prisoners-dilemma.ipynb](spatial-prisoners-dilemma.ipynb)

## What To Watch

- One round rewards defection. Repeated rounds reward reciprocity through Tit-for-Tat.
- Defectors spike early by eating naive cooperators, then starve once the cooperators are gone.
- Tit-for-Tat clusters form "shields": interior cells earn mutual-cooperation payoffs that no defecting border can beat.
- The update is local and synchronous, the same shape as Game of Life and Schelling.
- Set the iterated rounds to 1 (one-shot) and cooperation collapses: with no future round, Tit-for-Tat cannot retaliate.

## Read Next

- [Axelrod and Hamilton, The Evolution of Cooperation](https://www.science.org/doi/10.1126/science.7466396) - the 1981 Science paper.
- [Axelrod, The Evolution of Cooperation](https://www.basicbooks.com/titles/robert-axelrod/the-evolution-of-cooperation/9780465005642/) - the tournament and Tit-for-Tat.
- [Nowak and May, Evolutionary games and spatial chaos](https://www.nature.com/articles/359826a0) - the spatial model and its clustering patterns.
