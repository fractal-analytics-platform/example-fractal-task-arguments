from pydantic import validate_call
from pydantic import Field


@validate_call
def task2(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    array: list[int],
    array_with_default: list[int] = Field(default_factory=list),
    array_or_None: list[int] | None,
    array_or_None_with_default: list[int] | None = None,
    my_tuple: tuple[int, int, int],
):
    """
    Short description of task2

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        array: Type hint `list[int]`
        array_with_default: Type hint `list[int] = Field(default_factory=list)`
        array_or_None: Type hint `list[int] | None`
        array_or_None_with_default: Type hint `list[int] | None = None`
        my_tuple: Type hint `tuple[int, int, int]`
    """
    pass
