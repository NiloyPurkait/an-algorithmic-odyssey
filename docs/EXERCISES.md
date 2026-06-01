# Exercises

These prompts turn the notebooks into practice. Each exercise should produce three things: a prediction, a changed input or parameter, and one sentence explaining the observed result.

For full course assignments with implementation, proof, visual traces, and rubrics, use the [problem sets](../problem-sets/README.md). This file is the lightweight studio-practice layer.

## Module 1: Foundations

- Change the input sizes in the sorting notebook and describe how runtime growth changes.
- Turn the Antikythera crank by 19 years and explain why the Moon phase nearly returns.
- Use Levenshtein distance to rank three possible corrections for the same misspelled word.
- Compress a different text sample with Huffman coding and identify which symbol saved the most bits.
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
- Tune Boids separation, alignment, or cohesion and describe how the flock changes.
- Select Biomorph children for 10 generations and describe which visual traits accumulate.
- Adjust reaction-diffusion parameters and describe the visible pattern shift.
- Change Perlin noise octaves or persistence and compare smooth terrain against rough terrain.
- Run one more Penrose deflation step and describe what stays ordered despite never repeating.
- Checkpoint: create a small generated world, social grid, or organism set from one compact rule system, then explain whether structure comes from local interaction, movement, recursion, or selection.

## Module 4: Statistical Optimization

- Tune a Bloom filter to use less memory and measure the false-positive tradeoff.
- Change a Markov transition probability and describe the new long-run behavior.
- Add a page to the PageRank graph and predict which ranks move.
- Change the number of clusters in k-means and explain whether the grouping improves.
- Change a gradient descent learning rate and compare convergence speed or instability.
- Checkpoint: analyze a small dataset or network and state which answers are exact, estimated, or optimized.

## Module 5: Strategic Intelligence and Quantum Frontiers

- Change a Minimax board position and explain the best move.
- Increase MCTS playouts and compare whether the recommended move becomes more stable.
- Change Ant Colony or Genetic Algorithm parameters and compare solution quality.
- Encrypt a new message with Enigma and trace how rotor state changes the output.
- Generate a small RSA keypair, encrypt a short message, then explain what Shor's algorithm threatens.
- Checkpoint: compare where exhaustive search, random sampling, and quantum period finding each change what is practical.

## Response Standard

A strong student response is short but concrete:

1. Prediction: what should change and why.
2. Run: what input, parameter, or rule changed.
3. Observation: what actually happened.
4. Transfer: where the same idea appears in another notebook.
