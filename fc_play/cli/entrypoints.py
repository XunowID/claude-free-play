"""FC-Play CLI — commands and entry points for fc-play, fc-server, fc-admin."""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Optional

import typer
from rich.console import Console
from rich.table import Table

from fc_play.config.constants import APP_DISPLAY, APP_TAGLINE

cli = typer.Typer(
    name="fc-play",
    help=f"{APP_DISPLAY} — {APP_TAGLINE}",
    no_args_is_help=True,
    rich_markup_mode="rich",
)
console = Console()

# ─── Banner ────────────────────────────────────────────────────────────────

def _banner():
    console.print(f"""
[bold #f97316]┌────────────────────────────────────────────┐
│         FC-PLAY  v1.0.0                     │
│   Multi-provider model gateway              │
│   Fast. Flexible. Fabulous.                 │
└────────────────────────────────────────────┘[/]""")


# ─── Claude Launcher ───────────────────────────────────────────────────────

def _launch_claude():
    """Launch Claude Code through local proxy."""
    from fc_play.config.settings import get_settings
    settings = get_settings()

    # Check whether proxy server is already running
    import urllib.request
    import urllib.error
    proxy_alive = False
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{settings.port}/health", timeout=2)
        proxy_alive = True
    except Exception:
        proxy_alive = False

    if not proxy_alive:
        console.print("[bold #f97316]✦ Starting proxy server...[/]")
        # Start server in background
        import multiprocessing
        p = multiprocessing.Process(target=_run_server, args=(settings.host, settings.port, settings.log_level), daemon=True)
        p.start()
        import time
        time.sleep(1.5)  # brief wait for startup
        console.print(f"[dim]Proxy running on [bold]{settings.host}:{settings.port}[/][/]")

    # Find claude CLI
    claude_bin = shutil.which("claude")
    if not claude_bin:
        console.print("[red]✖ Claude CLI not found.[/]")
        console.print()
        console.print("  Install it first:")
        console.print("    [bold]macOS / Linux:[/]  npm install -g @anthropic-ai/claude-code")
        console.print("    [bold]Windows:[/]        npm install -g @anthropic-ai/claude-code")
        console.print()
        console.print("  Or download from: https://claude.ai/download")
        raise SystemExit(1)

    console.print(f"[bold #f97316]✦[/] Launching Claude via [bold]fc-play[/] proxy...")
    console.print()

    # Set proxy env
    env = os.environ.copy()
    env["ANTHROPIC_BASE_URL"] = f"http://{settings.host}:{settings.port}"
    if settings.anthropic_api_key:
        env["ANTHROPIC_API_KEY"] = settings.anthropic_api_key

    subprocess.run([claude_bin], env=env, check=False)


def _run_server(host: str, port: int, log_level: str):
    """Start uvicorn server (used by background launch)."""
    import uvicorn
    uvicorn.run("server:app", host=host, port=port,
                log_level=log_level.lower(), timeout_graceful_shutdown=5)


# ─── Commands ──────────────────────────────────────────────────────────────

@cli.command()
def server(
    host: str = typer.Option("0.0.0.0", "--host", help="Bind address"),
    port: int = typer.Option(3010, "--port", "-p", help="Port"),
    env: Optional[Path] = typer.Option(None, "--env", "-e", help=".env path"),
    log_level: str = typer.Option("INFO", "--log-level", "-l"),
    open: bool = typer.Option(False, "--open", "-o", help="Open admin browser"),
):
    """Start the proxy server."""
    _banner()
    if env:
        from dotenv import load_dotenv
        load_dotenv(env)

    if open:
        import webbrowser
        webbrowser.open(f"http://127.0.0.1:{port}/admin")

    import uvicorn
    console.print(f"[dim]Starting server on [bold]{host}:{port}[/][/]")
    uvicorn.run("server:app", host=host, port=port,
                log_level=log_level.lower(), timeout_graceful_shutdown=5)


@cli.command()
def tui(
    theme: str = typer.Option("midnight", "--theme", "-t",
                              help="midnight | emerald | ruby"),
):
    """Launch the terminal dashboard."""
    from fc_play.tui.app import run_tui
    run_tui(theme=theme)


@cli.command()
def admin(
    port: int = typer.Option(3010, "--port", "-p", help="Server port"),
):
    """Open admin UI in browser."""
    import webbrowser
    url = f"http://127.0.0.1:{port}/admin"
    console.print(f"[bold #f97316]✦[/] Admin UI: [bold]{url}[/]")
    webbrowser.open(url)


@cli.command()
def status():
    """Show current configuration status."""
    _banner()
    try:
        from fc_play.config.settings import get_settings
        settings = get_settings()
    except Exception as e:
        console.print(f"[red]Failed: {e}[/]")
        return

    t = Table(show_header=False, box=None, padding=(0, 2))
    t.add_column("Key", style="bold #78716c", no_wrap=True)
    t.add_column("Value", style="#f5f5f4")

    t.add_row("Server", f"{settings.host}:{settings.port}")
    t.add_row("Model", settings.model)
    t.add_row("Opus-tier", settings.model_opus or "—")
    t.add_row("Sonnet-tier", settings.model_sonnet or "—")
    t.add_row("Haiku-tier", settings.model_haiku or "—")

    providers = settings.configured_providers()
    active = [k for k, v in providers.items() if v]
    t.add_row("Active Providers", ", ".join(active) if active else "none")

    t.add_row("Rate Limit", f"{settings.rate_limit_requests}/{settings.rate_limit_window}s")
    t.add_row("Thinking", "Enabled" if settings.enable_thinking else "Disabled")
    t.add_row("Log Level", settings.log_level)
    console.print(t)
    console.print()


@cli.command()
def version():
    """Show version."""
    console.print(f"[bold #f97316]{APP_DISPLAY}[/] v1.0.0")
    console.print(f"[dim]{APP_TAGLINE}[/]")


@cli.callback(invoke_without_command=True)
def main_callback(ctx: typer.Context):
    """FC-Play — Multi-provider model gateway."""
    if ctx.invoked_subcommand is None:
        _launch_claude()


# ─── Entry points for pip-installed scripts ───────────────────────────────

def cli_entry():
    """Entry point for fc-play (launches Claude by default)."""
    cli()


def server_main():
    """Entry point for fc-server — start proxy + open admin."""
    sys.argv = ["fc-server", "server", "--open"]
    cli()


def admin_main():
    """Entry point for fc-admin — open admin UI in browser."""
    sys.argv = ["fc-admin", "admin"]
    cli()


def tui_main():
    """Entry point for fc-play-tui."""
    sys.argv = ["fc-play", "tui"]
    cli()


if __name__ == "__main__":
    cli()
