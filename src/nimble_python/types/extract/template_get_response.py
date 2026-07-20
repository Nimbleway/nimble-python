# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TemplateGetResponse", "PublishedVersion", "PublishedVersionMetadata", "PublishedVersionSample"]


class PublishedVersionMetadata(BaseModel):
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


class PublishedVersionSample(BaseModel):
    input: Optional[object] = None
    """Sample input parameters for the version."""

    output: Optional[object] = None
    """Sample output produced by the version."""


class PublishedVersion(BaseModel):
    """Published version details, when available."""

    id: str
    """Unique extract template version identifier."""

    created_at: datetime
    """When the version was created."""

    input_schema: Dict[str, object]
    """JSON schema describing accepted input parameters."""

    metadata: PublishedVersionMetadata
    """Metadata associated with this version."""

    name: str
    """Extract template name this version belongs to."""

    output_schema: Dict[str, object]
    """JSON schema describing extracted output."""

    version_number: int
    """Monotonic version number for the extract template."""

    samples: Optional[List[PublishedVersionSample]] = None
    """Sample input and output pairs for the version."""


class TemplateGetResponse(BaseModel):
    id: str
    """Unique extract template identifier."""

    created_at: datetime
    """When the extract template was created."""

    name: str
    """Stable extract template name."""

    updated_at: datetime
    """When the extract template was last updated."""

    published_version: Optional[PublishedVersion] = None
    """Published version details, when available."""

    published_version_id: Optional[str] = None
    """Identifier of the published version."""
