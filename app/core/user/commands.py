import imp
from pydantic import EmailStr
import typer
from app.core.db import db
from .services import crud
from app.core import config
from app.core.user import schema
from app.core.user.services import crud, roles
from app.core.roles import roles as roles_def


app = typer.Typer()


@app.command()
def by_mail(email: str = typer.Option(default=None, help="The email address of the user")):
    session = db.SessionLocal()
    user = crud.get_by_email(session, email)
    if not user:
        typer.echo("User not found")
        raise typer.Abort()
    typer.echo(user.name)


@app.command()
def seed_user():
    """Seed the super user into the database.

    Ideally, this will method will only be called right after the database
    has been set up. Because then the created user will receive the ID 1, which
    will be treated as the super across the app.

    Raises:
        typer.Abort: Not all values are set in environment variables
        typer.Abort: User could not be created.
    """
    session = db.SessionLocal()
    name = config.SUPER_USER_NAME
    email = EmailStr(config.SUPER_USER_EMAIL)
    password = config.SUPER_USER_PASSWORD

    if not name or not email or not password:
        typer.echo("Email, name or password not defined")
        raise typer.Abort()
    new_user_data = schema.UserCreate(email=email, name=name, password=password)
    user = crud.create_user(session, new_user_data)
    if not user:
        typer.echo("Could not create user")
        raise typer.Abort()
    roles.add_roles(db=session, user_id=str(
        user.id), new_roles=[roles_def.Roles.ADMIN.value])
    typer.echo(f"User successfully created with the id {user.id}")
