"""
Utility functions for the core cli functionality.
"""
import importlib
from typing import Any, Dict, List
import yaml

from app.core import config


def get_cli_settings():
    """ Get cli settings from config.yml"""
    with open(config.CONFIG_YML_PATH, encoding='utf-8') as stream:
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
