# Visual Trace Standard

This course should make computation visible. Each major notebook should expose the algorithm as a sequence of trace steps, then let students pause, step, and inspect the changing state.

## Minimum Standard

Every visual trace should show:

- the current operation
- the state before or after that operation
- the data structure that changed
- the invariant that remains true
- one or more counters such as comparisons, relaxations, iterations, flow, loss, or visits
- a failure case students can test

## Shared Pattern

Use the shared `courseware` package:

```python
from courseware import AlgorithmPlayer, AlgorithmTrace, render_trace_table

trace = AlgorithmTrace(
    "My Algorithm Trace",
    objective="What the algorithm is trying to accomplish.",
    complexity="The relevant time and space cost.",
)

trace.append(
    "start",
    {"state_name": initial_state},
    "What the learner should notice.",
    invariant="What is guaranteed to remain true.",
    operation="initialize",
)

display(render_trace_table(trace))
AlgorithmPlayer(trace, renderer=my_renderer).display()
```

## Renderer Targets

| Data Structure | Recommended Visual |
| --- | --- |
| Array | bars, highlighted indices, settled region |
| Matrix | heatmap, active cell, predecessor cells |
| Graph | nodes, edges, frontier, settled/visited nodes |
| Tree | expanded nodes, backed-up values, selected branch |
| Grid | cellular state, local neighborhood, generation counter |
| Probability vector | mass flow, stacked bars, long-run distribution |
| Optimization | loss curve, current point, trajectory, step size |
| Cryptography | state machine path, modular cycle, key dependency graph |
| Quantum period finding | modular-power cycle, period marker, gcd attempt |

## Interaction Standard

A strong trace answers four questions at every frame:

1. What just happened?
2. What changed?
3. What is still guaranteed?
4. What would break if an assumption changed?

## Notebook Contract

Each notebook now ends with a `Visual Trace + Rigor Studio` section. That section is the acceptance checklist for upgrading the notebook's animation:

- implement the animation target
- state the correctness handle
- justify the complexity handle
- test the failure mode
- complete the studio task

The shared `courseware.visual_tracing` module includes examples for bubble sort, Levenshtein distance, Dijkstra, Game of Life, k-means, and gradient descent. Other notebooks should follow the same trace shape.
