# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SerpRunBatchResponse", "Task"]


class Task(BaseModel):
    id: str
    """Unique task identifier."""

    api_query: object = FieldInfo(alias="_query")

    created_at: str
    """Timestamp when the task was created."""

    input: object
    """Original input data for the task."""

    state: Literal["pending", "queued", "in_progress", "success", "error"]
    """Current state of the task."""

    status_url: str
    """URL for checking the task status."""

    account_name: Optional[str] = None
    """Account name that owns the task."""

    api_type: Optional[
        Literal["web", "serp", "ecommerce", "social", "media", "agent", "extract", "fast-serp", "labs"]
    ] = None

    batch_id: Optional[str] = None
    """Batch ID if this task is part of a batch."""

    download_url: Optional[str] = None
    """URL for downloading the task results."""

    error: Optional[str] = None
    """Error message if the task failed."""

    error_type: Optional[str] = None
    """Classification of the error type."""

    modified_at: Optional[str] = None
    """Timestamp when the task was last modified."""

    output_url: Optional[str] = None
    """Storage location of the output data."""

    queue: Optional[str] = None
    """Queue name the task was submitted to."""

    status_code: Optional[float] = None
    """HTTP status code from the task execution."""


class SerpRunBatchResponse(BaseModel):
    """Response when a batch of SERP tasks is created successfully."""

    batch_id: str
    """Unique identifier for the batch."""

    batch_size: float
    """Number of tasks in the batch."""

    tasks: List[Task]
    """List of created tasks."""
