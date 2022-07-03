# -------------------------------------------------------------------------------
# Functionality for discovering all controllers following the configuration
# in the config.yml file.
# -------------------------------------------------------------------------------
import importlib
from typing import Any, List
from fastapi import APIRouter
import yaml

from app.core import config


def discover_controllers_from_config() -> List[Any]:
    """Get all controllers that are registered in config.yml"""
    with open(config.CONFIG_YML_PATH, encoding='utf-8') as stream:
        try:
            yaml_controller_paths = yaml.safe_load(stream).get('controllers')
            if not isinstance(yaml_controller_paths, list) or len(yaml_controller_paths) is 0:
                return []
            modules = []
            for path in yaml_controller_paths:
                module = importlib.import_module(f"{path}.router")
                modules.append(module)
            return modules
        except yaml.YAMLError as exc:
            print(exc)
            return []


def register_all_controllers() -> APIRouter:
    """Register all controllers from config.yml"""
    partial_routers = discover_controllers_from_config()
    router = APIRouter()
    for partial_router in partial_routers:
        router.include_router(partial_router.router)
    return router
