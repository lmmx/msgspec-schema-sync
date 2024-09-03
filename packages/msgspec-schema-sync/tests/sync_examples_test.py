from pathlib import Path

from pytest import fixture, importorskip, mark


def remove_if_exists(file_paths: list[Path]) -> None:
    assert all(isinstance(p, Path) for p in file_paths)
    for path in file_paths:
        path.unlink(missing_ok=True)


def assert_files_exist(file_paths: list[Path]) -> None:
    assert all(isinstance(p, Path) and p.exists() and p.is_file() for p in file_paths)


@fixture(autouse=True)
def cleanup(request):
    """Pre- and post-test cleanup of the files to be checked."""
    artifacts = request.node.callspec.params["files_to_check"]
    remove_if_exists(artifacts)
    yield
    remove_if_exists(artifacts)


@mark.parametrize(
    "module_to_import, files_to_check",
    [
        ("examples.sync_struct", [Path("FooStruct.json")]),
        ("examples.sync_struct_from_path", [Path("schema.json")]),
        ("examples.sync_struct_cli", [Path("schema.json")]),
    ],
)
def test_sync(module_to_import, files_to_check):
    importorskip(module_to_import)
    assert_files_exist(files_to_check)
