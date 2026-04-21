from pydantic import Json
from pydantic import BaseModel

from pydantic import validate_call


class MyModel(BaseModel):
    """
    Description of `MyModel`

    """

    name: str
    """
    Description of `name`
    """

    x: float
    """
    Description of `x`
    """

    y: float | None = None
    """
    Description of `y`
    """


@validate_call
def task7_json_strings(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    json_arg: Json[MyModel],
):
    """
    Short description of task1_scalars

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        json_arg: Type hint `Json[MyModel]`
    """
    pass
