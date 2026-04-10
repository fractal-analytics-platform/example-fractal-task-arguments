from enum import Enum
from typing import Literal
from typing import Optional

from pydantic import validate_call, Field


class MyEnum(Enum):
    """
    Description of `MyEnum`.
    """

    name1 = "Value 1"
    """
    Value 1
    """
    name2 = "Value 2"
    """
    Value 2
    """


@validate_call
def task1_scalars(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    int_1: int,
    int_2: int = 1,
    int_3: int | None = None,
    int_4: Optional[int] = None,
    str_1: str,
    str_2: str = "default",
    bool_1: bool = False,
    float_1: float,
    float_2: float = 1.23,
    float_3: float = Field(ge=0.0, le=100.0, default=50.0, multiple_of=5.0),
    enum_1: MyEnum,
    enum_2: MyEnum = MyEnum.name1,
    literal_1: Literal["a", "b", "c"],
    literal_2: Literal["a", "b", "c"] = "a",
):
    """
    Short description of task1_scalars

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        int_1: Type hint `int`
        int_2: Type hint `int = 1`
        int_3: Type hint `int | None = None`
        int_4: Type hint `Optional[int] = None`
        str_1: Type hint `str`
        str_2: Type hint `str = "default"`
        bool_1: Type hint `bool = False`
        float_1: Type hint `float`
        float_2: Type hint `float = 1.23`
        float_3: Type hint `float = Field(ge=0.0, le=100.0, default=50.0, multiple_of=5.0)`
        enum_1: Type hint `MyEnum`
        enum_2: Type hint `MyEnum = MyEnum.name1`
        literal_1: Type hint:` Type hint `Literal["a", "b", "c"]`
        literal_2: Type hint `Literal["a", "b", "c"] = "a"`
    """
    pass
