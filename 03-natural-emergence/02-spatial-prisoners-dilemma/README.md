# Spatial Prisoner's Dilemma

The Prisoner's Dilemma is a non-zero-sum game: two agents each choose to cooperate or defect, and betraying a cooperator pays best in a single round. This lesson places Always Defect, Always Cooperate, and Tit-for-Tat agents on a grid, lets each play its neighbors and copy whoever scores highest, and watches cooperation survive as clusters.

## Open

- [spatial-prisoners-dilemma.ipynb](spatial-prisoners-dilemma.ipynb)

## What To Watch

- One round rewards defection; repeated rounds reward reciprocity (Tit-for-Tat).
- Defectors spike early by eating naive cooperators, then starve once the cooperators are gone.
- Tit-for-Tat clusters form "shields": interior cells earn mutual-cooperation payoffs that no defecting border can beat.
- The update is local and synchronous, the same shape as Game of Life and Schelling.
- Set the iterated rounds to 1 (one-shot) and cooperation collapses: with no future round, Tit-for-Tat cannot retaliate.

## Read Next

- [Axelrod and Hamilton, The Evolution of Cooperation](https://www.science.org/doi/10.1126/science.7466396) - the 1981 Science paper.
- [Axelrod, The Evolution of Cooperation](https://www.basicbooks.com/titles/robert-axelrod/the-evolution-of-cooperation/9780465005642/) - the tournament and Tit-for-Tat.
- [Nowak and May, Evolutionary games and spatial chaos](https://www.nature.com/articles/359826a0) - the spatial model and its clustering patterns.
