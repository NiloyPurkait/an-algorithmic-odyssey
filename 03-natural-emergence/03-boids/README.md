# Boids

Boids turns flocking into three local vector rules. Each agent steers away from crowding, toward nearby headings, and toward nearby positions. Local motion rules create coordinated swarm behavior without a leader.

## Open

- [boids.ipynb](boids.ipynb)

## What To Watch

- Separation avoids crowding.
- Alignment adjusts heading toward nearby agents.
- Cohesion pulls an agent toward the local center of mass.
- Neighborhood radius and force limits often change the behavior more than the rule names suggest.

## Read Next

- [Reynolds, Flocks, Herds, and Schools](https://www.red3d.com/cwr/papers/1987/boids.html) - original paper page.
- [Reynolds, Steering Behaviors for Autonomous Characters](https://www.red3d.com/cwr/steer/) - steering rules beyond flocking.
- [Nature-inspired flocking overview on PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5686407/) - survey context for swarm models.
