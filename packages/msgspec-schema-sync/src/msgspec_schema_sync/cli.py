from argparse import ArgumentParser
from pathlib import Path

from msgspec import Struct
import msgspec

from .sync import sync_schema

__all__ = ("SyncCLI", "run_sync")


class SyncCLI(Struct):
    struct: str
    "Dotted import path to the msgspec struct"
    schema_path: str
    "File path to save the schema at"


parser = ArgumentParser(
    description="Config for syncing msgspec struct schemas to disk.",
)
for field, desc in [
    ("struct", "Dotted import path to the msgspec struct"),
    ("schema_path", "File path to save the schema at"),
]:
    parser.add_argument(f"--{field}", type=str, help=desc)


def run_sync():
    args = parser.parse_args()
    cli_config = msgspec.convert(vars(args), SyncCLI)
    sync_schema(**msgspec.structs.asdict(cli_config))
