# Spatial Predator-Prey

A grid of grass, rabbits, and foxes runs on one local rule in a cycle: rabbits graze grass into new rabbits, foxes eat rabbits into new foxes, and a fox with no prey nearby starves so the ground returns to grass. From a random start this organizes itself into rotating spiral waves that support long-lived coexistence in the finite grid. Remove the space - shuffle the grid so the population is well-mixed - and the spirals cannot form, stochastic drift can erase a species, and the cycle collapses. It bridges discrete cellular rules to continuous population models, and shows how space can stabilize coexistence.

## Open

- [predator-prey.ipynb](predator-prey.ipynb)

## What To Watch

- Each cell flips to its cyclic successor (grass to rabbit to fox to grass) only when enough neighbors already are it, so one local rule drives everything.
- Cyclic dominance plus space produces rotating spiral waves, and the three populations often cycle near balance instead of collapsing quickly.
- The failure mode is removing space: a well-mixed grid loses a species to extinction, and on a smaller grid it happens faster.
- Averaging the rule over the whole population gives continuous mean-field equations, a cyclic relative of Lotka-Volterra. In finite well-mixed populations, neutral cycles are vulnerable to drift. Spatial waves can damp that drift.

## Read Next

- [Volterra, Fluctuations in the Abundance of a Species considered Mathematically](https://doi.org/10.1038/118558a0) - early predator-prey equations, alongside Lotka's 1925 treatment.
- [Reichenbach, Mobilia, and Frey, Mobility promotes and jeopardizes biodiversity in rock-paper-scissors games](https://doi.org/10.1038/nature06095) - spiral waves and how mixing destroys coexistence.
- [May and Leonard, Nonlinear aspects of competition between three species](https://doi.org/10.1137/0129022) - the cyclic three-species model.
