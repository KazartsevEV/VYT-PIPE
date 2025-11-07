"""Input ingestion helpers."""

from __future__ import annotations

import base64
import mimetypes
from pathlib import Path
from shutil import copy2
from typing import Any, Dict


def copy_sources(cfg: Dict[str, Any], destination: Path) -> Path:
    """Copy or materialize the first configured source image.

    The starter repository ships a text-only ``*.xbase64`` asset to keep the
    history binary-free.  When such a file is encountered we decode it into a
    real image before proceeding with the rest of the pipeline.  Regular image
    paths are copied verbatim.
    """

    source_path = Path(cfg["source"][0])
    destination_path = destination / source_path.name
    destination_path.parent.mkdir(parents=True, exist_ok=True)

    if source_path.suffix == ".xbase64":
        destination_path = _materialize_xbase64(source_path, destination)
    else:
        copy2(source_path, destination_path)

    return destination_path


def _materialize_xbase64(source_path: Path, destination: Path) -> Path:
    """Decode a ``*.xbase64`` text blob into an image file."""

    raw_text = source_path.read_text(encoding="utf-8")
    cleaned = "".join(raw_text.split())
    payload = cleaned
    mime = None

    if cleaned.startswith("data:") and "," in cleaned:
        header, payload = cleaned.split(",", 1)
        mime = header[5:]
        if ";" in mime:
            mime = mime.split(";", 1)[0]

    binary = base64.b64decode(payload)

    # Prefer the stem (before the .xbase64 suffix) as the output file name.
    target = Path(source_path.stem)
    suffix = target.suffix

    if not suffix and mime:
        guessed = mimetypes.guess_extension(mime) or ""
        if guessed == ".jpe":
            guessed = ".jpg"
        suffix = guessed

    if suffix:
        output_name = target.name if target.suffix else f"{target.name}{suffix}"
    else:
        output_name = f"{target.name}.bin"

    output_path = destination / output_name
    output_path.write_bytes(binary)
    return output_path
