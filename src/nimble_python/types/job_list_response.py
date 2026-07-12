# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobListResponse", "Item", "ItemDestination", "ItemInputs", "ItemSchedule"]


class ItemDestination(BaseModel):
    """Where a job writes its results."""

    path: str
    """Destination path the output is written to."""

    type: Literal["file", "s3"]
    """Destination kind: a local 'file' or an 's3' bucket."""

    format: Optional[Literal["jsonl", "csv", "parquet"]] = None
    """Output file format."""


class ItemInputs(BaseModel):
    """Configuration for the input data a job processes."""

    type: Literal["s3", "inline", "file"]
    """
    How inputs are supplied: an 's3' bucket, 'inline' records, or an uploaded
    'file'.
    """

    data: Optional[List[Dict[str, object]]] = None
    """Inline list of input records. Used when type is 'inline'."""

    file_path: Optional[str] = None
    """Path to the input file; must start with 's3' or 'file\\__'.

    Used for 's3'/'file' types.
    """


class ItemSchedule(BaseModel):
    """Cron-based schedule controlling when a job runs automatically."""

    cron: str
    """Cron expression defining when the job runs."""

    enabled: bool
    """Whether the schedule is currently active."""


class Item(BaseModel):
    """A configured job: an agent plus its schedule, inputs, and destination."""

    id: str
    """Unique job identifier (job\\__<n>)."""

    name: str
    """Job name."""

    agent_name: Optional[str] = None
    """Name of the agent this job runs."""

    created_at: Optional[datetime] = None
    """When the job was created."""

    description: Optional[str] = None
    """Free-text description of the job."""

    destination: Optional[ItemDestination] = None
    """Where a job writes its results."""

    display_name: Optional[str] = None
    """Human-friendly job name shown in the UI."""

    inputs: Optional[ItemInputs] = None
    """Configuration for the input data a job processes."""

    last_run_at: Optional[datetime] = None
    """Timestamp of the most recent run."""

    last_run_status: Optional[Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]] = (
        None
    )
    """Status of the most recent run."""

    schedule: Optional[ItemSchedule] = None
    """Cron-based schedule controlling when a job runs automatically."""

    updated_at: Optional[datetime] = None
    """When the job was last updated."""


class JobListResponse(BaseModel):
    """A page of jobs."""

    items: List[Item]
    """Jobs on this page."""

    page: int
    """Current page number."""

    per_page: int
    """Number of items per page."""

    total: int
    """Total number of jobs matching the query."""
