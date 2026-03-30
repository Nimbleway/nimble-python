# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["GenerationGetResponse"]


class GenerationGetResponse(BaseModel):
    id: str

    status: str

    agent_name: Optional[str] = None

    completed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    error: Optional[str] = None

    generated_version: Optional[object] = None

    generated_version_id: Optional[str] = None

    source_version_id: Optional[str] = None

    started_at: Optional[datetime] = None

    summary: Optional[str] = None
