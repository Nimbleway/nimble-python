# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CrawlListParams"]


class CrawlListParams(TypedDict, total=False):
    status: Required[Literal["queued", "running", "succeeded", "failed", "canceled"]]
    """Filter crawls by their status."""

    cursor: Optional[str]
    """Cursor for pagination."""

    limit: int
    """Number of crawls to return per page."""
