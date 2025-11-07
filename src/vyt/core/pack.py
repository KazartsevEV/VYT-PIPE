"""ZIP packaging helper."""

from __future__ import annotations

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


def make_zip(out_dir: Path, zip_path: Path) -> Path:
    """Create a ZIP archive with all files under the output directory."""
    with ZipFile(zip_path, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in out_dir.rglob("*"):
            if file_path.is_file():
                archive.write(file_path, arcname=file_path.relative_to(out_dir.parent))
    return zip_path
