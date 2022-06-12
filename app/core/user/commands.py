import typer
from app.core.db import db
from .services import crud

app = typer.Typer()


@app.command()
def by_mail(email: str = typer.Option(default=None, help="The email address of the user")):
    session = db.SessionLocal()
    user = crud.get_by_email(session, email)
    if not user:
        typer.echo("User not found")
        raise typer.Abort()
    typer.echo(user.name)
