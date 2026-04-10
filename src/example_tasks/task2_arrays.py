from pydantic import validate_call
from pydantic import Field


@validate_call
def task2_arrays(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    simple_array: list[int],
    array_with_empty_default: list[int] = Field(default_factory=list),
    array_with_default: list[int] = Field(default=[1, 2, 3]),
    array_with_constraints: list[int] = Field(
        min_length=2,
        max_length=3,
        json_schema_extra={"uniqueItems": True},
    ),
    nullable_array: list[int] | None,
    nullable_array_with_null_default: list[int] | None = None,
    simple_tuple: tuple[int, int, int],
    tuple_with_default: tuple[int, int, int] = (1, 2, 3),
    non_homogeneous_tuple: tuple[int, float, str],
    nullable_tuple: tuple[int, int, int] | None,
):
    """
    Short description of task2_arrays

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        simple_array: Type hint `list[int]`
        array_with_empty_default: Type hint `list[int] = Field(default_factory=list)`
        array_with_default: Type hint `list[int] = Field(default=[1, 2, 3])`
        array_with_constraints: Type hint `list[int] = Field(min_length=2, max_length=3, json_schema_extra={"uniqueItems": True})`
        nullable_array: Type hint `list[int] | None`
        nullable_array_with_null_default: Type hint `list[int] | None = None`
        simple_tuple: Type hint `tuple[int, int, int]`
        tuple_with_default: Type hint `tuple[int, int, int] = (1, 2, 3)`
        non_homogeneous_tuple: Type hint `tuple[int, float, str]`
        nullable_tuple: Type hint `tuple[int, int, int] | None`
    """
    pass
