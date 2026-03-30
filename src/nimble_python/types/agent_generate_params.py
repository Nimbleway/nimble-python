# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["AgentGenerateParams", "CreateAgentGenerationRequest", "CreateAgentRefinementRequest"]


class CreateAgentGenerationRequest(TypedDict, total=False):
    agent_name: Required[str]

    prompt: Required[str]

    url: Required[str]

    input_schema: object

    metadata: Optional[object]

    output_schema: object


class CreateAgentRefinementRequest(TypedDict, total=False):
    from_agent: Required[str]

    prompt: Required[str]


AgentGenerateParams: TypeAlias = Union[CreateAgentGenerationRequest, CreateAgentRefinementRequest]
