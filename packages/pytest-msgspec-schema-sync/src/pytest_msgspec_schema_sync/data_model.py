from msgspec import Struct

__all__ = ("SchemaFieldInfo",)


class SchemaFieldInfo(Struct):
    enum_cls: str
    "Name of the test module enum it came from"
    schema_stem: str
    "Filename stem for the saved JSON schema"
    target: str
    "Dotted import path to the target Pydantic model"
