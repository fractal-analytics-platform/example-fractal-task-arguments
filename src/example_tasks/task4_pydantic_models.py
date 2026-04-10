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


@validate_call
def task4_pydantic_models(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    arg_1: SimpleModel,
    arg_2: SimpleModelAllOptional = Field(default_factory=SimpleModelAllOptional),
    tagged_union_1: TaggedUnion,
    tagged_union_2: TaggedUnion = InternalModel3(),
    nested_tagged_union: list[TaggedUnion] = Field(default_factory=list),
):
    """
    Short description of task4_pydantic_models

    Long description of this wonderful task that actually only represents a
    mock task for testing.


    FIXME
    """
    pass
