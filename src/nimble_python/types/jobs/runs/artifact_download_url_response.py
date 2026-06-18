# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactDownloadURLResponse"]


class ArtifactDownloadURLResponse(BaseModel):
    expires_at: datetime

    url: str
