# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentGenerateResponse", "GeneratedVersion", "GeneratedVersionMetadata"]


class GeneratedVersionMetadata(BaseModel):
    data_source: Optional[str] = None

    description: Optional[str] = None

    display_name: Optional[str] = None

    domain: Optional[str] = None

    entity_type: Optional[str] = None

    tags: Optional[List[str]] = None

    vertical: Optional[str] = None


class GeneratedVersion(BaseModel):
    id: str

    agent_name: str

    created_at: datetime

    input_schema: object

    metadata: GeneratedVersionMetadata

    output_schema: object

    steps: List[object]

    version_number: int

    output_sample_data: Optional[object] = None


class AgentGenerateResponse(BaseModel):
    id: str

    status: str

    agent_name: Optional[str] = None

    completed_at: Optional[datetime] = None

    created_at: Optional[datetime] = None

    error: Optional[str] = None

    generated_version: Optional[GeneratedVersion] = None

    generated_version_id: Optional[str] = None

    source_version_id: Optional[str] = None

    started_at: Optional[datetime] = None

    summary: Optional[str] = None
