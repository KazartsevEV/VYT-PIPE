"""Generate A4 tiles with overlap, markers, and numbering."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Tuple

from vyt.utils.units import mm_to_px

A4_MM: Tuple[float, float] = (210.0, 297.0)


def _parse_grid(grid: str) -> Tuple[int, int]:
    cleaned = grid.lower().replace(" ", "")
    cols_str, rows_str = cleaned.split("x", 1)
    return int(cols_str), int(rows_str)


def _strip_xml_declaration(svg_text: str) -> str:
    text = svg_text.lstrip()
    if text.startswith("<?xml"):
        _, _, rest = text.partition("?>")
        return rest.lstrip()
    return svg_text


def _cross_marker(cx: float, cy: float, size: float) -> str:
    half = size / 2
    return (
        f'<g stroke="#000" stroke-width="2" fill="none">'
        f'<line x1="{cx - half}" y1="{cy}" x2="{cx + half}" y2="{cy}" />'
        f'<line x1="{cx}" y1="{cy - half}" x2="{cx}" y2="{cy + half}" />'
        "</g>"
    )


def _mini_map(
    cols: int,
    rows: int,
    current_col: int,
    current_row: int,
    offset_x: float,
    offset_y: float,
    tile_w_vb: float,
) -> str:
    cell = 35
    padding = 12
    panel_w = cols * cell + padding * 2
    panel_h = rows * cell + padding * 2
    origin_x = offset_x + tile_w_vb - panel_w - 60
    origin_y = offset_y + 40
    rects = [
        f'<rect x="{origin_x}" y="{origin_y}" width="{panel_w}" '
        f'height="{panel_h}" fill="#f0f0f0" stroke="#444" stroke-width="2" />'
    ]
    for r in range(rows):
        for c in range(cols):
            x = origin_x + padding + c * cell
            y = origin_y + padding + r * cell
            fill = "#1a73e8" if (c == current_col and r == current_row) else "none"
            rects.append(
                f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" '
                f'stroke="#444" stroke-width="2" fill="{fill}" />'
            )
    legend = (
        f'<text x="{origin_x}" y="{origin_y + panel_h + 28}" '
        'font-family="Arial" font-size="24" fill="#000">Layout</text>'
    )
    return "".join(rects) + legend


def to_tiles(scene_svg: Path, cfg: Dict[str, Any], work: Path) -> List[Path]:
    """Split the composed scene into printable A4 tiles."""

    dpi = int(cfg["dpi"])
    margins_px = mm_to_px(cfg["margins_mm"], dpi)
    overlap_px = mm_to_px(cfg["overlap_mm"], dpi)
    cols, rows = _parse_grid(cfg["grid"])

    a4_w_px = mm_to_px(A4_MM[0], dpi)
    a4_h_px = mm_to_px(A4_MM[1], dpi)

    tile_w_vb = a4_w_px - 2 * margins_px + 2 * overlap_px
    tile_h_vb = a4_h_px - 2 * margins_px + 2 * overlap_px
    step_x = tile_w_vb - 2 * overlap_px
    step_y = tile_h_vb - 2 * overlap_px

    tiles_dir = work / "tiles" / "svg"
    tiles_dir.mkdir(parents=True, exist_ok=True)

    scene_content = _strip_xml_declaration(scene_svg.read_text(encoding="utf-8"))

    tiles: List[Path] = []
    for row in range(rows):
        for col in range(cols):
            offset_x = col * step_x
            offset_y = row * step_y
            page_number = row * cols + col + 1

            cross_size = 60
            cross_offset = 80
            markers = "".join(
                [
                    _cross_marker(offset_x + cross_offset, offset_y + cross_offset, cross_size),
                    _cross_marker(offset_x + tile_w_vb - cross_offset, offset_y + cross_offset, cross_size),
                    _cross_marker(offset_x + cross_offset, offset_y + tile_h_vb - cross_offset, cross_size),
                    _cross_marker(
                        offset_x + tile_w_vb - cross_offset,
                        offset_y + tile_h_vb - cross_offset,
                        cross_size,
                    ),
                ]
            )

            numbering = (
                f'<text x="{offset_x + tile_w_vb / 2}" y="{offset_y + tile_h_vb - 40}" '
                'text-anchor="middle" font-family="Arial" font-size="42" fill="#000">'
                f'Row {row + 1} / Col {col + 1}</text>'
            )

            mini_map = _mini_map(cols, rows, col, row, offset_x, offset_y, tile_w_vb)

            cut_box = (
                f'<rect x="{offset_x}" y="{offset_y}" width="{tile_w_vb}" height="{tile_h_vb}" '
                'fill="none" stroke="#555" stroke-dasharray="12 8" stroke-width="3" />'
            )

            bg_color = cfg.get("bg_gray", "#A0A0A0")

            svg = f"""
<svg xmlns="http://www.w3.org/2000/svg"
     width="{A4_MM[0]}mm" height="{A4_MM[1]}mm"
     viewBox="{offset_x} {offset_y} {tile_w_vb} {tile_h_vb}">
  <rect x="{offset_x}" y="{offset_y}" width="{tile_w_vb}" height="{tile_h_vb}" fill="{bg_color}" />
  {scene_content}
  {markers}
  {cut_box}
  {numbering}
  {mini_map}
  <text x="{offset_x + 40}" y="{offset_y + 80}" font-family="Arial" font-size="24" fill="#000">Page {page_number}</text>
</svg>
"""
            tile_path = tiles_dir / f"tile_{row + 1:02d}_{col + 1:02d}.svg"
            tile_path.write_text(svg, encoding="utf-8")
            tiles.append(tile_path)

    return tiles
