# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: datetime

    job_id: str

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]

    triggered_by: Literal["schedule", "manual"]

    finished_at: Optional[datetime] = None

    input_count: Optional[int] = None

    result_count: Optional[int] = None

    started_at: Optional[datetime] = None


class RunListResponse(BaseModel):
    items: List[Item]

    page: int

    per_page: int

    total: int
