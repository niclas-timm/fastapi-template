# -------------------------------------------------------------------------------
# Shell commands to execute commands on a remove server via ssh.
# -------------------------------------------------------------------------------
from paramiko import SSHClient
import typer

from app.core.ssh import utils

app = typer.Typer()
client = SSHClient()


@app.command()
def exec(
        env: str,
        command: str = typer.Option(
            default=None, help="The command you want to execute on the remote system."),
        dir: str = typer.Option(
        default=None, help="The directory on the server the command will be executed in. If not specified, the directory from config.yml will be used.")
):
    """Execute command on a remote server via ssh.

    The configuration for executing a command on a remove server must be made in app/config/config.yml.
    Args:
        env (str): An environemt as specified in the ssh section of config.yml
        command (str, optional): The command that will be executed on the remote servier.
    """
    if command is None:
        typer.echo("Please provide a command to execute.")
        raise typer.Abort()
    if env is None:
        typer.echo("Please select an environment.")
        raise typer.Abort()
    full_config = utils.get_ssh_config()
    if not full_config:
        typer.echo("Configuration not set.")
        raise typer.Abort()
    config = full_config.get('ssh')
    if not config:
        typer.echo('No ssh configuration provided')
        raise typer.Abort()
    client.load_system_host_keys()
    for key in config:
        values = config.get(key)
        if key != env:
            continue
        client.connect(values.get('host'),
                       username=values.get('user'))
        execution_dir = dir or values.get('dir')
        stdin, stdout, stderr = client.exec_command(
            f"cd {execution_dir} && {command}")
        if stderr.readlines():
            for err_line in stderr.readlines():
                print(err_line)
                client.close()
                typer.Abort()
        for std_out in stdout.readlines():
            print(std_out)
        break
    client.close()
