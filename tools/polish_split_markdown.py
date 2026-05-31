"""Polish generated notebook lead-ins after splitting chunky code cells."""

from __future__ import annotations

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INTRO_MARKER = "chunky_split_intro_v1"


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def target_names(target: ast.AST) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        names: list[str] = []
        for item in target.elts:
            names.extend(target_names(item))
        return names
    if isinstance(target, ast.Attribute):
        return [target.attr]
    return []


def short_list(items: list[str], limit: int = 4) -> str:
    shown = items[:limit]
    text = ", ".join(f"`{item}`" for item in shown)
    if len(items) > limit:
        text += ", and related helpers"
    return text


def classify_classes(names: list[str]) -> tuple[str, str]:
    name_text = short_list(names)
    lowered = " ".join(names).lower()
    if any(word in lowered for word in ["runner", "solver", "workshop", "machine", "bot"]):
        return "Algorithm engine", f"Define {name_text}, the class that runs the main simulation or algorithm."
    if any(word in lowered for word in ["replay", "snapshot", "step"]):
        return "Trace model", f"Define {name_text}, the structure used to capture replayable algorithm state."
    if any(word in lowered for word in ["graph", "grid", "diagram", "world", "tape"]):
        return "State model", f"Define {name_text}, the data structure the lesson will operate on."
    return "Object model", f"Define {name_text}, the named objects used by the next examples."


def polished_intro(source: str) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "**Setup.** Run this smaller block before continuing."

    body = tree.body
    if not body:
        return "**Setup.** Run this smaller block before continuing."

    kinds = [type(node).__name__ for node in body]

    if all(kind in {"Import", "ImportFrom"} for kind in kinds):
        return "**Imports and setup.** Load the libraries and shared tools used by the lesson."

    class_names = [node.name for node in body if isinstance(node, ast.ClassDef)]
    if class_names:
        label, sentence = classify_classes(class_names)
        return f"**{label}.** {sentence}"

    function_names = [
        node.name
        for node in body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    ]
    if function_names:
        prefix = " ".join(function_names).lower()
        if any(name.startswith(("draw_", "plot_", "render_", "display_")) for name in function_names):
            return f"**Visual helper.** Define {short_list(function_names)}, which turns state into something students can inspect."
        if any(name.startswith(("build_", "make_", "create_")) for name in function_names):
            return f"**Builder helper.** Define {short_list(function_names)}, which prepares reusable examples or traces."
        if any(name.startswith(("run_", "simulate_", "step_")) for name in function_names):
            return f"**Simulation helper.** Define {short_list(function_names)}, which advances the model and records behavior."
        if "distance" in prefix or "cost" in prefix or "score" in prefix:
            return f"**Scoring helper.** Define {short_list(function_names)}, which measures the quantity the algorithm optimizes."
        return f"**Helper functions.** Define {short_list(function_names)} so the later cells stay focused on behavior."

    assigned: list[str] = []
    for node in body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                assigned.extend(target_names(target))
        elif isinstance(node, ast.AnnAssign):
            assigned.extend(target_names(node.target))

    if any(kind in {"For", "While"} for kind in kinds):
        return "**Run the experiment.** Advance the algorithm and collect the state changes that make the behavior visible."

    if any(kind == "Try" for kind in kinds):
        return "**Interactive display.** Build the widget path when available, with a notebook-friendly fallback."

    if any(kind == "If" for kind in kinds):
        return "**Conditional path.** Handle the case distinction before moving to the next example."

    if any(kind == "With" for kind in kinds):
        return "**Display context.** Prepare the output area or file context for the next visual result."

    source_lower = source.lower()
    if any(word in source_lower for word in ["display(", "plt.", "animation", "html("]):
        return "**Inspect the result.** Render the current state so the algorithm is easier to reason about."

    if assigned:
        return f"**Example state.** Create {short_list(assigned)}, the concrete values used in the next run."

    if any(kind == "Expr" for kind in kinds):
        return "**Inspect the result.** Evaluate the expression and read the output before changing parameters."

    return "**Next piece.** Run this smaller block, then pause to check what changed."


def main() -> None:
    changed_cells = 0
    for path in sorted(ROOT.rglob("*.ipynb")):
        notebook = json.loads(path.read_text(encoding="utf-8"))
        changed = False
        cells = notebook.get("cells", [])
        for index, cell in enumerate(cells):
            if cell.get("cell_type") != "markdown":
                continue
            if cell.get("metadata", {}).get("course_upgrade") != INTRO_MARKER:
                continue
            next_code = None
            for candidate in cells[index + 1 :]:
                if candidate.get("cell_type") == "code":
                    next_code = candidate
                    break
                if candidate.get("cell_type") == "markdown":
                    break
            if next_code is None:
                continue
            new_source = polished_intro(cell_source(next_code)) + "\n"
            if cell_source(cell) != new_source:
                cell["source"] = new_source
                changed = True
                changed_cells += 1
        if changed:
            path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
            print(path.relative_to(ROOT))
    print(f"polished_intro_cells={changed_cells}")


if __name__ == "__main__":
    main()
