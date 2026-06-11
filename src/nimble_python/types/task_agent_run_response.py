# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskAgentRunResponse", "Error"]


class Error(BaseModel):
    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskAgentRunResponse(BaseModel):
    id: str
    """Run identifier."""

    created_at: datetime

    effort: Literal["quickest", "quick", "research", "pro", "max"]

    interaction_id: str
    """Interaction ID — pass as previous_interaction_id to reuse context."""

    is_active: bool
    """True while status is 'queued' or 'running'."""

    status: Literal["queued", "running", "completed", "failed", "cancelled"]

    completed_at: Optional[datetime] = None

    error: Optional[Error] = None

    prompt: Optional[str] = None

    started_at: Optional[datetime] = None

    web_search_agent_id: Optional[str] = None
    """Web Search Agent instance this run belongs to."""

    workspace_id: Optional[str] = None
