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
    "TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1",
    "TaskRunResultPublicV1Run",
    "TaskRunResultPublicV1RunError",
    "TaskRunFailedResultPublicV1",
    "TaskRunFailedResultPublicV1Error",
    "TaskRunFailedResultPublicV1Run",
    "TaskRunFailedResultPublicV1RunError",
]


class TaskRunResultPublicV1OutputTaskRunTextOutputPublicV1(BaseModel):
    content: str
    """The final prose answer."""

    trust: Dict[str, object]
    """Trust and citation metadata for the output."""

    type: Optional[Literal["text"]] = None
    """Output content type."""


class TaskRunResultPublicV1OutputTaskRunJsonOutputPublicV1(BaseModel):
    content: Union[Dict[str, object], List[object]]
    """The final structured output."""

    trust: Dict[str, object]
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

    workspace_id: Optional[str] = None
    """Workspace identifier associated with the run."""


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

    workspace_id: Optional[str] = None
    """Workspace identifier associated with the run."""


class TaskRunFailedResultPublicV1(BaseModel):
    error: TaskRunFailedResultPublicV1Error
    """Structured error detail."""

    run: TaskRunFailedResultPublicV1Run
    """Task run object with status 'failed'."""


RunGetResultResponse: TypeAlias = Union[TaskRunResultPublicV1, TaskRunFailedResultPublicV1]
