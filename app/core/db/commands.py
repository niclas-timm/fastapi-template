import typer
from app.core.db import db
from app.core import config
import os
import subprocess
from datetime import datetime

OUTPUT_DIR = "dumps"

app = typer.Typer()


@app.command()
def create_db_dump(container_name: str = typer.Option(default=None, help="The name of the postgres container.")):
    """Create a dump of the postgres database.

    Create a SQL dump of the local database and store it in the /dumps directory

    Args:
        container_name (str, optional): The name of the container your postgres database lives in.
    """
    user = config.DB_USERNAME
    database = config.DB_NAME
    if not user or not database:
        typer.echo("No database username or database name provided")
        typer.Abort()
    if not container_name:
        typer.echo("Please provide a container name")
        typer.Abort()
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    file_name = datetime.now().strftime("%Y%m%d_%H%M%S") + ".sql"
    subprocess.call(
        f"docker exec {container_name} pg_dump -U {user} --format=c {database} > {OUTPUT_DIR}/{file_name}", shell=True)


@app.command()
def import_db_dump(container_name: str = typer.Option(default=None, help="The name of the postgres container."),
                   file_name: str = typer.Option(
                       default=None, help="The name of the file that lives in the /dumps directory.")
                   ):
    user = config.DB_USERNAME
    database = config.DB_NAME
    if not user or not database:
        typer.echo("No database username or database name provided")
        typer.Abort()
    if not container_name:
        typer.echo("Please provide a container name")
        typer.Abort()
    if not os.path.isfile(f"{OUTPUT_DIR}/{file_name}"):
        typer.echo("The provided file could not be found.")
        typer.Abort()
    subprocess.call(
        f"docker container exec {container_name} pg_restore --verbose --clean --no-acl --no-owner -U {user} -d {database} /home/{file_name}", shell=True)
