# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AgentGenerateParams",
    "CreateAgentGenerationRequest",
    "CreateAgentGenerationRequestMetadata",
    "CreateAgentRefinementRequest",
]


class CreateAgentGenerationRequest(TypedDict, total=False):
    prompt: Required[str]

    url: Required[str]

    input_schema: Dict[str, object]

    metadata: Optional[CreateAgentGenerationRequestMetadata]

    name: Optional[str]

    output_schema: Dict[str, object]


class CreateAgentGenerationRequestMetadata(TypedDict, total=False):
    description: Optional[str]

    display_name: Optional[str]

    tags: SequenceNotStr[str]


class CreateAgentRefinementRequest(TypedDict, total=False):
    from_agent: Required[str]

    prompt: Required[str]


AgentGenerateParams: TypeAlias = Union[CreateAgentGenerationRequest, CreateAgentRefinementRequest]
