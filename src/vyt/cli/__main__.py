"""Typer-based CLI for the VYT-PIPE pipeline."""

from __future__ import annotations

import json
from pathlib import Path

import typer
import yaml
from rich import print

from vyt.core.pipeline import run_pipeline

app = typer.Typer(add_completion=False, help="VYT-PIPE CLI")


@app.command()
def make(config: Path = typer.Argument(..., exists=True, help="YAML config path")) -> None:
    """Запустить полный цикл по одному конфигу."""
    with open(config, "r", encoding="utf-8") as handle:
        cfg = yaml.safe_load(handle)
    result = run_pipeline(cfg)
    print("[green]OK[/] →", json.dumps(result, ensure_ascii=False, indent=2))


@app.command()
def batch(csv_path: Path, limit: int = 0) -> None:
    """Прогон по трекеру CSV (минимальная заглушка)."""
    print(f"Batch runner stub. CSV={csv_path}, limit={limit}")


@app.command()
def qa(id: str) -> None:
    """Показать QA.json по набору (заглушка)."""
    qa_path = Path(f"build/{id}/out/QA.json")
    if qa_path.exists():
        print(qa_path.read_text(encoding="utf-8"))
    else:
        print("QA not found")


@app.command()
def pack(id: str) -> None:
    """Собрать ZIP по готовому набору (заглушка)."""
    print(f"ZIP stub for {id} → TODO")


if __name__ == "__main__":
    app()
