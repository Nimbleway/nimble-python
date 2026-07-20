# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["VersionListResponse", "Item", "ItemMetadata", "ItemSample"]


class ItemMetadata(BaseModel):
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


class ItemSample(BaseModel):
    input: Optional[object] = None
    """Sample input parameters for the version."""

    output: Optional[object] = None
    """Sample output produced by the version."""


class Item(BaseModel):
    id: str
    """Unique extract template version identifier."""

    created_at: datetime
    """When the version was created."""

    input_schema: Dict[str, object]
    """JSON schema describing accepted input parameters."""

    metadata: ItemMetadata
    """Metadata associated with this version."""

    name: str
    """Extract template name this version belongs to."""

    output_schema: Dict[str, object]
    """JSON schema describing extracted output."""

    version_number: int
    """Monotonic version number for the extract template."""

    samples: Optional[List[ItemSample]] = None
    """Sample input and output pairs for the version."""


class VersionListResponse(BaseModel):
    items: List[Item]
    """Items returned in this page."""

    limit: int
    """Maximum number of items returned."""

    offset: int
    """Number of items skipped before this page."""

    total: int
    """Total number of items matching the query."""
