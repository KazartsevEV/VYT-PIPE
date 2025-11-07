"""Filesystem helper utilities."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable


def ensure_dirs(paths: Iterable[Path]) -> None:
    """Ensure that each provided path exists as a directory."""
    for path in paths:
        path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    """Write text content to a file using UTF-8 encoding."""
    path.write_text(content, encoding="utf-8")
