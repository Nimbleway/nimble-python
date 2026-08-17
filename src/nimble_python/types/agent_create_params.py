# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["AgentCreateParams", "Sources", "SourcesAllow", "SourcesBlock"]


class AgentCreateParams(TypedDict, total=False):
    agent_name: Optional[str]
    """Stable agent name."""

    description: Optional[str]
    """Agent description shown to users."""

    display_name: Optional[str]
    """Human-friendly agent name shown to users."""

    effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"]
    """Default effort level for this agent's runs."""

    goals: SequenceNotStr[str]
    """Ordered goals for the agent to follow."""

    icon: Optional[str]
    """Icon identifier used when presenting the agent."""

    is_active: bool
    """Whether the agent can be used to start new runs."""

    output_schema: Optional[Dict[str, object]]
    """JSON schema describing the structured output the agent should produce."""

    skill: Optional[str]
    """Skill or operating context for the agent."""

    sources: Sources
    """Source guidance for the agent."""

    suggested_questions: SequenceNotStr[str]
    """Suggested prompts users can run with this agent."""

    template: Optional[str]
    """Template name to materialize this instance from.

    When set, the scalar fields and child rows are copied from the template.
    """

    use_case: Optional[Literal["research", "enrichment", "dataset_building"]]
    """Primary use case supported by the agent."""


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
    """Source guidance for the agent."""

    allow: Iterable[SourcesAllow]
    """Source groups the agent is allowed to use."""

    avoid: Optional[str]
    """Free-text guidance describing sources or domains to avoid."""

    block: Iterable[SourcesBlock]
    """Source groups the agent should not use."""

    prioritize: Optional[str]
    """Free-text guidance describing sources or domains to prioritize."""
