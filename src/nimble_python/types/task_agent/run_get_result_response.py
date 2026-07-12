# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RunGetResultResponse",
    "TaskRunResult",
    "TaskRunResultOutput",
    "TaskRunResultOutputTaskRunTextOutput",
    "TaskRunResultOutputTaskRunTextOutputTrust",
    "TaskRunResultOutputTaskRunTextOutputTrustClaim",
    "TaskRunResultOutputTaskRunTextOutputTrustClaimCitation",
    "TaskRunResultOutputTaskRunTextOutputTrustSource",
    "TaskRunResultOutputTaskRunJsonOutput",
    "TaskRunResultOutputTaskRunJsonOutputTrust",
    "TaskRunResultOutputTaskRunJsonOutputTrustClaim",
    "TaskRunResultOutputTaskRunJsonOutputTrustClaimCitation",
    "TaskRunResultOutputTaskRunJsonOutputTrustSource",
    "TaskRunResultRun",
    "TaskRunResultRunError",
    "TaskRunFailedResult",
    "TaskRunFailedResultError",
    "TaskRunFailedResultRun",
    "TaskRunFailedResultRunError",
]


class TaskRunResultOutputTaskRunTextOutputTrustClaimCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    extract_template_name: Optional[str] = None

    source_category: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_intent: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_type: Optional[Literal["primary", "secondary"]] = None

    title: Optional[str] = None


class TaskRunResultOutputTaskRunTextOutputTrustClaim(BaseModel):
    callout: int

    citations: List[TaskRunResultOutputTaskRunTextOutputTrustClaimCitation]

    confidence: Literal["high", "medium", "low"]

    reasoning: str


class TaskRunResultOutputTaskRunTextOutputTrustSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    source_category: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_intent: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    title: Optional[str] = None


class TaskRunResultOutputTaskRunTextOutputTrust(BaseModel):
    claims: List[TaskRunResultOutputTaskRunTextOutputTrustClaim]

    confidence: Literal["high", "medium", "low"]

    reasoning: str

    sources: List[TaskRunResultOutputTaskRunTextOutputTrustSource]


class TaskRunResultOutputTaskRunTextOutput(BaseModel):
    """Text output from a completed task."""

    content: str
    """The final prose answer."""

    trust: TaskRunResultOutputTaskRunTextOutputTrust

    type: Optional[Literal["text"]] = None


class TaskRunResultOutputTaskRunJsonOutputTrustClaimCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    extract_template_name: Optional[str] = None

    source_category: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_intent: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_type: Optional[Literal["primary", "secondary"]] = None

    title: Optional[str] = None


class TaskRunResultOutputTaskRunJsonOutputTrustClaim(BaseModel):
    citations: List[TaskRunResultOutputTaskRunJsonOutputTrustClaimCitation]

    confidence: Literal["high", "medium", "low"]

    path: str

    reasoning: str


class TaskRunResultOutputTaskRunJsonOutputTrustSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    source_category: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    source_intent: Optional[Literal["official", "news", "social", "academic", "aggregator", "other"]] = None
    """
    What _kind_ of source this is (classified by the compress LLM), independent of
    TrustSourceType (how authoritative it is for a specific claim). Deliberately
    uses "official" rather than "primary" so the two axes can never collide.

    Also doubles as the sub-question's `source_intent` (what kind of source a
    question _needs_) — the two concepts overlap enough that a single enum lets
    `classify_source_importance` compare "what we got" against "what we asked for"
    directly.
    """

    title: Optional[str] = None


class TaskRunResultOutputTaskRunJsonOutputTrust(BaseModel):
    claims: List[TaskRunResultOutputTaskRunJsonOutputTrustClaim]

    confidence: Literal["high", "medium", "low"]

    reasoning: str

    sources: List[TaskRunResultOutputTaskRunJsonOutputTrustSource]


class TaskRunResultOutputTaskRunJsonOutput(BaseModel):
    """
    Structured JSON output from a completed task, produced when task_spec.output_schema.type is 'json'.
    """

    content: Union[Dict[str, object], List[object]]
    """Data conforming to the caller-supplied JSON schema.

    A dict for object schemas; a list for array schemas.
    """

    trust: TaskRunResultOutputTaskRunJsonOutputTrust

    type: Optional[Literal["json"]] = None


TaskRunResultOutput: TypeAlias = Union[TaskRunResultOutputTaskRunTextOutput, TaskRunResultOutputTaskRunJsonOutput]


class TaskRunResultRunError(BaseModel):
    """Error detail for a failed run."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunResultRun(BaseModel):
    """Task run object with status 'completed'."""

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

    error: Optional[TaskRunResultRunError] = None
    """Error detail for a failed run."""

    prompt: Optional[str] = None
    """Original user prompt before enrichment. Populated for Web Search Agent runs."""

    started_at: Optional[datetime] = None

    workspace_id: Optional[str] = None


class TaskRunResult(BaseModel):
    """Response for GET /tasks/runs/{run_id}/result — status 'completed'."""

    output: TaskRunResultOutput
    """Output from the completed task."""

    run: TaskRunResultRun
    """Task run object with status 'completed'."""


class TaskRunFailedResultError(BaseModel):
    """Structured error detail."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultRunError(BaseModel):
    """Error detail for a failed run."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultRun(BaseModel):
    """Task run object with status 'failed'."""

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

    error: Optional[TaskRunFailedResultRunError] = None
    """Error detail for a failed run."""

    prompt: Optional[str] = None
    """Original user prompt before enrichment. Populated for Web Search Agent runs."""

    started_at: Optional[datetime] = None

    workspace_id: Optional[str] = None


class TaskRunFailedResult(BaseModel):
    """Response for GET /tasks/runs/{run_id}/result when the run failed.

    Returned with HTTP 422 so callers can distinguish a failed run from a
    missing one (404) or an active one (408).
    """

    error: TaskRunFailedResultError
    """Structured error detail."""

    run: TaskRunFailedResultRun
    """Task run object with status 'failed'."""


RunGetResultResponse: TypeAlias = Union[TaskRunResult, TaskRunFailedResult]
