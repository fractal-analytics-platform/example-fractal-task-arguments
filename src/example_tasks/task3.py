from pydantic import validate_call


@validate_call
def task3(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    object_arg: dict[int, int],
    optional_object_arg: dict[str, int] | None = None,
    nested_object_arg: dict[str, dict[str, int]],
):
    """
    Short description of task3

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        object_arg: Type hint `dict[int, int]`
        optional_object_arg: Type hint `dict[int, int] | None = None`
        nested_object_arg: Type hint `dict[str, dict[str, int]]`
    """
    pass
