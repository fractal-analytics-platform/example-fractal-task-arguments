from typing import Annotated
from pydantic import BaseModel
from pydantic import Json
from pydantic import StringConstraints
from pydantic import NonNegativeFloat
from pydantic import validate_call

NonEmptyStr = Annotated[
    str,
    StringConstraints(
        min_length=1,
        strip_whitespace=True,
    ),
]


class SingleROI(BaseModel):
    FieldIndex: NonEmptyStr
    x_micrometer: float
    y_micrometer: float
    z_micrometer: float
    len_x_micrometer: NonNegativeFloat
    len_y_micrometer: NonNegativeFloat
    len_z_micrometer: NonNegativeFloat


class ROITable(BaseModel):
    # FIXME: By listing columns first, we cannot guarantee that all lists have the same length in a JSON Schema.
    FieldIndex: list[NonEmptyStr]
    x_micrometer: list[float]
    y_micrometer: list[float]
    z_micrometer: list[float]
    len_x_micrometer: list[NonNegativeFloat]
    len_y_micrometer: list[NonNegativeFloat]
    len_z_micrometer: list[NonNegativeFloat]


@validate_call
def task7_json_strings(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    single_roi: Json[SingleROI],
    # full_table: Json[ROITable],
):
    """
    Short description of task4_pydantic_models

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        single_roi: Type hint `Json[SingleROI]`.
        full_table: Type hint `Json[ROITable]`.
    """
    pass
