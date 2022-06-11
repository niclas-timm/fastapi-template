import typer
from app.core.db import db
from .services import crud

app = typer.Typer()


@app.command()
def by_mail(email: str):
    session = db.SessionLocal()
    user = crud.get_by_email(session, email)
    if not user:
        typer.echo("User not found")
        raise typer.Abort()
    typer.echo(user.name)
