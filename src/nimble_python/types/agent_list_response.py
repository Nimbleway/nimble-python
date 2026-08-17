# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "AgentListResponse",
    "Item",
    "ItemGoal",
    "ItemSources",
    "ItemSourcesAllow",
    "ItemSourcesBlock",
    "ItemSuggestedQuestion",
]


class ItemGoal(BaseModel):
    id: str
    """Unique goal identifier (wsag\\__<uuid>)."""

    goal: str
    """Goal text."""

    order: int
    """Zero-based goal position."""


class ItemSourcesAllow(BaseModel):
    id: str
    """Unique source group identifier (wsas\\__<uuid>)."""

    domains: List[str]
    """Domains included in this source group."""

    order: int
    """Zero-based source group position."""

    title: str
    """Source group title."""


class ItemSourcesBlock(BaseModel):
    id: str
    """Unique source group identifier (wsas\\__<uuid>)."""

    domains: List[str]
    """Domains included in this source group."""

    order: int
    """Zero-based source group position."""

    title: str
    """Source group title."""


class ItemSources(BaseModel):
    """Source guidance for the agent."""

    allow: Optional[List[ItemSourcesAllow]] = None
    """Source groups the agent is allowed to use."""

    avoid: Optional[str] = None
    """Free-text guidance describing sources or domains to avoid."""

    block: Optional[List[ItemSourcesBlock]] = None
    """Source groups the agent should not use."""

    prioritize: Optional[str] = None
    """Free-text guidance describing sources or domains to prioritize."""


class ItemSuggestedQuestion(BaseModel):
    id: str
    """Unique suggested question identifier (wsasq\\__<uuid>)."""

    order: int
    """Zero-based suggested question position."""

    question: str
    """Suggested prompt text."""


class Item(BaseModel):
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

    goals: List[ItemGoal]
    """Ordered goals for the agent to follow."""

    icon: str
    """Icon identifier used when presenting the agent."""

    is_active: bool
    """Whether the agent can be used to start new runs."""

    output_schema: Optional[Dict[str, object]] = None
    """JSON schema describing the structured output the agent should produce."""

    skill: str
    """Skill or operating context for the agent."""

    sources: ItemSources
    """Source guidance for the agent."""

    suggested_questions: List[ItemSuggestedQuestion]
    """Suggested prompts users can run with this agent."""

    updated_at: datetime
    """When the agent was last updated."""

    use_case: Literal["research", "enrichment", "dataset_building"]
    """Primary use case supported by the agent."""

    agent_name: Optional[str] = None
    """Stable agent name."""


class AgentListResponse(BaseModel):
    items: List[Item]
    """Items returned in this page."""

    limit: int
    """Maximum number of items returned."""

    offset: int
    """Number of items skipped before this page."""

    total: int
    """Total number of items matching the query."""
