"""FC-Play Terminal UI theme — Midnight, single default."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Theme:
    """Visual theme definition for the terminal UI."""

    name: str

    # Core colors
    primary: str
    primary_dim: str
    accent: str
    background: str
    surface: str
    text: str
    text_dim: str
    text_muted: str

    # Semantic colors
    success: str
    warning: str
    error: str
    info: str

    # Special
    border: str
    highlight: str
    link: str

    # Styles
    header_style: str = field(default="bold")
    title_style: str = field(default="bold")

    def __post_init__(self):
        object.__setattr__(self, "primary_fmt", f"bold {self.primary}")
        object.__setattr__(self, "success_fmt", f"bold {self.success}")
        object.__setattr__(self, "error_fmt", f"bold {self.error}")
        object.__setattr__(self, "warning_fmt", f"bold {self.warning}")
        object.__setattr__(self, "info_fmt", f"bold {self.info}")
        object.__setattr__(self, "dim_fmt", f"dim {self.text_muted}")


MIDNIGHT = Theme(
    name="midnight",
    primary="#6366f1",
    primary_dim="#4f46e5",
    accent="#22c55e",
    background="#0a0a0b",
    surface="#1a1a1e",
    text="#f4f4f5",
    text_dim="#a1a1aa",
    text_muted="#71717a",
    success="#22c55e",
    warning="#f59e0b",
    error="#ef4444",
    info="#3b82f6",
    border="#2a2a2e",
    highlight="#6366f1",
    link="#818cf8",
)

DEFAULT_THEME = MIDNIGHT
