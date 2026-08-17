# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RunListResponse", "Item", "ItemError"]


class ItemError(BaseModel):
    """Error details when the run failed."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class Item(BaseModel):
    id: str
    """Run identifier, format "task*run*{uuid}"."""

    created_at: datetime
    """When the run was created."""

    effort: Literal["low", "medium", "high", "x-high", "5x-high", "max"]
    """Effort level used for the run."""

    interaction_id: str
    """Interaction ID."""

    is_active: bool
    """True while status is 'queued' or 'running'."""

    status: Literal["queued", "running", "completed", "failed", "cancelled"]
    """Current run status."""

    web_search_agent_id: str
    """Web Search Agent instance this run belongs to."""

    completed_at: Optional[datetime] = None
    """When the run completed."""

    error: Optional[ItemError] = None
    """Error details when the run failed."""

    prompt: Optional[str] = None
    """Prompt submitted for the run."""

    started_at: Optional[datetime] = None
    """When the run started executing."""


class RunListResponse(BaseModel):
    items: List[Item]
    """Items returned in this page."""

    limit: int
    """Maximum number of items returned."""

    offset: int
    """Number of items skipped before this page."""

    total: int
    """Total number of items matching the query."""
