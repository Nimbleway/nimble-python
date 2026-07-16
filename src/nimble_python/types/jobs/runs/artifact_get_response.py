# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactGetResponse"]


class ArtifactGetResponse(BaseModel):
    """A file produced by a run."""

    id: str
    """Artifact identifier."""

    created_at: datetime
    """When the artifact was created."""

    description: str
    """Human-readable artifact description."""

    type: str
    """Artifact type."""
