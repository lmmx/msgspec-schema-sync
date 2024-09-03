from msgspec import Struct
from msgspec_schema_sync import sync_schema


class FooStruct(Struct):
    foo: int = 1


sync_schema(struct=FooStruct, schema_path="FooStruct.json")
