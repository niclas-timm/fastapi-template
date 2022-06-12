import typer
from app.commands import cli_apps

app = typer.Typer()

for cli_app in cli_apps:
    app.add_typer(cli_app["app"].app, name=cli_app["name"])


def start():
    app()
