# Problem Set 3: Natural Emergence

## Goals

Students should be able to distinguish local rules from global patterns, design parameter experiments, and recognize numerical artifacts.

## Problems

### 1. Cellular Automaton Trace

Run Game of Life from three initial states: one that dies, one that stabilizes, and one that moves or oscillates.

Deliverables:

- animation or generation snapshots
- live-cell count over time
- classification of each pattern
- explanation of synchronous update

### 2. Social Emergence and Segregation

Run Schelling's segregation model with at least three satisfaction thresholds.

Deliverables:

- initial and final grid snapshots for each threshold
- happy fraction over time
- mean same-neighbor ratio or cluster-size metric
- explanation of why a local tolerance threshold does not determine global mixing by itself
- short note about what the model omits about real segregation

### 3. Cooperation on a Grid

Run the spatial Prisoner's Dilemma seeded with Always Defect, Always Cooperate, and Tit-for-Tat.

Deliverables:

- grid snapshots at the start, at the defector peak, and at the final generation
- population fraction of each strategy over generations
- explanation of why Tit-for-Tat clusters survive while isolated cooperators are eaten
- one-shot test: set the iterated rounds to 1 and explain why cooperation collapses without the shadow of the future

### 4. Flocking and Swarm Behavior

Run the Boids simulation with at least two parameter settings: one coherent flock and one unstable or scattered flock.

Deliverables:

- animation or three time snapshots
- a short table of separation, alignment, and cohesion weights
- one metric such as alignment score or mean nearest-neighbor distance
- explanation of how local steering rules produce the observed group motion

### 5. Reaction-Diffusion Parameter Sweep

Choose two Turing-pattern parameter settings.

Deliverables:

- side-by-side final fields
- one animation or sequence of frames
- explanation of which parameter changed
- note about numerical stability, boundary conditions, or time-step sensitivity

### 6. Generated World Mini-Project

Combine at least two emergence rules into one small world. The rules can be grid-based, agent-based, or field-based.

Deliverables:

- visual output
- one parameter change
- prediction before the run
- observation after the run

## Reflection

Where else in the course do repeated local rules produce behavior that is hard to predict from one step alone?
