from typing import Annotated
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validate_call


class SimpleModelAllOptional(BaseModel):
    """
    Description of `SimpleModelAllOptional`.
    """

    x: int | None = None
    """
    Type hint: `int | None = None`
    """
    y: int = 1
    """
    Type hint: `int = 1`
    """


class SimpleModel(SimpleModelAllOptional):
    """
    Description of `SimpleModel`.
    """

    z: int
    """
    Type hint: `int`
    """


class InternalModel1(BaseModel):
    """
    Description of `InternalModel1`.
    """

    label: Literal["label1"] = "label1"
    """
    Type hint: `Literal["label1"] = "label1"`
    """
    field: int = 1
    """
    Type hint: `int = 1`
    """


class InternalModel2(BaseModel):
    """
    Description of `InternalModel2`.
    """

    label: Literal["label2"] = "label2"
    """
    Type hint: `Literal["label2"] = "label2"`
    """
    field: str
    """
    Type hint: `str`
    """


class InternalModel3(BaseModel):
    """
    Description of `InternalModel3`.
    """

    label: Literal["label3"] = "label3"
    """
    Type hint: `Literal["label3"] = "label3"`
    """
    field: bool = False
    """
    Type hint: `bool = False`
    """


TaggedUnion = Annotated[
    InternalModel1 | InternalModel2 | InternalModel3,
    Field(discriminator="label"),
]


class NestedModel(BaseModel):
    """
    Description of `NestedModel`
    """

    tagged_union_attribute: TaggedUnion
    """
    Type hint `tagged_union_attribute: TaggedUnion`
    """

    list_of_models: list[SimpleModel]
    """
    Type hint `list_of_models: list[SimpleModel]`
    """


@validate_call
def task4_pydantic_models(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    simple_arg_1: SimpleModel,
    simple_arg_2: SimpleModelAllOptional,
    nullable_arg: SimpleModel | None,
    nullable_arg_with_null_default: SimpleModel | None = None,
    tagged_union: TaggedUnion,
    tagged_union_with_default: TaggedUnion = InternalModel3(),
    nested_tagged_union: list[TaggedUnion] = Field(default_factory=list),
    nested_model: NestedModel,
):
    """
    Short description of task4_pydantic_models

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        simple_arg_1: Type hint `SimpleModel`
        simple_arg_2: Type hint `SimpleModelAllOptional`
        nullable_arg: Type hint `SimpleModel | None`
        nullable_arg_with_null_default: Type hint `SimpleModel | None = None`
        tagged_union: Type hint `TaggedUnion`
        tagged_union_with_default: Type hint `TaggedUnion = InternalModel3()`
        nested_tagged_union: Type hint `list[TaggedUnion] = Field(default_factory=list)`
        nested_model: Type hint `NestedModel`
    """
    pass
