# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "AgentGenerateParams",
    "CreateTemplateGenerationRequestPublicV1",
    "CreateTemplateGenerationRequestPublicV1Metadata",
    "CreateTemplateRefinementRequestPublicV1",
]


class CreateTemplateGenerationRequestPublicV1(TypedDict, total=False):
    prompt: Required[str]

    url: Required[str]

    input_schema: Dict[str, object]

    metadata: Optional[CreateTemplateGenerationRequestPublicV1Metadata]

    name: Optional[str]

    output_schema: Dict[str, object]


class CreateTemplateGenerationRequestPublicV1Metadata(TypedDict, total=False):
    description: Optional[str]

    display_name: Optional[str]

    tags: SequenceNotStr[str]


class CreateTemplateRefinementRequestPublicV1(TypedDict, total=False):
    from_agent: Required[str]

    prompt: Required[str]


AgentGenerateParams: TypeAlias = Union[CreateTemplateGenerationRequestPublicV1, CreateTemplateRefinementRequestPublicV1]
