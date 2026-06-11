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
    "AgentRunResultOutputAgentRunTextOutputBasi",
    "AgentRunResultOutputAgentRunTextOutputBasiCitation",
    "AgentRunResultOutputAgentRunJsonOutput",
    "AgentRunResultOutputAgentRunJsonOutputBasi",
    "AgentRunResultOutputAgentRunJsonOutputBasiCitation",
    "AgentRunResultRun",
    "AgentRunResultRunError",
    "AgentRunFailedResult",
    "AgentRunFailedResultError",
    "AgentRunFailedResultRun",
    "AgentRunFailedResultRunError",
]


class AgentRunResultOutputAgentRunTextOutputBasiCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    index: Optional[int] = None

    title: Optional[str] = None

    web_search_agent: Optional[str] = None


class AgentRunResultOutputAgentRunTextOutputBasi(BaseModel):
    field: str

    citations: Optional[List[AgentRunResultOutputAgentRunTextOutputBasiCitation]] = None

    confidence: Optional[Literal["high", "medium", "low"]] = None

    reasoning: Optional[str] = None


class AgentRunResultOutputAgentRunTextOutput(BaseModel):
    content: str
    """The final prose answer."""

    basis: Optional[List[AgentRunResultOutputAgentRunTextOutputBasi]] = None

    type: Optional[Literal["text"]] = None


class AgentRunResultOutputAgentRunJsonOutputBasiCitation(BaseModel):
    url: str

    excerpts: Optional[List[str]] = None

    index: Optional[int] = None

    title: Optional[str] = None

    web_search_agent: Optional[str] = None


class AgentRunResultOutputAgentRunJsonOutputBasi(BaseModel):
    field: str

    citations: Optional[List[AgentRunResultOutputAgentRunJsonOutputBasiCitation]] = None

    confidence: Optional[Literal["high", "medium", "low"]] = None

    reasoning: Optional[str] = None


class AgentRunResultOutputAgentRunJsonOutput(BaseModel):
    content: Union[Dict[str, object], List[object]]

    basis: Optional[List[AgentRunResultOutputAgentRunJsonOutputBasi]] = None

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
