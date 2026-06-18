# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactGetResponse"]


class ArtifactGetResponse(BaseModel):
    id: str

    created_at: datetime

    description: str

    type: str
