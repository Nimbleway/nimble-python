# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RunGetResultResponse",
    "TaskRunResultPublicV1",
    "TaskRunResultPublicV1Output",
    "TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1",
    "TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1Trust",
    "TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaim",
    "TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaimCitation",
    "TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustSource",
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1",
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1Trust",
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaim",
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaimCitation",
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustSource",
    "TaskRunResultPublicV1Run",
    "TaskRunResultPublicV1RunError",
    "TaskRunFailedResultPublicV1",
    "TaskRunFailedResultPublicV1Error",
    "TaskRunFailedResultPublicV1Run",
    "TaskRunFailedResultPublicV1RunError",
]


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaimCitation(BaseModel):
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


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaim(BaseModel):
    """Trust metadata for one claim in a prose answer, keyed by callout marker."""

    callout: int
    """Callout marker number referencing this claim in the answer text."""

    citations: List[TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaimCitation]
    """Citations backing this claim."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Confidence in this claim."""

    reasoning: str
    """Why this confidence level was assigned."""


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustSource(BaseModel):
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


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1Trust(BaseModel):
    """Trust and citation metadata for the output."""

    claims: List[TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustClaim]
    """Per-claim trust, keyed by callout markers in the answer text."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Overall confidence in the answer."""

    reasoning: str
    """Why this confidence level was assigned."""

    sources: List[TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1TrustSource]
    """Sources consulted while producing the answer."""


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1(BaseModel):
    content: str
    """The final prose answer."""

    trust: TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1Trust
    """Trust and citation metadata for the output."""

    type: Optional[Literal["text"]] = None
    """Output content type."""


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaimCitation(BaseModel):
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


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaim(BaseModel):
    """Trust metadata for one value in a structured (JSON) answer, keyed by JSON path."""

    citations: List[TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaimCitation]
    """Citations backing this value."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Confidence in this value."""

    path: str
    """JSON path of the value in the structured output this claim refers to."""

    reasoning: str
    """Why this confidence level was assigned."""


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustSource(BaseModel):
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


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1Trust(BaseModel):
    """Trust and citation metadata for the output."""

    claims: List[TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustClaim]
    """Per-value trust, keyed by JSON path in the structured output."""

    confidence: Literal["high", "medium", "low", "pre_existing"]
    """Overall confidence in the answer."""

    reasoning: str
    """Why this confidence level was assigned."""

    sources: List[TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1TrustSource]
    """Sources consulted while producing the answer."""


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1(BaseModel):
    content: Union[Dict[str, object], List[object]]
    """The final structured output."""

    trust: TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1Trust
    """Trust and citation metadata for the output."""

    type: Optional[Literal["json"]] = None
    """Output content type."""


TaskRunResultPublicV1Output: TypeAlias = Union[
    TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1, TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1
]


class TaskRunResultPublicV1RunError(BaseModel):
    """Error details when the run failed."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunResultPublicV1Run(BaseModel):
    """Task run object with status 'completed'."""

    id: str
    """Run identifier, format "task*run*{uuid}"."""

    created_at: datetime
    """When the run was created."""

    effort: Literal["low", "medium", "high", "x-high", "max"]
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

    error: Optional[TaskRunResultPublicV1RunError] = None
    """Error details when the run failed."""

    prompt: Optional[str] = None
    """Prompt submitted for the run."""

    started_at: Optional[datetime] = None
    """When the run started executing."""


class TaskRunResultPublicV1(BaseModel):
    output: TaskRunResultPublicV1Output
    """Output from the completed task."""

    run: TaskRunResultPublicV1Run
    """Task run object with status 'completed'."""


class TaskRunFailedResultPublicV1Error(BaseModel):
    """Structured error detail."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultPublicV1RunError(BaseModel):
    """Error details when the run failed."""

    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class TaskRunFailedResultPublicV1Run(BaseModel):
    """Task run object with status 'failed'."""

    id: str
    """Run identifier, format "task*run*{uuid}"."""

    created_at: datetime
    """When the run was created."""

    effort: Literal["low", "medium", "high", "x-high", "max"]
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

    error: Optional[TaskRunFailedResultPublicV1RunError] = None
    """Error details when the run failed."""

    prompt: Optional[str] = None
    """Prompt submitted for the run."""

    started_at: Optional[datetime] = None
    """When the run started executing."""


class TaskRunFailedResultPublicV1(BaseModel):
    error: TaskRunFailedResultPublicV1Error
    """Structured error detail."""

    run: TaskRunFailedResultPublicV1Run
    """Task run object with status 'failed'."""


RunGetResultResponse: TypeAlias = Union[TaskRunResultPublicV1, TaskRunFailedResultPublicV1]
