from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
README_PATH = PROJECT_ROOT / "README.md"

IGNORE_DIRS = {
    ".git",
    "__pycache__",
    ".venv",
    "venv",
    ".idea",
    ".vscode",
    ".pytest_cache",
}

IGNORE_FILES = {
    ".DS_Store",
}

START_MARKER = "<!-- PROJECT_STRUCTURE_START -->"
END_MARKER = "<!-- PROJECT_STRUCTURE_END -->"


def generate_tree(path: Path, prefix: str = "") -> list[str]:
    items = sorted(
        [p for p in path.iterdir() if not should_ignore(p)],
        key=lambda p: (p.is_file(), p.name.lower())
    )

    lines = []

    for index, item in enumerate(items):
        is_last = index == len(items) - 1
        connector = "└── " if is_last else "├── "

        lines.append(f"{prefix}{connector}{item.name}{'/' if item.is_dir() else ''}")

        if item.is_dir():
            extension = "    " if is_last else "│   "
            lines.extend(generate_tree(item, prefix + extension))

    return lines


def should_ignore(path: Path) -> bool:
    if path.is_dir() and path.name in IGNORE_DIRS:
        return True
    if path.is_file() and path.name in IGNORE_FILES:
        return True
    return False


def update_readme():
    if not README_PATH.exists():
        raise FileNotFoundError("README.md not found.")

    readme = README_PATH.read_text(encoding="utf-8")

    if START_MARKER not in readme or END_MARKER not in readme:
        raise ValueError("README.md must contain PROJECT_STRUCTURE markers.")

    tree_lines = [f"{PROJECT_ROOT.name}/"]
    tree_lines.extend(generate_tree(PROJECT_ROOT))

    tree_block = "```text\n" + "\n".join(tree_lines) + "\n```"

    before = readme.split(START_MARKER)[0]
    after = readme.split(END_MARKER)[1]

    new_readme = (
        before
        + START_MARKER
        + "\n\n"
        + tree_block
        + "\n\n"
        + END_MARKER
        + after
    )

    README_PATH.write_text(new_readme, encoding="utf-8")


if __name__ == "__main__":
    update_readme()
    print("README.md project structure updated.")