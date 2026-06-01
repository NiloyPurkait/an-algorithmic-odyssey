# Boids

Craig Reynolds introduced Boids in the late 1980s as an artificial-life model for coordinated animal motion. Instead of scripting a flock, each agent follows local steering rules for separation, alignment, and cohesion. Flocking becomes vector arithmetic, and neighborhood interactions produce leaderless motion.

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
