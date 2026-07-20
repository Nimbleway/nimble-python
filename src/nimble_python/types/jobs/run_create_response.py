# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunCreateResponse"]


class RunCreateResponse(BaseModel):
    """A single execution of a job."""

    id: str
    """Unique run identifier (run\\__<n>)."""

    created_at: datetime
    """When the run was created."""

    job_id: str
    """Identifier of the job this run belongs to."""

    status: Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]
    """Current run status."""

    triggered_by: Literal["schedule", "manual"]
    """What triggered the run: 'schedule' or 'manual'."""

    finished_at: Optional[datetime] = None
    """When the run finished."""

    input_count: Optional[int] = None
    """Number of input records processed."""

    result_count: Optional[int] = None
    """Number of result records produced."""

    started_at: Optional[datetime] = None
    """When the run started executing."""
