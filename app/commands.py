# -------------------------------------------------------------------------------
# A dict of all the typer command apps you want to register in your application.
# Take the default user app (app/core/user/commands.py) as reference when
# implementing new commands.
# -------------------------------------------------------------------------------

from app.core.user import commands as user_commands
cli_apps = [
    {
        "app": user_commands,  # The file the commands live in.
        "name": "user"  # The name you want your commands to be prefixed with. Here: python cli.py user <YOUR_COMMAND>
    }
]
