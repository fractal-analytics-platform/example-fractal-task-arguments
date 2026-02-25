from typing import Annotated
from typing import Literal
from enum import StrEnum

from pydantic import BaseModel
from pydantic import Field
from pydantic import validate_call
from example_tasks.task4 import TaggedUnion

class InternalModel4(BaseModel):
    """
    Description of InternalModel4.


    Attributes:
        label: FIXME, this should be not be here
        field: FIXME, this should be not be here
    """

    label: Literal["label4"] = "label4"
    """
    Type hint: `Literal["label5"] = "label5"`
    """
    field: int = 1
    """
    Type hint: `int = 1`
    """
    
    
NestedTaggedUnion = Annotated[
    TaggedUnion | InternalModel4,
    Field(discriminator="label"),
]

class EnumDropdown(StrEnum):
    """
    Description of `EnumDropdown`
    """
    name1 = "Value 1"
    name2 = "Value 2"
    
    
class NestedModel(BaseModel):
    """
    Description of `NestedModel`.

    Attributes:
        field_1: FIXME, this should be not be here
        field_2: FIXME, this should be not be here
        field_3: FIXME, this should be not be here
        field_4: FIXME, this should be not be here
    """
    field_1: str = "default value"
    """
    Type hint: `str = "default_value"`
    """
    field_2: int = 1
    """
    Type hint: `int = 1`
    """
    field_3: list[NestedTaggedUnion] | None = Field(default=None)
    """
    Type hint: `list[NestedTaggedUnion] | None = Field(default=None)`
    """
    field_4: list[NestedTaggedUnion] = Field(default_factory=list)
    """
    Type hint `list[NestedTaggedUnion] = Field(default_factory=list)`
    """
    
class NotCorrectlyHandled(BaseModel):
    """
    Description of `NotCorrectlyHandled`.

    Attributes:
        field_5: FIXME, this should be not be here
    """
    field_5: InternalModel4 | None = None
    """
    Type hint: `InternalModel4 | None = None`
    """
    

@validate_call
def task5(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    custom_title: str = Field(default="test",title="Custom title 2"),
    regex_arg: str = Field(default="test", pattern=r"^[a-zA-Z0-9_]+$"),
    list_arg: list[int] = Field(min_length=0, max_length=10, json_schema_extra={"uniqueItems": True}, default_factory=lambda: [1, 2, 3]),
    float_arg: float = Field(ge=0.0, le=100.0, default=50.0, multiple_of=5.0),
    nested_tagged_union_arg: NestedTaggedUnion,
    enum_arg: EnumDropdown | None = None,
    literal_arg: Literal["option1", "option2", "option3"] = "option1",
    nested_model_arg: NestedModel = NestedModel(),
    model_or_none: InternalModel4 | None = None,
    string_or_none: str | None = Field(default=None),
    factory_args: list[int] = Field(default_factory=lambda: [1, 2, 3]),
):
    """
    Short description of task5

    Args:
        custom_title: Type hint `str = Field(default="test",title="Custom title 2")`
        regex_arg: Type hint `str = Field(default="test", pattern=r"^[a-zA-Z0-9_]+$")`
        list_arg: Type hint `list[int] = Field(min_length=0, max_length=10, json_schema_extra={"uniqueItems": True}, default_factory=lambda: [1, 2, 3])`
        float_arg: Type hint `float = Field(ge=0.0, le=100.0, default=50.0, multiple_of=5.0)`
        nested_tagged_union_arg: Type hint `NestedTaggedUnion`
        enum_arg: Type hint `EnumDropdown | None = None`
        literal_arg: Type hint `Literal["option1", "option2", "option3"] = "option1"`
        nested_model_arg: Type hint `NestedModel = NestedModel()`
        model_or_none: Type hint `InternalModel4 | None = None`
        string_or_none: Type hint `str | None = Field(default=None)`
        factory_args: Type hint `list[int] = Field(default_factory=lambda: [1, 2, 3])`
    """
    pass
