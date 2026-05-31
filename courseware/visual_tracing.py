"""Reusable visual tracing tools for algorithm notebooks.

The course uses a common pattern:

1. Run an algorithm while recording small state snapshots.
2. Attach an invariant, operation count, and short explanation to each step.
3. Play those steps back with a renderer that fits the data structure.

The helpers below are intentionally dependency-light. They use matplotlib for
rendering and ipywidgets when available; without widgets, a notebook still gets
static frames and trace tables.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from html import escape
from math import ceil, cos, pi, sin
from typing import Any, Callable, Iterable, Mapping, Sequence


@dataclass
class TraceStep:
    """One inspectable moment in an algorithm run."""

    label: str
    state: dict[str, Any]
    description: str = ""
    focus: dict[str, Any] = field(default_factory=dict)
    metrics: dict[str, Any] = field(default_factory=dict)
    invariant: str = ""
    operation: str = ""


@dataclass
class AlgorithmTrace:
    """A named list of TraceStep objects."""

    title: str
    steps: list[TraceStep] = field(default_factory=list)
    objective: str = ""
    complexity: str = ""

    def append(
        self,
        label: str,
        state: Mapping[str, Any],
        description: str = "",
        focus: Mapping[str, Any] | None = None,
        metrics: Mapping[str, Any] | None = None,
        invariant: str = "",
        operation: str = "",
    ) -> None:
        self.steps.append(
            TraceStep(
                label=label,
                state=dict(state),
                description=description,
                focus=dict(focus or {}),
                metrics=dict(metrics or {}),
                invariant=invariant,
                operation=operation,
            )
        )

    def __len__(self) -> int:
        return len(self.steps)

    def __iter__(self) -> Iterable[TraceStep]:
        return iter(self.steps)

    def __getitem__(self, index: int) -> TraceStep:
        return self.steps[index]


class AlgorithmPlayer:
    """Notebook player for stepping through an AlgorithmTrace."""

    def __init__(
        self,
        trace: AlgorithmTrace,
        renderer: Callable[[TraceStep], Any],
        interval: int = 700,
    ) -> None:
        if not trace.steps:
            raise ValueError("AlgorithmPlayer requires at least one TraceStep.")
        self.trace = trace
        self.renderer = renderer
        self.interval = interval

    def show(self, index: int = 0) -> Any:
        """Render one frame."""
        index = max(0, min(index, len(self.trace.steps) - 1))
        return self.renderer(self.trace.steps[index])

    def display(self) -> Any:
        """Display an interactive player when ipywidgets is available."""
        try:
            import ipywidgets as widgets
            from IPython.display import clear_output, display
        except Exception:
            return self.show(0)

        slider = widgets.IntSlider(
            value=0,
            min=0,
            max=len(self.trace.steps) - 1,
            step=1,
            description="step",
            continuous_update=False,
            readout=True,
        )
        play = widgets.Play(
            value=0,
            min=0,
            max=len(self.trace.steps) - 1,
            step=1,
            interval=self.interval,
            description="play",
        )
        reset = widgets.Button(description="reset", icon="refresh")
        widgets.jslink((play, "value"), (slider, "value"))
        output = widgets.Output()

        def render_frame(change: object | None = None) -> None:
            with output:
                clear_output(wait=True)
                display(self.renderer(self.trace.steps[slider.value]))

        def reset_frame(change: object | None = None) -> None:
            slider.value = 0
            play.value = 0
            render_frame()

        slider.observe(render_frame, names="value")
        reset.on_click(reset_frame)
        render_frame()
        display(widgets.VBox([widgets.HBox([play, reset, slider]), output]))
        return None


def render_trace_table(trace: AlgorithmTrace, max_rows: int = 12) -> Any:
    """Return an HTML overview of the first trace steps."""
    try:
        from IPython.display import HTML
    except Exception:
        rows = [f"{i}: {step.label} - {step.description}" for i, step in enumerate(trace.steps)]
        return "\n".join(rows[:max_rows])

    rows = []
    for i, step in enumerate(trace.steps[:max_rows]):
        metric_text = ", ".join(f"{k}={v}" for k, v in step.metrics.items())
        rows.append(
            "<tr>"
            f"<td>{i}</td>"
            f"<td>{escape(step.label)}</td>"
            f"<td>{escape(step.operation)}</td>"
            f"<td>{escape(step.invariant)}</td>"
            f"<td>{escape(metric_text)}</td>"
            "</tr>"
        )
    if len(trace.steps) > max_rows:
        rows.append(
            f"<tr><td colspan='5'>... {len(trace.steps) - max_rows} more steps</td></tr>"
        )
    return HTML(
        "<table>"
        "<thead><tr><th>Step</th><th>Label</th><th>Operation</th>"
        "<th>Invariant</th><th>Metrics</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def _figure(title: str = "", width: float = 7, height: float = 4):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(width, height))
    if title:
        ax.set_title(title)
    return fig, ax


def render_array_bars(step: TraceStep, key: str = "array") -> Any:
    """Render an array as bars with highlighted indices."""
    values = list(step.state[key])
    highlights = set(step.focus.get("indices", []))
    colors = ["#e4572e" if i in highlights else "#4c78a8" for i in range(len(values))]
    fig, ax = _figure(step.label)
    ax.bar(range(len(values)), values, color=colors)
    ax.set_xticks(range(len(values)))
    ax.set_ylim(0, max(values) * 1.2 if values else 1)
    ax.set_xlabel(step.description)
    for i, value in enumerate(values):
        ax.text(i, value, str(value), ha="center", va="bottom", fontsize=9)
    return fig


def render_matrix(step: TraceStep, key: str = "matrix") -> Any:
    """Render a numeric matrix with optional focused cell."""
    import matplotlib.pyplot as plt
    import numpy as np

    matrix = np.array(step.state[key])
    fig, ax = _figure(step.label, width=6, height=5)
    ax.imshow(matrix, cmap="YlGnBu")
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            ax.text(j, i, str(matrix[i, j]), ha="center", va="center", fontsize=8)
    if "cell" in step.focus:
        r, c = step.focus["cell"]
        ax.add_patch(plt.Rectangle((c - 0.5, r - 0.5), 1, 1, fill=False, lw=3, ec="#e4572e"))
    ax.set_xlabel(step.description)
    ax.set_xticks(range(matrix.shape[1]))
    ax.set_yticks(range(matrix.shape[0]))
    return fig


def render_grid(step: TraceStep, key: str = "grid") -> Any:
    """Render a grid or cellular automaton state."""
    matrix = step.state[key]
    fig, ax = _figure(step.label, width=5, height=5)
    ax.imshow(matrix, cmap="viridis", interpolation="nearest")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel(step.description)
    return fig


def render_dijkstra_graph(step: TraceStep) -> Any:
    """Render a weighted graph state without requiring networkx."""
    graph = step.state["graph"]
    distances = step.state.get("distances", {})
    visited = set(step.state.get("visited", []))
    current = step.state.get("current")
    nodes = sorted(graph.keys())
    positions = step.state.get("positions") or _circular_positions(nodes)
    fig, ax = _figure(step.label, width=7, height=5)

    drawn_edges: set[tuple[str, str]] = set()
    for src, edges in graph.items():
        for dst, weight in edges.items():
            edge_key = tuple(sorted((src, dst)))
            if edge_key in drawn_edges:
                continue
            drawn_edges.add(edge_key)
            x1, y1 = positions[src]
            x2, y2 = positions[dst]
            ax.plot([x1, x2], [y1, y2], color="#9aa0a6", lw=1.5, zorder=1)
            ax.text((x1 + x2) / 2, (y1 + y2) / 2, str(weight), fontsize=8, color="#5f6368")

    for node in nodes:
        x, y = positions[node]
        if node == current:
            color = "#e4572e"
        elif node in visited:
            color = "#54a24b"
        else:
            color = "#4c78a8"
        ax.scatter([x], [y], s=900, color=color, edgecolor="white", linewidth=2, zorder=2)
        distance = distances.get(node, "inf")
        ax.text(x, y + 0.03, node, ha="center", va="center", color="white", fontweight="bold")
        ax.text(x, y - 0.15, str(distance), ha="center", va="center", fontsize=8)

    ax.set_axis_off()
    ax.set_xlabel(step.description)
    return fig


def render_kmeans(step: TraceStep) -> Any:
    """Render k-means points, assignments, and centroids."""
    import numpy as np

    points = np.array(step.state["points"], dtype=float)
    centers = np.array(step.state["centers"], dtype=float)
    labels = step.state.get("labels", [0] * len(points))
    fig, ax = _figure(step.label, width=6, height=5)
    palette = ["#4c78a8", "#f58518", "#54a24b", "#b279a2", "#e45756"]
    for label in sorted(set(labels)):
        mask = [i for i, item in enumerate(labels) if item == label]
        ax.scatter(points[mask, 0], points[mask, 1], s=70, color=palette[label % len(palette)])
    ax.scatter(centers[:, 0], centers[:, 1], s=240, color="#111111", marker="X")
    ax.set_xlabel(step.description)
    ax.grid(True, alpha=0.25)
    return fig


def render_gradient_descent(step: TraceStep) -> Any:
    """Render a one-dimensional loss curve and optimization history."""
    import numpy as np

    f = step.state["function"]
    history = step.state["history"]
    x_min, x_max = step.state.get("domain", (-4, 4))
    xs = np.linspace(x_min, x_max, 240)
    ys = [f(x) for x in xs]
    fig, ax = _figure(step.label, width=6, height=4)
    ax.plot(xs, ys, color="#4c78a8")
    hx = np.array(history)
    ax.plot(hx, [f(x) for x in hx], color="#e4572e", marker="o")
    ax.set_xlabel(step.description)
    ax.grid(True, alpha=0.25)
    return fig


def bubble_sort_trace(values: Sequence[int]) -> AlgorithmTrace:
    """Record every comparison and swap in bubble sort."""
    arr = list(values)
    trace = AlgorithmTrace(
        "Bubble Sort Trace",
        objective="Repeatedly move the largest unsorted value rightward.",
        complexity="O(n^2) comparisons, O(1) extra space.",
    )
    comparisons = swaps = 0
    trace.append("start", {"array": arr.copy()}, "Initial array.")
    for end in range(len(arr) - 1, 0, -1):
        for i in range(end):
            comparisons += 1
            trace.append(
                f"compare {i} and {i + 1}",
                {"array": arr.copy()},
                "Compare adjacent values.",
                focus={"indices": [i, i + 1]},
                metrics={"comparisons": comparisons, "swaps": swaps},
                invariant="Everything after the unsorted boundary is already settled.",
                operation="compare",
            )
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swaps += 1
                trace.append(
                    f"swap {i} and {i + 1}",
                    {"array": arr.copy()},
                    "Swap because the left value is larger.",
                    focus={"indices": [i, i + 1]},
                    metrics={"comparisons": comparisons, "swaps": swaps},
                    invariant="The maximum seen in this pass moves one step right.",
                    operation="swap",
                )
    trace.append(
        "sorted",
        {"array": arr.copy()},
        "No unsorted boundary remains.",
        metrics={"comparisons": comparisons, "swaps": swaps},
        invariant="Every adjacent pair is ordered.",
        operation="finish",
    )
    return trace


def levenshtein_trace(a: str, b: str) -> AlgorithmTrace:
    """Record dynamic-programming table construction for edit distance."""
    import numpy as np

    rows, cols = len(a) + 1, len(b) + 1
    dp = np.zeros((rows, cols), dtype=int)
    trace = AlgorithmTrace(
        "Levenshtein Distance Trace",
        objective="Find the cheapest sequence of edits from one string to another.",
        complexity="O(len(a) * len(b)) time and space.",
    )
    for i in range(rows):
        dp[i, 0] = i
    for j in range(cols):
        dp[0, j] = j
    trace.append(
        "base cases",
        {"matrix": dp.copy()},
        "Empty prefixes require only insertions or deletions.",
        invariant="Each filled cell is the edit distance between two prefixes.",
        operation="initialize",
    )
    for i in range(1, rows):
        for j in range(1, cols):
            cost = 0 if a[i - 1] == b[j - 1] else 1
            dp[i, j] = min(
                dp[i - 1, j] + 1,
                dp[i, j - 1] + 1,
                dp[i - 1, j - 1] + cost,
            )
            trace.append(
                f"fill ({i}, {j})",
                {"matrix": dp.copy()},
                f"Compare {a[i - 1]!r} with {b[j - 1]!r}.",
                focus={"cell": (i, j)},
                metrics={"cell_value": int(dp[i, j])},
                invariant="Solved prefix cells are never recomputed.",
                operation="min(delete, insert, replace/match)",
            )
    return trace


def dijkstra_trace(graph: Mapping[str, Mapping[str, float]], source: str) -> AlgorithmTrace:
    """Record Dijkstra's shortest-path decisions for nonnegative edges."""
    distances = {node: float("inf") for node in graph}
    distances[source] = 0
    visited: set[str] = set()
    trace = AlgorithmTrace(
        "Dijkstra Trace",
        objective="Settle shortest distances from one source through nonnegative edges.",
        complexity="O((V + E) log V) with a heap; O(V^2) in this compact teaching version.",
    )
    trace.append(
        "start",
        {"graph": graph, "distances": _clean_distances(distances), "visited": [], "current": source},
        "Only the source is known at distance 0.",
        invariant="Visited nodes have final shortest-path distances.",
        operation="initialize",
    )
    while len(visited) < len(graph):
        candidates = [(d, n) for n, d in distances.items() if n not in visited]
        distance, current = min(candidates)
        if distance == float("inf"):
            break
        visited.add(current)
        trace.append(
            f"settle {current}",
            {
                "graph": graph,
                "distances": _clean_distances(distances),
                "visited": sorted(visited),
                "current": current,
            },
            f"Node {current} now has its final distance.",
            metrics={"settled": len(visited)},
            invariant="No unsettled route can improve a settled node.",
            operation="extract-min",
        )
        for neighbor, weight in graph[current].items():
            if neighbor in visited:
                continue
            new_distance = distances[current] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                trace.append(
                    f"relax {current}->{neighbor}",
                    {
                        "graph": graph,
                        "distances": _clean_distances(distances),
                        "visited": sorted(visited),
                        "current": neighbor,
                    },
                    f"Improve {neighbor} through {current}.",
                    metrics={"candidate": new_distance},
                    invariant="Tentative distances are best known routes through settled nodes.",
                    operation="relax edge",
                )
    return trace


def game_of_life_trace(grid: Sequence[Sequence[int]], steps: int = 12) -> AlgorithmTrace:
    """Record Conway's Game of Life generations."""
    import numpy as np

    current = np.array(grid, dtype=int)
    trace = AlgorithmTrace(
        "Game of Life Trace",
        objective="Watch local neighbor rules create global motion or stability.",
        complexity="O(generations * rows * cols).",
    )
    for generation in range(steps + 1):
        trace.append(
            f"generation {generation}",
            {"grid": current.copy()},
            "Alive cells are bright; dead cells are dark.",
            metrics={"alive": int(current.sum())},
            invariant="The next state depends only on the current eight-neighbor counts.",
            operation="apply local rule",
        )
        current = _life_step(current)
    return trace


def kmeans_trace(points: Sequence[Sequence[float]], centers: Sequence[Sequence[float]], steps: int = 5) -> AlgorithmTrace:
    """Record k-means assignment and centroid updates."""
    import numpy as np

    pts = np.array(points, dtype=float)
    ctrs = np.array(centers, dtype=float)
    labels = [0] * len(pts)
    trace = AlgorithmTrace(
        "K-Means Trace",
        objective="Alternate nearest-center assignment with centroid recomputation.",
        complexity="O(iterations * k * n * dimensions).",
    )
    for iteration in range(steps):
        distances = ((pts[:, None, :] - ctrs[None, :, :]) ** 2).sum(axis=2)
        labels = distances.argmin(axis=1).tolist()
        trace.append(
            f"assign {iteration}",
            {"points": pts.copy(), "centers": ctrs.copy(), "labels": labels},
            "Each point joins its nearest center.",
            metrics={"iteration": iteration},
            invariant="Assignments minimize distance to the current centers.",
            operation="assign",
        )
        for k in range(len(ctrs)):
            members = pts[[i for i, label in enumerate(labels) if label == k]]
            if len(members):
                ctrs[k] = members.mean(axis=0)
        trace.append(
            f"update {iteration}",
            {"points": pts.copy(), "centers": ctrs.copy(), "labels": labels},
            "Centers move to the average of their assigned points.",
            metrics={"iteration": iteration},
            invariant="The objective never increases after a centroid update.",
            operation="update centroids",
        )
    return trace


def gradient_descent_trace(
    function: Callable[[float], float],
    derivative: Callable[[float], float],
    x0: float,
    learning_rate: float = 0.1,
    steps: int = 12,
    domain: tuple[float, float] = (-4, 4),
) -> AlgorithmTrace:
    """Record one-dimensional gradient descent."""
    x = x0
    history = [x]
    trace = AlgorithmTrace(
        "Gradient Descent Trace",
        objective="Follow the local slope downhill to reduce a loss.",
        complexity="O(iterations * cost_of_gradient).",
    )
    for step in range(steps + 1):
        trace.append(
            f"step {step}",
            {"function": function, "history": history.copy(), "domain": domain},
            f"x={x:.4f}, loss={function(x):.4f}",
            metrics={"x": round(x, 4), "loss": round(function(x), 4)},
            invariant="A small enough step moves opposite the local slope.",
            operation="x <- x - learning_rate * gradient",
        )
        x = x - learning_rate * derivative(x)
        history.append(x)
    return trace


def _circular_positions(nodes: Sequence[str]) -> dict[str, tuple[float, float]]:
    count = max(1, len(nodes))
    return {
        node: (cos(2 * pi * i / count), sin(2 * pi * i / count))
        for i, node in enumerate(nodes)
    }


def _clean_distances(distances: Mapping[str, float]) -> dict[str, str | float]:
    clean: dict[str, str | float] = {}
    for node, value in distances.items():
        clean[node] = "inf" if value == float("inf") else value
    return clean


def _life_step(grid: Any) -> Any:
    import numpy as np

    rows, cols = grid.shape
    next_grid = np.zeros_like(grid)
    for r in range(rows):
        for c in range(cols):
            total = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    total += grid[(r + dr) % rows, (c + dc) % cols]
            next_grid[r, c] = 1 if total == 3 or (grid[r, c] and total == 2) else 0
    return next_grid
