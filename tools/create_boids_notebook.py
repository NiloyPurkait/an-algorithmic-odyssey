"""Create the Boids notebook for Module 3."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "03-natural-emergence" / "01-boids" / "boids.ipynb"


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
        # Boids: Flocking & Swarm Intelligence

        A flock looks coordinated, but no bird needs a flight plan for the whole group.

        Craig Reynolds made the original Boids model in 1986 and published the classic SIGGRAPH paper, *Flocks, Herds, and Schools: A Distributed Behavioral Model*, in 1987. The idea is wonderfully course-shaped: complex group motion emerges from simple local rules followed by each individual agent.

        In this notebook, every boid is just a moving point with a position and velocity. The flock forms because nearby boids influence one another.
        """
    ),
    md(
        """
        ## 1. Mental Model

        Each boid looks only at local neighbors, then combines three steering rules:

        - **Separation**: steer away from nearby flockmates to avoid crowding.
        - **Alignment**: steer toward the average heading of nearby flockmates.
        - **Cohesion**: steer toward the average position of nearby flockmates.

        We will add one optional rule:

        - **Predator avoidance**: steer away from a threat point.

        The important idea is decentralization. There is no leader, no global route, and no central controller. The flock is the visible result of many small local decisions.
        """
    ),
    md(
        """
        ## 2. Build the Parameters

        The simulation uses vectors. A position is `[x, y]`; a velocity is also `[x, y]`.

        The parameters below control the whole personality of the flock: how far boids can see, how quickly they can turn, and how strongly each rule matters.
        """
    ),
    md("**Imports and setup.** Load the numerical and plotting tools used by the simulation."),
    code(
        """
        from dataclasses import dataclass

        import numpy as np
        import matplotlib.pyplot as plt
        from matplotlib import animation
        from IPython.display import HTML
        """
    ),
    md("**Simulation parameters.** Store the knobs that shape flock behavior."),
    code(
        """
        @dataclass(frozen=True)
        class FlockConfig:
            width: float = 100.0
            height: float = 70.0
            perception_radius: float = 14.0
            separation_radius: float = 6.0
            max_speed: float = 2.2
            max_force: float = 0.08
            separation_weight: float = 1.8
            alignment_weight: float = 1.0
            cohesion_weight: float = 0.9
            predator_weight: float = 2.8
            predator_radius: float = 18.0
        """
    ),
    md(
        """
        ## 3. Vector Helpers

        Steering forces should not be infinitely strong. These helpers keep vectors numerically polite:

        - `norms` measures vector lengths.
        - `limit_vectors` caps a vector's magnitude.
        - `wrap_positions` makes the world loop around at the edges.
        """
    ),
    md("**Vector helpers.** Define reusable operations for speed, steering, and world boundaries."),
    code(
        """
        def norms(vectors: np.ndarray) -> np.ndarray:
            return np.linalg.norm(vectors, axis=1)


        def limit_vectors(vectors: np.ndarray, max_length: float) -> np.ndarray:
            lengths = norms(vectors)
            scale = np.ones_like(lengths)
            too_large = lengths > max_length
            scale[too_large] = max_length / lengths[too_large]
            return vectors * scale[:, None]


        def wrap_positions(positions: np.ndarray, config: FlockConfig) -> np.ndarray:
            wrapped = positions.copy()
            wrapped[:, 0] %= config.width
            wrapped[:, 1] %= config.height
            return wrapped
        """
    ),
    md(
        """
        ## 4. Initialize the Flock

        Start the boids in random positions with random headings. At first, the motion looks noisy. After several steps, local interactions start creating visible flow.
        """
    ),
    md("**Initial state.** Create positions and velocities for a reproducible flock."),
    code(
        """
        def initialize_flock(count: int, config: FlockConfig, seed: int = 7) -> tuple[np.ndarray, np.ndarray]:
            rng = np.random.default_rng(seed)
            positions = rng.uniform([0, 0], [config.width, config.height], size=(count, 2))
            angles = rng.uniform(0, 2 * np.pi, size=count)
            speeds = rng.uniform(0.5, config.max_speed, size=count)
            velocities = np.column_stack([np.cos(angles), np.sin(angles)]) * speeds[:, None]
            return positions, velocities


        config = FlockConfig()
        positions, velocities = initialize_flock(100, config)

        print("positions shape:", positions.shape)
        print("velocities shape:", velocities.shape)
        """
    ),
    md(
        """
        ## 5. Find Local Neighbors

        A boid does not react to every other boid. It reacts to nearby flockmates inside its perception radius.

        The distance matrix below compares every boid against every other boid. This teaching version is `O(n^2)` per step, which is fine for 100 boids and beautifully direct. Large simulations usually use spatial hashing or grids to avoid checking every pair.
        """
    ),
    md("**Neighborhoods.** Compute who can see whom at the current moment."),
    code(
        """
        def pairwise_offsets(positions: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
            offsets = positions[:, None, :] - positions[None, :, :]
            distances = np.linalg.norm(offsets, axis=2)
            return offsets, distances


        def neighbor_masks(positions: np.ndarray, config: FlockConfig) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
            offsets, distances = pairwise_offsets(positions)
            not_self = distances > 0
            visible = (distances < config.perception_radius) & not_self
            too_close = (distances < config.separation_radius) & not_self
            return offsets, visible, too_close
        """
    ),
    md(
        """
        ## 6. Separation

        Separation is the anti-crowding rule. If neighbors are too close, a boid steers away from them. Closer neighbors push harder.
        """
    ),
    md("**Separation rule.** Turn nearby crowding into an avoidance force."),
    code(
        """
        def separation_force(positions: np.ndarray, velocities: np.ndarray, config: FlockConfig) -> np.ndarray:
            offsets, distances = pairwise_offsets(positions)
            mask = (distances < config.separation_radius) & (distances > 0)
            safe_distances = np.where(mask, distances, 1.0)
            repulsion = np.where(mask[:, :, None], offsets / safe_distances[:, :, None] ** 2, 0.0)
            desired = repulsion.sum(axis=1)
            desired = limit_vectors(desired, config.max_speed)
            return limit_vectors(desired - velocities, config.max_force)
        """
    ),
    md(
        """
        ## 7. Alignment and Cohesion

        Alignment makes headings agree. Cohesion pulls the flock together.

        Notice the balance: separation prevents collapse, cohesion prevents scattering, and alignment creates shared flow.
        """
    ),
    md("**Alignment rule.** Steer toward the average heading of local neighbors."),
    code(
        """
        def alignment_force(positions: np.ndarray, velocities: np.ndarray, config: FlockConfig) -> np.ndarray:
            _, visible, _ = neighbor_masks(positions, config)
            counts = visible.sum(axis=1)
            summed = visible.astype(float) @ velocities
            average = np.divide(summed, counts[:, None], out=np.zeros_like(summed), where=counts[:, None] > 0)
            desired = limit_vectors(average, config.max_speed)
            return limit_vectors(desired - velocities, config.max_force)
        """
    ),
    md("**Cohesion rule.** Steer toward the center of visible neighbors."),
    code(
        """
        def cohesion_force(positions: np.ndarray, velocities: np.ndarray, config: FlockConfig) -> np.ndarray:
            _, visible, _ = neighbor_masks(positions, config)
            counts = visible.sum(axis=1)
            summed = visible.astype(float) @ positions
            center = np.divide(summed, counts[:, None], out=positions.copy(), where=counts[:, None] > 0)
            desired = center - positions
            desired = limit_vectors(desired, config.max_speed)
            return limit_vectors(desired - velocities, config.max_force)
        """
    ),
    md(
        """
        ## 8. Predator Avoidance

        The predator is just a point. If a boid is close enough, it steers away.

        This makes the playground more alive: the flock scatters, then reforms when the threat is gone.
        """
    ),
    md("**Predator rule.** Add a local repulsion force from a threat point."),
    code(
        """
        def predator_force(positions: np.ndarray, velocities: np.ndarray, config: FlockConfig, predator=None) -> np.ndarray:
            if predator is None:
                return np.zeros_like(positions)

            predator = np.array(predator, dtype=float)
            away = positions - predator
            distances = np.linalg.norm(away, axis=1)
            mask = (distances < config.predator_radius) & (distances > 0)
            desired = np.zeros_like(positions)
            desired[mask] = away[mask] / distances[mask, None] ** 2
            desired = limit_vectors(desired, config.max_speed)
            return limit_vectors(desired - velocities, config.max_force)
        """
    ),
    md(
        """
        ## 9. One Simulation Step

        Now combine the rules.

        This is the algorithmic heart of Boids:

        ```text
        steering = separation + alignment + cohesion + predator avoidance
        velocity = velocity + steering
        position = position + velocity
        ```
        """
    ),
    md("**Update rule.** Combine local steering forces and advance the flock."),
    code(
        """
        def step_flock(
            positions: np.ndarray,
            velocities: np.ndarray,
            config: FlockConfig,
            predator=None,
        ) -> tuple[np.ndarray, np.ndarray]:
            steering = (
                config.separation_weight * separation_force(positions, velocities, config)
                + config.alignment_weight * alignment_force(positions, velocities, config)
                + config.cohesion_weight * cohesion_force(positions, velocities, config)
                + config.predator_weight * predator_force(positions, velocities, config, predator)
            )
            next_velocities = limit_vectors(velocities + steering, config.max_speed)
            next_positions = wrap_positions(positions + next_velocities, config)
            return next_positions, next_velocities
        """
    ),
    md(
        """
        ## 10. Measure Emergence

        A flock is visual, but we can still measure it.

        - **Polarization** is near `1` when headings align.
        - **Crowding** is the average nearest-neighbor distance.

        These are not the only possible metrics, but they help students connect the animation to data.
        """
    ),
    md("**Flock metrics.** Quantify alignment and crowding from the current state."),
    code(
        """
        def flock_metrics(positions: np.ndarray, velocities: np.ndarray) -> dict[str, float]:
            speeds = norms(velocities)
            headings = np.divide(velocities, speeds[:, None], out=np.zeros_like(velocities), where=speeds[:, None] > 0)
            polarization = np.linalg.norm(headings.mean(axis=0))

            _, distances = pairwise_offsets(positions)
            distances[distances == 0] = np.inf
            nearest = distances.min(axis=1)

            return {
                "polarization": float(polarization),
                "mean_nearest_distance": float(nearest.mean()),
            }
        """
    ),
    md("**Run the simulation.** Capture snapshots so the behavior can be replayed and plotted."),
    code(
        """
        def run_flock(
            count: int = 100,
            steps: int = 180,
            capture_every: int = 5,
            config: FlockConfig = FlockConfig(),
            predator=None,
            seed: int = 7,
        ) -> list[dict]:
            positions, velocities = initialize_flock(count, config, seed=seed)
            snapshots = []

            for step in range(steps + 1):
                if step % capture_every == 0:
                    snapshots.append({
                        "step": step,
                        "positions": positions.copy(),
                        "velocities": velocities.copy(),
                        "metrics": flock_metrics(positions, velocities),
                        "predator": predator,
                    })
                positions, velocities = step_flock(positions, velocities, config, predator=predator)

            return snapshots
        """
    ),
    md(
        """
        ## 11. Visualize Snapshots

        Each boid is drawn as a small arrow. Position shows where it is; arrow direction shows where it is heading.
        """
    ),
    md("**Visual helper.** Draw a single flock snapshot as a field of moving agents."),
    code(
        """
        def draw_snapshot(snapshot: dict, config: FlockConfig, ax=None, title: str | None = None):
            if ax is None:
                _, ax = plt.subplots(figsize=(8, 5))

            positions = snapshot["positions"]
            velocities = snapshot["velocities"]
            ax.quiver(
                positions[:, 0],
                positions[:, 1],
                velocities[:, 0],
                velocities[:, 1],
                angles="xy",
                scale_units="xy",
                scale=1.2,
                color="#2563eb",
                width=0.004,
            )
            if snapshot.get("predator") is not None:
                predator = np.array(snapshot["predator"])
                ax.scatter([predator[0]], [predator[1]], s=180, color="#dc2626", marker="X", label="predator")

            ax.set_xlim(0, config.width)
            ax.set_ylim(0, config.height)
            ax.set_aspect("equal")
            ax.set_title(title or f'step {snapshot["step"]}')
            ax.set_xticks([])
            ax.set_yticks([])
            return ax
        """
    ),
    md("**Inspect the result.** Compare early, middle, and late flock states."),
    code(
        """
        snapshots = run_flock(count=100, steps=180, capture_every=10, config=config, seed=4)

        chosen = [snapshots[0], snapshots[len(snapshots) // 2], snapshots[-1]]
        fig, axes = plt.subplots(1, 3, figsize=(14, 4))

        for ax, snapshot in zip(axes, chosen):
            metrics = snapshot["metrics"]
            title = (
                f'step {snapshot["step"]}\\n'
                f'polarization={metrics["polarization"]:.2f}, '
                f'nearest={metrics["mean_nearest_distance"]:.1f}'
            )
            draw_snapshot(snapshot, config, ax=ax, title=title)

        plt.tight_layout()
        plt.show()
        """
    ),
    md(
        """
        ## 12. Animate the Flock

        Run this cell to watch the flock organize over time. The animation uses saved snapshots so it stays notebook-friendly.
        """
    ),
    md("**Animation.** Turn the saved snapshots into a playable notebook animation."),
    code(
        """
        def animate_flock(snapshots: list[dict], config: FlockConfig) -> HTML:
            fig, ax = plt.subplots(figsize=(7, 5))

            def update(frame_index: int):
                ax.clear()
                snapshot = snapshots[frame_index]
                draw_snapshot(snapshot, config, ax=ax)
                metrics = snapshot["metrics"]
                ax.set_title(
                    f'step {snapshot["step"]} | '
                    f'polarization={metrics["polarization"]:.2f} | '
                    f'nearest={metrics["mean_nearest_distance"]:.1f}'
                )

            anim = animation.FuncAnimation(fig, update, frames=len(snapshots), interval=80)
            plt.close(fig)
            return HTML(anim.to_jshtml())


        animate_flock(snapshots, config)
        """
    ),
    md(
        """
        ## 13. Predator Playground

        Put the predator at a location and rerun the simulation. The flock should scatter locally and then bend around the threat.

        Try:

        - predator near the center: `(50, 35)`
        - predator near one edge: `(20, 50)`
        - no predator: `None`
        """
    ),
    md("**Predator run.** Compare ordinary flocking with a local threat in the scene."),
    code(
        """
        predator = (50, 35)
        predator_snapshots = run_flock(
            count=100,
            steps=180,
            capture_every=10,
            config=config,
            predator=predator,
            seed=4,
        )

        fig, axes = plt.subplots(1, 2, figsize=(11, 4))
        draw_snapshot(snapshots[-1], config, ax=axes[0], title="without predator")
        draw_snapshot(predator_snapshots[-1], config, ax=axes[1], title="with predator")
        plt.tight_layout()
        plt.show()
        """
    ),
    md("**Interactive display.** Use sliders when widgets are available, with a fallback for simpler notebook environments."),
    code(
        """
        try:
            import ipywidgets as widgets
            from IPython.display import display

            x_slider = widgets.FloatSlider(value=50, min=0, max=config.width, step=1, description="predator x")
            y_slider = widgets.FloatSlider(value=35, min=0, max=config.height, step=1, description="predator y")
            strength = widgets.FloatSlider(value=2.8, min=0, max=6, step=0.2, description="avoidance")

            def show_predator_run(predator_x, predator_y, avoidance):
                tuned = FlockConfig(predator_weight=avoidance)
                tuned_snapshots = run_flock(
                    count=90,
                    steps=120,
                    capture_every=12,
                    config=tuned,
                    predator=(predator_x, predator_y),
                    seed=5,
                )
                draw_snapshot(tuned_snapshots[-1], tuned, title="final state with predator")
                plt.show()

            controls = widgets.interactive_output(
                show_predator_run,
                {"predator_x": x_slider, "predator_y": y_slider, "avoidance": strength},
            )
            display(widgets.HBox([x_slider, y_slider, strength]), controls)
        except Exception:
            print("ipywidgets is not available. Edit the predator tuple in the previous cell and rerun it.")
        """
    ),
    md(
        """
        ## 14. Parameter Experiments

        Boids is perfect for controlled experiments. Change one weight at a time and predict the effect:

        - More separation: looser flock, fewer collisions.
        - More alignment: smoother shared direction.
        - More cohesion: tighter group, but risk of clumping.
        - More predator avoidance: sharper scattering.
        """
    ),
    md("**Run the experiment.** Compare three parameter regimes with the same random seed."),
    code(
        """
        experiments = {
            "balanced": FlockConfig(),
            "high separation": FlockConfig(separation_weight=3.2, cohesion_weight=0.7),
            "high cohesion": FlockConfig(separation_weight=1.1, cohesion_weight=2.2),
        }

        fig, axes = plt.subplots(1, len(experiments), figsize=(14, 4))
        for ax, (label, experiment_config) in zip(axes, experiments.items()):
            result = run_flock(count=100, steps=160, capture_every=20, config=experiment_config, seed=9)
            metrics = result[-1]["metrics"]
            title = f'{label}\\npolarization={metrics["polarization"]:.2f}, nearest={metrics["mean_nearest_distance"]:.1f}'
            draw_snapshot(result[-1], experiment_config, ax=ax, title=title)

        plt.tight_layout()
        plt.show()
        """
    ),
    md(
        """
        ## Mini-Challenge

        Choose one:

        1. Turn off alignment by setting `alignment_weight=0`. Does the flock still look coordinated?
        2. Turn off separation. What visual failure appears?
        3. Increase `perception_radius`. Does the flock become smoother or more rigid?
        4. Add two predator points by extending `predator_force`.

        A strong response includes:

        - prediction,
        - changed parameter,
        - observed visual result,
        - one metric comparison.
        """
    ),
    md(
        """
        ## Visual Trace + Rigor Studio

        **Problem frame.** Model flocking as decentralized multi-agent steering.

        **Interactive animation target.** Animate 100 boids with play controls, parameter sliders, and an optional predator point.

        **Correctness handle.** Each boid's acceleration is computed only from local neighbors and configured steering limits.

        **Complexity handle.** This teaching implementation is `O(n^2)` per step because it checks all boid pairs. A larger real-time simulation would use a spatial grid or tree to reduce neighbor search cost.

        **Failure mode to test.** Turn off separation and explain why cohesion alone collapses the flock into crowding.

        **Studio task.** Compare the flock's polarization and nearest-neighbor distance before and after changing one rule weight.
        """
    ),
    md(
        """
        ## Sources and Further Reading

        - Craig Reynolds, [Boids background page](https://www.red3d.com/cwr/boids/)
        - Craig Reynolds, [Flocks, Herds, and Schools: A Distributed Behavioral Model](https://red3d.com/cwr/papers/1987/boids.html), SIGGRAPH 1987
        - Daniel Shiffman, [The Nature of Code: Autonomous Agents](https://natureofcode.com/autonomous-agents/)
        - Allen Downey, [Think Complexity: Boids](https://eng.libretexts.org/Bookshelves/Computer_Science/Applied_Programming/Think_Complexity%3A_Exploring_Complexity_Science_with_Python_%28Downey%29/10%3A_Herds_Flocks_and_Traffic_Jams/10.03%3A_Boids)

        This notebook uses the canonical separation/alignment/cohesion model as a teaching version. Reynolds' original work included richer 3D animation and obstacle handling; the simplified two-dimensional version here is designed for clear experimentation.
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
NOTEBOOK.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print(NOTEBOOK)
