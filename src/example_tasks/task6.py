
from typing import Literal

from pydantic import BaseModel, ConfigDict
from pydantic import Field
from pydantic import validate_call


class ModelWithCoupledFields(BaseModel):
    """Model demonstrating if/then/else coupled field constraints in JSON schema.

    When field_1 is True, field_1_dependent must be a positive integer (>= 1).
    When field_1 is False, field_1_dependent must be exactly 0.

    Attributes:
        field_1: A boolean toggle controlling the constraint on field_1_dependent.
        field_1_dependent: Dependent on field_1. Must be 0 when field_1 is False,
            and a positive integer when field_1 is True.
    """

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "if": {"properties": {"field_1": {"const": True}}},
            "then": {"properties": {"field_1_dependent": {"minimum": 1}}},
            "else": {"properties": {"field_1_dependent": {"const": 0}}},
        },
    )

    field_1: bool = False
    field_1_dependent: int = Field(
        default=1,
        description="This field is dependent on field_1. "
        "If field_1 is False, this field should be set to 0. "
        "If field_1 is True, this field should be set to a positive integer.",
    )


class ModelWithDependentRequired(BaseModel):
    """Model demonstrating dependentRequired constraints in JSON schema.

    If enable_proxy is present in the object, proxy_url and proxy_port become required.
    Note: dependentRequired triggers when the field key is present, not based on its value.
    Since all fields have defaults, this effectively always requires proxy_url and proxy_port
    when enable_proxy is explicitly set.

    Attributes:
        enable_proxy: Whether to enable the proxy. When set, proxy_url and proxy_port are required.
        proxy_url: The proxy URL. Required when enable_proxy is present.
        proxy_port: The proxy port. Required when enable_proxy is present.
    """

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "dependentRequired": {
                "enable_proxy": ["proxy_url", "proxy_port"],
            }
        },
    )

    enable_proxy: bool = False
    proxy_url: str = Field(default="", description="URL of the proxy server.")
    proxy_port: int = Field(
        default=8080, ge=1, le=65535, description="Port of the proxy server."
    )


class ModelWithMultipleConditions(BaseModel):
    """Model demonstrating multiple independent coupled conditions via allOf in JSON schema.

    Two independent if/then conditions are applied simultaneously:
    - When mode is 'advanced', advanced_config becomes required.
    - When use_cache is True, cache_size must be at least 1.

    Attributes:
        mode: Processing mode. When set to 'advanced', advanced_config is required.
        advanced_config: Configuration string required when mode is 'advanced'.
        use_cache: Whether to enable caching. When True, cache_size must be >= 1.
        cache_size: Size of the cache. Must be >= 1 when use_cache is True.
    """

    model_config = ConfigDict(
        extra="forbid",
        json_schema_extra={
            "allOf": [
                {
                    "if": {"properties": {"mode": {"const": "advanced"}}},
                    "then": {"required": ["advanced_config"]},
                },
                {
                    "if": {"properties": {"use_cache": {"const": True}}},
                    "then": {"properties": {"cache_size": {"minimum": 1}}},
                },
            ]
        },
    )

    mode: Literal["simple", "advanced"] = "simple"
    advanced_config: str = Field(
        default="", description="Required when mode is 'advanced'."
    )
    use_cache: bool = False
    cache_size: int = Field(
        default=0,
        description="Size of the cache in MB. Must be >= 1 when use_cache is True.",
    )


class ModelWithMutuallyExclusiveFields(BaseModel):
    """Model demonstrating mutually exclusive optional fields in JSON schema.

    At most one of output_path or output_url may be provided — setting both is invalid.

    Attributes:
        output_path: Local filesystem path for output. Mutually exclusive with output_url.
        output_url: Remote URL for output. Mutually exclusive with output_path.
    """

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

    output_path: str = Field(
        default="",
        description="Local path for output. Cannot be set together with output_url.",
    )
    output_url: str = Field(
        default="",
        description="Remote URL for output. Cannot be set together with output_path.",
    )


@validate_call
def task6(
    *,
    # Fractal-specific arguments
    zarr_urls: list[str],
    zarr_dir: str,
    # Task-specific arguments
    model_with_coupled_fields: ModelWithCoupledFields = ModelWithCoupledFields(),
    model_with_dependent_required: ModelWithDependentRequired = ModelWithDependentRequired(),
    model_with_multiple_conditions: ModelWithMultipleConditions = ModelWithMultipleConditions(),
    model_with_mutually_exclusive_fields: ModelWithMutuallyExclusiveFields = ModelWithMutuallyExclusiveFields(),
):
    """
    Short description of task6

    Long description of this wonderful task that actually only represents a
    mock task for testing.

    Args:
        zarr_urls: List of input Zarr URLs.
        zarr_dir: Output directory for Zarr data.
        model_with_coupled_fields: if/then/else — field_1_dependent is constrained
            based on the value of field_1.
        model_with_dependent_required: dependentRequired — proxy_url and proxy_port
            become required when enable_proxy is present.
        model_with_multiple_conditions: allOf with multiple if/then — two independent
            coupled conditions applied simultaneously.
        model_with_mutually_exclusive_fields: not + allOf — output_path and output_url
            cannot both be set at the same time.

    """
    pass
