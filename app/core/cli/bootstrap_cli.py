"""
Bootstrapping the cli tool. It will register all sub-command files and start
The app in the "start" method.
"""
import typer
from app.core.cli.utils import get_cli_settings

app = typer.Typer()


def bootstrap_cli():
    """Start the typer app."""
    cli_apps = get_cli_settings()
    if not cli_apps:
        print("Could not load settings")
        return
    # Register all sub command files
    for cli_app in cli_apps:
        app.add_typer(cli_app["app"].app, name=cli_app["name"])
    app()
