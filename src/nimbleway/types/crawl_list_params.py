# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CrawlListParams"]


class CrawlListParams(TypedDict, total=False):
    query_status: Required[
        Annotated[Literal["pending", "in_progress", "completed", "failed", "canceled"], PropertyInfo(alias="status")]
    ]
    """Filter crawls by their status."""

    cursor: Optional[str]
    """Cursor for pagination."""

    limit: int
    """Number of crawls to return per page."""
