# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["JobGetResponse", "Destination", "Inputs", "Schedule"]


class Destination(BaseModel):
    """Where a job writes its results."""

    path: str
    """Destination path the output is written to."""

    type: Literal["file", "s3"]
    """Destination kind: a local 'file' or an 's3' bucket."""

    format: Optional[Literal["jsonl", "csv", "parquet"]] = None
    """Output file format."""


class Inputs(BaseModel):
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

    node_data: Optional[Dict[str, List[Dict[str, object]]]] = None
    """Inline input records keyed by source node id, e.g.

    {'source_a': [{...}]}. Used when type is 'inline' on a dynamic-workflow job,
    which has one source node per input file. Mutually exclusive with 'data'.
    """


class Schedule(BaseModel):
    """Cron-based schedule controlling when a job runs automatically."""

    cron: str
    """Cron expression defining when the job runs."""

    enabled: bool
    """Whether the schedule is currently active."""


class JobGetResponse(BaseModel):
    """A configured job: an agent plus its schedule, inputs, and destination."""

    id: str
    """Unique job identifier (job\\__<n>)."""

    name: str
    """Job name."""

    created_at: Optional[datetime] = None
    """When the job was created."""

    description: Optional[str] = None
    """Free-text description of the job."""

    destination: Optional[Destination] = None
    """Where a job writes its results."""

    display_name: Optional[str] = None
    """Human-friendly job name shown in the UI."""

    extract_template_name: Optional[str] = None
    """Name of the extract template this job runs."""

    inputs: Optional[Inputs] = None
    """Configuration for the input data a job processes."""

    last_run_at: Optional[datetime] = None
    """Timestamp of the most recent run."""

    last_run_status: Optional[Literal["PENDING", "RUNNING", "SUCCESS", "FAILED", "CANCELLED", "TIMEOUT", "WARNING"]] = (
        None
    )
    """Status of the most recent run."""

    schedule: Optional[Schedule] = None
    """Cron-based schedule controlling when a job runs automatically."""

    updated_at: Optional[datetime] = None
    """When the job was last updated."""
