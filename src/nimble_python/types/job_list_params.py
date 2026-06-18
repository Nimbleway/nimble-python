# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["JobListParams"]


class JobListParams(TypedDict, total=False):
    agent_name: Optional[str]
    """Filter by agent name"""

    page: int

    per_page: int

    q: Optional[str]
    """Search by name or display name"""
