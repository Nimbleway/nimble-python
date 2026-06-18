# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobRunResponse"]


class JobRunResponse(BaseModel):
    id: str

    created_at: datetime

    job_id: str

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]

    triggered_by: Literal["schedule", "manual"]

    finished_at: Optional[datetime] = None

    input_count: Optional[int] = None

    result_count: Optional[int] = None

    started_at: Optional[datetime] = None
