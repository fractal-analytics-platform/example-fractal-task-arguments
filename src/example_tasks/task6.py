from typing import Literal

from pydantic import BaseModel, ConfigDict
from pydantic import Field
from pydantic import validate_call


class ModelIfThenElse(BaseModel):
    """Model demonstrating if/then/else coupled field constraints."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "if": {
                "properties": {"control_parameter": {"const": True, "type": "boolean"}}
            },
            "then": {
                "properties": {"dependent_parameter": {"minimum": 1, "type": "number"}}
            },
            "else": {
                "properties": {"dependent_parameter": {"const": 0, "type": "number"}}
            },
        },
    )

    control_parameter: bool = False
    """
    A boolean toggle controlling the constraint on `dependent_parameter`.
    """
    dependent_parameter: int = Field(
        default=1,
        description=(
            "Dependent on `control_parameter`. Must be 0 when "
            "control_parameter is False, and a positive integer when "
            "control_parameter is True."
        ),
    )
    """
    An attribute with behavior that depends on `control_parameter`.
    """


class ModelDependentRequired(BaseModel):
    """Model demonstrating dependentRequired constraints."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "dependentRequired": {
                "include_advanced": ["advanced_1", "advanced_2"],
            }
        },
    )

    include_advanced: bool = False
    """
    Whether to include advanced attributes.
    """

    advanced_1: str = "default"
    """
    Advanced 1 description.
    """

    advanced_2: int
    """
    Advanced 1 description.
    """


class ModelWithMultipleIfThen(BaseModel):
    """Model demonstrating multiple independent conditions in allOf"""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "allOf": [
                {
                    "if": {
                        "properties": {"mode": {"const": "advanced", "type": "string"}}
                    },
                    "then": {"required": ["advanced_config"]},
                },
                {
                    "if": {
                        "properties": {"use_cache": {"const": True, "type": "boolean"}}
                    },
                    "then": {
                        "properties": {"cache_size": {"minimum": 1, "type": "number"}}
                    },
                },
            ]
        },
    )

    mode: Literal["simple", "advanced"] = "simple"
    """
    Processing mode. When set to 'advanced', advanced_config is required.
    """
    advanced_config: str
    """
    Configuration string required when mode is 'advanced'.
    """
    use_cache: bool = False
    """
    Determines whether cache_size is required
    """
    cache_size: int = 1
    """
    Size of the cache.
    """


class ModelMutuallyExclusive(BaseModel):
    """Model demonstrating mutually exclusive optional fields in JSON schema."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "not": {
                "allOf": [
                    {"required": ["output_path"]},
                    {"required": ["output_url"]},
                ]
            }
        },
    )

    output_path: str
    """
    Local path for output. Cannot be set together with output_url."
    """

    output_url: str
    """
    Remote URL for output. Cannot be set together with output_path.
    """


@validate_call
def task6(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    arg_if_then_else: ModelIfThenElse,
    # FIXME not supported in fractal-web yet:
    # arg_dependent_required: ModelDependentRequired,
    # arg_multiple_if_then: ModelWithMultipleIfThen,
    # arg_mutually_exclusive: ModelMutuallyExclusive,
):
    """
    Short description of task6

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        zarr_urls: List of input Zarr URLs.
        zarr_dir: Output directory for Zarr data.
        arg_if_then_else: Type hint `ModelIfThenElse`
        arg_dependent_required: Type hint `ModelDependentRequired`
        arg_multiple_if_then: Type hint `ModelWithMultipleIfThen`
        arg_mutually_exclusive: Type hint `ModelMutuallyExclusive`
    """
    pass
