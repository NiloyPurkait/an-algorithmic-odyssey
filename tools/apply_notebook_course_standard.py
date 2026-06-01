"""Append the course-standard visual/rigor studio block to every notebook."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
MARKER = "visual_rigor_studio_v1"


TOPICS = {
    "01-foundations/00-begin-odyssey/algorithmic-thinking.ipynb": {
        "problem": "Build the habit of tracing state and predicting growth before measuring it.",
        "visual": "Plot input size against operation count and let students scrub through growth classes.",
        "invariant": "The cost model must count the same operation under the same assumptions for every input size.",
        "complexity": "Separate constants, lower-order terms, and asymptotic growth.",
        "failure": "Wall-clock timing can lie when setup cost, cache behavior, or random input shape dominates.",
        "studio": "Measure two algorithms on the same input family, then explain where the empirical curve stops matching the asymptotic story.",
        "demo": "trace_template",
    },
    "01-foundations/00-begin-odyssey/sorting.ipynb": {
        "problem": "Turn unordered values into ordered structure using comparisons.",
        "visual": "Animate comparisons, swaps, settled regions, and operation counts on a bar chart.",
        "invariant": "Each pass increases the portion of the array known to be in final sorted order.",
        "complexity": "Compare best, average, and worst cases instead of giving one number.",
        "failure": "A visually sorted-looking prefix may still hide a disordering element later in the array.",
        "studio": "Build a trace for another sorting algorithm and compare its visual rhythm with bubble sort.",
        "demo": "bubble_sort",
    },
    "01-foundations/02-levenshtein-distance/levenshtein-distance.ipynb": {
        "problem": "Find the cheapest edit path between two strings.",
        "visual": "Fill the dynamic-programming matrix cell by cell, highlighting the three predecessor choices.",
        "invariant": "Every filled cell stores the optimal edit distance for two prefixes.",
        "complexity": "O(mn) time and O(mn) space, with a space-optimized O(min(m,n)) variant.",
        "failure": "The numeric distance ignores semantic meaning unless paired with a language model or frequency prior.",
        "studio": "Trace three candidate corrections and explain why the best edit distance is not always the best correction.",
        "demo": "levenshtein",
    },
    "01-foundations/03-gale-shapley/gale-shapley.ipynb": {
        "problem": "Find a stable matching through local proposals.",
        "visual": "Animate proposal arrows, rejections, and tentative matches as preferences narrow.",
        "invariant": "A receiver's tentative match can only improve according to that receiver's preference list.",
        "complexity": "At most n^2 proposals because each proposer asks each receiver at most once.",
        "failure": "The proposer-optimal result may be receiver-pessimal, so fairness depends on who proposes.",
        "studio": "Switch the proposing side and compare both the matching and the rejected proposal history.",
        "demo": "trace_template",
    },
    "01-foundations/04-huffman-coding/huffman-coding.ipynb": {
        "problem": "Compress symbols by giving frequent symbols shorter codes.",
        "visual": "Animate the priority queue as the two smallest trees merge into a new tree.",
        "invariant": "The two least frequent remaining subtrees can be siblings in some optimal prefix code.",
        "complexity": "O(k log k) for k distinct symbols with a priority queue.",
        "failure": "Huffman coding is optimal for independent symbol frequencies, not for context-dependent language structure.",
        "studio": "Compare a natural-language sample and a uniform sample; explain how the tree shape changes.",
        "demo": "trace_template",
    },
    "01-foundations/05-turing-universal-machine/universal-turing-machine.ipynb": {
        "problem": "Model computation as state, tape, and transition rules.",
        "visual": "Animate the tape head, current state, read symbol, write symbol, and movement direction.",
        "invariant": "At each step, the machine configuration is fully described by state, tape, and head position.",
        "complexity": "Discuss steps until halting; some machines have no finite bound because they do not halt.",
        "failure": "A tiny transition-table mistake can change halting behavior completely.",
        "studio": "Create a two-state machine, trace it for 20 steps, and state whether you expect it to halt.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/00-topological-sort/topological-sort.ipynb": {
        "problem": "Order tasks while respecting directed dependencies.",
        "visual": "Animate in-degree counts, ready nodes, emitted order, and cycle detection.",
        "invariant": "Every emitted node has no unmet incoming dependency.",
        "complexity": "O(V + E) with adjacency lists and an in-degree queue.",
        "failure": "A directed cycle means no valid topological order exists.",
        "studio": "Add one dependency that creates a cycle and show exactly where the ready queue empties.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/01-minimum-spanning-tree/minimum-spanning-tree.ipynb": {
        "problem": "Connect all vertices with minimum total edge cost.",
        "visual": "Animate sorted candidate edges, accepted edges, rejected cycles, and connected components.",
        "invariant": "By the cut property, the cheapest safe edge across a cut can be part of an MST.",
        "complexity": "O(E log E) for Kruskal plus near-constant union-find operations.",
        "failure": "A disconnected graph has a minimum spanning forest, not a single spanning tree.",
        "studio": "Change one edge weight and identify the first decision in the trace that changes.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/02-dijkstra/dijkstra.ipynb": {
        "problem": "Find shortest paths from one source when all edge weights are nonnegative.",
        "visual": "Animate settled nodes, frontier distances, and edge relaxations on the graph.",
        "invariant": "Once a node is settled, no unsettled route can produce a shorter path to it.",
        "complexity": "O((V + E) log V) with a heap; simpler teaching versions are O(V^2).",
        "failure": "Negative edge weights break the settled-node invariant.",
        "studio": "Add a negative edge and explain why the visual trace becomes misleading.",
        "demo": "dijkstra",
    },
    "02-spatial-graphs/03-a-star/a-star.ipynb": {
        "problem": "Use a heuristic to guide shortest-path search toward a goal.",
        "visual": "Animate open set, closed set, g-score, h-score, and f-score layers.",
        "invariant": "With an admissible and consistent heuristic, the first goal popped has optimal cost.",
        "complexity": "Worst-case exponential in path depth, but often far less search than uninformed methods.",
        "failure": "An overconfident heuristic can skip the true shortest path.",
        "studio": "Weaken and strengthen the heuristic, then compare the number of expanded nodes.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/04-voronoi-delaunay/voronoi-delaunay.ipynb": {
        "problem": "Turn scattered coordinate points into nearest-site regions and natural-neighbor graph edges.",
        "visual": "Animate sampled Voronoi territories, Delaunay edges, and a moving user point that changes ownership.",
        "invariant": "Each sampled location belongs to the site with minimum squared Euclidean distance.",
        "complexity": "Naive territory coloring is O(samples * sites); efficient planar Voronoi construction is O(n log n).",
        "failure": "Duplicate, nearly collinear, or edge-heavy point sets can create degenerate or unbounded geometry.",
        "studio": "Move three user points, identify their nearest sites, and explain one Delaunay edge as a shared Voronoi boundary.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/05-floyd-warshall/floyd-warshall.ipynb": {
        "problem": "Find every shortest path between every pair of nodes.",
        "visual": "Animate the distance matrix as each intermediate node becomes allowed.",
        "invariant": "After phase k, each entry is optimal using only the first k nodes as intermediates.",
        "complexity": "O(V^3) time and O(V^2) space.",
        "failure": "A negative cycle makes shortest distance undefined because cost can decrease forever.",
        "studio": "Choose one matrix cell and narrate the exact intermediate node that improves it.",
        "demo": "trace_template",
    },
    "02-spatial-graphs/06-edmonds-karp/edmonds-karp.ipynb": {
        "problem": "Move as much flow as possible from source to sink under capacity constraints.",
        "visual": "Animate BFS augmenting paths, bottleneck capacities, residual edges, and the final cut.",
        "invariant": "Flow conservation holds at every non-source and non-sink node after each augmentation.",
        "complexity": "O(VE^2), with each BFS choosing a shortest augmenting path in edge count.",
        "failure": "Ignoring residual back edges hides the ability to undo earlier local decisions.",
        "studio": "Lower one capacity and identify the first bottleneck that changes the final max flow.",
        "demo": "trace_template",
    },
    "03-natural-emergence/00-game-of-life/game-of-life.ipynb": {
        "problem": "Watch global behavior emerge from local neighbor rules.",
        "visual": "Animate generations on a grid with live-cell count and pattern classification.",
        "invariant": "The next board is computed synchronously from the current board, not updated in place.",
        "complexity": "O(generations * rows * columns).",
        "failure": "In-place updates accidentally let future cells influence the same generation.",
        "studio": "Trace a glider and one random seed; classify death, stability, oscillator, or movement.",
        "demo": "game_of_life",
    },
    "03-natural-emergence/01-schelling-segregation/schelling-segregation.ipynb": {
        "problem": "Show how local satisfaction rules can amplify into macro-level segregation.",
        "visual": "Animate a red/blue/empty grid through movement rounds with threshold and vacancy controls.",
        "invariant": "Each move preserves the counts of red agents, blue agents, and empty cells.",
        "complexity": "A naive round is O(n^2) for an n by n grid, with constant-size neighbor checks.",
        "failure": "Threshold, vacancy, boundary, or movement-rule changes can substantially change the macro-pattern.",
        "studio": "Run three thresholds and compare final same-neighbor ratio while naming what the model omits.",
        "demo": "trace_template",
    },
    "03-natural-emergence/02-boids/boids.ipynb": {
        "problem": "Model flocking as local steering among autonomous agents.",
        "visual": "Animate positions, velocity arrows, neighborhoods, alignment, cohesion, separation, and predator avoidance.",
        "invariant": "Each agent updates from the current snapshot of nearby agents before the next positions are accepted.",
        "complexity": "The direct neighborhood calculation is O(steps * agents^2); spatial indexing can reduce the neighbor search.",
        "failure": "Overweighting one steering rule can freeze the flock, scatter it, or collapse it into a clump.",
        "studio": "Compare balanced, scattered, and predator-driven flocks, then connect one metric to what the animation shows.",
        "demo": "trace_template",
    },
    "03-natural-emergence/03-biomorphs/biomorphs.ipynb": {
        "problem": "Show cumulative artificial selection over a compact integer genome.",
        "visual": "Animate a parent biomorph surrounded by eight mutated children, then promote the selected child.",
        "invariant": "Every child is a bounded integer mutation of its parent, and every drawing is deterministic from its genes.",
        "complexity": "Drawing a binary recursive biomorph is O(2^d) in depth d, capped by the depth gene.",
        "failure": "Too little mutation stagnates; too much mutation breaks parent-child continuity; high depth explodes branch count.",
        "studio": "Record a 10-generation lineage and distinguish random mutation from non-random selection.",
        "demo": "trace_template",
    },
    "03-natural-emergence/04-turing-patterns/turing-patterns.ipynb": {
        "problem": "Generate pattern from interacting chemical fields.",
        "visual": "Animate activator and inhibitor fields beside sliders for diffusion and reaction rates.",
        "invariant": "Each step applies the same local update rule to every cell in the field.",
        "complexity": "O(steps * rows * columns) for a fixed local stencil.",
        "failure": "Unstable parameters or time steps can create numerical artifacts instead of meaningful patterns.",
        "studio": "Move one parameter across a threshold and describe the pattern transition.",
        "demo": "trace_template",
    },
    "03-natural-emergence/05-perlin-noise/perlin-noise.ipynb": {
        "problem": "Create smooth pseudo-random structure for terrain and texture.",
        "visual": "Animate octaves accumulating into a final terrain map.",
        "invariant": "Nearby points share related gradients, which makes the output smooth rather than white noise.",
        "complexity": "O(samples * octaves) for a generated grid.",
        "failure": "Too many high-frequency octaves can erase the smoothness that makes Perlin noise useful.",
        "studio": "Compare one-octave terrain with multi-octave terrain and name the visual tradeoff.",
        "demo": "trace_template",
    },
    "03-natural-emergence/06-penrose-tiling/tiling.ipynb": {
        "problem": "Create non-repeating order through recursive geometric substitution.",
        "visual": "Animate deflation steps, color tile types, and preserve matching constraints.",
        "invariant": "Each substitution preserves the local matching rules that prevent periodic repetition.",
        "complexity": "Tile count grows exponentially with deflation depth.",
        "failure": "Floating-point drift can create tiny cracks unless geometry is handled carefully.",
        "studio": "Track one tile lineage through two deflations and explain what changes and what persists.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/00-bloom-filters/bloom-filters.ipynb": {
        "problem": "Trade exact membership for compact probabilistic memory.",
        "visual": "Animate hash functions setting bits and queries checking all required positions.",
        "invariant": "Inserted items never become false negatives as long as bits are never cleared.",
        "complexity": "O(k) insert and lookup for k hash functions.",
        "failure": "False positives rise as the bit array saturates.",
        "studio": "Keep the item count fixed, shrink the array, and measure how the false-positive rate changes.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/01-markov-chains/markov-chains.ipynb": {
        "problem": "Model a system whose next state depends only on its current state.",
        "visual": "Animate probability mass flowing through a transition graph over time.",
        "invariant": "The probability vector sums to one after every transition.",
        "complexity": "One dense transition step is O(n^2); sparse chains can be much cheaper.",
        "failure": "Reducibility or periodicity can prevent simple convergence to one stable distribution.",
        "studio": "Alter one transition probability and compare the long-run state distribution.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/02-pagerank/pagerank.ipynb": {
        "problem": "Rank nodes by stable importance under a random-surfer model.",
        "visual": "Animate rank mass moving across links with damping and teleportation.",
        "invariant": "Rank remains a probability distribution after every update.",
        "complexity": "Power iteration is O(iterations * edges) on a sparse web graph.",
        "failure": "Dangling nodes and disconnected components require damping or special handling.",
        "studio": "Add one link farm and explain how damping limits its influence.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/03-kmeans-cluster/kmeans-cluster.ipynb": {
        "problem": "Partition points by alternating nearest centers and center updates.",
        "visual": "Animate assignments, centroid movement, and objective value per iteration.",
        "invariant": "Each assignment/update phase does not increase within-cluster squared error.",
        "complexity": "O(iterations * k * n * dimensions).",
        "failure": "Different initial centers can lead to different local optima.",
        "studio": "Run three initializations and compare the final clusters and objective values.",
        "demo": "kmeans",
    },
    "04-statistical-optimization/04-gradient-descent/gradient-descent.ipynb": {
        "problem": "Optimize a model by following the local slope of a loss function.",
        "visual": "Animate the current point moving on a loss curve or surface with learning-rate control.",
        "invariant": "For a sufficiently small step on a smooth function, moving against the gradient locally lowers loss.",
        "complexity": "O(iterations * cost_of_gradient), with convergence depending on curvature and step size.",
        "failure": "A large learning rate can overshoot or diverge; nonconvex losses can trap local minima.",
        "studio": "Run three learning rates and classify each as slow, stable, or unstable.",
        "demo": "gradient_descent",
    },
    "04-statistical-optimization/05-penrose-linear-algebra/pseudoinverse.ipynb": {
        "problem": "Solve imperfect linear systems with least-squares structure.",
        "visual": "Animate projection onto column space and singular-value filtering.",
        "invariant": "The pseudoinverse solution minimizes residual norm and, when underdetermined, solution norm.",
        "complexity": "SVD-based methods are typically O(min(mn^2, m^2n)) for an m by n matrix.",
        "failure": "Tiny singular values amplify noise unless regularized or truncated.",
        "studio": "Perturb a nearly singular matrix and explain how the solution changes.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/05-penrose-linear-algebra/graph-notation.ipynb": {
        "problem": "Represent tensor and matrix operations as diagrams.",
        "visual": "Animate contraction by removing connected index wires and updating tensor shapes.",
        "invariant": "Connected wires represent summed indices; free wires represent output axes.",
        "complexity": "Contraction order can change cost by orders of magnitude.",
        "failure": "A visually simple diagram may hide an expensive intermediate tensor.",
        "studio": "Draw two contraction orders for the same expression and compare intermediate sizes.",
        "demo": "trace_template",
    },
    "04-statistical-optimization/06-fast-fourier-transform/fft.ipynb": {
        "problem": "Reveal frequency structure by evaluating a transform efficiently.",
        "visual": "Animate recursive even/odd splits and butterfly recombination.",
        "invariant": "Each butterfly combines two smaller transforms using roots of unity.",
        "complexity": "O(n log n), compared with O(n^2) for direct DFT.",
        "failure": "Sampling below the Nyquist rate aliases high frequencies into false low frequencies.",
        "studio": "Mix two sine waves, transform them, and identify both peaks.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/00-min-max/min-max.ipynb": {
        "problem": "Choose moves against an opponent who also chooses optimally.",
        "visual": "Animate game-tree expansion and value backup from leaves to root.",
        "invariant": "A max node takes the best child value; a min node takes the worst child value for max.",
        "complexity": "O(b^d) for branching factor b and depth d before pruning or heuristics.",
        "failure": "Wrong evaluation functions make limited-depth search confidently choose bad moves.",
        "studio": "Change one leaf value and trace whether the root decision changes.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/01-monte-carlo-search-tree/monte-carlo-search-tree.ipynb": {
        "problem": "Search huge game trees by sampling promising branches.",
        "visual": "Animate selection, expansion, rollout, and backpropagation with visit counts and win rates.",
        "invariant": "Backpropagated statistics summarize all simulations that passed through a node.",
        "complexity": "Budget-driven; cost is roughly playouts times rollout length.",
        "failure": "Too few playouts can overfit noise; poor rollout policy can bias the estimates.",
        "studio": "Double the playout budget until the recommended move stabilizes.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/02-ant-colony/ant-colony.ipynb": {
        "problem": "Use local agents and pheromone memory to search hard route spaces.",
        "visual": "Animate ant tours, pheromone evaporation, and reinforced edges.",
        "invariant": "Edges used by better solutions receive stronger reinforcement after each generation.",
        "complexity": "Budget-driven; cost scales with ants, iterations, and path construction length.",
        "failure": "Too much reinforcement too early can converge prematurely on a poor route.",
        "studio": "Change evaporation and explain whether exploration or exploitation dominates.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/02-ant-colony/genetic-algorithms.ipynb": {
        "problem": "Evolve candidate solutions using selection, crossover, and mutation.",
        "visual": "Animate population fitness distribution, parents, offspring, and mutation events.",
        "invariant": "Selection pressure increases high-fitness representation while mutation preserves variation.",
        "complexity": "Budget-driven; cost is population size times generations times fitness cost.",
        "failure": "Low diversity causes premature convergence; high mutation prevents refinement.",
        "studio": "Run low and high mutation rates and compare both best fitness and diversity.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/03-turing-enigma/enigma.ipynb": {
        "problem": "Understand encryption as a deterministic state machine.",
        "visual": "Animate rotor positions, signal path, reflection, and stepping after each character.",
        "invariant": "For a fixed state, Enigma maps each letter through a reversible wiring path.",
        "complexity": "Encryption is O(message length), while brute-force key search grows with the key space.",
        "failure": "Operational patterns and repeated settings can leak structure despite strong-looking machinery.",
        "studio": "Encrypt the same letter repeatedly and explain why outputs change.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/04-rsa/rsa.ipynb": {
        "problem": "Build public-key cryptography from modular arithmetic and factoring hardness.",
        "visual": "Animate modular exponentiation as repeated squaring and show key generation dependencies.",
        "invariant": "The public/private exponents are modular inverses modulo phi(n) or lambda(n).",
        "complexity": "Modular exponentiation is polynomial in bit length; factoring large n is the hard classical step.",
        "failure": "Small primes, bad padding, or reused structure can break RSA even without factoring.",
        "studio": "Generate a tiny key, encrypt one message, and trace each repeated-squaring step.",
        "demo": "trace_template",
    },
    "05-adversarial-and-quantum/05-shors-algorithm/shors-algorithm.ipynb": {
        "problem": "Convert factoring into period finding, then use quantum structure to accelerate the hard part.",
        "visual": "Animate modular powers forming a period and connect that period to a factor attempt.",
        "invariant": "If a chosen base has an even period r and a^(r/2) is not -1 mod n, gcd reveals a factor.",
        "complexity": "Quantum period finding is polynomial in bit length; the classical factoring baseline is not known to be polynomial.",
        "failure": "Some random bases produce unusable periods, so Shor repeats the attempt.",
        "studio": "For a small n, compute modular powers, find the period, and test the gcd step manually.",
        "demo": "trace_template",
    },
}


DEMO_CODE = {
    "bubble_sort": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, bubble_sort_trace, render_array_bars, render_trace_table

trace = bubble_sort_trace([5, 1, 4, 2, 8])
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_array_bars).display()
""",
    "levenshtein": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, levenshtein_trace, render_matrix, render_trace_table

trace = levenshtein_trace("kitten", "sitting")
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_matrix).display()
""",
    "dijkstra": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, dijkstra_trace, render_dijkstra_graph, render_trace_table

sample_graph = {
    "A": {"B": 2, "C": 5},
    "B": {"A": 2, "C": 1, "D": 4},
    "C": {"A": 5, "B": 1, "D": 1},
    "D": {"B": 4, "C": 1},
}
trace = dijkstra_trace(sample_graph, "A")
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_dijkstra_graph).display()
""",
    "game_of_life": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, game_of_life_trace, render_grid, render_trace_table

glider = [
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]
trace = game_of_life_trace(glider, steps=12)
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_grid).display()
""",
    "kmeans": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, kmeans_trace, render_kmeans, render_trace_table

points = [(1, 1), (1.2, 1.4), (0.8, 0.7), (4, 4), (4.3, 3.8), (3.7, 4.2)]
centers = [(0.5, 1.8), (4.8, 3.5)]
trace = kmeans_trace(points, centers, steps=4)
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_kmeans).display()
""",
    "gradient_descent": """
from pathlib import Path
import sys
from IPython.display import display

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware.visual_tracing import AlgorithmPlayer, gradient_descent_trace, render_gradient_descent, render_trace_table

f = lambda x: (x - 1.5) ** 2 + 0.4
df = lambda x: 2 * (x - 1.5)
trace = gradient_descent_trace(f, df, x0=-3, learning_rate=0.25, steps=10, domain=(-4, 4))
display(render_trace_table(trace))
AlgorithmPlayer(trace, render_gradient_descent).display()
""",
    "trace_template": """
from pathlib import Path
import sys

for candidate in [Path.cwd().resolve(), *Path.cwd().resolve().parents]:
    if (candidate / "courseware").exists():
        sys.path.insert(0, str(candidate))
        break

from courseware import AlgorithmPlayer, AlgorithmTrace, TraceStep, render_trace_table

# Convert the implementation above into snapshots:
# trace = AlgorithmTrace("Topic trace")
# trace.append("start", {"your_state": ...}, "What changed?", invariant="What remains true?")
# AlgorithmPlayer(trace, your_renderer).display()
print("Use AlgorithmTrace to turn this notebook's algorithm into a step-by-step visual player.")
""",
}


def markdown_cell(topic: dict[str, str]) -> dict:
    source = f"""
## Visual Trace + Rigor Studio

**Problem frame.** {topic["problem"]}

**Interactive animation target.** {topic["visual"]}

**Correctness handle.** {topic["invariant"]}

**Complexity handle.** {topic["complexity"]}

**Failure mode to test.** {topic["failure"]}

**Studio task.** {topic["studio"]}
"""
    return {
        "cell_type": "markdown",
        "metadata": {"course_upgrade": MARKER},
        "source": dedent(source).strip() + "\n",
    }


def code_cell(topic: dict[str, str]) -> dict:
    source = dedent(DEMO_CODE[topic["demo"]]).strip() + "\n"
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {"course_upgrade": MARKER},
        "outputs": [],
        "source": source,
    }


def main() -> None:
    for relative, topic in TOPICS.items():
        path = ROOT / relative
        notebook = json.loads(path.read_text(encoding="utf-8"))
        cells = [
            cell
            for cell in notebook.get("cells", [])
            if cell.get("metadata", {}).get("course_upgrade") != MARKER
        ]
        cells.append(markdown_cell(topic))
        cells.append(code_cell(topic))
        notebook["cells"] = cells
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"standardized {relative}")


if __name__ == "__main__":
    main()
