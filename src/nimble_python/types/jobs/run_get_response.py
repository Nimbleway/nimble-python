# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunGetResponse", "Job", "JobSchedule", "Error", "Summary"]


class JobSchedule(BaseModel):
    """Cron-based schedule controlling when a job runs automatically."""

    cron: str
    """Cron expression defining when the job runs."""

    enabled: bool
    """Whether the schedule is currently active."""


class Job(BaseModel):
    """Context of the job this run belongs to."""

    id: str
    """Unique job identifier (job\\__<n>)."""

    name: str
    """Internal job name."""

    display_name: Optional[str] = None
    """Human-friendly job name shown in the UI."""

    extract_template_name: Optional[str] = None
    """Name of the extract template this job runs."""

    schedule: Optional[JobSchedule] = None
    """Cron-based schedule controlling when a job runs automatically."""


class Error(BaseModel):
    """Error details for a failed run."""

    errors_sample: Optional[List[Dict[str, object]]] = None
    """Sample of individual error records from the run."""

    message: Optional[str] = None
    """Human-readable error message."""

    step: Optional[str] = None
    """Pipeline step where the error occurred."""


class Summary(BaseModel):
    """Aggregate metrics for a run."""

    input_count: Optional[int] = None
    """Number of input records processed."""

    match_rate: Optional[float] = None
    """
    Fraction of inputs that produced a result (result_count / input_count), from 0.0
    to 1.0.
    """

    result_count: Optional[int] = None
    """Number of result records produced."""


class RunGetResponse(BaseModel):
    """Full detail for a single run."""

    id: str
    """Unique run identifier (run\\__<n>)."""

    created_at: datetime
    """When the run was created."""

    job: Job
    """Context of the job this run belongs to."""

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]
    """Current run status."""

    triggered_by: Literal["schedule", "manual"]
    """What triggered the run: 'schedule' or 'manual'."""

    error: Optional[Error] = None
    """Error details for a failed run."""

    finished_at: Optional[datetime] = None
    """When the run finished."""

    inputs_sample: Optional[List[object]] = None
    """Sample of the run's input records."""

    started_at: Optional[datetime] = None
    """When the run started executing."""

    summary: Optional[Summary] = None
    """Aggregate metrics for a run."""
