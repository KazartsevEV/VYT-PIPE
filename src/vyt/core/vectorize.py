"""Vectorization stub module."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def to_svg(mask_png: Path, cfg: Dict[str, Any], work: Path) -> Path:
    """Produce a placeholder SVG referencing the raster mask."""
    svg_path = work / "vector.svg"
    svg_path.write_text(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" width="100%" height="100%">'
            f'<image href="{mask_png.as_posix()}" preserveAspectRatio="xMidYMid meet"/>'
            "</svg>"
        ),
        encoding="utf-8",
    )
    return svg_path
