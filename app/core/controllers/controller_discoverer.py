import importlib
from typing import Any, List
from fastapi import APIRouter
import yaml

from app.core import config


def discover() -> List[Any]:
    with open(config.CONFIG_YML_PATH) as stream:
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


def get_partial_routers() -> APIRouter:
    partial_routers = discover()
    router = APIRouter()
    for partial_router in partial_routers:
        router.include_router(partial_router.router)
    return router
