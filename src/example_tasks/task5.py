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
        label: FIXME
        field:
    """

    label: Literal["label4"] = "label4"
    field: int = 1
    
    
NestedTaggedUnion = Annotated[
    TaggedUnion | InternalModel4,
    Field(discriminator="label"),
]

class EnumDropdown(StrEnum):
    name1 = "Value 1"
    name2 = "Value 2"
    
    
class NestedModel(BaseModel):
    """Description of NestedModel.
    
    Attributes:
        field_1: xxx
        field_2: yyy
        field_3: list of pydantic models union with none. When the list is empty the field will be set to none.
        field_4: same as field_3 but with default value set to an empty list instead of none.
        field_5: optional pydantic model.
    """
    field_1: str = "default value"
    field_2: int = 1
    field_3: list[NestedTaggedUnion] | None = Field(default=None)
    field_4: list[NestedTaggedUnion] = Field(default_factory=list)
    
class NotCorrectlyHandled(BaseModel):
    # Field 5 is currently not correctly handled by the UI as there is no
    # way to set it to None
    field_5: InternalModel4 | None = None   
    

@validate_call
def task5(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    custom_title: str = Field(default="test",title="Custom title"),
    regex_arg: str = Field(default="test", pattern=r"^[a-zA-Z0-9_]+$"),
    list_arg: list[int] = Field(min_length=0, max_length=10, json_schema_extra={"uniqueItems": True}, default_factory=lambda: [1, 2, 3]),
    float_arg: float = Field(ge=0.0, le=100.0, default=50.0, multiple_of=5.0),
    nested_tagged_union_arg: NestedTaggedUnion,
    enum_arg: EnumDropdown | None = None,
    literal_arg: Literal["option1", "option2", "option3"] = "option1",
    nested_model_arg: NestedModel = NestedModel(),
    # model_or_none is currently not correctly handled by the UI
    # It can not be set to None but only to an instance of InternalModel4
    model_or_none: InternalModel4 | None = None,
    # This field is not support by the build tooling 
    # It will fail with the following erorr:
    # ValueError: Non-None default not supported, but parameter 'string_or_none' 
    # has type hint 'str | None' and default annotation=NoneType required=False default=None.
    # 
    # string_or_none: str | None = Field(default=None)
    #
    # default factories are not evaluated during the build process
    factory_args: list[int] = Field(default_factory=lambda: [1, 2, 3]),
    # Wish list: support for markdown some markdown rendering in the description of the task
    # and allow Field(description="Some **markdown** description") to override the 
    # default doc string description of the argument in the UI.
    # No need to support the full markdown syntax, just basic formatting like **bold**, *italic* and bullet points would be great.
    # markdown_description_arg: str = Field(default="test", description="This is a **markdown** description")
):
    """
    Short description of task5

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        custom_title: example of a way to add a custom title to the schema of an argument.
        regex_arg: example of a way to add a regex pattern to the schema of an argument.
        list_arg: example of a way to add a list with minimum and maximum length constraints to the schema of an argument.
        float_arg: example of a way to add a float with minimum and maximum value constraints to the schema of an argument.
        nested_tagged_union_arg: example of a way to add a nested tagged union argument (usefull to extend tagged unions defined in other tasks).
        enum_arg: menu argument using StrEnum, which will be rendered as a dropdown in the UI.
        literal_arg: menu argument using Literal, which will be rendered as a dropdown in the UI.
        nested_model_arg: example of a way to add a nested Pydantic model as an argument.
        model_or_none: example of a field that is currently not correctly handled by the UI.
        factory_args: example of a field with a default factory, which is not evaluated during the build process.
        
    """
    pass
