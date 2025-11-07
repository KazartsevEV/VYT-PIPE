"""Scene composition stub."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def build_scene(vector_svg: Path, cfg: Dict[str, Any], work: Path) -> Path:
    """Return the provided vector path as the composed scene placeholder."""
    return vector_svg
