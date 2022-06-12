# -------------------------------------------------------------------------------
# Bootstrapping the cli tool. It will register all sub-command files and start
# The app in the "start" method.
# -------------------------------------------------------------------------------
import typer
from app.commands import cli_apps

app = typer.Typer()

for cli_app in cli_apps:
    """Register all sub command files."""
    app.add_typer(cli_app["app"].app, name=cli_app["name"])


def start():
    """Start the typer app."""
    app()
