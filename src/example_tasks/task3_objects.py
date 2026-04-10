from pydantic import validate_call
from pydantic import Field


@validate_call
def task3_objects(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    simple_object: dict[str, str],
    object_with_default: dict[str, str] = Field(default_factory=dict),
    nullable_object: dict[str, str] | None,
    nested_object: dict[str, dict[str, int]],
):
    """
    Short description of task3_objects

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        simple_object: Type hint `dict[str, str]`
        object_with_default: Type hint `dict[str, str] = Field(default_factory=dict)`
        nullable_object: Type hint `dict[str, str] | None`
        nested_object: Type hint `dict[str, dict[str, int]]`
    """
    pass
