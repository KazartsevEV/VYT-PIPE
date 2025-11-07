"""Mask generation stub module."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

import cv2
import numpy as np
from PIL import Image

DEFAULT_BLUR_SIGMA = 0.0


def build_mask(src_img: Path, cfg: Dict[str, Any], work: Path) -> Path:
    """Convert the input image to a binary mask using Otsu thresholding."""
    image = cv2.imread(str(src_img))
    if image is None:
        raise FileNotFoundError(f"Unable to read image at {src_img}")
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur_sigma = cfg.get("style", {}).get("blur_sigma", DEFAULT_BLUR_SIGMA)
    if blur_sigma and blur_sigma > 0:
        gray = cv2.GaussianBlur(gray, (0, 0), blur_sigma)
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    if float(np.mean(threshold)) < 127:
        threshold = 255 - threshold
    output_path = work / "mask.png"
    Image.fromarray(threshold).save(output_path)
    return output_path
