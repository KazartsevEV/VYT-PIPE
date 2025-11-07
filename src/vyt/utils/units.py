"""Unit conversion helpers."""

from __future__ import annotations


def mm_to_px(mm: float, dpi: int) -> int:
    """Convert millimetres to pixels at the specified DPI."""
    return round(mm * dpi / 25.4)


def cm_to_px(cm: float, dpi: int) -> int:
    """Convert centimetres to pixels at the specified DPI."""
    return round(cm * dpi / 2.54)
