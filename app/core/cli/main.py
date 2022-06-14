# -------------------------------------------------------------------------------
# Bootstrapping the cli tool. It will register all sub-command files and start
# The app in the "start" method.
# -------------------------------------------------------------------------------
import typer
from app.core.cli.utils import get_command_settings

app = typer.Typer()


def start():
    """Start the typer app."""
    cli_apps = get_command_settings()
    if not cli_apps:
        print("Could not load settings")
        return
    for cli_app in cli_apps:
        """Register all sub command files."""
        app.add_typer(cli_app["app"].app, name=cli_app["name"])
    app()
