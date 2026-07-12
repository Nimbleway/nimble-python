# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactGetResponse"]


class ArtifactGetResponse(BaseModel):
    """A file produced by a run.

    Intentional subset of the bakery Artifact: `data_format` and `s3_path` are
    hidden from SDK consumers — internal storage details, not part of the
    public contract. Use the download-url endpoint to fetch the file.
    Bakery emits `id` as an int (crawlit native); the SDK contract is a string.
    """

    id: str
    """Artifact identifier."""

    created_at: datetime
    """When the artifact was created."""

    description: str
    """Human-readable artifact description."""

    type: str
    """Artifact type."""
