# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentRunParams", "Sources", "SourcesAllow", "SourcesBlock"]


class AgentRunParams(TypedDict, total=False):
    input: Required[str]
    """User prompt or task instructions for the run."""

    agent_name: Optional[str]
    """Stable agent name.

    On this no-agent-id route, an unseen name creates a new agent; an existing name
    reuses it. Ignored on the /{agent_id}/runs route.
    """

    effort: Optional[Literal["low", "medium", "high", "x-high", "5x-high", "max"]]
    """Canonical effort tier names for the research graph."""

    enable_events: bool
    """Whether to stream run events when supported."""

    input_data: Union[Iterable[Dict[str, object]], Dict[str, object], None]
    """
    Existing records to ENRICH: a list of partial rows, or a single object,
    mirroring output_schema's shape.
    """

    origin: Literal["api"]
    """Origin of public API runs. Public requests are always API-originated."""

    output_schema: Optional[Dict[str, object]]
    """JSON schema overriding the agent's default structured output for this run."""

    previous_interaction_id: Optional[str]
    """Previous interaction identifier used to continue a conversation."""

    skill: Optional[str]
    """Skill override for this run.

    One-time only, except when this run creates a new agent via agent_name, in which
    case it becomes the new agent's stored skill.
    """

    sources: Optional[Sources]
    """Source guidance overriding the agent default."""

    use_case: Optional[Literal["research", "enrichment", "dataset_building"]]
    """
    Only settable when this run creates a new agent (via agent_name, or when no
    agent is resolved), in which case it becomes the new agent's stored use_case.
    For a run against an existing agent, this must match the agent's own use_case —
    passing the same value is accepted as a no-op, a different value is rejected.
    """


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
