# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskAgentCreateParams", "Source"]


class TaskAgentCreateParams(TypedDict, total=False):
    agent_name: Optional[str]

    description: Optional[str]

    display_name: Optional[str]

    domain_expertise: Optional[str]

    effort: str

    goals: SequenceNotStr[str]

    icon: Optional[str]

    is_active: bool

    output_schema: Optional[Dict[str, object]]

    sources: Iterable[Source]

    suggested_questions: SequenceNotStr[str]

    template: Optional[str]
    """Template name to materialise this instance from.

    When set, scalar fields and child rows are copied from the template.
    """

    use_case: Optional[Literal["research", "enrichment", "dataset_building"]]

    workspace_id: Optional[str]


class Source(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]

    title: Required[str]

    order: int
