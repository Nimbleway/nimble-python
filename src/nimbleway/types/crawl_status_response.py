# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["CrawlStatusResponse", "Task"]


class Task(BaseModel):
    id: str

    url: str


class CrawlStatusResponse(BaseModel):
    id: str

    account_name: str

    completed: float

    created_at: str

    status: bool

    tasks: List[Task]

    total: float

    completed_at: Optional[str] = None

    name: Optional[str] = None
