"""Orchestrator for the VYT-PIPE processing pipeline."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict

from vyt.core import (
    bridge,
    compose,
    ingest,
    mask,
    pack,
    preview,
    qa,
    render_pdf,
    render_pptx,
    tile,
    vectorize,
)


def run_pipeline(cfg: Dict[str, Any]) -> Dict[str, Any]:
    """Execute the pipeline for a single configuration dictionary."""
    identifier = cfg["id"]
    root = Path("build") / identifier
    work = root / "work"
    out = root / "out"
    source_dir = work / "source_copy"

    for path in (work, out, source_dir):
        path.mkdir(parents=True, exist_ok=True)

    src_img = ingest.copy_sources(cfg, source_dir)
    mask_png = mask.build_mask(src_img, cfg, work)
    mask_fixed = bridge.enforce(mask_png, cfg, work)
    vector_svg = vectorize.to_svg(mask_fixed, cfg, work)
    scene_svg = compose.build_scene(vector_svg, cfg, work)
    tiles_svg = tile.to_tiles(scene_svg, cfg, work)
    pdf_pages, pdf_full, cover_pdf, instructions_pdf = render_pdf.build(tiles_svg, cfg, work, out)
    pptx_path = render_pptx.build(tiles_svg, cfg, work, out)
    preview_path = preview.make(scene_svg, cfg, out)
    qa_json = qa.run(mask_fixed, vector_svg, tiles_svg, cfg, out)
    zip_path = pack.make_zip(out, root / f"VYT_{identifier}.zip")

    return {
        "id": identifier,
        "time": datetime.now().isoformat(timespec="seconds"),
        "pdf": str(pdf_full),
        "cover": str(cover_pdf),
        "instructions": str(instructions_pdf),
        "pptx": str(pptx_path),
        "preview": str(preview_path),
        "zip": str(zip_path),
        "qa": str(qa_json),
    }
