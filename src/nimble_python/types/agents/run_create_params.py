# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["RunCreateParams", "Sources", "SourcesAllow", "SourcesBlock"]


class RunCreateParams(TypedDict, total=False):
    input: Required[str]
    """User prompt or task instructions for the run."""

    effort: Optional[Literal["low", "medium", "high", "x-high", "max"]]
    """Canonical effort tier names for the research graph."""

    enable_events: bool
    """Whether to stream run events when supported."""

    input_data: Union[Iterable[Dict[str, object]], Dict[str, object], None]
    """
    Existing records to ENRICH: a list of partial rows, or a single object,
    mirroring output_schema's shape.
    """

    output_schema: Optional[Dict[str, object]]
    """JSON schema overriding the agent's default structured output for this run."""

    previous_interaction_id: Optional[str]
    """Previous interaction identifier used to continue a conversation."""

    sources: Optional[Sources]
    """Source guidance overriding the agent default."""


class SourcesAllow(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]
    """Domains included in this source group."""

    title: Required[str]
    """Source group title."""

    order: int
    """Zero-based source group position."""


class SourcesBlock(TypedDict, total=False):
    domains: Required[SequenceNotStr[str]]
    """Domains included in this source group."""

    title: Required[str]
    """Source group title."""

    order: int
    """Zero-based source group position."""


class Sources(TypedDict, total=False):
    """Source guidance overriding the agent default."""

    allow: Iterable[SourcesAllow]
    """Source groups the agent is allowed to use."""

    avoid: Optional[str]
    """Free-text guidance describing sources or domains to avoid."""

    block: Iterable[SourcesBlock]
    """Source groups the agent should not use."""

    prioritize: Optional[str]
    """Free-text guidance describing sources or domains to prioritize."""
