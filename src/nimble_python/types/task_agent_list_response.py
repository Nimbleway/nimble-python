# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "TaskAgentListResponse",
    "TaskAgentListResponseItem",
    "TaskAgentListResponseItemGoal",
    "TaskAgentListResponseItemSources",
    "TaskAgentListResponseItemSourcesAllow",
    "TaskAgentListResponseItemSourcesBlock",
    "TaskAgentListResponseItemSuggestedQuestion",
]


class TaskAgentListResponseItemGoal(BaseModel):
    id: str

    goal: str

    order: int


class TaskAgentListResponseItemSourcesAllow(BaseModel):
    id: str

    domains: List[str]

    order: int

    title: str


class TaskAgentListResponseItemSourcesBlock(BaseModel):
    """Lenient response shape — domains are plain strings (no re-validation)."""

    domains: List[str]

    order: int

    title: str


class TaskAgentListResponseItemSources(BaseModel):
    """Response variant of AgentSources — preserves per-row id on allow rows."""

    allow: Optional[List[TaskAgentListResponseItemSourcesAllow]] = None

    avoid: Optional[str] = None

    block: Optional[List[TaskAgentListResponseItemSourcesBlock]] = None

    prioritize: Optional[str] = None


class TaskAgentListResponseItemSuggestedQuestion(BaseModel):
    id: str

    order: int

    question: str


class TaskAgentListResponseItem(BaseModel):
    id: str

    created_at: datetime

    description: str

    display_name: str

    domain_expertise: str

    effort: Literal["low", "medium", "high", "x-high", "max"]
    """Canonical effort tier names for the research graph."""

    goals: List[TaskAgentListResponseItemGoal]

    icon: str

    is_active: bool

    output_schema: Optional[Dict[str, object]] = None

    sources: TaskAgentListResponseItemSources
    """Response variant of AgentSources — preserves per-row id on allow rows."""

    suggested_questions: List[TaskAgentListResponseItemSuggestedQuestion]

    updated_at: datetime

    use_case: Literal["research", "enrichment", "dataset_building"]

    account_id: Optional[str] = None

    agent_name: Optional[str] = None

    workspace_id: Optional[str] = None


TaskAgentListResponse: TypeAlias = List[TaskAgentListResponseItem]
