from msgspec_schema_sync import sync_schema_from_path

# This path must be in an installed package
path_to_struct_cls = "msgspec_schema_sync.cli.SyncCLI"
sync_schema_from_path(struct=path_to_struct_cls, schema_path="schema.json")
