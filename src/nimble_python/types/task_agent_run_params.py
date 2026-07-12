# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["TaskAgentRunParams", "Sources", "SourcesAllow", "SourcesBlock"]


class TaskAgentRunParams(TypedDict, total=False):
    input: Required[str]

    effort: Optional[Literal["low", "medium", "high", "x-high", "max"]]
    """Canonical effort tier names for the research graph."""

    enable_events: bool

    output_schema: Optional[Dict[str, object]]

    previous_interaction_id: Optional[str]

    sources: Optional[Sources]
    """Source preferences for a web search agent instance."""


class SourcesAllow(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]

    title: Required[str]

    order: int


class SourcesBlock(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]

    title: Required[str]

    order: int


class Sources(TypedDict, total=False):
    """Source preferences for a web search agent instance."""

    allow: Iterable[SourcesAllow]

    avoid: Optional[str]

    block: Iterable[SourcesBlock]

    prioritize: Optional[str]
