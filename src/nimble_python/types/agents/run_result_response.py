# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RunResultResponse",
    "TaskRunResultPublicV2",
    "TaskRunResultPublicV2Output",
    "TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2",
    "TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2Trust",
    "TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaim",
    "TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaimCitation",
    "TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustSource",
    "TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2",
    "TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2Trust",
    "TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaim",
    "TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaimCitation",
    "TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustSource",
    "TaskRunResultPublicV2Run",
    "TaskRunResultPublicV2RunError",
    "TaskRunFailedResultPublicV2",
    "TaskRunFailedResultPublicV2Error",
    "TaskRunFailedResultPublicV2Run",
    "TaskRunFailedResultPublicV2RunError",
]


class TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaimCitation(BaseModel):
    """A citation backing a specific claim in the answer."""

    url: str
    """URL of the cited page."""

    excerpts: Optional[List[str]] = None
    """Verbatim excerpts supporting the claim."""

    extract_template_name: Optional[str] = None
    """Extract template used to read the source, when one was used."""

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
    """How authoritative the source is: 'primary' or 'secondary'."""

    title: Optional[str] = None
    """Title of the cited page."""


class TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaim(BaseModel):
    """Trust metadata for one claim in a prose answer, keyed by callout marker."""

    callout: int
    """Callout marker number referencing this claim in the answer text."""

    citations: List[TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaimCitation]
    """Citations backing this claim."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Confidence in this claim."""

    reasoning: str
    """Why this confidence level was assigned."""


class TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustSource(BaseModel):
    """A source consulted while producing the answer."""

    type: Literal["primary", "secondary"]
    """How authoritative the source is: 'primary' or 'secondary'."""

    url: str
    """URL of the source page."""

    extract_template_name: Optional[str] = None
    """Extract template used to read the source, when one was used."""

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
    """Title of the source page."""


class TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2Trust(BaseModel):
    """Trust and citation metadata for the output."""

    claims: List[TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustClaim]
    """Per-claim trust, keyed by callout markers in the answer text."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Overall confidence in the answer."""

    reasoning: str
    """Why this confidence level was assigned."""

    sources: List[TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2TrustSource]
    """Sources consulted while producing the answer."""


class TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2(BaseModel):
    content: str
    """The final prose answer."""

    trust: TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2Trust
    """Trust and citation metadata for the output."""

    type: Optional[Literal["text"]] = None
    """Output content type."""


class TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaimCitation(BaseModel):
    """A citation backing a specific claim in the answer."""

    url: str
    """URL of the cited page."""

    excerpts: Optional[List[str]] = None
    """Verbatim excerpts supporting the claim."""

    extract_template_name: Optional[str] = None
    """Extract template used to read the source, when one was used."""

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
    """How authoritative the source is: 'primary' or 'secondary'."""

    title: Optional[str] = None
    """Title of the cited page."""


class TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaim(BaseModel):
    """Trust metadata for one value in a structured (JSON) answer, keyed by JSON path."""

    citations: List[TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaimCitation]
    """Citations backing this value."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Confidence in this value."""

    path: str
    """JSON path of the value in the structured output this claim refers to."""

    reasoning: str
    """Why this confidence level was assigned."""


class TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustSource(BaseModel):
    """A source consulted while producing the answer."""

    type: Literal["primary", "secondary"]
    """How authoritative the source is: 'primary' or 'secondary'."""

    url: str
    """URL of the source page."""

    extract_template_name: Optional[str] = None
    """Extract template used to read the source, when one was used."""

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
    """Title of the source page."""


class TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2Trust(BaseModel):
    """Trust and citation metadata for the output."""

    claims: List[TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustClaim]
    """Per-value trust, keyed by JSON path in the structured output."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Overall confidence in the answer."""

    reasoning: str
    """Why this confidence level was assigned."""

    sources: List[TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2TrustSource]
    """Sources consulted while producing the answer."""


class TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2(BaseModel):
    content: Union[Dict[str, object], List[object]]
    """The final structured output."""

    trust: TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2Trust
    """Trust and citation metadata for the output."""

    type: Optional[Literal["json"]] = None
    """Output content type."""


TaskRunResultPublicV2Output: TypeAlias = Union[
    TaskRunResultPublicV2OutputTaskRunTextOutputPublicV2, TaskRunResultPublicV2OutputTaskRunJsonOutputPublicV2
]


class TaskRunResultPublicV2RunError(BaseModel):
    """Error details when the run failed."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunResultPublicV2Run(BaseModel):
    """Task run object with status 'completed'."""

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

    error: Optional[TaskRunResultPublicV2RunError] = None
    """Error details when the run failed."""

    prompt: Optional[str] = None
    """Prompt submitted for the run."""

    started_at: Optional[datetime] = None
    """When the run started executing."""


class TaskRunResultPublicV2(BaseModel):
    output: TaskRunResultPublicV2Output
    """Output from the completed task."""

    run: TaskRunResultPublicV2Run
    """Task run object with status 'completed'."""


class TaskRunFailedResultPublicV2Error(BaseModel):
    """Structured error detail."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultPublicV2RunError(BaseModel):
    """Error details when the run failed."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultPublicV2Run(BaseModel):
    """Task run object with status 'failed'."""

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

    error: Optional[TaskRunFailedResultPublicV2RunError] = None
    """Error details when the run failed."""

    prompt: Optional[str] = None
    """Prompt submitted for the run."""

    started_at: Optional[datetime] = None
    """When the run started executing."""


class TaskRunFailedResultPublicV2(BaseModel):
    error: TaskRunFailedResultPublicV2Error
    """Structured error detail."""

    run: TaskRunFailedResultPublicV2Run
    """Task run object with status 'failed'."""


RunResultResponse: TypeAlias = Union[TaskRunResultPublicV2, TaskRunFailedResultPublicV2]
