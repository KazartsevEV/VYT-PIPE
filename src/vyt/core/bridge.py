"""Enforce minimal bridge thickness on mask silhouettes."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import cv2
import numpy as np
from PIL import Image

from vyt.utils.units import mm_to_px


def enforce(mask_png: Path, cfg: Dict[str, Any], work: Path) -> Path:
    """Thicken fragile areas in the binary mask using a distance transform."""

    dpi = int(cfg["dpi"])
    min_bridge_mm = float(cfg.get("min_bridge_mm", 1.2))
    min_bridge_px = max(1, mm_to_px(min_bridge_mm, dpi))
    radius = max(1, int(round(min_bridge_px / 2)))
    kernel_size = radius * 2 + 1

    mask = cv2.imread(str(mask_png), cv2.IMREAD_GRAYSCALE)
    if mask is None:
        raise FileNotFoundError(f"Mask image not found: {mask_png}")

    binary = (mask > 127).astype(np.uint8)
    dist = cv2.distanceTransform(binary, cv2.DIST_L2, 5)

    # Identify pixels where the bridge is thinner than half the minimum target.
    thin_threshold = max(1.0, min_bridge_px / 2.0)
    thin_regions = (dist < thin_threshold).astype(np.uint8)
    if not thin_regions.any():
        return mask_png

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (kernel_size, kernel_size))

    dilated = cv2.dilate(binary, kernel, iterations=1)
    region_of_interest = cv2.dilate(thin_regions, kernel, iterations=1)
    reinforced = np.where(region_of_interest > 0, dilated, binary)

    out_path = work / "mask_bridge.png"
    Image.fromarray((reinforced * 255).astype(np.uint8)).save(out_path)
    return out_path
