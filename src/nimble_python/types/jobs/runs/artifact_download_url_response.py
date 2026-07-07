# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactDownloadURLResponse"]


class ArtifactDownloadURLResponse(BaseModel):
    """A pre-signed URL for downloading an artifact."""

    expires_at: datetime
    """When the download URL expires."""

    url: str
    """Pre-signed URL to download the artifact."""
