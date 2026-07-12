# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TaskAgentRunResponse", "Error"]


class Error(BaseModel):
    """Error detail for a failed run."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskAgentRunResponse(BaseModel):
    """Task run status returned by list/create/get endpoints."""

    id: str
    """Run identifier, format "task*run*{uuid}"."""

    created_at: datetime

    effort: Literal["low", "medium", "high", "x-high", "max"]
    """Canonical effort tier names for the research graph."""

    interaction_id: str
    """Interaction ID — pass as previous_interaction_id to reuse context."""

    is_active: bool
    """True while status is 'queued' or 'running'."""

    status: Literal["queued", "running", "completed", "failed", "cancelled"]
    """
    Lowercase status values used in API responses (distinct from the DB-level
    TaskRunStatus enum).
    """

    web_search_agent_id: str
    """Web Search Agent instance this run belongs to.

    Every task run is agent-bound (see AGENTS-1666). Use this to build the nested
    URL /api/v2/web-search-agents/{web_search_agent_id}/runs/{id}.
    """

    completed_at: Optional[datetime] = None

    error: Optional[Error] = None
    """Error detail for a failed run."""

    prompt: Optional[str] = None
    """Original user prompt before enrichment. Populated for Web Search Agent runs."""

    started_at: Optional[datetime] = None

    workspace_id: Optional[str] = None
