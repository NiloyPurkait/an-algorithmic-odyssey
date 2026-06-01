"""Create the Voronoi and Delaunay spatial-graphs notebook."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "02-spatial-graphs" / "04-voronoi-delaunay" / "voronoi-delaunay.ipynb"


def md(source: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": dedent(source).strip() + "\n",
    }


def code(source: str) -> dict:
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": dedent(source).strip() + "\n",
    }


cells = [
    md(
        """
        # Voronoi Diagrams and Delaunay Triangulation: Territories From Points

        Scatter points on a map. Now ask a simple question:

        > Which point is closest to every location?

        A **Voronoi diagram** answers that by dividing the plane into territories. Every location inside a cell is closer to that cell's site than to any other site. A **Delaunay triangulation** connects sites that are natural neighbors, giving a graph that is the geometric dual of the Voronoi diagram.

        This notebook sits in Spatial Graphs because it turns continuous space into discrete structure. Maps become territories. Territories imply neighboring sites. Neighboring sites become a graph that later algorithms can search, optimize, or reason about.
        """
    ),
    md(
        """
        ## 1. The Mental Model

        Voronoi and Delaunay are two views of the same geometry.

        - **Voronoi cell**: all locations closer to one site than to any other site.
        - **Voronoi boundary**: locations where two or more sites are tied.
        - **Delaunay edge**: a connection between two sites whose Voronoi cells share a boundary.
        - **Delaunay triangle**: a triangle whose circumcircle contains no other site in its interior.

        This has a very practical feel: nearest cell tower, nearest hospital, closest warehouse, likely service region, cracked stone texture, procedural map borders.

        Careful modeling note: real cell-phone handoff is not just nearest tower. Signal strength, terrain, tower load, radio technology, and policy matter. Voronoi is the clean geometric first model.
        """
    ),
    md("## 2. Build the Ingredients"),
    md("**Imports and setup.** Load numerical, plotting, and computational-geometry tools."),
    code(
        """
        from dataclasses import dataclass
        from itertools import combinations

        import matplotlib.pyplot as plt
        import numpy as np
        from IPython.display import HTML
        from matplotlib import animation
        from matplotlib.colors import ListedColormap
        from scipy.spatial import Delaunay, KDTree, Voronoi
        """
    ),
    md("**Configuration.** Keep bounds, random seed, and sampling resolution in one named object."),
    code(
        """
        @dataclass(frozen=True)
        class GeometryConfig:
            width: float = 100.0
            height: float = 70.0
            site_count: int = 18
            seed: int = 12
            grid_size: int = 260
        """
    ),
    md("**Sample sites.** Generate reproducible points, with a small margin so edge cells are easier to see."),
    code(
        """
        def generate_sites(config: GeometryConfig) -> np.ndarray:
            rng = np.random.default_rng(config.seed)
            margin = 7
            return rng.uniform(
                [margin, margin],
                [config.width - margin, config.height - margin],
                size=(config.site_count, 2),
            )


        config = GeometryConfig()
        sites = generate_sites(config)
        sites[:5]
        """
    ),
    md(
        """
        ## 3. Nearest Site Rule

        Before using a geometry library, build the rule directly. A location belongs to the site with the smallest squared distance.

        Squared distance is enough because square roots preserve order: if `a < b`, then `sqrt(a) < sqrt(b)`.
        """
    ),
    md("**Distance table.** Compute distances from many query points to every site at once."),
    code(
        """
        def squared_distances(samples: np.ndarray, sites: np.ndarray) -> np.ndarray:
            offsets = samples[:, None, :] - sites[None, :, :]
            return np.sum(offsets * offsets, axis=2)


        def nearest_site_indices(samples: np.ndarray, sites: np.ndarray) -> np.ndarray:
            return np.argmin(squared_distances(samples, sites), axis=1)


        test_points = np.array([[20, 20], [60, 30], [80, 60]])
        nearest_site_indices(test_points, sites)
        """
    ),
    md("**Sampling grid.** Turn the plane into many query points so the territories become visible."),
    code(
        """
        def grid_samples(config: GeometryConfig) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
            xs = np.linspace(0, config.width, config.grid_size)
            ys = np.linspace(0, config.height, config.grid_size)
            grid_x, grid_y = np.meshgrid(xs, ys)
            samples = np.column_stack([grid_x.ravel(), grid_y.ravel()])
            return grid_x, grid_y, samples


        def sampled_voronoi_labels(sites: np.ndarray, config: GeometryConfig) -> np.ndarray:
            _, _, samples = grid_samples(config)
            return nearest_site_indices(samples, sites).reshape(config.grid_size, config.grid_size)
        """
    ),
    md("**Draw the mosaic.** Color each sampled location by its nearest site."),
    code(
        """
        def palette(count: int) -> ListedColormap:
            base = plt.cm.tab20(np.linspace(0, 1, 20))
            colors = np.vstack([base for _ in range((count // 20) + 1)])[:count]
            return ListedColormap(colors)


        def draw_sampled_voronoi(
            sites: np.ndarray,
            config: GeometryConfig,
            user_point: tuple[float, float] | None = None,
            ax=None,
            title: str = "Sampled Voronoi territories",
        ):
            if ax is None:
                _, ax = plt.subplots(figsize=(8, 5))

            labels = sampled_voronoi_labels(sites, config)
            ax.imshow(
                labels,
                origin="lower",
                extent=[0, config.width, 0, config.height],
                cmap=palette(len(sites)),
                alpha=0.58,
                interpolation="nearest",
            )
            ax.scatter(sites[:, 0], sites[:, 1], s=46, color="#111827", edgecolor="white", linewidth=1.2, zorder=3)

            if user_point is not None:
                user = np.array(user_point, dtype=float)
                owner = nearest_site_indices(user[None, :], sites)[0]
                ax.scatter([user[0]], [user[1]], s=110, color="#f97316", edgecolor="white", linewidth=1.5, zorder=4)
                ax.plot([user[0], sites[owner, 0]], [user[1], sites[owner, 1]], color="#f97316", linewidth=2, zorder=4)
                ax.scatter([sites[owner, 0]], [sites[owner, 1]], s=140, facecolor="none", edgecolor="#f97316", linewidth=3, zorder=5)
                ax.set_title(f"{title} | user belongs to site {owner}")
            else:
                ax.set_title(title)

            ax.set_xlim(0, config.width)
            ax.set_ylim(0, config.height)
            ax.set_aspect("equal")
            ax.set_xticks([])
            ax.set_yticks([])
            return ax


        draw_sampled_voronoi(sites, config)
        plt.show()
        """
    ),
    md(
        """
        ## 4. Exact Voronoi Ridges

        The sampled mosaic explains the definition. Now use `scipy.spatial.Voronoi`, which calls the Qhull geometry library under the hood, to compute the diagram's vertices and ridges.

        A ridge is a Voronoi boundary segment. Some ridges are unbounded because cells at the edge of the plane continue forever. That edge behavior is a real modeling issue, not a plotting bug.
        """
    ),
    md("**Ridge plotter.** Draw finite Voronoi ridges over the sampled territories."),
    code(
        """
        def draw_voronoi_ridges(sites: np.ndarray, config: GeometryConfig, ax=None):
            if ax is None:
                _, ax = plt.subplots(figsize=(8, 5))

            draw_sampled_voronoi(sites, config, ax=ax, title="Voronoi ridges over sampled territories")
            diagram = Voronoi(sites)

            finite_count = 0
            infinite_count = 0
            for ridge_vertices in diagram.ridge_vertices:
                if -1 in ridge_vertices:
                    infinite_count += 1
                    continue
                segment = diagram.vertices[ridge_vertices]
                ax.plot(segment[:, 0], segment[:, 1], color="#0f172a", linewidth=2.2, alpha=0.92)
                finite_count += 1

            return diagram, {"finite_ridges": finite_count, "infinite_ridges": infinite_count}


        diagram, ridge_counts = draw_voronoi_ridges(sites, config)
        print(ridge_counts)
        plt.show()
        """
    ),
    md(
        """
        ## 5. Delaunay Triangulation

        Delaunay triangulation connects the sites into triangles. Its key geometric property:

        > The circumcircle of any Delaunay triangle contains no other site in its interior.

        In practice, the Delaunay graph is a useful "natural neighbor" graph. It tends to avoid skinny unnatural connections and often becomes a good starting point for terrain meshes, navigation graphs, interpolation, and spatial analysis.
        """
    ),
    md("**Delaunay edges.** Extract unique edges from the triangles returned by SciPy."),
    code(
        """
        def delaunay_edges(triangulation: Delaunay) -> set[tuple[int, int]]:
            edges = set()
            for triangle in triangulation.simplices:
                for a, b in combinations(triangle, 2):
                    edges.add(tuple(sorted((int(a), int(b)))))
            return edges


        triangulation = Delaunay(sites)
        edges = delaunay_edges(triangulation)

        print("triangles:", len(triangulation.simplices))
        print("unique edges:", len(edges))
        """
    ),
    md("**Draw the dual graph.** Overlay Delaunay edges on top of the Voronoi territories."),
    code(
        """
        def draw_delaunay(sites: np.ndarray, config: GeometryConfig, ax=None, title: str = "Delaunay natural-neighbor graph"):
            if ax is None:
                _, ax = plt.subplots(figsize=(8, 5))

            draw_sampled_voronoi(sites, config, ax=ax, title=title)
            triangulation = Delaunay(sites)
            ax.triplot(sites[:, 0], sites[:, 1], triangulation.simplices, color="#2563eb", linewidth=1.8, alpha=0.95)
            ax.scatter(sites[:, 0], sites[:, 1], s=50, color="#111827", edgecolor="white", linewidth=1.2, zorder=3)
            return triangulation


        draw_delaunay(sites, config)
        plt.show()
        """
    ),
    md(
        """
        ## 6. The Dual Relationship

        For points in general position, two sites are connected by a Delaunay edge exactly when their Voronoi cells share a boundary.

        SciPy exposes that relationship directly: `Voronoi.ridge_points` stores the pair of sites on the two sides of each Voronoi ridge.
        """
    ),
    md("**Compare edge sets.** Check that Voronoi ridge pairs and Delaunay edges agree on this point set."),
    code(
        """
        def voronoi_ridge_edges(diagram: Voronoi) -> set[tuple[int, int]]:
            return {tuple(sorted(map(int, pair))) for pair in diagram.ridge_points}


        voronoi_edges = voronoi_ridge_edges(diagram)
        delaunay_edge_set = delaunay_edges(triangulation)

        print("Voronoi neighbor pairs:", len(voronoi_edges))
        print("Delaunay edges:", len(delaunay_edge_set))
        print("sets match:", voronoi_edges == delaunay_edge_set)
        """
    ),
    md(
        """
        ## 7. Moving User Playground

        Now move a user point through the map. The rule is simple: find the nearest site, then highlight that site and the connection.

        This is the educational payoff: the diagram is not just a pretty mosaic. It is a nearest-neighbor query made visible.
        """
    ),
    md("**Nearest query.** Use a KD-tree for fast nearest-site lookup."),
    code(
        """
        tree = KDTree(sites)


        def nearest_with_tree(user_point: tuple[float, float]) -> tuple[int, float]:
            distance, index = tree.query(np.array(user_point, dtype=float))
            return int(index), float(distance)


        nearest_with_tree((72, 38))
        """
    ),
    md("**Animate a path.** Watch ownership change as the user crosses Voronoi boundaries."),
    code(
        """
        def user_path(config: GeometryConfig, frames: int = 36) -> np.ndarray:
            t = np.linspace(0, 1, frames)
            x = 8 + (config.width - 16) * t
            y = config.height * (0.5 + 0.28 * np.sin(2 * np.pi * t))
            return np.column_stack([x, y])


        def animate_user_walk(sites: np.ndarray, config: GeometryConfig) -> HTML:
            path = user_path(config)
            fig, ax = plt.subplots(figsize=(8, 5))

            def update(frame_index: int):
                ax.clear()
                point = tuple(path[frame_index])
                owner, distance = nearest_with_tree(point)
                draw_sampled_voronoi(sites, config, user_point=point, ax=ax, title="Moving nearest-site query")
                ax.set_title(f"step {frame_index} | nearest site {owner} | distance {distance:.1f}")

            anim = animation.FuncAnimation(fig, update, frames=len(path), interval=120)
            plt.close(fig)
            return HTML(anim.to_jshtml())


        animate_user_walk(sites, config)
        """
    ),
    md("**Interactive point.** If widgets are available, move the user point by hand."),
    code(
        """
        try:
            import ipywidgets as widgets
            from IPython.display import display

            x_slider = widgets.FloatSlider(value=50, min=0, max=config.width, step=1, description="user x")
            y_slider = widgets.FloatSlider(value=35, min=0, max=config.height, step=1, description="user y")

            def show_user(user_x, user_y):
                owner, distance = nearest_with_tree((user_x, user_y))
                draw_sampled_voronoi(sites, config, user_point=(user_x, user_y), title=f"site {owner}, distance {distance:.1f}")
                plt.show()

            controls = widgets.interactive_output(show_user, {"user_x": x_slider, "user_y": y_slider})
            display(widgets.HBox([x_slider, y_slider]), controls)
        except Exception:
            print("ipywidgets is not available. Edit the point in the next cell instead.")
        """
    ),
    md("**Fallback query.** Use this cell when widgets are not available."),
    code(
        """
        user = (72, 38)
        owner, distance = nearest_with_tree(user)
        print(f"user point {user} belongs to site {owner} at distance {distance:.2f}")
        draw_sampled_voronoi(sites, config, user_point=user)
        plt.show()
        """
    ),
    md(
        """
        ## 8. Stress and Failure Modes

        Geometry algorithms have assumptions. Try these cases:

        - **Clustered points**: tiny cells become hard to see.
        - **Nearly collinear points**: triangulation can become numerically fragile.
        - **Unbounded cells**: edge territories extend outside the plotted rectangle.
        - **Wrong metric**: Euclidean distance may be wrong if roads, rivers, buildings, or radio obstacles matter.
        """
    ),
    md("**Compare cases.** Generate three site sets and look for visual or numerical artifacts."),
    code(
        """
        def clustered_sites(config: GeometryConfig) -> np.ndarray:
            rng = np.random.default_rng(config.seed)
            cluster = rng.normal([config.width * 0.45, config.height * 0.55], [9, 6], size=(config.site_count, 2))
            return np.clip(cluster, [4, 4], [config.width - 4, config.height - 4])


        def nearly_collinear_sites(config: GeometryConfig) -> np.ndarray:
            rng = np.random.default_rng(config.seed)
            x = np.linspace(8, config.width - 8, config.site_count)
            y = config.height * 0.5 + rng.normal(0, 1.0, size=config.site_count)
            return np.column_stack([x, y])


        cases = {
            "balanced": sites,
            "clustered": clustered_sites(config),
            "nearly collinear": nearly_collinear_sites(config),
        }

        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        for ax, (name, case_sites) in zip(axes, cases.items()):
            draw_delaunay(case_sites, config, ax=ax, title=name)
        plt.tight_layout()
        plt.show()
        """
    ),
    md(
        """
        ## 9. Mini-Challenge

        Try one:

        1. Increase the number of sites and describe how average cell size changes.
        2. Move the user point across a boundary and identify the exact ownership switch.
        3. Build a road graph from Delaunay edges, weight edges by Euclidean distance, then run Dijkstra from one site to another.
        4. Replace Euclidean distance with "weighted distance" where one site has stronger signal range. What breaks about ordinary Voronoi cells?
        """
    ),
    md("**Challenge helper.** Convert Delaunay edges into a weighted graph for later graph algorithms."),
    code(
        """
        def delaunay_weighted_graph(sites: np.ndarray) -> dict[int, dict[int, float]]:
            triangulation = Delaunay(sites)
            graph = {i: {} for i in range(len(sites))}
            for a, b in delaunay_edges(triangulation):
                weight = float(np.linalg.norm(sites[a] - sites[b]))
                graph[a][b] = weight
                graph[b][a] = weight
            return graph


        graph = delaunay_weighted_graph(sites)
        for node in range(5):
            neighbors = ", ".join(f"{nbr}:{dist:.1f}" for nbr, dist in sorted(graph[node].items()))
            print(f"{node}: {neighbors}")
        """
    ),
    md(
        """
        ## Visual Trace + Rigor Studio

        **Problem frame.** Turn continuous coordinates into ownership regions and natural-neighbor graph edges.

        **Interactive animation target.** Animate site insertion, territory coloring, Delaunay edges, and a moving user point that changes ownership.

        **Correctness handle.** Every sampled location is assigned to the site with minimum squared Euclidean distance.

        **Complexity handle.** Naive territory coloring is `O(samples * sites)`. A single naive nearest-site query is `O(sites)`, while KD-tree lookup is typically much faster for repeated queries. Efficient Voronoi construction in the plane can be done in `O(n log n)` time.

        **Failure mode to test.** Nearly collinear or duplicate points can create degenerate geometry; edge cells are unbounded unless the world is explicitly clipped.

        **Studio task.** Pick one point, show its nearest site, then name the Delaunay neighbors of that site and explain why those are local geometric neighbors.
        """
    ),
    md(
        """
        ## Sources and Further Reading

        - SciPy, [`scipy.spatial` tutorial](https://scipy.github.io/devdocs/tutorial/spatial.html)
        - SciPy, [`scipy.spatial.Voronoi`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Voronoi.html)
        - SciPy, [`scipy.spatial.Delaunay`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.Delaunay.html)
        - Qhull, [official project page](https://www.qhull.org/)
        - Steven Fortune, [A Sweepline Algorithm for Voronoi Diagrams](https://www.ibr.cs.tu-bs.de/courses/ws2526/ag/material/papers/Ch4/Fortune-1987-voronoi.pdf), Algorithmica 2, 153-174 (1987)

        This notebook uses sampled coloring for pedagogy and SciPy/Qhull for exact Voronoi and Delaunay structures.
        """
    ),
]


notebook = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "name": "python",
            "pygments_lexer": "ipython3",
        },
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}


NOTEBOOK.parent.mkdir(parents=True, exist_ok=True)
NOTEBOOK.write_text(json.dumps(notebook, indent=1), encoding="utf-8")
print(NOTEBOOK)
