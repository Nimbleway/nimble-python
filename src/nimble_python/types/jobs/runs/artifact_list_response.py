# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ...._models import BaseModel

__all__ = ["ArtifactListResponse", "Item"]


class Item(BaseModel):
    id: str

    created_at: datetime

    description: str

    type: str


class ArtifactListResponse(BaseModel):
    items: List[Item]
