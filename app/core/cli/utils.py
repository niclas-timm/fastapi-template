from ctypes import Union
import importlib
from typing import Any, Dict, List
import yaml


def get_config():
    with open('app/config.yml') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return False


def get_command_settings():
    with open('app/config.yml') as stream:
        try:
            cli_commands: List[Dict[str, Any]] = []
            commands = yaml.safe_load(stream).get('commands')
            for command in commands:
                name = command[command.rindex('.')+1:]
                module = importlib.import_module(f"{command}.commands")
                cli_commands.append({
                    "name": name,
                    "app": module
                })
            return cli_commands
        except yaml.YAMLError as exc:
            print(exc)
            return False
