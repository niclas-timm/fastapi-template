from paramiko import SSHClient
import typer

from app.core.cli import utils as cli_utils

app = typer.Typer()
client = SSHClient()


@app.command()
def exec(env, command: str = typer.Option(default=None, help="The command you want to execute on the remote system.")):
    if command is None:
        print("Please provide a command to execute.")
        typer.Abort()
    if env is None:
        print("Please select an environment.")
        typer.Abort()
    full_config = cli_utils.get_config()
    if not full_config:
        print("Configuration not set.")
        typer.Abort()
        return
    config = full_config.get('ssh')
    client.load_system_host_keys()
    for key in config:
        values = config.get(key)
        if key != env:
            continue
        client.connect(values.get('host'),
                       username=values.get('user'))
        stdin, stdout, stderr = client.exec_command(
            f"cd {values.get('dir')} && {command}")
        if stderr.readlines():
            for err_line in stderr.readlines():
                print(err_line)
                client.close()
                typer.Abort()
        for std_out in stdout.readlines():
            print(std_out)
        break
    client.close()
