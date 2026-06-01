# Exercises

These prompts turn the notebooks into practice. Each exercise should produce three things: a prediction, a changed input or parameter, and one sentence explaining the observed result.

For full course assignments with implementation, proof, visual traces, and rubrics, use the [problem sets](../problem-sets/README.md). This file is the lightweight studio-practice layer.

## Module 1: Foundations

- Change the input sizes in the sorting notebook and describe how runtime growth changes.
- Turn the Antikythera crank by 19 years and explain why the Moon phase nearly returns.
- Use Levenshtein distance to rank three possible corrections for the same misspelled word.
- Compress a different text sample with Huffman coding and identify which symbol saved the most bits.
- Run one more Penrose deflation step and count how the tile total grows with depth.
- Checkpoint: build a tiny spelling helper that combines edit distance with frequency or compression statistics, then compare its symbolic computation with the Antikythera notebook's physical ratio computation.

## Module 2: Spatial Graphs

- Add one dependency to the topological-sort graph and predict how the order changes.
- Add one expensive edge to Dijkstra, then compare the chosen path before and after.
- Run A* with a weaker heuristic and note whether it explores more nodes.
- Move a user point through a Voronoi diagram and identify where cell ownership changes.
- Lower one capacity in Edmonds-Karp and identify the new bottleneck.
- Checkpoint: design a delivery network and explain which graph or geometry algorithm answers each planning question.

## Module 3: Natural Emergence

- Change a Game of Life starting pattern and track whether it dies, stabilizes, or moves.
- Change Schelling's satisfaction threshold and compare the final same-neighbor ratio.
- Seed the Prisoner's Dilemma grid with all three strategies and find the generation where defectors peak before Tit-for-Tat clusters take over.
- Tune Boids separation, alignment, or cohesion and describe how the flock changes.
- Adjust reaction-diffusion parameters and describe the visible pattern shift.
- Checkpoint: create a small social grid or simulation from one compact rule system, then explain whether structure comes from local interaction, movement, or strategy.

## Module 4: Statistical Optimization

- Tune a Bloom filter to use less memory and measure the false-positive tradeoff.
- Change a Markov transition probability and describe the new long-run behavior.
- Add a page to the PageRank graph and predict which ranks move.
- Change the number of clusters in k-means and explain whether the grouping improves.
- Change a gradient descent learning rate and compare convergence speed or instability.
- Change Perlin noise octaves or persistence and compare smooth output against rough output.
- Checkpoint: analyze a small dataset or network and state which answers are exact, estimated, or optimized.

## Module 5: Strategic Search and Metaheuristics

- Change a Minimax board position and explain the best move.
- Increase MCTS playouts and compare whether the recommended move becomes more stable.
- Change Ant Colony or Genetic Algorithm parameters and compare solution quality.
- Select Biomorph children for 10 generations and describe which visual traits accumulate under cumulative selection.
- Checkpoint: take one hard search problem and compare how exhaustive search, sampling (MCTS), and a metaheuristic each scale.

## Module 6: Cryptography and Quantum Frontiers

- Encrypt a new message with Enigma and trace how rotor state changes the output.
- Generate a small RSA keypair, encrypt a short message, then explain why factoring `n` would break it.
- Run the zero-knowledge cave verifier for `k` rounds, compute the cheat's success `(1/2)^k`, and find the `k` that beats one in a million; then make the challenge predictable and watch a cheat pass every round.
- Run Grover's algorithm on 8 states, watch the target probability peak at two iterations, then keep iterating and explain why over-rotation makes it worse.
- Build a modular-power table for a small composite and find the period, the way Shor's algorithm relies on.
- Checkpoint: connect RSA's factoring assumption to Shor's period finding and explain what changes what is practical.

## Response Standard

A strong student response is short but concrete:

1. Prediction: what should change and why.
2. Run: what input, parameter, or rule changed.
3. Observation: what actually happened.
4. Transfer: where the same idea appears in another notebook.
