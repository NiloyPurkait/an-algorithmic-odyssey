# Spatial Predator-Prey

A grid of grass, rabbits, and foxes runs on one local rule in a cycle: rabbits graze grass into new rabbits, foxes eat rabbits into new foxes, and a fox with no prey nearby starves so the ground returns to grass. From a random start this organizes itself into rotating spiral waves that let all three species coexist indefinitely. Remove the space - shuffle the grid so the population is well-mixed, the assumption the classic Lotka-Volterra equations make - and the spirals cannot form, the cycle drifts, and a species goes extinct. It bridges discrete cellular rules to the continuous differential equations of population ecology, and shows that space itself can stabilize coexistence.

## Open

- [predator-prey.ipynb](predator-prey.ipynb)

## What To Watch

- Each cell flips to its cyclic successor (grass to rabbit to fox to grass) only when enough neighbors already are it, so one local rule drives everything.
- Cyclic dominance plus space produces rotating spiral waves, and the three populations cycle while staying balanced near a third each.
- The failure mode is removing space: a well-mixed grid loses a species to extinction, and on a smaller grid it happens faster.
- Averaging the rule over the whole grid gives the continuous mean-field equations, whose neutrally stable boom-bust cycles drift to extinction without space to damp them.

## Read Next

- [Volterra, Variazioni e fluttuazioni del numero d'individui in specie animali conviventi](https://doi.org/10.1038/118558a0) - the original predator-prey equations (with Lotka, 1925-1926).
- [Reichenbach, Mobilia, and Frey, Mobility promotes and jeopardizes biodiversity in rock-paper-scissors games](https://doi.org/10.1038/nature06095) - spiral waves and how mixing destroys coexistence.
- [May and Leonard, Nonlinear aspects of competition between three species](https://doi.org/10.1137/0129022) - the cyclic three-species model.
