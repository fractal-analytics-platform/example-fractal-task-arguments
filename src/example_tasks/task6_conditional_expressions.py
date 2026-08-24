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
            "if": {
                "properties": {
                    "advanced_path": {
                        "type": "string"
                    }
                }
            },
            "then": {
                "properties": {
                    "advanced_1": {
                        "type": "string"
                    },
                    "advanced_2": {
                        "type": "integer"
                    }
                }
            }
        },
    )

    advanced_path: str | None = None
    """
    When included, advanced attributes must be set.
    """

    advanced_1: str | None = "default"
    """
    Advanced 1 description.
    """

    advanced_2: int | None = None
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
                    "then": {
                        "properties": {"advanced_config": {"type": "string"}},
                        "required": ["advanced_config"],
                    },
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
    advanced_config: str | None = None
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


def _get_jschema_extra_mutually_exclusive(
    *,
    name1: str,
    name2: str,
    type1: str,
    type2: str,
) -> dict:
    return {
        "not": {
            "allOf": [
                {"properties": {name1: {"type": type1}}, "required": [name1]},
                {"properties": {name2: {"type": type2}}, "required": [name2]},
            ]
        }
    }


class ModelMutuallyExclusive(BaseModel):
    """Model demonstrating mutually exclusive optional fields in JSON schema."""

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra=_get_jschema_extra_mutually_exclusive(
            name1="output_path",
            name2="output_url",
            type1="string",
            type2="string",
        ),
    )

    output_path: str | None = None
    """
    Local path for output. Cannot be set together with output_url."
    """

    output_url: str | None = None
    """
    Remote URL for output. Cannot be set together with output_path.
    """


@validate_call
def task6_conditional_expressions(
    *,
    # Fractal-specific arguments
    zarr_url: str,
    # Task-specific arguments
    arg_if_then_else: ModelIfThenElse,
    arg_dependent_required: ModelDependentRequired,
    arg_multiple_if_then: ModelWithMultipleIfThen,
    arg_mutually_exclusive: ModelMutuallyExclusive,
):
    """
    Short description of task6_conditional_expressions

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
