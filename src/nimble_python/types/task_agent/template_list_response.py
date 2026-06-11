# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "TemplateListResponse",
    "TemplateListResponseItem",
    "TemplateListResponseItemGoal",
    "TemplateListResponseItemSource",
    "TemplateListResponseItemSuggestedQuestion",
]


class TemplateListResponseItemGoal(BaseModel):
    id: str

    goal: str

    order: int


class TemplateListResponseItemSource(BaseModel):
    id: str

    domains: List[str]

    order: int

    title: str


class TemplateListResponseItemSuggestedQuestion(BaseModel):
    id: str

    order: int

    question: str


class TemplateListResponseItem(BaseModel):
    id: str

    created_at: datetime

    description: str

    display_name: str

    domain_expertise: str

    effort: str

    goals: List[TemplateListResponseItemGoal]

    icon: str

    output_schema: Optional[Dict[str, object]] = None

    sources: List[TemplateListResponseItemSource]

    suggested_questions: List[TemplateListResponseItemSuggestedQuestion]

    template_name: str

    updated_at: datetime

    use_case: Literal["research", "enrichment", "dataset_building"]


TemplateListResponse: TypeAlias = List[TemplateListResponseItem]
