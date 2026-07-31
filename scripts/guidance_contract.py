"""Shared guidance-document lifecycle contract for repository scripts."""

from __future__ import annotations

import re
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent
ACTIVE_AREAS = ("architecture", "libraries", "practices", "stacks")
SETTLED_STATUSES = frozenset({"accepted", "deprecated"})
ALLOWED_FRONTMATTER_FIELDS = {"status"}
REQUIRED_HEADINGS = {
    "accepted": ("Decision", "Revisit when"),
    "draft": (
        "Tentative preference",
        "Why this is uncertain",
        "Promotion questions",
        "If accepted",
    ),
    "deprecated": ("Replacement", "Rationale"),
}


def guidance_documents() -> list[tuple[Path, set[str]]]:
    """Return guidance documents and the statuses allowed at each path."""
    documents: list[tuple[Path, set[str]]] = []

    for area in ACTIVE_AREAS:
        for path in sorted((REPOSITORY_ROOT / area).rglob("*.md")):
            if path.name != "README.md":
                documents.append((path, {"accepted", "deprecated"}))

    for path in sorted((REPOSITORY_ROOT / "draft").rglob("*.md")):
        if path.name != "README.md":
            documents.append((path, {"draft"}))

    return documents


def parse_frontmatter(lines: list[str]) -> tuple[dict[str, str], int, list[str]]:
    """Parse the repository's deliberately minimal frontmatter format."""
    errors: list[str] = []
    if not lines or lines[0] != "---":
        return {}, 0, ["must begin with YAML frontmatter"]

    try:
        closing_index = lines.index("---", 1)
    except ValueError:
        return {}, 0, ["frontmatter is missing its closing delimiter"]

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:closing_index], start=2):
        if not line:
            continue

        match = re.fullmatch(r"([a-z][a-z0-9_-]*): ([a-z][a-z0-9_-]*)", line)
        if match is None:
            errors.append(f"line {line_number}: unsupported frontmatter syntax")
            continue

        key, value = match.groups()
        if key in fields:
            errors.append(f"line {line_number}: duplicate frontmatter field {key!r}")
            continue
        fields[key] = value

    unknown_fields = sorted(fields.keys() - ALLOWED_FRONTMATTER_FIELDS)
    if unknown_fields:
        errors.append(f"unknown frontmatter fields: {', '.join(unknown_fields)}")

    return fields, closing_index + 1, errors
