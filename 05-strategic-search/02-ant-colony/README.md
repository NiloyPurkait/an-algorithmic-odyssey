# Ant Colony Optimization

Ant colony optimization turns collective trail-following into a search method. Candidate routes are built probabilistically from distance and pheromone, good tours reinforce their edges, and evaporation keeps exploration alive. Many weak local choices can concentrate around useful paths.

## Open

- [ant-colony.ipynb](ant-colony.ipynb)

## What To Watch

- Pheromone reinforcement increases the chance of reusing a good path.
- Evaporation prevents early paths from dominating forever.
- The balance between reinforcement and evaporation controls exploration versus exploitation.
- Too much early reinforcement locks the colony into a poor route.

## Read Next

- [Dorigo and Gambardella, Ant Colony System](https://doi.org/10.1109/4235.585892) - ant colony optimization for the traveling salesman problem.
