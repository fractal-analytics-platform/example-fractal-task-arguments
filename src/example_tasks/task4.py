from enum import Enum
from typing import Annotated
from typing import Literal

from pydantic import BaseModel
from pydantic import Field
from pydantic import validate_call


class ModelAllOptional(BaseModel):
    """
    Description of `ModelAllOptional`.
    """

    x: int | None = None
    """
    Type hint: `int | None = None`
    """
    y: int = 1
    """
    Type hint: `int = 1`
    """


class ModelSomeRequired(BaseModel):
    """
    Description of `ModelSomeRequired`.
    """

    x: int | None = None
    """
    Type hint: `int | None = None`
    """
    y: str
    """
    Type hint: `str`
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
    field: bool
    """
    Type hint: `bool`
    """



TaggedUnion = Annotated[
    InternalModel1 | InternalModel2 | InternalModel3,
    Field(discriminator="label"),
]


class Model2(BaseModel):
    label: Literal["label2"] = "label2"
    """
    Type hint: `Literal["label2"] = "label2"`
    """
    field2: int
    """
    Type hint: `int`
    """


class Model3(BaseModel):
    label: Literal["label3"] = "label3"
    """
    Type hint: `Literal["label3"] = "label3"`
    """
    field3: str
    """
    Type hint: `str`
    """


class MyEnum(Enum):
    name1 = "Value 1"
    """
    Enum value 1
    """
    name2 = "Value 2"
    """
    Enum value 2
    """


@validate_call
def task4(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    pydantic_1: ModelAllOptional,
    pydantic_2: ModelAllOptional = ModelAllOptional(),
    pydantic_3: ModelAllOptional = Field(default_factory=ModelAllOptional),
    pydantic_4: ModelSomeRequired,
    tagged_union: TaggedUnion = InternalModel1(),
    nested_tagged_union: list[TaggedUnion] = Field(default_factory=list),
):
    """
    Short description of task4

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        pydantic_1: Type hint `ModelAllOptional`
        pydantic_2: Type hint `ModelAllOptional = ModelAllOptional()`
        pydantic_3: Type hint `ModelAllOptional = Field(default_factory=ModelAllOptional)`
        pydantic_4: Type hint `ModelSomeRequired`
        tagged_union: Type hint `TaggedUnion = InternalModel1()`
        nested_tagged_union: Type hint `list[TaggedUnion] = Field(default_factory=list)`
    """
    pass
