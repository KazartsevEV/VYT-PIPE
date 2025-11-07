"""Preview generation stub."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def make(scene_svg: Path, cfg: Dict[str, Any], out: Path) -> Path:
    """Create an empty placeholder preview file."""
    preview_path = out / f"VYT_{cfg['id']}_preview.jpg"
    preview_path.write_bytes(b"")
    return preview_path
