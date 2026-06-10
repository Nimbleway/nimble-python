# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["AgentGetResponse", "FeatureFlags", "InputProperty"]


class FeatureFlags(BaseModel):
    is_localization_supported: Optional[bool] = None

    is_pagination_supported: Optional[bool] = None


class InputProperty(BaseModel):
    default: Union[str, bool, float, None] = None

    description: Optional[str] = None

    examples: Optional[List[object]] = None

    is_localization_param: Optional[bool] = None

    is_pagination_param: Optional[bool] = None

    name: Optional[str] = None

    required: Optional[bool] = None

    rules: Optional[List[str]] = None

    type: Optional[str] = None


class AgentGetResponse(BaseModel):
    display_name: str

    is_public: bool

    name: str

    description: Optional[str] = None

    domain: Optional[str] = None

    entity_type: Optional[str] = None

    feature_flags: Optional[FeatureFlags] = None

    input_properties: Optional[List[InputProperty]] = None

    managed_by: Optional[str] = None

    output_schema: Optional[Dict[str, object]] = None

    vertical: Optional[str] = None
