# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "TaskAgentListResponse",
    "TaskAgentListResponseItem",
    "TaskAgentListResponseItemGoal",
    "TaskAgentListResponseItemSource",
    "TaskAgentListResponseItemSuggestedQuestion",
]


class TaskAgentListResponseItemGoal(BaseModel):
    id: str

    goal: str

    order: int


class TaskAgentListResponseItemSource(BaseModel):
    id: str

    domains: List[str]

    order: int

    title: str


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

    effort: str

    goals: List[TaskAgentListResponseItemGoal]

    icon: str

    is_active: bool

    output_schema: Optional[Dict[str, object]] = None

    sources: List[TaskAgentListResponseItemSource]

    suggested_questions: List[TaskAgentListResponseItemSuggestedQuestion]

    updated_at: datetime

    use_case: Literal["research", "enrichment", "dataset_building"]

    account_id: Optional[str] = None

    agent_name: Optional[str] = None

    workspace_id: Optional[str] = None

    workspace_name: Optional[str] = None


TaskAgentListResponse: TypeAlias = List[TaskAgentListResponseItem]
