"""Compatibility shim for legacy imports.

The papercut tooling previously exposed its functionality from
``papercut_panel_builder``.  The project now uses ``make_papercut_panel`` as the
monolithic script entry-point, but we keep this module so older automation that
imports ``papercut_panel_builder`` continues to function without changes.
"""

from __future__ import annotations

from make_papercut_panel import *  # noqa: F401,F403

