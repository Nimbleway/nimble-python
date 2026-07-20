# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["GenerationGetResponse", "GeneratedVersion", "GeneratedVersionMetadata", "GeneratedVersionSample"]


class GeneratedVersionMetadata(BaseModel):
    """Metadata associated with this version."""

    data_source: Optional[str] = None
    """Data source associated with the version."""

    description: Optional[str] = None
    """Version description shown to users."""

    display_name: Optional[str] = None
    """Human-friendly version display name."""

    domain: Optional[str] = None
    """Domain associated with the version."""

    entity_type: Optional[str] = None
    """Entity type produced by the version."""

    tags: Optional[List[str]] = None
    """Tags associated with the version."""

    vertical: Optional[str] = None
    """Business vertical associated with the version."""


class GeneratedVersionSample(BaseModel):
    input: Optional[object] = None
    """Sample input parameters for the version."""

    output: Optional[object] = None
    """Sample output produced by the version."""


class GeneratedVersion(BaseModel):
    """Generated version details, when available."""

    id: str
    """Unique extract template version identifier."""

    created_at: datetime
    """When the version was created."""

    input_schema: Dict[str, object]
    """JSON schema describing accepted input parameters."""

    metadata: GeneratedVersionMetadata
    """Metadata associated with this version."""

    name: str
    """Extract template name this version belongs to."""

    output_schema: Dict[str, object]
    """JSON schema describing extracted output."""

    version_number: int
    """Monotonic version number for the extract template."""

    samples: Optional[List[GeneratedVersionSample]] = None
    """Sample input and output pairs for the version."""


class GenerationGetResponse(BaseModel):
    id: str
    """Unique extract template generation identifier."""

    status: str
    """Current generation status."""

    completed_at: Optional[datetime] = None
    """When the generation completed."""

    created_at: Optional[datetime] = None
    """When the generation was created."""

    error: Optional[str] = None
    """Error message when generation failed."""

    generated_version: Optional[GeneratedVersion] = None
    """Generated version details, when available."""

    generated_version_id: Optional[str] = None
    """Identifier of the generated version."""

    name: Optional[str] = None
    """Extract template name associated with the generation."""

    source_version_id: Optional[str] = None
    """Identifier of the version being refined."""

    started_at: Optional[datetime] = None
    """When the generation started executing."""

    summary: Optional[str] = None
    """Summary of the generation result."""
