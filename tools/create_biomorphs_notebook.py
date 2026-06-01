"""Create the Dawkins Biomorphs natural-emergence notebook."""

from __future__ import annotations

import json
from pathlib import Path
from textwrap import dedent


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "03-natural-emergence" / "02-biomorphs" / "biomorphs.ipynb"


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
        # Dawkins' Biomorphs: Artificial Selection in Gene Space

        Richard Dawkins introduced **Biomorphs** in *The Blind Watchmaker* as a visual argument for cumulative selection. A biomorph is a simple branching drawing controlled by a compact genome. Mutate the genome a little, choose the most interesting child, and repeat.

        The surprise is not that randomness creates polished forms. It usually does not. The surprise is that **random mutation plus non-random selection** can walk through gene space toward forms that look designed.

        This notebook uses a teaching version of the idea: nine integer genes control a recursive two-dimensional branching figure. Students select among mutants and watch a lineage change over generations.
        """
    ),
    md(
        """
        ## 1. The Mental Model

        A biomorph has two representations:

        - **Genotype**: the nine integer genes.
        - **Phenotype**: the visible branching drawing produced by those genes.

        Each generation follows a small evolutionary loop:

        1. Start with one parent genome.
        2. Make children by changing one or more genes by `+1` or `-1`.
        3. Select one child.
        4. Promote that child to parent.
        5. Repeat.

        The selection in this notebook is artificial: the student or an explicit score chooses. That differs from natural selection, where environmental survival and reproduction decide which variants persist.
        """
    ),
    md("## 2. Build the Genome"),
    md("**Imports and setup.** Load the numerical, plotting, and display tools used by the playground."),
    code(
        """
        from dataclasses import dataclass

        import matplotlib.pyplot as plt
        import numpy as np
        from IPython.display import HTML, clear_output, display
        from matplotlib import animation
        """
    ),
    md("**Genome bounds.** Each gene is an integer; clipping keeps drawings readable and recursion bounded."),
    code(
        """
        GENE_COUNT = 9
        GENE_MIN = np.array([-9, -9, -9, -9, -9, -9, -9, -9, 1])
        GENE_MAX = np.array([9, 9, 9, 9, 9, 9, 9, 9, 8])


        @dataclass(frozen=True)
        class BiomorphGenome:
            genes: tuple[int, ...]

            def __post_init__(self):
                if len(self.genes) != GENE_COUNT:
                    raise ValueError("A biomorph genome must contain exactly 9 genes.")

            @property
            def array(self) -> np.ndarray:
                return np.array(self.genes, dtype=int)
        """
    ),
    md("**Starting parent.** Use a modest, symmetric starting genome so changes are easy to see."),
    code(
        """
        def clip_genes(values: np.ndarray) -> BiomorphGenome:
            clipped = np.clip(values.astype(int), GENE_MIN, GENE_MAX)
            return BiomorphGenome(tuple(int(x) for x in clipped))


        parent = BiomorphGenome((1, 0, 2, 2, 0, 0, 0, 0, 5))
        parent
        """
    ),
    md(
        """
        ## 3. Genotype to Phenotype

        The mapping below is intentionally transparent. It is inspired by Dawkins' biomorphs rather than a byte-for-byte reconstruction of the original program.

        The first eight genes control branch geometry:

        - trunk length
        - length decay
        - left and right branch angles
        - curvature
        - asymmetry
        - fan width
        - twig rotation

        The ninth gene controls recursion depth.
        """
    ),
    md("**Decode genes.** Convert nine integers into drawing parameters."),
    code(
        """
        def decode_genome(genome: BiomorphGenome) -> dict[str, float]:
            g = genome.array
            return {
                "base_length": 8.0 + g[0] * 0.7,
                "decay": np.clip(0.66 + g[1] * 0.018, 0.48, 0.82),
                "left_angle": np.deg2rad(28 + g[2] * 3.2),
                "right_angle": np.deg2rad(28 + g[3] * 3.2),
                "bend": np.deg2rad(g[4] * 1.8),
                "asymmetry": g[5] * 0.025,
                "fan": 1.0 + g[6] * 0.035,
                "twig": np.deg2rad(g[7] * 2.4),
                "depth": int(g[8]),
            }
        """
    ),
    md("**Recursive branches.** Grow a branching stick figure from the decoded parameters."),
    code(
        """
        def biomorph_segments(genome: BiomorphGenome) -> np.ndarray:
            params = decode_genome(genome)
            segments: list[tuple[float, float, float, float, int]] = []

            def grow(x: float, y: float, angle: float, length: float, depth: int, side: int) -> None:
                if depth <= 0 or length <= 0.15:
                    return

                x2 = x + np.cos(angle) * length
                y2 = y + np.sin(angle) * length
                segments.append((x, y, x2, y2, depth))

                next_length = length * params["decay"]
                skew = 1 + side * params["asymmetry"]
                left = angle + side * params["left_angle"] * params["fan"] + params["bend"] + params["twig"]
                right = angle - side * params["right_angle"] * params["fan"] + params["bend"] - params["twig"]

                grow(x2, y2, left, next_length * max(0.35, skew), depth - 1, side)
                grow(x2, y2, right, next_length * max(0.35, 2 - skew), depth - 1, side)

            grow(0, 0, np.pi / 2, params["base_length"], params["depth"], 1)
            grow(0, 0, -np.pi / 2, params["base_length"] * 0.9, params["depth"], -1)
            return np.array(segments, dtype=float)
        """
    ),
    md("**Draw one biomorph.** Normalize the line drawing so every genome fits inside its panel."),
    code(
        """
        def draw_biomorph(genome: BiomorphGenome, ax=None, title: str | None = None, color: str = "#2563eb"):
            if ax is None:
                _, ax = plt.subplots(figsize=(4, 4))

            segments = biomorph_segments(genome)
            if len(segments) == 0:
                return ax

            xy = segments[:, :4].reshape(-1, 2)
            center = xy.mean(axis=0)
            span = np.ptp(xy, axis=0).max()
            scale = 1 if span == 0 else 1.75 / span

            for x1, y1, x2, y2, depth in segments:
                p1 = (np.array([x1, y1]) - center) * scale
                p2 = (np.array([x2, y2]) - center) * scale
                linewidth = 0.55 + 0.16 * depth
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linewidth=linewidth, solid_capstyle="round")

            ax.set_xlim(-1.15, 1.15)
            ax.set_ylim(-1.15, 1.15)
            ax.set_aspect("equal")
            ax.axis("off")
            if title is not None:
                ax.set_title(title, fontsize=10)
            return ax


        draw_biomorph(parent, title=f"parent genes={parent.genes}")
        plt.show()
        """
    ),
    md(
        """
        ## 4. Mutation

        A child is a nearby point in gene space. In this playground, each child mutates a small number of genes by `+1` or `-1`.

        The key idea is locality: children usually resemble the parent, but not exactly. That resemblance lets selection accumulate changes instead of starting from scratch every generation.
        """
    ),
    md("**Mutate one genome.** Change a few randomly chosen genes by one step."),
    code(
        """
        def mutate_genome(
            genome: BiomorphGenome,
            rng: np.random.Generator,
            mutation_count: int = 1,
            step: int = 1,
        ) -> BiomorphGenome:
            values = genome.array.copy()
            for _ in range(mutation_count):
                gene_index = int(rng.integers(0, GENE_COUNT))
                values[gene_index] += int(rng.choice([-step, step]))
            return clip_genes(values)


        rng = np.random.default_rng(7)
        mutate_genome(parent, rng)
        """
    ),
    md("**Make a family.** Create eight mutated children around a parent."),
    code(
        """
        def make_children(
            parent: BiomorphGenome,
            seed: int,
            child_count: int = 8,
            mutation_count: int = 1,
        ) -> list[BiomorphGenome]:
            rng = np.random.default_rng(seed)
            children = []
            seen = {parent.genes}
            while len(children) < child_count:
                child = mutate_genome(parent, rng, mutation_count=mutation_count)
                if child.genes not in seen:
                    children.append(child)
                    seen.add(child.genes)
            return children


        children = make_children(parent, seed=3)
        [child.genes for child in children[:3]]
        """
    ),
    md(
        """
        ## 5. The 3x3 Selection Panel

        The parent sits in the center. Eight children surround it. In a notebook environment with widgets, the buttons let the student choose a child and advance the lineage. The fallback cells still show the same idea with a chosen child index.
        """
    ),
    md("**Panel renderer.** Draw parent plus eight children in a stable 3x3 layout."),
    code(
        """
        PANEL_POSITIONS = [
            (0, 0), (0, 1), (0, 2),
            (1, 0),         (1, 2),
            (2, 0), (2, 1), (2, 2),
        ]


        def draw_family(parent: BiomorphGenome, children: list[BiomorphGenome], generation: int = 0, selected: int | None = None):
            fig, axes = plt.subplots(3, 3, figsize=(8, 8))
            for ax in axes.ravel():
                ax.axis("off")

            for child_index, (row, col) in enumerate(PANEL_POSITIONS):
                color = "#f97316" if selected == child_index else "#2563eb"
                draw_biomorph(children[child_index], ax=axes[row, col], title=f"child {child_index}", color=color)

            draw_biomorph(parent, ax=axes[1, 1], title=f"parent | generation {generation}", color="#111827")
            fig.suptitle("Artificial selection panel", fontsize=14)
            plt.tight_layout()
            return fig


        draw_family(parent, children, generation=0)
        plt.show()
        """
    ),
    md("**Manual selection.** Change `chosen_child` and rerun to promote a different child."),
    code(
        """
        chosen_child = 2
        next_parent = children[chosen_child]
        print("chosen child:", chosen_child)
        print("parent genes:", parent.genes)
        print("child genes :", next_parent.genes)

        draw_family(parent, children, generation=0, selected=chosen_child)
        plt.show()
        """
    ),
    md("**Clickable playground.** Use buttons when `ipywidgets` is available."),
    code(
        """
        try:
            import ipywidgets as widgets

            state = {
                "parent": parent,
                "generation": 0,
                "seed": 100,
                "children": make_children(parent, seed=100),
            }
            output = widgets.Output()

            def redraw(selected: int | None = None):
                with output:
                    clear_output(wait=True)
                    draw_family(state["parent"], state["children"], generation=state["generation"], selected=selected)
                    plt.show()

            def choose(index: int):
                state["parent"] = state["children"][index]
                state["generation"] += 1
                state["seed"] += 1
                state["children"] = make_children(state["parent"], seed=state["seed"])
                redraw()

            buttons = []
            for i in range(8):
                button = widgets.Button(description=f"choose {i}", layout=widgets.Layout(width="86px"))
                button.on_click(lambda _, i=i: choose(i))
                buttons.append(button)

            redraw()
            display(widgets.HBox(buttons), output)
        except Exception:
            print("ipywidgets is not available. Use the manual selection cell above.")
        """
    ),
    md(
        """
        ## 6. A Scripted Selection Run

        Human preference is hard to test in a static notebook, so we can also define an explicit selection score. This does not claim to model biological fitness. It is a controlled way to show cumulative selection.

        The score below rewards visual spread and branch count. It tends to select larger, more intricate forms.
        """
    ),
    md("**Phenotype metrics.** Measure visible complexity from the line segments."),
    code(
        """
        def phenotype_metrics(genome: BiomorphGenome) -> dict[str, float]:
            segments = biomorph_segments(genome)
            xy = segments[:, :4].reshape(-1, 2)
            width = float(np.ptp(xy[:, 0]))
            height = float(np.ptp(xy[:, 1]))
            total_length = float(np.sum(np.linalg.norm(segments[:, 2:4] - segments[:, 0:2], axis=1)))
            return {
                "segments": float(len(segments)),
                "width": width,
                "height": height,
                "total_length": total_length,
                "area_proxy": width * height,
            }


        def visual_interest_score(genome: BiomorphGenome) -> float:
            metrics = phenotype_metrics(genome)
            return metrics["area_proxy"] + 0.06 * metrics["total_length"] + 0.45 * metrics["segments"]


        phenotype_metrics(parent)
        """
    ),
    md("**Cumulative selection.** Repeatedly choose the highest-scoring child."),
    code(
        """
        def run_selection(
            start: BiomorphGenome,
            generations: int = 10,
            seed: int = 20,
            mutation_count: int = 1,
        ) -> list[dict]:
            lineage = []
            current = start
            for generation in range(generations + 1):
                score = visual_interest_score(current)
                lineage.append({
                    "generation": generation,
                    "genome": current,
                    "score": score,
                    "metrics": phenotype_metrics(current),
                })
                children = make_children(current, seed=seed + generation, mutation_count=mutation_count)
                current = max(children, key=visual_interest_score)
            return lineage


        lineage = run_selection(parent, generations=10, seed=42)
        [(step["generation"], round(step["score"], 1), step["genome"].genes) for step in lineage[:4]]
        """
    ),
    md("**Lineage strip.** Compare generation 0 against later selected descendants."),
    code(
        """
        def draw_lineage(lineage: list[dict]):
            picks = [0, len(lineage) // 4, len(lineage) // 2, 3 * len(lineage) // 4, len(lineage) - 1]
            fig, axes = plt.subplots(1, len(picks), figsize=(14, 3.2))
            for ax, index in zip(axes, picks):
                step = lineage[index]
                draw_biomorph(
                    step["genome"],
                    ax=ax,
                    title=f'gen {step["generation"]}\\nscore {step["score"]:.0f}',
                    color="#2563eb",
                )
            plt.tight_layout()
            return fig


        draw_lineage(lineage)
        plt.show()
        """
    ),
    md("**Score plot.** Watch whether selected variation accumulates in the chosen direction."),
    code(
        """
        def plot_lineage_scores(lineage: list[dict]):
            generations = [step["generation"] for step in lineage]
            scores = [step["score"] for step in lineage]
            plt.figure(figsize=(7, 3.4))
            plt.plot(generations, scores, marker="o", color="#2563eb")
            plt.xlabel("generation")
            plt.ylabel("visual interest score")
            plt.title("Cumulative selection under an explicit score")
            plt.grid(alpha=0.25)
            plt.show()


        plot_lineage_scores(lineage)
        """
    ),
    md(
        """
        ## 7. Selection Versus Random Drift

        To isolate the effect of selection, compare the scripted selector against a random walk that mutates but chooses a random child each generation.
        """
    ),
    md("**Random drift baseline.** Keep mutation but remove directed selection."),
    code(
        """
        def run_random_drift(start: BiomorphGenome, generations: int = 10, seed: int = 20) -> list[dict]:
            rng = np.random.default_rng(seed)
            lineage = []
            current = start
            for generation in range(generations + 1):
                lineage.append({
                    "generation": generation,
                    "genome": current,
                    "score": visual_interest_score(current),
                    "metrics": phenotype_metrics(current),
                })
                children = make_children(current, seed=seed + generation)
                current = children[int(rng.integers(0, len(children)))]
            return lineage


        selected = run_selection(parent, generations=16, seed=50)
        drift = run_random_drift(parent, generations=16, seed=50)

        plt.figure(figsize=(7, 3.6))
        plt.plot([s["generation"] for s in selected], [s["score"] for s in selected], marker="o", label="selected")
        plt.plot([s["generation"] for s in drift], [s["score"] for s in drift], marker="o", label="random drift")
        plt.xlabel("generation")
        plt.ylabel("visual interest score")
        plt.title("Mutation with and without selection")
        plt.legend()
        plt.grid(alpha=0.25)
        plt.show()
        """
    ),
    md("**Animate the selected lineage.** Replay the cumulative walk through gene space."),
    code(
        """
        def animate_lineage(lineage: list[dict]) -> HTML:
            fig, ax = plt.subplots(figsize=(4, 4))

            def update(frame_index: int):
                ax.clear()
                step = lineage[frame_index]
                draw_biomorph(step["genome"], ax=ax, title=f'gen {step["generation"]} | score {step["score"]:.0f}')

            anim = animation.FuncAnimation(fig, update, frames=len(lineage), interval=260)
            plt.close(fig)
            return HTML(anim.to_jshtml())


        animate_lineage(selected)
        """
    ),
    md(
        """
        ## 8. Failure Modes

        Artificial selection is powerful, but the knobs matter.

        - **Mutation too small**: the lineage can stagnate.
        - **Mutation too large**: children stop resembling the parent, so selection loses continuity.
        - **Depth too high**: recursion can explode the number of branches.
        - **Selection score too narrow**: the run optimizes the score, not some universal notion of beauty or fitness.
        """
    ),
    md("**Mutation pressure.** Compare conservative and aggressive mutation settings."),
    code(
        """
        conservative = run_selection(parent, generations=8, seed=80, mutation_count=1)
        aggressive = run_selection(parent, generations=8, seed=80, mutation_count=5)

        fig, axes = plt.subplots(2, 3, figsize=(9, 6))
        for row, (label, run) in enumerate([("conservative", conservative), ("aggressive", aggressive)]):
            for col, index in enumerate([0, len(run) // 2, len(run) - 1]):
                draw_biomorph(run[index]["genome"], ax=axes[row, col], title=f"{label}\\ngen {run[index]['generation']}")
        plt.tight_layout()
        plt.show()
        """
    ),
    md(
        """
        ## 9. Mini-Challenge

        Try one:

        1. Change one gene by hand and describe the visible effect.
        2. Run 10 generations by selecting children yourself. Save the final genome and describe its ancestry.
        3. Change the scoring function and compare the selected lineage.
        4. Cap the depth gene at `5`, then explain the complexity tradeoff.
        """
    ),
    md("**Manual gene edit.** Change one number and compare parent versus edited phenotype."),
    code(
        """
        edited = clip_genes(parent.array + np.array([0, 0, 3, -2, 1, 0, 0, 0, 1]))

        fig, axes = plt.subplots(1, 2, figsize=(7, 3.5))
        draw_biomorph(parent, ax=axes[0], title=f"parent\\n{parent.genes}", color="#111827")
        draw_biomorph(edited, ax=axes[1], title=f"edited\\n{edited.genes}", color="#f97316")
        plt.tight_layout()
        plt.show()
        """
    ),
    md(
        """
        ## Visual Trace + Rigor Studio

        **Problem frame.** Show how complex-looking forms can emerge from a compact genome, random mutation, and non-random artificial selection.

        **Interactive animation target.** Render a parent biomorph in the center of a 3x3 grid, surround it with eight mutants, and let a selected child become the next parent.

        **Correctness handle.** Every child genome differs from the parent by bounded integer mutations, and every phenotype is deterministically drawn from its genome.

        **Complexity handle.** Drawing cost is proportional to the number of recursive branches. With binary branching and depth `d`, the teaching renderer is `O(2^d)` per biomorph, capped by the depth gene.

        **Failure mode to test.** Increase mutation count and show how too much mutation breaks visual continuity between parent and child.

        **Studio task.** Record a 10-generation lineage, explain which genes changed, and distinguish random mutation from non-random selection.
        """
    ),
    md(
        """
        ## Sources and Further Reading

        - Richard Dawkins, *The Blind Watchmaker* (1986), the original popular presentation of Biomorphs.
        - Open Library, [The Blind Watchmaker](https://openlibrary.org/works/OL1966501W/The_Blind_Watchmaker)
        - Richard Dawkins and later biomorph research discussed in [The evolution of evolvability in artificial life](https://pmc.ncbi.nlm.nih.gov/articles/PMC10971585/)

        This notebook uses a transparent teaching implementation of nine-gene recursive biomorphs. It is designed for experimentation rather than exact historical emulation of Dawkins' original program.
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
