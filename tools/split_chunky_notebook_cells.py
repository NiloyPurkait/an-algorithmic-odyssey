"""Split oversized notebook code cells into smaller lesson steps.

The splitter is deliberately conservative: it cuts only between top-level
Python statements. Large classes, functions, loops, and try blocks remain intact
because splitting inside them would break syntax or execution order.
"""

from __future__ import annotations

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MIN_LINES_TO_SPLIT = 25
TARGET_LINES_PER_CHUNK = 22
INTRO_MARKER = "chunky_split_intro_v1"
CODE_MARKER = "chunky_split_code_v1"


def line_count(source: str) -> int:
    return len(source.splitlines())


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    if isinstance(source, list):
        return "".join(source)
    return source


def markdown_cell(text: str) -> dict:
    return {
        "cell_type": "markdown",
        "metadata": {"course_upgrade": INTRO_MARKER},
        "source": text.strip() + "\n",
    }


def code_cell(source: str, original_metadata: dict) -> dict:
    metadata = dict(original_metadata)
    metadata["course_upgrade"] = CODE_MARKER
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": metadata,
        "outputs": [],
        "source": source.strip("\n") + "\n",
    }


def split_source(source: str) -> list[str]:
    if line_count(source) < MIN_LINES_TO_SPLIT:
        return [source]

    try:
        tree = ast.parse(source)
    except SyntaxError:
        return [source]

    if len(tree.body) <= 1:
        return [source]

    lines = source.splitlines()
    segments: list[str] = []
    cursor = 0
    for node in tree.body:
        start = max(cursor, getattr(node, "lineno", 1) - 1)
        end = getattr(node, "end_lineno", None)
        if end is None:
            return [source]
        segment_lines = lines[cursor:end]
        segment = "\n".join(segment_lines).strip("\n")
        if segment.strip():
            segments.append(segment)
        cursor = end
    if cursor < len(lines):
        tail = "\n".join(lines[cursor:]).strip("\n")
        if tail.strip():
            segments.append(tail)

    chunks: list[str] = []
    current: list[str] = []
    current_lines = 0
    for segment in segments:
        segment_lines = line_count(segment)
        if current and current_lines + segment_lines > TARGET_LINES_PER_CHUNK:
            chunks.append("\n\n".join(current))
            current = [segment]
            current_lines = segment_lines
        else:
            current.append(segment)
            current_lines += segment_lines
    if current:
        chunks.append("\n\n".join(current))

    if len(chunks) == 1:
        return [source]
    return chunks


def describe_chunk(source: str, index: int, total: int) -> str:
    try:
        tree = ast.parse(source)
    except SyntaxError:
        return "**Setup.** Run this smaller block before continuing."

    kinds = [type(node).__name__ for node in tree.body]
    names = []
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.append(node.name)
        elif isinstance(node, ast.Assign):
            for target in node.targets:
                names.extend(extract_target_names(target))
        elif isinstance(node, ast.AnnAssign):
            names.extend(extract_target_names(node.target))

    if all(kind in {"Import", "ImportFrom"} for kind in kinds):
        return "**Imports and setup.** Load the libraries and shared setup used by the next cells."
    elif any(kind == "ClassDef" for kind in kinds):
        class_names = [node.name for node in tree.body if isinstance(node, ast.ClassDef)]
        return f"**Object model.** Define `{', '.join(class_names)}`, the named structure used by the simulation."
    elif any(kind in {"FunctionDef", "AsyncFunctionDef"} for kind in kinds):
        function_names = [
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        ]
        shown = ", ".join(f"`{name}`" for name in function_names[:4])
        if len(function_names) > 4:
            shown += ", ..."
        return f"**Helper functions.** Define {shown} so later cells stay focused on behavior."
    elif any(kind in {"For", "While"} for kind in kinds):
        return "**Run the experiment.** Advance the algorithm and record how state changes."
    elif any(kind == "Try" for kind in kinds):
        return "**Interactive display.** Build the widget path, with a fallback for simpler notebook environments."
    elif any(kind in {"If", "With"} for kind in kinds):
        return "**Control path.** Handle the condition or display context before continuing."
    elif any(kind == "Expr" for kind in kinds):
        return "**Inspect the result.** Display the current output so the behavior is visible."
    elif names:
        shown = ", ".join(f"`{name}`" for name in names[:5])
        if len(names) > 5:
            shown += ", ..."
        return f"**Example state.** Create the next piece of working state: {shown}."
    else:
        return "**Next piece.** Run this smaller block, then pause to check what changed."


def extract_target_names(target: ast.AST) -> list[str]:
    if isinstance(target, ast.Name):
        return [target.id]
    if isinstance(target, (ast.Tuple, ast.List)):
        names: list[str] = []
        for item in target.elts:
            names.extend(extract_target_names(item))
        return names
    if isinstance(target, ast.Attribute):
        return [target.attr]
    return []


def split_notebook(path: Path) -> tuple[int, int]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    new_cells: list[dict] = []
    split_cells = 0
    added_markdown = 0

    for cell in notebook.get("cells", []):
        if cell.get("metadata", {}).get("course_upgrade") == INTRO_MARKER:
            continue
        if cell.get("cell_type") != "code":
            new_cells.append(cell)
            continue

        source = cell_source(cell)
        chunks = split_source(source)
        if len(chunks) == 1:
            new_cells.append(cell)
            continue

        split_cells += 1
        original_metadata = cell.get("metadata", {})
        for index, chunk in enumerate(chunks, start=1):
            new_cells.append(markdown_cell(describe_chunk(chunk, index, len(chunks))))
            new_cells.append(code_cell(chunk, original_metadata))
            added_markdown += 1

    notebook["cells"] = new_cells
    if split_cells:
        path.write_text(json.dumps(notebook, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    return split_cells, added_markdown


def main() -> None:
    total_split = 0
    total_markdown = 0
    for path in sorted(ROOT.rglob("*.ipynb")):
        split_cells, added_markdown = split_notebook(path)
        if split_cells:
            total_split += split_cells
            total_markdown += added_markdown
            rel = path.relative_to(ROOT)
            print(f"{rel}: split {split_cells} cells into {added_markdown} guided steps")
    print(f"total_split_cells={total_split}")
    print(f"total_added_markdown={total_markdown}")


if __name__ == "__main__":
    main()
