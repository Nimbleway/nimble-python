# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskAgentCreateResponse", "Goal", "Sources", "SourcesAllow", "SourcesBlock", "SuggestedQuestion"]


class Goal(BaseModel):
    id: str

    goal: str

    order: int


class SourcesAllow(BaseModel):
    id: str

    domains: List[str]

    order: int

    title: str


class SourcesBlock(BaseModel):
    """Lenient response shape — domains are plain strings (no re-validation)."""

    domains: List[str]

    order: int

    title: str


class Sources(BaseModel):
    """Response variant of AgentSources — preserves per-row id on allow rows."""

    allow: Optional[List[SourcesAllow]] = None

    avoid: Optional[str] = None

    block: Optional[List[SourcesBlock]] = None

    prioritize: Optional[str] = None


class SuggestedQuestion(BaseModel):
    id: str

    order: int

    question: str


class TaskAgentCreateResponse(BaseModel):
    id: str

    created_at: datetime

    description: str

    display_name: str

    domain_expertise: str

    effort: Literal["low", "medium", "high", "x-high", "max"]
    """Canonical effort tier names for the research graph."""

    goals: List[Goal]

    icon: str

    is_active: bool

    output_schema: Optional[Dict[str, object]] = None

    sources: Sources
    """Response variant of AgentSources — preserves per-row id on allow rows."""

    suggested_questions: List[SuggestedQuestion]

    updated_at: datetime

    use_case: Literal["research", "enrichment", "dataset_building"]

    account_id: Optional[str] = None

    agent_name: Optional[str] = None

    workspace_id: Optional[str] = None
