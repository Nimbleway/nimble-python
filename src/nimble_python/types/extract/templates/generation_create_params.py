# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "GenerationCreateParams",
    "CreateExtractTemplateGenerationRequestPublicV2",
    "CreateExtractTemplateGenerationRequestPublicV2Metadata",
    "CreateExtractTemplateRefinementRequestPublicV2",
]


class CreateExtractTemplateGenerationRequestPublicV2(TypedDict, total=False):
    prompt: Required[str]
    """Instructions for generating the extract template."""

    url: Required[str]
    """Example URL used to generate the extract template."""

    input_schema: Dict[str, object]
    """Optional JSON schema describing expected input parameters."""

    metadata: Optional[CreateExtractTemplateGenerationRequestPublicV2Metadata]
    """Metadata to attach to the generated extract template."""

    name: Optional[str]
    """Optional stable name for the generated extract template."""

    output_schema: Dict[str, object]
    """Optional JSON schema describing desired extracted output."""


class CreateExtractTemplateGenerationRequestPublicV2Metadata(TypedDict, total=False):
    """Metadata to attach to the generated extract template."""

    description: Optional[str]
    """Description for the generated template."""

    display_name: Optional[str]
    """Human-friendly display name for the generated template."""

    tags: SequenceNotStr[str]
    """Tags to associate with the generated template."""


class CreateExtractTemplateRefinementRequestPublicV2(TypedDict, total=False):
    from_extract_template: Required[str]
    """Name of the source extract template to refine."""

    prompt: Required[str]
    """Instructions for refining the extract template."""


GenerationCreateParams: TypeAlias = Union[
    CreateExtractTemplateGenerationRequestPublicV2, CreateExtractTemplateRefinementRequestPublicV2
]
