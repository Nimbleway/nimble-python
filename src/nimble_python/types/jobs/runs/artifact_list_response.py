# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactListResponse", "Item"]


class Item(BaseModel):
    """A file produced by a run."""

    id: str
    """Artifact identifier."""

    created_at: datetime
    """When the artifact was created."""

    description: str
    """Human-readable artifact description."""

    type: str
    """Artifact type."""


class ArtifactListResponse(BaseModel):
    """Artifacts produced by a run."""

    items: List[Item]
    """Artifacts produced by the run."""
