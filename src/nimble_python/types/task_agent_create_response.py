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
    domains: List[str]

    title: str

    order: Optional[int] = None


class Sources(BaseModel):
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

    effort: str

    goals: List[Goal]

    icon: str

    is_active: bool

    output_schema: Optional[Dict[str, object]] = None

    sources: Sources

    suggested_questions: List[SuggestedQuestion]

    updated_at: datetime

    use_case: Literal["research", "enrichment", "dataset_building"]

    account_id: Optional[str] = None

    agent_name: Optional[str] = None

    workspace_id: Optional[str] = None

    workspace_name: Optional[str] = None
