# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["BatchProgressResponse"]


class BatchProgressResponse(BaseModel):
    """Lightweight batch progress without task details."""

    id: str
    """Unique identifier for the batch."""

    completed: bool
    """Whether all tasks in the batch have finished."""

    completed_count: float
    """Number of tasks that have completed so far."""

    progress: float
    """Completion ratio between 0 and 1."""

    status: Literal["success"]

    completed_at: Optional[str] = None
    """ISO timestamp when the batch completed."""
