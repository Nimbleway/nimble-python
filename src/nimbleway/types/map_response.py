# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MapResponse", "Link"]


class Link(BaseModel):
    url: str

    description: Optional[str] = None

    title: Optional[str] = None


class MapResponse(BaseModel):
    """Response schema for map requests."""

    links: List[Link]
    """Array of mapped links with optional titles and descriptions."""

    success: bool
    """Indicates if the map request was successful."""

    task_id: str
    """Unique identifier for the map task."""
