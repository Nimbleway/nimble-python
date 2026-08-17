# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentGetResponse", "Goal", "Sources", "SourcesAllow", "SourcesBlock", "SuggestedQuestion"]


class Goal(BaseModel):
    id: str
    """Unique goal identifier (wsag\\__<uuid>)."""

    goal: str
    """Goal text."""

    order: int
    """Zero-based goal position."""


class SourcesAllow(BaseModel):
    id: str
    """Unique source group identifier (wsas\\__<uuid>)."""

    domains: List[str]
    """Domains included in this source group."""

    order: int
    """Zero-based source group position."""

    title: str
    """Source group title."""


class SourcesBlock(BaseModel):
    id: str
    """Unique source group identifier (wsas\\__<uuid>)."""

    domains: List[str]
    """Domains included in this source group."""

    order: int
    """Zero-based source group position."""

    title: str
    """Source group title."""


class Sources(BaseModel):
    """Source guidance for the agent."""

    allow: Optional[List[SourcesAllow]] = None
    """Source groups the agent is allowed to use."""

    avoid: Optional[str] = None
    """Free-text guidance describing sources or domains to avoid."""

    block: Optional[List[SourcesBlock]] = None
    """Source groups the agent should not use."""

    prioritize: Optional[str] = None
    """Free-text guidance describing sources or domains to prioritize."""


class SuggestedQuestion(BaseModel):
    id: str
    """Unique suggested question identifier (wsasq\\__<uuid>)."""

    order: int
    """Zero-based suggested question position."""

    question: str
    """Suggested prompt text."""


class AgentGetResponse(BaseModel):
    id: str
    """Unique web search agent identifier (wsa\\__<uuid>)."""

    created_at: datetime
    """When the agent was created."""

    description: str
    """Agent description shown to users."""

    display_name: str
    """Human-friendly agent name shown to users."""

    effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"]
    """Default effort level for this agent's runs."""

    goals: List[Goal]
    """Ordered goals for the agent to follow."""

    icon: str
    """Icon identifier used when presenting the agent."""

    is_active: bool
    """Whether the agent can be used to start new runs."""

    output_schema: Optional[Dict[str, object]] = None
    """JSON schema describing the structured output the agent should produce."""

    skill: str
    """Skill or operating context for the agent."""

    sources: Sources
    """Source guidance for the agent."""

    suggested_questions: List[SuggestedQuestion]
    """Suggested prompts users can run with this agent."""

    updated_at: datetime
    """When the agent was last updated."""

    use_case: Literal["research", "enrichment", "dataset_building"]
    """Primary use case supported by the agent."""

    agent_name: Optional[str] = None
    """Stable agent name."""
