# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["TemplateListResponse", "Item", "ItemGoal", "ItemSource", "ItemSuggestedQuestion"]


class ItemGoal(BaseModel):
    id: str
    """Unique goal identifier (wsag\\__<uuid>)."""

    goal: str
    """Goal text."""

    order: int
    """Zero-based goal position."""


class ItemSource(BaseModel):
    id: str
    """Unique source group identifier (wsas\\__<uuid>)."""

    domains: List[str]
    """Domains included in this source group."""

    order: int
    """Zero-based source group position."""

    title: str
    """Source group title."""


class ItemSuggestedQuestion(BaseModel):
    id: str
    """Unique suggested question identifier (wsasq\\__<uuid>)."""

    order: int
    """Zero-based suggested question position."""

    question: str
    """Suggested prompt text."""


class Item(BaseModel):
    id: str
    """Unique template identifier (wsat\\__<uuid>)."""

    created_at: datetime
    """When the template was created."""

    description: str
    """Template description shown to users."""

    display_name: str
    """Human-friendly template name shown to users."""

    effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"]
    """Default effort level for runs created from this template."""

    goals: List[ItemGoal]
    """Ordered goals for the template."""

    icon: str
    """Icon identifier used when presenting the template."""

    output_schema: Optional[Dict[str, object]] = None
    """JSON schema describing the structured output the agent should produce."""

    skill: str
    """Skill or operating context for the template."""

    sources: List[ItemSource]
    """Ordered source groups for the template."""

    suggested_questions: List[ItemSuggestedQuestion]
    """Suggested prompts for the template."""

    template_name: str
    """Stable template name used to create agent instances."""

    updated_at: datetime
    """When the template was last updated."""

    use_case: Literal["research", "enrichment", "dataset_building"]
    """Primary use case supported by the template."""


class TemplateListResponse(BaseModel):
    items: List[Item]
    """Items returned in this page."""

    limit: int
    """Maximum number of items returned."""

    offset: int
    """Number of items skipped before this page."""

    total: int
    """Total number of items matching the query."""
