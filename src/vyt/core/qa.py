"""QA placeholder module."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable


def run(mask_png: Path, vector_svg: Path, tiles_svg: Iterable[Path], cfg: Dict[str, Any], out: Path) -> Path:
    """Write a stub QA JSON file."""
    qa_path = out / "QA.json"
    qa_path.write_text(
        json.dumps({"id": cfg["id"], "status": "stub"}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return qa_path
