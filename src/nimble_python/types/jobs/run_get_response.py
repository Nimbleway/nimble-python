# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunGetResponse", "Job", "JobSchedule", "Error", "Summary"]


class JobSchedule(BaseModel):
    cron: str

    enabled: bool


class Job(BaseModel):
    id: str

    name: str

    agent_name: Optional[str] = None

    display_name: Optional[str] = None

    schedule: Optional[JobSchedule] = None


class Error(BaseModel):
    errors_sample: Optional[List[Dict[str, object]]] = None

    message: Optional[str] = None

    step: Optional[str] = None


class Summary(BaseModel):
    input_count: Optional[int] = None

    match_rate: Optional[float] = None

    result_count: Optional[int] = None


class RunGetResponse(BaseModel):
    id: str

    created_at: datetime

    job: Job

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]

    triggered_by: Literal["schedule", "manual"]

    error: Optional[Error] = None

    finished_at: Optional[datetime] = None

    inputs_sample: Optional[List[object]] = None

    started_at: Optional[datetime] = None

    summary: Optional[Summary] = None
