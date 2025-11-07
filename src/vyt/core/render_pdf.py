"""PDF rendering helpers (placeholder)."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

import cairosvg
from pikepdf import Pdf


def build(tiles_svg: Iterable[Path], cfg: Dict[str, Any], work: Path, out: Path) -> Tuple[List[Path], Path, Path, Path]:
    """Render SVG tiles to PDFs and merge them into a single document."""
    pdf_pages: List[Path] = []
    for index, tile in enumerate(tiles_svg, start=1):
        pdf_path = work / "tiles" / "pdf" / f"tile_{index:02d}.pdf"
        pdf_path.parent.mkdir(parents=True, exist_ok=True)
        cairosvg.svg2pdf(url=str(tile), write_to=str(pdf_path))
        pdf_pages.append(pdf_path)

    full_pdf = out / f"VYT_{cfg['id']}_A4_pages.pdf"
    merged = Pdf.new()
    for pdf in pdf_pages:
        merged.pages.extend(Pdf.open(pdf).pages)
    merged.save(full_pdf)

    cover_pdf = out / f"VYT_{cfg['id']}_cover.pdf"
    cover_pdf.write_bytes(b"%PDF-1.4\n% cover stub\n")

    instructions_pdf = out / f"VYT_{cfg['id']}_instructions.pdf"
    instructions_pdf.write_bytes(b"%PDF-1.4\n% instructions stub\n")

    return pdf_pages, full_pdf, cover_pdf, instructions_pdf
