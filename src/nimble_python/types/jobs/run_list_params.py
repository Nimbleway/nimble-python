# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["RunListParams"]


class RunListParams(TypedDict, total=False):
    page: int

    per_page: int

    status: Optional[str]
    """Filter by status"""
