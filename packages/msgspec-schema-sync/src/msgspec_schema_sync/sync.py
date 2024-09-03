from __future__ import annotations

from json import dumps, loads
from importlib import import_module
from functools import reduce
from pathlib import Path
from typing import TypeAlias, TypeVar

import msgspec
from msgspec import Struct

__all__ = ("import_dotted_path", "write_schema", "sync_schema", "sync_schema_from_path")

T = TypeVar("T", bound=Struct)
ImportString: TypeAlias = str


def import_dotted_path(import_path: str):
    module_name, *subpath = import_path.split(".")
    return reduce(getattr, subpath, import_module(module_name))


def write_schema(struct_schema: dict, schema_path: Path) -> None:
    schema_path.parent.mkdir(exist_ok=True, parents=True)
    schema_json = dumps(struct_schema, indent=2)
    schema_path.write_text(schema_json)
    return


def sync_schema(struct: type[T], schema_path: Path) -> None:
    """
    Synchronize the schema of a msgspec struct to a JSON file on disk.

    Args:
        struct: The msgspec struct.
        schema_path: The path to the existing JSON schema file.
        mjs_kwargs: The kwargs to pass to the `struct_json_schema()` method.
    """
    schema_path = Path(schema_path)
    fresh = msgspec.json.schema(struct)
    if exists := schema_path.exists():
        previous = loads(schema_path.read_text())
    if not exists or previous != fresh:
        write_schema(struct_schema=fresh, schema_path=schema_path)
    return


def sync_schema_from_path(
    struct: ImportString,
    schema_path: str | Path,
) -> None:
    """Trivial wrapper using an ImportString to load the struct class."""
    return sync_schema(struct=import_dotted_path(struct), schema_path=Path(schema_path))
