# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RunGetResultResponse",
    "AgentRunResult",
    "AgentRunResultOutput",
    "AgentRunResultOutputAgentRunTextOutput",
    "AgentRunResultOutputAgentRunTextOutputTrust",
    "AgentRunResultOutputAgentRunTextOutputTrustClaim",
    "AgentRunResultOutputAgentRunTextOutputTrustClaimCitation",
    "AgentRunResultOutputAgentRunTextOutputTrustClaimSource",
    "AgentRunResultOutputAgentRunTextOutputTrustSource",
    "AgentRunResultOutputAgentRunJsonOutput",
    "AgentRunResultOutputAgentRunJsonOutputTrust",
    "AgentRunResultOutputAgentRunJsonOutputTrustClaim",
    "AgentRunResultOutputAgentRunJsonOutputTrustClaimCitation",
    "AgentRunResultOutputAgentRunJsonOutputTrustClaimSource",
    "AgentRunResultOutputAgentRunJsonOutputTrustSource",
    "AgentRunResultRun",
    "AgentRunResultRunError",
    "AgentRunFailedResult",
    "AgentRunFailedResultError",
    "AgentRunFailedResultRun",
    "AgentRunFailedResultRunError",
]


class AgentRunResultOutputAgentRunTextOutputTrustClaimCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunTextOutputTrustClaimSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunTextOutputTrustClaim(BaseModel):
    callout: int

    citations: List[AgentRunResultOutputAgentRunTextOutputTrustClaimCitation]

    confidence: Literal["high", "medium", "low"]

    reasoning: str

    source: Optional[AgentRunResultOutputAgentRunTextOutputTrustClaimSource] = None


class AgentRunResultOutputAgentRunTextOutputTrustSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunTextOutputTrust(BaseModel):
    claims: List[AgentRunResultOutputAgentRunTextOutputTrustClaim]

    confidence: Literal["high", "medium", "low"]

    reasoning: str

    sources: List[AgentRunResultOutputAgentRunTextOutputTrustSource]


class AgentRunResultOutputAgentRunTextOutput(BaseModel):
    content: str
    """The final prose answer."""

    trust: AgentRunResultOutputAgentRunTextOutputTrust

    type: Optional[Literal["text"]] = None


class AgentRunResultOutputAgentRunJsonOutputTrustClaimCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunJsonOutputTrustClaimSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunJsonOutputTrustClaim(BaseModel):
    citations: List[AgentRunResultOutputAgentRunJsonOutputTrustClaimCitation]

    confidence: Literal["high", "medium", "low"]

    path: str

    reasoning: str

    source: Optional[AgentRunResultOutputAgentRunJsonOutputTrustClaimSource] = None


class AgentRunResultOutputAgentRunJsonOutputTrustSource(BaseModel):
    type: Literal["primary", "secondary"]

    url: str

    extract_template_name: Optional[str] = None

    title: Optional[str] = None


class AgentRunResultOutputAgentRunJsonOutputTrust(BaseModel):
    claims: List[AgentRunResultOutputAgentRunJsonOutputTrustClaim]

    confidence: Literal["high", "medium", "low"]

    reasoning: str

    sources: List[AgentRunResultOutputAgentRunJsonOutputTrustSource]


class AgentRunResultOutputAgentRunJsonOutput(BaseModel):
    content: Union[Dict[str, object], List[object]]

    trust: AgentRunResultOutputAgentRunJsonOutputTrust

    type: Optional[Literal["json"]] = None


AgentRunResultOutput: TypeAlias = Union[AgentRunResultOutputAgentRunTextOutput, AgentRunResultOutputAgentRunJsonOutput]


class AgentRunResultRunError(BaseModel):
    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class AgentRunResultRun(BaseModel):
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

    error: Optional[AgentRunResultRunError] = None

    prompt: Optional[str] = None

    started_at: Optional[datetime] = None

    web_search_agent_id: Optional[str] = None
    """Web Search Agent instance this run belongs to."""

    workspace_id: Optional[str] = None


class AgentRunResult(BaseModel):
    output: AgentRunResultOutput

    run: AgentRunResultRun


class AgentRunFailedResultError(BaseModel):
    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class AgentRunFailedResultRunError(BaseModel):
    message: str
    """Human-readable error description."""

    ref_id: str
    """Reference ID (equals the run id)."""


class AgentRunFailedResultRun(BaseModel):
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

    error: Optional[AgentRunFailedResultRunError] = None

    prompt: Optional[str] = None

    started_at: Optional[datetime] = None

    web_search_agent_id: Optional[str] = None
    """Web Search Agent instance this run belongs to."""

    workspace_id: Optional[str] = None


class AgentRunFailedResult(BaseModel):
    error: AgentRunFailedResultError

    run: AgentRunFailedResultRun


RunGetResultResponse: TypeAlias = Union[AgentRunResult, AgentRunFailedResult]
