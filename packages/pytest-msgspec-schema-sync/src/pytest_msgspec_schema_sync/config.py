from typing import Literal

from msgspec import Struct

__all__ = ("PluginConfig",)


class PluginConfig(Struct):
    schema_location: Literal["repo_root", "package_root"] = "package_root"
    "Location to store schema files"
    schema_dir: str = "schemas"
    "Name of the directory to store schema files"
    repo_flatten: bool = False
    "Put all schemas in one directory when synced under repo root"
